# 📦 其他研究 | 2026年07月28日

> 本类共 **169** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-169](./part-04.md)

---

### 51. [Data eccentricity, asymptotics of Gaussian RBF reproducing kernel Hilbert space, and kernel PCA](https://arxiv.org/abs/2607.21823)

**<font color=#1a73e8>作者：</font>** Sergio A. Alvarez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that, up to isotropic scaling, the Gaussian RBF reproducing kernel Hilbert space (RKHS) is asymptotically isometric to Euclidean space in the large bandwidth limit. This strongly suggests that kernel-based constructions reliant on metric properties of the RKHS will yield results for Gaussian RBF kernels that similarly approach those of linear kernels for large bandwidths. The asymptotic behavior of Gaussian CKA can be understood in this light. We further consider kernel PCA, showing that Gaussian RBF eigenvalues, eigenprojections, and principal components all converge to those of classical (linear) PCA as bandwidth $\sigma \rightarrow \infty$. For a given data representation, both the RKHS feature embeddings and the orthogonal PCA eigenframes of the two kernel types differ asymptotically by a geometric similarity transformation, up to a residual of size $O \left (\frac{\rho}{\sigma} \right )^2$, where $\rho$ is a measure of geometric eccentricity of the representation, equal to the ratio of maximum to median pairwise distance between data examples. Experiments over a diverse collection of data sets demonstrate that $\rho$ provides a simple and reliable predictor of dataset-specific convergence behavior in the top principal directions.

---


### 52. [A Graph-Based Control Interface for Traffic Signals on Heterogeneous Road Networks](https://arxiv.org/abs/2607.21831)

**<font color=#1a73e8>作者：</font>** Bertil Braun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a traffic-signal control interface in which a shared graph neural network assigns scores to individual traffic movements. Each junction converts these scores into its own variable-sized set of legal signal phases using a deterministic incidence matrix. Directed corridor nodes provide traffic context, while movement nodes represent controlled input-to-output paths through junctions. Typed mean aggregation produces one scalar per movement; phase definitions and signal timing remain outside the learned network. This makes graph size and junction-specific action count independent of the learned parameter shapes. PPO experiments evaluate the interface on unseen synthetic grid geometries, altered signal coverage, and five heterogeneous city graphs. The policies retained performance across unseen geometries within the synthetic grid family, while changes in signal coverage exposed sensitivity to a signal-coverage distribution shift. A single trained city-policy instance executed across all five city graphs, with heterogeneous outcomes. These results provide feasibility evidence rather than a general estimate of transfer to arbitrary road networks.

---


### 53. [ToolGuardian: Declarative Security for AI Agent-Tool Interactions](https://arxiv.org/abs/2607.21835)

**<font color=#1a73e8>作者：</font>** Arun Ravindran, Saurabh Deochake  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on external tools, expanding capability while creating a new security boundary: third-party tools may appear benign at the interface level while embedding unsafe behavior in implementation. Existing defenses rely on weak metadata, collapse characterization and policy judgment into a single decision, or use heuristic/LLM enforcement that lacks deterministic, auditable reasoning over task context and multi-tool composition.
This paper presents ToolGuardian, a policy-driven framework for securing agent-tool interactions through pre-admission vetting and task-aware runtime authorization. ToolGuardian uses progressive characterization to convert evidence into structured facts: descriptions capture declared intent, system-call traces expose coarse behavior, mock execution reveals observed effects, and source analysis identifies latent behavior. ToolGuardian's core contribution is an Answer Set Programming (ASP)-based declarative policy layer that reasons explicitly over capabilities, effects, task context, and composition. We compare ASP against heuristic and LLM-based policy realizations using identical inputs and output contracts.
We evaluate ToolGuardian on 16 MCP-style tools, including 8 malicious variants derived from real open-source tools, and 20 runtime scenarios. For vetting, ASP reaches a deny-class F1 of 0.86 and 88% accuracy using description, syscall, and observed-effect evidence. For runtime authorization, fully specified realizations classify all scenarios correctly, while ablations show that removing compositional and conformance rules substantially degrades performance.

---


### 54. [Certified in Theory, Broken in Practice: Assumption Gaps in Cryptographic Model Certification](https://arxiv.org/abs/2607.21839)

**<font color=#1a73e8>作者：</font>** Carter Luck, Olive Franzese-McLaughlin, Elisaweta Masserova 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving machine learning auditing protocols allow auditors to assess models for properties such as accuracy or fairness, without revealing their internals or training data. This makes them especially attractive for auditing models deployed in sensitive domains such as healthcare or finance. For these protocols to be meaningful in real-world audit settings, though, their guarantees must reflect how the model will behave once deployed, rather than merely certifying its behavior during an audit. Existing security definitions often miss this mark: most certify model behavior only on a fixed audit dataset, without ensuring that the same guarantees generalize to other datasets drawn from the same distribution.
As we show, this gap allows a model provider to attack many cryptographic model certification (CMC) schemes built on secure zero knowledge proofs (ZKP) by carefully engineering training data, resulting in models that exhibit benign behavior during an audit, but pathological behavior in practice. For example, we empirically demonstrate that an attacker can certify that a model achieves over 99% accuracy on an audit dataset, but less than 30% accuracy on fresh samples from the same distribution.
To address this gap, we formalize rigorous cryptographic security notions tailored to CMC frameworks, introduce a generic protocol template, and prove that it satisfies these requirements. Our results thus offer both cautionary evidence about existing approaches and constructive guidance for designing secure, privacy-preserving ML auditing protocols.

---


### 55. [Toward High-Fidelity 3D Point-Cloud Learning for Brain Folding Morphology Prediction Using Trans-Unet](https://arxiv.org/abs/2607.21840)

**<font color=#1a73e8>作者：</font>** Geran Zhao, Xiaotian Li, Poorya Chavoshnejad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning high-fidelity point-cloud features in the 3D space poses significant challenges, including permutation invariance, lack of local context, difficulty in fine-grained surface reconstruction, and high computational cost. In this article, we propose Trans-Unet, a novel framework that addresses these issues by first tansforming 3D point-cloud data into a 2D grid domain and then employing a U-shaped hybrid model that integrates Convolutional Neural Networks, and self-attention mechanisms. The proposed Trans-Unet effectively learns and reconstructs precise features from high-resolution 3D point-cloud data (with 40,401 points in surface and 2,382 points in fiber) derived from a predefined finite element brain patch growth model, enabling accurate prediction of brain folding patterns. By combining multiple techniques, Trans-Unet leverages the complementary strengths: the 3D-to-2D transformation preserves fine-grained structural information while significantly reducing computational cost and the curse of dimensionality; convolutional blocks capture hierarchical, low-level local representations; and the self-attention mechanism models global, high-level semantics and long-range dependencies. The dataset consists of 3D point-clouds containing both brain surface patches and fiber information generated by a large-scale finite element model. Trans-Unet is applied to predict brain surface folding from the initial state (state 0 or states 0-2) to the final state (state 3). Experimental results demonstrate that Trans-Unet achieves high-resolution predictions of brain patch growth, surpassing existing methods in both fidelity and accuracy.

---


### 56. [Closing the Loop: Training-Free Revisit Consistency for Autoregressive Generative Rendering](https://arxiv.org/abs/2607.21848)

**<font color=#1a73e8>作者：</font>** Wenchao Ma, Changran Liu, Sharon X. Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent conditional video generation models have shown promising potentials to transform 3D engine renderings, such as depth maps and untextured geometry, into photorealistic videos for gaming and immersive content creation. These applications require long-horizon auto-regressive generation that continuously synthesizes new frames while preserving a persistent 3D world. Auto-regressive generators synthesize video chunk by chunk with a bounded KV cache, so when the camera revisits a location after its context has been evicted, the model often regenerates inconsistent appearance, even though the conditioning renderings (e.g., depth) remain perfectly aligned with the underlying this http URL address this revisit inconsistency without any post-training by exploiting correspondences the 3D engine already provides: temporal correspondence retrieves pose-matched historical latent chunks into the KV cache as loop-closure memory, while spatial correspondence from camera pose and depth reprojection biases token-level attention toward geometrically corresponding regions of the retrieved chunks. We demonstrate our method on loop-closure trajectories mined from TartanAir and TartanGround dataset to mirror complicate real-world application scenarios, where it outperforms existing training-free baselines on revisit consistency without losing overall video quality. Project Page: this https URL

---


### 57. [SCALE: Self-Supervised Constraint-Aware Layout GEneration for Local P&R DRV Fixing at Advanced Nodes](https://arxiv.org/abs/2607.21850)

