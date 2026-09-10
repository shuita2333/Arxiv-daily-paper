# 📦 其他研究 | 2026年09月11日

> 本类共 **176** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-176](./part-04.md)

---

### 51. [Teacher Geometry Shapes Learnability in Teacher-Student Networks](https://arxiv.org/abs/2609.09595)

**<font color=#1a73e8>作者：</font>** Kai J. Sandbrink, Flavio Martinelli, Alexander van Meegen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Teacher-student systems, in which a teacher neural network generates training labels so that a student neural network can learn to implement the same function, are widely used as an abstract setting to study learning. However, the structure of the teachers is often overlooked by assuming randomly-generated, normally-distributed parameters. This hides substantial variation in how learnable different teachers are. We formalize learnability as the success rate of converging to the global minimum, as a function of overparameterization, learning algorithm, student initialization distribution, and teacher geometry. We both identify an easy distribution that maximizes node dissimilarity and a hard distribution that minimizes it, and show that these two distributions induce markedly different success rates across a large range of settings and for different activation functions. To explain the gap, we study the loss landscape of small neural networks that contain two distinct kinds of suboptimal local minima, out-of-bounds (OOB) minima at the edge of the data distribution and interior minima within. Assuming infinite data and a fast readout layer, we analytically reduce the loss landscape of small networks to two dimensions, showing that the region of attraction of interior minima changes as a function of teacher structure. In larger networks, maximally dissimilar teachers induce more interior minima, while minimally dissimilar teachers induce more OOB minima. Motivated by these analyses, we show that differentially increasing the learning rate of the readout layer and decreasing the learning rate of the inner biases increases success rates. These findings provide an important step in narrowing the gap between the study of teacher-student networks and more structured functions that arise in practice.

---


### 52. [RouteBridge: Reliability-Routed Bidirectional Distillation Between Neural Radiance Fields and 3D Gaussian Splatting](https://arxiv.org/abs/2609.09606)

**<font color=#1a73e8>作者：</font>** YuanHang Wang, Xin Cao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural radiance fields (NeRFs) and 3D Gaussian Splatting (3DGS) encode a scene with complementary inductive biases, but existing cross-representation distillation typically fixes one representation as teacher for the entire scene. A globally fixed teacher can propagate local reconstruction errors. We present RouteBridge, a bidirectional framework that selects the teaching direction for each ray. Its reliability estimator combines photometric residuals with representation-specific geometric evidence and routes supervision from NeRF to 3DGS, from 3DGS to NeRF, or abstains. A renderer-independent interface transfers color, opacity, and normalized depth without shared features or point correspondence. On mip-NeRF 360, the NeRF and 3DGS exports reach 28.56 and 28.77 dB, respectively. The 3DGS export improves over 3DGS by 1.56 dB and over NeRF-GS by 0.45 dB while reducing LPIPS to 0.207. On static three-view DTU, RouteBridge obtains 21.12 dB. Ablations show that both adaptive routing and geometric ray targets contribute to the improvement.

---


### 53. [Marker-free eye-gaze estimation using a single image and depth from defocus](https://arxiv.org/abs/2609.09610)

**<font color=#1a73e8>作者：</font>** David Hurtubise-Martin, Feriel Fass, Djemel Ziou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a marker-free eye-gaze estimation approach using a single 2D camera, such as an integrated laptop webcam. The gaze-related features are estimated from iris localization and head pose estimated by using depth from defocus. A variational Bayesian multinomial logistic regression framework is used as mapping from the estimated features to the position of regard, based on an 8-dimensional feature vector of head-pose and iris-displacement parameters. No external marker is needed. Experiments were conducted by estimating the gaze of people watching a computer screen at different distances and compared against five existing methods. The obtained scores demonstrate the effectiveness of the proposed approach.

---


### 54. [Scalable Composition of Byzantine Agreements under Reorder Attacks](https://arxiv.org/abs/2609.09623)

**<font color=#1a73e8>作者：</font>** Jing Chen, Jin Dong, Jichen Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Byzantine agreement (BA) is a foundational building block in distributed systems, and the security analysis of BA protocols under multi-instance executions has attracted increasing attention. However, most existing adversary models focus solely on party corruption and neglect important threats posed by adversarial manipulations of communication channels in the network. Through channel attacks, messages can be reordered across multiple executions and lead to violations of the protocol's security guarantees,
In this work, we present the first adversary model that combines party corruption and channel attacks. Based on this model, we establish new security thresholds for Byzantine agreement under parallel and concurrent compositions, supported by complementary impossibility and possibility results that match each other to form a tight bound. For the impossibility result, we show that even authenticated Byzantine agreement protocols cannot be secure under parallel composition when $n \leq 3t$ or $n \leq 2c + 2t + 1$, where $t$ and $c$ denote the number of corrupted parties and communication channels, respectively, and $n$ is the number of parties.
For the possibility result, we prove the existence of secure protocols for unauthenticated Byzantine agreement under parallel and concurrent composition, when $n > \max\{3t, 2c+2t+1\}$. We first provide general black-box compilers that transform any single-instance secure BA protocol into one that is secure under parallel and concurrent executions without additional security assumptions. To optimize performance, we further design refined compilers using erasure-correcting codes. These refined versions significantly reduce communication overhead, particularly for long messages, where they achieve a constant multiplicative overhead compared with the original protocol, thus achieving the same asymptotic communication complexity.

---


### 55. [Hyperbolic Geometry for Open-World Object Detection in Remote Sensing Imagery](https://arxiv.org/abs/2609.09626)

**<font color=#1a73e8>作者：</font>** Wuzhou Li, Jiawei Zhou, Shenghang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-world object detection (OWOD) extends closed-set detection by requiring models to identify unknown objects and incrementally learn them once annotations become available. In remote sensing imagery, object categories often exhibit latent hierarchical relationships that may be inadequately represented in the Euclidean spaces commonly adopted by existing methods, limiting unknown-object recall and incremental-learning performance. To address this issue, we investigate hyperbolic geometry for OWOD in remote sensing imagery and propose HyRS-OWOD. To improve unknown object recall, we design a two-step unknown-object discovery mechanism: a Decoupled Objectness Learning (DOL) module that disentangles foreground perception from semantic information to separate foreground proposals from background regions, followed by a Hyperbolic Uncertainty Learning (HUL) component that leverages the radius of hyperbolic embeddings as an uncertainty-aware cue for known-unknown discrimination. For incremental learning, we develop a Hyperbolic Metric Learning (HML) strategy that enhances inter-class separability, facilitating the incorporation of novel categories while mitigating catastrophic forgetting. Experiments on three remote sensing benchmarks demonstrate consistent improvements in unknown recall and incremental learning over state-of-the-art OWOD methods.

---


### 56. [Seven Sources of Physical AI Capability Formation](https://arxiv.org/abs/2609.09627)

**<font color=#1a73e8>作者：</font>** Gang Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Capabilities relevant to Physical AI can arise from materially different formation histories, yet existing taxonomies organized by morphology, architecture, learning algorithm, task, or domain do not directly answer what gives rise to a capability. We define a capability-formation source as a factor materially contributing to capability formation, distinct from components or construction steps. We identify seven non-exclusive sources: Recorded-Experience (RE), Predictive-Modeling (PM), Evaluative-Interaction (EI), Surrogate-Environment (SE), Mechanism-Grounded (MG), Embodied-Coupling (EC), and Evolution-Driven (ED) Formation. Using reconstructive induction with theoretical saturation, we traced a research matrix to primary studies, deduplicated the literature, set coding rules, and conducted three rounds of maximum-difference and negative-case sampling. Challenges included curriculum and self-supervised learning, active inference, open-ended and developmental learning, planning and search, neuro-symbolic architectures, digital twins, generative physical world models, and morphology-control co-design. Within the scope and criteria fixed as of September 4, 2026, all 49 evidence records were explainable by the seven sources individually or in combination. No R1-R3 challenge produced an irreducible eighth source, and R3 required no new core definition or substantive boundary rule. We therefore claim theoretical saturation within the stated scope, not logical completeness or exhaustive future coverage. The framework distinguishes similarity in observed capability from similarity in how it was formed, supporting analysis of explanation, transfer, replication, dependencies, governance evidence, and geoeconomic foundations.

---


### 57. [LightMedSeg-ISLES: Stroke Lesion Segmentation with 81x Fewer Parameters than nnU-Net](https://arxiv.org/abs/2609.09634)

