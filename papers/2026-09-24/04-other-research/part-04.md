# 📦 其他研究 | 2026年09月24日

> 本类共 **275** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-275](./part-06.md)

---

### 151. [xWhyL: Causal Interactive Learning](https://arxiv.org/abs/2609.26037)

**<font color=#1a73e8>作者：</font>** Nicholas Tagliapietra, Florian Peter Busch, Moritz Willig 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explanations are central to causal reasoning, and cognitive science has long established that the human drive to explain is itself a mechanism for learning about causality. Despite this, learning from those abductive signals is largely ignored in artificial intelligence. While explainable AI (XAI) increasingly draws on causal models to generate explanations, the converse direction about what explanations can do for causality remains largely unexplored. To fill this gap, we propose xWhyL, a formal framework connecting causality and XAI by learning causal models from explanations. We develop a mathematical theory that translates explanations into a learning signal complementary to observational data, and demonstrate how it enables overcoming the limits of observational causal discovery. As explanations can be derived from incorrect beliefs and clash with data, a tension we call the Causal Tug-of-War, we prove conditions under which our framework rejects misspecified explanations rather than absorbing them. Our practical instantiation, Causal Interactive Learning (CIL), shows how expert explanations can efficiently support causal discovery and distinguish correct from incorrect explanations.

---


### 152. [EMERGE: Resolution-Agnostic Point Cloud Generation with Equivariant Graph-Based Diffusion](https://arxiv.org/abs/2609.26039)

**<font color=#1a73e8>作者：</font>** Ilias Mitsouras, Nikolaos Chaidos, Giorgos Stamou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud generation has emerged as a crucial task for accurately capturing and reproducing the complexity of the physical world. However, existing generative approaches, predominantly relying on Transformers and Variational Autoencoders (VAEs), frequently ignore the continuous, non-grid topologies inherent to 3D spaces. Although the integration of graph-based structures has yielded significant benefits in related discriminative vision tasks, such geometric architectures remain noticeably absent from 3D generative modeling. To address this gap, we introduce EMERGE (Equivariant Multi-scale GNN for Resolution-agnostic point cloud GEneration), the first fully $SE(3)$-equivariant graph-based diffusion backbone explicitly designed to generate point clouds while preserving continuous spatial symmetries. Our framework bypasses the rigid resolution dependencies of standard generative pipelines, enabling zero-shot inference at multiple, arbitrary spatial resolutions. Extensive empirical evaluations demonstrate that EMERGE achieves State-of-the-Art generation quality across standard metrics, while the strong inherent geometric inductive biases enable significantly faster training convergence compared to existing baseline methods.

---


### 153. [Canonical locks that encode part-whole hierarchies](https://arxiv.org/abs/2609.26046)

**<font color=#1a73e8>作者：</font>** Rajat Modi, Yogesh Singh Rawat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> One of the challenges in representational learning is how to encode part-whole hierarchies in a neural net. Prior works rely on flattening tree-like structures into string-like sequences and training a sequence-to-sequence model via autoregression. While such a representation works for parse-trees in NLP, it is not entirely clear how to make it work for images. Thus, we propose a geometric primitive called canonical locks. The key idea is that parts/wholes can be modelled as higher-dimensional vectors ($d \geq 4$), and information can be encoded in their relative phase differences.
Inductively, the net consists of positionally-bound bottom-up and top-down neural fields, which drive each other to achieve a state of thermal equilibrium. Additionally, we show the existence of a few symmetrical configurations in the net. The computational iterations taken to break these symmetries depend on the angle between parts/wholes arranged on a disk (or more precisely a ring) in higher dimensions. It also appears to have connections to the psychological phenomenon of mental rotation.

---


### 154. [Adversarial Course-of-Action Generation: Game-Theoretic Multi-Agent Algorithms for COA matching & COA generation](https://arxiv.org/abs/2609.26059)

**<font color=#1a73e8>作者：</font>** Natan Vidra, Alina Kapanova, Arun Kanhai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Course-of-action (COA) generation is a distributed planning problem: a system must propose structured candidate actions, evaluate them against an adversarial response, and surface options that remain tactically coherent under changing conditions. We present COA-Bench, a small offline benchmark and reproducibility artifact for comparing COA generation policies through self-play. Following the BattleCOA terminology, we reserve COA matching for asset-effect matching and COA generation for course-of-action generation; the present artifact does not implement either DecisionFunction directly. Instead, it represents COAs as typed action chains with conditional branches, assigns a synthetic COA quality score, compares opposing COAs with a BLUE-vs-RED advantage score and Nash-gap distance, and scores doctrinal coherence with an FM 3-0-inspired heuristic rubric. Across 50 synthetic scenarios spanning five operational templates, a sampled best-response policy that draws eight RED candidates reduces BLUE advantage from .516 to .485 and BLUE wargame win rate from .920 to .820; a two-stage multi-agent council with five BLUE proposer agents, RED-team adjudication, and critique-driven revision obtains .509 BLUE advantage and .820 BLUE win rate. We also identify and fix a benchmark-design issue in which scenario framing was stored as metadata but had no effect on generated COA content. COA-Bench is not an operational battle-management system and uses no real, classified, proprietary, or human-subject data. The contribution is an inspectable evaluation harness, preliminary benchmark evidence, and lessons for building auditable agentic planning artifacts.

---


### 155. [Towards Adaptive Federated Graph Clustering: A Global Community-aware Contrastive Learning-based Approach](https://arxiv.org/abs/2609.26063)

**<font color=#1a73e8>作者：</font>** Yinlin Zhu, Di Wu, Wang Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated graph learning (FGL) enables multiple clients to collaboratively train graph models without sharing their private graph data, providing a promising paradigm for mining knowledge from distributed graph repositories. While most existing FGL methods focus on supervised tasks, real-world graphs are often massive and unlabeled, making federated graph clustering an important yet still immature research direction. Notably, this task is particularly challenging due to the inherent subgraph heterogeneity across clients, which leads to client-specific community structures. In this work, we identify two critical limitations in existing federated graph clustering methods: (1) unrealistic pre-defined cluster cardinality assumptions and (2) incomplete inter-community separation. To address these challenges, we propose AdaFGC, an Adaptive Federated graph clustering framework based on Global community-aware Contrastive learning. AdaFGC introduces an over-complete set of global community anchors to model the global community structure and adaptively estimate clustering cardinality via cross-client anchor refinement. In addition, it employs a global community-aware contrastive learning scheme that uses the shared anchors as contrastive prototypes to explicitly enforce community-level attraction and repulsion across clients, complemented by node-level and topology-level objectives that stabilize local representations. Extensive experiments on eight benchmark datasets demonstrate that AdaFGC consistently outperforms existing supervised and unsupervised FGL baselines across multiple clustering metrics.

---


### 156. [SPEANet: Structural Prior Enhanced Attention Network for Parameter-Efficient Remote Sensing Object Detection](https://arxiv.org/abs/2609.26064)

**<font color=#1a73e8>作者：</font>** Wei Lu, Junjie Li, Feifei Sang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing object detection (RSOD) requires compact backbones capable of preserving weak geometric cues under extreme scale variation and background clutter. Fixed structural operators provide complementary contour and frequency responses without introducing learnable operator coefficients. However, directly injecting these responses can amplify content-irrelevant textures, while applying a uniform operator design across the hierarchy may be poorly matched to stage-specific representation requirements. We propose the Structural Prior Enhanced Attention Network (SPEANet), a parameter-efficient RSOD backbone that integrates fixed operators through stage-specific prior extraction and context-conditioned response modulation. SPEANet assigns smoothed contour and multi-order directional modeling to shallow, high-resolution features, while employing a compact approximation-detail interaction mechanism in deeper stages. Learned spatial gates regulate the resulting prior responses before residual fusion. Experiments on five benchmarks, together with evaluations across seven detection frameworks on DOTA-v1.0, achieve a favorable accuracy-parameter trade-off. With Oriented R-CNN, SPEANet achieves 78.55\% mAP on DOTA-v1.0, 72.24\% mAP on DOTA-v1.5, and 67.30\% mAP on DIOR-R using 23.0M total parameters, including a 5.97M-parameter backbone.

---


### 157. [FuncCode: Compressing Kolmogorov--Arnold Networks in Function Space with Hardware-Aware Quantization](https://arxiv.org/abs/2609.26067)