**<font color=#1a73e8>作者：</font>** Chia-Tung Ho, Haoyu Yang, Guanglei Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As semiconductor manufacturing advances toward sub-2nm nodes, local place-and-route (P&R) design-rule violation (DRV) fixing is increasingly limited by complex rule interactions, dense multi-layer routing geometries, and foundry-specific constraints. While Large Language Models (LLMs) have recently demonstrated strong capabilities in EDA scripting and documentation, their application to visual layout understanding remains largely unexplored: diagnosing DRC violations from layout imagery demands precise geometric reasoning and foundry-specific rule knowledge absent from general-purpose VLM training. We propose SCALE, a framework with a self-supervised layout-generation stage for local DRV fixing at advanced nodes. Multi-layer layout geometry is serialized into structured text, and a fine-tuned language model learns to reconstruct randomly masked polygons from surrounding BEOL context alone without violation labels. At inference, natural-language rule constraints and high-temperature sampling steer generation toward diverse, violation-prone layout variants validated by an industrial signoff DRC checker, producing DRC-annotated layout--violation pairs used to fine-tune a domain-adapted DRC-VLM. This VLM provides rule-aware geometric guidance for local DRV repair, boosting state-of-the-art agents' solve rates by +12--25% (up to 97%) on 100 real sub-2nm cases spanning enclosure, spacing, width, and color-spacing violations.

---


### 58. [Filtering Offensive Content Changes Its Visibility but Not User Behavior: Two Randomized Controlled Trials with 200,000 Users on Nextdoor](https://arxiv.org/abs/2607.21853)

**<font color=#1a73e8>作者：</font>** David J. Grüning, Matthew Katsaros  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We investigate the effectiveness of interventions that reduce the visibility of offensive content on the local social platform Nextdoor. Content filtering -- hiding or downranking offensive content that brushes against a platform's rules without clearly breaking them -- is deployed across virtually every major platform, yet almost no field evidence exists on whether it changes user behavior. We report two large-scale randomized controlled trials, each involving 100,000 users. Study 1 (2022) tested a report-triggered filter applied to comments in post threads and produced a modest 12% reduction in views of offensive comments; across eleven further measures of platform behavior we found no significant effects. Study 2 (2023-2024) remedied Study 1's central limitation -- a weak manipulation driven by slow, report-based eligibility -- by proactively scoring posts and comments at creation with Google Jigsaw's Perspective API and filtering them from the newsfeed. This produced a near-complete (95%) reduction in views of offensive posts, yet across thirteen further measures we again found no significant effects. Across two independent trials spanning different content types, filtering mechanisms, classifiers, and countries -- and despite manipulation strength rising from 12% to 95% -- filtering reliably reduced the visibility of offensive content without altering platform visitation, content consumption, or content production. These convergent null results provide rare field evidence on a ubiquitous intervention and underscore the complexity of effectively moderating online platforms.

---


### 59. [Searching the Space of Feed-Forward Neural-Network Weight-Update Rules with Fixed Depth Symbolic Regression](https://arxiv.org/abs/2607.21855)

**<font color=#1a73e8>作者：</font>** Charles Brum, Edward Finkelstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate whether symbolic regression can discover explicit neural network weight-update rules that outperform standard hand-designed optimizers on small symbolic regression benchmarks. Candidate update rules are represented as fixed-depth symbolic expressions over operands derived from common optimizers, including gradient, momentum, adaptive-gradient, and moment-estimate quantities. Across 30 benchmark/neural network combinations, the symbolic regression procedure found an update rule outperforming the best hyperparameter-tuned established optimizer in 25 cases, with an aggregate MSE reduction of 44.47\% over the improved cases. The discovered rules do not all share a single common symbolic form, but many combine adaptive normalization, momentum-like quantities, nonlinear transformations, and rational expressions. These results suggest that symbolic regression can serve as a lightweight mechanism for discovering compact optimizer variants, while also highlighting the need for larger-scale validation.

---


### 60. [LeAct: Learning to Reason from Expert Actions](https://arxiv.org/abs/2607.21856)

**<font color=#1a73e8>作者：</font>** Ziran Yang, Chengshuai Shi, Raj Ghugare 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern reasoning models depend on reasoning data, today sourced from human annotations or distilled from stronger LLMs. However, a rich and largely untapped source of supervision lies in expert systems (e.g., game engines, classical planners, theorem provers), which routinely produce near-optimal actions across diverse domains. But these experts are silent: they commit to an action without writing down the chain of thought (CoT) behind it. Recovering that CoT as natural-language reasoning would distill expert knowledge into a student that generalizes beyond the demonstrated actions. We treat it as a latent variable and study how to recover it from the action alone. Our approach, LeAct (Learning to reason from Actions), optimizes this latent variable: the student samples candidate CoTs for each expert action, and we retain those that measurably improve its own probability of recovering the action. Across imperfect-information games at multiple scales and a simulated robotics benchmark, LeAct reaches the solver's numerical floor on small enumerable games. At larger scale, it is $5\times$ closer to the solver than the strongest expert-iteration baseline. At Flop Hold'em ($\sim 10^9$ infosets), LeAct wins head-to-head by $+60$ mbb/g, and on the robotics probe it is the only training recipe that improves on direct imitation. We present a principled framework and the result: expert systems become a categorically new source of reasoning teachers for foundation models.

---


### 61. [DAGForge: Auditable Causal DAG Authoring with Biomedical Literature](https://arxiv.org/abs/2607.21859)

**<font color=#1a73e8>作者：</font>** Yi-han Sheu, Michael R. Steigman, Yu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constructing causal directed acyclic graphs (DAGs) is a core step in biomedical causal analysis, yet it remains a largely manual process. Analysts must connect study variables to prior literature, evaluate uncertain causal claims, and preserve sufficient provenance for expert review. We present DAGForge, a browser-based system for authoring causal DAGs as auditable, evidence-linked artifacts. Given free-text descriptions of study concepts, DAGForge creates a reproducible literature snapshot, uses an LLM-based reasoning module to generate structured pairwise causal judgments grounded in verbatim evidence excerpts, and assembles those judgments into a constraint-checked graph. Each proposed edge includes confidence estimates, provenance, and a reviewable rationale. The interface supports study specification, progress monitoring, evidence review, graph comparison, adjustment-set computation, and export. In evaluations against both compact benchmark DAGs and reference DAGs derived from published literature, DAGForge achieves high edge recall on the literature-based cohort while retaining verifiable evidence trails absent from LLM-only baselines. DAGForge thus reduces the burden of causal DAG curation while making the resulting assumptions auditable, supporting the design, analysis, and interpretation of biomedical studies.

---


### 62. [Data Quality over Capacity: Internalizing Documents into LoRA Adapters for Closed-Book QA](https://arxiv.org/abs/2607.21861)

**<font color=#1a73e8>作者：</font>** Joan Figuerola Hurtado  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study baking documents directly into the weights of a 4-bit Gemma-4-e4b model via LoRA, so a system can answer questions about a corpus closed-book: no retrieval and no context-window budget. Across roughly 100 training runs from single documents to a 99-document corpus, we find that once adapter capacity is adequate, training-data quality is the dominant lever on closed-book accuracy, outweighing LoRA rank, learning rate, and two alternative architectures combined; capacity itself is a hard gate below which no data intervention helps. A single curation pass (shortening gold answers to canonical 1-6 word spans and dropping trivia) moved closed-book accuracy from 57.7% to 85.7% on a 15-document corpus, a larger jump than any architectural change. We confirm a capacity trend (rank must grow with corpus size) entangled with a coupling between rank and learning rate that we initially misdiagnosed. On a 15-document slice we add a real retrieval baseline: the internalized adapter (84.2% recall) beats a BM25-RAG pipeline with a base reader (58.9%) and even a realistic gold-chunk oracle (65.6%) at lower latency. We report the full arc, including three misdiagnoses, as a case study in debugging LLM training empirically.

---


### 63. [Decentralized Compute on Untrusted Hardware Using Intel TDX and Encrypted CVMs](https://arxiv.org/abs/2607.21865)

**<font color=#1a73e8>作者：</font>** Venish Patidar, Dhruv Bindra, Ahmed Darwich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid growth of artificial intelligence workloads has generated an unprecedented demand for secure and scalable compute resources. However, centralized cloud providers continue to dominate both pricing and security models. In an increasingly competitive AI landscape, where the compromise of training data or model weights can confer a significant advantage, there is a critical need for a computing infrastructure that safeguards data at rest, in transit, and in use, while remaining affordable and broadly accessible. Furthermore, existing GPU cluster offerings (e.g., 8xH100s, 8xH200s, 8xB200s) create financial barriers that limit access for organizations, startups, and independent researchers seeking secure, high-performance computing environments.
This paper introduces a decentralized, confidential computing platform that leverages Intel Trust Domain Extensions (TDX), Intel Trust Authority (ITA) and NVIDIA Confidential Computing (CC) to establish a distributed ecosystem of fully encrypted Confidential Virtual Machines (CVMs). The proposed architecture incentivizes hardware providers to contribute Intel TDX capable compute resources. Each participating provider is provisioned with a freshly instantiated, uniquely encrypted Ubuntu 24.04 CVM, providing data protection across all stages, at rest, in transit, and in use.
By decentralizing the confidential computing stack and leveraging confidential computing across independently operated nodes, this work demonstrates a viable alternative to traditional cloud-based infrastructures. The proposed system offers enhanced security assurances, transparent cost structures, and democratized access to enterprise-grade secure compute capabilities, paving the way for a more open, secure, and equitable foundation for next-generation AI development.