**<font color=#1a73e8>作者：</font>** Giorgi Nikvashvili, Hanxue Gu, Jie Bao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large networks and ensembles often lead medical image segmentation challenges, but their storage and inference demands complicate deployment. We present LightMedSeg-ISLES, a 1.26-million-parameter pipeline for T1-weighted stroke lesion segmentation in ISLES'26. On a 146-case held-out cohort, flip test-time augmentation produces 0.618 mean Dice and 0.599 lesion-wise F1. A 102.35-million-parameter nnU-Net ResEnc-L produces 0.634 Dice and 0.544 lesion-wise F1 after size filtering. LightMedSeg therefore retains 97.5\% of nnU-Net's Dice with 81.4$\times$ fewer parameters while improving lesion-wise F1 by 0.055. Its four-pass TTA operating point requires 4.7$\times$ fewer FLOPs per standardized patch than nnU-Net. It also slightly exceeds filtered UNETR++ and nnFormer. Longer training and stronger augmentation add 0.0358 Dice without increasing capacity, establishing a strong single-checkpoint alternative to much larger models.

---


### 58. [Cascading Gradient Inversion via LT-Code Inspired Peeling in Federated Learning](https://arxiv.org/abs/2609.09659)

**<font color=#1a73e8>作者：</font>** Saeed Shariati, Mohsen Alambardar Meybodi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning shares model updates rather than raw data, yet these updates can be inverted to reconstruct the clients' training data. Analytic reconstruction attacks, which invert a gradient in closed form, degrade as the batch grows: prior single-round attacks recover only about half of a batch of size $100$ even when the attacker fully controls the network parameters, and known upper bounds limit what any such method can recover. We establish a connection between gradient inversion and the theory of erasure-correcting codes, and use it to construct attacks that exceed these bounds. Our attacks recover batches exactly, together with every sample's label, from a single FedSGD round, and certify each recovery without ground-truth data. On eight image and tabular benchmarks they outperform prior single-round attacks by a wide margin. Even a passive attacker who only observes an honestly trained network recovers $94$--$100\%$ of ImageNet batches at sizes up to $128$, more than prior single-round attacks achieve even with active manipulation of the model, and in the active setting more than $90\%$ is recovered at batch sizes of several hundred. These results show that the privacy leakage of federated learning has been underestimated.

---


### 59. [Session Attestation for Unmodified TLS Services in Confidential Virtual Machines](https://arxiv.org/abs/2609.09668)

**<font color=#1a73e8>作者：</font>** Qi Gu, Sheng Ma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Confidential virtual machines simplify the migration of existing services into trusted execution environments, yet attesting their network connections often requires changing applications, TLS implementations, or certificates. We present SessionLatch, which provides session attestation while preserving all three. The key insight is that a trusted observation of the server's locally generated ephemeral public key, combined with standard TLS key confirmation, establishes the TEE endpoint guarantee without accessing TLS secrets. This moves attestation integration to the operating system: a temporary latch holds client encrypted records while evidence exchange overlaps the application TLS handshake, then removes itself after verification. The resulting connection retains enterprise service authentication and the native TLS data path, with no additional payload encryption. Mutual attestation uses the same construction and overlaps evidence generation at both endpoints. We implement Linux andWindowsintegrationandevaluaterealHygonCSVattestation. SessionLatch reduces short-upload mean latency by 63.1%/23.0% relative to TNG in interleaved Linux/Windows experiments. These results show that session attestation can strengthen existing confidential services without making a permanent proxy part of their data path.

---


### 60. [Recovering Biomechanical Signals from Missing Keypoints Using Temporal Interpolation in Monocular Gait Analysis](https://arxiv.org/abs/2609.09670)

**<font color=#1a73e8>作者：</font>** Shubham Jariwala  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular pose estimation enables low-cost gait analysis but is sensitive to missing keypoints caused by occlusion, detection errors, or efficiency-driven model reduction. While prior work on recovering missing joints focuses on complex learned models, the effectiveness of simple temporal methods remains underexplored. We evaluate knee-angle estimation under a missing-ankle-keypoint condition and test a first-order temporal interpolation scheme as a recovery mechanism. Across 527 frames of monocular walking video (428 with valid baseline detections), removing the ankle keypoint increased mean angular error to 23.4° +/- 46.7° and collapsed signal variance to near zero. Temporal interpolation reduced error to 1.1° +/- 6.7° and restored variance and smoothness to within a few percent of baseline. These results indicate that gait signals possess sufficient temporal redundancy for a simple, computationally trivial interpolation scheme to recover a critical missing joint, without resorting to learned reconstruction models. The findings support low-complexity, real-time-compatible designs for gait analysis in resource-constrained or occlusion-prone monocular settings.

---


### 61. [Muon-C: Operator-Aligned Muon for Convolutional Kernels](https://arxiv.org/abs/2609.09676)

**<font color=#1a73e8>作者：</font>** Jiaxin Qing, Lexin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon replaces matrix momentum with an approximately orthogonal polar direction, but its geometry depends on the matrix representation. For convolution, standard unfolding describes a local patch map rather than the convolution operator. We introduce Muon-C, an operator-aligned optimizer that represents kernel momentum as frequency-wise channel-transfer matrices, polarizes these blocks independently, and uses a critical Fourier grid to return updates exactly to the original finite kernel support. We show that the new geometry arises from combining the block partition and Fourier coordinates. The exact-polar direction is a linear minimization oracle under the critically sampled convolution norm. Its worst-case guarantee relative to the continuous convolution-operator norm is never weaker than unfolding and is strictly stronger for $3\times3$ kernels. On CIFAR-10 flow matching with matched applied-update RMS, Muon-C reaches 9.87 FID at 40k iterations, compared with 22.26 for unfolded Muon and 51.31 for Adam. It reaches their final quality using $0.62\times$ and $0.64\times$ their model FLOPs, respectively. Under equal tuning budgets, Muon-C achieves 3.42 FID. Gains persist across data scales and transfer to classification across convolutional architectures.

---


### 62. [Safe to Stop? Risk-Constrained Stopping for Sequential Clinical Diagnosis Agents](https://arxiv.org/abs/2609.09678)

**<font color=#1a73e8>作者：</font>** Yuexin Wu, Vasile Rus  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical diagnosis agents must decide not only what test to request next, but also when to diagnose or defer. Existing agent benchmarks largely evaluate accuracy after fixed or unconstrained interaction, leaving autonomous stopping reliability implicit. We present Cros, a risk-constrained stopping layer combining state-wise error ranking, policy design on disjoint development splits, and LTT-style exact tests of selective diagnostic error and minimum autonomous coverage for complete sequential policies. Its finite-sample guarantee requires the candidate family, testing rule, and any randomization to be frozen before calibration labels are accessed. On a 1,834-episode MIMIC-derived abdominal-pain benchmark, the full ranker achieves exploratory state-error AUROC 0.853, compared with 0.715 for maximum class probability and 0.552 for the backbone's native stop score. On the previously viewed 367-episode evaluation split, analytically averaging over the frozen Cros weights yields 16.9% selective error at 78.8% coverage, cost 5.57, and 0.68 tests, versus 30.8% error at 100% coverage, cost 8.14, and 1.53 tests under native stopping. Forced continuation is non-monotone: error is 28.3% with HPI alone and 34.3% after full workup. However, the uniform-weight mixture ablation is cheaper on this viewed split despite missing the locked development margins, and Cros nominally satisfies the joint criterion in only 6 of 20 development resplits. Because evaluation labels were inspected during earlier development, these findings provide exploratory feasibility and audit evidence, not a confirmatory safety certificate.

---


### 63. [Settling: Equilibrium Inference for Non-Convex Validity Sets](https://arxiv.org/abs/2609.09682)

**<font color=#1a73e8>作者：</font>** Lyes Saad Saoud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many learning systems return a single point estimate even when admissible outputs form disconnected or non-convex sets. Under squared loss, an ambiguous conditional distribution can therefore have a Bayes-optimal conditional mean that is invalid. We formalize this failure as conditional mean collapse and introduce Settling, an equilibrium-based inference operator that separates proposal generation, consistency evaluation, and test-time equilibrium selection. The operator treats a mean-seeking proposal as an initialization and refines it toward a locally stable configuration; conditional on initialization, refinement is deterministic. We establish exact-gradient descent, local convergence, and an inexact-gradient robustness condition relevant to learned consistency critics. In a reproducible 100-context geometric diagnostic, the mean-seeking baseline succeeds in 0/100 contexts, stochastic denoising in 100/100, and Settling in 99/100 while producing substantially lower trajectory roughness. A 1,200-run sensitivity study yields 97-100% success across obstacle-jitter ranges up to 0.20 and 94-100% across one-time initialization perturbations from 0.05 to 0.50. Cross-domain panels remain mechanism illustrations; learned high-dimensional validation remains an open empirical test.

---


### 64. [Which Medical Questions Deserve Rationales? Perturbation-Sensitive Selection for Robust QA](https://arxiv.org/abs/2609.09684)