**<font color=#1a73e8>作者：</font>** Kazi Ahmed Asif Fuad, Lizhong Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov--Arnold Networks (KANs) replace scalar edge weights with learnable univariate functions, increasing flexibility but also parameter memory because each edge stores multiple coefficients, often together with a separate base branch. We introduce FuncCode, a basis-agnostic compression approach that forms shared codebooks from sampled edge responses, codes the basis and base branches independently, and exports the resulting codebooks and per-edge indices in a quantized, bit-packed format. Across spline and polynomial KANs, sampled edge responses exhibit $13$--$35\%$ lower effective rank than their coefficient representations. Further replicated controls show that function-space clustering alone is statistically tied with coefficient-space clustering; the consistent accuracy gain comes from preserving the distinct sharing structure of the two branches. On a ten-seed MNIST benchmark, FuncCode compresses spline and GRAM KANs by $31.6\times$ and $17.6\times$ with only $0.31$ and $0.34$ pp accuracy loss. On a 6.1M-edge convolutional KAGN, it achieves $19.9\times$ compression while remaining within $0.54$ pp of dense accuracy on CIFAR-10 and $1.89$ pp on CIFAR-100. After compression, per-edge indices account for up to $99.4\%$ of stored weight bits, making the representation index-bound. Across nine bit-exact FPGA accelerators, FuncCode reduces SplineKAN post-route weight memory by $3.87\times$ relative to dense INT4, without increasing cycle count or latency. The FuncCode implementation is available at this https URL.

---


### 158. [RankCert: When Can Simulated Learners Safely Select an AI Tutor? Robust Decision Certification Under Structural Uncertainty](https://arxiv.org/abs/2609.26069)

**<font color=#1a73e8>作者：</font>** Nizam Kadir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulation-based tutor selection can be unstable when predictively adequate learner models imply different policy rankings. RankCert certifies one of eight equal-budget tutoring policies only when model-averaged utility, probability-best, posterior regret, cross-domain rank, family coverage, and leave-one-domain-out and leave-one-visible-family-out averages support the same candidate; otherwise it abstains. We evaluated RankCert in 1,280 frozen held-out settings spanning five rotating held-out oracle families, 64 scenarios per family, and four cohort sizes. Calibration used a licensed, de-identified EdNet-KT1 derivative with 5,000 learners and 590,056 retained responses; all five family representatives passed the frozen adequacy gate. Minimum-domain mean pairwise top-1 agreement was 0.272917 (95% CI [0.253646, 0.293229]), showing substantial structural disagreement. Cohort-noise variance decreased from n = 30 to n = 300, while the structural family share remained nonzero. RankCert reduced total held-out decision loss relative to full-coverage point selection by 0.006605 normalized-outcome units (95% CI [0.004859, 0.008407]). At comparable coverage, however, it did not reduce selective risk relative to a confidence-gated point certificate (difference -0.000213; 95% CI [-0.003238, 0.002384]; Holm p = 0.929654). Certification occurred in 3.75% of settings and only in stable scenarios; RankCert abstained in every ambiguous, misspecified, and structural-conflict setting. "Safe" denotes only benchmark-scoped decision certification under the declared utility and uncertainty set; no human-learning, causal, deployment-effectiveness, or general-safety claim is made.

---


### 159. [Fast Matrix Multiplication in fp8: Certified Coefficient Optimization and Measured Error](https://arxiv.org/abs/2609.26077)

**<font color=#1a73e8>作者：</font>** Shuxiao Xie, Shuyang Xie, Yuan Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A Strassen-type algorithm has many realizations with the same exact product and multiplication count yet different fp8 error because basis changes reshape coefficient geometry, posing the question of which to run. No current account settles this: classical stability controls worst-case $\ell_1$ growth, not the expected-error magnitude, and the Dumas--Pernet--Sedoglavic optimizer could only be called probably optimal, its global optimality unproved. To settle this, we attach to each realization a coefficient functional $\Phi$, a scalar summary of its coefficient geometry, which we minimize over the change-of-basis orbit. This Kempf--Ness problem on a Hadamard manifold lets us certify the global $\Phi$ optimum rather than merely search for it: an exact moment-map zero fixes $\Phi_{\min} = 200/9$, and de Groote's classification extends that optimality to every exact real rank-7 $2\times2$ decomposition. Every exact real rank-7 realization therefore has a $\Phi$-predicted RMS constant at least $5/3$ times that of the cubic algorithm, at fixed noise coefficient. We then introduce an explicit block-scaled e4m3 model in which $\Phi$ is the leading-order coefficient of relative expected mean-squared error, and we test the resulting $\Phi$-predicted ordering against realized fp8 error. Ordering and re-basing experiments support that prediction within tested fused block-scaled regimes, and on real matmul tiles from four architecture families the $\Phi$-optimal realization falls in the fp8 low-error region. Across two $\sim$70B models on real deep_gemm kernels, the same realization removes 10 to 55% of classic Strassen's excess NLL over the clean model. Algorithm realization thus becomes a mathematically certified design problem rather than a tuning choice: an independent low-precision axis with a global $\Phi$ optimum and measured fp8 relevance.

---


### 160. [ToW3D: Consistency-aware Interactive Point-based Mesh Editing on GANs](https://arxiv.org/abs/2609.26078)

**<font color=#1a73e8>作者：</font>** Haixu Song, Fangfu Liu, Chenyu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose ToW3D that enables precise and consistent control over 3D generative adversarial networks (GANs) with the Tug-of-War competition between shape deformation and appearance consistency. Existing point-based GAN editing methods such as DragGAN and GANWarping have yielded impressive performance for 2D image manipulation. However, as 3D generators present weaker generalization ability compared with 2D due to limited training data, they would suffer from drastic changes in global appearance when editing local areas of meshes. To address this, we design a pipeline of ``drag locally, shove globally'', which iteratively performs two optimization steps: 1) pull the point towards the target, and 2) push the structure and semantics back to the source. Specifically, we design a structure adaption module based on structure which guarantees the preservation of basic geometric properties, and a semantic preservation module that maintains semantic similarity across different views. Extensive qualitative and quantitative experiments demonstrate superiority of our ToW3D approach over prior methods in terms of appearance consistency and fidelity especially under large deformations.

---


### 161. [Learning to Link: Automatic Re-identification of BLE Devices Under MAC Address Randomisation](https://arxiv.org/abs/2609.26079)

**<font color=#1a73e8>作者：</font>** Reem Abdulrhman Alghamdi, Alberto Verna, Marco Mellia  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bluetooth Low Energy (BLE) employs MAC address randomisation -- via Resolvable Private Address (RPA) -- to mitigate long-term device tracking on public advertising channels. Existing research has shown that advertising packets contain metadata and structural features that allow re-identifying a target device via manually crafted rules. In this work, we investigate the feasibility of automating the process of tracking BLE devices despite MAC randomisation by leveraging machine learning algorithms for the signature creation. Based on the actual Bluetooth traffic from target devices, we characterise the persistence of advertising-layer features across RPA changes and formulate device linkage as a supervised classification problem. Using simple decision tree classifiers as a proof-of-feasibility approach, we evaluate the distinguishability of target and non-target devices under varying address rotation patterns. Our results reinforce prior work demonstrating that advertising-layer metadata can enable device re-identification under MAC randomisation, to the point where such linkage can be automated using standard supervised learning techniques, without any specific knowledge of the technology.

---


### 162. [The Fleet Is the Model: Engineering Collective Intelligence with Fusion-MoA Pioneer R1](https://arxiv.org/abs/2609.26080)

**<font color=#1a73e8>作者：</font>** Zongyou Yang, Yinghan Hou  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The model exposed to an application need not be a single checkpoint; it can be a governed fleet. Existing serving systems manage checkpoints and replicas, while multi-agent frameworks compose model calls without defining a stable collective identity, effect authority, or member-level evolution. We present Fusion-MoA, a runtime that exposes independently served heterogeneous Cells as one OpenAI-compatible model. A versioned Profile controls membership and evidence admission; read-only Analysts contribute bounded evidence, while a sole Executor retains all final-answer and tool authority. Cells can be qualified, promoted, or rolled back without changing the public API. We evaluate an eight-Cell, three-lineage deployment through three operational witnesses. On a fixed HMMT P1-P10 slice, the collective solves 8/10 problems versus 6/10 for the strongest individual Cell, and a preserved trace shows minority knowledge transferred to three initially incorrect or empty Cells. On 20 Terminal-Bench 2.1 tasks, all tool actions remain attributable to one Executor, with zero Analyst actions and zero bypass effects. Six Cells are promoted and one incompatible candidate is locally rolled back while the service remains available. Fusion-MoA demonstrates that heterogeneous model capability can be operated as one observable, authority-bounded, and independently evolvable service.

---


### 163. [Margin-Drop Coordinates for Cross-Budget Robustness Evaluation](https://arxiv.org/abs/2609.26081)

