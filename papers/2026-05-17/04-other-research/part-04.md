# 📦 其他研究 | 2026年05月17日

> 本类共 **337** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-337](./part-07.md)

---

### 151. [A Novel Schur-Decomposition-Based Weight Projection Method for Stable State-Space Neural-Network Architectures](https://arxiv.org/abs/2605.14489)

**<font color=#1a73e8>作者：</font>** Sergio Vanegas, Lasse Lensu, Fredy Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building black-box models for dynamical systems from data is a challenging problem in machine learning, especially when asymptotic stability guarantees are required. In this paper, we introduce a novel stability-ensuring and backpropagation-compatible projection scheme based on the Schur decomposition for the state matrix of linear discrete-time state-space layers, as well as an alternative pre-factorized formulation of the methodology. The proposed methods dynamically project the quasi-triangular factor of the state matrix's real Schur decomposition onto its nearest stable peer, ensuring stable dynamics with minimal overparameterization. Experiments on synthetic linear systems demonstrate that the method achieves accuracy and convergence rates comparable to those of state-of-the-art stable-system identification techniques, despite a marginal increase in computational complexity. Furthermore, the lower weight count facilitates convergence during training without sacrificing accuracy in stacked neural-network architectures with static nonlinearities targeting real-world datasets. These results suggest that the Schur-based projection provides a numerically robust framework for identifying complex dynamics on par with the State of the Art while satisfying strict asymptotic-stability requirements.

---


### 152. [Learning Scenario Reduction for Two-Stage Robust Optimization with Discrete Uncertainty](https://arxiv.org/abs/2605.14494)

**<font color=#1a73e8>作者：</font>** Tianjue Lin, Jianan Zhou, Jieyi Bi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two-Stage Robust Optimization (2RO) with discrete uncertainty is challenging, often rendering exact solutions prohibitive. Scenario reduction alleviates this issue by selecting a small, representative subset of scenarios to enable tractable computation. However, existing methods are largely problem-agnostic, operating solely on the uncertainty set without consulting the feasible region or recourse structure. In this paper, we introduce PRISE, a problem-driven sequential lookahead heuristic that constructs reduced scenario sets by evaluating the marginal impact of each scenario. While PRISE yields high-quality scenario subsets, each selection step requires solving multiple subproblems, making it computationally expensive at scale. To address this, we propose NeurPRISE, a neural surrogate model built on a GNN-Transformer backbone that encodes the per-scenario structure via graph convolution and captures cross-scenario interactions through attention. NeurPRISE is trained via imitation learning with a gain-aware ranking objective, which distills marginal gain information from PRISE into a learned scoring function for scenario ranking and selection. Extensive results on three 2RO problems show that NeurPRISE consistently achieves competitive regret relative to comprehensive methods, maintains strong calability with varying numbers of scenarios, and delivers 7-200x speedup over PRISE. NeurPRISE also exhibits strong zero-shot generalization, effectively handling instances with larger problem scales (up to 5x), more scenarios (up to 4x), and distribution shifts.

---


### 153. [ROAD: Adaptive Data Mixing for Offline-to-Online Reinforcement Learning via Bi-Level Optimization](https://arxiv.org/abs/2605.14497)

**<font color=#1a73e8>作者：</font>** Letian Yang, Xu Liu, Yiqiang Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline-to-online reinforcement learning harnesses the stability of offline pretraining and the flexibility of online fine-tuning. A key challenge lies in the non-stationary distribution shift between offline datasets and the evolving online policy. Common approaches often rely on static mixing ratios or heuristic-based replay strategies, which lack adaptability to different environments and varying training dynamics, resulting in suboptimal tradeoff between stability and asymptotic performance. In this work, we propose Reinforcement Learning with Optimized Adaptive Data-mixing (ROAD), a dynamic plug-and-play framework that automates the data replay process. We identify a fundamental objective misalignment in existing approaches. To tackle this, we formulate the data selection problem as a bi-level optimization process, interpreting the data mixing strategy as a meta-decision governing the policy performance (outer-level) during online fine-tuning, while the conventional Q-learning updates operate at the inner level. To make it tractable, we propose a practical algorithm using a multi-armed bandit mechanism. This is guided by a surrogate objective approximating the bi-level gradient, which simultaneously maintains offline priors and prevents value overestimation. Our empirical results demonstrate that this approach consistently outperforms existing data replay methods across various datasets, eliminating the need for manual, context-specific adjustments while achieving superior stability and asymptotic performance.

---


### 154. [HASTE: Training-Free Video Diffusion Acceleration via Head-Wise Adaptive Sparse Attention](https://arxiv.org/abs/2605.14513)

**<font color=#1a73e8>作者：</font>** Xuzhe Zheng, Yuexiao Ma, Jing Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based video generation has advanced substantially in visual fidelity and temporal coherence, but practical deployment remains limited by the quadratic complexity of full attention. Training-free sparse attention is attractive because it accelerates pretrained models without retraining, yet existing online top-$p$ sparse attention still spends non-negligible cost on mask prediction and applies shared thresholds despite strong head-level heterogeneity. We show that these two overlooked factors limit the practical speed-quality trade-off of training-free sparse attention in Video DiTs. To address them, we introduce a head-wise adaptive framework with two plug-in components: Temporal Mask Reuse, which skips unnecessary mask prediction based on query-key drift, and Error-guided Budgeted Calibration, which assigns per-head top-$p$ thresholds by minimizing measured model-output error under a global sparsity budget. On Wan2.1-1.3B and Wan2.1-14B, our method consistently improves XAttention and SVG2, achieving up to 1.93 times speedup at 720P while maintaining competitive video quality and similarity metrics.

---


### 155. [ArcGate: Adaptive Arctangent Gated Activation](https://arxiv.org/abs/2605.14518)

**<font color=#1a73e8>作者：</font>** Avik Bhattacharya, Siddhant Dnyanesh Gole, Subhasis Chaudhuri 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Activation functions are central to deep networks, influencing non-linearity, feature learning, convergence, and robustness. This paper proposes the Adaptive Arctangent Gated Activation (ArcGate) function, a flexible formulation that generates a broad spectrum of activation shapes via a three-stage non-linear transformation. Unlike conventional fixed-shape activations such as ReLU, GELU, or SiLU, ArcGate uses seven learnable parameters per layer, allowing the neural network to autonomously optimize its non-linearity to the specific requirements of the feature hierarchy and data distribution. We evaluate ArcGate using ResNet-50 and Vision Transformer (ViT-B/16) architectures on three widely used remote sensing benchmarks: PatternNet, UC Merced Land Use, and the 13-band EuroSAT MSI multispectral dataset. Experimental results show that ArcGate consistently outperforms standard baselines, achieving a peak overall accuracy of 99.67% on PatternNet. Most notably, ArcGate exhibits superior structural resilience in noisy environments, maintaining a 26.65% performance lead over ReLU under moderate Gaussian noise (standard deviation 0.1). Analysis of the learned parameters reveals a depth-dependent functional evolution, where the model increases gating strength in deeper layers to enhance signal propagation. These findings suggest that ArcGate is a robust and adaptive general node activation function for high-resolution earth observation tasks.

---


### 156. [Enjoy Your Layer Normalization with the Computational Efficiency of RMSNorm](https://arxiv.org/abs/2605.14521)

**<font color=#1a73e8>作者：</font>** Yuxin Guo, Yihao Yue, Yunhao Ni 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Layer normalization (LN) is a fundamental component in modern deep learning, but its per-sample centering and scaling introduce non-negligible inference overhead. RMSNorm improves efficiency by removing the centering operation, yet this may discard benefits associated with centering. This paper propose a framework to determine whether an LN in an arbitrary DNN can be replaced by RMSNorm without changing the model function. The key idea is to fold LN's centering operation into upstream general linear layers by enforcing zero-mean outputs through the column-centered constraint (CCC) and column-based weight centering (CBWC). We extend the analysis to arbitrary DNNs, define such LNs as foldable LNs, and develop a graph-based detection algorithm. Our analysis shows that many LNs in widely used architectures are foldable, enabling exact inference-time conversion and end-to-end acceleration of 2% to 12% without changing model predictions. Experiments across multiple task families further show that, when exact equivalence is partially broken in practical training settings, our method remains competitive with vanilla LN while improving efficiency.

---