**<font color=#1a73e8>作者：</font>** Yuexin Wu, Dayou Yu, Vasile Rus  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical question-answering datasets often contain answer labels, whereas high-quality rationales remain scarce, noisy, or costly to validate. This changes the acquisition question: rather than asking which questions should be labeled, we ask which already-labeled questions should receive rationale supervision under a fixed token budget. We study an offline version of this problem in which candidate rationales are visible to the selector but withheld from downstream training unless selected. We propose root-mean-square Robustness-based Sample Prioritization (RMS-RSP), which perturbs hidden states only at rationale tokens and measures the resulting shift in the gold-versus-best-distractor margin. Across five medical QA datasets, MedGemma-4B-IT, three training seeds, ten budgeted non-RSP selectors, and an unbudgeted full-supervision reference, RMS-RSP provides a deliberately qualified result. Its locked-budget accuracy is 60.61% on average versus 60.08% for Random, with a statistically resolved gain only on AfriMed-QA (+1.44 points). Its full-budget accuracy area is not better than Random. However, after three answer-option reorderings, RMS-RSP improves robust accuracy and semantic consistency by 1.91 and 2.85 points on average, respectively, with the same direction on all five datasets. Training on every pool rationale raises macro accuracy to 63.74%, but consumes 29--254 times more rationale tokens and does not uniformly improve robustness. These findings do not establish universal accuracy gains; they instead suggest that rationale-local boundary sensitivity can identify supervision that improves invariance to semantically equivalent formatting changes.

---


### 65. [ALIGN-HOLD: Experience Alignment for Real-Time Hold Control in Large-Scale Ride-Hailing Matching at DiDi](https://arxiv.org/abs/2609.09685)

**<font color=#1a73e8>作者：</font>** Zuhao Zhang, Xu Liu, Kai Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time hold control is a high-leverage mechanism in large-scale ride-hailing systems: by selectively deferring driver-order pairs, the platform can wait for better matching opportunities and improve end-to-end passenger-driver experience. Existing production systems such as EXHOLD learn bandit-based hold policies from handcrafted combinations of trip completion, cancellations, waiting time, and driver effort. However, designing such rewards becomes increasingly difficult as marketplace preferences are heterogeneous and observed passenger-driver behavior can be sparse, noisy, and affected by dynamic supply-demand conditions.
We present ALIGN-HOLD, a production-scale experience alignment framework that learns hold policy from implicit marketplace preferences. ALIGN-HOLD constructs complementary preference pairs from order trajectories, driver trajectories, and contemporaneous local matching graphs, and trains an experience Reward Model (RM) using balanced multi-view sampling and model-adaptive hard preference sampling. During simulator-based policy learning, the frozen RM provides a dense, context-dependent reward and supports label-free filtering of low-identifiability interactions whose behavioral feedback is difficult to attribute to matching quality.
We deploy ALIGN-HOLD on DiDi's ride-hailing platform and evaluate it in a 28-day randomized A/B experiment, covering approximately 100,000 passenger requests per day. Compared with the deployed production policy, ALIGN-HOLD achieves statistically significant improvements in trip completion rate and driver income, while significantly reducing passenger cancellations before and after driver acceptance. Complementary ablations, RM diagnostics, and behavioral analyses validate the contributions of the proposed components. ALIGN-HOLD has been fully ramped up and is currently serving DiDi's Brazil marketplace.

---


### 66. [Kernel-Complexity Edge Sanitization for Training-Free Defense against Structural Graph Attacks](https://arxiv.org/abs/2609.09698)

**<font color=#1a73e8>作者：</font>** Yaning Jia, Shenyang Deng, Yaoqing Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have achieved remarkable success across diverse applications, yet they remain highly vulnerable to adversarial attacks that maliciously perturb graph structure. Existing defenses often lack rigorous theoretical grounding, rely on attack-specific heuristics, or require costly retraining procedures such as adversarial training. To address these limitations, we propose Kernel-Complexity Edge Sanitization (KCES), a training-free and model-agnostic framework for defending against structural attacks. KCES is built upon Graph Kernel Complexity (GKC), a principled metric derived from the graph Gram matrix that appears in a generalization upper bound on the GNN test error. From this bound, we define an edge-specific KC score that quantifies each edge's structural influence via its induced change in GKC. KCES then identifies and prunes high-KC edges, which are empirically enriched with adversarial perturbations under structural attacks, to mitigate their harmful impact. Computationally efficient and scalable, KCES operates as a lightweight preprocessing step without retraining and can be seamlessly integrated with existing defenses. Extensive experiments demonstrate that KCES consistently outperforms representative robust baselines across diverse attack settings and scales effectively to large graphs. Supported by theoretical analysis and extensive empirical validation, KCES provides a principled and efficient framework for securing GNNs. Our code is available at this https URL.

---


### 67. [AppetiteCheck: Feasibility of Momentary Vagus Nerve Stimulation as an Implicit Intervention for Eating Behavior](https://arxiv.org/abs/2609.09700)

**<font color=#1a73e8>作者：</font>** Tan Gemicioglu, Jas Brooks, Pedro Lopes 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Overeating and emotional eating are common health issues that affect people even without an eating disorder. The vagus nerve plays a critical role in the gut-brain axis, and implanted vagus nerve stimulators have been associated with reduced appetite. In this paper, we propose transcutaneous cervical vagus nerve stimulation (tcVNS) as a ubiquitous system to provide immediate, low-effort intervention during an eating episode. In a study with 24 participants, we evaluated a mobile, handheld tcVNS device during a single episode of distracted snacking. We found that participants ate 9.6% less and 23.6% more slowly during vagus nerve stimulation than during sham stimulation. Post-snacking satiety was the same in both conditions, while heart rate was lower during vagus nerve stimulation. The stimulation was described as subtle and barely noticeable. Overall, these results provide evidence for the feasibility of non-invasive vagus nerve stimulation as a low-attention intervention for managing eating behavior -- one that can be packaged inside ubiquitous interactive systems. As such, we extend the design space of implicit interfaces toward physiological intervention, motivating future ubiquitous systems that pair eating-related sensing with low-attention interventions.

---


### 68. [Decision Shifts, Lost Label Functionality, and an Inconclusive Grounding Audit in Correctness-Gated Multi-Teacher Distillation](https://arxiv.org/abs/2609.09702)

**<font color=#1a73e8>作者：</font>** Xiaofei Feng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Candidate decision correctness and rationale grounding are different objectives. We examine correctness-gated multi-teacher distillation in a fixed experiment. Eight arms share 4,330 sources, a 63.9M-parameter student, 12,990 optimization rows, 406 updates, evidence inputs, and a decoder; seven teacher-based arms use one fixed three-response pool. Three seeds are evaluated on 267 held-out examples. Relative to unfiltered distillation, the correctness-weighted arm differed in accuracy by +0.1660 (95% observed-matrix interval [0.0670, 0.2455]), five-label macro-F1 by +0.1323 ([0.0916, 0.1731]), and task-defined conditional unsafe-action rate by -0.4979 ([-0.5926, -0.3686]). These shifts do not imply uniformly better behavior. Source-label SFT had the highest mean macro-F1 (0.586). The weighted arm had zero Refuted recall in every seed, and two seeds assigned NotEnoughInfo to all 167 claim examples. In an availability-amended audit at one reference seed, weighted and unfiltered outputs had 0/20 versus 1/20 evidence-supported positives and 20/20 versus 19/20 positives containing unsupported material. Samples were non-paired, source overlap was not serialized, and the amendment followed automatic summarization but preceded annotation. The audit therefore cannot estimate a common-source grounding effect and is inconclusive about system-level improvement or harm. Hard filtering already achieved 0.660 accuracy, 0.530 macro-F1, and 0.135 conditional unsafe rate. The implemented weighted arm showed no demonstrated incremental decision benefit over hard filtering. This fixed-matrix failure analysis shows decision redistribution with lost label functionality; the available human audit does not establish a grounding gain.

---


### 69. [Cross-Species Animal Re-Identification with Semantic Consistency Learning](https://arxiv.org/abs/2609.09705)

