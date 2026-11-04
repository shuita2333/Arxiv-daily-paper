# 📦 其他研究 | 2026年11月05日

> 本类共 **280** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-280](./part-06.md)

---

### 151. [Making Smell Actionable in Design: Lexicon, Movement Patterns, and Gesture Cards](https://arxiv.org/abs/2611.04609)

**<font color=#1a73e8>作者：</font>** Anran Feng, Shengyu Gao, Xingyu Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smell is powerful in design, yet it often remains vague and difficult to work with in studios and classrooms. While olfactory HCI has produced devices, toolkits, and scenario-based applications, designers still lack teachable, shareable resources that link smell to bodily action. This paper presents a three-phase research program that makes smell actionable by moving from lived smell experiences to movement patterns and, finally, to gesture resources. We study olfactory-motor mappings and package the results as teachable design representations through a progressively narrowing method: (1) extracting smell-verb-intent relations from user narratives; (2) capturing and clustering embodied enactments into standardized upper-limb trajectory families; and (3) translating these trajectories into gesture card representations for design teaching and ideation through design workshops. We present a three-phase translational framework and empirically derived smell-gesture correspondences that structure the smell-intent-trajectory-gesture pathway, together with reusable assets (lexicon, trajectory atlas, gesture tables, and cards) that support teaching, reuse, and adaptation across contexts.

---


### 152. [CAPSkip: Cancellation-Aware Prefix Skipping for Selective Backpropagation](https://arxiv.org/abs/2611.04611)

**<font color=#1a73e8>作者：</font>** Heejin Choi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Per-step selective back-propagation forwards every example of a mini-batch but back-propagates only some of them. Most rules rank examples by loss or gradient magnitude, but such scalar scores ignore cancellation between per-example gradients: the gradient removed by a set can be much smaller than its individual magnitudes suggest. We introduce CAPSkip (Cancellation-Aware Prefix Skipping). Among the examples the model already classifies correctly, CAPSkip skips the longest prefix, in increasing order of last-layer gradient norm, whose vector sum stays within a relative budget $b$ of the batch's last-layer gradient. In exact arithmetic this bounds the change of the raw final-layer gradient, using rank-one contributions already available from the forward pass; the bound does not extend to deeper layers, optimizer updates, or the training trajectory. Because the cumulative distortion is not monotone in the prefix length, CAPSkip scans all prefixes; a factorised Gram matrix makes the scan cheap and keeps it on the device. With activation reuse and selected-row backward, CAPSkip fine-tunes DeiT-S on CIFAR-100 for 103 epochs in 0.576x the time of 103-epoch dense training, and is +0.25 pp [+0.08, +0.42] above an approximately time-matched 59-epoch dense run (n=3).

---


### 153. [Policy Network Diffusion](https://arxiv.org/abs/2611.04614)

**<font color=#1a73e8>作者：</font>** Jiate Liu, Deheng Ye  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have shown remarkable progress in AI-generated content, including images and videos. In this paper, we explore whether diffusion models can generate the parameters of policy networks in reinforcement learning (RL), and whether the generated policies exhibit generalization capabilities. To achieve this, we propose Diffusion-based Conditional Policy Network Parameter Generation (DPPG), which consists of a Transformer-based autoencoder and a task-conditioned diffusion model. The autoencoder achieves a high compression rate by patchifying network parameters, while the task-conditioned diffusion model generates corresponding parameters conditioned on different environments. Our experiments demonstrate that, with a single unified DPPG model, we can synthesize high-quality policies across a diverse set of tasks from different environment domains, including Classic Control, Atari games, and MuJoCo. Additionally, our method can generate networks with a larger number of parameters compared to previous approaches. Furthermore, we find that in previously unseen environments, DPPG can generate parameters that achieve faster convergence and reach competitive performance, showcasing the potential future applications of parameter generation via diffusion.

---


### 154. [Gradient-Guided Orientation Learning for Weakly Supervised Oriented Object Detection](https://arxiv.org/abs/2611.04616)

**<font color=#1a73e8>作者：</font>** Junyong Jang, Juheon Park, Minyoung Jeon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised oriented object detection (WS-OOD) aims to reduce the annotation cost of rotated bounding boxes by leveraging cheaper annotations such as horizontal boxes or points. However, these weak annotations provide no explicit orientation information, forcing existing methods to infer object angles through indirect geometric consistency or equivariant constraints. Such indirect supervision often becomes ambiguous and unstable under real-world appearance variations, including illumination changes, color shifts, shadows, and background clutter. In this paper, we present a simple yet effective gradient-guided orientation learning strategy for WS-OOD. Motivated by the observation that the input image itself contains useful orientation priors, our method extracts dominant gradient-based orientation cues from object regions and converts them into pseudo-angle labels for auxiliary supervision, enabling the detector to learn orientation-aware representations without requiring rotated bounding box annotations or extra learnable parameters. Furthermore, since AP can mask substantial angular errors when spatial IoU remains high, we introduce an orientation-aware evaluation metric that incorporates angular discrepancies into the standard AP protocol. Extensive experiments on weakly supervised oriented detection benchmarks demonstrate that the proposed pseudo-angle supervision improves both detection performance and orientation estimation quality, while the proposed metric provides a more faithful assessment of angle prediction than conventional AP alone.

---


### 155. [Polyp Matching Using Deep Learning](https://arxiv.org/abs/2611.04624)

**<font color=#1a73e8>作者：</font>** Kristian Dalsbø Hindberg, Puneet Sharma, Benedicte Schelde-Olesen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A key challenge in colon capsule endoscopy (CCE) analysis is accurately identifying whether multiple images depict the same polyp, which is critical to avoid over-counting and unnecessary clinical interventions. Additionally, this prevents prolonged follow-up colonoscopies where endoscopists search for duplicate polyps without precise localization. This study presents a novel contrastive learning-based approach to polyp matching using a Siamese neural network architecture. The model was trained on a dataset from the Danish CareForColon2015 trial. The dataset comprises 5,103 image pairs of confirmed same polyp and 5,103 pairs of different polyps, annotated by experienced clinicians. The proposed model employs ResNet variants (ResNet18, ResNet34, ResNet50), DenseNet121 and EfficientNet B0/B3 as backbones and utilizes contrastive learning with cosine vector distance metric for classification. Experimental results demonstrate high classification accuracies of up to 92% and AUC values close to 0.98. These results suggest that automated polyp matching has the potential to reduce polyp over-counting, improve patient risk stratification, and reduce unnecessary follow-up colonoscopies.

---


### 156. [MambaHand: Local Identity and Behavioral Sequence Learning with Mamba for Dynamic Hand Gesture Authentication](https://arxiv.org/abs/2611.04626)

**<font color=#1a73e8>作者：</font>** Zenan Lin, Junduan Huang, Xilai Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic hand gesture authentication (DHGA) is an emerging biometric technique that contains both physiological and behavioral identity characteristics. However, existing methods primarily rely on convolutional networks or manually designed motion representations, making it difficult to jointly capture fine-grained local identity differences and long-range behavioral dependencies during hand gesture execution. To address these challenges, we propose a two-stream identity representation learning framework, MambaHand Net, to combine CNNs with Mamba for DHGA. The proposed framework consists of a Local Identity Stream (LIS) and a Behavioral Sequential Stream (BSS). The LIS extracts frame-wise local identity cues with a convolutional network, while the BSS preserves spatial tokens from intermediate visual features and constructs first-order and second-order temporal difference sequences to model multi-order behavioral variations. Moreover, the bidirectional Mamba is incorporated into the BSS to model semantic motion across different spatial locations, enabling efficient long-range modeling of hand gesture execution habits. Finally, attention-guided spatial token aggregation and a two-stream fusion strategy are used to integrate local identity cues and multi-order behavioral patterns into a discriminative identity representation. Our method achieves state-of-the-art (SOTA) average performance on the SCUT-DHGA benchmark dataset, demonstrating that combining CNNs with Mamba is an effective new solution for DHGA.

---


### 157. [ReXMo: End-to-End Video Character Replacement with Expression and Motion Preservation](https://arxiv.org/abs/2611.04633)

**<font color=#1a73e8>作者：</font>** Hualiang Wei, Wenhui Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video character replacement aims to replace actors while preserving facial expressions, motions, and scene dynamics. Existing methods typically rely on masked generation with pose guidance, limiting fine-grained expression and motion preservation in complex scenes. We propose ReXMo, an end-to-end framework that supports single-, multi-, and selective character replacement scenarios. ReXMo introduces paired triplet supervision, where synthesized driving videos and original videos share identical performances but different identities, enabling scalable training through synthetic data generation. An In-Context Diffusion Transformer learns identity transformation by jointly conditioning on driving videos, reference identities, and text prompts, while an Expression Enhancement Adapter improves facial expression preservation in multi-person scenes. Extensive experiments demonstrate that ReXMo outperforms existing methods in identity fidelity, motion consistency, expression preservation, and visual quality. Our dataset and code will be publicly released.

