# 📦 其他研究 | 2026年06月24日

> 本类共 **654** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

---

### 401. [Imagine to Ensure Safety in Hierarchical Reinforcement Learning](https://arxiv.org/abs/2606.22509)

**<font color=#1a73e8>作者：</font>** Gregory Gorbov, Artem Latyshev, Aleksandr I. Panov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work investigates the safe exploration problem in reinforcement learning, where an agent must maximize cumulative performance while simultaneously satisfying safety constraints. This challenge becomes even more pronounced in long-horizon tasks, where existing safe methods face fundamental limitations due to compounding estimation errors and restricted exploration capabilities. To address this problem, we propose a method that combines a learnable world model with two complementary policies a high-level policy and a low-level policy to promote safety at both hierarchical levels. The high-level policy generates intermediate subgoals that bias exploration toward safe regions, while the low-level policy uses imagined rollouts in the learned world model to reduce unsafe behaviors when reaching these subgoals. The proposed method was evaluated on challenging long-horizon navigation and manipulation tasks with high-dimensional action spaces, where it significantly outperforms existing Safe RL baselines in both success rate and strong empirical constraint satisfaction, consistently meeting the prescribed safety budget across seeds, while prior approaches fail to effectively solve these complex long-horizon scenarios.

---


### 402. [Fed-CausalDiff: Decoupled Synchronization for Federated Do-Simulation and Policy Evaluation](https://arxiv.org/abs/2606.22510)

**<font color=#1a73e8>作者：</font>** Pengfei Li, Mohammad Khalil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While federated learning enables collaborative modelling on decentralised data, standard methods merely fit historical observations. This purely observational approach is fundamentally insufficient for interventional inference and policy evaluation, as sequential actions dynamically alter future states. We propose \textbf{Fed-CausalDiff}, a federated causal diffusion framework for do-simulation. The architecture decomposes the evolution of the latent state into a global causal score function and a local confounding score function. This design enables \emph{decoupled synchronisation} (DSS), where clients aggregate only the shared causal mechanism while retaining site-specific confounders locally to handle heterogeneity. Experiments on four datasets demonstrate that Fed-CausalDiff achieves better ATE and policy-value estimation accuracy, offering a favorable trade-off between communication cost and inference fidelity.

---


### 403. [Biological Sex Determination in Cadavers Using Deep Learning Algorithms from Computed Tomography Images of Pelvis and Skull](https://arxiv.org/abs/2606.22515)

**<font color=#1a73e8>作者：</font>** Giovanna Herculano Tormena, Davi Nascimento Araújo, Germano Coimbra Soares de Carvalho 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sexual identification of decomposed cadavers challenges traditional methods dependent on visual anthropological analysis. This study evaluates state-of-the-art deep learning (including YOLO26, YOLO11, ConvNeXt-Tiny, EfficientNetV2, ViT-B16, VGG16, and ResNet50) with transfer learning to automatically determine biological sex from forensic computed tomography (CT) scans. We analyzed 141 autopsied cadavers from the Forensic Medical Institute of Goiânia-GO, including a broad age range and varying conditions of preservation. The three-dimensional reconstructions of the pelvis and skull were converted into standardized two-dimensional profile projections, contributing to the study of this new technical approach. Data augmentation techniques compensated for sample limitations. Two scenarios were validated: binary and quaternary classification (one class per sex vs. one class per anatomical region of each sex). The best-performing model achieved highly consistent results on the pelvis region and still satisfactory performance on the skull region, reaching an overall patient-level accuracy of 95.65%, recall of 92.86%, F1- score of 94.36%, and precision of 97.22%, maintaining consistent performance across the evaluated cases, including those with trauma-related artifacts. Results indicate the technical feasibility of the methodology, demonstrating that deep learning models can provide objective, high-speed skeletal analysis. Since the study was conducted using data from a single institution and a single computed tomography scanner, further validation across multiple centers and scanners is required to assess the generalizability of the proposed approach

---


### 404. [The Scissors Effect: When Resize-Based Input Diversity Helps or Hurts Transfer Attacks](https://arxiv.org/abs/2606.22516)

**<font color=#1a73e8>作者：</font>** Yuhang Jiang, Xiaojing Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Input Diversity (DI), which applies random resizing and padding at each attack iteration, is a near-default ingredient of transfer-based adversarial attacks, widely assumed to improve transferability. We show this assumption is regime-dependent and, for robustly trained surrogates, often reversed. Varying only the surrogate, increasing the DI probability raises transfer success for standard surrogates but lowers it for robust ones: the two response curves separate like a pair of scissors, a pattern we call the Scissors Effect. The effect is strong and consistent on ImageNet, where blind DI costs the robust source 10.3% attack success on average across CNN, ViT, Swin, and ConvNeXt targets and across ten attacks spanning 2018-2024; it is smaller on CIFAR-10 unless DI is made aggressive. A controlled robustness-strength sweep that varies only the training budget shows the harm is graded rather than binary, crossing from beneficial to harmful already in the little-robustness regime. We trace it to gradient geometry: a resize/translation decomposition attributes roughly 67% of the harm to resize, and a direct source-target gradient-alignment measurement confirms the same resize operation improves alignment for standard surrogates but degrades it for robust ones. We summarize the regime with Local Gradient Consistency (LGC), a single input-space probe that separates the two surrogate types, and prove a bias-variance crossover theorem isolating where DI helps from where its resize bias dominates. A training-free rule (CG-DI) that disables diversity when LGC is high avoids the loss on robust surrogates while keeping DI's benefit on standard ones, positioning the Scissors Effect as a DI-specific manifestation of the broader robustness-transferability trade-off.

---


### 405. [Detecting and Understanding Vulnerabilities in Fully Homomorphic Encryption Frameworks](https://arxiv.org/abs/2606.22519)

**<font color=#1a73e8>作者：</font>** Yiteng Peng, Dongwei Xiao, Zhibo Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) allows computations to be performed directly on encrypted data without decryption, offering strong privacy guarantees for sensitive data analysis. This capability is important for privacy-sensitive applications like secure cloud computing, finance, and healthcare. The complexity of FHE schemes, however, has hindered their practical adoption. To make FHE accessible to a broader range of developers, a new generation of specialized frameworks has emerged to translate high-level FHE programs into complex FHE operations, introducing a new programming paradigm. However, the inherent complexity of FHE frameworks makes them prone to incorrect implementation logic. Unlike mere crashes, logic bugs in these frameworks can silently corrupt encrypted computation, potentially leading to severe financial losses and security vulnerabilities in FHE-enhanced applications.
In this work, we introduce HERTA, the first automated testing tool tailored for FHE frameworks. HERTA leverages metamorphic testing to uncover deep-seated implementation bugs and vulnerabilities across the multi-layered FHE software stack. To that end, we design a set of novel metamorphic relations (MRs) derived specifically from FHE semantics. These MRs stress the most challenging aspects of the pipeline, enabling automated correctness testing without the need for a manual ground truth. Our evaluation of HERTA on 3 leading industry frameworks discovered 21 previously unknown bugs, several of which have already been confirmed and fixed by developers. Furthermore, our hazard analysis reveals the critical security impact these bugs pose to the integrity and availability of FHE-based services.

---


### 406. [Projection-Volume Fidelity Divergence: Diagnosing and Controlling Optimization Drift in Sparse-View 3D Gaussian Tomography](https://arxiv.org/abs/2606.22525)

**<font color=#1a73e8>作者：</font>** Yikuang Yuluo, Ao Wang, Shen Kuan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-view computed tomography is a severely ill-posed inverse problem, where recent 3D Gaussian Splatting methods offer an efficient explicit representation for tomographic reconstruction. However, we find that projection-domain optimization can be misleading in this setting: the rendered projections may continue to improve while the reconstructed volume deteriorates. We identify this failure mode as Projection-Volume Fidelity Divergence (PVFD), a representation-level optimization drift caused by anisotropic Gaussian deformation and view-specific primitive co-adaptation under sparse Radon constraints. To characterize this behavior, we introduce geometry- and volume-level diagnostics that measure needle-like Gaussian degeneration and the stability of the voxelized density field. Based on these observations, we propose LADES, a ground-truth-free optimization controller for sparse-view Gaussian tomography. LADES combines Linearly Annealed Dropout, which applies strong stochastic masking in early training to disrupt premature primitive co-adaptation and gradually restores full capacity for structural consolidation, with Structure-Aware Early Stopping, which terminates densification according to the saturation of Gaussian population growth rather than validation PSNR. Experiments on sparse-view CT reconstruction show that LADES improves volumetric fidelity, suppresses structural degeneration, and substantially reduces training time while maintaining competitive projection accuracy. These results suggest that robust Gaussian-based tomography requires monitoring and controlling volumetric structure, rather than optimizing projection fit alone.

---


### 407. [Trajectory Forcing: Structure-First Generation with Controllable Semantic Trajectories](https://arxiv.org/abs/2606.22527)