---


### 64. [Scaling Laws for Classical Machine Learning on Tabular Data: A Benchmark Study](https://arxiv.org/abs/2607.21866)

**<font color=#1a73e8>作者：</font>** Kaihua Ding  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prior classical-ML learning-curve work fits power laws to tree, linear, and kernel models on tabular data, but at small scale: typically one curve, one team, a handful of cells. We present a distributed classroom-scale replication: 127 students each ran a fixed protocol on 3 assigned datasets, drawn from 18 tabular classification and regression datasets and 6 model families (Boosting, Random Forest, SVM, Linear/Logistic, Ridge, Lasso), yielding 11,536 training runs and 1,648 fitted power-law curves of the form error(N) = a N^(-b) + c. Three findings. (1) Power laws fit: R^2 > 0.8 on 77.7% of cells, with tree ensembles dominating at full data (Boosting 50% of datasets, RandomForest 33%; linear models underperform on classification). (2) Approximate shared exponents within a model family: for 5 of 6 families, a single family-level exponent predicts each family's cross-dataset curves nearly as well as per-dataset exponents (R^2 gap < 0.011), though AIC favors the unconstrained fit and curve collapse is partial (32-58% of points within +/-0.5 dex). We frame this as approximate predictive compressibility, not dataset-independent universality; Lasso fails outright (negative control) and Ridge is fragile under leave-one-dataset-out. (3) Replicator-implementation variance: with random_state=42 fixed, independent re-implementations of the same protocol still differ by mean CV(b) = 0.144 on the fitted exponent -- not seed variance, but the spread induced by unconstrained parts of the protocol (preprocessing, encoding, missing-value handling). We release the aggregated curves, per-cell fits, and a practical data-requirement table for N* to reach target error 0.15.

---


### 65. [When Is a Learned Command Adapter Worth It? Closed-Loop Identification and Counterfactual Auditing of Frozen Locomotion Policies](https://arxiv.org/abs/2607.21867)

**<font color=#1a73e8>作者：</font>** Zongtan Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Adding a learned adapter to a frozen, command-conditioned locomotion policy is worthwhile only if the interface exposes improvements that are both real and recoverable from deployment-time observations. We introduce an adapter necessity audit that separates global operating-point gain,same-state counterfactual headroom, deployment gain over a cross-fitted fixed action, and state-allocation gain over a frequency-matched randomized policy. Source-cluster learner refits map these quantities and constraint violations to a GO/NO-GO/ABSTAIN decision. Closed-loop command- response identification provides optional decision features. On Go2, an archived scale-prefix diagnostic finds 5.2% same-state headroom but only 0.55% recovered allocation gain. Our confirmatory audit evaluates direct, scale, heading, and yaw interventions on twenty independent clusters for each of three query distributions induced by direct control, VGCC, and MPC, using 200 full learner refits. At 1% deployment and allocation thresholds and a 5% violation tolerance, direct queries return NO-GO, while VGCC and MPC queries ABSTAIN. VGCC has the largest mean deployment gain (1.34%), but its allocation lower bound is 0.09% and its violation upper bound is 6.25%. A deployment-representative twenty-cluster H1 audit also returns NO-GO, whereas a learner-level synthetic control returns GO. The audit therefore tests whether observable signal justifies state-dependent adaptation rather than presuming that an adapter is valuable.

---


### 66. [Multi-Agent System-driven Digital Twins for predictive maintenance: architectures, technologies and open research challenges](https://arxiv.org/abs/2607.21873)

**<font color=#1a73e8>作者：</font>** Korota Arsène Coulibaly, Mohamed Hamlich  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital twins have emerged as a foundational technology within the context of Industry 4.0, offering a paradigm for the real-time virtual representation of physical systems. However, managing their growing complexity, particularly in distributed industrial environments, requires intelligent architectures capable of autonomous decision-making, dynamic adaptability, and inter-agent coordination. This systematic review explores the intersection between Multi-Agent Systems and Digital Twins, with a particular focus on predictive maintenance applications in resource-constrained contexts. Through a critical analysis of over 547 papers published in high-impact journals (IEEE Transactions, Nature, Elsevier, MDPI), we establish a taxonomy of existing hybrid architectures, identify persistent technological bottlenecks, and formulate three open research questions concerning: (i) the deployment of artificial intelligence on resource-constrained microcontrollers, (ii) distributed multi-node coordination via lightweight communication protocols, and (iii) the hierarchical orchestration of Digital Twins toward smart factory control integrating residual life estimation and explainable Artificial Intelligence. The results of this analysis reveal that, despite significant progress, no existing system offers an integrated embedded-distributed hierarchical solution that simultaneously meets the requirements of Industry 5.0.

---


### 67. [Variance-Reduced Q-Learning over Static and Time-Varying Networks](https://arxiv.org/abs/2607.21876)

**<font color=#1a73e8>作者：</font>** Sreejeet Maity, Feng Zhu, Aritra Mitra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We investigate a decentralized reinforcement learning problem involving multiple agents that interact with the same Markov Decision Process (MDP). The agents can exchange information over a network to collectively learn the optimal state-action value function. For this setting, we introduce a novel epoch-based distributed $Q$-learning algorithm called VRDQ, where within each epoch, agents locally estimate the Bellman optimality operator and diffuse information using a consensus-based protocol. For both static and time-varying networks, we establish high-probability finite-time convergence rates for VRDQ that enjoy linear speedups from collaboration. Crucially, we prove that such speedups in sample-complexity require only $\tilde{O}(1)$ communication, substantially improving upon the communication costs in prior work.

---


### 68. [Farmland Extent and Visible Boundary Mapping from 1 m NAIP Imagery Using Residual U-Net and Text-Prompted SAM 3 Refinement](https://arxiv.org/abs/2607.21881)

**<font color=#1a73e8>作者：</font>** Mohammadreza Narimani, Vikram Anand, Parastoo Farajpoor  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agricultural field maps are often proprietary, incomplete, or outdated, yet they provide the spatial framework for crop monitoring, production accounting, and land-conversion analysis. This study presents a reproducible workflow for mapping farmland extent and visible boundaries from 1 m NAIP RGB imagery. Thirty-seven scenes spanning open cropland, peri-urban interfaces, semi-arid irrigation geometries, and fragmented mosaics were annotated in CVAT and converted to binary masks. Non-overlapping 256 x 256 patches yielded 5,698 samples, split by source scene into 3,850 training, 770 validation, and 1,078 test patches. A residual U-Net (ResUNet) trained with a Dice-dominant loss, L = 2.5(1 - Dice) + BCE, achieved test accuracy 0.8808, IoU 0.8605, Dice 0.9234, precision 0.8766, and recall 0.9794. A frozen SAM 3 branch prompted with "agricultural farmland field" was fused with ResUNet by logical OR. On selected difficult patches, Dice improved from 0.858 to 0.955 (orchard rows) and from 0.804 to 0.903 (fragmented parcels). Sliding-window stitching produced coherent regional masks (example tile Dice 0.898 and 0.919). The product is a semantic farmland-extent layer, not a cadastral parcel map, and supports agricultural monitoring where current field layers are unavailable.

---


### 69. [Remedying Coarsening-Based GNN Training under Heterophily via Adaptive Complementary Enhancement](https://arxiv.org/abs/2607.21885)

**<font color=#1a73e8>作者：</font>** Guoming Li, Jian Yang, Xukun Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coarsening-based training for graph neural networks (GNNs), i.e.\ training on coarsened graphs rather than the original large ones, has become a promising direction for scaling GNNs to massive graphs. However, prior work has been evaluated almost exclusively on \textit{homophilic} graphs, leaving the more challenging \textit{heterophilic} settings underexplored. We show, both empirically and theoretically, that existing coarsening-based training methods suffer significant performance degradation on heterophilic graphs due to inevitable loss of graph information during coarsening. To address this, we propose {\bf A}daptive {\bf C}omplementary {\bf E}nhancement, a plug-and-play, model-agnostic strategy that reintegrates the information discarded in coarsening: ACE learns a projector for re-constructing original node features and applies \textit{anisotropic structural regularization} to embed local heterophily. We further adopt \textit{homoscedastic uncertainty weighting} to adaptively balance the combined training objective of primary coarsened-graph training loss and full-graph auxiliary loss with augmented node features re-constructed by the heterophily-aware projector. Extensive experiments show that ACE drives consistent gains on heterophilic benchmarks while preserving competitive results on homophilic graphs with minimal computational overhead. Code is available at the GitHub repository: this https URL.

