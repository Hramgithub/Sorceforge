# Render Candidate Manifest - RT-G1-VIRAL-RENDER-001

Manifest id: `RCM-G1-VIRAL-RENDER-001`

Status: `frozen`

Frozen at: 2026-07-17T17:40:00Z

Selected-page predecessor: `SPM-G1-VIRAL-001`

Accepted protocol:

- Revision: `5ee1760f9e9106d7cb0429a76cdc2d9d5758b03a`
- File blob: `4d494e83d8d63dd3778a3813b3ee529449cee51a`

Render candidate:

| Field | Value |
|---|---|
| `render_candidate_id` | `RC-G1-VIRAL-PYMUPDF-300DPI-RGB-PNG-001` |
| `renderer_engine` | PyMuPDF |
| `renderer_module` | `fitz` |
| `renderer_version` | `1.27.2.3` |
| `renderer_source` | local Python environment |
| `python_executable` | `D:\NRI\.tools\python-3.13.14\python.exe` |
| `page_box` | PyMuPDF default page rectangle |
| `resolution_dpi` | 300 |
| `color_space` | RGB |
| `bit_depth` | 8-bit per channel PNG output |
| `image_container` | PNG |
| `compression_policy` | PyMuPDF PNG writer default; no lossy post-processing |
| `alpha_transparency` | disabled (`alpha=False`) |
| `rotation_orientation` | honor PDF page rotation as rendered by PyMuPDF |
| `anti_aliasing` | PyMuPDF default rasterization at 300 DPI |
| `preprocessing_policy` | none |

Permitted output:

- One PNG page image per selected ordinal page 1-20.
- One output manifest binding every image to this candidate, `SPM-G1-VIRAL-001`,
  the accepted protocol revision/blob, and `BA-G1-VIRAL-RENDER-001`.

Invalidation:

- Stale if source path/hash, `SPM-G1-VIRAL-001`, accepted protocol
  revision/blob, renderer engine/version/source, Python executable, DPI, color
  space, PNG writer behavior, alpha policy, page box handling, rotation policy,
  preprocessing policy, or comparison plan changes.