---


### 158. [SAT Encoding for Set of At-Most-K Cardinality Constraints with Ladder Shape](https://arxiv.org/abs/2611.04637)

**<font color=#1a73e8>作者：</font>** Hieu Truong Xuan, Tuyen Kieu Van, Khanh To Van  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel SAT encoding designed to represent a sequence of At-Most-K cardinality constraints arranged in a ladder-like structure, referred to as the Ladder AMK constraint. These AMK constraints feature a ladder-like arrangement, with shared common variables in the center and two variables differing at the beginning and the end. The proposed encoding first decomposes the sequence of AMK constraints into separated blocks, then encodes each block as a whole rather than encoding each AMK constraint individually. This approach improves the efficiency of constraint solving in SAT solvers by significantly reducing the size of the encoding, precisely the number of variables, and the generated clauses required. To achieve this, the encoding employs Sequential Counter to encode each block and constructs clauses that link adjacent blocks, ensuring equivalence with the input constraints. Compared to the previously proposed encoding that uses BDD for Ladder AMO constraint, our encoding requires fewer variables and clauses. Our study is the first study that develops SAT encoding for Ladder AMK constraints with k>1. Experimental results on single Ladder AMO and Ladder AMK constraints indicate that our encoding significantly enhances both the size of the encoding and the efficiency of solving time compared to existing encodings. Furthermore, by evaluating on the two real-world combinatorial problems, namely Anti-bandwidth Problem and Nurse Rostering Problem, we found that the proposed encoding surpasses alternative encodings, as well as more advanced Constraint Programming and Mixed Integer Programming solvers. In summary, the SAT encoding technique presented in this paper provides a more efficient method for encoding sequence constraint, specifically Ladder AMK constraint, which could enhance the effectiveness of SAT solving for various problems involving this type of constraint.

---


### 159. [Does LinUCB Need Valid Confidence Sets?](https://arxiv.org/abs/2611.04641)

**<font color=#1a73e8>作者：</font>** Ahmed Ben Yahmed, Marc Abeille, David Janz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that replacing LinUCB's usual confidence width $\beta$ by any fixed $\alpha>0$ preserves sublinear regret when the action set is $M$-smooth and $m$-strongly convex. Our high-probability regret bound for this generalisation, $\alpha$-LinUCB, establishes that valid confidence sets are not necessary for the success of LinUCB. We identify the mechanism behind this result: action-set curvature drives $\alpha$-LinUCB to explore every direction, even when optimism is not guaranteed. To analyse this mechanism, we introduce a logarithmically capped spectral potential that, unlike the standard log-determinant potential, caps contributions from well-explored directions. This yields lower bounds on the smallest eigenvalue of the design matrix. At the standard confidence width $\alpha=\beta\asymp\sqrt{d\log T}$, our $T$-round regret bound in $d$ dimensions is $O\bigl(\frac{M}{m}d\sqrt{T\log T}\bigr)$, up to iterated-logarithmic factors, improving the horizon dependence of the classical LinUCB guarantee by a factor of $\sqrt{\log T}$.

---


### 160. [Therapy-FIS: A Dataset for Assessing Facilitative Interpersonal Skills in Psychotherapeutic Setting](https://arxiv.org/abs/2611.04645)

**<font color=#1a73e8>作者：</font>** Qijian Zheng, Wanqing Lin, Yuanfang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Facilitative Interpersonal Skills (FIS) is a performance-based assessment method that provides a structured framework for evaluating the interpersonal competencies of mental health professionals. However, existing FIS assessment relies heavily on human observer ratings, making the evaluation process labor-intensive, costly, and difficult to scale. Progress toward automated FIS assessment has also been constrained by the lack of publicly available professional data in psychotherapy settings. To address this limitation, we introduce Therapy-FIS, a dataset for automated FIS assessment in standardized psychotherapy tasks. To our knowledge, Therapy-FIS is the first publicly available dataset in this domain. It contains facial, acoustic, and textual signals derived from standardized therapist responses to standardized mock patient stimulus clips, based on 890 therapist video recordings and 8 patient videos, and is rated with eight FIS subscale ratings and an overall FIS score. Built on Therapy-FIS, we further establish a benchmark with two downstream tasks: Therapist Performance Rating and Joint Therapist--mock-Patient Performance Rating. We also introduce a competitive baseline, DyadicFIS, with gated fusion and routed readout under therapist-only and dyadic settings. DyadicFIS obtains the best macro CCC(Concordance Correlation Coefficient) scores on both tasks (0.2807 and 0.3299). Therapy-FIS offers a reproducible resource for data-driven automated assessment of therapeutic interpersonal skills in mental health.

---


### 161. [BhopalMLS: A LiDAR Dataset for Semantic Scene Understanding in Heterogeneous Urban Environments](https://arxiv.org/abs/2611.04654)

**<font color=#1a73e8>作者：</font>** Pyare Lal Chauhan, Vaibhav Kumar, Bharat Lohani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce BhopalMLS, a large-scale Mobile Laser Scanning (MLS) dataset from a dense, heterogeneous urban environment in Bhopal, India, with mixed traffic, informal structures, and narrow unplanned streets. It spans approximately 10 km of road corridors with over 1.2 billion points and 19,518 annotated instances across 62 fine-grained static categories, grouped into 12-class and 21-class benchmark taxonomies; 6 optional moving-class subclasses support dynamic-object analysis. Existing 3D datasets, collected in well-planned cities, are structurally more uniform than such unplanned settings, and lack their subtype diversity. On semantic and instance segmentation at both granularities, fine-tuned foundation models surpass supervised baselines: Utonia(L) reaches 71.28% mIoU (vs. PTv3's 68.04% from scratch) and 44.07% mAP50 on the 12-class benchmark. Cross-region experiments against four established datasets (Ke-MLS, Toronto-3D, Paris-Lille-3D, SemanticKITTI) reveal a consistent asymmetric transferability: models trained on BhopalMLS transfer better than the reverse on every pair, for both Utonia(L) and Concerto(L) (mean 21.5, up to 36 mIoU points), holding even when the target is denser. Factor-controlled retraining at a fixed label budget, repeated on both models, attributes this to the coverage of BhopalMLS's subtype inventory rather than to dataset size or corridor geometry: collapsing each class to a single subtype costs 13.0 and 13.3 mIoU points for Utonia(L) and Concerto(L). BhopalMLS therefore offers a testbed for 3D perception beyond well-planned cities. Data and an interactive viewer are at this https URL.

---


### 162. [Exploiting Biases in Attention for Transformers](https://arxiv.org/abs/2611.04657)

**<font color=#1a73e8>作者：</font>** Charles Herr, Gabriele Spadaro, Enzo Tartaglione  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attention is known to be sparse in vision transformers. In particular, we analyze the unequal relevance of attention-matrix columns to the final computation and show that this phenomenon becomes increasingly pronounced with network depth. This can be interpreted as saying that tokens have an absolute importance for the attention process, independently of queries. Inspired by this, we propose a reformulation of the attention formula that makes this phenomenon explicit by adding an input-dependent bias to the query-key dot product. We show that this new term gives each token a scalar value indicating its anticipated influence on other tokens during the attention process, and can thus serve as a proxy for pruning attention maps. Across multiple transformer model sizes, this allows us to substantially reduce the computational cost of attention, in terms of both FLOPs and inference latency, while retaining most of the original classification accuracy. We publicly released the code and models at this https URL.

---


### 163. [Leakage-free evaluation of residual graph convolutional networks for network intrusion detection](https://arxiv.org/abs/2611.04660)

**<font color=#1a73e8>作者：</font>** Zahid Iqbal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks are increasingly proposed for network intrusion detection, yet many reported results come from protocols in which test flows shape the graph used for training, duplicated flows sit on both sides of the split, or a single split is reported. This study measures what a residual graph convolutional network gains over simpler models once these sources of optimism are removed. CICIDS2017 and NF-UNSW-NB15-v2 were cleaned with label-aware removal of exact duplicates, removing 69% of NF-UNSW-NB15-v2 flows. Flows were linked in a nearest-neighbour graph built from training flows only, and validation and test flows were attached to their nearest training flows at prediction time. A two-layer residual network was compared with eight models under the same settings, including a nearest-neighbour vote over the same graph, gradient-boosted trees and a random forest, over three seeds that each draw a new split, with ablations, leave-one-family-out and feature-noise tests. On CICIDS2017 the residual network reached a binary F1 of 98.11% (SD 0.18) and on NF-UNSW-NB15-v2 90.57% (0.38), indistinguishable from a multilayer perceptron without the graph and from other graph networks. Tree ensembles were 1.48 to 1.57 F1 points higher on CICIDS2017 and led on the area under the precision-recall curve on both datasets; their CICIDS2017 multiclass macro-F1 reached 93.08% against 64.51%, a gap mainly from benign flows the residual network assigned to small attack classes. No ablation, including transductive graph construction, changed F1 beyond seed variation. Under Gaussian feature noise (SD 0.5), the residual network kept an F1 of 96.16%, while XGBoost fell to 0.67%. Under a leakage-controlled protocol, message passing over flow graphs adds no measurable accuracy over a perceptron, and tree ensembles remain stronger on both; the advantage of graph models lies in robustness to feature noise.