### 157. [From Sparse to Dense: Spatio-Temporal Fusion for Multi-View 3D Human Pose Estimation with DenseWarper](https://arxiv.org/abs/2605.14525)

**<font color=#1a73e8>作者：</font>** Ling Li, Changjie Chen, Yuyan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In multi-view 3D human pose estimation, models typically rely on images captured simultaneously from different camera views to predict a pose at a specific moment. While providing accurate spatial information, this traditional approach often overlooks the rich temporal dependencies between adjacent frames. We propose a novel 3D human pose estimation input method: the sparse interleaved input to address this. This method leverages images captured from different camera views at various time points (e.g., View 1 at time $t$ and View 2 at time $t+\delta$), allowing our model to capture rich spatio-temporal information and effectively boost performance. More importantly, this approach offers two key advantages: First, it can theoretically increase the output pose frame rate by N times with N cameras, thereby breaking through single-view frame rate limitations and enhancing the temporal resolution of the production. Second, using a sparse subset of available frames, our method can reduce data redundancy and simultaneously achieve better performance. We introduce the DenseWarper model, which leverages epipolar geometry for efficient spatio-temporal heatmap exchange. We conducted extensive experiments on the Human3.6M and MPI-INF-3DHP datasets. Results demonstrate that our method, utilizing only sparse interleaved images as input, outperforms traditional dense multi-view input approaches and achieves state-of-the-art performance. The source code for this work is available at: this https URL

---


### 158. [Language Generation as Optimal Control: Closed-Loop Diffusion in Latent Control Space](https://arxiv.org/abs/2605.14531)

**<font color=#1a73e8>作者：</font>** ZiYi Dong, Yuliang Huang, Weijian Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work reformulates language generation as a stochastic optimal control problem, providing a unified theoretical perspective to analyze autoregressive and diffusion models and explain their limitations (Efficiency-Fidelity Paradox, Irreversibility Error Propagation, Optimization Tractability and Fidelity) in terms of combination of trajectory singularity, adjoint state vanishing, and gradient absence. To address these issues, we approximate the solution to the Hamilton-Jacobi-Bellman (HJB) equation, yielding an optimal policy that acts as a closed-loop controller. To bypass the intractability of directly solving the HJB PDE, we employ Flow Matching as the optimal trajectory solver within the rectified latent control space. This allows our Manta-LM with Global Integral Operator to approximate the global vector field, effectively realizing a model that simultaneously achieves high-fidelity text generation and efficient, low-cost parallel sampling. Empirically, our method achieves strong performance on language modeling and conditional generation tasks, while exhibiting improved stability, efficiency, and controllability.

---


### 159. [PROVE: A Perceptual RemOVal cohErence Benchmark for Visual Media](https://arxiv.org/abs/2605.14534)

**<font color=#1a73e8>作者：</font>** Fuhao Li, Shaofeng You, Jiagao Hu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Evaluating object removal in images and videos remains challenging because the task is inherently one-to-many, yet existing metrics frequently disagree with human perception. Full-reference metrics reward copy-paste behaviors over genuine erasure; no-reference metrics suffer from systematic biases such as favoring blurry results; and global temporal metrics are insensitive to localized artifacts within edited regions. To address these limitations, we propose RC (Removal Coherence), a pair of perception-aligned metrics: RC-S, which measures spatial coherence via sliding-window feature comparison between masked and background regions, and RC-T, which measures temporal consistency via distribution tracking within shared restored regions across adjacent frames. To validate RC and support community benchmarking, we further introduce PROVE-Bench, a two-tier real-world benchmark comprising PROVE-M, an 80-video paired dataset with motion augmentation, and PROVE-H, a 100-video challenging subset without ground truth. Together, RC metrics and PROVE-Bench form the PROVE (Perceptual RemOVal cohErence) evaluation framework for visual media. Experiments across diverse image and video benchmarks demonstrate that RC achieves substantially stronger alignment with human judgments than existing evaluation protocols. The code for RC metrics and PROVE-Bench are publicly available at: this https URL.

---


### 160. [Learning from Failures: Correction-Oriented Policy Optimization with Verifiable Rewards](https://arxiv.org/abs/2605.14539)

**<font color=#1a73e8>作者：</font>** Mengjie Ren, Jie Lou, Boxi Cao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as an effective paradigm for improving the reasoning capabilities of large language models. However, RLVR training is often hindered by sparse binary rewards and weak credit assignment, resulting in ambiguous optimization signals and underutilization of the useful information embedded in failed trajectories. To address this challenge, we propose Correction-Oriented Policy Optimization (CIPO), a simple and effective extension to RLVR that converts on-policy failed trajectories into correction-oriented supervision, without relying on any external signals. By jointly optimizing correction samples derived from the model's own failed attempts together with the standard RLVR objective, CIPO improves learning effectiveness while explicitly enhancing the model's ability to correct its own errors. Extensive experiments across 11 benchmarks spanning mathematical reasoning and code generation demonstrate that CIPO consistently and significantly outperforms strong baselines in both reasoning and correction performance. Moreover, CIPO yields stronger pass@K gains, indicating that it improves the model's intrinsic reasoning capacity rather than merely redistributing probability mass over existing correct answers.

---


### 161. [Discovering Physical Directions in Weight Space: Composing Neural PDE Experts](https://arxiv.org/abs/2605.14546)

**<font color=#1a73e8>作者：</font>** Pengkai Wang, Pengwei Liu, Yuanyi Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in neural operators have made partial differential equation (PDE) surrogate modeling increasingly scalable and transferable through large-scale pretraining and in-context adaptation. However, after a shared operator is fine-tuned to multiple regimes within a continuous physical family, it remains unclear whether the resulting weight-space updates merely form isolated regime experts or reveal reusable physical structure. Starting from a shared family anchor, we fine-tune low- and high-regime endpoint experts and show that their updates can be separated into a family-shared adaptation and a direction aligned with the underlying physical parameter. This separation reinterprets endpoint experts as finite-difference probes of a local physical direction in weight space, explaining why static averaging can interpolate between regimes but attenuates endpoint-specific physics. Building on this perspective, we propose Calibration-Conditioned Merge (CCM), a post-hoc coordinate readout method for composing neural PDE experts along this physical direction. Given physical metadata, a calibrated coordinate mapping, or a short observed rollout prefix, CCM infers the target composition coordinate and deploys a single merged checkpoint for the remaining rollout. We evaluate CCM on the reaction--diffusion system, viscosity-parameterized two-dimensional Navier--Stokes equations, and radial dam-break dynamics. Across these benchmarks, CCM achieves its strongest gains in extrapolative regimes, reducing out-of-distribution rollout error relative to the family anchor by 54.2%, 42.8%, and 13.8%, respectively. Further experiments across FNO scales, a DPOT-style backbone, and ablations confirm that endpoint fine-tuning is not arbitrary checkpoint drift, but reveals a calibratable physical direction for training-free transfer across PDE regimes.

---


### 162. [Local Spatiotemporal Convolutional Network for Robust Gait Recognition](https://arxiv.org/abs/2605.14548)

**<font color=#1a73e8>作者：</font>** Xiaoyun Wang, Cunrong Li, Wu Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition, as a promising biometric technology, identifies individuals through their unique walking patterns and offers distinctive advantages including non-invasiveness, long-range applicability, and resistance to deliberate disguise. Despite these merits, capturing the intrinsic motion patterns concealed within consecutive video frames remains challenging due to the complexity of video data and the interference of external covariates such as viewpoint changes, clothing variations, and carrying conditions. Existing approaches predominantly rely on either static appearance features extracted from individual silhouette frames or employ complex sequential models (\eg, LSTM, 3D convolutions) that demand substantial computational resources and sophisticated training strategies. To address these limitations, we propose a Local Spatiotemporal Convolutional Network (LSTCN), a structurally simple yet highly effective dual-branch architecture that endows standard two-dimensional convolutional networks with the capacity to extract temporal information. Specifically, we introduce a Global Bidirectional Spatial Pooling (GBSP) mechanism that reduces the dimensionality of gait tensors by decomposing spatial features into horizontal and vertical strip-based local representations, enabling the temporal dimension to participate in standard 2D convolution operations. Building upon this, we design a Local Spatiotemporal Convolutional (LSTC) layer that jointly processes temporal and spatial dimensions, allowing the network to adaptively learn strip-based gait motion patterns. We further extend this formulation with asymmetric convolution kernels that independently attend to the temporal, spatial, and joint spatiotemporal domains, thereby enriching the extracted feature representations.