**<font color=#1a73e8>作者：</font>** Shuoyi Chen, Yuejia Li, Mang Ye  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalizable animal Re-Identification (ReID) aims to recognize individual animals across species with diverse morphologies and ecological contexts. Unlike person ReID, where different domains share similar body structures, animal species often exhibit drastically different anatomical structures and visual patterns, making it difficult to establish shared visual correspondences. As a result, representations learned across species tend to form fragmented embedding spaces, which severely limits cross-species generalization. To address this challenge, we propose Semantic Consistency Learning (SCL), a framework designed to learn representations that remain stable across appearance variations while preserving semantic structures shared across species. SCL consists of two complementary components. Foreground-Background Decoupled Spectral Normalization (FDSNorm) stabilizes feature statistics by suppressing environment-induced style variations in a region-aware manner, while Cross-species Neighborhood Modeling (CNM) captures transferable relational structures across species through dynamic feature neighborhoods. Extensive experiments on 11 public animal ReID datasets demonstrate that SCL consistently outperforms state-of-the-art methods under multiple cross-species evaluation protocols and generalizes effectively to previously unseen species and ecological domains. Code is available at this https URL.

---


### 70. [VFNet: Multi-View Spatio-Temporal Model for Void Fraction Estimation in Gas-Liquid Two-Phase Flow](https://arxiv.org/abs/2609.09711)

**<font color=#1a73e8>作者：</font>** Md Adnan Faisal Hossain, Raghav Rajeev, Kumar Nishant 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Void fraction, which quantifies the proportion of the fluid flow volume occupied by the gas phase, is a key parameter in the characterization of gas-liquid two-phase flow. Existing estimation methods either rely on flow assumptions that do not generalize across different fluids or on intrusive sensing that disturbs the flow behavior. We propose VFNet, a dual-branch spatio-temporal neural network for void-fraction prediction from synchronized multi-view videos of two-phase flow. A local branch extracts features from confined spatial regions and fuses the synchronized dual views, while a spatio-temporal branch captures the global evolution of the flow across space and time to refine a coarse geometric estimate. Trained on simulated computational fluid dynamics (CFD) data with known ground-truth void fractions and evaluated against both learning-based and traditional baselines, VFNet achieves the best performance across a broad range of metrics and also improves downstream flow-pattern classification on real two-phase flow data.

---


### 71. [How Far Do Capability Cues Travel? Anthropomorphism and Differentiated Trust in a Platform-Embedded AI Assistant](https://arxiv.org/abs/2609.09713)

**<font color=#1a73e8>作者：</font>** Chenchen Mao, Hanjing Shi, Haiyan Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visible AI capabilities need not translate into broader judgments of trustworthiness. In a randomized 2 x 2 experiment with 270 U.S.-based Reddit users, an embedded assistant displayed one or three functions, with or without a brief rationale. Displaying three functions increased perceived multifunctionality; no other randomized main effect survived correction across the six outcomes. Rationale availability did not reliably increase perceived intelligence. Exploratory analysis indicated stronger uptake of the functional display at higher objective AI literacy. Among concurrently measured judgments, perceived multifunctionality was associated with perceived intelligence, which was associated with anthropomorphism and all three trust dimensions. After accounting for perceived intelligence, anthropomorphism was positively associated with benevolence, but not reliably with integrity or ability. These findings separate interface effects from relationships among users' perceptions and show why ability, integrity, and benevolence should be evaluated separately.

---


### 72. [EEGBind: Detecting Source-Level Interictal Epileptiform Discharges via EEG-Centric Multimodal Binding](https://arxiv.org/abs/2609.09728)

**<font color=#1a73e8>作者：</font>** Muchen Li, Anglin Liu, Xuetian Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Source-level analysis of interictal epileptiform discharges (IEDs) is relevant to presurgical evaluation and treatment planning because it helps characterize where epileptiform activity is likely to arise. Beyond detecting whether an IED is present, this setting requires assigning IED-positive activity to clinically meaningful brain-region categories. This setting is challenging because source-region evidence in short electroencephalography (EEG) windows can be subtle, partial, and affected by subject variability, class imbalance, and imperfect multimodal context. We present EEGBind, an EEG-centric multimodal binding framework for five-class source-level IED classification. EEGBind treats EEG as the primary modality and binds synchronized video-context features around an EEG-centric representation. Instead of relying on early or overly strong multimodal fusion, which may perturb the source-sensitive EEG representation, EEGBind uses video context as auxiliary evidence for robust classification. A view-consistent repair stage is further used to improve hidden-set robustness while preserving the learned source-class boundary. On the NeuroMM 2026 Grand Challenge Track 3 NMM-Source-IED benchmark, EEGBind achieves 0.8395 on weighted-F1 and outperforms strong competitors. These results support EEG-centric multimodal binding as a practical strategy for source-level IED classification. The open-source code is available at this https URL.

---


### 73. [Can Artificial Intelligence Support Healthcare and Mental Health Through Early Cyberbullying Detection ? The Impact of Emotion-Aware AI on Proactive Online Safety](https://arxiv.org/abs/2609.09735)

**<font color=#1a73e8>作者：</font>** Hamed Jelodar, Amir Firouzi, Yen-Wu Lo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare systems, mental health, and public well-being are increasingly affected by cyberbullying and harmful online interactions. This paper presents CareGuard, an early-warning framework designed to support healthcare-driven mental health protection and proactive online safety through the detection of cyberbullying-related content using advanced natural language processing techniques. CareGuard integrates zero-shot semantic labeling with fine-tuned transformer-based models, including BERT, DistilBERT, and RoBERTa, to enable robust and context-aware classification across sensitive cyberbullying categories. To improve efficiency and reduce unnecessary computation in healthcare-oriented monitoring settings, the framework incorporates an emotion-aware filtering mechanism alongside cosine similarity-based semantic screening, allowing the system to focus on semantically relevant and emotionally salient content. Experimental results on benchmark datasets demonstrate that CareGuard effectively balances detection accuracy and computational efficiency, highlighting its potential for scalable deployment in healthcare systems, mental health monitoring, and online safety applications.

---


### 74. [IAE-VTG: Interaction-Aligned Action-Entity Video Temporal Grounding](https://arxiv.org/abs/2609.09736)

**<font color=#1a73e8>作者：</font>** Shiwen Zhao, Qi Zhang, Sezer Karaoglu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Temporal Grounding (VTG) localizes the video segment that matches a natural-language query. Many queries describe an action performed by a particular entity. Existing methods often encode the query as a whole or use general video-text interactions, without explicitly checking whether the action and entity occur together. They may therefore select a segment that contains both concepts but not the event described by the query. We propose Interaction Aligned Action-Entity Video Temporal Grounding (IAE-VTG), which models this rela?tionship at both the representation and training assignment levels. First, the Fine-grained Disentangled Interaction Module (FDIM) separates action and entity related query information and aligns it with complementary motion and appearance features. It then combines token-level interactions to build representations that capture the relationship between the action and entity. Second, Interaction-Sensitive Assignment (ISA) adds this interaction evidence to bipartite matching, so training targets are selected using both temporal overlap and semantic compatibility. This reduces supervision from temporally plausible but semantically incorrect proposals. Experiments on QVHighlights, Charades?STA, and TACoS show that IAE-VTG consistently improves strong baselines and achieves competitive or state-of-the-art performance on standard grounding metrics. Additional analyses show that the method is especially effective when similar actions or entities appear at multiple times and produces more reliable assignments for complex events.

---


### 75. [Distilling Image Prototypes for Guided Test-Time Adaptation](https://arxiv.org/abs/2609.09737)

**<font color=#1a73e8>作者：</font>** Liwen Wang, Xingbo Dong, Iman Yi Liao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-Time Adaptation (TTA) enhances the robustness of models against distribution shifts but faces two critical challenges: error accumulation from noisy pseudo-labels and catastrophic forgetting of source knowledge. Uncertainty-based approaches designed to mitigate error accumulation often yield overconfident or computationally expensive estimates, while strategies intended to prevent forgetting via prototype replay rely on static representations that easily become misaligned as the model adapts. To address these issues, this paper proposes a novel framework, Distilling Image Prototype for Guided Test-Time Adaptation (DIPTTA). The core of the proposed approach is the introduction of a Distill Image Prototype (DIP), a compact set of synthetic images that serves as a dynamic and regenerative anchor of source knowledge. This prototype enables a dynamic feature replay mechanism that continuously generates feature prototypes aligned with the current state of the model, thus effectively preventing catastrophic forgetting. Furthermore, the DIP anchors a source-calibrated uncertainty estimation method, which provides a less biased measure of sample reliability by leveraging stable source knowledge, thereby robustly suppressing error accumulation. Extensive experiments on multiple benchmarks demonstrate that DIPTTA significantly outperforms state-of-the-art methods, particularly under severe domain shifts. The source code is available at this https URL.

---


### 76. [MethaneFuse: Learning from Multi-Sensor Satellite Observations for Methane Plume Detection](https://arxiv.org/abs/2609.09762)