---


### 164. [Feature-Based and Deep Learning Methods for Astronomical Light Curve Classification](https://arxiv.org/abs/2611.04664)

**<font color=#1a73e8>作者：</font>** V. Baymakanov, Kh. Khamitov, A. Raimova 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We compare feature-based machine learning and end-to-end deep learning for variable star classification using the Zwicky Transient Facility (ZTF) StarEmbed dataset, which contains about 40,000 objects across seven imbalanced classes. Classical models trained on physically motivated features consistently outperform deep networks trained directly on raw light curves. We find that limited labeled data contributes to the performance gap, while the multivariate, irregularly sampled, and morphologically diverse nature of light curves poses additional challenges for deep learning models. While deep learning holds promise for learning representations directly from observations, our results indicate that current models fail to generalize with the available training set size. These findings motivate further investigation of the benefits of scaling labeled datasets and self-supervised pretraining on large unlabeled surveys. This work establishes a quantitative baseline for future research and highlights the need for further innovations to unlock the potential of deep learning in astronomical time series analysis.

---


### 165. [Phase-DGS: Phase-guided Dynamic Gaussian Splatting from Unsynchronized Multi-view Video](https://arxiv.org/abs/2611.04666)

**<font color=#1a73e8>作者：</font>** Hosung Jeon, Jun Young Jeong, Sangwoon Kwak 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatiotemporal scene reconstruction with Dynamic Gaussian Splatting (DGS) fundamentally depends on perfect temporal synchronization across all cameras, an assumption rarely achievable in practice. Industry-standard synchronization requires expensive specialized hardware and complex setup, while data-driven alternatives including audio-based alignment, geometry matching, and pose tracking remain limited by restrictive environmental or scene-specific assumptions. To overcome these limitations, we propose Phase-DGS, a framework that replaces conventional timestamps with a semantic phase representing each frame's inherent state within the underlying motion cycle. Frames capturing the same motion state share the same phase regardless of which camera records them or when, naturally establishing spatiotemporal correspondence across unsynchronized cameras. We validate Phase-DGS under temporal offsets, frame drops, and camera freezes, achieving up to +8.5 dB PSNR improvement over baselines while enabling seamless integration with existing DGS backbones including RealTime-4DGS and FreeTimeGS.

---


### 166. [FedCSGA: Client Selection Based on Genetic Algorithm for Federated Learning](https://arxiv.org/abs/2611.04667)

**<font color=#1a73e8>作者：</font>** Ghani Haider, Majid Kundroo, Leo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative training of machine learning models across distributed clients while preserving data privacy. In practical deployments, FL relies on selecting a subset of clients in each communication round to reduce communication cost, mitigate stragglers, and improve training efficiency under heterogeneous data and system conditions. In heterogeneous edge computing environments, both statistical heterogeneity and system heterogeneity significantly affect convergence efficiency and model performance. However, existing client selection methods often address these factors independently, overlooking their coupled and dynamic impact across communication rounds. To address this limitation, we propose FedCSGA, a Client Selection method for Federated learning based on a Genetic Algorithm. FedCSGA encodes client subsets as chromosomes and evaluates these subsets through a non-linear fitness function that jointly integrates resource-aware metrics and history-aware participation weighting. This design captures subset-level interactions, mitigates persistent selection bias, and balances statistical utility with system efficiency. Extensive experiments on FMNIST, CIFAR-10, CIFAR- 100, and Tiny-ImageNet demonstrate that FedCSGA consistently outperforms state-of-the-art baselines across diverse heterogeneity settings, achieving accuracy improvements of up to 7.0% and faster convergence with fewer communication rounds. These results validate the effectiveness of jointly modeling statistical and system factors to achieve robust and efficient learning in heterogeneous federated environments.

---


### 167. [Sheaf-MPNN: A Library for Sheaf Neural Networks as Message Passing](https://arxiv.org/abs/2611.04670)

**<font color=#1a73e8>作者：</font>** Alessio Borgi, Mario Severino, Luke Braithwaite 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard Graph Neural Networks (GNNs) implicitly assume that neighboring nodes share the same feature space, which contributes to oversmoothing and poor performance on heterophilic graphs. Sheaf Neural Networks (SNNs) remove this assumption by giving each node and edge its own vector space and learning restriction maps that transform features as they move between neighbors. These maps define a sheaf Laplacian that drives diffusion over the graph, but existing implementations often assemble it explicitly as a global sparse block matrix, which adds memory and computational overhead and can hinder scalability. In this paper, we introduce Sheaf-MPNN, a PyTorch Geometric library that reformulates sheaf diffusion as local incidence-wise transport and aggregation, eliminating the need to construct the global Laplacian. Sheaf-MPNN implements fifteen families of SNNs under a unified message-passing framework, each supporting both homogeneous and heterogeneous graphs, and directed and undirected settings, with diagonal, general, orthogonal, and low-rank restriction maps and attention-based predictors. We further provide a unified benchmarking suite covering node- and graph-level tasks, heterogeneous graph learning, and computational efficiency, enabling systematic and reproducible comparisons across architectures. We establish theoretical equivalence between these message-passing formulations and their original counterparts and identify the architectural mechanisms needed to preserve their propagation dynamics. This unified perspective provides a principled foundation for implementing, comparing, and extending sheaf-based architectures within standard graph learning frameworks. Source code is available at this https URL.

---


### 168. [CardioVascBench:Prioritized Diagnosis Generation from Real-World Chinese Cardiovascular Records](https://arxiv.org/abs/2611.04687)

**<font color=#1a73e8>作者：</font>** Minghao Kong, Muyao Chen, Jianhao Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying the primary diagnosis alone does not fully characterize a model's diagnosis-generation performance. We introduce CardioVascBench, a retrospective benchmark for prioritized diagnosis generation from real-world Chinese cardiovascular inpatient records. It contains 3,262 de-identified cases, with 2,174 for training and 1,088 for evaluation, linking clinical narratives and textual ECG reports to expert-verified, ordered discharge diagnoses standardized to ICD-10. An English translation of the evaluation set supports aligned cross-lingual comparison. Our evaluation protocol combines terminology normalization and rank-aware scoring to separately assess primary-diagnosis identification, reference-diagnosis coverage, and list precision. Evaluation across 36 systems shows that higher primary-diagnosis accuracy does not necessarily imply higher list precision against discharge references. We also provide CardioKG-Agent, a knowledge-enhanced baseline combining entity normalization, constrained graph retrieval, and guideline evidence. In a staged comparison of three baseline models, supervised fine-tuning plus the agent achieves a 73.5% higher mean composite score than fine-tuning alone, representing a system-level gain. These results measure retrospective agreement with recorded diagnoses; agreement between metric rankings and physician judgments remains to be validated. CardioVascBench supports research on diagnosis prioritization and knowledge-enhanced generation.

---


### 169. [Uncertainty-Aware Prototype Learning for Open-Set Test-Time Adaptation](https://arxiv.org/abs/2611.04689)

**<font color=#1a73e8>作者：</font>** Jinwu Hu, Langyu Bian, Jian Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Open-set test-time adaptation (TTA) aims to adapt source-trained models to unlabeled test streams where covariate-shifted in-distribution (csID) samples and covariate-shifted out-of-distribution (csOOD) samples may coexist. Existing TTA methods are typically designed under a closed-set assumption and therefore lack explicit mechanisms for reliably distinguishing csID from csOOD samples. Consequently, csOOD samples may be mistakenly included in confidence-enhancing adaptation, producing harmful gradients that degrade known-class performance. To address this, we propose Uncertainty-Aware Prototype Learning for Open-Set Test-Time Adaptation (UAPA), a plug-and-play method for reliable open-set adaptation. Specifically, we first introduce Uncertainty-Driven ID/OOD Separation, which combines a classifier-prototype score with a mini-batch-normalized evidence-derived uncertainty score to distinguish csID from csOOD samples. We then propose a Dynamic Prototype Refinement strategy that periodically refines class-specific target prototypes using buffered csID features to progressively follow the estimated class directions. Lastly, we introduce Contrastive Prototype Entropy Adaptation, which applies entropy minimization to csID samples and entropy maximization to csOOD samples, while prototype-level contrastive learning aligns csID features with their corresponding target prototypes and reduces the maximum similarity between csOOD features and known-class prototypes. Empirically, UAPA outperforms the strongest baselines on the CIFAR benchmarks and Tiny-ImageNet-C, improving average OSCR by 2.08 and 1.28 percentage points, respectively.

---


### 170. [Just Between Us? Exploring a Wearable-Mediated Channel for Discreet Human-Agent Interaction in a Shared Game Setting](https://arxiv.org/abs/2611.04692)