---


### 163. [Multi-Dimensional Model Integrity and Responsibility Assessment Index and Scoring Framework](https://arxiv.org/abs/2605.14550)

**<font color=#1a73e8>作者：</font>** Phuc Truong Loc Nguyen, Thanh Hung Do, Truong Thanh Hung Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence in high-stakes tabular domains cannot be evaluated by predictive performance alone, yet current practice still assesses explainability, fairness, robustness, privacy, and sustainability mostly in isolation. We propose the Model Integrity and Responsibility Assessment Index (MIRAI), a unified evaluation framework that measures tabular models across these five dimensions under a controlled comparison setting and aggregates them into a single score. MIRAI combines established metrics through normalized and direction-aligned dimension scores, which enables direct comparison across models with different architectural and computational profiles. Experiments on healthcare, financial, and socioeconomic datasets show that higher predictive performance does not necessarily imply better overall integrity and responsibility. In several cases, simpler models achieve a stronger cross-dimensional balance than more complex deep tabular architectures. MIRAI provides a compact and practical basis for responsible model selection in regulated settings.

---


### 164. [SeesawNet: Towards Non-stationary Time Series Forecasting with Balanced Modeling of Common and Specific Dependencies](https://arxiv.org/abs/2605.14551)

**<font color=#1a73e8>作者：</font>** Hao Li, Lu Zhang, Liu Chong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instance normalization (IN) is widely used in non-stationary multivariate time series forecasting to reduce distribution shifts and highlight common patterns across samples. However, IN can over-smooth instance-specific structural information that is essential for modeling temporal and cross-channel heterogeneity. While prior methods further suppress distribution discrepancies or attempt to recover temporal specific dependencies, they often ignore a central tension: how to adaptively model common and instance-specific dependency based on each instance's non-stationary structures. To address this dilemma, we propose SeesawNet, a unified architecture that dynamically balances common and instance-specific dependency modeling in both temporal and channel dimensions. At its core is Adaptive Stationary-Nonstationary Attention (ASNA), which captures common dependencies from normalized sequences and specific dependencies from raw sequences, and adaptively fuses them according to instance-level non-stationarity. Built upon ASNA, SeesawNet alternates dedicated temporal and channel relationship modeling to jointly capture long-range and cross-variable dependencies. Extensive experiments on multiple real-world benchmarks demonstrate that SeesawNet consistently outperforms state-of-the-art methods.

---


### 165. [LiWi: Layering in the Wild](https://arxiv.org/abs/2605.14552)

**<font color=#1a73e8>作者：</font>** Yu He, Fang Li, Haoyang Tong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative models have empowered impressive layered image generation, yet their success is largely confined to graphic design domains. The layering of in-the-wild images remains an underexplored problem, limiting fine-grained editing and applications of images in real-world scenarios. Specifically, challenges remain in scalable layered data and the modeling of object interaction in natural images, such as illumination effects and structural boundary. To address these bottlenecks, we propose a novel framework for high-fidelity natural image decomposition. First, we introduce an Agent-driven Data Decomposition (ADD) pipeline that orchestrates agents and tools to synthesize layered data without manual intervention. Utilizing this pipeline, we construct a large-scale dataset, named LiWi-100k, with over 100,000 high-quality layered in-the-wild images. Second, we present a novel framework that jointly improves photometric fidelity and alpha boundary accuracy. Specifically, shadow-guided learning explicitly models the illumination effects, and degradation-restoration objective provides boundary-correction supervision by recovering clean foreground image from degraded one. Extensive experiments demonstrate that our framework achieves state-of-the-art (SoTA) performance in natural image decomposition, outperforming existing models in RGB L1 and Alpha IoU metrics. We will soon release our code and dataset.

---


### 166. [Efficient Multi-objective Prompt Optimization via Pure-exploration Bandits](https://arxiv.org/abs/2605.14553)

**<font color=#1a73e8>作者：</font>** Donghao Li, Chengshuai Shi, Weijuan Ou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prompt engineering has become central to eliciting the capabilities of large language models (LLMs). At its core lies prompt selection -- efficiently identifying the most effective prompts. However, most prior investigations overlook a key challenge: the inherently multi-faceted nature of prompt performance, which cannot be captured by a single metric. To fill this gap, we study the multi-objective prompt selection problem under two practical settings: Pareto prompt set recovery and best feasible prompt identification. Casting the problem into the pure-exploration bandits framework, we adapt provably efficient algorithms from multi-objective bandits and further introduce a novel design for best feasible arm identification in structured bandits, with theoretical guarantees on the identification error in the linear case. Extensive experiments across multiple LLMs show that the bandit-based approaches yield significant improvements over baselines, establishing a principled and efficient framework for multi-objective prompt optimization.

---


### 167. [PyCSP3-Scheduling: A Scheduling Extension for PyCSP3](https://arxiv.org/abs/2605.14559)

**<font color=#1a73e8>作者：</font>** Sohaib Afifi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> PyCSP$^3$ provides a productive way to build constraint models for solving combinatorial constrained problems and export them to XCSP$^3$, preserving a complete separation between modeling and solving. However, it lacks native support for scheduling abstractions such as interval variables, sequence variables, and resource functions. As a result, scheduling models must be encoded with low-level integer variables and manual channeling constraints, even though PyCSP$^3$ already provides global constraints like NoOverlap and Cumulative on integer arrays. We present PyCSP$^3$ Scheduling, a library that adds scheduling abstractions to PyCSP$^3$ through 53 dedicated constraints and 27 expressions, and compiles them down to standard PyCSP$^3$/XCSP$^3$ constraints, maintaining the modeling/solving separation that underpins the PyCSP$^3$ ecosystem. On 261 paired instances across 17 model families (5 runs each), both formulations produce identical objectives on all 72 doubly-proved optimal pairs and nearly half of the families (8/17) remain structurally unchanged after compilation; however, runtime performance diverges across families, with clear gains on some (up to 5.8x) and regressions on others due to the overhead of compilation decompositions. Code and benchmarks are available at: this https URL

---


### 168. [SpectraFlow: Unifying Structural Pretraining and Frequency Adaptation for Medical Image Segmentation](https://arxiv.org/abs/2605.14566)

**<font color=#1a73e8>作者：</font>** Zhiquan Chen, Haitao Wang, Guowei Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation remains challenging in low-data regimes, where scarce annotations often yield poor generalization and ambiguous boundaries with missing fine structures. Recent self-supervised pretraining has improved transferability, but it often exhibits a texture bias. In contrast, accurate segmentation is inherently geometry-aware and depends on both topological consistency and precise boundary preservation. To address this problem, we propose a two-stage framework that couples structure-aware encoder pretraining with boundary-oriented decoding. In Stage-1, we aim to learn structure-aware representations for downstream segmentation in low-data regimes. To this end, we propose Mixed-Domain MeanFlow Pretraining, which aligns images and binary masks in a shared latent space through latent transport regression, where masks act as conditional structural guidance rather than prediction targets, making the pretraining task-agnostic. To further improve training stability under scarce supervision, we incorporate a lightweight Dispersive Loss to prevent representation collapse. In Stage-2, we fine-tune the pretrained encoder with a lightweight decoder that combines Direct Attentional Fusion for adaptive cross-scale gating and Frequency-Directional Dynamic Convolution for high-frequency boundary refinement under appearance variation. Experiments on ISIC-2016, Kvasir-SEG, and GlaS demonstrate consistent gains over state-of-the-art methods, with improved robustness in low-data settings and sharper boundary delineation.

---


### 169. [Bridging Brain and Semantics: A Hierarchical Framework for Semantically Enhanced fMRI-to-Video Reconstruction](https://arxiv.org/abs/2605.14569)