**<font color=#1a73e8>作者：</font>** Yanliang Huang, Zhen Zhang, Peng Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed-budget robustness evaluation can select the wrong frozen vision encoder. An encoder that survives a shallow attack may lose most of that robustness when the same evaluation is strengthened. We ask whether the shallow evaluation contains enough information to identify this budget fragility. For each clean-correct sample, the evaluation records the clean pairwise margin, the first-order linearized margin-drop scale, the margin drop from a clean-start one-step attack, and the drop reached by an iterative attack. Normalizing by that scale gives three margin-drop coordinates capturing clean margin slack, one-step shortfall, and drift, where drift is the additional normalized margin drop the iterative attack reaches beyond the one-step perturbation. Together, they reconstruct the normalized post-attack margin and therefore the pass-or-fail outcome. Across 42 pretrained frozen vision encoders, the shallow survival rate carries essentially no rank information about subsequent PGD-10 to PGD-200 collapse, at Spearman -0.006, while the median shallow drift coordinate ranks the same collapse at +0.811. The result persists in a held-out encoder pool and under an $\ell_\infty$ evaluation. With deep evaluation limited to 11 encoders, ranking by shallow drift recovers 11 of the 17 high-collapse encoders, compared with 5 under survival-rate ranking. The full coordinate decomposition further distinguishes cases that share the same fixed-budget residual but diverge at deeper budgets, and separates margin repair from drift repair under interventions, revealing distinct repair paths that endpoint robustness alone does not identify.

---


### 164. [BDSLI: A hybrid CNN-Transformer model for Bengali Sign Language interpretation](https://arxiv.org/abs/2609.26088)

**<font color=#1a73e8>作者：</font>** Abir Bin Yousuf, Muhammad Iqbal Hossain  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study introduces a novel hybrid CNN-Transformer architecture to address the limited progress in Bengali SLR, focusing on isolated sign word recognition and sentence generation. This specific model combination is new to Bengali SLR tasks. A custom video dataset was developed, featuring 62 distinct Bengali sign words (250 samples/class), along with a separate test dataset. The CNN-Transformer model demonstrated superior performance against all comparative and baseline models (e.g., CNN-LSTM, standalone TCN), achieving a 99.58% training accuracy (99.48% validation) and a 98.65% test accuracy. The trained model was subsequently deployed in a web application for real-world validation.

---


### 165. [Match One, Learn with Graph: One-to-Graph Query Collaboration with Backward Sharing for Object Detection](https://arxiv.org/abs/2609.26092)

**<font color=#1a73e8>作者：</font>** Wenxiao Fan, Jingling Fu, Luohang Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-to-one (O2O) matching enables Detection Transformers (DETRs) to perform end-to-end set prediction by assigning each object to a single positive query. However, the strongest classification, center, scale, and overlap evidence for an object is often distributed across multiple queries. This mismatch leaves only the matched owner positively supervised for the object, while other evidence-bearing queries receive no box target for it. We term this query knowledge fragmentation. To exploit such complementary evidence without one-to-many supervision, we propose BS-O2G, a plug-in that builds a sparse prediction-aware graph from decoded features, boxes, and class distributions to organize query collaboration in feature and optimization spaces while preserving the original O2O matcher, positive labels, and objective. One-to-Graph (O2G) calibration propagates relative messages over this graph to consolidate query evidence in the forward pass, whereas Backward Sharing (BS) reuses its transposed detached adjacency to route gradients across persistent query basis vectors without changing the decoder input in the forward pass. Experiments across diverse DETR methods, backbones, COCO, and CrowdHuman show consistent gains and faster convergence with negligible parameter/FLOP growth and modest runtime overhead, supporting graph-based query collaboration as an alternative to expanding positive assignments.

---


### 166. [FusionMMT: A Unified Multimodal and Multitask Learning Framework for Nuclear Fusion](https://arxiv.org/abs/2609.26095)

**<font color=#1a73e8>作者：</font>** Qiang Chen, Xiao Wang, Qingquan Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the growing global demand for energy, nuclear fusion has emerged as a promising direction for future clean energy. Tokamaks represent one of the leading approaches to magnetic-confinement fusion. Achieving high-performance, long-pulse, and steady-state operation requires effective diagnosis of plasma states. However, existing intelligent diagnostic methods are largely limited to either multimodal single-task or unimodal multitask learning, while a unified multimodal multitask learning framework remains underexplored. To address this gap, we construct EAST-VTD640, a multimodal multitask dataset that integrates vision and time-series diagnostics from 640 EAST shots for disruption prediction, edge-localized mode (ELM) recognition, and H98 regression. On this basis, we present FusionMMT, the first unified multimodal multitask framework for intelligent tokamak plasma diagnostics. FusionMMT employs multi-scale, time-aware, and variable-aware modeling to handle heterogeneous sampling rates and the high computational cost of high-frequency sequences. It further combines task-adaptive multimodal fusion with progressive multitask optimization to learn shared and task-specific representations while mitigating cross-task conflicts and optimization imbalance. Extensive experiments on EAST-VTD640 show that FusionMMT outperforms representative multimodal multitask methods across disruption prediction, ELM recognition, and H98 regression. The source code will be released on this https URL

---


### 167. [Beyond Classification Accuracy: Quantifying Fingerprint Complexity in Encrypted Darknet Services](https://arxiv.org/abs/2609.26096)

**<font color=#1a73e8>作者：</font>** Javeriah Saleem, Rafiqul Islam, Md Zahidul Islam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing darknet traffic studies primarily evaluate service fingerprintability through classification performance, providing limited insight into why certain services are easier or harder to identify. This paper introduces the Fingerprint Complexity Score (FCS), a framework for quantifying the intrinsic complexity of darknet service fingerprints using behavioral overlap, uncertainty, disagreement, and persistent confusion. Experiments on 25 services across the Tor, I2P, FreeNet, and ZeroNet anonymity networks reveal substantial variation in fingerprint complexity, with behavioral overlap emerging as the dominant contributor. Validation using Random Forest, Extra Trees, and XGBoost demonstrates a strong inverse relationship between fingerprint complexity and recognition performance (Pearson r = -0.706, Spearman \r{ho} = -0.765, p < 0.001). The findings show that service fingerprintability is fundamentally governed by behavioral complexity, providing a new perspective for analyzing behavioral information leakage in anonymity networks.

---


### 168. [MIAR: Medical Image Super-Resolution With Autoregressive Modeling](https://arxiv.org/abs/2609.26103)

**<font color=#1a73e8>作者：</font>** Fang Li, Yinglong Li, Hongyu Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Image Super-Resolution (MISR) aims to enhance spatial resolution without requiring hardware modifications. Although deep learning has yielded promising results, existing paradigms face a critical trade-off: diffusion-based methods suffer from prohibitive inference latency and compromised structural fidelity, whereas regression-based models typically produce over-smoothed results that lack perceptual realism. To address these limitations, we propose MIAR, which reformulates super-resolution as a conditional and progressive next-scale prediction task through a multi-scale autoregressive framework. To ensure structural fidelity, we augment the autoregressive backbone with a Scale-Adaptive Structural Decoder. Furthermore, we integrate a hierarchical beam search strategy during inference to mitigate the recursive error accumulation inherent in autoregressive generation, a phenomenon that is especially pronounced in medical images. Extensive experiments demonstrate that MIAR establishes new state-of-the-art benchmarks while maintaining superior fidelity. Notably, our framework achieves a 7.86% improvement in the perceptual metric MUSIQ compared with the state of the art, while simultaneously delivering a 2.02x speedup over diffusion-based methods.

---


### 169. [Neoadjuvant chemotherapy response prediction using pretreatment diffusion and contrast-enhanced magnetic resonance imaging with clinical variables](https://arxiv.org/abs/2609.26105)

**<font color=#1a73e8>作者：</font>** Pablo García Marcos, Paula Puerta González, Guillermo Lorenzo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prediction of pathological complete response before neoadjuvant chemotherapy may facilitate more tailored therapeutic planning for breast cancer patients. This work proposes a deep-learning model for pretreatment data only, combining apparent diffusion coefficient maps, dynamic contrast-enhanced magnetic resonance imaging, and clinical variables. The study uses the public ACRIN 6698/I-SPY2 multicenter dataset. The architecture employs EfficientNet-B0 pretrained encoders for image feature extraction and late fusion with clinical information. Multiple clinical variables were evaluated, including age, race, histological type, HR/HER2 subtype, SBR grade, and maximum diameter. Only HR/HER2 subtype improved the average area under the receiver operating characteristic curve (AUC) and was retained in the final model. Using stratified five-fold cross-validation, standalone apparent diffusion coefficient maps achieved a mean AUC of 0.79, whereas dynamic contrast-enhanced magnetic resonance imaging achieved 0.74. Adding HR/HER2 subtype improved performance to 0.83 and 0.81, respectively. The final configuration, using both imaging modalities and HR/HER2 subtype, achieved an AUC of 0.86. These results support pretreatment multimodal learning for response prediction, although external validation is required before clinical use.

---


### 170. [Early Prediction of Pathological Complete Response to Neoadjuvant Chemotherapy Using Temporal Deep Learning on DWI](https://arxiv.org/abs/2609.26106)