**<font color=#1a73e8>作者：</font>** Atikkhan Faridkhan Nilgar, Manuel Dietrich, Kristof Van Laerhoven  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In shared settings, social robots may need to exchange information with an individual while limiting co-present others' access to or interpretation of that information. Publicly observable speech and gestures may not adequately support such exchanges. We investigate a wearable-mediated channel for discreet interaction that combines in-ear audio messages with deliberate rightward head tilts as responses. To examine its feasibility and participants' experiences, we studied 20 pairs (40 participants) playing a card game with a screen-based conversational agent representing a social robot, controlled by a researcher in a Wizard-of-Oz setup. Each pair played with and without the channel. One participant wore the device (the wearer), while the other (the non-wearer) was informed about the channel after gameplay. The channel conveyed information that could help the wearer or robot character select an opponent they could defeat. The information exchange and subsequent opponent selection occurred as intended in 39 of 40 channel-mediated turns. Wearers reported low perceived pressure/tension in both conditions, with no statistically significant difference between conditions, and favorable usability immediately after use. Retrospective interviews, however, revealed varied accounts of noticing the interaction among non-wearers and contrasting perceptions of teamwork and unfairness. These findings support the feasibility of wearable-mediated exchanges within this game and identify awareness and fairness as considerations for future designs.

---


### 171. [Surrogate Models for Stochastic Al-Cu Phase-Field Solidification](https://arxiv.org/abs/2611.04695)

**<font color=#1a73e8>作者：</font>** Simon Savukoski, Tatu Pinomaa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Phase-field models resolve microstructural evolution during rapid alloy solidification, but their computational cost limits long trajectories, stochastic ensembles, and studies across process conditions. We present a variance-preserving denoising diffusion bridge model (VP-DDBM) for state-conditioned prediction of two-dimensional Al-Cu solidification. Given the current phase, concentration, and prescribed temperature fields, the model predicts the subsequent state and is applied autoregressively. Across two held-out thermal gradients, VP-DDBM produces lower long-horizon errors than deterministic U-Net and SI-ConvNeXt baselines in domain-mean phase, domain-mean Cu concentration, and leading-tip position. It also retains fine dendritic structure over long rollouts, whereas the deterministic U-Net progressively smooths the morphology. VP-DDBM predicts the phase and concentration evolution approximately $73\times$ faster than the phase-field solver, showing potential for faster process-condition screening and ensemble-based microstructure studies.

---


### 172. [Learning from Unlabeled Photographs for General Oral Image Analysis](https://arxiv.org/abs/2611.04709)

**<font color=#1a73e8>作者：</font>** Zhong-Shi Zhang, Zi-Li Yu, Xiao Xiao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Oral photographs contain rich clinical information and hold significant potential for artificial intelligence applications; however, most models are trained for individual tasks and rely on costly expert annotations. We hypothesized that self-supervised training on unlabeled oral photographs could produce transferable visual representations for heterogeneous vision tasks. To test this hypothesis, we developed DOVE (Dental Optical Visual Encoder) by domain-adaptive self-supervised pretraining on approximately 530,000 unlabeled oral photographs collected from publicly accessible sources. DOVE was benchmarked against 3 established baselines across 5 classification datasets and 4 segmentation datasets, covering both frozen backbone evaluation and end-to-end finetuning. DOVE achieved the strongest overall performance, ranking best in few-shot transfer and label efficiency on most benchmarks. Under the 20-shot frozen-backbone protocol, DOVE outperformed the second best DINOv3 by 4.37 percentage points in mean macro-F1 across classification datasets and by 4.49 percentage points in mean macro-Dice across segmentation tasks. Under end-to-end finetuning, DOVE achieved at least 80% of the strongest full-data baseline's performance across most evaluation datasets using only 10% of the labeled training data. Qualitative retrieval and feature analyses further indicated better organization of image-level and spatial representations. These findings support DOVE as a generalizable and label-efficient backbone for oral vision research.

---


### 173. [DenseTwins: Dense Modality Decoupling for Multimodal Self-Supervision](https://arxiv.org/abs/2611.04710)

**<font color=#1a73e8>作者：</font>** Carlo Sgaravatti, Daniele Kopyshevskiy, Davide Secco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal perception is central to many computer vision applications, including robotics and autonomous driving, where different sensing modalities provide complementary cues. Self-supervised learning offers a scalable solution for exploiting large amounts of unlabeled multimodal data. However, existing methods either neglect modality-specific information by enforcing feature-space alignment between modalities or learn only global representations without preserving spatial structure. We propose DenseTwins, a multimodal self-supervised framework that learns dense representations by explicitly decoupling the dense feature space into shared and modality-specific components. The proposed approach combines dense cross-modal correspondences with redundancy-reduction objectives, enabling the model to capture both shared semantics and modality-specific cues within a structured dense embedding space. DenseTwins jointly optimizes an intra-modal objective across augmented views and a cross-modal objective that aligns shared features while decorrelating modality-specific information. We evaluate DenseTwins across multiple multimodal benchmarks and sensing setups, achieving state-of-the-art or competitive performance across multimodal self-supervised baselines. Code available at: this https URL.

---


### 174. [Cycle WAM: Coupling Action and Video through Cycle Consistency](https://arxiv.org/abs/2611.04711)

**<font color=#1a73e8>作者：</font>** Qinglin Yang, Jiepeng Wang, Yuxing Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video modeling have driven substantial progress in world action models (WAMs). Existing approaches exploit pretrained video priors by decoding actions from latent representations or inferring them from generated videos. The underlying link is causal: robot actions produce changes in the scene, and video observations of these changes provide evidence for inferring the actions that produced them. However, existing training formulations do not by themselves ensure that actions and their predicted visual consequences are consistent, potentially limiting the use of pretrained capabilities. We treat video and action as paired modalities linked by this causal relationship and learn their correspondence through a unified training framework designed to better exploit pretrained video priors. Cycle WAM first augments video-action co-training with bidirectional conversion to reinforce cross-modal correspondence and recover forward and inverse dynamics. It then introduces a differentiable cycle-reconstruction objective to further couple the two mappings. The resulting model supports both forward and inverse dynamics, with the potential to improve performance through more effective use of pretrained video priors. Cycle WAM achieves state-of-the-art performance among comparable methods on LIBERO-Pro and substantially improves DreamZero on DROID. Comparisons with UWM characterize its inverse-dynamics performance and show sharper visual detail in the displayed forward-dynamics predictions.

---


### 175. [VISAGE: Vertex-based Intrinsic Surface Appearance GEneration via Dual-Stream Diffusion for Arbitrary 3D Heads](https://arxiv.org/abs/2611.04712)

**<font color=#1a73e8>作者：</font>** Jeremias Krauß, Pragati Jaiswal, René Schuster 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering identity-faithful, physically based surface appearance for 3D human heads from sparse images remains challenging. Existing methods often rely on UV-based pipelines, introducing seam artefacts, or operate in image space, limiting surface consistency. We present VISAGE, Vertex-based Intrinsic Surface Appearance GEneration, a surface-based conditional diffusion framework that synthesises per-vertex albedo and roughness directly on arbitrary mesh topologies, without requiring consistent UV parameterisation at training time. VISAGE combines global spectral processing with local geodesic K-Nearest-Neighbour refinement, enforcing structural coherence while restoring detail beyond the truncated spectral basis. Multi-view RGB images condition the network via visibility-aware cross-attention, enabling occlusion-robust synthesis across the full head surface. Region-specific modules specialise in semantically demanding and distinct areas (eyes, mouth, skin and hair), while a tangent-space output projection recovers fine iris detail. We further introduce a scalable procedural augmentation pipeline that enriches raw geometry scans with physically plausible albedo, roughness and normal maps for training. The predicted attributes render directly as a single RGBA vertex-colour channel. VISAGE reduces FID by 42.7% on NPHM and 22.5% and 4.4% on zero-shot FaceVerse and i3DMM, respectively, relative to the strongest baseline, with a 7.2M-parameter core network.

---


### 176. [TEXMET: A Deep Learning Benchmark for Archaeological Textile Reconstruction](https://arxiv.org/abs/2611.04734)

**<font color=#1a73e8>作者：</font>** Muhammad Hamza Zafar, Davit Gigilashvili, Jon Yngve Hardeberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The reconstruction of fragmented historical textiles presents a significant challenge in computational archaeology. The Oseberg ship burial, dating to 834 CE, yielded hundreds of degraded textile fragments that have resisted systematic computational analysis. While deep learning has revolutionized image-based puzzle solving, progress on archaeological textiles has been limited by the lack of domain-specific datasets and systematic evaluation of modern architectures. To address this gap, we present TEXMET, a curated dataset of 18,644 historical textile images from the Metropolitan Museum of Art's Open Access collection, representing the first textile-specific benchmark for puzzle-solving research. Using TEXMET, we conduct a systematic evaluation of three state-of-the-art puzzle-solving models: JPDVT, FCViT, and DiffAssemble. Our experiments reveal that the transformer-based models pre-trained on standard datasets fail to generalize to textiles, but domain-specific fine-tuning proves highly effective. The graph-based DiffAssemble model, when fine-tuned on TEXMET, achieves 85.89% puzzle accuracy on textile data. Most significantly, applying this fine-tuned model to 45 highly degraded Oseberg fragments yields a performance increase from 26.67% to 64.44% puzzle accuracy. These results establish TEXMET as a new benchmark for textile reconstruction and demonstrate that domain adaptation is essential for applying puzzle-solving methods to imagery of real archaeological materials.

