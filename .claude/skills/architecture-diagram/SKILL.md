---
name: architecture-diagram
description: Draw architecture, data flow, network, and deployment diagrams as draw.io files, with an HTML preview. Works for any cloud provider, on-premises systems, or generic software components. Use when the user says "draw a diagram", "architecture diagram", "data flow diagram", "diagram this", or asks to visualize a system from a description or notes.
---

# Architecture Diagram

Produce a `.drawio` file the user can edit in draw.io (diagrams.net) and an `.html` file that previews it in a browser.

## 1. Understand the system

The description can come from the conversation, an account or project note in `Notes/`, or research results. Before drawing, list:

- Every component and what it does.
- The direction of data or requests between components, and the protocol or event for each.
- Boundaries: cloud accounts, regions, networks, subnets, data centers, trust zones.
- External actors: users, client apps, partners, SaaS services, third-party APIs.
- The diagram type: overview, data flow, network, or deployment.

Ask about anything that changes the picture. Do not add components the description does not include.

## 2. Pick the shapes

draw.io has shape libraries for the major providers. Use the provider's library when the system runs on that provider, and generic shapes for everything else.

| Provider | Style prefix | Shape list |
|---|---|---|
| AWS | `mxgraph.aws4.*` | `Sidebar-AWS4.js` |
| Azure | `mxgraph.azure.*` and image icons | `Sidebar-Azure.js` |
| Google Cloud | `mxgraph.gcp2.*` | `Sidebar-GCP2.js` |
| Kubernetes | `mxgraph.kubernetes.*` | `Sidebar-Kubernetes.js` |
| Generic | `shape=cylinder3` (database), `shape=mxgraph.basic.*`, `shape=umlActor`, rounded rectangles | `Sidebar-Basic.js` |

The sidebar files are in `src/main/webapp/js/diagramly/sidebar/` of https://github.com/jgraph/drawio. Look up each shape name there before you use it. A wrong name renders as an empty box, so never guess one.

## 3. Write the XML

```xml
<mxfile>
  <diagram name="Architecture" id="arch-1">
    <mxGraphModel grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1600" pageHeight="900" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- boundary groups (cloud, region, network) as containers -->
        <!-- components, with parent set to their container -->
        <!-- edges with source, target, and a label -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Layout rules:

- Flow left to right or top to bottom.
- Put components inside the boundary they run in. Provider services go inside that provider's cloud group; network-bound services go inside the network group.
- Keep at least 40px between shapes. Align shapes on the grid. Nothing overlaps.
- Group related parts (entry, compute, data, integration) in columns or rows.
- Every edge has a `source` and a `target` and a short label ("HTTPS", "events", "nightly batch"). Use orthogonal edges (`edgeStyle=orthogonalEdgeStyle`) and route them around shapes.
- Label every shape with its name and, if useful, its role.
- Colors: the provider's default icon colors; light fills for network boundaries; dashed red or orange lines for security or trust boundaries.
- Leave out comments and extra whitespace in the saved file.

For a large diagram, write the XML in parts and join them into one file before saving. Never save a partial file.

## 4. Save and preview

Save next to the related note, for example `Notes/Accounts/<Name>/<Project>/Architecture.drawio`, or under `Notes/Projects/<Project>/`. A finished diagram for someone else goes in `Outbox/`.

Then build the preview with the bundled script, which escapes the XML for you:

```bash
python3 .claude/skills/architecture-diagram/scripts/drawio_to_html.py "<path>/Architecture.drawio"
```

It writes `Architecture.html` next to the `.drawio` file. Opening it loads the draw.io viewer from `viewer.diagrams.net`, so the preview needs internet access.

## 5. Check it

- Parse the file: `python3 -c 'import sys, xml.etree.ElementTree as ET; ET.parse(sys.argv[1])' "<file>.drawio"`.
- Every edge's `source` and `target` match an existing cell `id`.
- Every component from step 1 is in the diagram, and nothing else is.
- Open the HTML preview and look at it. Fix overlaps and crossing edges.

Tell the user where both files are, and that the `.drawio` file opens in draw.io desktop or at https://app.diagrams.net for editing.