**<font color=#1a73e8>作者：</font>** Pablo García Marcos, Md. Tarequl Islam, Paula Puerta González 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Early identification of non-responders to neoadjuvant chemotherapy (NACT) is crucial for timely treatment adaptation in breast cancer. However, many existing predictive models rely on multiparametric magnetic resonance imaging (MRI), late treatment time points, or extensive clinical data, which limits their applicability. This study proposes a deep learning framework for early prediction of pathological complete response (pCR) using only diffusion-weighted MRI (DW-MRI) acquired at baseline and after the first NACT cycle. This framework feeds cropped tumor-centered patches to an EfficientNet-based temporal model that directly learns tumor shape and local tissue characteristics without explicit radiomic feature engineering. The model, trained with 10-fold cross-validation, achieved an area under the receiver operating characteristic curve (AUC) of 0.90 for pCR prediction after one cycle, providing actionable information after a single treatment cycle while avoiding gadolinium administration and reducing dependence on heterogeneous clinical data. By focusing on the baseline-to-first-cycle window instead of later stages, the approach supports earlier escalation or de-escalation of NACT, and its exclusive reliance on DW-MRI facilitates protocol standardization, multi-centre deployment and privacy-preserving data sharing. These results demonstrate that DW-MRI-based deep learning on tumor-centered patches constitutes a minimally invasive, clinically deployable strategy for early pCR prediction, with direct implications for personalized treatment adaptation in neoadjuvant breast cancer therapy.

---


### 171. [Certified Mechanistic Interpretability: Lifting Single-Input Findings to Bounded Neighbourhoods](https://arxiv.org/abs/2609.26112)

**<font color=#1a73e8>作者：</font>** Zhen Zhang, Yanliang Huang, Peng Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability reverse-engineers transformer circuits one input at a time, leaving observed mechanisms without guarantees over bounded input neighbourhoods. We address this gap with a framework based on constrained polynomial-zonotope (CPZ) propagation that lifts mechanistic-interpretability observations from a single input to certified statements over a bounded set of perturbations. Three internal-attention queries (top-$k$ stability, evidence mass, and attention entropy) are formulated as tractable programs over the simplex of attention weights, and CPZ propagation through transformer blocks is shown to preserve the softmax simplex and the LayerNorm zero-mean identity exactly. A recursive Jacobian zonotope construction extends the same certificates across layer depth by linearising the block stack at the input and avoids per-layer generator growth. We instantiate the framework on transformer attention; the resulting certificates offer a way to sharpen mechanistic statements that single-input inspection cannot resolve on its own, and to inform downstream decisions in regimes where empirical heuristics may be misleading.

---


### 172. [A Cross-Dataset based Zero-Day Intrusion Detection System by Integrating Siamese Network and Reinforcement Learning](https://arxiv.org/abs/2609.26115)

**<font color=#1a73e8>作者：</font>** Md. Meheraj Hossain, Saumik Das Turja, Sibgatullah Tasnim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Zero-day threats are nascent for the Internet of Things (IoT) network security, which demands cognitive detec-tion mechanisms that can identify emerging malicious behavior. Conventional intrusion detection mechanisms fail to generalize dynamic zero-day exploits within sophisticated IoT environments. This paper proposes a hybrid zero-day intrusion detection system using Siamese network-based anomaly correlation and reinforcement learning-based adaptive defense. Furthermore, the paper uses unsupervised machine learning classifiers over benchmark IoT datasets with the intention of detection of known attack types compared to unknown anomalies using distance-based similarity analysis to detect possible zero-day attacks. To facilitate adaptability, a Proximal Policy Optimization (PPO) reinforcement learning-based agent dynamically adjusts the defense policy with continuous feedback and optimization. Experimental evaluations demonstrate 99.28% training accuracy, 99.07% accuracy in unknown attack detection, and 93.94% zero-day detection ratio, confirming the convergence and stability of the model on this http URL system offers a self-learning and extensible defense mechanism of IoT deployments by finding the right balance between precision, latency and false positives. This deep anomaly correlation with adaptive reinforcement learning is a firm base on which the next generation and autonomic cyber security solutions can take the reins as the zero-day threats keep changing their course.

---


### 173. [Vorch-Human: Unified Multi-Task Human-Centric Generation via Long-Horizon Continuation](https://arxiv.org/abs/2609.26117)

**<font color=#1a73e8>作者：</font>** Yang Ding, Haoran Yu, Xin Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human-centric audio-visual generation spans several closely related tasks: animating a person from driving speech, jointly generating speech and video from a voice reference, and synthesizing a scene from paired appearance and voice references. Existing systems commonly solve these tasks with separate models, even though they share the same target modalities and differ mainly in which observations are provided as conditions. We present Vorch-Human, a unified human-centric generation framework built on a dual-stream audio-video diffusion transformer. Vorch-Human augments the conventional noisy audio/noisy video interface with clean condition-audio and condition-video token groups. Per-token task embeddings, temporal position types, condition masks, and a shared multimodal prompt encoder allow driving speech, timbre examples, first frames, and subject images to be expressed within one model. To supply the supervision required by this interface, we develop a two-level data pipeline. Level 1 analyzes each clip with speech recognition, vocal separation, face detection and tracking, active-speaker and synchronization models, audio/visual speaker clustering, and multimodal caption correction; it produces subject-indexed speech, appearance, and timbre annotations. Level 2 links the same person across clips from a common source video and mines identity- and outfit-consistent reference images after face, body, quality, pose, and vision-language verification. Finally, we adapt Vorch-Human to long-form audio-driven generation by training with clean latent prefixes and using the same frozen-prefix recurrence at inference. Each segment contributes only its newly generated suffix, reducing boundary discontinuity and long-horizon identity drift. Experiments on short and five-minute generation demonstrate strong identity preservation, audio-visual synchronization, and temporal stability.

---


### 174. [FairMon: A Tool for Monitoring and Visualizing Algorithmic Fairness](https://arxiv.org/abs/2609.26123)

**<font color=#1a73e8>作者：</font>** Jan Baumeister, Bernd Finkbeiner, Vladimir Krsmanovic 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Runtime monitoring has recently been proposed as a rigorous method for analyzing algorithmic fairness of autonomous decision systems used in critical scenarios such as credit lending, job application, and the criminal justice system. Prior work has shown that runtime monitoring, in principle, can be an effective technique for establishing the kind of human oversight required by legislation such as the EU Artificial Intelligence Act. In practice, the available monitoring tools have not been developed with this application in mind and display several critical shortcomings in these scenarios. In this paper, we present FairMon, a runtime monitoring tool tailored to fairness analysis of high-stakes decision systems. FairMon uses RTLola as a flexible specification language for monitors, which we have extended with conditional probability operators that allow for concise descriptions of algorithmic fairness properties. The tool also features a real-time visualization of intermediary values, enabling human insight into the dynamics of the monitored system.

---


### 175. [When Big Data Becomes a Curse: Spatial Heterogeneity and the Limits of Learning from Passive Acoustic Monitoring Data](https://arxiv.org/abs/2609.26125)

**<font color=#1a73e8>作者：</font>** Gabriel Spadon, Wayne Renaud, Priyanka Aravindan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Passive Acoustic Monitoring produces large archives whose recordings are clustered by deployment, season, station identifier, and acquisition configuration. We analyze 908,072 AIS-labeled 679-second recordings from 38 deployments, 20 Atlantic Canadian station identifiers, and 21 receiver positions. The AIS-contact prior varies by more than 200-fold, and per-deployment screening distributions require local interpretation. Bidirectional cross-season transfer over the 18 station identifiers observed in both seasons predicts station identity above the 5.56% uniform-chance level, with balanced accuracy of 15.9% for AIS-contact and 16.4% for no-AIS-contact recordings. The same descriptors predict the two hydrophone models at 74.1% and 85.6% balanced accuracy, respectively, but hydrophone model is strongly confounded with season and other deployment-level acquisition differences. On a retrospectively screened and capped benchmark of 54m507 recordings, repeated station-grouped holdout yields an ROC-AUC of 0.612 with a station-bootstrap 95% interval of 0.582 to 0.648, compared with 0.661 under a random-window diagnostic. Their paired difference is 0.049 (0.040 to 0.056). Removing raw energy changes unseen-station ROC-AUC from 0.612 to 0.603, while an exploratory training-station scale analysis is non-monotonic. These results show that random-window validation overstates transfer to unseen station identifiers in this corpus. They support dependence-aware validation and broader independent spatial sampling, while spatial-expert models remain a hypothesis rather than an established remedy.

---


### 176. [The Cost of Conservation: Coordination-Memory Laws for Exact-Support Generation](https://arxiv.org/abs/2609.26126)