---


### 177. [TAPES: Task-Aligned Joint Predictive Pretraining for Transaction Event Sequences](https://arxiv.org/abs/2611.04747)

**<font color=#1a73e8>作者：</font>** Ruobing Zuo, Weiyu Han, Huilin He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transaction event sequences support diverse prediction tasks in online commerce and digital financial services. The same transaction records can yield prediction targets with different semantics, including values, changes, and relations to past events. These targets impose different constraints on history representations, but their predictability alone does not establish the downstream utility of a target set. Moreover, target-wise prediction losses do not explicitly model conditional co-occurrence among targets. To address these challenges, we propose TAPES, a task-aligned joint predictive pretraining framework for transaction sequences. TAPES constructs a finite collection of candidate target sets from admissible field-operator combinations. It selects a target set according to the downstream utility of representations learned through short joint pretraining trials under matched budgets. It then reinitializes the encoder and pretrains it on the selected targets through a joint likelihood parameterized by a shared discrete latent variable, before downstream supervised adaptation. Experiments in a real-world transaction-risk setting and on multiple public financial benchmarks spanning diverse downstream tasks demonstrate that TAPES outperforms representative baselines. Ablation studies further validate the contributions of predictive target selection and joint modeling.

---


### 178. [What Does It Mean to Remove an Edge? Intervention-Aware Fidelity for Graph Neural Network Explanations](https://arxiv.org/abs/2611.04751)

**<font color=#1a73e8>作者：</font>** Rocco Mattia Di Mauro, Marco Grassia, Giuseppe Mangioni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural network explanations are often evaluated via deletion fidelity, i.e., by deleting their top-ranked edges and measuring the resulting change in model output. Yet, in a message-passing GNN, "deleting an edge" does not specify a unique intervention. Structural deletion removes the edge from the graph and recomputes quantities such as degree normalization and attention, whereas message suppression leaves this structural context intact while blocking the message carried by the edge. The meaning of deletion fidelity therefore depends on what the intervention targets in the model computation. We formalize this distinction and derive sufficient conditions for exact equivalence. The two interventions coincide for additive message passing with edge-set-independent coefficients, but can diverge when aggregation depends on the presence of zero messages or when removing an edge changes the coefficients applied to surviving messages. We then construct intervention-specific edge attributions and evaluate each resulting ranking under both interventions, testing whether their relative fidelity changes with the evaluation intervention. Across nine datasets and a panel of GIN, GCN, and GATv2 models at depths 2--5, all nine GIN controls satisfy the equivalence predicted by the theory. On the target logit, the relative fidelity of the two rankings depends on the evaluation intervention in 10 of 11 reportable GCN and GATv2 cells, and in nine of them each ranking has the larger deletion area under the intervention it was built with. Deletion fidelity is thus not a property of an edge ranking alone. Evaluation protocols should explicitly report the intervention, output functional, target, and perturbation unit, and test alternative intervention semantics when the scientific question does not uniquely determine one.

---


### 179. [Bounded AUKS: A Novel Evaluation Metric for Anomaly Detection via Bounded Area Under the Kolmogorov--Smirnov Curve](https://arxiv.org/abs/2611.04754)

**<font color=#1a73e8>作者：</font>** Yanshuo Zhang, Juan Du  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent literature widely used global metrics such as AUROC and AUPRO to quantify the detection performance. AUROC and AUPRO scores are approaching 100% in some public datasets such as MVTec AD dataset and VisA dataset, which misleadingly suggests that the pixel-level anomaly detection task has already been solved. Threshold-independent metrics represented by AUROC inherently ignore the threshold selection process, which is inevitable in practical applications. Although AUPRO restricts the False Positive rates (FPRs) to an acceptable range, extremely low FPRs can lead to increased false negative rates (FNRs). We argue that there is a lack of metrics capable of quantifying the separation between the anomaly score distributions of normal and anomalous samples, which hinders advancements in anomaly detection. In response, we propose the Bounded Area Under the Kolmogorov--Smirnov curve (Bounded AUKS), a partial integral metric that integrates the difference between TPR and FPR within a data-driven bounded range. Specifically, we introduce AUKS from KS integral as a direct measure of separability between the anomaly score distributions. The bounded range is determined only by score distributions of normal test samples. Lower bound excludes the uninformative high-FPR region. Upper bound avoids evaluation in extreme regions that aggressively push FPR towards zero, which result in a very low recall. Our experiments on 9 models across MVTec AD and VisA datasets show that Bounded AUKS can address the limitations of existing metrics and has a better performance in evaluating unsupervised anomaly detection models.

---


### 180. [iMED: A Multi-Endoscope Dataset for Surgical 3D Perception](https://arxiv.org/abs/2611.04755)

**<font color=#1a73e8>作者：</font>** Sierra Bonilla, Fengyi Jiang, Chinedu Nwoye 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce iMED, the first synchronized multi-endoscope dataset for robot-assisted minimally invasive surgery (RAMIS), designed to address a fundamental limitation in surgical vision benchmarking: the absence of independent held-out viewpoints. Existing surgical datasets capture single-trajectory sequences from a single endoscope, making it impossible to distinguish geometric generalization from photometric interpolation along a narrow forward-facing path. iMED provides 340 sequences ~170K synchronized timepoints with 4 views per timepoint) recorded simultaneously from two independent stereo endoscopes across ex vivo, postmortem, and live surgical settings, spanning 14 specimens with diverse anatomical regions and motion regimes. The dataset includes calibrated camera intrinsics, ArUco-based frame-wise pose estimates with uncertainty quantification, instrument segmentation masks, and rich clinical metadata. Using a train-on-one-endoscope, test-on-another evaluation protocol, we benchmark 23 state-of-the-art methods across rigid and deformable novel view synthesis, pose estimation, feature matching, and monocular depth estimation. Our experiments show that methods relying primarily on photometric supervision degrade substantially under this held-out-endoscope setting, while methods with explicit geometric regularization are more robust across views in our benchmark. Notably, large-scale foundation models transfer surprisingly well to surgical imagery, often outperforming domain-specific models, suggesting pitfalls in current fine-tuning protocols. iMED establishes a new evaluation protocol for geometric generalization in surgical vision.

---


### 181. [Non-Interfering Asymmetric AdamW Updates for Constrained Exploration of Equifinality in Hybrid Models](https://arxiv.org/abs/2611.04756)

**<font color=#1a73e8>作者：</font>** Ekaterina Gikalo, Zavud Baghirov, Christian Reimers 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid models let neural networks supply the unresolved parameters of a process-based simulator, and are fitted to observations that constrain aggregate fluxes and storages but not the internal partitioning that produces them. Such a fit is equifinal: configurations indistinguishable in the observed aggregates can disagree substantially about the unobserved internals, and therefore about the mechanism they attribute to the same data. We study evapotranspiration, whose total flux is observed while its split into transpiration and evaporation is not. A model ensemble built from random seeds alone spans only a narrow band of the partitionings the data admit. We produce the spread deliberately, training members under auxiliary repulsion on transpiration, subject to the fit to observations not degrading. Non-interference is usually arranged by making the auxiliary gradient orthogonal to the main one, but under AdamW the applied step is a preconditioned momentum direction, so orthogonality between raw gradients no longer implies it. We introduce Non-interfering Asymmetric Network Optimization (NANO), an update whose first-order effect on the main loss is exactly that of the main objective alone, whose auxiliary step is bounded, and which concentrates repulsion in the coordinates the main gradient leaves idle.

---


### 182. [Koopman Generative Operators for Efficient Probabilistic Time-Series Forecasting](https://arxiv.org/abs/2611.04760)

**<font color=#1a73e8>作者：</font>** Raz Marshanski, Liran Nochumsohn, Mayank Jauhari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic time-series forecasting requires models that simultaneously capture structured temporal dynamics, expressive uncertainty, and efficient inference, yet existing approaches fall short of this goal: latent dynamical models impose structure but rely on restrictive generation mechanisms, while modern generative methods such as diffusion and flow matching achieve flexibility at the cost of iterative and computationally expensive sampling. We introduce the Koopman Generative Operator (KGO), a probabilistic forecasting method that conceptualizes prediction as the evolution of structured uncertainty. KGO integrates three core components: (1) Koopman Patch Embedding (KoPE) for temporally consistent latent trajectory extrapolation; (2) Koopman Flow Matching (KoFM), which enables fast, single-step generation through a closed-form matrix exponential in a Koopman latent space, bypassing iterative sampling; and (3) an Adaptive Uncertainty Gate (AUG), which provides probabilistic forecasts by adapting uncertainty per-variable and per-horizon, corresponding to a learned decomposition of aleatoric uncertainty without manual tuning. By unifying these components, KGO achieves state-of-the-art accuracy on 13/17 ProbTS benchmarks in CRPS and 16/17 in NMAE. Further, by eliminating iterative sampling, KGO delivers at least a 25$\times$ reduction in inference time compared to iterative generative models. These results position KGO as a practical and principled framework that advances the accuracy-efficiency trade-off in probabilistic time-series forecasting, combining leading accuracy on the evaluated benchmarks with fast, single-step generation.