**<font color=#1a73e8>作者：</font>** Yujie Wei, Chenglong Ma, Jianxiong Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic visual experiences as videos from functional magnetic resonance imaging (fMRI) is pivotal for advancing the understanding of neural processes. However, current fMRI-to-video reconstruction methods are hindered by a semantic gap between noisy fMRI signals and the rich content of videos, stemming from a reliance on incomplete semantic embeddings that neither capture video-specific cues (e.g., actions) nor integrate prior knowledge. To this end, we draw inspiration from the dual-pathway processing mechanism in human brain and introduce CineNeuron, a novel hierarchical framework for semantically enhanced video reconstruction from fMRI signals with two synergistic stages. First, a bottom-up semantic enrichment stage maps fMRI signals to a rich embedding space that comprehensively captures textual semantics, image contents, action concepts, and object categories. Second, a top-down memory integration stage utilizes the proposed Mixture-of-Memories method to dynamically select relevant "memories" from previously seen data and fuse them with the fMRI embedding to refine the video reconstruction. Extensive experimental results on two fMRI-to-video benchmarks demonstrate that CineNeuron surpasses state-of-the-art methods across various metrics.

---


### 170. [Uncertainty Quantification for Large Language Diffusion Models](https://arxiv.org/abs/2605.14570)

**<font color=#1a73e8>作者：</font>** Artem Vazhentsev, Vladislav Smirnov, David Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Diffusion Models (LLDMs) are emerging as an alternative to autoregressive models, offering faster inference through higher parallelism. Similar to autoregressive LLMs, they remain prone to hallucinations, making reliable uncertainty quantification (UQ) crucial for safe deployment. However, existing UQ methods are fundamentally misaligned with this new paradigm: they assume autoregressive factorization or use expensive repeated sampling, negating the efficiency of LLDMs. In this work, we present the first systematic study of UQ for LLDMs and propose lightweight, zero-shot uncertainty signals derived from the iterative denoising process, leveraging intermediate generations, token remasking dynamics, and denoising complexity. We further adapt a state-of-the-art UQ method to LLDMs by combining masked diffusion likelihoods with trajectory-based semantic dissimilarity. We prove that expected trajectory dissimilarity lower bounds the masked diffusion training objective, which motivates its usage as an uncertainty score. Comprehensive experiments across three tasks, eight datasets, and two models show that our method achieves a great cost-performance trade-off: it approaches the strongest sampling-based baselines while incurring up to 100x lower computational overhead. Our work demonstrates that LLDMs can deliver both fast inference and reliable hallucination detection simultaneously.

---


### 171. [Woodelf++: A Fast and Unified Partial Dependence Plot Algorithm for Decision Tree Ensembles](https://arxiv.org/abs/2605.14578)

**<font color=#1a73e8>作者：</font>** Ron Wettenstein, Alexander Nadel, Udi Boker  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Partial Dependence Plots (PDPs) visualize how changes in a single feature affect the average model prediction. They are widely used in practice to interpret decision tree ensembles and other machine learning models. Joint-PDPs extend this idea to pairs of features, revealing their combined effect. Partial Dependence Interaction Values (PDIVs) measure feature interactions. The Any-Order-PDIVs task computes these interactions for every feature subset across all rows of the dataset.
We introduce Woodelf++, a unified and efficient approach for computing all these useful explainability tools on decision tree ensembles, building on Woodelf, an algorithm for efficient SHAP computation. By deriving suitable metrics over pseudo-Boolean functions, Woodelf++ can compute PDPs (exact and approximate), Joint-PDPs, and Any-Order-PDIVs in a unified framework. Our method delivers substantial complexity improvements over the state of the art, including an exponential gain for Any-Order-PDIVs. Additionally, we introduce and efficiently compute Full PDPs, which leverage the model's split thresholds to faithfully capture its behavior across all possible feature values.
Woodelf++ is implemented in pure Python and supports GPU acceleration. On a dataset with 400,000 rows, Woodelf++ computes PDP and Joint-PDP up to 6x faster than the state of the art and up to five orders of magnitude faster than scikit-learn. For Any-Order-PDIVs, the gap is even larger: Woodelf++ computes all interaction values in 5 minutes, while the state of the art is estimated to require over 1,000,000 years.

---


### 172. [Med-DisSeg: Dispersion-Driven Representation Learning for Fine-Grained Medical Image Segmentation](https://arxiv.org/abs/2605.14579)

**<font color=#1a73e8>作者：</font>** Zhiquan Chen, Haitao Wang, Guowei Zou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate medical image segmentation is fundamental to precision medicine, yet robust delineation remains challenging under heterogeneous appearances, ambiguous boundaries, and large anatomical variability. Similar intensity and texture patterns between targets and surrounding tissues often lead to blurred activations and unreliable separation. We attribute these failures to representation collapse during encoding and insufficient fine grained multi scale decoding. To address these issues, we propose Med DisSeg, a dispersion driven medical image segmentation framework that jointly improves representation learning and anatomical delineation. Med DisSeg combines a lightweight Dispersive Loss with adaptive attention for fine grained structure segmentation. The Dispersive Loss enlarges inter sample margins by treating in batch hidden representations as negative pairs, producing well dispersed and boundary aware embeddings with negligible overhead. Based on these enhanced representations, the encoder strengthens structure sensitive responses, while the decoder performs adaptive multi scale calibration to preserve complementary local texture and global shape information. Extensive experiments on five datasets spanning three imaging modalities demonstrate consistent state of the art performance. Moreover, Med DisSeg achieves competitive results on multi organ CT segmentation, supporting its robustness and cross task applicability.

---


### 173. [A Picture is Worth a Thousand Words? An Empirical Study of Aggregation Strategies for Visual Financial Document Retrieval](https://arxiv.org/abs/2605.14581)

**<font color=#1a73e8>作者：</font>** Ho Hung Lim, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual RAG has offered an alternative to traditional RAG. It treats documents as images and uses vision encoders to obtain vision patch tokens. However, hundreds of patch tokens per document create retrieval and storage challenges in a vector database. Practical deployment requires aggregating them into a single vector. This raises a critical question: does single-vector aggregation lose key information in financial documents? We develop a diagnostic benchmark using financial documents where changes in single digits can lead to significant semantic shifts. Our experiments show that single-vector aggregation collapses different documents with almost identical vectors. Metrics show that the patch level detects semantic changes, and confirm that aggregation obscures these details. We identify global texture dominance as the root cause. Our findings are consistent across model scales, retrieval-optimized embeddings, and multiple mitigation strategies, highlighting significant risks for single-vector visual document retrieval in financial applications.

---


### 174. [Angel or Demon: Investigating the Plasticity Interventions' Impact on Backdoor Threats in Deep Reinforcement Learning](https://arxiv.org/abs/2605.14587)

**<font color=#1a73e8>作者：</font>** Oubo Ma, Ruixiao Lin, Yang Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extensive research has highlighted the severe threats posed by backdoor attacks to deep reinforcement learning (DRL). However, prior studies primarily focus on vanilla scenarios, while plasticity interventions have emerged as indispensable built-in components of modern DRL agents. Despite their effectiveness in mitigating plasticity loss, the impact of these interventions on DRL backdoor vulnerabilities remains underexplored, and this lack of systematic investigation poses risks in practical DRL deployments. To bridge this gap, we empirically study 14,664 cases integrating representative interventions and attack scenarios. We find that only one intervention (i.e., SAM) exacerbates backdoor threats, while other interventions mitigate them. Pathological analysis identifies that the exacerbation is attributed to backdoor gradient amplification, while the mitigation stems from activation pathway disruption and representation space compression. From these findings, we derive two novel insights: (1) a conceptual framework SCC for robust backdoor injection that deconstructs the mechanistic interplay between interventions and backdoors in DRL, and (2) abnormal loss landscape sharpness as a key indicator for DRL backdoor detection.

---


### 175. [Silent Collapse in Recursive Learning Systems](https://arxiv.org/abs/2605.14588)

**<font color=#1a73e8>作者：</font>** Zhipeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive learning -- where models are trained on data generated by previous versions of themselves -- is increasingly common in large language models, autonomous agents, and self-supervised systems. However, standard performance metrics (loss, perplexity, accuracy) often fail to detect internal degradation before it becomes irreversible. Here we identify a phenomenon we call silent collapse: under broad recursive conditions, model internal distributions -- predictive entropy, representational diversity, and tail coverage -- progressively contract even as conventional metrics appear stable or improving.
We discover that silent collapse is not abrupt. Its onset is reliably preceded by three trajectory-level precursors: (1) contraction of anchor entropy, (2) freezing of representation drift, and (3) erosion of tail coverage. These signals manifest multiple generations before any degradation in standard validation metrics, enabling early warning.
Based on these precursors, we propose the MTR (Monitor--Trust--Regulator) framework, a lightweight metacognitive loop that monitors trajectory statistics, estimates a slow-timescale trust variable, and adaptively modulates the effective learning intensity. MTR provides early warning and actively prevents silent collapse without requiring access to pristine real data -- a critical advantage when original data is unavailable, contaminated, or private.