**<font color=#1a73e8>作者：</font>** Merve Kocabas, Gege Gao, Bernhard Schölkopf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-based generative models produce strong images, yet their controllability remains largely endpoint-centric: users specify conditions and receive final outputs, while the intermediate generative dynamics remain hidden. Recent methods have begun to exploit generation order and process decomposition to improve sample quality, but still treat intermediate states as internal computation rather than objects for interaction. We propose Trajectory Forcing (TF), a trajectory-centric framework that makes the generation path explicit, semantic, and editable. TF organizes synthesis as a sequence of semantically structured stages, progressing from global layout to object-, part-, and detail-level representations. Each stage produces a decodable latent state that can be inspected, evaluated, and locally edited before the next stage begins. To instantiate this path, we derive coarse-to-fine teacher hierarchies by clustering pretrained visual representations such as DINOv2, and train a hierarchy-conditioned one-step flow-matching model at each level. We further introduce trajectory-aware metrics that measure structural consistency and local controllability beyond endpoint quality metrics such as FID. Experiments show that TF achieves competitive sample quality while exposing coherent intermediate states and supporting localized edits across semantic levels. By shifting the focus from final images to the generative path itself, TF opens a route toward controllable, trajectory-aware image synthesis.

---


### 408. [Generative Robust Optimisation](https://arxiv.org/abs/2606.22536)

**<font color=#1a73e8>作者：</font>** Yuhui Yin, Vassilis M. Charitopoulos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical uncertainty sets for robust optimisation impose fixed geometric shapes that cannot represent the complex dependencies present in real-world data. We propose Generative Robust Optimisation (GRO), a framework in which a deep generative model defines the uncertainty set as the image of a neural network decoder over a calibrated latent set, naturally accommodating nonlinear correlations, asymmetry, and multimodality. A five-point evaluation framework (reconstruction fidelity, distribution matching, latent regularity, robust relevance, and computational tractability) provides systematic, model-agnostic criteria for assessing any neural network-based uncertainty set. We instantiate this framework with a Wasserstein Adversarial Autoencoder employing Gaussian mixture model-guided training for latent regularity and constraint-consistency regularisation for robust relevance. Restricting the decoder to ReLU activations enables exact worst-case verification through mixed-integer programming embedding. Extensive experiments on a production planning problem across six uncertainty distributions and six generative architectures, together with a multi-period facility location study, validate the framework and demonstrate that systematic attention to all five criteria yields uncertainty sets that are simultaneously expressive, well-calibrated, and optimisation-tractable.

---


### 409. [PolicyTrim: Boosting Intrinsic Policy Efficiency of Vision-Language-Action Models](https://arxiv.org/abs/2606.22540)

**<font color=#1a73e8>作者：</font>** Xianghui Wang, Feng Chen, Wenbo Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models provide a unified paradigm for robotic manipulation, yet their real-world deployment is often bottlenecked by execution efficiency. While existing efforts predominantly focus on compute-centric efficiency to reduce per-step inference latency, the intrinsic \textbf{policy efficiency} of these models remains largely unexplored. Policy efficiency is fundamentally affected by two factors, namely the effective executable length of predicted action chunks and the total physical steps required to complete a task. These two factors jointly determine the total number of forward inference calls during execution. We observe that current VLA policies struggle with planning unreliability and action redundancy, suffering from severe prediction degradation at the tail of action chunks and tending to generate unnecessarily redundant physical steps. To address this, we propose \textbf{PolicyTrim}, a reinforcement learning-based post-training framework that extends the reliable action chunk length and reduces redundant physical steps. For reliable chunk extension, we employ a dynamic exploration strategy that explicitly rewards the successful completion of longer executable lengths, progressively pushing the trustworthy prediction horizon to its empirical limit. For step efficiency, we design a redundancy-aware reward that directly favors successful task completions with fewer steps while penalizing unreproducible shortcuts, effectively eliminating redundant physical actions. Extensive experiments across three benchmarks and three VLA models demonstrate that PolicyTrim improves action chunk utilization by 3$\times$ and reduces physical execution steps by 51.4\%. Ultimately, our framework delivers up to a 5.83$\times$ end-to-end deployment speedup without compromising task success rates.

---


### 410. [MAPS: Multi-Anchor Projection Similarity for Joint Vision-Language Geo-Localization](https://arxiv.org/abs/2606.22543)

**<font color=#1a73e8>作者：</font>** Yutong Hu, Siyuan Tan, Shaocheng Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans localize places by integrating perceptual cues from vision with semantic reasoning from language, forming a scene understanding that is both intuitive and structured. Although existing geo-localization models have made substantial progress in cross-view and cross-modal settings, they are largely built upon point-to-point alignment, which is insufficient for joint vision-language queries. In such queries, visual and textual cues do not simply act as independent references, but jointly define a semantic subspace for locating the target. In this paper, we formulate vision-language geo-localization (VLGL) with joint image-text queries as a multi-anchor geometric alignment problem and propose a unified framework for this setting. To realize this formulation, we propose Multi-Anchor Projection Similarity (MAPS), a new metric which constructs an anchor plane from visual and textual query features in a high-dimensional space and measures similarity by the projection length of the target feature onto this plane. Unlike cosine similarity which evaluates isolated pairwise relations, MAPS captures the geometric consistency between the target feature and the joint query subspace, providing a more discriminative ranking criterion during retrieval. To make the learned representation consistent with this geometry, we further introduce a MAPS-based contrastive loss that drives target features toward the corresponding anchor plane. The proposed framework, similarity metric, and training objective jointly yield state-of-the-art performance in VLGL.

---


### 411. [Venice-H1: Failure-Aware Query Re-Ranking with Multi-Scale Grid Signatures for Referring Image Segmentation](https://arxiv.org/abs/2606.22546)

**<font color=#1a73e8>作者：</font>** Nicolò Savioli  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Referring Image Segmentation (RIS) systems generate multiple candidate masks per expression but rely on a simple heuristic--typically the argmax detection score--to select the final output. We identify query selection as a failure-case bottleneck: although heuristic selection succeeds on 82-93% of samples, the residual 7-18% of failures dominate the error budget, leaving a best-query selection gap of 3-11% mIoU. We introduce Venice-H1, a lightweight, backbone-decoupled post-hoc re-ranking module that encodes each candidate through multi-scale grid signatures--compact spatial descriptors pooled onto 4x4, 8x8, and 16x16 grids--and feeds them to a Transformer-based re-ranker with a Failure Gate (ROCAUC 0.78-0.82) that intervenes only when the default choice is likely suboptimal. Instantiated on DeRIS-L and DeRIS-B, Venice-H1 achieves delta_fail of +1.40 and +0.89 mIoU with strictly positive 95% CIs on all 16/16 (split, backbone) pairs and harmful-switch rates below 0.53%. Zero-shot transfer to medical referring segmentation (MS-CXR, M3D-RefSeg-2D) yields +1.16 and +0.51 mIoU without RIS-backbone fine-tuning. The module adds approximately 11.3M parameters and under 1 ms latency.

---


### 412. [Mitigating Measurement-Induced Training Instability in Hybrid Quantum Neural Networks for Protein Classification](https://arxiv.org/abs/2606.22551)

**<font color=#1a73e8>作者：</font>** Milton Mondal, Sushovan Chanda, Mohamad Mahdi Alawieh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid Quantum Neural Network (QNN) classifiers produce logits as expectation values of quantum measurement operators. For standard Pauli measurements, these outputs are intrinsically bounded to the interval [-1,1]. When such bounded logits are used directly with the cross-entropy loss applied to softmax-normalized logits for multi-class classification, the loss function operates in a regime of weak sensitivity to logit differences. As a consequence, parameter gradients are suppressed, leading to unstable optimization in variational quantum classifiers (VQCs). In this work, we identify this effect as measurement-induced logit contraction, a previously uncharacterized source of trainability degradation in hybrid QNNs. To address this limitation, we introduce a learnable scaling parameter, termed Quantum Measurement Temperature (QMT), which rescales quantum measurement outputs prior to the loss. Unlike post-hoc calibration, QMT acts during training and compensates for the physically imposed bounds on quantum measurement outputs. This rescaling increases gradient magnitude and variance, thereby improving loss sensitivity. The proposed mechanism is architecture-agnostic and does not modify the quantum ansatz, circuit depth, or measurement operators. Experiments on fluorescence microscopy images and a six-class variant of Fashion MNIST demonstrate that QMT consistently enhances logit separation, strengthens gradients, stabilizes training across random initializations, and improves classification accuracy, relative to unscaled measurement readouts. These results demonstrate that QMT enables stable and reliable training of hybrid QNNs for practical applications.

---


### 413. [HiMatch-AD: DINOv3-driven Hierarchical Matching for Training-free Medical Anomaly Detection](https://arxiv.org/abs/2606.22556)