---


### 70. [PrivDNN: A Secure Multi-Party Computation Framework for Deep Learning using Partial DNN Encryption](https://arxiv.org/abs/2607.21895)

**<font color=#1a73e8>作者：</font>** Liangqin Ren, Zeyan Liu, Fengjun Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In the past decade, we have witnessed an exponential growth of deep learning models, platforms, and applications. While existing DL applications and Machine Learning as a service (MLaaS) frameworks assume fully trusted models, the need for privacy-preserving DNN evaluation arises. In a secure multi-party computation scenario, both the model and the data are considered proprietary, i.e., the model owner does not want to reveal the highly valuable DL model to the user, while the user does not wish to disclose their private data samples either. Conventional privacy-preserving deep learning solutions ask the users to send encrypted samples to the model owners, who must handle the heavy lifting of ciphertext-domain computation with homomorphic encryption. In this paper, we present a novel solution, namely, PrivDNN, which (1) offloads the computation to the user side by sharing an encrypted deep learning model with them, (2) significantly improves the efficiency of DNN evaluation using partial DNN encryption, (3) ensures model accuracy and model privacy using a core neuron selection and encryption scheme. Experimental results show that PrivDNN reduces privacy-preserving DNN inference time and memory requirement by up to 97% while maintaining model performance and privacy. Codes can be found at this https URL

---


### 71. [Learning Adaptive Semantic Gaussian Allocation for 3D Occupancy](https://arxiv.org/abs/2607.21896)

**<font color=#1a73e8>作者：</font>** Kanglin Ning, Yiran Zhao, Wenrui Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic 3D Gaussians provide a compact representation for 3D semantic occupancy prediction by rendering semantic primitives into a voxel volume under voxel-wise supervision. Recent methods have improved the modeling ability and efficiency of this representation through more flexible primitive shapes, geometry-guided initialization, and progressive densification. However, these advances mainly determine how primitives are represented, initialized, or added, and do not explicitly address how to select the most useful Gaussians when their total number must be limited to control memory and computation. This imbalance creates an allocation bottleneck: redundant Gaussians remain in simple regions, while difficult regions receive insufficient semantic support. We propose the Semantic Gaussian Allocation Transformer (SAGFormer), which uses Gaussian attributes and local geometric-semantic features to score candidates and select a fixed final Gaussian set. Experiments on nuScenes-SurroundOcc and SSCBench-KITTI-360 show that SAGFormer improves occupancy prediction under the evaluated protocols and yields more semantically consistent and better-utilized Gaussian representations. Under similar final counts and raw coverage, it reduces semantic mixing, strengthens class-consistent voxel support, and produces fewer unused Gaussians. The results indicate that explicit capacity allocation is a useful complement to Gaussian refinement for semantic occupancy prediction.

---


### 72. [ISPCloak: Weaponizing ISP for Optimization-Free Physical Camouflage against Deepfake Detectors](https://arxiv.org/abs/2607.21897)

**<font color=#1a73e8>作者：</font>** Jiale Zhao, Jiajun Wan, Lei Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative models has spurred the critical need to evaluate the worst-case robustness of deepfake detectors. In this paper, we reveal a fundamental blind spot in current forensic paradigms: while existing detectors excel at capturing digital synthesis artifacts, their effectiveness drops drastically when AI-generated content is cloaked in authentic physical imaging characteristics. We posit that genuine photographs inherently possess hardware-intrinsic statistical signatures, which are imperceptible footprints imprinted by optical sensors and Image Signal Processing (ISP) pipelines, and are fundamentally absent in purely data-driven generative models. Driven by this insight, we propose ISPCloak, a novel optimization-free adversarial attack framework that explicitly weaponizes the ISP pipeline to mislead the judgment of deepfake detectors. Rather than relying on computationally expensive gradient perturbations, our method first employs an Invertible ISP network to project images into the RAW domain. Then, we seamlessly imprint the complex statistical priors of real cameras onto AI-generated images by injecting realistic Poisson-Gaussian sensor noise and conducting forward ISP reconstruction. Synergized with generative artifact suppression and adaptive masking, this streamlined physical simulation enables ultra-fast generation of adversarial examples. Extensive experiments show that embedding authentic physical perturbations fundamentally disrupts a broad range of current detection mechanisms, yielding universally evasive adversarial examples with imperceptible visual alterations.

---


### 73. [Cleaning the NTP Pool: Detecting and Mitigating NTP-Sourced IPv6 Scanning](https://arxiv.org/abs/2607.21903)

**<font color=#1a73e8>作者：</font>** Erik Rye, Robert Beverly  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The ephemeral and random nature of IPv6 client addresses presents a practical challenge to attacks that depend on Internet-wide scanning or reconnaissance -- the adversary must first \emph{find} the client's IPv6 address. While a well-positioned passive adversary can potentially harvest some active IPv6 client addresses, such power is typically reserved for e.g. large CDN or Internet exchange points. In contrast, prior work has shown the feasibility of a low-power entity to easily join the volunteer-based NTP Pool and harvest large quantities of active IPv6 client addresses.
In this work, we develop a methodology to not only rigorously identify such IPv6 address harvesting and the entities gathering addresses, but also characterize \emph{what} these entities subsequently do with the addresses. Specifically, we query all NTP Pool servers across the global Internet over the course of one-year using unique IPv6 client addresses, and monitor and correlate any later activity targeting these addresses. In sum, we identify 22 NTP Pool servers, within 4 primary clusters, that are part of larger monitoring infrastructures that utilize the gathered addresses for reconnaissance, port scanning, and service and vulnerability enumeration. To better understand the legal and ethical gray area of such behavior, we both engage with the NTP Pool operators and a cybersecurity insurance firm running one of the harvesting and scanning clusters. The NTP Pool has since integrated our system into their monitoring infrastructure to remove such NTP servers, while the firm changed its operational policy to be more transparent and provide clear opt-out mechanisms.

---


### 74. [Diffusion Models in Medical Image Inpainting: Challenges, Solution Taxonomy, and Future Directions](https://arxiv.org/abs/2607.21904)

**<font color=#1a73e8>作者：</font>** Arthur Dantas Mangussi, Joana Cristo Santos, Ricardo Cardoso Pereira 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image inpainting aims to reconstruct missing or corrupted regions of an image while preserving as much as possible, visual and semantic consistency. In medical imaging, this task is particularly important because artifacts, missing information, and pathological alterations can compromise diagnostic reliability and downstream clinical applications. Recently, diffusion models have emerged as state-of-the-art generative approaches for medical image inpainting due to their ability to generate anatomically consistent reconstructions. This survey presents a systematic review of diffusion-based methods for medical image inpainting, covering the main architectures, applications, datasets, and evaluation strategies reported across 60 studies. In addition, we propose a taxonomy for diffusion-based approaches. The analysis reveals a rapid growth of research interest in diffusion-based medical image inpainting, with denoising diffusion probabilistic models and latent diffusion models emerging as the dominant architectures. The reviewed studies mainly focus on artifact removal, data augmentation, pseudo-healthy tissue reconstruction, and anomaly detection, particularly in magnetic resonance imaging and computed tomography imaging. Overall, diffusion models demonstrate strong performance in producing anatomically plausible reconstructions and aiding downstream clinical tasks. However, the review also highlights important challenges, including the lack of standardized benchmarks, limited dataset diversity, and restricted validation procedures across diverse clinical applications and imaging scenarios.

---


### 75. [MissHyper: Restoring Clinical Synchronicity in Missingness-Guided Hypergraph Forecasting](https://arxiv.org/abs/2607.21922)

**<font color=#1a73e8>作者：</font>** Mingyi Ma, Qingxiong Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical irregular multivariate time series are shaped not only by physiological dynamics but also by the measurement process that determines when and what to observe. In event-centric models, however, co-timestamp structure can be flattened too early: measurements acquired at the same timestamp are embedded as isolated nodes, leaving local patient-state context unavailable until later message-passing layers. We study this pre-propagation representation bottleneck and address it by restoring co-timestamp context before message passing begins. We propose MissHyper, a missingness-guided hypergraph forecasting model with pre-propagation synchronicity restoration. MissHyper augments each event with a local support-density cue, aggregates co-timestamp records to recover patient-state context, and uses a missingness-guided gate to adaptively fuse node-specific evidence with the recovered context. Across PhysioNet 2012, MIMIC-III, and MIMIC-IV, MissHyper achieves consistent gains in multi-step forecasting and outperforms a strong hypergraph baseline. These results suggest that improving event initialization can benefit sparse clinical forecasting without requiring a redesigned downstream propagation architecture. Ablations indicate that snapshot restoration, adaptive fusion, and support-density encoding all contribute, pointing to event initialization as a critical design axis for sparse clinical forecasting.