---


### 176. [FedStain: Modeling Higher-Order Stain Statistics for Federated Domain Generalization in Computational Pathology](https://arxiv.org/abs/2605.14590)

**<font color=#1a73e8>作者：</font>** Fengyi Zhang, Junya Zhang, Wenzhuo Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust whole-slide image (WSI) analysis under strict data-governance remains challenging due to substantial cross-institutional stain heterogeneity. Domain generalization (DG) mitigates these shifts but typically requires centralized data, conflicting with privacy regulations. Federated learning (FedL) provides a decentralized alternative; however, existing FedL and federated DG (FedDG) approaches rely almost exclusively on low-order statistics, assuming Gaussian-like stain distributions. In contrast, real-world staining processes often produce asymmetric, heavy-tailed color distributions due to biochemical diffusion and scanner nonlinearity. Consequently, current methods fail to model the higher-order, non-Gaussian characteristics dominating real-world stain variability. To address this, we propose FedStain, a stain-aware FedDG framework explicitly incorporating higher-order stain moments--skewness and kurtosis--as compact statistical descriptors exchanged during federated optimization. These descriptors require no pixel-level data transmission, preserving strict privacy and communication efficiency, while enabling the global model to capture stain variability missed by low-order statistics. FedStain also employs a contrastive, cross-site parameter aggregation strategy to promote stain-invariant representations without relaxing data constraints. Extensive experiments on Camelyon17 and our new MvMidog-Fed benchmark show FedStain yields consistent improvements, outperforming state-of-the-art FedL, DG, and FedDG baselines by up to +3.9% absolute accuracy. To our knowledge, FedStain is the first FedDG approach to explicitly model higher-order stain statistics, enabling robust cross-institutional deployment in computational pathology.

---


### 177. [Privacy Auditing with Zero (0) Training Run](https://arxiv.org/abs/2605.14591)

**<font color=#1a73e8>作者：</font>** Tudor Cebere, Mathieu Even, Linus Bleistein 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy auditing provides empirical lower bounds on the differential privacy parameters of learning algorithms. Existing methods, however, require interventional access to the training pipeline, either to retrain multiple times or to randomize data inclusion. This is often infeasible for large deployed systems such as foundation models. We introduce Zero-Run privacy auditing, a post-hoc framework for auditing models using two fixed datasets: examples known to be training-set members and examples known to be non-members. In this observational regime, membership is no longer randomized; instead, member and non-member data often differ in distribution, so membership inference scores may reflect a distribution shift rather than algorithmic leakage. Drawing on ideas from causal inference, we formalize this confounding effect and propose two complementary corrections that yield valid privacy audits. Our first approach models the combined effect of distribution shift and algorithmic leakage as an adaptive composition, producing conservative global corrections. Our second approach conditions on observed data and adjusts pointwise membership guesses, yielding sharper instance-dependent bounds. Experiments on synthetic data and large-scale models show that Zero-Run auditing enables practical privacy evaluation when retraining or controlled data insertion is infeasible.

---


### 178. [VMU-Diff: A Coarse-to-fine Multi-source Data Fusion Framework for Precipitation Nowcasting](https://arxiv.org/abs/2605.14597)

**<font color=#1a73e8>作者：</font>** Chunlei Shi, Hao Li, Yufeng Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Precipitation nowcasting is a vital spatio-temporal prediction task for meteorological applications but faces challenges due to the chaotic property of precipitation systems. Existing methods predominantly rely on single-source radar data to build either deterministic or probabilistic models for extrapolation. However, the single deterministic model suffers from blurring due to MSE convergence. The single probabilistic model, typically represented by diffusion models, can generate fine details but suffers from spurious artifacts that compromise accuracy and computational inefficiency. To address these challenges, this paper proposes a novel coarse-to-fine Vision Mamba Unet and residual Diffusion (VMU-Diff) based precipitation nowcasting framework. It realizes precipitation nowcasting through a two-stage process, i.e., a deterministic model-based coarse stage to predict global motion trends and a probabilistic model-based fine stage to generate fine prediction details. In the coarse prediction stage, rather than single-source radar data, both radar and multi-band satellite data are taken as input. A spatial-temporal attention block and several Vision mamba state-space blocks realize multi-source data fusion, and predict the future echo global dynamics. The fine-grained stage is realized by a spatio-temporal refine generator based on residual conditional diffusion models. It first obtains spatio-temporal residual features based on coarse prediction and ground truth, and further reconstructs the residual via conditional Mamba state-space module. Experiments on Jiangsu SWAN datasets demonstrate the improvements of our method over state-of-the-art methods, particularly in short-term forecasts.

---


### 179. [Fast Rates for Inverse Reinforcement Learning](https://arxiv.org/abs/2605.14599)

**<font color=#1a73e8>作者：</font>** Andreas Schlaginhaufen, Maryam Kamgarpour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We establish novel structural and statistical results for entropy-regularized min-max inverse reinforcement learning (Min-Max-IRL) with linear reward classes in finite-horizon MDPs with Borel state and action spaces. On the structural side, we show that maximum likelihood estimation (MLE) and Min-Max-IRL are equivalent at the population level, and at the empirical level under deterministic dynamics. On the statistical side, exploiting pseudo-self-concordance of the Min-Max-IRL loss, we prove that both the trajectory-level KL divergence and the squared parameter error in the Hessian norm decay at the fast rate $\mathcal{O}(n^{-1})$, where $n$ is the number of expert trajectories. Our guarantees apply under misspecification and require no exploration assumptions. We further extend reward-identifiability results to general Borel spaces and derive novel results on the derivatives of the soft-optimal value function with respect to reward parameters.

---


### 180. [SciPaths: Forecasting Pathways to Scientific Discovery](https://arxiv.org/abs/2605.14600)

**<font color=#1a73e8>作者：</font>** Eric Chamoun, Yizhou Chi, Yulong Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific progress depends on sequences of enabling contributions, yet existing AI4Science benchmarks largely focus on citation prediction, literature retrieval, or idea generation rather than the dependencies that make progress possible. In this paper, we introduce discovery pathway forecasting: given a target scientific contribution and the prior literature available at a specified time, the task is to (1) identify the enabling contributions required to realize it and (2) ground each in prior work when such prior work exists. We present SciPaths, a benchmark of 262 expert-annotated gold pathways and 2,444 silver pathways constructed from machine learning and natural language processing papers, where each pathway records enabling contributions, roles, rationales, and prior-work groundings or unmapped decisions. Evaluating frontier and open-weight language models, we find that the best model reaches only 0.189 F1 under strict semantic matching, with core methodological dependencies hardest to recover. Prior-work grounding improves substantially when gold enabling contributions are provided, showing that decomposition quality is a major bottleneck for end-to-end pathway recovery. SciPaths therefore shifts evaluation toward a missing capability in scientific forecasting: reasoning backward from a target contribution to the enabling scientific building blocks and prior-work dependencies that make it feasible.

---


### 181. [Towards Accurate Single Panoramic 3D Detection: A Semantic Gaussian Centric Approach](https://arxiv.org/abs/2605.14601)

**<font color=#1a73e8>作者：</font>** Kanglin Ning, Yiran Zhao, Wenrui Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional object detection in panoramic imagery is crucial for comprehensive scene understanding, yet accurately mapping 2D features to 3D remains a significant challenge. Prevailing methods often project 2D features onto discrete 3D grids, which break geometric continuity and limit representation efficiency. To overcome this limitation, this paper proposes PanoGSDet, a monocular panoramic 3D detection framework built upon continuous semantic 3D Gaussian representations. The proposed framework comprises a panoramic depth estimation component and a semantic Gaussian component. The panoramic depth estimation component extracts the equirectangular semantic and depth features from the monocular panorama input. The semantic Gaussian component includes a semantic Gaussian lifting module that projects spherical features into 3D semantic Gaussians, a semantic Gaussian optimization module that refines these semantic Gaussians, and a Gaussian guided prediction head that generates 3D bounding boxes from optimized Gaussian representations. Extensive experiments on the Structured3D dataset demonstrate that our method significantly outperforms existing methods.

---