**<font color=#1a73e8>作者：</font>** Jiayu Huo, Jingyuan Hong, Meng Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Anomaly detection is essential for medical image analysis, where pathological regions often appear as rare deviations from normal anatomical structures. While training-based methods have achieved promising performance, they require task-specific optimization and extensive normal data, which limits scalability across modalities and institutions. Training-free approaches offer greater flexibility by leveraging pretrained visual representations, yet existing methods typically rely on simple nearest-neighbor retrieval and naive aggregation strategies, which may fail to capture hierarchical semantics and ignore the reliability of multiple anomaly responses. In this work, we propose HiMatch-AD, a DINOv3-driven hierarchical matching framework for training-free medical anomaly detection. Our method first retrieves semantically relevant normal references via dual-branch matching that jointly considers global CLS-token similarity and patch-level representations. Hierarchical anomaly maps are then generated across multiple transformer stages by comparing clustered normal features with query representations. To robustly aggregate anomaly responses, we introduce a unified uncertainty-based fusion mechanism that adaptively weights maps according to their reliability. The entire framework operates without any task-specific training. Extensive experiments on the BMAD benchmark, including brain MRI, liver CT, and retinal OCT datasets, demonstrate that HiMatch-AD consistently outperforms both training-based and DINO-based state-of-the-art methods, which highlights the effectiveness of multi-level matching and uncertainty-aware fusion for scalable medical anomaly detection.

---


### 414. [MacAgentBench: Benchmarking AI Agents on Real-World macOS Desktop](https://arxiv.org/abs/2606.22557)

**<font color=#1a73e8>作者：</font>** Yikun Fu, Bowen Fu, Zhenyu Wu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer use agents (CUAs) have advanced rapidly in desktop automation, and a growing number of users deploy CUAs such as OpenClaw on Mac Mini for always-on automation. However, existing benchmarks, including those for macOS, evaluate agents without framework augmentation and rely on binary evaluation. As a result, they fail to capture both the framework capabilities leveraged by modern CUAs and the partial progress on long-horizon, multi-application tasks. We present MacAgentBench, a comprehensive macOS agent benchmark comprising 676 tasks across 25 applications, with nearly 60% involving both GUI and CLI interaction. The benchmark adopts deterministic rule-based evaluation and introduces fine-grained multi-checkpoint scoring with capability annotations for multi-application tasks. Experiments across three frameworks and 16 models show that the best configuration, Claude Opus 4.6 on OpenClaw, attains 73.7% Pass@1, while this advantage is primarily driven by the skill library rather than by framework design. Fine-grained metrics further reveal that models with similar Pass@1 can differ substantially in sub-goal completion. Our code and data are publicly available at this https URL.

---


### 415. [Concept-Constrained Prompt Learning for Few-Shot CLIP Adaptation](https://arxiv.org/abs/2606.22567)

**<font color=#1a73e8>作者：</font>** Na Sang, Ding Ma, Rui Sang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Few-shot prompt learning is an effective strategy for adapting CLIP to downstream tasks, but class-only prompt optimization can overfit base-class supervision and weaken transfer to unseen classes. We propose Concept-Constrained Prompt Learning (CCPL), a lightweight regularization framework that anchors learnable class prompts to frozen concept-level text prototypes without updating CLIP encoders. CCPL learns a set of shared context tokens, instantiates class prompts by appending class names, and constructs frozen concept prototypes from a class-level concept bank. During training, a text-space cosine consistency objective aligns learnable class-prompt embeddings with frozen concept prototypes; concept dropout provides additional regularization against over-reliance on fixed concept lists. At inference, CCPL optionally fuses class-prompt logits with concept-prototype logits using a controllable ensemble weight alpha. Our default configuration uses text-space concept regularization lambda = 0.5, concept dropout p = 0.3 and weak concept-guided fusion (alpha = 0.1), with no KL-based prediction consistency term. Experiments under identical automatically-generated fallback splits show that CCPL improves the base-to-new harmonic mean on DTD (+0.6) and EuroSAT (+2.9) compared with CoOp, while remaining near-neutral on OxfordPets (-0.1). Ablations indicate that text-space concept regularization is consistently beneficial, while the best concept-guided inference strength is dataset- and protocol-sensitive. These results suggest concept constraints are most effective when concept prototypes align naturally with dataset semantics, and identify fine-grained categories as a current boundary condition. The code is released at: this https URL.

---


### 416. [The Power of Light: Improving Synthetic-to-Real Domain Adaptation through Physically-Based Indirect Illumination](https://arxiv.org/abs/2606.22574)

**<font color=#1a73e8>作者：</font>** Hooman Tavakoli Ghinani, Tatjana Legler, Martin Ruskowski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While synthetic data generation resolves the manual labeling bottleneck in computer vision, minimizing the syn-to-real domain gap requires optimizing rendering variables. This paper presents a systematic study analyzing the impact of lighting configurations and background complexity on object detection performance. We introduce SmartSDG, an automated, reproducible pipeline built on NVIDIA Isaac Sim using Physically-Based Shading (PBS), alongside ILLUM\_INTRUCK, a new multi-object industrial benchmark dataset. Through 18 controlled experiments utilizing a state-of-the-art YOLOv12 framework, we demonstrate that complex, indirect lighting configurations paired with domain-relevant background variability significantly increase visual cue richness. Our quantitative findings show that avoiding direct specular peaks preserves crucial surface textures, mitigates the domain gap, reduces false positives, and accelerates model convergence compared to using conventional direct-light synthetic data. Ultimately, we provide actionable virtual scene design guidelines to maximize object detection robustness in industrial automation.

---


### 417. [Context-Aware Distillation and Ablation for Text2DSL](https://arxiv.org/abs/2606.22578)

**<font color=#1a73e8>作者：</font>** Alexander V. Kozachok, Alexander M. Nazimov, Shamil G. Magomedov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We extend our prior work on Text2DSL automatic generation of domain-specific language (DSL) code from natural language descriptions along two complementary axes. First, we replace prompt-only synthetic generation with context-aware distillation, in which a teacher large language model (DeepSeek-V4-Flash) operates under an explicitly defined structured context comprising a BNF grammar, an API specification, and a closed identifier vocabulary; the resulting corpus is verified by a two-tier pipeline combining AST validation through esprima and runtime acceptance through the production polkitd daemon and the pkcheck client. This scales the verified PolkitBench corpus from 4,204 to 10,073 natural-language-to-Polkit-rule pairs at 100.0% AST validity and 99.7% runtime pass rate. Second, we conduct the per-component factorial ablation of structured context that was identified as future work in the precursor study: eight conditions C0-C7 are evaluated on GigaChat-10B-A1.8B with the new corpus. Three findings emerge. (i) The new harder corpus collapses the baseline mode (Syntax Valid 97.6% -> 58.5%, Combined Score 0.482 -> 0.252), whereas the context-enhanced mode degrades only marginally (Syntax 98.6% -> 97.4%, Combined 0.801 -> 0.750), confirming that structured context is not a cosmetic improvement but a load-bearing mechanism. (ii) The best absolute condition is the full context C7 across all metrics, while the strongest partial conditions (C5 = BNF + Vocabulary, C6 = API + Vocabulary) both contain the vocabulary. (iii) A Shapley-style decomposition assigns the largest semantic-quality effect to the vocabulary (Combined +0.198), the largest structural-validity effects to API (+24.7 pp) and BNF (+22.3 pp).

---


### 418. [Stationary Robust Mean-Field Games under Model Mismatches](https://arxiv.org/abs/2606.22579)

**<font color=#1a73e8>作者：</font>** Yue Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying multi-agent reinforcement learning (MARL) in the real world is often limited by model mismatches between the training simulators and the true environment, which could be further amplified through strategic interactions and result in severe performance degradation upon deployment. Distributional robustness offers a principled response by optimizing policies against worst-case transition models drawn from an uncertainty set, but standard robust MARL frameworks become increasingly intractable as the number of agents grows. This paper develops an infinite-horizon, stationary mean-field game framework that incorporates distributional model uncertainty directly into the population-coupled dynamics. We establish a robust dynamic programming principle with a contractive Bellman operator and prove the existence of a stationary robust mean-field equilibrium via a fixed-point argument. We further develop the first concrete algorithm with convergence guarantees. We then connect the mean-field solution to a finite-population robust game whose ambiguity sets depend on the empirical distribution, showing that the mean-field equilibrium policy induces approximate equilibrium behavior as the population size increases. Under a contractive robust-dynamics regime, we further obtain explicit non-asymptotic error bounds. Numerical experiments further illustrate the qualitative and quantitative impact of robustness under multiple uncertainty models, validating our theoretical findings.

---


### 419. [From CVE to CWE: Syscall-Based HIDS Generalisation](https://arxiv.org/abs/2606.22581)