**<font color=#1a73e8>作者：</font>** Yuyao Wang, Juliana Y. Leung, Di Niu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Methane plume detection from satellite imagery is constrained by incomplete observations: public satellites provide complementary spatial, spectral, and atmospheric evidence, but real plume cases rarely contain fully paired multi-sensor measurements because of revisit schedules, cloud coverage, acquisition quality, and the transient nature of emissions. Most learning-based detectors rely on single-sensor inputs, especially Sentinel-2 (S2), leaving many reported plume cases unusable.
We construct MethaneUnion, a temporal multi-sensor dataset built from Carbon Mapper plume reports and matched S2, Landsat 8/9 (L8/9), EMIT, and Sentinel-5P (S5P) observations. Built on MethaneUnion, MethaneFuse learns from heterogeneous satellite observations under partial sensor availability without requiring complete four-sensor measurements.
MethaneUnion expands usable coverage from 3,211 valid S2-matched plume cases to 8,981 reported plume cases with multi-sensor observations. At the representative 480 m setting, MethaneFuse achieves 84.87 F1 and 93.62 AUROC, improving over the strongest baseline by 5.65 F1 and 8.30 AUROC points while reducing false positives by 8.19 points. Sensor-availability experiments show that MethaneFuse improves detection when S2 is available and transfers plume knowledge to L8/9, EMIT, and S5P when S2 is unavailable. These results demonstrate the value of learning from incomplete heterogeneous sensor observations for practical methane plume detection.

---


### 77. [SymbolicLight V2: Hybrid Neuromorphic Architecture and Sparse Execution for Low-Energy Language Inference](https://arxiv.org/abs/2609.09772)

**<font color=#1a73e8>作者：</font>** Ting Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> SymbolicLight V2 combines sparse event computation with continuous-state processing in a hybrid neuromorphic language architecture. Extending V1's spike-gated dual paths, it adds graded signed events at further projections and softmax-free local attention. We implement the 194M-parameter model on an Alveo U50C FPGA using digital fixed-point arithmetic and on an ARM CPU using sparse integer execution. Across three same-checkpoint FPGA implementations at 175 MHz, active-row weight gathering and valid-state KV loading raise decode throughput from 474.6 to 643.2 tokens/s for a 32-token prefix and 128 outputs. Estimated gross card energy falls from 0.06087 to 0.04407 J per generated token, a 27.6% reduction. Complete-request energy, including prefill, falls by 24.4-27.7% across three prefix lengths. An independent idle split attributes 82.8% of gross card energy to loaded idle, explaining the benefit of shorter token latency. Against the recorded RTX 5090 compiled-FP32 baseline, integer FPGA execution uses 89.1% less estimated card energy during short-context decode; arithmetic precisions differ, and the GPU baseline is not the lowest-energy tested configuration. On four Cortex-A76 cores of a ROCK 5T, complete requests reach 65.4 tokens/s at 9.80 W and 0.151 J per generated token at the adapter's AC input. These results connect event sparsity to omitted computation and data movement. The mechanisms also support other dedicated V2 implementations: increasing throughput by a greater factor than active power lowers energy per generated token. Evaluation holds the deployed checkpoint fixed; its quality trails a same-budget dense control, so the results do not establish equal-quality efficiency.

---


### 78. [NEXUS-MI: Communication-Aware Federated Personalization for Gateway-Coordinated Motor-Imagery Brain-Computer Interfaces](https://arxiv.org/abs/2609.09786)

**<font color=#1a73e8>作者：</font>** Daniel Adu Worae, Aarthy Nagarajan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG)-based motor-imagery brain-computer interfaces (MI-BCIs) vary across subjects and sessions, complicating personalization from limited calibration data. Federated learning can exploit shared representations without centralizing raw EEG, but existing federated MI studies largely assume regular synchronization. We introduce NEXUS-MI, a gateway-coordinated federated personalization framework that treats synchronization as a coupled learning-and-communication control problem. Raw EEG and classifier heads remain local, while an edge coordinator maintains the shared backbone. We evaluate NEXUS-MI through offline replay using BCI Competition IV Dataset 2a (BCICIV-2a; 9 subjects, 4 classes) and OpenBMI (54 subjects, 2 classes). Session 1 supports backbone learning, and Session 2 provides limited-calibration personalization and held-out testing. An ideal-link reference and six heterogeneous-link policies characterize gateway participation, buffering, stale-update admission, and backbone-download control. The principal comparison holds delayed-update handling fixed while contrasting non-adaptive and communication-aware synchronization. Paired subject-level comparisons use Holm adjustment, and robustness across five matched realizations is assessed by hierarchical bootstrap. Communication-aware coordination reduced server-to-client backbone traffic by approximately 42% on both datasets, while cohort-level accuracy differences were small and realization-dependent. Cohort averages also concealed subject-level vulnerability, with losses reaching approximately 12 percentage points on BCICIV-2a relative to the ideal-link reference. These findings establish gateway synchronization as an explicit design variable in federated MI personalization and motivate joint evaluation of personalized accuracy, communication cost, update freshness, and subject-level reliability.

---


### 79. [Evaluating Model Retraining under Drift: Paired Comparisons of Cumulative Subgroup Disparity](https://arxiv.org/abs/2609.09788)

**<font color=#1a73e8>作者：</font>** Aaron Ceross  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Choosing when to retrain a deployed classifier requires assessing subgroup error rates across the sequence of models used, including periods between updates. We compare complete scheduled, loss-triggered, and subgroup-gap-triggered policies with retaining the initial model on the same observations and delayed labels. For true-positive and false-positive rates separately, the outcome is the paired difference in absolute subgroup gaps summed over deployment windows. Population evaluation in simulation, action records, and alternative schedules assess how measurement and retraining behaviour affect these comparisons. In a follow-up sample of 400 new trajectories per condition across two simulated drift regimes, all three policies had lower mean cumulative disparity, equivalent to reductions of 0.04 to 0.88 percentage points in the average gap per window. Evaluating the unchanged models against the known generating distributions preserved all mean directions, but finite-window and population comparisons agreed on whether updating increased, reduced or left cumulative disparity unchanged in 69 to 92 percent of trajectories. Under subgroup-specific drift, smaller true-positive-rate gaps accompanied lower sensitivity in both groups. In an exploratory American Community Survey replay, person weighting reversed all three race false-positive-rate mean comparisons without changing predictions or actions; all three weighted intervals included zero. Policy comparisons require group-specific rates, action distributions, and an explicit evaluation population alongside mean disparity. These analyses are non-confirmatory. Shared replay requires policy-independent observations and complete labels after the specified delay.

---


### 80. [Pairit: A Platform for Live Experiments on Human-AI Collaboration](https://arxiv.org/abs/2609.09789)

**<font color=#1a73e8>作者：</font>** Harang Ju, Sinan Aral  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Organizational design in the era of artificial intelligence requires experimental methods that can test how human-AI groups coordinate, delegate, and make decisions. Programmable platforms coordinate live human-to-human sessions or real-time human-AI chat, but researchers cannot easily declare experiment protocols in which AI participants both communicate and act on shared work within one auditable configuration. Here we introduce Pairit, an online platform that facilitates the design, testing, and deployment of experiments that test human-AI organizational designs and interventions. Through a single YAML configuration file, researchers declare an executable experiment graph (pages, routing, randomization, matchmaking, chat, shared workspaces, server-hosted agents, surveys, timers, and custom HTML components) and combine any number of humans and AI agents in live sessions. We have validated the feasibility of the platform through multiple live deployments, including peer-reviewed published studies, capturing high-resolution process traces of communication, negotiation, and collaborative work in live human-AI dyads. By representing complex interactive protocols as standardized, auditable configuration files, Pairit provides reusable infrastructure for specifying, deploying, and sharing live human-AI organizational experiments.

---


### 81. [A practical DIRECT-type algorithm for medium-scale black-box global optimization](https://arxiv.org/abs/2609.09796)

**<font color=#1a73e8>作者：</font>** Linas Stripinis, Remigijus Paulavičius  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The DIRECT algorithm is a deterministic global optimization method known for its versatility and balanced exploration-exploitation strategy. However, DIRECT-type algorithms are primarily effective for low-dimensional problems and often exhibit slow convergence as dimensionality increases, limiting their applicability to more complex optimization tasks. To address this limitation, this paper introduces X-DTC-GL, a novel DIRECT-type algorithm that incorporates dynamic partitioning and hybridization techniques. The dynamic partitioning approach adaptively refines the search space based on local one-dimensional surrogate models, enabling rapid subdivision of promising hyper-rectangles. The hybridization strategy selectively employs a hill-climbing method to exploit promising regions identified by the surrogate models. Extensive experiments on four diverse benchmark suites demonstrate that X-DTC-GL significantly outperforms existing DIRECT-type baselines, achieving improvements of ~12% in solvability and ~27% in solution quality. Performance-profile analyses indicate the fastest convergence on up to ~40% of instances, the best runtime performance on ~17% of problems, and competitive overall execution times. By improving performance within the partition-based framework, these advances strengthen the algorithm's competitiveness in state-of-the-art black-box optimization.