### 182. [One Step to the Side: Why Defenses Against Malicious Finetuning Fail Under Adaptive Adversaries](https://arxiv.org/abs/2605.14605)

**<font color=#1a73e8>作者：</font>** Itay Zloczower, Eyal Lenga, Gilad Gressel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model providers increasingly release open weights or allow users to fine-tune foundation models through APIs. Although these models are safety-aligned before release, their safeguards can often be removed by fine-tuning on harmful data. Recent defenses aim to make models robust to such malicious fine-tuning, but they are largely evaluated only against fixed attacks that do not account for the defense. We show that these robustness claims are incomplete. Surveying 15 recent defenses, we identify several defense mechanisms and show that they share a single weakness: they obscure or misdirect the path to harmful behavior without removing the behavior itself. We then develop a unified adaptive attack that breaks defenses across all defense mechanisms. Our results show that current approaches do not provide robust security; they mainly stop the attacks they were designed against. We hope that our unified adaptive adversary for this domain will help future researchers and practitioners stress-test new defenses before deployment.

---


### 183. [MambaRain: Multi-Scale Mamba-Attention Framework for 0-3 Hour Precipitation Nowcasting](https://arxiv.org/abs/2605.14606)

**<font color=#1a73e8>作者：</font>** Chunlei Shi, Cui Wu, Xiang Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate precipitation nowcasting over extended horizons (0-3 hours) is essential for disaster mitigation and operational decision-making, yet remains a critical challenge in the field. Existing deterministic approaches are predominantly constrained to shorter prediction windows (0-2 hours), exhibiting severe performance degradation beyond 90 minutes owing to their inherent difficulty in capturing long-range spatiotemporal dependencies from radar-derived observations. To address these fundamental limitations, we propose MambaRain, a novel multi-scale encoder-decoder architecture that synergistically integrates Mamba's linear-complexity long-range temporal modeling with self-attention mechanisms for explicit spatial correlation capture. The core innovation lies in a hybrid design paradigm wherein Mamba blocks leverage selective state space mechanisms to model global temporal dynamics across extended sequences with computational efficiency, while self-attention modules explicitly characterize spatial correlations within precipitation fields - a capability inherently absent in Mamba's sequential processing paradigm. This complementary synergy enables comprehensive spatiotemporal representation learning, effectively extending the viable forecasting horizon to 2-3 hours with substantial accuracy improvements. Furthermore, we introduce a spectral loss formulation to mitigate blurring artifacts characteristic of chaotic precipitation systems, thereby preserving fine-scale motion details critical for nowcasting accuracy. Experimental validation demonstrates that MambaRain substantially outperforms existing deterministic methodologies in 0-3 hour nowcasting tasks, with particularly pronounced performance gains in the challenging 2-3 hour prediction range.

---


### 184. [ViMU: Benchmarking Video Metaphorical Understanding](https://arxiv.org/abs/2605.14607)

**<font color=#1a73e8>作者：</font>** Qi Li, Xinchao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Any new medium, once it emerges, is used for more than the transmission of overt content alone. The information it carries typically operates on two levels: one is the content directly presented, while the other is the subtext beneath it-the implicit ideas and intentions the creator seeks to convey through the medium. Likewise, since video technologies became widely adopted, video has served not only as a powerful tool for recording and communicating visual information, but also as a vehicle for emotions, attitudes, and social meanings that are often difficult to articulate explicitly. Thus, the true meaning of many videos does not reside solely in what is shown on screen; it is often embedded in context, style of expression, and the viewer's social experience. Some forms of such video subtext are humorous, while others carry irony, mockery, or criticism. These implicit meanings can also be interpreted very differently across cultural backgrounds and social groups. However, most existing video understanding models still focus primarily on literal visual comprehension, such as recognizing objects, actions, or temporal relations, and lack a systematic ability to understand the metaphorical, ironic, and social meanings embedded in videos. To bridge this gap, we introduce ViMU, the first benchmark designed to systematically evaluate the subtext understanding capabilities of frontier models in videos. ViMU assesses whether video understanding models can go beyond literal perception to infer implicit meaning while grounding their interpretations in multimodal evidence and answering both open-ended and multiple-choice questions. Importantly, all questions are designed to be hint-free, ensuring that no key evidence is disclosed to models before answering.

---


### 185. [Deep Image Segmentation via Discriminant Feature Learning](https://arxiv.org/abs/2605.14609)

**<font color=#1a73e8>作者：</font>** Adam Dawid Sztamborski, Raül Pérez-Gonzalo, Antonio Agudo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate image segmentation remains challenging, particularly in generating sharp, confident boundaries. While modern architectures have advanced the field, many of them still rely on standard loss functions like Cross-Entropy and Dice, which often neglect the discriminative structure of learned features, leading to inaccurate boundaries. This work introduces Deep Discriminant Analysis (DDA), a differentiable, architecture-agnostic loss function that embeds classical discriminant principles for network training. DDA explicitly maximizes between-class variance while minimizing within-class one, promoting compact and separable feature distributions without increasing inference cost. Evaluations on the DIS5K benchmark demonstrate that DDA consistently improves segmentation accuracy, boundary sharpness, and model confidence across various architectures. Our results show that integrating discriminant analysis offers a simple, effective path for building more robust segmentation models.

---


### 186. [CalibAnyView: Beyond Single-View Camera Calibration in the Wild](https://arxiv.org/abs/2605.14615)

**<font color=#1a73e8>作者：</font>** Boying Li, Cheng Zhang, Weirong Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera calibration is a fundamental prerequisite for reliable geometric perception, yet classical approaches rely on controlled acquisition setups that are impractical for in-the-wild imagery. Recent learning-based methods have shown promising results for single-view calibration, but inherently neglect geometric consistency across multiple views. We introduce CalibAnyView, a unified formulation that supports an arbitrary number of input views ($N \geq 1$) by explicitly modeling cross-view geometric consistency. To facilitate this, we construct a large-scale multi-view video dataset covering diverse real-world scenarios, including multiple camera models, dynamic scenes, realistic motion trajectories, and heterogeneous lens distortions. Building on this dataset, we develop a multi-view transformer that predicts dense perspective fields, which are further integrated into a geometric optimization framework to jointly estimate camera intrinsics and gravity direction. Extensive experiments demonstrate that CalibAnyView consistently outperforms state-of-the-art methods, achieves strong robustness under single-view settings, and further improves with multi-view inference, providing a reliable foundation for downstream tasks such as 3D reconstruction and robotic perception in the wild.

---


### 187. [SliceGraph: Mapping Process Isomers in Multi-Run Chain-of-Thought Reasoning](https://arxiv.org/abs/2605.14619)

**<font color=#1a73e8>作者：</font>** Kang Chen, Junjie Nian, Yixin Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-run chain-of-thought reasoning is usually collapsed to final-answer aggregates, which discard howsampled trajectories share, split, and rejoin through intermediate computation. We propose SliceGraph, a post-hoc problem-model-cell graph built by mutual-kNN over sparse activation-key Jaccard similarity between CoT slices, and treat it as a measurement object for process geometry rather than as a decoding program. Across sampled CoT ensembles from three primary 4B/8B models on math and science benchmarks, blinded annotation supports SliceGraph biconnected components as shared reasoning-state units and process families as within-family strategy-coherent route units. In 85.5% of 954 problem-model cells, correct CoTs sharing the same normalized answer split into multiple process families; among cells with at least two such runs, 76.6% of run pairs are cross-family on average. We call such same-answer, family-divergent correct trajectories process isomers. A label-seeded reward field provides a separate value-landscape layer: success-associated regions often split into disconnected high-value cores, and route families specialize over these core footprints rather than merely duplicating one another. A typed-state transition analysis further shows that process families navigate the same atlas with distinct transition kernels under matched null controls. Representation ablations, a cross-architecture replication, and two cross-scale replications support the robustness of the route-family scaffold, showing that final-answer aggregation overlooks this structured multi-route process geometry.

---


### 188. [An Amortized Efficiency Threshold for Comparing Neural and Heuristic Solvers in Combinatorial Optimization](https://arxiv.org/abs/2605.14624)