**<font color=#1a73e8>作者：</font>** Alexander V. Kozachok, Stanislav G. Vyugov, Shamil G. Magomedov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Host intrusion detection systems (HIDS) based on system-call traces are typically trained and evaluated against individual Common Vulnerabilities and Exposures (CVE) instances. In operational settings, however, defenders need to recognise new exploits of an already known type of weakness. We empirically examine whether a one-class anomaly detector trained on the normal behaviour of a set of CVEs that share a Common Weakness Enumeration (CWE) class generalises to a different, unseen CVE inside the same class. Using six scenarios drawn from LID-DS-2021 and grouped into three CWE families (CWE-307 broken authentication, CWE-89 SQL injection, CWE-434 unrestricted file upload), we extract a 66-dimensional Peng-Guo-style feature vector per sliding window and train Isolation Forest and SGD One-Class SVM detectors with normal-only thresholds calibrated to fixed target false positive rates. We define and answer four research questions covering self-detection, asymmetric cross-CVE transfer, the value of a combined CWE-level normal profile, and the effect of feature filtering on transferability. The combined CWE-307 detector reaches F1 = 0.6976 at calibration target FPR = 0.05 (precision = 0.8994, recall = 0.5698), whereas CWE-89 and CWE-434 collapse to F1 <= 0.21 under the same protocol. Cross-CVE transfer turns out to be strongly direction-dependent and dominated by the breadth of the source normal profile rather than by the CWE label. We conclude that CWE-level generalisation in HIDS is empirically attainable for some but not all weakness families with current syscall features, and we argue that calibrated FPR is a methodological prerequisite for honest reporting in this setting.

---


### 420. [Training-free Task Classification for Multi-Task Model Merging](https://arxiv.org/abs/2606.22589)

**<font color=#1a73e8>作者：</font>** Jungyong Son, Jinwook Jung, Sungyong Baik  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ever since the advent of foundation models and the pre-training-finetuning paradigm, there have been numerous efforts to merge multiple task-specific experts into a single multi-task model. Prior work largely focuses on finding a single merged model, but it often underperforms individual experts due to parameter interference. To resolve this, dynamic model merging employs routing to activate task-relevant parameters per input. However, existing routers typically require either additional training with abundant labeled datasets or assume the access to task IDs of each input at inference time. In this work, we aim to close the gap to expert performance without additional training or task-ID-access assumption. To this end, we formulate routing as training-free task classification for each test input. Using singular value decomposition (SVD)-based low-rank manifold approximations for each task, SiM scores tasks by the projection residual of the test input feature onto each task manifold and routes accordingly. The task manifolds are pre-computable offline from a pretrained backbone using a small per-task support set (e.g., 32 examples per task) prior to merging process, requiring no router training and no data during the merging process. Moreover, SiM integrates seamlessly with subspace-/mask-based merging that represents task-expert via lightweight compressed task vectors, avoiding the need to store full expert parameters. Experiments across computer vision and natural language processing benchmarks under task-unknown inference demonstrate that SiM substantially improves merged-model performance and consistently narrows the gap to individual task experts.

---


### 421. [On the Position Bias of On-Policy Distillation](https://arxiv.org/abs/2606.22600)

**<font color=#1a73e8>作者：</font>** Yan Xie, Sijie Zhu, Tiansheng Wen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-Policy Distillation (OPD) improves the learning efficiency of standard reinforcement learning through dense, token-level supervision from teachers. In the standard KL objective of OPD, token-level losses are uniformly averaged, implying equal weights for all tokens. However, we discover that not all tokens are created equal: as student rollouts grow longer, they deviate further from the teacher's distribution, leading to degraded supervision quality at later positions. As a result, OPD using only the first 30% of tokens can perform comparably to using all tokens, whereas OPD using only the last 30% of tokens barely learns anything. In this work, we provide a principled understanding of this issue through the lens of constrained optimization. Based on these insights, we derive Importance-Weighted On-Policy Distillation (IW-OPD), in which the weight assigned to each token depends on the accumulated discrepancy between the student's and teacher's distributions, naturally upweighting earlier tokens and downweighting later ones with larger deviations. We show that IW-OPD converges significantly faster than OPD, with better learning efficiency, and achieves better final performance than standard OPD in both same-size and cross-scale settings, improving performance up to 6.9 points on AIME-2025.

---


### 422. [Automated sign detection across the Electronic Babylonian Library: A large-scale dataset and end-to-end cuneiform OCR pipeline](https://arxiv.org/abs/2606.22608)

**<font color=#1a73e8>作者：</font>** Wentao Che, Esteban Garcés Arias, Asim Niaz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning to read cuneiform tablets is an extremely demanding task; consequently, of the roughly half million excavated tablets, only a small fraction has been analysed by Assyriologists. Computer vision offers a promising avenue for decipherment but requires large, densely annotated datasets. To address this limitation, the largest annotated cuneiform sign dataset to date is used, and a Deformable Detection Transformer (DETR)-based object detection model is evaluated under two class granularities of 173 and 106 classes. The proposed system integrates automatic tablet-side extraction, heuristic line grouping, and n-gram-based textual similarity evaluation to bridge visual sign detection and textual structure, and achieves consistent improvements of up to 28-37% over prior work on COCO-style detection metrics. At inference, the method is applied to 87,668 tablet fragments from the Electronic Babylonian Library (eBL) corpus, producing nearly 2.9 million sign detections. Although the approach operates without linguistic priors and remains sensitive to tablet damage and layout variability, it provides a scalable and interpretable foundation for corpus-wide cuneiform analysis and supports future integration with multimodal and linguistic modelling frameworks.

---


### 423. [Supporting Tutors in the Gig Economy with Automated Feedback: A Case Study on Ringle](https://arxiv.org/abs/2606.22609)

**<font color=#1a73e8>作者：</font>** Yeon Su Park, Sieun Kim, Keighley Overbay 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The rise of online tutoring platforms in the gig economy has made education more scalable, flexible, and on-demand. These platforms rely on learner evaluations as the primary feedback for tutors and platforms. However, such feedback offers limited guidance for tutors' improvement and makes it difficult to monitor tutor quality at scale. To this end, we explored AI-powered automated feedback and how tutors perceive and respond to it. We deployed a research probe on Ringle, a popular online English tutoring platform, that analyzed tutors' lessons and provided automated feedback. We then surveyed 36 tutors about their experience. Our findings reveal that while tutors perceived automated feedback more negatively than learner feedback, they found it useful for self-monitoring and understanding platform expectations, though discrepancies between them often caused confusion. Based on these insights, we propose design considerations for feedback systems for online educational gig platforms.

---


### 424. [SkillAudit: From Fixed-Suite Benchmarking to Skill-Centered Assessment](https://arxiv.org/abs/2606.22613)

**<font color=#1a73e8>作者：</font>** Dexu Yu, Youhua Li, Zhaoyang Guan 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills have become a practical way to extend large language model agents, but the growing skill ecosystem still lacks a reliable way to judge whether a skill is worth deploying. Existing evaluation methods remain largely anchored to fixed task suites, assessing skills through performance on predefined tasks and environments. As skill marketplaces expand, this paradigm becomes inadequate: fixed suites can conflate a skill's marginal contribution with backbone strength and miss its value when tasks fall outside the skill's intended scope. We introduce SkillAudit, an end-to-end framework for skill-centered assessment that takes an arbitrary agent skill as input and automatically generates a comprehensive, multi-dimensional evaluation report spanning utility, efficiency/cost, and safety. SkillAudit focuses on the skill artifact itself and constructs capability-aligned evaluation tasks directly from the skill package. The generated tasks are conducted in isolated sandbox environments to collect execution evidence, followed by automated checks with LLM-based judging to produce auditable results. To dissect the agent skills, we propose the baseline comparison principle to measure utility and efficiency/cost, and introduce a two-stage detection paradigm combining static semantic analysis with dynamic runtime verification to assess safety risks. After scanning top-ranked real-world skill packages spanning 23 occupational categories, we found that over 7% of skills are at risky status.

---


### 425. [Federated Learning for Global Carbon Emission Forecasting: A Hybrid Time-Series Approach with Statistical and Neural Models](https://arxiv.org/abs/2606.22618)

**<font color=#1a73e8>作者：</font>** Attia Qammar, Qazi Haseeb Yousaf, Ali Azam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Climate change, primarily driven by carbon dioxide (CO2) emissions, requires accurate forecasting tools to support effective mitigation policies and sustainable development strategies. Existing forecasting approaches typically rely on centralized data collection, which is often restricted by privacy regulations and the distributed nature of emission data across countries and industrial sectors. This paper proposes a novel federated hybrid forecasting framework that integrates ARIMA-based trend modeling, GARCH-based volatility modeling, LSTM-Attention temporal representation learning, and XGBoost prediction within a privacy-preserving federated learning environment. The proposed framework enables collaborative learning among distributed clients without requiring the exchange of raw data. Experimental evaluation across 14 clients demonstrates strong forecasting performance, achieving client R2 values between 0.50 and 0.97 with an average of 0.73, RMSE values ranging from 0.06 to 2.35 with an average of 1.21, and MAPE values between 1.5% and 11.3% with an average of 6.5%. The results indicate that the proposed framework provides an accurate, scalable, and regulation-compliant solution for collaborative carbon-emission forecasting.