---


### 76. [LatentFlow: Visual Analytics for Latent Space Analysis in Molecular Graph Neural Networks](https://arxiv.org/abs/2607.21941)

**<font color=#1a73e8>作者：</font>** Shiyi Liu, Jiaqing Chen, Nicholas Hadler 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemists and materials scientists increasingly use machine learning models, such as graph neural networks (GNNs), to predict properties of molecules and the outcomes of their reactions. Beyond predictive performance, understanding how these models organize chemical information internally in their latent spaces, i.e., the embeddings of the molecules, is critical. Analyzing latent spaces helps diagnose model behavior and assess whether the learned embeddings are organized in ways that reflect meaningful chemical relationships. Unfortunately, existing methods provide limited support for analyzing latent spaces across layers and across different model states (e.g., training epochs, model configurations, and input data), making it difficult to understand how these latent spaces evolve throughout a model or relate to chemical concepts. We present LatentFlow, a visual analytics system developed in collaboration with a domain expert for analyzing latent spaces in molecular GNNs. LatentFlow groups embeddings into clusters and supports exploration of latent spaces by tracking how these clusters change across layers and model states using a modified Sankey diagram. To support interpretation, LatentFlow links these clusters to representative molecules and their shared substructures, and it allows scientists to introduce their own domain knowledge and compare it with the patterns found in the latent spaces. We evaluate LatentFlow through two case studies. The results show that LatentFlow helps scientists understand how latent spaces evolve, identify meaningful molecular patterns, and better interpret model behavior.

---


### 77. [VisionPulse: A Virtual Reality System Enabling Accessible Discovery and Navigation for Blind and Low Vision Users](https://arxiv.org/abs/2607.21944)

**<font color=#1a73e8>作者：</font>** Samuel Martin, Pooyan Fazli, Hasti Seifi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Free exploration is an important aspect of many engaging virtual reality (VR) experiences, yet remains largely inaccessible to blind and low vision (BLV) users due to its reliance on visual feedback. Existing approaches support BLV navigation through prebuilt menus of environment and audio beacons, but offer limited support for free-form discovery. We present VisionPulse, an accessible VR system that enables BLV users to explore virtual environments through natural head and hand movements, combined with auditory, haptic, and text-to-speech feedback. VisionPulse introduces a discovery-driven approach that allows users to progressively uncover regions and objects, alongside navigation support through waypoint guidance and object localization via responsive audio and orientation-based haptics. A study with 12 BLV participants showed a strong preference for VisionPulse's discovery-based exploration and multimodal feedback, without negatively impacting task performance or perceived workload. Our findings underscore the importance of accessible, free-form VR experiences, and contribute insights for inclusive VR design.

---


### 78. [Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge](https://arxiv.org/abs/2607.21946)

**<font color=#1a73e8>作者：</font>** Jiseok Kwak, Suhyeon Jo, Taewoo Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This technical report presents our approach to Challenge Track~3: SeePhys Pro at the 3rd AI for Math Workshop, where the task is to answer college-level physics questions whose statement and figure may be given partly or entirely as an image. Visual physics problems become substantially harder for large language models when the decisive information resides in a figure rather than in the text, and this modality gap widens as more of the problem migrates into the image. We address the task with a two-stage framework: a visual information extraction stage that re-expresses figure content as solver-readable text to close the modality gap, and a reasoning stage that orchestrates three heterogeneous solvers through multi-agent debate. Our analysis yields two findings: the gain from orchestration comes from reliable answer selection rather than from additional debate, and the value of a figure aid scales with how much of the problem is locked inside the image. The resulting pipeline improves overall accuracy over a single-agent baseline from 0.643 to 0.802 on the public split, and won 1st place on both the public and the private leaderboard (private overall 0.743).

---


### 79. [MA-DAR: Manifold-Aligned Dynamic Adaptive Routing for Continual Temporal Knowledge Graph Reasoning](https://arxiv.org/abs/2607.21949)

**<font color=#1a73e8>作者：</font>** Xiangjun Shi, Chong Mu, Jinchuan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual temporal knowledge graph (TKG) reasoning aims to continuously incorporate newly emerging facts while preserving previously acquired knowledge. Replay-based continual learning has achieved promising performance by revisiting historical representations. However, existing methods primarily focus on what to replay, while largely overlooking how replayed representations should be integrated with current ones. Such direct integration often gives rise to two critical forms of representation conflict: \textit{norm domination} and \textit{semantic blurring}, ultimately degrading continual reasoning performance. To address these challenges, we propose MA-DAR (Manifold-Aligned Dynamic Adaptive Routing), a lightweight plug-and-play framework for replay representation fusion. MA-DAR first aligns replayed and current representations onto a shared manifold to alleviate distribution discrepancies. It then employs a dynamic gating mechanism to learn dimension-wise fusion weights, adaptively determining the contribution of replayed and current representations to the fused representation. Furthermore, a polarization regularizer encourages more decisive routing behaviors by discouraging ambiguous gating decisions, resulting in more stable and effective knowledge integration. Extensive experiments on four public continual TKG benchmarks demonstrate that MA-DAR consistently improves the performance of representative TKG encoders while remaining effective under different replay settings. Comprehensive ablation studies and visualization analyses further verify the effectiveness of manifold alignment and dynamic adaptive routing in mitigating representation conflicts and improving continual reasoning.

---


### 80. [Incentives and Market Structure in Intent-Based Exchanges: Evidence from a Solver-Reward Reform](https://arxiv.org/abs/2607.21955)

**<font color=#1a73e8>作者：</font>** Ruiyang Zhang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intent-based decentralized exchanges delegate execution to a competitive class of agents -- solvers -- whose behavior is shaped by protocol-designed reward rules. We measure how a change to those rules reshapes who captures value, using a governance-dated natural experiment: CoW Protocol CIP-74 (effective 8 December 2025), which replaced a fixed solver-reward cap with one tied to protocol revenue and introduced an ad-valorem volume fee. Using daily solver shares over 395 days, we find the reform reallocated trading value by order size. The robust signature is a monotone size gradient: concentration fell in small orders and rose in large ones across four order-value buckets (Spearman rho=1.00, exact permutation p=0.042) -- a pattern that survives dropping the single largest solver. Aggregate concentration also rose (volume-weighted HHI 0.176->0.241), substantially carried by the incumbent top solver. By trade count the market de-concentrated (count-HHI -0.060). A simple solver-economics model rationalizes the pattern: an ad-valorem fee is competitively neutral, while a revenue-linked reward cap raises the marginal payoff to inventory-rich solvers on large orders -- consistent with restricted-entry predictions (Chitra et al. 2024). A control venue (UniswapX) shows no matching break. We detect no change in average execution quality (~7 bps bound). A triple-difference exploiting a February 2026 fee cut is directionally consistent but underpowered. Reward design measurably reallocates who captures value in intent markets, without moving the average price users receive.

---


### 81. [Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings](https://arxiv.org/abs/2607.21962)

**<font color=#1a73e8>作者：</font>** Quentin Spencer  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmarks for LLM-agent memory typically generate conversations first and extract answer keys afterwards -- with documented label-error and contamination problems -- and they overwhelmingly measure short interaction histories. We invert the pipeline: a seeded life-script sampler emits facts with validity intervals, volatility classes, and source channels before any text exists; an LLM renderer writes chat and email from per-event fact manifests; a fidelity verifier confirms every planted fact; and questions are instantiated mechanically from the script, so gold answers are script-valid by construction and separately validated for answerability. The synthetic, fictionalized corpus (~380 questions, 15 types) embeds features absent from the benchmarks we survey: per-fact validity intervals, sent/received trust distinctions, injection probes in a benign harness, and as-of-date question sets. Benchmarking five memory architectures against a no-memory control (fixed answerer, versioned LLM judge, three replicates, two horizons), we find backend rankings invert with history length: the budgeted curated-map memory that leads at three weeks loses recall of evicted content by nine weeks (96% to 72%) while a provenance-typed graph rises to 90%; the inversion is positive for all six users under complete cross-family re-judging (exact p=0.031). A full-rendered-history baseline ties or exceeds the best memory system at the short horizon but shows no judge-independent advantage at nine weeks, at about twice the read cost. Write-stage quality strongly correlates with downstream quality (weakly-written facts fail 24% vs 2%), and injection resistance tracked whether provenance boundaries survive representation. A layered architecture performs best among the memory systems in both regimes (96.8% short-horizon) and is released as Veracium, an open-source library, with the corpus generator and harness.