**<font color=#1a73e8>作者：</font>** Zhen Zhang, Amr Alanwar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many AI systems make decisions locally, even when every realized output must obey an additive conservation law, such as selecting exactly a fixed number of items. This constraint can be statistically invisible: small subsets of a balanced fixed-budget output look increasingly independent, yet communication-free coordinate-parallel generation needs exponentially many pre-shared plans, while a sequential exact sampler needs only logarithmic memory. We study product measures conditioned on additive conservation laws in the intermediate regime where one plan is selected before a fixed-order pass, every plan is a bounded-state stochastic executor whose support is entirely legal, and the mixture of plan laws approximates the target distribution in total variation. Our main result identifies the optimal asymptotic selector rate, up to constant factors, with the killed spectral profile of the conservation-difference walk. The resulting coordination cost decreases as an inverse power of live-state width, with an exponent determined by intrinsic conservation rank rather than alphabet size; the law extends to noncentral budgets and heterogeneous local scores. The converse is driven by a state-versus-resource-sum obstruction, while a rate-matching construction compiles discrepancy control into exact-support finite-state plans. Complementary results characterize block-parallel plan complexity and the benefit of programmable output order. Together, these results show precisely how online memory substitutes for front-loaded coordination in exact-support generation.

---


### 177. [Zeta-Transform Evaluation for Higher-Order Vanishing Key Recovery](https://arxiv.org/abs/2609.26132)

**<font color=#1a73e8>作者：</font>** Sunyeop Kim, Insung Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hemmert's key-recovery algorithm for Classic McEliece is based on higher-order vanishing. It computes a basis of $\ker(\widetilde\varphi_A^{(p)})$, where $A=H'''$ is the shortened parity-check matrix used in the attack. For Classic McEliece parameters, this kernel computation is the dominant cost of the attack. We show that the sums defining $\widetilde\varphi_A^{(p)}$ can be evaluated, column by column, as weighted upper zeta transforms on the Boolean lattice. Since only selected levels of these transforms are required by $\widetilde\varphi_A^{(p)}$, restricting their evaluation to the band between level $p$ and the lowest required level yields exact evaluations of both $\widetilde\varphi_A^{(p)}$ and its transpose. Using the resulting truncated zeta-transform evaluation in the Wiedemann-based kernel computation reduces the cost of the repeated matrix--vector products without changing the overall key-recovery algorithm. The exact cost depends on the weight distribution of the non-pivot columns of $H'''$. We therefore consider two models: an all-one model, in which every relevant binary coordinate is active, and a Bernoulli$(1/2)$ model, in which the coordinates are independently active with probability $1/2$. For the five Classic McEliece parameter sets, our method reduces the estimated key-recovery cost by $14.09$--$41.19$ bits in the all-one model and by $7.25$--$22.48$ bits in the Bernoulli$(1/2)$ model.

---


### 178. [When Verifiers Vote Backwards under Verdict Substitution: Signed Pivotal Value in Correlated Self-Consistency](https://arxiv.org/abs/2609.26144)

**<font color=#1a73e8>作者：</font>** Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Replacing one ballot can change a majority decision only on queries decided by a single vote; this structural fact requires no independence assumption. We study the sign of that change using a labeled, verdict-style intervention: one correctness signal replaces one correctness-indicator ballot in $k{=}7$ self-consistency panels. This diagnostic intervention is not identical to deployed answer-identity plurality. A primary MATH-500 experiment ($n{=}570$) gives a different-model verifier a $+24.2$pp pivotal gain, whereas a role-reversed configuration gives $-11.2$pp; an exploratory code stress test (14 pivotal rows across 9 tasks) gives $-24.5$pp. An exact signed-gain decomposition accounts for all observed signs through the verifier's state-specific accuracy and the composition of the two one-vote tally states, rather than global accuracy or model provenance. Same-source signals lose accuracy on the pivotal stratum (65$\to$44\% in the primary configuration), while error correlations provide a descriptive error-association diagnostic. Controlled degradation and a $k\in\{3,5,7\}$ subset sensitivity analysis probe the stability of the observed pattern around this accounting. Under the evaluated ties-incorrect answer-identity plurality analysis, the structural zero and strong-verifier benefit persist, but the role-reversed harm attenuates to $-0.9$pp and is not significant. The results therefore establish harmful verdict substitution, not universally harmful deployed plurality, and motivate a testable but unverified hypothesis for negative process-reward-model weights.

---


### 179. [Unanimity Without Persuasion: A Single Round of Debate Erases the Disagreement That Verification Needs](https://arxiv.org/abs/2609.26145)

**<font color=#1a73e8>作者：</font>** Yang Shu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A debate panel can become unanimous without becoming more correct. This is dangerous for downstream safeguards: a substituted verification ballot can change only narrow-margin votes, while richer arbiters lose disagreement as a natural targeting signal. We show that one debate round can erase that resource without requiring persuasion. Tracking a heterogeneous 7-judge panel through a blind round and three debate rounds on 600 code-correctness candidates, unanimity on a fixed cohort jumps from 39.5\% to 95.2\% in round 1 (93.1\% of the total collapse), while accuracy moves by less than one point and 96.3\% of verdict flips follow the displayed peer majority. An execution-based verification ballot corrects 8 of 2,037 pre-debate candidate-substitution instances but changes zero in every later round; by round 3 every wrong decision is unanimous, erasing dissent that had flagged two-thirds of the panel's errors. Identical-cohort controls explain why: no-peer reconsideration reproduces 79.6\% of the collapse, real labels without reasoning reproduce 91.5\%, and random labels steer flips toward whatever they display; the full-debate condition adds 4.3 percentage points over labels only (clustered 95\% CI 0.7--8.1). The one-round collapse reproduces in two additional real runs and two fake-label seeds, remains under panel sizes 3--7, and appears in MATH-500. Parse failures concentrate on contested candidates ($p<0.001$), making attrition non-ignorable. The design implication is operational: verify before any second-pass evaluation or peer exposure, and never treat post-debate unanimity as independent evidence of reliability.

---


### 180. [From Risk Scoring to Risk Allocation: A Density-Driven Framework for Diverse Monitoring in Multi-Agent Systems](https://arxiv.org/abs/2609.26146)

**<font color=#1a73e8>作者：</font>** Zhaohui Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Risk monitoring in multi-agent systems is commonly built on a per-state primitive that scores each state independently and selects the top K. Under crowding, where many agents share the same fragility, this approach picks redundant alerts whose risks are jointly correlated, a pattern we describe as ``herding in monitoring.'' We propose a paradigm shift from risk scoring to risk allocation, supported by two contributions. First, we identify the Crowding Paradox, namely that P(risk | x) $\propto$ p(x) rather than 1/p(x), so density rather than anomaly score is the operative risk signal; on financial data, density-based scoring reaches AUROC $\geq$ 0.94 at 5d/10d/20d crash horizons, while five anomaly baselines all fall below 0.80. Second, given a density-derived fragility score, we recast monitoring as combinatorial subset selection over interdependent states and map it to a QUBO objective with a $\lambda$-controlled risk--diversity tradeoff. The resulting Pareto frontier contains standard diverse-subset methods (MMR, k-DPP) as fixed operating points; the gain over greedy grows monotonically with scale, from +24% at n=15 to +66% at n=200; a learned $\lambda$ policy reaches 99.5% of an oracle grid-search objective; and the formulation transfers to traffic and multi-agent reinforcement learning. The same QUBO instances execute without modification on Rigetti superconducting QPUs (Ankaa-3 and Cepheus-1-108Q via Amazon Braket), which we report as a compatibility property of the formulation rather than a claim of quantum advantage at this scale.

---


### 181. [Designing Task-Induced Arousal: A Multimodal Stress Induction Method for Interactive Experiments](https://arxiv.org/abs/2609.26156)

**<font color=#1a73e8>作者：</font>** Morten Roed Frederiksen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> HCI and HRI studies often require short, repeatable arousal manipulations that can run while participants continue interacting with a device or robot. These experiments are often challenged by the need to induce arousal in settings that still resemble real interaction. Participants must continue using a device, touching a robot, or producing sensor data while the manipulation unfolds. We aimed to develop a compact and repeatable way to induce controlled task-related arousal during interactive experiments by combining a lightweight browser-based pacing task, escalating timing demands and urgency cues, and a concurrent physical hotwire-style challenge. In an A-B-A within-participant study, the induction condition significantly increased mental demand, temporal demand, effort, frustration, and SAM arousal (all p < .001), while perceived performance decreased (p < .001). GSR peak rate increased relative to both calm conditions (p = .030) and escalated over time (p < .001). Grip variability also increased (p = .036), as did release speed (both p < .001), while valence remained above the scale midpoint. These results provide initial evidence that the combined procedure induces controlled, relatively high-valence task-related arousal and may serve as a reusable experimental tool for future human-computer and human-robot interaction studies.

---


### 182. [Toward User-Mediated Self-Repair in Ubiquitous Robots Through Goal-Oriented Agentic AI](https://arxiv.org/abs/2609.26157)