---


### 426. [DR-Mamba: Automatic Inference-Time Domain Adaptation for Document Image Binarization via Sample-Conditioned Detail-Background Suppression](https://arxiv.org/abs/2606.22625)

**<font color=#1a73e8>作者：</font>** Sheng-Wei Chan, Jen-Shiun Chiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Degraded document image binarization is sensitive to domain shifts caused by paper aging, bleed-through, stains, shadows, and uneven illumination, and the foreground-background separation of recent learning-based methods can become unstable on unseen degradation domains. We propose DR-Mamba, a sample-conditioned detail-background suppression framework that performs automatic inference-time domain adaptation for document image binarization. Unlike test-time adaptation methods that require gradient updates or auxiliary data at inference, DR-Mamba adapts to each input document through input-dependent gates within a single forward pass, requiring no target-domain labels, no fine-tuning, and no test-time parameter updates. Instead of using Mamba-style selective scanning as a single generic feature path, DR-Mamba reinterprets it as fast-slow route modeling: a fast detail route captures local stroke structures, while a slow background route accumulates spatially persistent degradation responses. The two routes are integrated through an input-dependent subtractive gate that explicitly suppresses background interference rather than fusing features by addition or concatenation. We further add full-resolution detail-guided reconstruction and thin-stroke-aware supervision to recover fine strokes lost during downsampling. Evaluated under a leave-one-year-out protocol on DIBCO-style benchmarks, where each held-out year is treated as an unseen degradation domain, DR-Mamba shows that per-document, per-location subtractive suppression improves cross-domain robustness, with particularly strong performance on the most severely degraded held-out fold.

---


### 427. [Scalable Maximum Entropy Reinforcement Learning for Diffusion Policies via Adjoint Matching](https://arxiv.org/abs/2606.22630)

**<font color=#1a73e8>作者：</font>** Serge Thilges, Onur Celik, Denis Blessing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion policies have recently emerged as a powerful paradigm for representing complex action distributions in reinforcement learning (RL). However, their application to online RL remains limited by the challenge of scalable training in the absence of ground-truth data, where standard optimization techniques such as score matching are not directly applicable. In this work, we introduce a highly efficient algorithm for optimizing diffusion policies by leveraging recent advances in stochastic optimal control. Our approach is based on adjoint matching, which enables simulation-free training and circumvents the need for explicit likelihood estimation or costly backpropagation through the diffusion process. Furthermore, we propose several extensions that improve the robustness and stability of the method in practical settings. Empirical results demonstrate that our approach achieves competitive performance while significantly reducing computational overhead, making diffusion policies more viable for online RL scenarios.

---


### 428. [4DVLT: Dynamic Scene Understanding with Worldline-Centered Vision-Language Tracking](https://arxiv.org/abs/2606.22631)

**<font color=#1a73e8>作者：</font>** Chaoyue Li, Boxue Yang, Shengyao Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D dynamic scene understanding requires grounding language to a persistent worldline that binds identity, metric 3D motion, and synchronized multi-view 2D projections. Existing paradigms capture only part of this structure: large multimodal models reason over rich visual evidence but rarely preserve metric topology, while vision-language tracking remains tied to fragmented 2D or 3D outputs and local continuation. We therefore introduce \textbf{4DVLT}, a worldline-centered task for instruction-conditioned 4D dynamic scene understanding in fully observed multi-view video, and \textbf{Instruct-4D}, a benchmark with 129.4K question-answer pairs, 64.7K target entities, 851 scenes, and 9 reasoning-oriented query types. To address this setting, we present \textbf{4DTrack}, which casts instruction-conditioned tracking as graph-conditioned worldline inference through an object-centric 4D state graph, metric-guided routing, bidirectional decoding, and kinematic calibration. On Instruct-4D, 4DTrack-Qwen3.5-9B reaches 62.68 $\mathrm{TGA}_{\mathrm{Top1}}$ and surpasses the best adapted VLT baseline by 19.62 points. These results show that worldline-centered modeling improves both target grounding and recovered worldline quality. The project page is available at this https URL.

---


### 429. [ColumnKeeper: Efficient Solutions to the ColumnDisturb Vulnerability in DRAM-based Systems](https://arxiv.org/abs/2606.22632)

**<font color=#1a73e8>作者：</font>** Andreas Kosmas Kakolyris, F. Nisa Bostanci, Ataberk Olgun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern DRAM chips are vulnerable to read disturbance phenomena such as RowHammer and RowPress, which induce bitflips after accessing nearby rows a certain number of times (the read disturbance threshold). ColumnDisturb is a new, fundamentally different DRAM read disturbance phenomenon. Specifically, ColumnDisturb (i) disturbs DRAM columns instead of rows, and (ii) increases the number of affected DRAM cells from those in only a few neighboring rows to all cells across three consecutive DRAM subarrays.
We propose ColumnKeeper, the first set of ColumnDisturb mitigations, in two variants: ColumnKeeper-D (CK-D), a deterministic mechanism, and ColumnKeeper-P (CK-P), a probabilistic one. CK-D exploits DRAM's open-bitline architecture to provide deterministic security guarantees at low performance and energy overheads: it uses two counters per subarray to track activations affecting the odd and even columns, and refreshes one row in a subarray when either counter reaches a predetermined threshold. CK-P instead refreshes one row in three consecutive subarrays upon a row activation in the middle subarray, with a predetermined probability, providing configurable security guarantees at low area overhead.
Both mechanisms prevent ColumnDisturb bitflips at low performance, energy, and area overheads. At the current experimentally-demonstrated ColumnDisturb threshold (1M), CK-D and CK-P incur very low average single-core performance overheads of 0.15% and 0.36%, respectively. For near-future thresholds (128K), these rise to a still low average of 1.70% and 2.73%. Mitigating ColumnDisturb at low thresholds (e.g., 16K) remains possible by adopting smaller subarray sizes or enabling subarray-level parallelism. CK-D and CK-P require low area overheads of 0.1 mm^2 and 0.03 mm^2, respectively. ColumnKeeper is freely available at this https URL .

---


### 430. [Learning Entropy Signature for Image Representation and Classification](https://arxiv.org/abs/2606.22634)

**<font color=#1a73e8>作者：</font>** Jan Glaser, Ivo Bukovsky, Noriyasu Homma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning Entropy (LE) has recently been extended to image analysis through Spatial Learning Entropy Maps (SLEMs), which are two-dimensional LE distributions that highlight unusually high learning activity across an image. Unlike conventional image descriptors, SLEMs are generated by incremental, sample-wise learning of a pretrained feedforward MLP network, where local pixel neighborhoods are presented sequentially in a fixed spatial order to predict the corresponding central pixels. Consequently, the learning activity at each image location depends not only on its local structure but also on the knowledge acquired from previously processed locations. This paper introduces Learning Entropy Signatures (LES), an image descriptor derived from SLEM using the K largest LE locations. LES captures the spatial organization of learning-relevant image structures and provides a compact representation of image content based on learning weight behavior. Experimental evaluation on image classification tasks shows that a relatively small number of K largest LE locations preserve substantial discriminative information. The results indicate a close relationship between the learning of neural weights and information relevance, extending the role of Learning Entropy from time series to images and, within images, from structural point extraction to compact image representation and classification.

---


### 431. [MaRS: Robust Out-of-Distribution Detection via Mahalanobis Residual Scoring](https://arxiv.org/abs/2606.22649)

**<font color=#1a73e8>作者：</font>** Francesco Di Salvo, Sebastian Doerrich, Christian Ledig  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models provide highly descriptive representations for medical images, yet their reliability degrades under distribution shifts arising from changes in patients, devices, or acquisition conditions. Reliable out-of-distribution (OOD) detection is therefore essential for safe deployment. Recent post-hoc detectors efficiently exploit frozen embeddings (\emph{e.g.}, kNN), whereas reconstruction-based OOD detection in latent feature space has seen limited adoption due to inconsistent performance. In this work, we show that the limitation of reconstruction-based methods in latent space does not stem from poor reconstruction quality, but from how reconstruction errors are scored. Standard $L_2$ residual norms collapse the anisotropic residual structure, thereby suppressing informative deviations. To address this limitation, we introduce \texttt{MaRS} (Mahalanobis Residual Scoring), a label-free OOD detector that learns an in-distribution manifold using a lightweight autoencoder and measures deviation via a Mahalanobis distance on reconstruction residuals, yielding variance-aware OOD scores. Across three imaging modalities, multiple types of distribution shift, and different model families and scales, \texttt{MaRS} outperforms established confidence-, distance-, and reconstruction-based baselines, while remaining fully post-hoc and lightweight. The code is available at this https URL.

---


### 432. [Confidently Wrong: Severity-Aware Calibration of Prompt-Injection Detectors under Attack Shift](https://arxiv.org/abs/2606.22659)