---


### 183. [Pixel-space video generation with U-JiT](https://arxiv.org/abs/2611.04764)

**<font color=#1a73e8>作者：</font>** Théophane Vallaeys, Jakob Verbeek, Matthieu Cord  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Latent diffusion and flow matching models are ubiquitous in state-of-the-art generative video models. While highly effective, relying on pretrained autoencoders to compress the data into a lower-dimensional latent space also comes with drawbacks. First, training proceeds in two stages: autoencoder pretraining, with compression and reconstruction objectives, followed by latent generative model training, precluding fully end-to-end training. Second, autoencoders also lead to an inherent loss of signal, and the trade-off between reconstruction quality and generative performance in the latent space is still an active area of research. In this paper we explore the viability of generative video models directly in pixel space. We analyze recent approaches in pixel-space generative modeling of images that rely on basic transformer designs, and identify several shortcomings that limit their effectiveness for the high-dimensional pixel-space video generation. To overcome these limitations, we propose a UNet-like transformer architecture along with improvements to the training recipe and sampling strategy. We conduct controlled experiments, training latent and pixel-space models from scratch on Kinetics-600. For the standard frames-to-video task at 128 resolution, our U-JiT model improves generative FVD by 27% over prior state-of-the-art results, and by 14% against the JiT pixel-space baseline. Scaling to higher 256 resolution, we find the improvement over pixel-space and latent-based models grows as we increase the spatiotemporal compression rate up to $64 \times 64 \times 8$. Finally, we find that U-JiT improves per-frame FID by 27% over latent models and 61% over pixel-space models on class-to-video generation, with respectively 9% and 56% reduction in FVD.

---


### 184. [Cooperative Multi-Agent Reinforcement Learning with Submodular Trajectory Rewards](https://arxiv.org/abs/2611.04774)

**<font color=#1a73e8>作者：</font>** Yasaman Zolfimoselo, Nikolas Geroliminis, Maryam Kamgarpour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study cooperative multi-agent reinforcement learning with decoupled dynamics and a monotone submodular reward function over joint trajectories. Due to the non-additive reward, an optimal policy may depend on the history of all agents. This dependence makes exact optimization exponential in the horizon and the number of agents. To overcome this challenge while retaining theoretical guarantees, we introduce pre-window curvature $c_m$, which quantifies how states visited more than $m$ steps earlier reduce current marginal gains. Using this curvature to control the error from restricting the policy of each agent to depend only on its last $m+1$ states, we propose a greedy algorithm that exploits the decoupled dynamics to optimize local policies sequentially. For fixed $m$, the algorithm achieves a $\frac{1-c_m}{2-c_m}$ approximation guarantee up to estimation error, and its computation time is polynomial in the number of agents and the horizon. We recover the known $1/2$-factor approximation for time-additive rewards and obtain an approximation factor no smaller than the known total-curvature bound for a single agent. We formulate multi-agent traffic monitoring as an example of this framework and evaluate our algorithm on it.

---


### 185. [On the Complexity of Finite-Sum Nonconvex-Strongly-Concave Minimax Optimization with Exact Proximal Oracles](https://arxiv.org/abs/2611.04806)

**<font color=#1a73e8>作者：</font>** Yuxing Peng, Zhiqing Tang, Weijia Jia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Finite-sum nonconvex-strongly-concave minimax problems arise in adversarial training and distributionally robust learning. Their known lower bounds cover only linear-span algorithms, zero-respecting algorithms, or a restricted proximal protocol. They leave open the power of exact component proximal steps, whose responses are global saddle points of regularized component problems and can expose directions that gradients do not reveal. We show that neither unrestricted adaptivity nor exact proximal access improves the polynomial complexity. We consider $n$ components with joint mean-squared smoothness $L$ and condition number $\kappa$, started from a point with primal gap at most $\Delta$ and joint gradient norm at most $\sqrt{2L\Delta}$. For $\varepsilon^2/(L\Delta)$ below a universal constant, every randomized adaptive algorithm with exact component values, gradients, and proximal responses needs $\Omega(n+\min\{\sqrt n\,\kappa,n^{3/4}\sqrt\kappa\}L\Delta/\varepsilon^2)$ component queries in the worst case to find an $\varepsilon$-stationary point of the value function. A method using only component gradients attains this rate up to a factor $\log^2(2+\kappa)$, including initialization. Zhou (arXiv:2610.04944) concurrently proves the same rate for zero-respecting first-order methods. In our hard instances, every component admits proximal steps with the same step sizes, and a response for a component reveals hidden directions only up to the first one assigned to another component.

---


### 186. [RAHC: Rule-Augmented Hyper-Relational Knowledge Graph Completion for Materials Synthesis](https://arxiv.org/abs/2611.04809)

**<font color=#1a73e8>作者：</font>** Jiawei Sun, Sijia Xu, Zihan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery depends on reusing experimental knowledge, yet records scattered across papers and repositories are often incomplete. In materials synthesis, recovering missing conditions requires reasoning about the target material and the observed context of a specific experiment. Hyper-relational knowledge graphs (HKGs) represent this context through qualifiers, but existing completion methods leave domain knowledge and experimental regularities implicit. We propose RAHC, a rule-augmented HKG framework for single-slot and joint multi-slot synthesis-condition completion. RAHC builds a traceable rule catalog from training records and retrieved literature, retrieves rules for each query-candidate pair, and separately encodes graph structure and rule evidence. Hard rules constrain candidate validity, while soft rules guide ranking. RAHC-G aggregates rules using global reliability; RAHC-Q additionally learns query-specific relevance. Gated fusion combines structural and rule representations, while tuple-conclusion rules provide cross-condition evidence for joint completion. Experiments on five materials-synthesis datasets show improvements in single-slot and joint completion under Semi-inductive and Open-Answer Inductive settings, with Semi-inductive MRR gains of up to 15.6% over MAYPL. RAHC also improves performance on the entity-disjoint ILPC'22 Small benchmark, supporting transfer to fully inductive KG completion. These results support experimental condition selection, synthesis planning, and the reuse of scientific knowledge.

---


### 187. [AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests](https://arxiv.org/abs/2611.04813)

**<font color=#1a73e8>作者：</font>** Shu Zhou, Ziyang He, Yuxin Rao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial agents are becoming an important class of real-world AI systems. Financial tasks vary widely in type and difficulty, and many are open-ended with no ground-truth answers. However, existing benchmarks neither capture this breadth and open-endedness nor separate grounding from correctness. To bridge this gap, we introduce $\textbf{AgenticFinBench}$, a benchmark of 230 real-world financial tasks spanning 8 categories, 2 languages, and 4 complexity levels. We also propose a reference-free evaluation framework that combines question-specific rubrics with a two-stage claim audit that detects hallucinations, defined as claims absent from the agent's trace and refuted by external evidence. This framework better matches how financial work is assessed in practice. Experiments across 18 agent configurations reveal three key findings: (1) Ignoring hallucinations can overstate agent performance: hallucination auditing lowers the baseline leader's score by 7.58 points and moves it to fourth place. (2) Harness differences explain more variation in evidence grounding than model differences (28.6% vs 8.8%). (3) Quality scores fall from 89.44 on direct retrieval to 79.18 on the most complex tasks. Case studies show that agents struggle to explain how events affect company profits or stock prices, compare financial data on a consistent basis, and justify their conclusions. By releasing AgenticFinBench, we aim to advance financial reasoning, factual verification, and agent design for more reliable responses to diverse real-world financial requests. Our project page is at $\textbf{this https URL}$.

---


### 188. [Sleep-Disordered Breathing Detection with Quantum Recurrent Neural Networks](https://arxiv.org/abs/2611.04818)

**<font color=#1a73e8>作者：</font>** Alejandro Mayorga-Redondo, José Daniel Viqueira, Diego Alvarez-Estevez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work investigates the application of Quantum Recurrent Neural Networks to the binary classification of sleep-disordered breathing events in time-series data, aiming to distinguish between apneic and normal breathing episodes. A variational classical--quantum architecture is proposed and evaluated against classical Recurrent Neural Network models. Experiments were conducted on multiple real-world datasets with varying levels of complexity to assess the strengths and limitations of the quantum approach. In the comparative analysis, both classical and quantum models showed comparable performance. The quantum model achieved superior performance on the smallest dataset, while yielding slightly weaker results in the most complex setting. However, the quantum approach exhibited notable strengths, such as competitive performance despite a drastically reduced parameter count and low-qubit regime, as well as good generalization capabilities. These results suggest that, despite current hardware and algorithmic limitations, variational quantum recurrent models represent a promising alternative for time-series classification as Quantum Computing technologies continue to mature.