---


### 82. [TextSLIP: Text Self-Supervised CLIP for Medical Report Generation](https://arxiv.org/abs/2607.21970)

**<font color=#1a73e8>作者：</font>** Haoyu Jiang, Ziping Cong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automating radiology report generation is important for improving reporting consistency and clinical workflows . While Contrastive Language--Image Pretraining (CLIP) has advanced medical vision language modeling, existing CLIP-style approaches may still provide insufficient fine-grained semantic supervision for complex report generation. Standard CLIP primarily optimizes cross-modal alignment, without explicitly structuring the textual embedding space that guides visual representation learning. To address this limitation, we propose TextSLIP, a general medical vision-language pretraining framework that augments CLIP with intra-modal text contrastive learning. By improving textual embedding discriminability through self-supervised augmented text pairs, TextSLIP is designed to provide finer-grained linguistic supervision to the visual encoder. As an initial validation, we pretrain TextSLIP on a curated dataset of 7 million brain MRI image-text pairs and fine-tune the pretrained visual encoder within a report generation architecture. In controlled comparisons with CLIP-style baselines, TextSLIP shows consistent improvements on report generation metrics. Ablation studies further suggest that text-side self-supervision contributes to the observed gains. These results indicate that text-level contrastive learning is a promising direction for improving medical visual-textual alignment, while broader validation across additional medical domains remains an important next step.

---


### 83. [On the Convergence of Stochastic Low-Rank Adaptation](https://arxiv.org/abs/2607.21975)

**<font color=#1a73e8>作者：</font>** Ru Wang, Chengchang Liu, John C.S. Lui  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) optimizes $J(B,A)=\mathcal L(W_\mathrm{base}+sBA)$ over two adapters $B \in \mathbb{R}^{m \times r}$ and $A \in \mathbb{R}^{r \times n}$ that form a low-rank update to a frozen pretrained weight matrix $W_\mathrm{base} \in \mathbb{R}^{m \times n}$. The prior analysis shows LoRA-GD takes $\exp\{\mathcal{O}(\epsilon^{-2})\}$ oracle calls to find an $\epsilon$-stationary point such that $\|\nabla J(B,A)\|\leq \epsilon$ in the deterministic setting. We sharpen the analysis and show that $\mathcal{O}(\epsilon^{-4})$ full-gradient evaluations suffice for the same first-order criterion. We further study stochastic LoRA under unbiased gradient estimates and finite variance. We propose LoRA-NSGDM, which finds an $\epsilon$-stationary point with $\mathcal{O}(\epsilon^{-8})$ stochastic oracle complexity. Under the additional mean-square smoothness condition, we use variance reduction strategy and propose LoRA-STORM, which improves the stochastic oracle complexity to $\mathcal{O}(\epsilon^{-6})$.

---


### 84. [Analyzing Toxic Behavior and Its Impact on the Mastodon Community](https://arxiv.org/abs/2607.21980)

**<font color=#1a73e8>作者：</font>** Pasan Kamburugamuwa, Scrivner, Olga B  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mastodon as a decentralized federation of independently moderated social servers poses unique challenges for the detection and mitigation of toxic content. There are no unified moderation standards. The ecosystem is very diverse and uneven. This paper explores the development and spread of toxicity in Mastodon, utilizing machine learning methods to examine user posts. The results offer clarity on toxicity trends and its implications for community health and decentralized governance.

---


### 85. [J-CoT: Chain-of-Thought in J-Space](https://arxiv.org/abs/2607.21981)

**<font color=#1a73e8>作者：</font>** Junde Wu, Jiayuan Zhu, Fengling Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought prompting improves language-model reasoning by carrying intermediate states across successive computation steps. However, relying on natural language as the only recurrent interface is overly restrictive, since many transient computations do not need to be fully verbalized. Existing latent-reasoning methods remove this constraint by recurrently propagating continuous hidden states. However, these methods pass a dense hidden vector as a whole, without an explicit mechanism for selecting and organizing the information needed by the next reasoning step. This motivates an intermediate interface that remains linguistically grounded without requiring a decoded sentence. We introduce \textbf{J-CoT}, a recurrent reasoning framework built on \emph{J-space}, a vocabulary-indexed coordinate system within the model's hidden representations. Within each cycle, the model computes in its full hidden space. At the cycle boundary, J-CoT expresses the intermediate state as vocabulary-indexed coefficients, carries these coefficients forward as a \emph{J-thought}, and maps them back into the model's hidden representation for the next cycle. J-CoT therefore requires neither a fluent intermediate rationale nor recurrence over the complete hidden state. Under matched backbone and inference settings, J-CoT-Zero matches or exceeds the strongest evaluated latent-reasoning baseline on every benchmark, while J-CoT-Train obtains the highest score across the evaluated mathematical, scientific, coding, and structured path-reasoning tasks.

---


### 86. [From Perturbation Correction to Geometry-Aware Sampling: Sharpness-Guided Equilibrium Sampling for Balanced Flat Minima in Long-Tailed Learning](https://arxiv.org/abs/2607.21999)

**<font color=#1a73e8>作者：</font>** Jiaxin Deng, Junbiao Pang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-tailed learning couples two sources of poor generalization: head classes dominate training exposure, while under-represented classes often converge to sharper regions of the loss landscape. Conventional re-sampling addresses the former without considering geometry, whereas existing long-tailed sharpness-aware minimization (SAM) methods modify losses or perturbations only after biased mini-batches have been drawn. We introduce Sharpness-Guided Equilibrium Sampling (SGS), which treats the sampling distribution as an active control variable for optimization geometry. SGS dynamically adjusts subsequent mini-batches by increasing the sampling probability of less frequently sampled classes while suppressing classes with large SAM-induced loss changes, using only cumulative class counts and EMA sharpness estimates obtained from the standard SAM update, without class-wise perturbations or additional backward passes. We characterize this sampling process through a continuous-time stochastic differential equation and a sampling-dependent PAC-Bayes analysis, explaining how frequency-sharpness feedback can move training toward a more balanced flatness profile. On CIFAR-100 LT with an imbalance ratio of 100, SGS-SAM improves Focal-SAM by 10.85 points in tail accuracy and 3.56 points overall. On ImageNet-LT, it improves ImbSAM by 6.59 points on tail classes and 1.20 points overall. Its training time is only $1.02\times$ that of vanilla SAM. Beyond these gains, SGS establishes a sampling-side route to loss-landscape control, suggesting that future long-tailed methods can jointly regulate data exposure and optimization geometry rather than treating either as fixed.

---


### 87. [Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning](https://arxiv.org/abs/2607.22002)

**<font color=#1a73e8>作者：</font>** Heyang Jiang, Henry Liu, Baharan Mirzasoleiman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has emerged as a highly effective framework for improving LLM reasoning, with methods such as GRPO among its most successful instantiations. However, GRPO relies on repeated generation of long chain-of-thought rollouts. Training time scales with the number of rollouts, a large fraction of which are uninformative. Thus, GRPO is computationally expensive and unstable. To mitigate this, existing approaches either generate a larger pool of rollouts and filter the most informative prompts, or leverage historical signals for filtering at later stages of training. These strategies offer modest performance gains, but slow down the overall process. To address this, we propose VarIance Guided Online Rollout allocation (VIGOR) which instead of allocating a fixed rollout budget per example, begins with a small number of rollouts for all examples in a batch and iteratively allocates additional rollouts to those with the highest group reward variance until a fixed total rollout budget is reached. Theoretically, we show that under RLVR, reward variance controls the gradient magnitude, and derive VIGOR's closed-form speedup ratio over GRPO, which grows with refinement rounds under Pareto-distributed reward variance. Experiments on mathematical reasoning and coding tasks show that VIGOR reaches target accuracy with up to 2.3$\times$ fewer rollouts on math, reaches GRPO's final coding full pass rate with 1.49$\times$ fewer rollouts, and improves the coding average test pass rate by 3.4 points.

---


### 88. [Energy Manifold Natural Gradient Descent: Riemannian Optimization for Neural PDE Solvers](https://arxiv.org/abs/2607.22004)