**<font color=#1a73e8>作者：</font>** Morten Roed Frederiksen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ubiquitous robotic systems often lack traditional visual interfaces, necessitating resilient natural language interaction for maintenance and repair tasks. This paper presents a goal oriented agentic AI architecture designed to enable non-expert users to perform technical repairs through situated dialogue. The framework utilizes a multi-layered approach that decouples high-level strategic planning from reactive conversational execution to transform unconstrained human instructions into a structured hierarchy of goals. We conducted a study involving twenty participants to evaluate the system's efficacy using a physical hardware testbed. The architecture achieved a 95\% task completion rate, and participants reported positive self-efficacy following real-time guidance that adapted to conversational diversions and linguistic variations. A comparative analysis with an online baseline revealed that the transition to a physical environment significantly decreased perceived social presence (p=.0005), and trust and competence, (p=.037), while the agentic framework remained robust throughout the interaction. These findings indicate that goal oriented agentic AI can support the sustainability of body-worn technologies by empowering users to perform critical maintenance in ubiquitous contexts.

---


### 183. [The Free-Recipe Limit: Every Recipe Effect Measures Which Premise of an Idealised Learner Broke](https://arxiv.org/abs/2609.26160)

**<font color=#1a73e8>作者：</font>** Wenhui Chen, Jianlin Chen, Ziyao Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fix a corpus and send recipe search to infinity: try every order of the skills, every arrangement from blocked to interleaved, every composition, and keep the best. Two quantities decide what that search was worth: the diameter of the reachable set it explores, and the resolution at which anyone can tell two endpoints apart. Where the diameter falls below the resolution, no amount of search converts into a decision, and the signature is not an absence of winners but winners that do not survive re-running. We measure this recipe-search wall with 761 fine-tuning runs on 12 base models (0.5B-14B, three pretraining families) over competition-mathematics skills: base checkpoints, supervised fine-tuning under AdamW, exact-match scoring at k=4. Within one coherent domain at fixed volume the three classical freedoms average 0.010-0.021 against a 0.019 floor, and the largest contrast, 0.0619, clears a three-seed resolution and then reads +0.010 and -0.015 on two reruns. The departure with a systematic answer is coherence: halving one pooled corpus and letting the halves write answers under incompatible but equally correct conventions moves arrangement from capability to allocation between conventions, by two orders of magnitude over a same-convention control, and writing the convention into the input switches the phenomenon off. The switch replicates on a second pretraining family and survives an independent re-execution of its own protocol, with a re-execution spread (0.087) smaller than the resolution a search-selected order cell carries (0.144). Order itself is a transient whose sign crosses zero three times inside a single run. Volume, the one lever nobody calls a recipe, is the one that reliably pays. A public scorecard grades all 26 pre-registered claims: 18 supported, 5 failed, 2 untested, 1 mixed.

---


### 184. [Moving6DPoSe: A Multimodal Database for Monocular 6D Pose Estimation and Segmentation of Moving Objects](https://arxiv.org/abs/2609.26161)

**<font color=#1a73e8>作者：</font>** Ignacio Bugueno-Cordova, Javier Ruiz-del-Solar, Rodrigo Verschae  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating the 6D pose of moving objects remains challenging due to motion blur and the limited temporal resolution of conventional frame-based cameras. Existing event-based datasets further provide limited sensing modalities, annotations, and motion scenarios. We introduce Moving6DPoSe, a multimodal database comprising two complementary subsets: Moving6DPoSe-R with real-world recordings and Moving6DPoSe-S with synthetic sequences generated from the same objects. The dataset contains 16 scanned objects and 1,702 real and synthetic rosbags spanning multiple motion scenarios, with annotations for semantic segmentation, object detection, and monocular 6D pose estimation. We further provide baseline results for all three tasks across frame and event-based modalities. Experimental results show that event-based representations achieve more robust moving-object segmentation than conventional RGB images, while monocular orientation estimation remains challenging, highlighting the potential of Moving6DPoSe for moving-object perception research.

---


### 185. [MGRL-RSCC: Multi-Granularity Reward Reinforcement Learning for Fine-Grained Remote Sensing Change Captioning](https://arxiv.org/abs/2609.26166)

**<font color=#1a73e8>作者：</font>** Futian Wang, Mengqi Wang, Xiao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote Sensing Change Captioning (RSCC), which aims to generate accurate and detailed linguistic descriptions of ground object variations from bi-temporal remote sensing images, is a critical and challenging task in intelligent remote sensing interpretation. The mainstream autoregressive training paradigm faces severe exposure bias and train-test distribution mismatch, resulting in cumulative generation errors. They tend to produce conservative and template-fixed captions while ignoring subtle scene change details. To address these challenges, this paper proposes a novel multi-granularity reward reinforcement learning paradigm, termed MGRL-RSCC. Specifically, we first leverage a CNN and hierarchical self-attention module to extract and enhance visual features from bi-temporal remote sensing images. A Transformer decoder is then utilized to complete visual-to-linguistic translation. Different from existing methods, we design a dual-decoding strategy and a two-stage joint optimization scheme, which combines token-level supervised learning via greedy decoding and multi-granularity reward-driven self-critical reinforcement learning via sampling decoding. We further construct three complementary reward functions covering linguistic fluency, change state consistency, and structural-semantic relevance to comprehensively optimize caption quality and alleviate false and missing change descriptions. Extensive experiments on multiple public RSCC benchmark datasets demonstrate that the proposed MGRL-RSCC effectively mitigates exposure bias and conservative generation problems in traditional autoregressive methods. The source code and pre-trained models will be released on this https URL

---


### 186. [Activation-Energy Pruning for Spiking Neural Networks: Unsupervised Personalization via Spike-Count Saliency](https://arxiv.org/abs/2609.26167)

**<font color=#1a73e8>作者：</font>** Joseph Bingham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation-energy pruning -- removing weights whose product of magnitude and cumulative pre-synaptic spike count falls below a threshold -- was established as an effective unsupervised personalization strategy for conventional deep neural networks~\citep{BINGHAM2025101242}. This paper asks what happens when the same criterion is applied to spiking neural networks (SNNs), where activation energy is not merely a useful heuristic but a literal physical quantity proportional to the metabolic cost of each synapse. The answer is surprising on three counts.
First, gradient-based pruning methods that perform competitively on conventional networks (SNIP, GraSP, magnitude pruning) consistently underperform on SNNs, collapsing to near-chance accuracy by $\sigma = 0.2$ sparsity across all tested architectures and datasets. We trace this to a systematic incompatibility between surrogate-gradient saliency estimation and the binary spike-train representation, though we cannot rule out that alternative surrogate choices or hyperparameter settings might partially mitigate the effect.
Second, activation-energy pruning applied to a neuromorphic benchmark \emph{improves} over the source model at high sparsity ($98.4 \pm 0.4\%$ vs.\ $97.2 \pm 0.7\%$ at $\sigma = 0.8$ on N-MNIST), a phenomenon with no counterpart in the conventional network setting. We interpret this result as consistent with experience-dependent cortical specialisation: removing connections active only for non-target classes may reduce cross-class interference and produce a cleaner target representation, though we note this is an interpretive analogy rather than a mechanistic demonstration.

---


### 187. [Refusal without Discrimination: What Encoded Prompts Do to Safety-Trained Models](https://arxiv.org/abs/2609.26176)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Haowen Xu, Xiao Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Encoded-prompt attacks are evaluated almost entirely on their harmful arm: a benchmark sends obfuscated harmful requests and reports how often the model complied. We show that this arm carries almost no information about the model under test. Across four independently post-trained 7-8B models, refusal of harmful homoglyph-encoded prompts spans 0.08 -- inside the 0.10 ceiling that sampling noise alone produces at n=100 -- while the same four models span 0.57 on the identical requests in plaintext. What the encoding destroys is not refusal but discrimination: on one model the gap between harmful and benign refusal falls from +0.82 in plaintext to exactly 0.00 under the encoding, benign and harmful requests being refused at an identical 0.99. A benchmark reading only the harmful arm scores that model and one retaining a +0.61 gap identically. We then ask whether post-training repairs this, using a published recipe on identical base weights. It does not: across a full SFT -> DPO -> RLVR pipeline, plaintext harm discrimination improves from +0.55 to +0.80 while the encoding-induced loss is unchanged at 0.34-0.50, and on every encoding tested the standard harmful-arm metric moves in the opposite direction to discrimination. None of this is visible without controls the field does not routinely run. We report eight instrument defects, each with the control that caught it; they share a direction, in that every defect on the behaviour axis inflated apparent safety.

---


### 188. [Unread or Unenforced? Separating Representation from Enforcement Failure in Content Guards](https://arxiv.org/abs/2609.26178)