---


### 189. [Reconstructing Fraudulent Strategies in Online Payments via Interpretable Inverse Reinforcement Learning](https://arxiv.org/abs/2611.04819)

**<font color=#1a73e8>作者：</font>** Huilin He, Weiyu Han, Linbo Shao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Payment fraud causes financial losses and undermines users' trust in web payment services. Although fraud detection is a critical defense for payment security, complex and diverse fraudulent behaviors can still evade detection. Generating fraud samples for data augmentation can broaden detectors' coverage of different fraud patterns. However, existing methods matching the distribution of transaction attributes alone do not ensure that generated sequences preserve the sequential relationships among transaction choices, payment feedback, and subsequent behavioral adjustments. To this end, we propose PaySeqGen, an interpretable inverse reinforcement learning framework that reconstructs fraud behavior policies from fraudsters' observed payment trajectories. We design a mechanism for constructing candidate actions to support plausible payment sequence generation while enabling exploration. The framework also learns interpretable behavioral rewards that capture fraudsters' preferences across different transaction contexts. By alternating between reward learning and policy optimization, the framework reconstructs policies that generate new fraud sequences for detector augmentation and learns interpretable rewards supporting sequential fraud-pattern analysis in real trajectories. Experiments in real-world payment scenarios at Ant International, a leading global digital payment provider, show that PaySeqGen outperforms state-of-the-art generative augmentation methods. Reward-based trajectory analysis also identifies fraud patterns of practical value, helping analyst locating suspicious segments and examine multistep fraud tactics. Evaluation in the deployed system of online payment further confirms its effectiveness.

---


### 190. [Radial distortion homography estimation from affine-covariant or orientation-covariant features](https://arxiv.org/abs/2611.04822)

**<font color=#1a73e8>作者：</font>** Marcus Valtonen Örnhag, Stefan Adalbjörnsson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present minimal solvers for joint homography and radial distortion estimation using affine- or orientation-covariant features. The core contribution is a set of novel constraints that exploit local feature geometry inherent to affine descriptors, enabling solvers that require fewer correspondences than point-based methods. Using modern robust estimation frameworks, we demonstrate that the proposed solvers are advantageous to the current state-of-the-art with a significant speed-up in the presence of outliers while maintaining comparable or superior estimation accuracy. The proposed solvers are tested on both synthetic and real images containing challenging fisheye distortions.

---


### 191. [Anomaly Detection on Resource-Constrained Devices with Reservoir Computing](https://arxiv.org/abs/2611.04835)

**<font color=#1a73e8>作者：</font>** Marco Angioli, Mathias Persson, Hiroto Tamura 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection at the edge requires the deployment of models that achieve competitive performance, while minimizing computational cost and memory footprint. In this article, we investigate the suitability of the Mahalanobis Distance of Reservoir States (MDRS), an unsupervised time-series anomaly detection method, for resource-constrained devices and propose two optimizations to reduce its computational requirements. Specifically, we replace random reservoir connectivity (MDRS-Rand) with a circular shift (MDRS-Circ) and show that the anomaly score for an entire time series can be computed from the final reservoir state alone. Furthermore, we show that exploiting the reservoir's temporal memory enables more efficient input preprocessing, further reducing computational cost. We evaluate the MDRS variants on the MLPerf Tiny anomaly detection benchmark against the reference autoencoder and other anomaly detection methods, and deploy their inference kernels on a NUCLEO-F401RE microcontroller to assess latency, estimate energy consumption, and measure memory footprint. Among the evaluated methods, only MDRS and the autoencoder meet the benchmark's performance target, with MDRS requiring fewer operations and smaller models. With optimized preprocessing, MDRS achieves an ROC AUC of 0.869, a model size of 24 KB, an estimated energy consumption of 24 uJ per inference, and a latency of 0.32 ms, corresponding to a 75.9x speedup over the autoencoder with standard preprocessing.

---


### 192. [HTCE: Homeomorphism-inspired Topological Cross-Scene Experience Canonicalization and Reuse for Object Navigation](https://arxiv.org/abs/2611.04836)

**<font color=#1a73e8>作者：</font>** Xiaoran Xu, Yupeng Wu, Tianyu Xue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As embodied agents perform object-goal navigation across residential environments, they accumulate successful experiences whose semantic structure recurs across scenes even when geometric trajectories do not. Reusing such experience is challenging because differences in region naming and observation granularity produce distinct graph representations of similar approaches, while meaningful differences in anchors, branches, and endpoints must stay distinguishable. We introduce HTCE, a homeomorphism-inspired topological framework that canonicalizes and reuses navigation experience. Feature and topology subdivisions characterize representational variations, and their semantically constrained reductions produce comparable semantic sequences and structural signatures while preserving semantic anchors, branching relations, and navigation endpoints. HTCE then retrieves historical successful approaches through subdivision-aware matching as guidance for a frozen vision-language policy. Canonicalization compresses the experience index losslessly, merging 17.7--23.6\% of distinct stored route descriptions while retaining full task performance. Under a single frozen vision-language backbone shared by all compared systems, HTCE attains the best SR and SPL in every setting---59.9\%/31.8\% on HM3D v0.1, 71.0\%/31.5\% on HM3D v0.2, and 46.6\%/16.6\% on MP3D---with SR gains of up to 4.9 points and structured retrieval contributing up to 2.8 SPL points. The code is available in this https URL

---


### 193. [Found by Search, Broken by a Shortcut: Transfer and Tampering of Searched Intrinsic Rewards](https://arxiv.org/abs/2611.04838)

**<font color=#1a73e8>作者：</font>** Chase J. Metoyer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a search over innate drives find intrinsic rewards that help a reinforcement-learning agent learn, transfer to a task it never saw, and resist an exploit that was absent during the search? Each candidate reward combines four generic events (a new view, a pickup, a drop and a toggle), each with a weight, a relief and a refill rate. We ran three pre-registered stages; the search protocol was locked in a public, timestamped commit before any search result existed. CMA-ES and an equal-budget random search used 1,560 PPO training runs, and the final evaluation and tamper test used 340. On the held-out task, KeyCorridorS3R2, the CMA-ES-selected reward (E) beat task-only PPO, episodic novelty and the random-search-selected reward (R) in all 3 registered comparisons, all of them meaningful by the registered size rule. Among these generic rewards E transferred best; the earlier paper's satiation reward, which on this task is given hand-wired key and locked-door events, did better (20 of 20 seeds solved against 4 of 20; descriptive). On UnlockPickup, where that reward uses generic events, E's mean area exceeded it by 0.276 (descriptive). On the training tasks there was no registered difference between E and R: both E-over-R tests missed. A free reset action, absent during the search, collapsed E's learning on DoorKey-8x8 (mean area 0.829 without it, 0.136 with it; registered) to below task-only PPO (descriptive). The searched drives helped on every task tested, but a reward given task-specific events did better on the held-out task, and selection gave E no protection against an exploit absent from the search.

---


### 194. [DGC-Net: Cross-Modal Dynamic Routing with Global-Guided Compensation in Multimodal Sentiment Analysis](https://arxiv.org/abs/2611.04841)

**<font color=#1a73e8>作者：</font>** Linan Zhu, Huaijing Wu, Xiao Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> User-generated videos, including opinion vlogs and video reviews, provide a rich source of people's attitudes toward products, services, and social topics. Understanding the sentiment expressed by speakers is important for analyzing online opinions, as transcripts alone may not capture the attitude and intensity conveyed through vocal tone and facial expressions. Multimodal sentiment analysis (MSA) addresses this need by integrating textual, acoustic, and visual cues. However, these cues are often subtle, noisy, and inconsistent across modalities. Existing local affective cue modeling methods typically operate within individual modalities and overlook global contexts from other modalities. This may cause cross-modal affective cue inconsistency. Hierarchical global-local fusion methods integrate global semantics with fine-grained local affective cues. However, they commonly determine the relative contributions of the two representations implicitly, preventing the global-local contributions from adapting to the sample-dependent reliability of local cues and resulting in either insufficient use of informative local cues or excessive interference from unreliable ones. To address these issues, we propose DGC-Net, a Dynamic Gating and Global-Guided Compensation Network for MSA. DGC-Net mitigates cross-modal affective cue inconsistency through cross-modal contribution-aware dynamic expert routing. This mechanism uses auxiliary global contexts to guide local expert selection. Moreover, global-guided dynamic compensation fusion alleviates sample-dependent global-local contribution imbalance while preserving global semantic as the primary anchor and adaptively incorporating expert-refined local cues. Experiments on five multimodal benchmark datasets demonstrate the effectiveness and general applicability of DGC-Net, and ablation studies verify the contribution of each proposed component.