**<font color=#1a73e8>作者：</font>** Md Anas Biswas  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt-injection detectors are deployed as guards: a model scores an input and a downstream system trusts or blocks it on that score. I study the confidence of these scores, not only their accuracy, when the attack distribution shifts away from the clean benchmark on which the operating point was chosen. I evaluate three released detectors, ProtectAI-v2 and two Prompt-Guard-2 checkpoints, at a single source-calibrated threshold that I freeze and transport across five shifts. I report a severity metric S, how confident a detector is on the attacks it misses, alongside the false-negative rate and discrimination. Across every shift and every detector, severity on the missed attacks stays between 0.99 and 1.00 while the false-negative rate ranges from 0.01 to 0.97: when these detectors miss, they miss with near-certainty. All three confidently pass indirect behavior-hijack injection, a blind spot unanimous across two vendors and a fourfold size range. Standard pooled calibration error does not register this; one detector it rates well-calibrated, at 0.06, is miscalibrated at 0.91 on the attacks alone. Run against live models, the missed injections leak the majority of working exploits, passing them at the rate they catch others. A controlled experiment traces the cause to content-keying rather than injection structure, an instruction-tuned model used as a judge shows the same hijack blind spot, and a black-box rewriter exploits the content-keying to manufacture working confident misses, most effectively on the most dangerous attack category. Code and data are public.

---


### 433. [Prompting Diffusion Models for Zero-Shot Instance Segmentation](https://arxiv.org/abs/2606.22660)

**<font color=#1a73e8>作者：</font>** Irem Zeynep Alagöz, Nils Morbitzer, Andrea Ramazzina 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Several disruptive research directions have recently emerged in computer vision, including foundation models achieving previously unseen zero-shot performance in scene understanding, even interactively, and generative models that synthesize extremely realistic images. The latter have also been shown to be highly effective in scene understanding tasks thanks to their rich priors. However, for promptable segmentation, foundation models struggle with accurately segmenting an object's region, leading to false positives and over-segmentation. Notably, early attempts that leverage generative priors use prompts only during post-processing, yielding suboptimal segments because the process is agnostic to the user input. In this paper, we target these limitations with Prompt2Seg, a spatial conditioning framework for diffusion-based segmentation. Prompt2Seg augments a frozen diffusion segmentation model with a conditioning branch. Our approach takes spatial prompts, represented as 2D Gaussians or confidence maps, as explicit input signals, training the model to respond directly to user intent. Fine-tuned on a deliberately constrained set of object categories drawn from Hypersim and Virtual KITTI 2, Prompt2Seg generalizes zero-shot to a wide range of unseen object types and visual domains. We evaluate on seven datasets ranging from standard benchmarks to more challenging domains, including paintings, egocentric views, and X-ray data. Furthermore, we demonstrate that Prompt2Seg consistently outperforms the underlying diffusion segmentation backbone across all benchmarks. Our results suggest that the rich priors encoded in generative pretraining, combined with principled spatial conditioning, offer a compelling path toward broadly generalizing interactive segmentation without large-scale mask supervision.

---


### 434. [LSTM Variants for Chaotic Dynamical Systems: An Empirical Study on the Lorenz Attractor](https://arxiv.org/abs/2606.22662)

**<font color=#1a73e8>作者：</font>** Ruslan Gokhman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting chaotic dynamical systems such as the Lorenz attractor is notoriously difficult: small numerical errors are amplified exponentially over long autoregressive rollouts. We study seven recurrent and convolutional architectures for the AI-DEEDS 2026 Chaotic Systems Challenge: a vanilla LSTM, an LSTM with additive attention, a Bidirectional LSTM (BiLSTM), a BiLSTM trained with the Huber loss, a Temporal Convolutional Network (TCN), a CNN front-end followed by an LSTM, and a CNN front-end followed by a BiLSTM. All models share the same pre-processing, sequence length, and rollout procedure, isolating the contribution of each design choice. The challenge scores predictions on a 0-100 scale where higher is better. We obtain leaderboard scores between 45.72 and 58.81, with the BiLSTM trained with Huber loss being the strongest configuration. Two findings stand out: (i) adding additive attention to the unidirectional baseline degraded performance by over ten points, and (ii) prepending a CNN front-end to either an LSTM or a BiLSTM did not help and slightly hurt the score. Per-pair RMSE measurements confirm that the BiLSTM family generalizes better in the harder pairs (6-7), while the LSTM + Attention model collapses there (RMSE up to 8.94 on pair 6). We discuss why bidirectional context and a robust loss help in chaotic regimes while attention and CNN front-ends fail in this setting.

---


### 435. [Clipping the Price of Adaptivity at the Tail](https://arxiv.org/abs/2606.22669)

**<font color=#1a73e8>作者：</font>** Itai Kreisler, Yair Carmon, Oliver Hinder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive stochastic convex optimization (SCO) methods face a fundamental ``price of adaptivity'' barrier: under the standard set of assumptions, they cannot efficiently adapt to large uncertainty in both the initial distance to optimality and the Lipschitz constant. We circumvent this barrier by requiring a small amount of additional structure common to many learning problems. Specifically, we assume that the objective decomposes into a model and a loss function, enabling us to intervene by modifying the model's output before it passes to the loss function. Under this assumption, we design a method that clips the learned model output in tail events where it deviates too much from the output of a fixed reference model. Our method matches the optimal bounds for known-parameter SCO up to logarithmic factors in the uncertainty in the distance and Lipschitz parameters, thus efficiently adapting to large uncertainty in both.

---


### 436. [SATURN: Symbolic Spatial Reasoning for Multi-Perspective Grounding](https://arxiv.org/abs/2606.22694)

**<font color=#1a73e8>作者：</font>** Danial Kamali, Tanawan Premsri, Shreya Rajpal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) remain unreliable when spatial reasoning requires composing relations whose meanings depend on frames of reference. Existing neuro-symbolic methods make reasoning more explicit, but often depend on brittle geometric procedures and hard decisions over noisy perception. We propose SATURN, a neuro-symbolic framework for perspective-aware compositional spatial reasoning. SATURN reconstructs an approximate 3D scene, derives soft perspective-aware spatial predicates, and composes them with a training-free Pythonic symbolic executor, separating perception from reasoning while preserving uncertainty through multi-hop inference. We also introduce 3D FORCE, a diagnostic benchmark that controls reasoning depth, view, and perspective composition across spatial arrangement grounding (SAG) and referring expression grounding (REF). On 3D FORCE, VLMs and spatially trained models degrade sharply as depth and perspective complexity increase, whereas SATURN remains stable and outperforms strong baselines. On the real-world MindCube benchmark, SATURN achieves 78.57% overall accuracy, outperforming the strongest baseline by 14 pp.

---


### 437. [NullFlow: One-Step Generative Reconstruction](https://arxiv.org/abs/2606.22696)

**<font color=#1a73e8>作者：</font>** Xiao Shi, Edward P. Chandler, Chicago Y. Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose NullFlow, a principled framework for one-step generative image reconstruction. Our key idea is to confine the generative flow to a measurement-consistent subspace. Because the flow never leaves this subspace, NullFlow needs no separate data-fidelity corrections, unlike existing solvers. NullFlow samples in a single network evaluation by learning the flow's average velocity, avoiding the step-by-step integration of traditional flow matching methods. We prove that the average velocity of this constrained flow yields a training objective whose global minimizer is a one-step posterior sampler. We show on image inpainting that NullFlow matches state-of-the-art diffusion solvers while cutting inference from hundreds of network evaluations to one.

---


### 438. [SCRUB-FL: Sanitizing and Cleansing Representations via Unlearning of Backdoors](https://arxiv.org/abs/2606.22700)

**<font color=#1a73e8>作者：</font>** Osama Wehbi, Sarhad Arisdakessian, Omar Abdel Wahab 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative model training without sharing raw data, making it a promising paradigm for privacy-sensitive applications. However, its decentralized nature makes it inherently vulnerable to backdoor attacks, where malicious clients embed hidden triggers into local training data to manipulate model predictions. Existing defenses mainly operate during before and during aggregation cannot fully eliminate backdoor behaviors that persist in the converged global model. Moreover, the effectiveness of post-training sanitization is often limited by the server's lack of knowledge of trigger patterns or poisoned clients after convergence, resulting in residual backdoor behaviors or accuracy degradation due to neuron entanglement. To address this limitation, we propose SCRUB-FL (Sanitizing and Cleansing Representations via Unlearning of Backdoors), a two-phase solution for post-training backdoor removal in FL. During training, clients identify suspicious samples using spectral analysis and activation clustering, then train lightweight Wasserstein Generative Adversarial Network with Gradient Penalty (WGAN-GP) models to capture trigger-related distributions. The generator parameters are aggregated server-side to construct a global representation of suspicious patterns without exposing raw data. After convergence, the server synthesizes trigger-approximating samples and applies machine unlearning to erase the trigger-target association by redistributing predictions toward a uniform distribution. Experimental evaluations on CIFAR-10 and GTSRB across three attack types and up to 40% malicious participation demonstrate that SCRUB-FL reduces the backdoor attack success rate to as low as 3.88% while maintaining over 91% normal task accuracy, outperforming state-of-the-art defenses without requiring prior trigger knowledge or a large clean proxy dataset at the server.

