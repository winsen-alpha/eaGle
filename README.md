# <Repository Name>

Anomaly detection and attack scenario reconstruction on system provenance graphs.

The pipeline trains an anomaly detection model on a provenance graph, scores the nodes of a target graph, and then reconstructs the attack scenario by combining rule matching with anomaly subtree detection.

---

## Table of Contents

- [Repository Structure](#repository-structure)
- [Data Format](#data-format)
- [Rule Format](#rule-format)
- [Usage](#usage)
- [Pipeline Overview](#pipeline-overview)
- [Input Files](#input-files)
- [Output Files](#output-files)
- [Contact](#contact)

---

## Repository Structure

| File | Description |
| --- | --- |
| `setup.py` | Initialization script |
| `train.py` | Training script for the anomaly detection component |
| `test.py` | Detection script for the anomaly detection component |
| `data_process_train.py` | Data processing script for the training stage |
| `data_process_test.py` | Data processing script for the detection stage |
| `fine_ruleMatch.py` | Fine-grained rule matching script |
| `subtree.py` | Anomaly subtree detection algorithm |
| `coarse_ruleMatch.py` | Coarse-grained rule matching script |

---

## Data Format

The training data and the test data are named `train.txt` and `test.txt` respectively.

Each line in these files represents **one edge** in the source graph. Fields are separated by a **tab** character.

| # | Field |
| --- | --- |
| 1 | Source node name |
| 2 | Source node type |
| 3 | Destination node name |
| 4 | Destination node type |
| 5 | Edge type |
| 6 | Timestamp |

Example line layout:

```
src_node_name	src_node_type	dst_node_name	dst_node_type	edge_type	timestamp
```

---

## Rule Format

The fine-grained rule set and the coarse-grained rule set are defined in `fine_rules.txt` and `coarse_rules.txt` respectively.

Each line represents one rule. Fields are separated by a **space**:

| # | Field |
| --- | --- |
| 1 | Node name |
| 2 | Anomaly description |

Example line layout:

```
node_name anomaly_description
```

---

## Usage

A complete training + detection run consists of the following steps:

1. **Initialize**

   ```bash
   python setup.py
   ```

2. **Train the anomaly detection model**

   ```bash
   python train.py
   ```

3. **Run detection on the source graph data**

   ```bash
   python test.py
   ```

   Node anomaly scores are written to `anomaly_score.txt`.

4. **Perform fine-grained and coarse-grained rule matching on the source graph data**

   ```bash
   python fine_ruleMatch.py
   ```

   Matching results are written to `fine_rules_id.txt` and `coarse_rules_id.txt`. The fine-grained and coarse-grained rule sets are defined in `fine_rules.txt` and `coarse_rules.txt` — see [Rule Format](#rule-format).

5. **Perform anomaly subtree detection**

   ```bash
   python subtree.py
   ```

   Takes the graph topology and the node anomaly scores as input, and outputs the topology of the anomaly subtrees.

6. **Match attack steps on the detected anomaly subtrees**

   ```bash
   python coarse_ruleMatch.py
   ```

   The matched result — that is, the reconstructed attack scenario — is written to `ans.txt`.

---

## Pipeline Overview

```
setup.py
   │
   ▼
train.py  ──►  data_process_train.py  ──►  anomaly detection model
                                                   │
                                                   ▼
test.py  ──►  data_process_test.py  ──►  anomaly_score.txt
                                                   │
                                                   ▼
fine_ruleMatch.py  ──►  fine_rules_id.txt
                       coarse_rules_id.txt
                                                   │
                                                   ▼
subtree.py  ──►  anomaly subtree topology
                                                   │
                                                   ▼
coarse_ruleMatch.py  ──►  ans.txt  (reconstructed attack scenario)
```

---

## Input Files

| File | Consumed by | Content |
| --- | --- | --- |
| `train.txt` | `train.py` | Training graph edges |
| `test.txt` | `test.py` | Test graph edges |
| `fine_rules.txt` | `fine_ruleMatch.py` | Fine-grained rule set |
| `coarse_rules.txt` | `fine_ruleMatch.py` | Coarse-grained rule set |

---

## Output Files

| File | Produced by | Content |
| --- | --- | --- |
| `anomaly_score.txt` | `test.py` | Anomaly score for each node |
| `fine_rules_id.txt` | `fine_ruleMatch.py` | Fine-grained rule matching results |
| `coarse_rules_id.txt` | `fine_ruleMatch.py` | Coarse-grained rule matching results |
| `ans.txt` | `coarse_ruleMatch.py` | Reconstructed attack scenario |

---

## Contact

For questions or discussion, please contact [wangsu@zgclab.edu.cn](mailto:wangsu@zgclab.edu.cn).