**<font color=#1a73e8>作者：</font>** Haoyu Zhang, Yi Feng, Mohammad Zandsalimy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> When an encoded attack passes a content guard, the guard either never represented the payload's harmful content or represented it and failed to act. End-to-end attack success rate reports one number for both, yet the remedies are opposite: one is a representational limit that more safety training cannot reach, the other a decision rule that it can. We separate them by reading a guard's own residual stream -- a content probe fitted on plaintext and transferred, without refitting, to the encoded condition -- alongside its verdict logits, at the cost of one forward pass and no judge model.
Doing this honestly is most of the problem, and it is our main contribution. A permutation test licenses the decode measurement on 17 of 19 conditions for one open guard and 12 of 19 for another; a length-matched null and a control floor calibrated on conditions the guard's base model provably cannot decode reduce both to 4. The discarded cells are not marginal ones: the largest result in our first analysis -- a guard representing a cipher at AUROC 0.72 while blocking none of it -- is an artefact on an encoding its base model decodes at rate zero. On one guard, two screens sharing no input agree exactly on which conditions to reject.
What survives is a policy failure that is real but narrower than the uncontrolled analysis claimed: 7 to 23 per 100 prompts represented and not blocked on conditions the guards block heavily, and 56 per 100 on one condition a guard barely blocks. Blocked without decoding is near zero throughout, so neither guard reacts to the appearance of encoding rather than to content. On genuine ciphers both guards block essentially nothing, and we report those cells as unmeasured rather than as evidence of failure to decode.

---


### 189. [TREND-10K: A Comprehensive Dataset for Next-Generation Video Quality Assessment Based on Preference-Driven Media](https://arxiv.org/abs/2609.26187)

**<font color=#1a73e8>作者：</font>** Ziheng Jia, Zicheng Zhang, Junqi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing prominence of short-video platforms, coupled with the advanced commercialization of AI-generated content (AIGC) videos, has led to a shift in the types of video media trend consumed by users in their daily lives. Traditional user-generated content (UGC) is gradually being replaced by professional short dramas and AIGC entertainment. Consequently, VQA for contemporary media content has become increasingly important. This requires a unified evaluation framework that can handle diverse video content and evolving media trends. In this context, we introduce TREND-10K, a next-generation comprehensive VQA dataset consisting of the trend-driven part and the static part, containing $10,000$ videos across a wide spectrum of content types. The trend-driven part is based on the TREND-Search framework, which captures user preference profiles from trending lists on online platforms and formulates sampling strategies based on these profiles. The static part, on the other hand, is composed of supplementary samples selected from publicly available datasets. To support unified evaluation for various video types, we incorporate three evaluation dimensions: technical, aesthetic, and AIGC-trace. Experiments show that our dataset ensures high annotation quality and exhibits remarkable generalization across multiple content categories. In conclusion, our work presents a robust framework for advancing VQA, addressing challenges caused by the temporal evolution of user perceptual habits and preferences.

---


### 190. [End-to-End Visual Odometry with RNNs and Attention](https://arxiv.org/abs/2609.26188)

**<font color=#1a73e8>作者：</font>** Ruiyu Li, Yinjia Liu, Alexander Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Odometry (VO) is the process of estimating the ego-motion of an object by analyzing visual information such as a sequence of frames from one or multiple cameras. It has been a popular research topic in computer vision and robotics, and its applications include mobile robotic systems as well as autonomous driving. In this project, we investigate existing end-to-end deep-learning approaches to VO, and propose a novel temporal attention-based model to improve upon the baseline. In addition, while the vast majority of existing deep-learning-based approaches to VO are trained on driving data, we investigate the performance of deep-learning-based VO to the more dynamic and complex problem of hand-held cameras.

---


### 191. [Topology-Aware Parameter-Efficient Adaptation for Cross-Dataset Retinal Vessel Segmentation](https://arxiv.org/abs/2609.26189)

**<font color=#1a73e8>作者：</font>** Yongsong Huang, Tomo Miyazaki, Kai Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retinal vessel segmentation in multi-domain deployment requires a source model to adapt to domains that differ in imaging conditions and annotation conventions. Conventional parameter-efficient fine-tuning reduces target-specific storage, but its highly restricted adaptation subspace can be insufficient for reconstructing thin, connected vascular structures. We therefore ask how target-specific capacity should be allocated so that topology-aware supervision remains effective under a strict per-domain parameter budget. Based on this principle, we propose TAPDecoderFT, a topology-responsive, role-structured adaptation framework. Specifically, TAPDecoderFT shares a fixed source parameter state across deployment domains, uses low-rank residuals for target-specific private/fusion feature mixing, and retains a trainable dense-reconstruction path comprising the decoder, output head, and refinement module. To promote structurally faithful predictions, the compact target state is jointly optimized with a region-overlap and topology-aware objective that encourages centerline continuity and thin-branch recovery. It improves both DSC and clDice over GenericLoRA-r4 and narrow TAP-r4 in all six directions and is comparable to full fine-tuning.

---


### 192. [Partially Observed Sparse Graphs: The Unknown Sampling Rate is a Tail Index](https://arxiv.org/abs/2609.26199)

**<font color=#1a73e8>作者：</font>** Jian Xu, Delu Zeng, John Paisley 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A large graph is often available only in part: a crawl stopped by its budget, a panel, a partial dump. When the sampled fraction $s$ is known by design the total edge count follows from $\hat e=e_s/s^2$ and no model is needed. We treat the case where $s$ is unknown and the population size is known. Our main result is a reduction: under a sparse exchangeable (graphex) model the expected non-isolated fraction obeys $n_s/n_1\to s^{1+\sigma}$, so the sampling rate becomes estimable once the tail index $\sigma$ is, and substituting it back gives $e_s(n_1/n_s)^{2/(1+\sigma)}$ -- the same estimator, with the design quantity inferred. Estimating global edge cardinality in a sparse graph is therefore, in expectation, tail-index estimation, and the quadratic graphon estimator is the case $\sigma=0$: it fails by an identity rather than by a fit ($260\%$ median error against $27\%$). We bound the finite-size error of the substitution and show the reduction is \emph{modular} in the tail-index estimator --- filled with a published closed-form one it reaches $21.7\%$ over $13$ networks and $39$ sampling budgets with no fitting at all. Fitting a full graphex additionally returns the degree distribution at any size and a generative object, in a representation where sparsity is a coordinate and the interpolation path is dictated rather than chosen. Two limits are exact: rank-one graphexes have transitivity fixed by the degree profile, so high-clustering graphs lie outside the class; and under snowball or random-walk crawls every method here fails, the design-based oracle worst of all ($7.8\%$ to $588\%$).

---


### 193. [Beyond the Lab: Large-Scale Remote Cybersickness Research in Virtual Reality Using the VERA Platform](https://arxiv.org/abs/2609.26203)

**<font color=#1a73e8>作者：</font>** Matt Gottsacker, Gerd Bruder, Daniel Zielasko 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cybersickness remains a major barrier for the adoption of virtual reality (VR), yet most existing knowledge is derived from laboratory-based studies with relatively small and homogeneous participant samples. In this paper, we investigate whether remote VR studies can produce cybersickness findings comparable to traditional in-lab experiments while enabling larger and more diverse participant populations. Using the Virtual Experience Research Accelerator (VERA), we deployed a remote adaptation of the standardized Cybersicker testbed for cybersickness research and collected data from N=263 participants using their own consumer VR headsets. We compared these results against a previously published in-lab dataset and a demographically matched subset of the remote sample. Across cohorts, cybersickness outcomes were consistent in direction and temporal pattern, including symptom onset trajectories, Fast Motion Sickness Scale (FMS) ratings, and Simulator Sickness Questionnaire (SSQ) responses, supporting the validity of remote cybersickness human-subjects research. Leveraging the larger remote dataset, we additionally examined demographic and individual-difference factors associated with cybersickness. These analyses confirm at scale the effects of sex, sickness susceptibility, and sickness expectation reported in smaller laboratory samples, and they add well-powered evidence on the contested relationship between age and cybersickness. These findings demonstrate that the VERA platform provides a viable means of remotely replicating laboratory-based studies and highlight its ability to support large, demographically diverse participant samples. This work establishes a validated methodological foundation for future large-scale remote studies of cybersickness and other VR research topics.

---


### 194. [RCShift: Certifying When Partial Linkage Suffices for Finite-Sample Decisions](https://arxiv.org/abs/2609.26207)

**<font color=#1a73e8>作者：</font>** Shuheng Cao, Ruiqi Chen, Zhenhao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Systems with costly gold outcomes and cheaper auxiliary observations must decide how much record linkage to retain. Complete pairing retains every joint counter, while separate margins retain none. Neither endpoint is calibrated to a declared finite-sample decision. Universal reconstruction can retain cycle directions invisible to the likelihood-ratio family. Family-exact storage can exceed what the decision requires because certified residual loss may fit within finite-sample slack. We introduce RCShift, which certifies two routes to sufficiency under a declared observation contract. Its exact mode characterizes minimum-cost family-exact storage through LR-visible cycle directions. Its approximate mode bounds reverse Le Cam deficiency. Its integer mode certifies whether a chosen set preserves the full experiment's minimum integer record count at specified size and power. In a rank-two witness, one aligned counter preserves a four-record minimum. An equal-cost misaligned counter and the margins require eleven records, while universal reconstruction requires two counters. A local perturbation has positive reverse deficiency yet retains the four-record minimum. Proof-checked scheduling bounds instantiate the contract before gold computation and yield exact reconstruction on the admitted tree support. RCShift turns partial-linkage storage into decision-calibrated measurement design for the declared family, costs, target, and common strictly positive support.