---


### 82. [Quantifying IIoT Sensor Node Criticality by Fusing its Data Criticality and Security Vulnerability](https://arxiv.org/abs/2609.09807)

**<font color=#1a73e8>作者：</font>** Sachin K. Sen, Gour C. Karmakar, Shaoning Pang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of the Industrial Internet of Things (IIoT) into manufacturing has transformed industrial operations by optimising production management and ensuring product quality through smart industrial sensors that regulate processes based on real-time data. However, these sensor nodes are highly vulnerable to cyber threats, posing significant security risks that compromise their reliability and integrity. While existing research explores cybersecurity vulnerabilities and cyberattack-based methods for ranking critical nodes, some studies assess node criticality based on the impact of sensor data on product quality. However, a comprehensive approach that integrates both data criticality and cybersecurity vulnerability remains unexplored. To bridge this gap, this study introduces a novel framework that evaluates IIoT sensor node criticality by leveraging Dempster--Shafer (D-S) theory to fuse data criticality and cybersecurity vulnerabilities. The proposed method is validated using a dataset from red wine production, demonstrating its effectiveness in ranking sensor nodes based on both factors. The results show that criticality rankings based on security vulnerability scores computed using CVSS version 4.0 differ significantly from those obtained with CVSS version 3.1, highlighting the influence of enhanced vulnerability assessment methodologies. While initially applied to wine manufacturing, this framework is adaptable to broader industrial applications with minimal modifications, offering a robust approach to securing IIoT-enabled production systems.

---


### 83. [Online Inverse Integer Linear Optimization via Small-Gradient Skipping: Constant Regret and Finite Mistakes](https://arxiv.org/abs/2609.09809)

**<font color=#1a73e8>作者：</font>** Akira Kitaoka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In online inverse linear optimization, the learner predicts a weight at each round, observes the optimal action of the agent, and updates its prediction. In the general setting, the gap of $\log T$ between the regret upper bound $O(d \log T)$ and the lower bound $\Omega(d)$ is unresolved (here $T$ is the total number of rounds and $d$ is the dimension). When the action set is M-convex, the regret is known to be bounded by $O(d \log d)$, but the method attaining it computes a center of gravity at every round. This paper therefore proposes Small-Gradient Skipping (SGS), a mechanism that skips the update at rounds without a mistake in the case where the correct action is uniformly separated from the other candidates, and applies it to online gradient descent, the online Newton step, and MetaGrad. The number of mistakes is then bounded, for all three, by a quantity independent of $T$; and for the online Newton step and for MetaGrad with SGS, the dimension dependence of the regret becomes $O(d^2)$ when the forward problem is an integer linear program, that is, the factor $\log T$ is removed. Moreover, when the action set is M-convex, the regret is bounded efficiently without computing a center of gravity.

---


### 84. [Lightweight Zero Trust via Automotive SDN](https://arxiv.org/abs/2609.09817)

**<font color=#1a73e8>作者：</font>** Friedrich Wiemer, Florian Wagner  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zonal in-vehicle networks ship Ethernet, MACsec, and TSN, but treat the network itself as trusted: once configured at the factory, there is no standardized runtime way to easily revoke access, rotate keys, or contain a compromised ECU. Zero Trust Architecture targets exactly that gap, yet existing automotive ZTA proposals bolt on dedicated infrastructure that duplicates the SDN management plane already required to enable SDVs. Thus, ZTA is not yet adopted in the automotive domain, and the question remains: can we do better? We answer this in two steps.
Step 1 analyses what Open Alliance TC17~v1.0 MACsec/MKA with pre-shared CAKs already provides in terms of NIST SP~800-207 ZTA tenets. Step 2 adds CORECONF/YANG management as proposed in Open Alliance TC19, maps the SDN Controller and Agents one-to-one onto NIST's PE, PA, and PEP. We then instantiate this with two YANG-based mechanisms: a network-access-control flow and a key-management scheme.
The result fully covers five and two partially of the seven tenets with no ZTA-specific infrastructure added.

---


### 85. [In Medical Claims Data, Enhancing Predictive Performance for Major Adverse Cardiovascular Events Using Cross Attention](https://arxiv.org/abs/2609.09824)

**<font color=#1a73e8>作者：</font>** Yuhei Fujioka, Daitaro Misawa, Tatsuyoshi Ikenoue 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical claims data comprise the financial details, including the expenses and billing information, as well as the clinical information, such as the diagnoses and treatments, of patients visiting medical facilities. Recently, it has been acknowledged that large databases can be constructed from medical claims data for medical research purposes. However, the clinical information within these datasets is often medically unstructured, limiting its application in comprehensive analyses. This study enhances predictive model performance for major adverse cardiovascular events (MACE), a leading cause of death worldwide. Models that predict MACE are crucial to clinical practice guidelines. We utilize a cross-attention mechanism to develop a method that effectively weights the relationships between diagnoses and treatments. Effectively repre- senting the clinical information contained in medical claims data, this approach generates more representative features for predicting MACE. The ROC-AUC score of our proposed cross-attention-based model was 0.7720, higher than other benchmark models including the conventional atherosclerotic cardiovascular disease model, the light gradient boosting machine, and a self-attention-based model. These results indicate that integrating the clinical structure of medical claims data using a cross-attention mechanism significantly enhances the performance of predictive models.

---


### 86. [Freezing of Gait Prediction Under Spatial Occlusion: An IMU-Supervised Cross-Modal Distillation Approach](https://arxiv.org/abs/2609.09826)

**<font color=#1a73e8>作者：</font>** Chandan Biswas, Aryan Singh, Anabik Pal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parkinson's disease is a progressive neurodegenerative disorder characterised by gradual deterioration of movement control. Automated freezing-of-gait (FOG) detection supports the objective assessment of gait-related motor impairment. Two common approaches are used for FOG prediction: (i) analysing video recordings of the patient's movements and (ii) analysing data collected using inertial measurement unit (IMU) wearable sensors attached to the patient's lower limbs. Video-based approaches may suffer detection errors during continuous turning-in-place tasks because the lower limbs undergo substantial geometric self-occlusion, degrading pose-estimation accuracy. IMU-based approaches are generally less affected by visual occlusion; however, they are difficult to deploy outside clinical or laboratory settings, as the sensors must be attached securely and remain in place throughout the assessment. Motivated by this, we propose a cross-modal subspace distillation framework to mitigate the limitations of unimodal FOG detection by combining IMU accuracy with video-based practicality. We extract invariant latent topologies from a pre-trained kinematic oracle to structurally supervise a non-encoded visual architecture during training. To resolve periods of severe spatial occlusion, a dual-stream visual model probabilistically fuses skeletal graph nodes and continuous spatial pixels, dynamically shifting reliance to uninterrupted pixel boundaries as joint tracking confidence drops. Evaluated against a public, multi-modal sequence dataset of Parkinson's individuals executing continuous $360^\circ$ turns, empirical results demonstrate that applying sensory boundary topologies strictly mitigates tracking evaluation entropy. Our constrained optimisation confirms that highly precise FOG prediction bounds can be achieved over zero-wearable inference environments.

---


### 87. [Layerwise Tunable Lifting Scheme for the Convolutional Neural Network](https://arxiv.org/abs/2609.09827)

**<font color=#1a73e8>作者：</font>** Abdumannon Yovkochov, An Le, Sungbal Seo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work introduces a family of tunable lifting schemes for biorthogonal wavelet filter banks. We propose three lifting strategies: low-pass tuning (LS-LayLatt-LP), high-pass tuning (LS-LayLatt-HP), and a sequential lifting scheme that jointly adapts low- and high-frequency branches (LS-LayLatt-Sequential). All proposed designs are formulated using a lattice-based lifting structure, which guarantees invertibility and stability for arbitrary parameter values within the lifting functions. We evaluated the proposed methods by integrating them into a ResNet-18 backbone for image classification on the Describable Textures Dataset (DTD), as well as for anomaly detection on hazelnut images from the MVTec-AD dataset and private KRC102S dataset. Experimental results demonstrate consistent performance improvements across all evaluated tasks.

---


### 88. [SkNeXt enables topology-guided neuronal reconstruction from petabyte-scale microscopy data](https://arxiv.org/abs/2609.09832)