**<font color=#1a73e8>作者：</font>** Zhangyong Liang, Huanhuan Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Energy natural gradient descent (ENGD) aligns parameter updates with the curvature of an underlying function-space energy, but existing formulations assume an unconstrained Euclidean parameter domain. We introduce \EMNGDfull{}, a manifold optimization framework for physics-informed and variational neural PDE solvers whose parameters lie on a Riemannian manifold. EMNGD restricts the energy-induced quadratic model to feasible tangent directions and uses retractions to preserve parameter constraints throughout optimization. Under coercivity, we prove that the push-forward of the undamped EMNGD direction is the best feasible approximation to the function-space Newton vector in the energy metric. We establish coordinate invariance, exact reduction to ENGD in Euclidean space, global first-order convergence with Armijo backtracking, and robustness to inexact tangent solves. For quadratic residual energies and generalized Gauss--Newton pullbacks, the Woodbury identity transfers the tangent system to sample space without changing the direction. Nyström approximation provides scalable sample-space solves with controlled direction error and recovers the exact direction after iterative convergence. On the evaluated neural PDE benchmarks, EMNGD achieves higher accuracy and faster convergence than the compared state-of-the-art baselines. Woodbury preserves the EMNGD direction, while scalable-solver diagnostics quantify the accuracy--cost trade-off of preconditioning and residual subsampling.

---


### 89. [What Clinicians Need: Designing, Developing and Evaluating an AI-Based Decision Support System for Autism Assessment](https://arxiv.org/abs/2607.22005)

**<font color=#1a73e8>作者：</font>** Ulrike Schäfer, William Saakyan, Matthias Norden 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI methods promise to support autism spectrum condition (ASC) diagnostics in adults, a complex and time-consuming process, that is characterized by a shortage of specialized clinicians. To date, clinicians' needs and their interaction with such AI-based support remain underexplored. Our work aims to develop and evaluate an AI-based clinical decision support system (CDSS) for ASC assessment, and to investigate how it impacts clinicians' decision-making. By interviewing clinicians of varying experience levels, we identified five challenges and derived design strategies. Based on that, we developed SIT-CARE, a CDSS, which provides AI-based recommendations and data visualizations of clinically relevant nonverbal behavior. Through an evaluation study with newly recruited clinicians, we found that SIT-CARE led to different decision paths in regard to the ASC assessment, which are reflected in clinicians' mental models and decision changes. Overall, SIT-CARE demonstrated potential in improving initial diagnostic assessments, supporting in-depth diagnosis and empowering less experienced clinicians.

---


### 90. [Practical Graph Optimisation and AI-Driven Models for Active Directory Security Hardening](https://arxiv.org/abs/2607.22009)

**<font color=#1a73e8>作者：</font>** Huy Q. Ngo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Microsoft's Active Directory (AD) is a directory service that enables the IT admin to manage security permissions and control access within a Windows domain network. As a core management system in many of organisation, AD has become a primary target for adversaries. While many solutions for hardening attack graphs exist, these efforts fall short in addressing several key practical challenges specific to the AD attack graph. First, existing models often assume the graph is static, whereas a real-world AD environment is highly dynamic. Second, most proposed solutions are limited to the defensive measure of revoking vulnerabilities (edge removal), while more active defence mechanisms are largely unstudied. Third, because not all remediations are implementable, a practical end-to-end model must incorporate system admin feedback into the prioritisation process. This thesis aims to address these limitations by studying and proposing a number of game-theoretic and optimisation-based decision-making models. First, we propose a honeypot/decoy placement model based on the principle of minimising the number of shortest paths and the number of Domain Admin-reachable nodes. Second, building on this model, we introduce a defence strategy that considers the dynamic/temporal nature of the AD graph, where the objective is to find the location to deploy decoys that maximises the worst-case incident response time. Third, we introduce an adaptive prioritisation model that queries each high-risk attack path to the IT administrator for mediation. Finally, we introduce an end-to-end adaptive prioritisation model that minimises the approval effort of the system admin by finding a general adaptive edge-removal policy that generalises the system admin's decisions to edges with similar risk features. We show that the problems underlying all of the contributed models are computationally intractable.

---


### 91. [Cross-Domain Off-Policy Evaluation and Learning for Contextual Bandits](https://arxiv.org/abs/2607.22012)

**<font color=#1a73e8>作者：</font>** Yuta Natsubori, Masataka Ushiku, Yuta Saito  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-Policy Evaluation and Learning (OPE/L) in contextual bandits is rapidly gaining popularity in real systems because new policies can be evaluated and learned securely using only historical logged data. However, existing methods in OPE/L cannot handle many challenging but prevalent scenarios such as few-shot data, deterministic logging policies, and new actions. In many applications, such as personalized medicine, content recommendations, education, and advertising, we need to evaluate and learn new policies in the presence of these challenges. Existing methods cannot evaluate and optimize effectively in these situations due to the notorious variance issue or limited exploration in the logged data. To enable OPE/L even under these unsolved challenges, we propose a new problem setup of Cross-Domain OPE/L, where we have access not only to the logged data from the target domain in which the new policy will be implemented but also to logged datasets collected from other domains. This novel formulation is widely applicable because we can often use historical data not only from the target hospital, country, device, or user segment but also from other hospitals, countries, devices, or segments. We develop a new estimator and policy gradient method to solve OPE/L by leveraging both target and source datasets, resulting in substantially enhanced OPE/L in the previously unsolved situations in our empirical evaluations.

---


### 92. [EVL-MCoT: Enhanced Vision-Language Multi-CoT for Harmful Meme Detection](https://arxiv.org/abs/2607.22016)

**<font color=#1a73e8>作者：</font>** Hao Yang, Jin Wang, Xuejie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> MEMEs are widely used on the internet and often carry strong elements of sarcasm or irony. Understanding their hidden meanings typically requires a joint interpretation of text and vision. Existing methods focus on the dual-stream vision-language model to extract the visual and text simultaneously, which lacks background information and prior knowledge about the comprehensive explanation of MEME. One feasible option is to adopt chain-of-thought (CoT). However, the simple CoT approach lacks multi-perspective thinking, which may compromise the reliability of the resulting answers. Moreover, it often relies on shallow feature fusion, lacking the fusion of local details and fine-grained visual-prompt text alignment. This limitation prevents a deeper understanding of the intricate connections between the visual and the text. Herein, an enhanced vision-language multi-CoT (EVL-MCoT) approach is proposed to address these limitations. By promoting multi-CoT, EVL-MCoT enhances consistency and reduces bias in the decision-making process. Additionally, we design a prototype-guided and context-guided decoding framework, which incorporates visual prototypes to guide the fusion process and enables the model to align textual and visual information more precisely. We achieve promising results on the HatefulMemes and MultiOff datasets. The source code has been publicly released and is available at this https URL.

---


### 93. [Agent Security Needs Redefinition through a Holistic Framework](https://arxiv.org/abs/2607.22024)

**<font color=#1a73e8>作者：</font>** Vincent Siu, Jingxuan He, Kyle Montgomery 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent security is widely treated as a question about action content. Defenses ask whether an instruction looks malicious. Benchmarks ask whether an agent performs a harmful sounding action. \textbf{We argue that agent security is fundamentally a contextual problem, and that the current content based framing systematically misdefines it.} A command to ``delete user data'' might be a routine administrative request or a prompt injection attacking production systems, and the content alone cannot distinguish the two. Authorization context can. Across every injection task in AgentDojo and WASP, the same action is one an authenticated user would plausibly request in a routine workflow, which makes the conflation a structural property of evaluating security through content.
We operationalize contextual security through four properties that must hold jointly and be evaluated continuously across the agent's trajectory. Source Authorization asks who issued the command. Task Alignment specifies the agent's authorized objective. Action Alignment evaluates whether each action serves that objective. Data Isolation governs information flows across privilege boundaries. Under this reframing, indirect prompt injection becomes a Source Authorization violation. Snapshot benchmarks are structurally incapable of evaluating Data Isolation. Existing defenses are reorganized around the property they actually approximate. The contextual reframing changes which defenses are coherent, which evaluations measure something useful, and which attack patterns evaluation can see at all.

---


### 94. [CEL: Comprehensive Counterfactual Explanations Library and Benchmark](https://arxiv.org/abs/2607.22045)

**<font color=#1a73e8>作者：</font>** Oleksii Furman, Łukasz Lenkiewicz, Marcel Musiałek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations are a prominent approach in explainable artificial intelligence (xAI), providing actionable guidance on what input changes would alter a model's prediction to a desired outcome. While early methods primarily focused on minimal feature changes, recent work incorporates additional properties such as sparsity, actionability and plausibility. Despite this progress, fair and systematic evaluation remains challenging. Existing studies often rely on different data splits, predictive models, and evaluation metrics, which limits objective comparison across methods. To fill this gap, we introduce CEL (Counterfactual Explanations Library), a unified library and benchmark for counterfactual explanations designed to support consistent implementation and evaluation. CEL includes 18 datasets of varying size and complexity and provides implementations or reimplementations of 14 widely used counterfactual methods. Using this standardized setup, we conduct a comprehensive quantitative comparison across a variety of methods on datasets that differ in size, number, and types of attributes. The evaluation protocol incorporates multiple complementary metrics capturing validity, coverage, sparsity, proximity, and distributional plausibility, including density- and outlier-based measures to assess the realism of generated counterfactuals. To the best of our knowledge, this is the first comprehensive benchmark that systematically evaluates recent counterfactual explanation methods within a unified and reproducible framework. While prior libraries and benchmarking efforts exist in the literature, many are outdated, limited in scope, or lack consistent evaluation protocols. The proposed benchmark aims to improve reproducibility, enable fair comparison, and establish a workbench for the development of future counterfactual explanation methods.