**<font color=#1a73e8>作者：</font>** Sohaib Afifi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A common critique of neural combinatorial-optimization solvers is that they are less energy-efficient than CPU metaheuristics, given the operational energy cost of training them on GPUs. This paper examines the inferential step from "training is expensive" to "neural solvers are net-inefficient", which is where the critique actually goes wrong. Training the network costs a large fixed amount of GPU energy; running the metaheuristic costs a small amount of CPU energy on every instance, repeated as long as the solver is deployed. The two are not commensurable until a deployment volume is fixed. We define the Amortized Efficiency Threshold (AET) as the deployment volume above which a neural solver breaks even with a heuristic baseline in total energy or carbon, under an explicit constraint on solution quality. We show that the cumulative-energy ratio between the two solvers tends to a constant strictly below one whenever the network wins per-instance, and that this limit does not depend on how the training cost was measured. An embodied-carbon term amortizes hardware fabrication symmetrically on both sides. We instantiate the framework on the Multi-Task VRP (MTVRP) environment at n=20 customers across 19 problem variants and five training seeds, with HGS via PyVRP as the heuristic baseline. The measured crossover sits near $1.58 \times 10^5$ deployed instances; the per-instance ratio is 0.41, reflecting the moderate size of the instances tested. The contribution is the framework, the open instrumentation, and the measurement protocol; structural convergence of the ratio at larger problem sizes is left to future empirical work.

---


### 189. [UniTriGen: Unified Triplet Generation of Aligned Visible-Infrared-Label for Few-Shot RGB-T Semantic Segmentation](https://arxiv.org/abs/2605.14626)

**<font color=#1a73e8>作者：</font>** Ping Zhou, Haoyu Wang, Mengmeng Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> RGB-T semantic segmentation requires strictly aligned VIS-IR-Label triplets; however, such aligned triplet data are often scarce in real-world scenarios. Existing generative augmentation methods usually adopt cascaded generation paradigms, decomposing joint triplet generation into local conditional processes. As a result, consistency among VIS, IR, and Label in spatial structure, semantic content, and cross-modal details cannot be reliably maintained. To address this issue, we propose UniTriGen, a unified triplet generation framework that directly generates spatially aligned, semantically consistent, and modality complementary VIS-IR-Label triplets under the guidance of text prompts. UniTriGen first introduces a unified triplet generation mechanism, where VIS, IR, and Label are jointly encoded into a shared latent space and modeled with a diffusion process to enforce global cross-modal consistency. Lightweight modality-specific residual adapters are further integrated into this mechanism to accommodate modality-specific imaging characteristics and output formats. To mitigate generation bias caused by imbalanced scene and class distributions in limited paired triplets, UniTriGen also employs a scene-balanced and class-aware few-shot sampling strategy, which induces a more balanced sampling distribution and enhances the scene and class diversity of generated triplets. Experiments show that UniTriGen generates high-quality aligned triplets from limited real paired data, thereby achieving consistent performance improvements across various RGB-T semantic segmentation models.

---


### 190. [SmartWalkCoach: An AI Companion for End-to-End Walking Guidance, Motivation, and Reflection](https://arxiv.org/abs/2605.14628)

**<font color=#1a73e8>作者：</font>** Xianzhe Zhang, Mingxuan Hu, Bufan Xue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present SmartWalkCoach, a mobile AI companion that supports the full walking journey: from pre-walk planning to in-walk guidance through to post-walk reflection. Addressing a gap between map navigation and motivational coaching, SmartWalkCoach orchestrates three lightweight agents: (1) GeographyAgent for conversational route curation from nearby points of interest and user preferences while delegating pathfinding to map APIs; (2) AccompanyAgent for context-aware, just-in-time prompts that blend informational cues with relational encouragement; and (3) SummaryAgent for concise reflection and next-step planning. This end-to-end, tool-using design aims to lower cognitive load in planning and sustain engagement and motivation during walking through delivering dynamic, cadence-aware interventions. We conducted an in-the-wild, two-period AB/BA crossover study (N=12), where each participant completed two comparable walks with counterbalanced conditions: Information-only versus Information+Motivation. Linear mixed models show that adding motivational, companion-like dialogue significantly improved outcomes: participants reported higher positive feelings and better user experience, with no evidence of carryover. Thematic analysis surfaced two design imperatives for mobile companions: supportive, relational expression and context-aware timing (e.g., avoiding high-load moments, intervening at fatigue/milestones). Our contributions are: (i) an end-to-end, tool-using agent architecture for everyday walking that reduces cognitive load during planning and accompaniment; (ii) a controlled field evaluation linking context-aware motivation to affect and UX gains; and (iii) actionable design guidance on expression, timing, and frequency for mHealth this http URL outline limitations and paths toward multimodal, voice-first companions, with adaptive personalization mechanisms.

---


### 191. [Action-Inspired Generative Models](https://arxiv.org/abs/2605.14631)

**<font color=#1a73e8>作者：</font>** Eshwar R. A., Debnath Pal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Action-Inspired Generative Models (AGMs), a dual-network generative framework motivated by the observation that existing bridge-matching methods assign uniform regression weight to every stochastic transition in the transport landscape, regardless of whether a given bridge sample lies along a structurally coherent trajectory or a degenerate one. We address this by introducing a lightweight learned scalar potential $V_\phi$ that scores bridge samples online and modulates the drift objective via importance weights derived through a stop-gradient barrier -- preventing adversarial feedback between the two networks whilst preserving $V_\phi$'s guiding signal. Crucially, $V_\phi$ comprises only $\sim$1.4% of the primary drift network's parameter count, adds no overhead to the inference graph, and requires no iterative half-bridge fitting or auxiliary stochastic differential equation (SDE) solvers: it is a plug-and-play enhancement to any bridge-matching training loop. At inference, $V_\phi$ is discarded entirely, leaving standard Euler-Maruyama integration of the exponential moving average (EMA) drift. We demonstrate that selectively penalising uninformative transport paths through the learned potential yields consistent improvements in generation quality across fidelity and coverage metrics.

---


### 192. [DRL-STAF: A Deep Reinforcement Learning Framework for State-Aware Forecasting of Complex Multivariate Hidden Markov Processes](https://arxiv.org/abs/2605.14632)

**<font color=#1a73e8>作者：</font>** Manrui Jiang, Jingru Huang, Yong Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting multivariate hidden Markov processes is challenging due to nonlinear and nonstationary observations, latent state transitions, and cross-sequence dependencies. While deep learning methods achieve strong predictive accuracy, they typically lack explicit state modeling, whereas Hidden Markov Models (HMMs) provide interpretable latent states but struggle with complex nonlinear emissions and scalability. To address these limitations, we propose DRL-STAF, a Deep Reinforcement Learning based STate-Aware Forecasting framework that jointly predicts next-step observations and estimates the corresponding hidden states for complex multivariate hidden Markov processes. Specifically, DRL-STAF models complex nonlinear emissions using deep neural networks and estimates discrete hidden states using reinforcement learning, reducing the reliance on predefined transition structures and enabling flexible adaptation to diverse temporal dynamics. In particular, DRL-STAF mitigates the state-space explosion encountered by typical multivariate HMM-based methods. Extensive experiments demonstrate that DRL-STAF outperforms HMM variants, standalone deep learning models, and existing DL-HMM hybrids in most cases, while also providing reliable hidden-state estimates.

---


### 193. [Capacitive Touchscreens at Risk: A Practical Side-Channel Attack on Smartphones via Electromagnetic Emanations](https://arxiv.org/abs/2605.14633)

**<font color=#1a73e8>作者：</font>** Yukun Cheng, Changhai Ou, Shiyu Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Capacitive touchscreens in modern smartphones introduce severe side-channel vulnerabilities. However, existing attacks often require restrictive conditions or invasive measurements. This paper presents TESLA, a novel, contactless electromagnetic (EM) side-channel attack that exploits inherent EM emanations during touchscreen scanning. We demonstrate that these emanations encode the spatiotemporal evolution of touch interactions, forming a unified leakage basis. By secretly placing an EM probe near the victim's device, TESLA enables attackers to extract highly sensitive information, including screen-unlocking PIN codes, keyboard inputs, interacting application categories, and continuous handwriting trajectories. Compared to existing attacks, TESLA offers a broader range of attack targets, more efficient sample acquisition, and operations in practical attack scenarios. Extensive evaluations on popular commercial smartphones, specifically the iPhone X, Xiaomi 10 Pro, Samsung S10, and Huawei Mate 30 Pro, validate the effectiveness of TESLA. It achieves remarkable inference accuracy in diverse settings such as private meeting rooms and public libraries, with success rates of 99.3% for PIN code recognition, 97.6% for keyboard input reconstruction, and 95.0% for application inference, respectively. Simultaneously, it attains a 76.8% character recognition accuracy and a high geometric similarity (Jaccard index of 0.74) for 2D handwriting trajectory reconstruction.