**<font color=#1a73e8>作者：</font>** Jiayi Ding, Hu Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in high-resolution fluorescence and electron microscopy have enabled nanoscale imaging across increasingly large brain volumes, but the resulting terabyte- to petabyte-scale datasets make complete neuronal reconstruction prohibitively expensive in computation, data movement, and manual proofreading. Here, we present SkNeXt, a topology-first framework for scalable neuronal reconstruction from large volumetric microscopy datasets. Instead of densely processing entire image volumes, SkNeXt first converts neuronal morphology into compact SWC skeletons that preserve long-range connectivity. Proofreading is therefore focused on sparse neuronal trees, allowing branch, continuity, and connectivity errors to be corrected before high-resolution reconstruction. The corrected skeletons then serve as persistent structural priors for recovering detailed morphology while preserving neuronal identity and topology. Crucially, SkNeXt also uses neuronal skeletons as spatial indices for selective data access, retrieving high-resolution image regions only along reconstructed trajectories and bypassing most background and signal-free volumes. This substantially reduces I/O and computational overhead, allowing reconstruction cost to scale with neuronal morphology rather than total dataset size. Using SkNeXt, we reconstructed neurons from a petabyte-scale super-resolution fluorescence dataset of the mouse brain on a single GPU within one week, without requiring exhaustive dense inference across the complete imaging volume.

---


### 89. [TempTPI: Informer-Based trajectory prediction for maritime vessels](https://arxiv.org/abs/2609.09840)

**<font color=#1a73e8>作者：</font>** Kevin Ferneding, Veronika Lietavcova, Aleksandra M. Blachowiak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate long-term trajectory prediction for maritime vessels is essential for safety and logistical efficiency. While deep learning models, particularly Transformers, have shown promise in processing Automatic Identification System (AIS) data, they often struggle with the quadratic computational complexity of self-attention and the loss of accuracy over extended forecasting horizons. This study proposes TempTPI, a novel prediction framework that integrates an Informer-based encoder with a multi-channel temporal encoding mechanism. The Informer architecture leverages a ProbSparse self-attention mechanism to reduce computational overhead and focus on the most significant dependencies, while the temporal encoder utilizes Fourier-like frequency expansions to capture cyclic patterns (hourly, daily, and seasonal) in vessel behavior. We evaluate our model against the state-of-the-art TPTrans architecture using AIS data from Danish waters. Experimental results demonstrate that TempTPI consistently outperforms existing methods across prediction windows of 1 to 5 hours. Notably, at a 5-hour horizon, the proposed model achieves a 55% improvement in Mean Squared Error (MSE), offering a robust solution for long-range maritime situational awareness.

---


### 90. [Subgroup Membership Inference Audits of Differentially Private Synthetic Text](https://arxiv.org/abs/2609.09848)

**<font color=#1a73e8>作者：</font>** Yidan Sun, Viktor Schlegel, Srinivasan Nandakumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Synthetic data releases are increasingly proposed in the literature as a means of sharing realistic data replicas in lieu of sensitive private datasets. Even when the worst-case privacy leakage of such releases is bounded by means of differential privacy (DP), in practice a residual risk remains. Membership inference attack (MIA) audits are conducted to empirically quantify this risk. However, existing methods only measure average-case risk for randomly drawn records, which might conceal the risk to vulnerable subgroups. To highlight this issue, we define a subgroup-targeted membership inference game in which the target pool is an explicit parameter, and instantiate it with an audit of 32 proxies under three scenarios with different levels of attacker knowledge, across four datasets, three generators (DP-SGD fine-tuning, API-based prompting, and activation steering), and five privacy budgets. The audit shows that synthetic releases leak subgroup membership and that prior attacks systematically underestimate this leakage. DP is effective at the aggregate level: it substantially reduces average leakage at every budget we test. Three observations temper this picture. First, the remaining leakage is concentrated rather than spread out: under DP, a tenth of the records carries roughly 40% of it. Second, the protection DP delivers in practice is uneven: within its worst-case guarantee, the noise removes more of the measured leakage from random records than from high-risk ones---and a merged-pool audit that scores both record types against shared negatives confirms this at the record level. Third, \emph{which} records leak proves to be a property of the release mechanism rather than of the record alone, so record-level risk cannot be assessed independently of the release.

---


### 91. [Pretraining and Distillation Matter More Than Architecture Family for Label-Free Single-Cell Classification](https://arxiv.org/abs/2609.09863)

**<font color=#1a73e8>作者：</font>** Philip Graemer, Giuseppe Di Caprio  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Choosing a deep learning architecture for label-free single-cell classification remains an open question, with microscopy benchmarks reporting conflicting conclusions about CNNs versus transformers. We present a controlled benchmark on LIVECell phase-contrast microscopy data using source-image-disjoint train/validation/test splits to prevent parent-image leakage and matched optimisation, augmentation, and evaluation protocols across EfficientNet, Vision Transformer (ViT), and EVA-02 models. This allows the effects of architecture, pretraining, fine-tuning, tokenisation, and distillation to be disentangled. We find that the previously reported CNN advantage is largely explained by pretraining rather than architecture: the smallest pretrained model outperforms the strongest model trained from scratch despite far fewer parameters. Pretraining improves macro-F1 by 3-4 points, while the gap between the best pretrained CNN and transformer is below 0.5 points. Architectural choices nevertheless matter: ViT-S/8 outperforms ViT-S/16 and matches the four-times-larger ViT-B/16 at a quarter of the parameters, showing that finer tokenisation benefits small cell crops. Conversely, layer-wise learning-rate decay, central to the EVA-02 fine-tuning recipe, degrades performance, highlighting that transfer heuristics from natural-image recognition may not generalise to microscopy. Finally, knowledge distillation substantially improves the deployment frontier: compact EfficientNet-B0 students distilled from teacher councils outperform every individually trained backbone, including the EfficientNet-B5 and EVA-02 teachers. Overall, our results show that rigorous control of pretraining and evaluation is essential for interpreting biomedical architecture benchmarks, while distillation may be a more effective route to practical single-cell classification than architecture choice alone.

---


### 92. [Shifting Relational Paradigms for Affective Computing: Affective Resonance, Vitality Affects, and Vocal Interaction Fields](https://arxiv.org/abs/2609.09864)

**<font color=#1a73e8>作者：</font>** Cy Gorman, Yihang Yao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Affective computing has largely followed an individual-state paradigm, extracting discrete emotion labels or arousal/valence from isolated speakers. We argue this framing is incomplete for interaction. Drawing on affective resonance and vitality-contour accounts, we propose a relational framework in which the primary unit of affective analysis is the interactional field constituted within vocal dynamics. As a proof of concept, we present a preliminary empirical study using continuous self-supervised speech representations to detect directional expressive coupling in multi-party conversation. Coupling is regime-specific, concentrated at sub-second timescales, and collapses under exclusive-speech negative controls, consistent with a relational account of affective dynamics. We introduce design frameworks for Artificial Affective Resonance Intelligence grounded in Affective Resonance Dynamic Ontologies, supported by null-calibrated directional coupling analyses across interaction regimes.

---


### 93. [CLFTv2: Efficient Camera-LiDAR Fusion for Semantic Segmentation via Hierarchical Feature Pyramids](https://arxiv.org/abs/2609.09881)

**<font color=#1a73e8>作者：</font>** Toomas Tahves, Mauro Bellone, Raivo Sell  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation for autonomous driving requires reliable detection of vulnerable road users (VRUs) despite heavy class imbalance. We introduce CLFTv2, a hierarchical camera-LiDAR fusion framework replacing global ViT attention with a Swin-based multi-scale encoder and a lightweight FPN-style residual decoder. Operating in the 2D perspective domain, CLFTv2 integrates multi-scale geometric cues through shifted-window attention and per-scale residual fusion, avoiding the computational overhead of query-matching decoders. Across three driving datasets, CLFTv2 consistently improves VRU recall. On ZOD, CLFTv2-Large achieves 53.5\% mIoU, improving pedestrian IoU from 35.5\% to 44.9\% over the prior CLFT model. On Waymo, CLFTv2 reaches 61.7\% mIoU. Additionally, a modality-isolation study suggests ViT's global receptive field yields stronger fusion gains only under dense LiDAR returns. Compared to a Swin-based Mask2Former adaptation, CLFTv2 requires 1.4$\times$ fewer GFLOPs and delivers 2.2$\times$ higher throughput, while achieving comparable overall accuracy. These results demonstrate that hierarchical local-attention fusion offers an efficient, scalable alternative to global-attention and query-based decoders for real-time on-vehicle perception in intelligent transportation systems. Source code is publicly available.

---


### 94. [Albedo Estimation via Latent Bridge Matching](https://arxiv.org/abs/2609.09884)