---


### 95. [A Smooth Phase-Separation Model for Weak-Boundary Segmentation of Homogeneous Structures](https://arxiv.org/abs/2607.22053)

**<font color=#1a73e8>作者：</font>** Zihan Li, Jiebao Sun, Fanghui Song 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segmentation of adjacent structures with similar intensity distributions remains a challenging problem in image analysis, particularly when object boundaries are weak or ambiguous. Under such conditions, classical variational models may suffer from degenerated image-driven forces, leading to boundary leakage or undesired merging of neighboring regions. To address these limitations, we propose a smooth phase-separation variational model based on the Cahn--Hilliard equation for weak-boundary segmentation of homogeneous-appearance structures. The proposed framework integrates softmax-based region fitting with Cahn--Hilliard phase-field regularization to maintain interface discrimination under weak image-driven forces. We further introduce a mixed $L^2-H^{-1}$ gradient flow, which preserves higher-order interfacial regularization while allowing adaptive changes of phase masses, establish the continuous energy dissipation law, and prove the existence and uniqueness of weak solutions in the natural solution class. For numerical computation, we develop a stabilized scalar auxiliary variable (SAV) scheme that is linear, FFT-based, and satisfies a modified discrete energy dissipation law. Numerical experiments on synthetic and medical images demonstrate that the proposed method effectively separates adjacent homogeneous structures across weak boundaries and achieves competitive segmentation accuracy and improved boundary localization compared with representative variational, phase-field, and deep learning methods.

---


### 96. [BioZKFHE: Scalable Encrypted Biometric Identification via Verifiable Homomorphic Similarity Evaluation](https://arxiv.org/abs/2607.22065)

**<font color=#1a73e8>作者：</font>** Rundong Xin, Taotao Wang, Xiaoxiao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large-scale biometric identification in outsourced settings requires two properties simultaneously: biometric templates and queries must remain protected during computation, and the encrypted similarity outputs produced by an untrusted compute node must be verifiably correct before any application result is released. Existing FHE-based biometric systems primarily address confidentiality, while practical verifiability introduces two bottlenecks in the underlying encrypted 1:N matching layer: rotation- and bandwidth-heavy similarity evaluation and the high cost of proving repeated homomorphic similarity traces. We present BioZKFHE, a framework for scalable encrypted biometric identification via verifiable homomorphic similarity evaluation that combines BGV homomorphic computation with committee-mediated proof opening/decryption and smart-contract verification of opened proof batches. To reduce encrypted storage and avoid rotation-heavy encrypted 1:N matching, we propose Single-Coefficient Multi-Value (SCMV) packing, which binds multiple quantized embedding values into each plaintext entry through base-T expansion. To make proof generation practical, we propose Parallelizable and Verifiable Similarity Computation (PVSC), which exploits the Double-CRT execution structure of BGV to decompose each blockwise similarity trace into parallel proof instances that are opened and checked before result release. Under standard lattice assumptions and explicit committee/verifier assumptions, we analyze recoverability, noise growth, confidentiality, encrypted-output integrity, and finalized-result integrity. Experiments on FaceNet and MobileFaceNet show near-lossless biometric utility, up to 67 percent encrypted-storage reduction, and about 22 to 44 seconds end-to-end proof-verified runtime for 10k to 40k templates.

---


### 97. [Rethinking Multi-Branch and Cross-Backbone Fusion for Vehicle Re-Identification in the Foundation-Model Era](https://arxiv.org/abs/2607.22068)

**<font color=#1a73e8>作者：</font>** Yu Wang, Hongyu Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-branch architectures and CNN-Transformer fusion have long been regarded as effective ways to improve vehicle re-identification (Re-ID) by combining complementary representations. In this work, we revisit this assumption in the foundation-model era through a comprehensive empirical study. A single DINOv3-pretrained ConvNeXt trained with a tuned recipe achieves 88.19 mAP on VeRi-Wild Small and 77.47 mAP on VeRi-Wild Large using visual cues alone, matching the strongest protocol-verified metadata-dependent multi-branch baseline. Applying training-free re-ranking further improves performance to 92.38 and 83.68 mAP, respectively. Using this strong baseline together with retrieval-level branch diagnostics, we evaluate whether increasing representational diversity still provides measurable gains. Across both benchmarks, concatenating multiple branches built on a shared backbone changes the best single-branch performance by less than one mAP point while increasing the embedding dimension by 4x, and the resulting representation has an effective rank close to the original feature dimension. We further study cross-backbone fusion using an asymmetric frozen-anchor strategy to combine ConvNeXt and Vision Transformer representations. Despite these favorable conditions, Transformer branches consistently remain 13-15 mAP below the ConvNeXt backbone, and paired per-query bootstrap analysis estimates the largest observed fusion gain to be only +0.11 mAP (95% confidence interval). Our results suggest that, under the evaluated setting, improving a single strong foundation-model backbone together with retrieval-stage re-ranking is more effective than increasing architectural complexity through additional branches or heterogeneous backbones. We restrict our conclusions to single-seed training and one family of foundation models and discuss conditions under which these observations may not hold.

---


### 98. [ReCowGnition: A Realistic Biometric Benchmark for Cow Face Recognition](https://arxiv.org/abs/2607.22071)

**<font color=#1a73e8>作者：</font>** Marco Huber, Marco Kiesewalter, Judith Louise Pieper 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the development of precision livestock farming and the advances in computer vision, visual animal biometrics has gained attention. Using biometric technologies that have been proven effective for humans to identify livestock can increase animal welfare as well as production efficiency. However, challenges such as complex scenarios, similar appearances, occlusions, and non-cooperative behavior, as well as the limited amount of publicly available labeled datasets, remain. In this work, we contribute a novel, publicly available cow face benchmark dataset that has been collected in a realistic automatic scenario with 6,838 images of 161 different cows at a dairy farm. In addition to the public dataset, we define two verification and four identification evaluation protocols to foster comparable research in the cow recognition research field. Further, we provide evaluation results on our dataset of six benchmark models, which include models trained on limited data, cross-species fine-tuned models, and zero-shot foundation model approaches.

---


### 99. [Alleviating Regional Shortcuts for Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2607.22072)

**<font color=#1a73e8>作者：</font>** Haichen Zhou, Yazhe Lyu, Yixiong Zou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot class-incremental learning (FSCIL) aims to incrementally learn novel classes with only a few samples while avoiding forgetting base classes. However, current methods show a tendency to misclassify novel-class samples into base classes, which we find to be caused by the excessive focus on base-class-discriminative regions on novel-class samples. In this work, we aim to explore the underlying mechanism for an interpretation and solution. We first provide a compositional view to analyze the transferred and reused spatial patterns on novel-class samples. Then, through extensive experiments and theoretical analysis, we identify both empirically and theoretically that a shortcut exists in the model's base-class training, which naturally forms the excessive focus on only the most discriminative regions (primitives), which we term as the regional shortcut. Finally, based on this interpretation, to address this problem, we propose a compositional-learning-based method to learn two primitive sets (a common set and a discriminative set), which alleviates the regional shortcut by constraining the model to learn and utilize the common primitive set for base- and novel-class recognition. Extensive experiments on standard FSCIL benchmarks demonstrate the effectiveness of our approach, yielding consistent improvements over existing state-of-the-art methods in both accuracy and interpretability.

---


### 100. [FSE: Continual Learning for Named Entity Recognition by Fast-Slow Experts](https://arxiv.org/abs/2607.22075)

**<font color=#1a73e8>作者：</font>** Yunan Zhang, Yang Fan, Heng Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual Learning for Named Entity Recognition (CLNER) enable models to incrementally learn new entity types without forgetting previously acquired ones. However, existing methods suffer from catastrophic forgetting and insufficient exploitation of shared information across tasks. This paper proposes FSE, a Fast-Slow Experts enhanced span-based NER model for CLNER. The shared fast expert learns token-level links to efficiently filter out unlikely spans, while the task-specific slow expert performs span classification only on the remaining candidates. It stabilizes learning by promoting knowledge sharing across tasks and maintains plasticity by reducing learning burden at each task. A length-decay negative sampling strategy to mitigate span imbalance is also introduced. Extensive experiments on OntoNotes and FewNERD synthestic datasets demonstrate that FSE achieves state-of-the-art performance in CLNER scenarios, with effectiveness of each component, empirical evidence of faster convergence and expected functionality of both experts.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-169](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