---


### 194. [How to Evaluate and Refine your CAM](https://arxiv.org/abs/2605.14641)

**<font color=#1a73e8>作者：</font>** Luca Domeniconi, Alessandra Stramiglio, Michele Lombardi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Class attribution maps (CAMs) provide local explanations for the decisions of convolutional neural networks. While widely used in practice, the evaluation of CAMs remains challenging due to the lack of ground-truth explanations, making it difficult to evaluate the soundness of existing metrics. Independently, most commonly used CAM methods produce low-resolution attribution maps, which limits their usefulness for detailed interpretability.
To address the evaluation challenge, we introduce a synthetic dataset with ground-truth attributions that enables a rigorous comparison of CAM evaluation metrics. Using this dataset, we analyze existing metrics and propose ARCC, a new composite metric that more reliably identifies faithful explanations. To address the low resolution issue, we introduce RefineCAM, a method that produces high-resolution attribution maps by aggregating CAMs across multiple network layers. Our results show that RefineCAM consistently outperforms existing methods according to the proposed evaluation.

---


### 195. [Unbiased and Second-Order-Free Training for High-Dimensional PDEs](https://arxiv.org/abs/2605.14643)

**<font color=#1a73e8>作者：</font>** Jaemin Seo, Surin Lee, Jae Yong Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning methods based on backward stochastic differential equations (BSDEs) have emerged as competitive alternatives to physics-informed neural networks (PINNs) for solving high-dimensional partial differential equations (PDEs). By leveraging probabilistic representations, BSDE approaches can avoid the curse of dimensionality and often admit second-order-free training objectives that do not require explicit Hessian evaluations. It has recently been established that the commonly used Euler-Maruyama (EM) time discretization induces an intrinsic bias in BSDE training losses. While high-order schemes such as Heun can fully eliminate this bias, such schemes re-introduce second-order spatial derivatives and incur substantial computational overhead. In this work, we provide a principled analysis of EM-induced loss bias and propose an unbiased, second-order-free training framework that preserves the computational advantages of BSDE methods. Our code is available at this https URL.

---


### 196. [Vision-Based Water Level and Flow Estimation](https://arxiv.org/abs/2605.14645)

**<font color=#1a73e8>作者：</font>** ZhiXin Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the rapid evolution of computer vision, vision-based methodologies for water level and river surface velocity estimation have reached significant maturity. Compared to traditional sensing, these techniques offer superior interpretability, automated data archiving, and enhanced system robustness. However, challenges such as environmental sensitivity, limited precision, and complex site calibration persist. This work proposes an integrated framework that synergizes state-of-the-art (SOTA) vision models with statistical modeling. By leveraging physical priors and robust filtering strategies, we improve the accuracy of water level detection and flow estimation. Code will be available at this https URL

---


### 197. [TERRA-CD: Multi-Temporal Framework for Multi-class and Semantic Change Detection](https://arxiv.org/abs/2605.14651)

**<font color=#1a73e8>作者：</font>** Omkar Oak, Rukmini Nazre, Rujuta Budke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Urban vegetation monitoring plays a vital role in understanding environmental changes, yet comprehensive datasets for this purpose remain limited. To address this gap, we present the Temporal Remote-sensing Repository for Analyzing Change Detection (TERRA-CD), a benchmark dataset comprising 5,221 Sentinel-2 image pairs from 2019 and 2024, covering 232 cities across the USA and Europe. The dataset features three distinct annotation schemes: 4-class land cover mapping masks, 3-class vegetation change masks, and 13-class semantic change masks capturing all possible land cover transitions. Using various deep learning approaches including Siamese networks, STANet variants, Bi-SRNet, Changemask, Post-Classification Comparison, and HRSCD strategies, we evaluated the dataset's effectiveness for both vegetation Multi-class Change Detection as well as Semantic Change Detection. The proposed dataset and methods are available at this https URL.

---


### 198. [Beyond Instance-Level Self-Supervision in 3D Multi-Modal Medical Imaging](https://arxiv.org/abs/2605.14654)

**<font color=#1a73e8>作者：</font>** Tan Pan, Shuhao Mei, Yixuan Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised pre-training methods in medical imaging typically treat each individual as an isolated instance, learning representations through augmentation-based objectives or masked reconstruction. They often do not adequately capitalize on a key characteristic of physiological features: anatomical structures maintain consistent spatial relationships across individuals (instances), such as the thalamus being medial to the basal ganglia, regardless of variations in brain size, shape, or pathology. We propose leveraging this cross-instance topological consistency as a supervisory signal. The challenge arises from the inherent variability in medical imaging, which can differ significantly across instances and modalities. To tackle this, we focus on two alignment regimes. (i) Intra-instance: with pixel-level correspondences available, a cross-modal triplet objective explicitly preserves local neighborhood topology. (ii) Inter-instance: without such supervision, we derive pseudo-correspondences to control partial neighborhood alignment and prevent topology collapse across modalities. We validate our approach across 7 downstream multi-modal tasks, achieving average improvements of 1.1% and 5.94% in segmentation and classification tasks, respectively, and demonstrating significantly better robustness when modalities are missing at test time.

---


### 199. [Slower Generalization, Faster Memorization: A Sweet Spot in Algorithmic Learning](https://arxiv.org/abs/2605.14659)

**<font color=#1a73e8>作者：</font>** Shin So, Kyelim Lee, Albert No  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Critical-data-size accounts of grokking suggest a natural post-threshold intuition: once training data is sufficient to identify the underlying rule, additional data should accelerate validation convergence. We show that this intuition can fail in a controlled structured-output task. In Needleman--Wunsch (NW) matrix generation, small Transformers reach high validation exact-match accuracy fastest at an intermediate dataset size, not at the largest one. Past this dataset-size sweet spot, generalization remains achievable but requires more gradient updates. Conversely, in the regime where partial validation competence first appears, larger datasets can require fewer updates to reach high training accuracy, suggesting that emerging rule structure can accelerate fitting beyond example-wise memorization. A multiplication baseline does not show the same post-threshold slowdown. These results separate the critical data size for the onset of generalization from the dataset size that optimizes update-based convergence, and identify structured-output tasks where learning the rule and completing exact-fitting can diverge.

---


### 200. [MindGap: A Conversational AI Framework for Upstream Neuroplastic Intervention in Post-Traumatic Stress Disorder](https://arxiv.org/abs/2605.14660)

**<font color=#1a73e8>作者：</font>** Eranga Bandara, Ross Gore, Asanga Gunaratna 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-Traumatic Stress Disorder (PTSD) is fundamentally a neuroplastic problem traumatic contact events encode over-reactive neural pathways through Hebbian long-term potentiation, producing hair-triggered amygdala-HPA stress cascades that fire before conscious awareness can intercept them. Existing therapeutic approaches, prolonged exposure, EMDR, cognitive behavioural therapy, operate predominantly downstream of the reactive cascade, teaching patients to tolerate or reframe distress after it has arisen. While clinically valuable, these suppression-based approaches do not produce the upstream pathway dissolution that constitutes lasting structural neural reorganisation. This paper proposes MindGap, a privacy-preserving on-device conversational AI framework that delivers structured neuroplastic rehabilitation for PTSD through the practice of dependent origination, a Buddhist psychological framework that identifies the precise moment between the pre-cognitive affective signal and the reactive elaboration that follows as the site of therapeutic intervention. MindGap guides patients through three progressive layers of observation at this feeling tone gap: noticing the bare affective signal before reactive elaboration, recognising it as self-arising rather than caused by the stimulus, and recognising the conditioned implicit belief beneath the feeling. Each layer corresponds to progressively deeper prefrontal regulatory engagement and progressively deeper long-term depression-mediated weakening of the reactive pathway, producing genuine upstream dissolution rather than downstream suppression. Running entirely on-device with no data egress, MindGap delivers daily calibrated exposure sessions through a fine-tuned lightweight large language model, making it deployable in sensitive clinical and military contexts where cloud-based solutions are not permitted.

---


> [!TIP]
> 当前位于：**151-200**（第 4/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-337](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