---


### 439. [Modular Diffusion Models for Structured Visual Recognition](https://arxiv.org/abs/2606.22702)

**<font color=#1a73e8>作者：</font>** Siddhesh Khandelwal, Björn Ommer, Leonid Sigal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional supervised methods for structured visual recognition tasks -- such as object detection, segmentation, and scene graph generation -- often produce deterministic, fixed outputs, limiting their ability to capture the inherent uncertainty in complex visual scenes. As a consequence, such point estimates are unable to capture the prediction uncertainty (or multi modality) intrinsic to these problems, often arising from natural ambiguities (e.g., ambiguity in size of partially occluded objects, local ambiguity of exact segmentation boundary, etc.) as well as noise and sparsity of training data. To address this limitation, we present Modular Diffusion Models (MDMs), a simple and novel framework that learns a distribution over structured outputs for a given input image. MDMs decompose the diffusion process into distinct, task-specific modules, each focused on capturing a different aspect of the structured information space, such as object categories, spatial locations, and inter-object relationships. This modular design allows each component to be learned independently, with seamless integration at inference without additional training. Furthermore, the modularity of MDMs enables the diffusion process to easily operate over the heterogeneous output space common in many structured learning tasks (e.g., a continuous bounding boxes and discrete class labels). Experimental results over three distinct structured tasks -- object detection, instance segmentation, and scene graph generation -- highlight the benefits of our proposed framework.

---


### 440. [VeriPort: Automated and Verified Patch Backporting at Scale](https://arxiv.org/abs/2606.22704)

**<font color=#1a73e8>作者：</font>** Jonah Ghebremichael, Wenxin Jiang, Mikola Lysenko 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> One of the key challenges for securing the software supply chain is addressing known vulnerabilities in third-party open-source dependencies. Security patches are frequently only available for the latest version of a dependency, leaving developers with the choice of either upgrading to the latest version (risking breaking changes) or manually backporting the security fix. Prior work backports to a single version that must be specified in advance and does not produce sufficient evidence to demonstrate that their patches block exploitation and preserve functionality. In this paper, we present VeriPort, an end-to-end agentic system that scalably backports a patch for a given vulnerability advisory to every affected version of the package. For each backport, VeriPort builds a chain of evidence to confirm that the patch blocks exploitation and preserves intended behavior. VeriPort reliably resolves 95.3% of 128 backporting tasks in BackportBench, outperforming the best existing solution (Claude Code) by 22.7 percentage points. We further deployed VeriPort on 169 high- and critical-severity CVEs and have generated over 5,000 verified backported patches. Moreover, VeriPort's value extends beyond simply backporting patches. It uncovered 2,100 versions incorrectly reported as affected and 127 previously unidentified vulnerable versions across 92 advisories, and 23 advisories have since been corrected upstream by removing 387 versions and adding 81.

---


### 441. [One-Prompt Censorship Evasion via Generative Diffusion Models](https://arxiv.org/abs/2606.22717)

**<font color=#1a73e8>作者：</font>** Shiyi Ling, Yuhang Gan, Chen Qian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The escalating arms race between Internet censorship and evasion has driven censors to evolve from static rule-based filtering to sophisticated deep learning-based traffic analysis. While recent automated evasion tools have attempted to counter this by leveraging stochastic search and programmable heuristics, they continue to suffer from insufficient evasion robustness across diverse censorship modalities and poor usability due to complex, mechanism-specific configurations that require manual fitness tuning or domain-specific languages. In this paper, we propose a paradigm shift that reframes censorship evasion as a semantic image-to-image editing task, allowing users to execute it with a single prompt. We introduce FlowPaint, a novel generative framework that leverages the "world knowledge" of large diffusion models to automatically reshape censored traffic into benign patterns. FlowPaint utilizes an instruction-tuned diffusion architecture to perform semantic editing on network flows. Evaluations against both industrial-grade rule-based middleboxes and learning-based classifiers demonstrate that FlowPaint outperforms existing censorship evasion baselines, enabling users to counter diverse censorship paradigms solely by varying natural language instructions

---


### 442. [Generative Relightable Avatars](https://arxiv.org/abs/2606.22718)

**<font color=#1a73e8>作者：</font>** Kunwar Maheep Singh, Christian Theobalt, Rishabh Dabral  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Generative Relightable Avatars (GRA), a person-specific method for photorealistic free-view rendering and environment-map relighting of full-body humans. We postulate that modeling fine-grained appearance details is inherently a one-to-many problem that can benefit from a generative formulation. In contrast to fully regressive relightable avatar methods, GRA follows a hybrid approach that combines controllable, physics-grounded relighting with probabilistic refinement. Starting from a tracked animated mesh, we optimize material parameters in UV-space and render a coarse relit appearance under a target HDR environment map. Next, we refine the textures with a feed-forward model to capture pose-dependent texture dynamics and illumination effects beyond simplified reflectance assumptions. Finally, a fine-tuned video-to-video diffusion model transforms the physically grounded renderings into temporally coherent, high-detail videos while preserving 3D control, with an error-recycling strategy for generating long videos. Experimental evaluations demonstrate our method's improved perceptual quality over prior relightable avatar baselines. Project Page: this https URL

---


### 443. [moBERTo: A Modern Encoder for Portuguese via Continued Pretraining of ModernBERT](https://arxiv.org/abs/2606.22722)

**<font color=#1a73e8>作者：</font>** Thiago Laitz, Thales Sales Almeida, João Guilherme Alves Santos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Encoder-only transformer models remain essential for production NLP pipelines. We introduce moBERTo, a Portuguese adaptation of ModernBERT obtained through continued pretraining of the ModernBERT-base checkpoint on 60 billion tokens (5 epochs over a 12-billion-token corpus curated from FineWeb2 and filtered with educational and STEM classifiers). We preserve the original architecture, including rotary positional embeddings, alternating local-global attention, flash attention, and unpadding. We evaluate moBERTo across information retrieval (including long-context retrieval at up to 8,192 tokens), document classification, named entity recognition, and natural language understanding. Our best variant, which combines a Portuguese tokenizer with subword-matching embedding transfer and long-context post-training, achieves the highest average reranking nDCG@10 across three Portuguese retrieval benchmarks and the best results on PLUE-PT. Through ablation studies, we show that (i) continued pretraining is strongly preferable to training from scratch, particularly for preserving long-context capabilities; (ii) tokenizer adaptation improves token-level tasks but degrades long-context retrieval; (iii) a dedicated long-context post-training phase at 8,192 tokens further improves reranking and NER; and (iv) encoder-only architectures remain competitive with larger decoder-only alternatives for discriminative tasks. We publicly release the model weights at this https URL and training data at this https URL on Hugging Face.

---


### 444. [Subspace-Constrained Federated Learning with Low-Rank Adaptation](https://arxiv.org/abs/2606.22724)

**<font color=#1a73e8>作者：</font>** Neranjan Senarath, Rohit Muralitharan, Sadia Asif  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated low-rank adaptation methods are attractive for fine-tuning large models under communication and privacy constraints, but heterogeneous client data can induce geometric misalignment between local low-rank updates. We study whether this subspace misalignment leads to destructive aggregation and slower convergence in LoRA-based federated learning. We propose a subspace-regularized federated LoRA objective that encourages local client updates to remain close to a shared global reference subspace. We present a complete empirical evaluation on two pretrained models, RoBERTa-large and SmolLM-360M, over HellaSwag in a non-IID 10-client federated setting, across 3 random seeds (42, 43, 44), yielding 24 total experimental runs (4 methods x 3 seeds x 2 models). On RoBERTa-large, Subspace-Reg achieves the strongest mean best accuracy (0.454 +/- 0.023), mean final accuracy (0.429 +/- 0.011), and lowest final loss (1.363) across all three seeds, outperforming FedAvg, SVD redistribution, and FedSVD baselines by a large margin. On SmolLM-360M, FedAvg leads on accuracy, revealing that accuracy gains are model-dependent. Crucially, Subspace-Reg achieves near-perfect basis overlap, approximately 0.9999, on both models and across all seeds, versus 0.958 to 0.991 for all baselines, providing robust support for the geometric alignment hypothesis. The code is publicly available at this https URL.

---


### 445. [Interpretable Uncertainty Routing Separating Emotion Ambiguity from Distribution Shift in Facial Expression Recognition](https://arxiv.org/abs/2606.22725)