---


### 195. [Improved Multiplayer Bandit Algorithm for Bernoulli Rewards](https://arxiv.org/abs/2609.26213)

**<font color=#1a73e8>作者：</font>** Khang Nguyen, Ricardo Parada, William Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study the multiplayer multi-armed bandit problem with information asymmetry under Bernoulli rewards, for three information structures: asymmetry in actions, in rewards, and in both. Replacing the Hoeffding-style confidence intervals of prior work with Kullback--Leibler (KL) divergence-based bounds gives strictly tighter regret guarantees in each case. We propose \texttt{mKL-UCB}, \texttt{mKL-UCB-Intervals} and \texttt{mKL-DSEE}, and show that the improvement factor is at least two by Pinsker's inequality and far larger when reward means are near zero or one. For asymmetry in rewards we prove that two arms' KL intervals separate after a deterministic number of samples, and that $M$ independent players accelerate elimination further.

---


### 196. [Bridging the Data Gap: Digital Twin as a New Paradigm for AI-based Radio Sensing](https://arxiv.org/abs/2609.26214)

**<font color=#1a73e8>作者：</font>** Éloi Sainte-Beuve, Guillaume Larue, Louis-Adrien Dufrène 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a methodology that places a 3D digital twin (DT) of the environment as the main enabler behind the development of radio sensing at scale. The DT acts as a world model, providing geometry, materials, and transmitter/receiver placements to a ray-tracing engine that generates time-indexed channel impulse responses (CIRs) for large numbers of plausible scenes (moving people and objects, layout variants, seasonal/weather conditions, etc). From these synthetic sequences, we train a sequential neural network that maps CIR time series to spatial occupancy estimates, enabling device-free localization (DFL) without instrumented targets. We posit that sensing is best approached as an environment-conditioned learning problem: rather than seeking a single global model, we advocate training or fine-tuning local models specialized to a site-specific DT. As a first experiment, we introduce a novel State Space Model architecture, trained and evaluated across multiple room geometries. The localization performances obtained demonstrate the potential of the approach.

---


### 197. [Who Assures the Verifier? An Executable Assurance-Locus Audit of the European Digital Identity Wallet](https://arxiv.org/abs/2609.26220)

**<font color=#1a73e8>作者：</font>** Anton Sokolov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The European Digital Identity Wallet (EUDI Wallet) architecture places material duties on relying parties: they register services and intended uses, authenticate to Wallet Units, validate presentations and trust anchors, and make risk-based status decisions. Wallet certification and the emerging Functional Conformance Assessment Framework provide increasingly structured wallet-side evidence. A different question remains: what independently rerunnable evidence shows that the concrete relying-party verifier version used in a transaction enforced the applicable request, presentation and reliance-decision controls? We conduct an assurance-locus audit of current law, Architecture and Reference Framework (ARF) 3.0.0, ETSI metadata, FCAF scope and three pinned open-source verifier codebases. We then design a 17-rule research profile, a machine-readable evidence receipt and 36 frozen synthetic transactions. Three heterogeneous study-authored implementations (Python, JavaScript and jq) execute 108 cases with zero oracle mismatches and zero cross-path disagreements. The experiment establishes determinism and implementability of the proposed decision model, not product conformance or certification. Source inspection finds substantial protocol-verification mechanisms in all three public codebases but no single audited evidence object joining RP registration and purpose, exact verifier/policy version, transaction verdict and downstream attribute use. We therefore propose an RP-as-system-under-test evidence unit that complements, rather than displaces, wallet certification, registration and supervision. A preregistered census of 26 appointed experts is prepared to test content validity and governance feasibility; recruitment awaits the applicable ethics/data-protection determination.

---


### 198. [Quantum-Ready Secure WAN: A Risk Assessment and Migration Framework](https://arxiv.org/abs/2609.26225)

**<font color=#1a73e8>作者：</font>** Saeed Alam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise wide-area networks (WANs) use quantum-vulnerable public-key cryptography to authenticate peers and establish keys for Internet Protocol Security (IPsec), Transport Layer Security (TLS), and software-defined WAN services. Harvest-now, decrypt-later collection already threatens data whose protection lifetime may exceed the time needed to migrate, while a future cryptographically relevant quantum computer would also endanger certificates and other authentication dependencies. Post-quantum standards and government directives now define algorithms and transition milestones, but they do not tell an enterprise which WAN services to migrate first or what evidence is sufficient for deployment. This paper proposes a vendor-neutral framework that separates exposure priority, migration readiness, and evidence confidence, and maps those outputs to staged security, operational, and governance gates. It also defines a complete evaluation design for classical and ML-KEM hybrid key establishment in TLS 1.3 and IKEv2/IPsec. The retained artifact is narrower: it contains author-reported aggregate TLS p50, p95, and p99 latencies at configured loss settings of 0%, 1%, 3%, and 5%, an arithmetic checker, and limited environment and MTU/MSS notes. At those settings, the TLS-H minus TLS-C p95 differences are 0.00, 0.16, 0.38, and 0.63 ms, corresponding to 0.00%, 1.32%, 3.07%, and 5.00% relative to TLS-C. These values are descriptive aggregate observations, not inferential results, because per-trial data, sample counts, original captures, and timestamped logs were not retained. Protocol-size and MTU/MSS calculations are reported separately from measured behavior, and unsupported IKE, resource, throughput, retransmission, and downgrade outcomes are excluded.

---


### 199. [High-Order Liquid Evidence Modeling for Continuous and Subtle GNSS Spoofing Detection in Autonomous Driving](https://arxiv.org/abs/2609.26231)

**<font color=#1a73e8>作者：</font>** Muhammad Ayub Sabir, Junbiao Pang, Fatima Ashraf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous and subtle GNSS spoofing poses a serious threat to autonomous vehicles because forged positions may remain locally plausible while gradually becoming inconsistent with vehicle motion observed by non-GNSS onboard sensors. Existing AV-oriented detectors commonly rely on residual thresholds or feature-level classification and provide limited modeling of how weak GNSS--motion inconsistency develops and persists over time. This paper formulates subtle GNSS spoofing detection as a causal sequential evidence-modeling problem and proposes a high-order liquid evidence detector. The method first compares the displacement implied by consecutive GNSS positions with that inferred from independent onboard motion observations and converts their difference into uncertainty-normalized residual evidence. It then represents the current inconsistency, its local evolution, excess above the normal level, accumulated persistence, and displacement validity as causal weak evidence. These cues are mapped into instantaneous, evolutionary, and persistent latent states, aligned through a bounded Kirchhoff-inspired symmetric exchange, and combined through an explicit third-order interaction to capture their coordinated support for spoofing. To model how this coordinated evidence develops over time, second-order liquid dynamics track its memory and evolution to estimate causal spoofing probabilities, which are converted into confirmed alarms using validation-selected threshold and persistence parameters. Experiments on the AV--GPS dataset family demonstrate strong controlled and external generalization, together with clear sequential alarm behavior. On Dataset-1, the proposed detector achieves an AUROC of 0.9932 and an AUPRC of 0.9843, while obtaining the lowest false-positive rate among the learning-based baselines. Code: this https URL.

---


### 200. [The Temporal Moderation Gap: Text-to-Video Safety Filters Are Blind to Harm in Motion](https://arxiv.org/abs/2609.26233)

**<font color=#1a73e8>作者：</font>** Yuxin Cao, Fusen Guo, Yuezhong Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-video (T2V) services inherit their safety stack from image generation, pairing a keyword prompt filter with a per-frame checker that blocks a clip whenever one sampled frame looks unsafe. This stack has a blind spot unique to video. We prove that any moderator ignoring frame order accepts a harmful clip whenever it accepts that clip's benign shuffle, so harm carried by the ordering alone escapes. Empirically, the unmodified benchmark prompt already lands a clip in this moderation gap on 32.7% of Sequential-Action targets over four held-out seeds, and paraphrasing, scene splitting, and a feedback-driven prompt search show no significant improvement (paired McNemar $p\ge0.12$), so prompt engineering is not needed to expose the vulnerability. Dense-scoring all 97 rendered frames shows that about a third of the delivered clips merely hide an unsafe frame, while the rest stay harmful as ordered videos even though every frame passes, an order-blind residual the unmodified prompt reaches on a quarter of Sequential-Action targets. We also document a measurement pitfall, since scoring a searched prompt on its own render seed inflates a 7.5% per-generation rate into an apparent 46.7%. A user study confirms that people read these clips as harmful and their shuffles as safe. The fix is to read frame order, and an order-aware detector separates these clips from their own shuffles at AUC 0.74 where per-frame checking sits at chance, which is the signal deployed moderation throws away.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-275](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