**<font color=#1a73e8>作者：</font>** Carme Corbi, David Serrano-Lozano, Javier Vazquez-Corral 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Intrinsic Image Decomposition (IID) have increasingly relied on generative models. However, progress remains limited by three key challenges: (a) insufficient physical consistency, (b) high computational cost at inference time, and (c) limited generalization capabilities. In this work, we show that latent bridge matching (LBM) effectively addresses these limitations for albedo estimation. We introduce a novel LBM-based architecture that enforces physical consistency through a pixel reconstruction loss, benefits from the inherent efficiency of LBM low-cost inference, and improves generalization across diverse datasets by incorporating a shading conditioning. In this extended version, we additionally show that conditioning the shading estimator itself on the predicted albedo further improves reconstruction fidelity, and we benchmark our best model against stateof-the-art IID methods across five real and synthetic datasets.

---


### 95. [Decision Transformer for UAV-Mounted RIS-Assisted Dynamic D2D Communications](https://arxiv.org/abs/2609.09885)

**<font color=#1a73e8>作者：</font>** Yaxuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper studies unmanned aerial vehicle (UAV)-mouted reconfigurable intelligent surface (RIS)-assisted device-to-device (D2D) communication with stochastic link activation. It models UAV motion and attitude, time-varying Rician angles, and angle-dependent RIS reflection. A joint optimization of UAV trajectory, attitude, and RIS phases is formulated to maximize average sum rate under mobility, energy, and hardware constraints. The problem is addressed using deep reinforcement learning and a Decision Transformer trained on expert trajectories from multiple scenarios. Results demonstrate effective cross-scenario generalization, with zero-shot transfer outperforming direct DRL transfer and online fine-tuning achieving competitive performance with fewer interactions.

---


### 96. [StreetDiff: Multi-view Street Scenes Generation via Cross-view Consistent Multi-view Stable Diffusion with Structure Prompts](https://arxiv.org/abs/2609.09890)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Yanyifan Wang, Weiyuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view diffusion models have shown strong performance in scenes with strong geometric priors and sparse semantics, such as indoor rooms or simple outdoor environments (e.g., fields, courtyards). However, they often fail to maintain cross-view consistency under camera rotation, especially in structurally complex urban environments. Without explicit modeling of spherical correspondence across views, existing approaches tend to produce object duplication, structural distortion, and layout inconsistency. To address this limitation, we propose StreetDiff, a multi-view diffusion framework that explicitly enforces cross-view alignment during denoising. StreetDiff introduces a Panorama--Perspective Synergy design to decouple global layout reasoning from local detail synthesis, and incorporates a Panorama Alignment Module (PAM) that establishes spherical-projection-based attention constraints across views. By injecting structured alignment constraints without modifying the diffusion backbone, our framework achieves robust cross-view coherence in challenging urban street scene generation tasks. In addition, we construct Street360, a large-scale HDR multi-view urban panorama dataset. Extensive experiments demonstrate that StreetDiff significantly improves structural consistency and visual fidelity compared to prior multi-view diffusion generation methods.

---


### 97. [ProMeta: Few-shot PROTAC-targeted degradation prediction across E3 ligases](https://arxiv.org/abs/2609.09891)

**<font color=#1a73e8>作者：</font>** Yuansheng Liu, Yufei Ye, Tao Tang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proteolysis-targeting chimeras (PROTACs) have emerged as a transformative therapeutic strategy that selectively degrades historically ''undruggable'' targets via the ubiquitin-proteasome system. Despite growing efforts to develop computational predictors of PROTAC degradation activity, existing supervised approaches remain severely challenged by data scarcity and imbalance across E3 ligases, limiting their ability to generalize beyond well-studied ligase contexts. In practice, labeled data are heavily concentrated on a few ligases (e.g., CRBN and VHL), while the majority of E3 ligases remain underexplored yet are critical for expanding the design space of targeted degraders. Developing methods that enable robust cross-ligase generalization with minimal labeled data is therefore essential for improving the practical utility of computational PROTAC discovery. We reformulate PROTAC degradation activity prediction across E3 ligases as a few-shot meta-learning problem and present ProMeta, a prototype-based graph neural network trained through episodic meta-learning on source-E3 tasks and evaluated on held-out target-E3 tasks through support-conditioned inference. ProMeta performs inference without updating the encoder by dynamically estimating class prototypes from minimal target-ligase support samples. On the CRBN-to-VHL benchmark, ProMeta achieves AUROC values of 0.796 under K=2, Q=3 and 0.883 under K=2, Q=5, improving by 19.9% and 6.8%, respectively, over the corresponding supervised GNN baseline. Reverse VHL-to-CRBN transfer under the same protocol yielded AUROC values of 0.702 (K=2, Q=3) and 0.821 (K=2, Q=5), confirming bidirectional applicability while revealing direction and data-regime dependence. Together, these results support ProMeta as a practical framework for cross-ligase few-shot prediction under the evaluated support/query protocols.

---


### 98. [Contrastive Projection: Reading Transformer Internals by Differencing Logit Lenses](https://arxiv.org/abs/2609.09902)

**<font color=#1a73e8>作者：</font>** Olli Tuomi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reading a transformer's internal states in token space is easy to do and hard to trust: a logit lens on a single hidden state is dominated, at intermediate layers, by the generic tokens the model would predict for almost any input. We read the difference instead. Subtracting two closely matched prompts' hidden states and projecting through the unembedding cancels the shared component and surfaces what separates them, an operation equivalent to reading a RepE/ActAdd steering vector through a logit lens. Built into a training-free tracer that reads at every position, sub-layer, and head and averages over designed baselines, it traces a compound- noun MLP->attention chain in Phi-2, confirmed there by activation patching, with the same distinction recovered across three architectures by readout and probe rather than by patching; it reads what retrieval surfaces for real versus fictional entities, and reads metaphor as a set of domain-to-domain mappings rather than a single figurativity feature. A cross-seed control marks the boundary: across five networks differing only in initialization, the same distinction surfaces as almost entirely different tokens (top-10 overlap 0.08). What a computation looks like in token space is network-specific; the distinction it draws is not

---


### 99. [Beyond Conventional Federated Learning via High-Order Regularization](https://arxiv.org/abs/2609.09904)

**<font color=#1a73e8>作者：</font>** Alireza Kabgani, Masoud Ahookhosh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated clients that perform several local optimization steps can return parameter displacements with widely different magnitudes. The quadratic regularization of FedProx grows linearly with displacement and therefore offers limited control over the contrast between ordinary and unusually large client movements. We here introduce HiFedProx, which replaces the quadratic penalty with a scale-matched power-type regularizer indexed by $p\geq2$. All powers have the same regularization-gradient magnitude at a reference displacement $R$, while every $p>2$ gives a weaker response below $R$ and a stronger response above it. An exact affine reference calculation shows that increasing $p$ compresses relative displacement disparities, although very large powers approach fixed-radius behavior and increase local curvature. HiFedProx combines this geometry with finite-budget stochastic client optimization and same-minibatch Armijo backtracking. In paired five-seed experiments on a frozen 60-writer FEMNIST subset, a common-parameter study over $p\in\{2,3,4,5,6,7,8\}$ shows similar clean-training performance but substantial gains under composite stress. The lowest moderate- and severe-stress losses occur at $p=7$ and $p=6$, improving over $p=2$ by $11.44\%$ and $23.16\%$, respectively. Although displacement-tail ratios continue to decrease through $p=8$, predictive performance peaks in an intermediate range and Armijo trial cost increases with $p$. These results indicate that the exponent should be calibrated rather than maximized. In our experiments, $p=5$--$7$ provides the most useful range.

---


### 100. [Meta-LinEXP3: Online-within-Online Learning for Adversarial Linear Contextual Bandits](https://arxiv.org/abs/2609.09907)

**<font color=#1a73e8>作者：</font>** Hao Li, Jie Xu, Zheng Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Meta-learning has emerged as an effective paradigm for transferring knowledge across sequential bandit tasks. While substantial progress has been made for stochastic bandits and non-contextual adversarial bandits, meta-learning for adversarial linear contextual bandits (ALCBs) with random action sets remains largely unexplored. To address this problem, we propose Meta-LinEXP3, an online-within-online algorithm that constructs a predictable task-level prior from completed tasks to guide the inner LinEXP3 learner. For known context distributions, we develop a policy-centered estimator that achieves an intrinsic-dimension $\mathcal{O}(\sqrt{n})$ per-task regret bound. For unknown distributions, we introduce a past-only regularized moment estimator with an $\mathcal{O}(n^{2/3})$ leading regret term and explicit finite-sample error. We further establish a direct connection between prior accuracy and transfer regret, showing that increasingly accurate priors yield sublinear transfer-dependent regret across tasks. Experiments demonstrate the effectiveness of Meta-LinEXP3, including its application to structured hyperspectral tensor sampling.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-176](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