**<font color=#1a73e8>作者：</font>** Keito Inoshita, Takato Ueno  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facial expression recognition (FER) is inherently ambiguous: human annotators frequently disagree, and models deployed in real environments face distribution shift. Crucially, these two conditions demand different downstream actions, as ambiguous in-distribution faces should be reported with their ambiguity whereas out-of-distribution inputs should be rejected. However, a single uncertainty score conflates the two. In this study, uncertainty decomposition into aleatoric and epistemic components for FER is investigated, and Uncertainty-Aware Routing (UAR), an inference-time routing mechanism that exploits the separation, is introduced. Specifically, aleatoric and epistemic uncertainties are obtained from a Deep Ensemble of fully fine-tuned DINOv2 models and are each validated against an independent external signal: aleatoric against human annotator disagreement, and epistemic against distribution shift induced by image corruptions. The proposed dual-validation protocol reveals that aleatoric recovers annotator disagreement with Spearman correlation 0.66 (95% CI: 0.64-0.68), and epistemic detects corruption-induced shifts, achieving average AUROC of 0.699 at the highest corruption severity. UAR retains approximately 1.8 times more ambiguous in-distribution faces than single-uncertainty routing at a matched out-of-distribution rejection rate. A strong label-distribution-learning baseline achieves comparable disagreement recovery but cannot separate ambiguity from shift and therefore cannot route, establishing that the value of decomposition lies in the separation enabling interpretable and differentiated action selection.

---


### 446. [Text Dictates, Music Decorates: Energy-based Attention for Editable Dance Motion Generation](https://arxiv.org/abs/2606.22726)

**<font color=#1a73e8>作者：</font>** Seong Jong Yoo, Siyuan Peng, Felix Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Choreographic motion generation poses unique challenges for AI, demanding precise semantic control over complex, temporally structured, and expressive full-body dynamics. While existing models can synthesize motion from music, they remain largely black boxes. Conversely, attempting to condition generation on both text and music frequently leads to modality collapse, where dense acoustic rhythms overwhelm sparse semantic text prompts, destroying user controllability. To resolve this spatial-temporal conflict, we propose STREAM (Structural-Temporal Rhythmic Energy-based Attention for Motion), a modality-decoupled diffusion transformer. STREAM strictly separates conditioning pathways: global text semantics dictate the kinematic structure via Adaptive Layer Normalization (AdaLN), while a novel Bimodal Energy-Based Attention Module (BEAM) routes these features to the musical beat without overwriting the semantics. We further introduce Motorica++, a newly curated dataset enriched with domain-specific dance vocabulary and frame-level semantic annotations from existing Motorica dataset. Additionally, to rigorously quantify zero-shot editability, we propose the Exchange Evaluation Protocol and Editable Dance Score (EDS). Through extensive experiments, STREAM achieves state-of-the-art alignment between motion and music while perfectly preserving choreographic semantics, positioning AI not merely as a reactive synthesizer, but as a controllable, collaborative partner for artistic direction. The source code and datasets are available at this https URL.

---


### 447. [Closed-loop Auto Research for Molecular Property Prediction: Discovering and Certifying Generalizable Improvements](https://arxiv.org/abs/2606.22731)

**<font color=#1a73e8>作者：</font>** Jingjie Ning, Xiaochuan Li, Ji Zeng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Closed-loop Auto Research extends automated machine learning from fixed-dataset fitting to changing the research workflow, with language-model agents editing representations and model code and acquiring external evidence. Molecular property prediction spans many small endpoints. We ask whether this action space yields improvements generalizing beyond the validation signal selecting them.
We isolate three Auto Research axes, features, models, and external evidence, under a file-level ablation lock attributing each gain to one axis over a strong baseline. Across 36 endpoints in three benchmark suites we score each selected configuration once on a held-out test whose labels the search never read. A routed pipeline taking each endpoint's best validation axis reaches positive held-out gains of 0.013, 0.011, and 0.042, the transferable axis differing by suite, data on TDC, model on Polaris, feature and model on MoleculeNet. The largest model-search gain falls from 0.041 on validation to 0.003 on test, while curated data reaches 0.022 but negative 0.019 on test, two non-transfer signatures. Curated external data raises held-out CYP2C9-substrate performance by 0.17 and half-life by 0.08, admitted through a contamination filter rejecting same-source files overlapping 64 to 89 percent of test structures, necessary but not sufficient for transfer. A matched-trial automated machine learning control did not reproduce the agent's code-level model intervention, reaching 0.006 against 0.042, and the pipeline stays competitive with an 84M-parameter pretrained 3D model on the shared training split.
The experiments stay within molecular property prediction, but separating discovery from held-out certification is a domain-agnostic lesson for any closed-loop system optimising a proxy for a held-out quantity.

---


### 448. [Error Highways: Scaling Predictive Coding to Very Deep Networks](https://arxiv.org/abs/2606.22744)

**<font color=#1a73e8>作者：</font>** Amirhossein Mohammadi, Alexander G. Ororbia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive coding networks (PCNs) offer a biologically-plausible, local-learning alternative to back-propagation of errors (backprop). Nevertheless, they have remained largely confined to shallow architectures and evaluated on simple machine intelligence benchmarks. A central obstacle to scaling PCNs is that the learning signal decays rapidly as it propagates away from the clamped boundaries, leaving interior layers effectively unchanged. To directly counter this problem, we propose highway error propagation (HEP), a scheme that augments the free energy function underlying predictive coding (PC) by altering its neural structure with feedback matrices $V_{L\to i}$ that couple selected hidden states directly to the clamped output error. Since this coupling is linear in the hidden state, the highway pathway delivers a correction at every inference step whose magnitude is independent of depth, in contrast to vanilla PC where the output error reaches the $i$-th hidden layer with attenuation that decays exponentially in depth. This bypasses the Jacobian chain while preserving the local PC synaptic update rule. On MNIST and Fashion-MNIST, we show that HEP effectively trains MLPs of up to 128 layers with accuracy that is robust with respect to depth.

---


### 449. [RaysUp: Ultra-light Universal Feature Upsampling via Geometry-Aware Ray Representation](https://arxiv.org/abs/2606.22749)

**<font color=#1a73e8>作者：</font>** Yuchuan Ding, Linfei Li, Lin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained Vision Foundation Models (VFMs) have become central to modern computer vision due to their powerful semantic representations and strong generalization ability. However, their patchified or pooled outputs are inherently low-resolution, limiting their effectiveness in tasks requiring fine-grained, pixel-level reasoning. Existing feature upsampling approaches either degrade semantic fidelity or rely on VFM-specific retraining and heavy architectures, hindering efficiency and scalability. To address these challenges, we propose RaysUp, an ultra-lightweight, task-agnostic, and VFM-agnostic feature upsampling framework that reconstructs high-resolution feature maps at arbitrary resolutions. Unlike conventional 2D interpolation or attention-based schemes, RaysUp lifts feature reconstruction into a geometry-aware ray domain. Specifically, we introduce a Spatially Decoupled Guidance Encoder for direction-aware guidance encoding, an Any-Resolution Cross-Attention mechanism for resolution-flexible reconstruction, and a novel Ray Positional Encoding (RayPE) that injects implicit 3D geometric priors via 6D Plucker ray coordinates. Finally, a Geometry-Aware Neighborhood Attention module further ensures content-adaptive bilateral aggregation while preserving geometric consistency. Extensive experiments across diverse dense prediction tasks demonstrate that RaysUp achieves state-of-the-art performance while using only 16% of the parameters of AnyUp and delivering approximately 7x faster inference. These results highlight a substantially improved accuracy-efficiency trade-off and establish RaysUp as a practical and scalable solution for universal feature upsampling. Code is available at this https URL.

---


### 450. [One-Step Flow Matching for Generative Modeling of Path-Dependent Physical Fields](https://arxiv.org/abs/2606.22752)

**<font color=#1a73e8>作者：</font>** Yijing Zhou, Jasmin Jelovica  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical simulations for intricate geometries with path-dependent constitutive models face difficulties due to the enormous computational cost they require. Recently, the emergence of generative AI models, which succeed in image and video synthesis tasks, has provided a promise to further improve simulations. Although U-Net-based denoising diffusion probabilistic models (DDPMs) have been adopted for elastic stress field generation, they typically require hundreds of sampling steps, and applications of generative models to path-dependent, e.g. plastic, stress fields remain very limited. In this work, we propose a novel flow matching (FM) model based on a transformer backbone for high-resolution path-dependent stress field generation with stochastic loading-unloading paths and geometry. The proposed model operates within the latent space of a variational autoencoder (VAE) and formulates the simulation of plastic fields as a video synthesis task, directly generating the stress fields across all time steps. Meanwhile, we design a non-Gaussian source distribution for flow matching, such that crossings among conditional transport paths are reduced during training. This enables our model to generate satisfactory samples in one step without relying on distillation. In addition, we introduce token-level loading embeddings and two auxiliary networks to further enhance the model performance in path-dependent simulation. The results demonstrate that, even with a limited training dataset, our model can accurately generate high-resolution path-dependent fields. It is much more computationally efficient than finite element analysis, providing a speedup of 6 to 7 times over FEM on CPUs and approximately two orders of magnitude speedup on consumer-grade GPUs.

---


> [!TIP]
> 当前位于：**401-450**（第 9/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-654](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