---


### 195. [One Assistant, Many Memories: Benchmarking Real-World Group Assistance When Recall Is Not Enough](https://arxiv.org/abs/2611.04867)

**<font color=#1a73e8>作者：</font>** Zhanghao Hu, Linhai Zhang, Qian Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The value of memory lies not only in recall but in using it to provide appropriate assistance. Recent benchmarks test memory use in personalisation and agentic tasks, but seldom evaluate assistance without fixed answers or integration across multiple participants. Group chats make both challenges more acute: an assistant must integrate information from multiple members, track revisions and conflicts over time, and produce one response for the group. Yet existing group memory benchmarks rely on synthetic conversations and inherit constrained evaluation from general memory benchmarks, focusing on recall against fixed answers or decisions over a closed set. We introduce GroupAssistBench, the first memory benchmark from real-world group conversations with a deployed group assistant, covering 80,299 messages in 50 groups and costing over $53K. Over the same histories, GroupAssistBench evaluates memory recall (L1) with reference answers and memory use (L2) with service requests without fixed answers across single, distributed, and conflicting memories (M1--M3). Requests are verified to require group history, memories are anchored to their sources, and L2 uses tailored rubrics with penalties derived from real user feedback. Across evaluations of frontier models with full context, retrieval methods, and memory systems, the strongest memory system rivals full context on recall but falls far behind on use, especially for distributed and conflicting memories. Together, two additions that relate retrieved memories and bind remembered facts as response constraints bring consistent gains, showing that group memory systems must improve use, not recall alone.

---


### 196. [Leakage-Resilient Computation via Matrix Refreshing](https://arxiv.org/abs/2611.04876)

**<font color=#1a73e8>作者：</font>** Stefan Dziembowski, Sebastian Faust  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Leakage-resilient cryptography protects secrets against side-channel attacks, in which a physical implementation reveals partial information about its internal state. A fundamental primitive in this area is a leakage-resilient storage, which allows a secret to be stored in a way that remains secure even if an adversary learns some information about the storage's internal state. A popular approach represents a secret as the inner product of two $n$-bit vectors, called shares. The shares are stored and processed separately by two parts of the implementation, called the left and right parties. Because leakage accumulates over time, the shares must be refreshed repeatedly. We prove that a simple refresh, in which the left party multiplies its share by a uniform invertible matrix $M$ and the right party multiplies its share by $M^{-1}$, is secure under continual local leakage. After $T$ refreshes, each allowing at most $\lambda$ bits of leakage per party, the transcripts for two stored secrets are at statistical distance at most $C\cdot T\cdot 2^{6\lambda-n/9}$ for an absolute constant $C$.
We also obtain a Boolean-circuit compiler with statistical privacy error at most $C\cdot S\cdot 2^{18\lambda-n/27}$ for $S$ operations and at most $\lambda$ bits of local leakage per party per operation. The guarantee covers repeated stateful evaluations with adaptively chosen public inputs, with $S$ counting all operations across invocations. Thus, for polynomial-size circuits, a constant leakage fraction is tolerated with share length depending only on the security parameter. We formalize the refreshing bound, the composition and compiler guarantees, and the expected-work bounds in Lean 4. Our results also provide efficient simulation: the leakage can be reproduced from the public inputs and the circuit outputs alone, with expected polynomial overhead.

---


### 197. [DLER: Dual-Logit Experience Replay for Online Continual Learning](https://arxiv.org/abs/2611.04885)

**<font color=#1a73e8>作者：</font>** Huiwei Lin, Shanshan Feng, Kong Aik Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online continual learning aims to continuously train neural networks on a non-stationary data stream in a single pass. Rehearsal-based methods alleviate catastrophic forgetting by replaying stored samples, but the imbalance between current and previous data often leads to predictions biased toward current classes. Many approaches have been proposed to overcome the forgetting problem by correcting the bias; however, they still need to be improved in an online fashion. By decomposing the dot-product logits into an angle factor and a norm factor, our analysis reveals that the angle factor efficiently captures novel knowledge but is particularly susceptible to prediction bias, whereas the norm factor helps preserve historical knowledge. Based on these observations, we propose Dual-Logit Experience Replay (DLER), which exploits dual-logits for both model optimization and memory management. Specifically, DLER learns current samples using cosine logits and incorporates additional dot-product logits when replaying previous samples to mitigate prediction bias. To strengthen dual-logit learning under limited replay memory, an auxiliary supervised contrastive objective promotes angular compactness within each class, extending corrections learned from limited replay samples to other samples of the same class. Meanwhile, we introduce a memory update strategy that preferentially retains samples for which dot-product prediction assigns a higher probability to the correct class than cosine prediction, aligning sample selection with dual-logit training. Extensive experiments on three datasets demonstrate the effectiveness of DLER, particularly under limited memory budgets.

---


### 198. [FourSight: Stable FP4 RL Post-Training via Sequence Filtering and Sparse Channel Compensation](https://arxiv.org/abs/2611.04887)

**<font color=#1a73e8>作者：</font>** Yining Wei, Tianyuan Wu, Gu Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training increasingly targets low-bit deployment, with NVFP4 weight-and activation quantization (W4A4) becoming the state-of-the-practice format. However, integrating NVFP4 into RL degrades rollout quality and amplifies cross-engine training-inference mismatch (TIM), destabilizing training. We show that these failures are concentrated rather than uniform - severely mismatched tail tokens concentrate in a few outlier sequences, while policy weights remain largely intact and quantization error concentrates in a few high-variance activation channels. Guided by this, we present FourSight, an algorithm-system co-design with two targeted solutions: TIM-aware sequence filtering that excludes drifted trajectories from policy updates, and sparse precision compensation that keeps only top-variance channels in BF16 while retaining native NVFP4 elsewhere. We further design a fused SpliceGEMM kernel with specialized prefill and decode datapaths to minimize overhead. FourSight sustains near-BF16 accuracy and strong FP4 deployment quality across models and engines, while improving step-to-accuracy by 1.76-2.60x and staying within 2.3% of FP4 step time up to 120B-scale models.

---


### 199. [Fault-tolerant shallow recurrent decoders for sparse sensing with missing sensor measurements](https://arxiv.org/abs/2611.04893)

**<font color=#1a73e8>作者：</font>** Matteo Romilio Pasqual, Matteo Tomasetto, J. Nathan Kutz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world sensing systems are inherently imperfect: sensors may fail, intermittently disconnect, operate with asynchronous sampling rates, and be subject to noise, leading to measurement streams that are irregular, incomplete, and heterogeneous. Nevertheless, sensing strategies for real-time state reconstruction typically assume synchronous and continuously active sensors, a constraint that substantially limits their applicability in operational environments. In this work, we introduce fault-tolerant sparse sensing strategies in the context of shallow recurrent decoders (SHRED) to enable high-dimensional state estimation from sparse, asynchronous, and missing sensor measurements. Specifically, we consider naive imputation strategies, fault-tolerant recurrent temporal encoders, and we introduce four different transformer-based masking mechanisms to make SHRED explicitly aware of sensor availability through the binary data-availability mask. Moreover, we further introduce a multi-step decoding training objective for SHRED, resulting in smoother latent trajectories and more robust predictions. Throughout a synthetic benchmark and three real-world problems in hydrodynamic and ocean modeling, we show that (i) transformer-based masking mechanisms outperform standard imputation techniques and fault-tolerant recurrent architectures, (ii) the multi-step decoding training objective enhances reconstruction fidelity and robustness in the presence of heterogeneous missing-data patterns, while (iii) the computational efficiency of SHRED is preserved, with no additional inference-time overhead.

---


### 200. [VisSearch-Bench: Evaluating Long Horizon Visual Search in Multimodal Agents](https://arxiv.org/abs/2611.04894)

**<font color=#1a73e8>作者：</font>** ZhengXian Wu, Qianhao Nie, Zhuohong Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal agents use web and image tools to answer questions beyond their internal knowledge. Some search tasks use images mainly to identify an initial entity, then rely on text retrieval. These tasks offer limited insight into how agents connect information across images, objects, and search steps. We therefore focus on visual context management. This involves organizing and using visual information and linking it to other findings during search. Visually intensive tasks require agents to combine object appearance, local details, or spatial relations with external information. We introduce VisSearch-Bench, with 204 human-written tasks across 7 main domains and 25 subdomains. It covers Set-wise Visual Search, Sequential Visual Search, Hybrid Wide-Deep Search, Competitive Visual Disambiguation, and Visual-Structure-Guided Search. Each task provides a reference answer, traceable evidence, and scoring rules. Accuracy measures complete task success, while Process Score measures the correctness and completeness of individual results and subquestion answers. Across 16 multimodal models, the best system fully solves only 26.47% of tasks, even with search tools. These results highlight the challenge of linking visual evidence with search results to produce complete answers.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-280](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
