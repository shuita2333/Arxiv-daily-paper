# 📦 其他研究 | 2026年06月17日

> 本类共 **509** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

---

### 351. [Learned Image Compression for Vision-Language-Action Models](https://arxiv.org/abs/2606.16253)

**<font color=#1a73e8>作者：</font>** Hyeonjun Kim, Jegwang Ryu, Sangbeom Ha 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models increasingly rely on high-frequency multi-camera observations, making visual communication a major bottleneck for real-time robotic control in bandwidth-constrained or distributed deployment settings. Existing image and video codecs, however, are designed to preserve generic visual fidelity rather than the control performance of downstream VLA policies. In this work, we introduce SPARC (SPatially Adaptive Rate Control), a learned image compression framework tailored for VLA-driven robots. Our key observation is that the importance of visual information varies substantially across both camera views and spatial regions within an image. Based on this observation, SPARC employs a lightweight temporal mask selector that adaptively allocates bitrate over latent representations according to task relevance while leveraging temporal context. We further introduce a tilted rate loss that stabilizes training by reducing the tendency of entropy-based objectives to over-suppress rare yet task-critical visual patterns. Experiments on diverse robotic benchmarks, including RoboCasa365, VLABench, and LIBERO, show that SPARC consistently achieves stronger control performance than conventional image/video codecs and recent learned compression methods under the same bitrate budget. We additionally demonstrate real-world deployment benefits in remote-control settings, where our method substantially improves the bitrate-success tradeoff.

---


### 352. [KeepLoRA++: Continual Learning with Layer-Scaled Residual Gradient Adaptation](https://arxiv.org/abs/2606.16256)

**<font color=#1a73e8>作者：</font>** Mao-Lin Luo, Yi-Lin Zhang, Zi-Hao Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual learning for pre-trained vision-language models requires balancing three competing objectives: retaining pre-trained knowledge, preserving knowledge from a sequence of learned tasks, and maintaining the plasticity to acquire new knowledge. This paper presents KeepLoRA++, balancing these objectives through a unified dual-dimensional knowledge retention mechanism. We analyze knowledge distribution of Transformer architecture from both inter-layer and intra-layer perspectives. The inter-layer perspective examines how retention is distributed across layers, while the intra-layer perspective focuses on the parameter space within each layer. Our analysis reveals a structural property: general transferable knowledge is mainly encoded in the shallow layers and the principal subspace of the parameters, while task-specific adaptations are localized in the deep layers and the residual subspace. Motivated by this insight, KeepLoRA++ introduces a layer-scaled residual gradient adaptation method. New tasks are learned by restricting LoRA parameter updates to the residual subspace, combined with a shallow-to-deep layer scaling, to prevent interference with previously acquired capabilities. Specifically, the gradient of a new task is projected onto a subspace orthogonal to both the principal subspace of the pre-trained model and the dominant directions of previous task features, while simultaneously assigning smaller update magnitudes to shallow layers and larger ones to deeper layers. Our theoretical analysis and empirical evaluations confirm that KeepLoRA++ successfully balances these three competing objectives, consistently outperforming representative baselines across image classification, visual question answering, and video understanding tasks.

---


### 353. [Variance Reduction for Non-Log-Concave Sampling with Applications to Inverse Problems](https://arxiv.org/abs/2606.16257)

**<font color=#1a73e8>作者：</font>** M. Berk Sahin, Ahmet Ege Tanriverdi, Behzad Sharif 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from high-dimensional, non-log-concave distributions with unnormalized densities is a fundamental challenge in machine learning, particularly when the exact gradient of the potential is unavailable and must be approximated via stochastic gradients that exhibit high variance under a fixed budget of gradient computations per iteration. Although variance reduction techniques such as SGD with momentum, STORM, and PAGE have demonstrated improved convergence properties in non-convex optimization, their implications for sampling from non-log-concave distributions remain largely unexplored. In this work, we develop the first unified analysis of these estimators for sampling from non-log-concave distributions. We establish improved non-asymptotic convergence rates in $\varepsilon$-relative Fisher information and, under a Poincaré inequality assumption, in squared total variation distance, and further prove weak convergence to the target distribution. We extend our analysis to solving inverse problems with score-based generative priors. We empirically validate our theory and demonstrate that, under a fixed gradient computations per iteration, variance-reduction techniques consistently improve sample quality in two standard imaging applications.

---


### 354. [Contrastive Learning for Seismic Horizon Tracking with Domain-Specific Priors](https://arxiv.org/abs/2606.16271)

**<font color=#1a73e8>作者：</font>** Alexandre Thouvenot, Lionel Boillot, Vincent Gripon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised 3D seismic horizon tracking faces a key limitation: signal-based propagators provide accurate trace-level alignment but often fail near faults, whereas texture-driven deep models are more robust to discontinuities, typically at the cost of labeled data requirements and reduced trace-level precision. We propose a self-supervised fusion of both paradigms in which signal-derived local horizon correspondences act as domain-specific priors to train a texture-based deep learning model. Specifically, we estimate reliable trace-to-trace flows from reflector slopes and use them to form positive pairs in a contrastive objective, while restricting training to high-confidence neighborhoods, optionally augmented with a fault mask. The objective is not to infer ambiguous correspondences close to discontinuities, but to preserve horizon identity across them. As a result, the network learns voxel-wise embeddings that preserve local signal continuity while enabling horizon propagation beyond discontinuities through similarity search. Experiments on the public F3 dataset and a faulted synthetic dataset achieve lower mean absolute error (MAE) than unsupervised baselines and competitive performance against a semi-supervised method using a single labeled slice.

---


### 355. [RealityBridge: Bridging Editable 3D Gaussian Splatting Driving Simulations and Real-World Videos](https://arxiv.org/abs/2606.16278)

**<font color=#1a73e8>作者：</font>** Zhenhua Wu, Yun Pang, Mingkun Chang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tail hazardous scenarios are essential for safety-oriented autonomous driving, yet they are difficult to collect and reproduce at scale. Editable 3D Gaussian Splatting (3DGS) simulation offers a promising alternative by reconstructing real driving scenes and supporting controllable scene editing. However, edited 3DGS-rendered videos still suffer from a significant Sim-to-Real gap, including rendering artifacts, degraded foreground assets, inconsistent illumination, and temporal flickering. Existing restoration and video generation methods are insufficient for this task, as they often fail to jointly repair 3DGS-specific artifacts, improve visual realism, and ensure temporal consistency. To fill this gap, we propose RealityBridge, a structure-preserving and asset-aware Sim-to-Real framework for edited 3DGS driving videos. RealityBridge uses multimodal controls, including rendered videos, foreground masks, edge maps, and semantic masks, together with a lightweight GateNet for adaptive condition allocation across backbone layers. We further construct targeted training data and introduce autoregressive long-video training with reward-guided post-training to improve restoration quality, temporal stability, and hallucination suppression. Extensive experiments on internal and public driving datasets show that RealityBridge outperforms existing methods in artifact removal, illumination harmonization, and long-sequence temporal consistency.

---


### 356. [HiMPO: Hindsight-Informed Memory Policy Optimization for Less-Entangled Credit in Long-Horizon Agents](https://arxiv.org/abs/2606.16285)

**<font color=#1a73e8>作者：</font>** Jiangze Yan, Yi Shen, Wenjing Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents rely on memory mechanisms to compress interaction history, but optimizing memory writing faces a distinct credit assignment challenge: a memory update may be rewarded or penalized due to downstream tool failures, noisy observations, or reasoning errors rather than its own contribution. This causally entangled credit can lead agents to discard useful evidence or preserve irrelevant information. We propose HiMPO, a Hindsight-Informed Memory Policy Optimization framework for assigning less-entangled credit to memory-writing actions in long-horizon agents. HiMPO first estimates the local utility of a memory update by comparing the task-relevant information recoverable from the previous and updated memories under the same pre-write state. It then uses hindsight relevance as a bounded retrospective filter that attenuates memory credit when local utility is not supported by the target outcome. The resulting memory-specific advantage is applied only to memory tokens, while trajectory-level rewards optimize the rest of the agent behavior. Across judge-based open-domain tasks and objective compressive-memory QA, HiMPO improves over strong memory-based and RL-based baselines while preserving compressed-context efficiency. Controlled interventions further show that HiMPO reduces blame leakage from tool-induced errors and improves attribution fidelity of memory updates.

---


### 357. [An affordable hardware-aware neural architecture search for deploying convolutional neural networks on ultra-low-power computing platforms](https://arxiv.org/abs/2606.16290)

**<font color=#1a73e8>作者：</font>** Andrea Mattia Garavagno, Edoardo Ragusa, Antonio Frisoli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hardware-aware neural architecture search (HW-NAS) allows the integration of Convolutional Neural Networks (CNNs) in microcontrollers devices by automatically designing neural architectures that can fit prearranged hardware constraints. However, state-of-the-art HW-NAS target high-performance microcontrollers, whose power consumption does not meet sensing nodes requirements. This work presents a HW-NAS generating tiny CNNs that can run on ultra-low-power microcontrollers, featuring a lightweight search procedure enabling its execution even on embedded devices. Empirical results on three well-known benchmarks for tiny computer vision proved that the proposed HW-NAS was able to generate tiny CNNs while preserving state-of-the-art classification accuracy.

---


### 358. [Sex-based Network-Specific Differences in Connectomes: A Krakencoder-Based Analysis](https://arxiv.org/abs/2606.16294)

**<font color=#1a73e8>作者：</font>** Vibhashree S H, Debanjali Bhattacharya, Vamshi Krishna Kancharla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This study examines how deficiencies in one brain connectome modality propagate to the other, using the Krakencoder as a simulation framework. Structural and functional connectomes from 702 healthy participants in the Human Connectome Project were analyzed, with the impact of each of the Yeo-7 functional networks assessed separately. Seven scenarios were considered, each involving the removal of a single network while the remaining networks were preserved. The resulting perturbations in cross-modal predictions were quantified using three complementary metrics: KL divergence on eigenvalue spectra, Frobenius norm, and Wasserstein distance. In addition, the persistence of sex-specific information within the predicted connectomes was evaluated. Across all metrics and both prediction directions, the Default Mode Network produced the largest perturbations, whereas the Somatomotor network yielded the smallest. Sex differences in network-level perturbation signatures were subtle, with the best result being an accuracy of 66.09% from connectomes predicted under network-removal conditions. In contrast, connectomes predicted from intact inputs achieved substantially higher sex classification accuracy, reaching up to 84.76%. These findings confirm that full predicted connectomes retain considerably more sex-discriminative information than perturbation-derived signatures alone.

---


### 359. [DDTNet: Degradation Disentanglement and Transfer Network for Test-Time All-in-One De-weathering Adaptation](https://arxiv.org/abs/2606.16298)

**<font color=#1a73e8>作者：</font>** Kuan-Hung Lin, Fu-Jen Tsai, Yan-Tsung Peng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-in-one adverse weather image restoration aims to remove multiple degradations, such as rain, haze, and snow, using a single unified model. Despite their broad applicability, existing methods typically compromise performance, delivering balanced but suboptimal results for individual degradation types. This issue becomes more pronounced when a domain gap exists between training and testing data. Motivated by the observation that modeling degradation patterns is more feasible than recovering clean content, we propose the Degradation Disentanglement and Transfer Network (DDTNet), which focuses specifically on degradation transfer. By disentangling degradation patterns from target-domain degraded images and transferring them to source domain clean images, DDTNet generates domain-adaptive paired training data. These pairs are then used to fine-tune restoration models, significantly enhancing their adaptability across diverse weather conditions and domains. The core of DDTNet is the Degradation Disentanglement Module (DDM), which comprises Degradation Coupled Attention (DCA) to capture both general and weather-specific features, thereby enabling effective disentanglement and transfer of degradation patterns. Experimental results demonstrate that DDTNet significantly and consistently improves existing all-in-one models across real-world deraining, desnowing, and dehazing datasets.

---


### 360. [One-Step Generalization Ratio Guided Optimization for Domain Generalization](https://arxiv.org/abs/2606.16301)

**<font color=#1a73e8>作者：</font>** Sumin Cho, Dongwon Kim, Kwangsu Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain Generalization (DG) aims to train models that generalize to unseen target domains but often overfit to domain-specific features, known as undesired correlations. Gradient-based DG methods typically guide gradients in a dominant direction but often inadvertently reinforce spurious correlations. Recent work has employed dropout to regularize overconfident parameters, but has not explicitly adjusted gradient alignment or ensured balanced parameter updates. We propose GENIE (Generalization-ENhancing Iterative Equalizer), a novel optimizer that leverages the One-Step Generalization Ratio (OSGR) to quantify each parameter's contribution to loss reduction and assess gradient alignment. By dynamically equalizing OSGR via a preconditioning factor, GENIE prevents a small subset of parameters from dominating optimization, thereby promoting domain-invariant feature learning. Theoretically, GENIE balances convergence contribution and gradient alignment among parameters, achieving higher OSGR while retaining SGD's convergence rate. Empirically, it outperforms existing optimizers and enhances performance when integrated with various DG and single-DG methods.

---


### 361. [Explainable Flood Segmentation on Sentinel-1 SAR Imagery: A Comparative Study of CNN and Transformer Architectures](https://arxiv.org/abs/2606.16302)

**<font color=#1a73e8>作者：</font>** Arundhuti Banerjee, David Daou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid and accurate flood prediction is essential for disaster response and mitigation planning. Synthetic Aperture Radar (SAR) sensors in satellites are well-suited for this purpose because they operate independently of weather and daylight conditions. Although SAR-based data enable all-weather flood monitoring, distinguishing flooded land from permanent water remains a significant challenge, particularly when flooding is defined strictly as inundated land. This study provides a comprehensive comparison of convolutional neural network (CNN) and vision transformer architectures for multi-class flood segmentation using Sentinel-1 SAR imagery, specifically trained to separate flooded land from permanent water bodies and land. Three state-of-the-art (SOTA)CNN-based models, U-Net, U-Net++, and DeepLabV3 with ResNet-34 backbone, and three SegFormer variants (b0,b1,b2) were evaluated in two benchmark datasets, the ETCI NASA dataset and SenFloods11, using scene-based data splits to ensure a realistic assessment of spatial generalization. The results demonstrate that SegFormer-b2 significantly outperforms the U-Net baseline on the ETCI dataset (higher flood IoU across all 7 test scenes in the Wilcoxon signed-rank test), while after fine-tuning on Sen1Floods11, the advantage narrows to within the range of scene variability and is concentrated in spatially fragmented flood events. The study includes both qualitative and quantitative explainability techniques to visually comprehend model decisions and systematically assess prediction reliability. Qualitative analysis reveals that SegFormer-b2 produces more spatially coherent Grad-CAM activations focused on flood-relevant features, while U-Net generates more informative uncertainty estimates along flood boundaries.

---


### 362. [pFedUL: Layer-Aware Federated Unlearning for Personalized Federated Learning](https://arxiv.org/abs/2606.16304)

**<font color=#1a73e8>作者：</font>** Zhuodong Liu, Xiangyu Li, Zhihao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated unlearning (FU) enables the removal of specific data contributions from federated learning (FL) models to comply with regulations such as the General Data Protection Regulation (GDPR). However, most existing FU methods are designed for the FedAvg paradigm, where all clients share a single global model. In practice, personalized federated learning (pFL) methods such as FedPer, FedRep, Ditto, and FedBN have become widely adopted due to their superior handling of non-IID data. These methods decompose the model into shared global layers and client-specific personalized layers, fundamentally altering the semantics of unlearning, yet this setting has received little attention. We formalize FU under the pFL paradigm, identifying a tension between unlearning completeness on shared layers and personalization preservation for remaining clients. We then propose pFedUL, a layer-aware selective unlearning framework comprising three components: (1) gradient-based layer-wise contribution attribution that separately quantifies the target client's influence on shared and personalized parameters, (2) adaptive selective unlearning that applies differentiated forgetting strategies across layer types, and (3) a lightweight recalibration protocol enabling remaining clients to restore personalization with minimal overhead. We further introduce two new metrics, Personalization Preservation Score (PPS) and Cross-client Fairness Index (CFI), to evaluate pFL-specific unlearning quality. Experiments on CIFAR-10, CIFAR-100, and FEMNIST under varying non-IID settings indicate that pFedUL achieves unlearning effectiveness comparable to full retraining while maintaining an average of 97.3\% personalized accuracy for remaining clients. Compared with six state-of-the-art FU methods adapted to the pFL setting, pFedUL consistently achieves superior personalization preservation.

---


### 363. [QK-Normed MLA: QK normalization without full key caching](https://arxiv.org/abs/2606.16310)

**<font color=#1a73e8>作者：</font>** Yizhou Han, Yao Zhao, Jun Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Query-key (QK) normalization stabilizes attention by controlling the scale of queries and keys before the dot product, but is not immediately compatible with Multi-head Latent Attention (MLA). MLA achieves efficient decoding by caching low-dimensional latent states instead of full keys, whereas post-projection QK RMSNorm appears to require the fully projected key for every cached token. We show this apparent incompatibility is an implementation artifact, not an architectural constraint. RMSNorm decomposes into a static affine weight and a dynamic scalar RMS statistic. The static key-side weight can be absorbed into the MLA query-side projection; the dynamic key statistic reduces to one inverse-RMS scalar per token and KV group. The resulting formulation is exactly equivalent to explicit post-projection QK RMSNorm in exact arithmetic and preserves MLA's latent decode path. In our 400M runs trained for up to 100B tokens, QK-Normed MLA achieves lower training loss and better downstream accuracy than QK clipping, while H800 decode benchmarks show less than 2% latency overhead up to 256k context. These results make QK normalization a practical stabilization option for MLA models without requiring full-key caching.

---


### 364. [Training-free sparse attention based on cumulative energy filtering](https://arxiv.org/abs/2606.16317)

**<font color=#1a73e8>作者：</font>** Chunlu Li, Yixuan Pan, Bai Du 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse attention accelerates Diffusion Transformers (DiTs) for video generation by computing only the important tokens while skipping the rest. The token selection strategy is key to balancing sparsity and accuracy. We formulate the token filtering process as a dual-goal optimization problem: maximizing sparsity and minimizing accuracy degradation. Existing algorithms cannot fulfill both objectives simultaneously. For example, Top-p only considers the accuracy constraint, while Top-k maintains a fixed computational budget but loosens the accuracy constraint.
This paper demonstrates that maintaining a fixed recall rate is sufficient for ensuring accuracy, whereas a fixed threshold is suboptimal for reducing computational cost. Therefore, we propose a dynamic thresholding scheme to improve sparsity while maintaining the same level of accuracy. Furthermore, our algorithm is deeply integrated with Flash Attention (FA), eliminating the need for any additional masking computation overhead. Experimental results on Wan 2.2 validate that, compared to the BLASST algorithm which is also integrated with FA, our dynamic thresholding strategy enhances sparsity from 61.42\% to 82\% with a VBench metric drop of less than 5\%. This results in an approximate 15\% in attention computation and a $1.61\times$ increase in computational efficiency, which is 1.18x higher than that of BLASST.

---


### 365. [Architectural Wisdom: A Framework for Governing Optimization in AI Systems](https://arxiv.org/abs/2606.16319)

**<font color=#1a73e8>作者：</font>** Edward Y. Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern AI systems exhibit structural failures that capability scaling alone does not reliably fix: they optimize under-specified objectives with no architectural mechanism to question whether the objective should be optimized at all. Engagement maximization can amplify harmful pathways; tool-using agents can commit irreversible actions; preference-trained language models can become sycophantic. We argue that this failure is a wisdom problem, not an intelligence problem. We use "wisdom" in a deliberately architectural sense, not as a claim about virtue, consciousness, or moral omniscience. Intelligence accepts a goal and optimizes within it; wisdom interrogates whether the goal should be optimized at all. The two are separable architectural properties. We propose architectural wisdom as a corrigible objective-governance layer above the optimization substrate. The layer makes three structural commitments explicit and nondegenerate before any action: temporal horizon, relational boundary, and irreversibility. It is realized by four components (Structural Utility Transform, Moral Admissibility Interface, Arbitration and Escalation Controller, Value Revision Channel) that compute a six-coordinate wisdom tuple over horizon, relational coverage, irreversibility, admissibility, value revision, and auditability. We motivate the architecture by eight cases drawn from contemporary AI failures, secular wisdom traditions, and hard ethical situations, and defend the distinction against the intelligence-completeness thesis using goal-questioning over goal-taking, Bostrom's orthogonality, structural separation in our exemplar cases, and persistent failure modes despite capability scaling. The framework is the conceptual contract for a larger architecture whose formal specifications and empirical validation are developed in subsequent work.

---


### 366. [PaperJury: Due-Process Review for Bounded LaTeX Revision](https://arxiv.org/abs/2606.16322)

**<font color=#1a73e8>作者：</font>** Yiran Wang, Ruixuan An, Biao Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pre-submission hardening of human-authored LaTeX computer science papers differs from drafting assistance because it requires adversarial whole-paper review, explicit no-fix outcomes, and bounded artifact-safe revision. Existing writing assistants, critique generators, and judge-centered loops lack durable issue identity across rounds, deterministic routing from critique to adjudication, and manuscript control that can reject invalid concerns or defer author-dependent ones. We present PaperJury, a closed-loop review-verdict-revise-verify system built on a deterministic-versus-semantic split: deterministic orchestration manages decomposition, a frozen claim spine, a durable ledger, routing, stopping, and exact-once patch application, while semantic agents are limited to bounded review, judgment, and repair. PaperJury combines bounded holistic review, contestability-based routing, a due-process trial, and risk-proportional guard chains for anchor-bounded edits, yielding terminal outcomes of invalid-drop, valid-fixable, and author-required. In a two-arm expert-review evaluation on held-out Vision, natural language processing, and machine learning papers against four baselines, we assess issue quality, verdict and routing quality, edit safety, convergence behavior, and cost, supporting the thesis that load-bearing safety and completion logic should reside in deterministic orchestration rather than model discretion. PaperJury is available at this https URL.

---


### 367. [HAFMat: Hybrid Priors Guided Adaptive Fusion for Single-Image Human Material Estimation](https://arxiv.org/abs/2606.16323)

**<font color=#1a73e8>作者：</font>** Yu Jiang, Jiahao Xia, Jiongming Qin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physically based rendering (PBR) material estimation is a fundamental appearance decomposition task with broad applications in virtual content creation, relighting, and digital human rendering. However, estimating PBR materials from a single human image remains highly ill-posed, since illumination, geometry, and reflectance are heavily entangled in the observed appearance. To mitigate this ambiguity, we propose HAFMat, a hybrid-prior-guided framework for single-image human material estimation. Our method introduces guidance maps that encode complementary cues, including appearance, body geometry, structure, and prior material predictions from pre-trained models. A key observation is that these guidance cues are heterogeneous: some cues mainly provide texture-level constraints, while others convey higher-level semantic information. To exploit this property, we design a Multi-layer Adaptive Feature Fusion Mechanism, which adaptively fuses guidance features with decoder features at different stages. This design enables texture-dominant and semantic-dominant cues to guide material decoding at appropriate levels, leading to more accurate and physically plausible material estimation. Extensive experiments on both synthetic and real data demonstrate that our method achieves state-of-the-art performance in material estimation and downstream relighting.

---


### 368. [Attention-Based Prototype Calibration for Multi-Rater Few-Shot Medical Image Segmentation](https://arxiv.org/abs/2606.16325)

**<font color=#1a73e8>作者：</font>** Truong Vu, Minh Khoi Ho, Yutong Xie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot medical image segmentation methods typically assume a single ground-truth annotation, overlooking systematic variability across expert raters commonly observed in clinical datasets. We propose an attention-based prototype calibration framework for few-shot multi-rater segmentation that models rater-specific deviations from a consensus representation in prototype space. A lightweight yet principled attention operator directly refines rater prototypes without modifying the backbone feature extractor, making the approach fully compatible with existing prototype-based few-shot segmentation methods. This design preserves semantic consistency while enabling personalized segmentation outputs with minimal computational overhead. Experiments on multi-rater medical imaging datasets demonstrate consistent improvements over baseline prototype approaches, highlighting the effectiveness of structured prototype calibration for modeling annotation variability. Our code is available at this https URL.

---


### 369. [Exploiting Search in Symbolic Numeric Planning with Patterns](https://arxiv.org/abs/2606.16329)

**<font color=#1a73e8>作者：</font>** Matteo Cardellini, Enrico Giunchiglia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a procedure for numeric planning based on Symbolic Pattern Planning (SPP). Given a numeric planning problem $\Pi$, a pattern $\prec$ is a sequence of actions used to define a formula encoding the subsequences of $\prec$ executable from a starting state $S$. Cardellini, Giunchiglia, and Maratea (2024a) follow the Planning as Satisfiability approach by defining, at each step $n \ge 0$, a formula $\Pi^\prec_n$ in which $(i)$ the pattern $\prec$ is computed only for $n=0$ in the initial state $I$ of $\Pi$, and then exploited at each step $n$, $(ii)$ the starting state $S$ is set to $I$, and $(iii)$ the set $G$ of goals is required to hold in the last state that can be reached by one of the subsequences of $\prec$ concatenated $n$ times. The procedure begins with $n=0$, terminates as soon as $\Pi^\prec_n$ is satisfiable, and otherwise proceeds by incrementing $n$. In this paper, possibly at each step, $(i)$ we symbolically search for an intermediate state $P$ reachable from $I$, closer to a goal state, $(ii)$ dynamically recompute the pattern $\prec_h$ -- to be used in the next step -- in $P$, $(iii)$ refine the pattern $\prec_g$ used to reach $P$, and $(iv)$ start the new search from the state $S$ which can be either the initial state $I$ or the last computed intermediate state $P$, exploiting the computed patterns $\prec_g$ and $\prec_h$ to define the pattern $\prec$ to be used in the search. In particular, at each step, we define a formula $\Pi^{\prec}_{S,P}$ encoding the existence of a state $P'$ closer than $P$ to a goal state, with $P'$ reachable from the starting state $S$ when using the pattern $\prec$. We present different techniques for producing such formulas, each corresponding to a different strategy for exploring the search space. We prove their correctness and completeness, the latter under certain conditions.

---


### 370. [Phase-Aware Guidance Injection for Recurrent MAPPO in Assembly-Line Disruption Recovery](https://arxiv.org/abs/2606.16330)

**<font color=#1a73e8>作者：</font>** Xin Huang, Yongcai Wang, Fengyi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Disruption recovery in industrial assembly lines requires timely decisions under machine faults, worker absence, and emergency orders. Existing methods either rely on rigid handcrafted recovery logic or learn adaptive policies that do not readily exploit heterogeneous external recovery knowledge at decision time to reduce abnormal recovery time (ART) and preserve on-time delivery (OTD). To address this gap, we propose a phase-aware guidance injection framework that augments a trained recurrent MAPPO (RMAPPO) scheduling policy through logit-level action bias during evaluation. The framework provides a unified decision-time interface for rule-based, replay-based, and online LLM-based guidance, while activating intervention only during abnormal and recovery phases. Experiments on a custom AssemblyLineEnv show that high-quality rule guidance yields the strongest gains, replay-based guidance degrades smoothly under imperfect availability, and online LLM guidance still provides useful intermediate improvements. These results show that decision-time guidance injection can exploit heterogeneous recovery hints without redesigning the actor.

---


### 371. [Diffusion Offline Reinforcement Learning for Fair and Energy-Efficient UAV-Assisted Wireless Networks](https://arxiv.org/abs/2606.16331)

**<font color=#1a73e8>作者：</font>** Eslam Eldeeb, Hirley Alves  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The integration of generative artificial intelligence with wireless communication and signal processing systems has opened new avenues for intelligent, data-driven decision-making in future 6G networks. This work proposes a diffusion soft actor-critic (Diffusion-SAC) approach that leverages offline reinforcement learning (RL) enhanced by denoising diffusion probabilistic models (DDPMs) to optimize trajectory and scheduling control in unmanned aerial vehicle (UAV) networks. While offline RL methods, such as conservative Q-learning (CQL), can learn from static datasets, they often struggle to generalize in low-data or dynamic conditions. To address this, we combine the robustness of CQL with the generative power of diffusion models, enabling expressive and signal-aware policy learning that generalizes beyond behavior policies. Applied to a UAV-assisted wireless network, the proposed framework minimizes transmission energy and improves fairness among devices. Simulations show that Diffusion-SAC outperforms standard offline RL baselines, achieving more stable convergence and higher rewards even with limited datasets. The method enhances data efficiency, reduces energy consumption, and increases throughput by more than 35 % compared to existing algorithms, demonstrating its potential for robust policy learning in next-generation wireless control systems.

---


### 372. [Differentiable Packing of Irregular 3D Objects with Adaptive Container Estimation](https://arxiv.org/abs/2606.16333)

**<font color=#1a73e8>作者：</font>** Palak Gupta, Shanmuganathan Raman  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing approaches either fix the container in advance or optimize only a single container dimension through an outer search loop, leaving the remaining dimensions as a manual tuning problem. We present a differentiable packing framework that jointly optimizes all 6N object pose parameters and all three container side lengths inside a single gradient-based loop. The formulation combines six physics-inspired, differentiable loss terms computed directly on triangle meshes through axis-aligned bounding-box proxies. An adaptive squeezing mechanism periodically tightens the container whenever the overlap loss falls below a pair-count-scaled threshold, producing a large initial drop in container volume, followed by small refinements. All pairwise computations are written in tensor-broadcasting form, giving a 3.4 to 54 times speedup over a reference loop-based implementation. The pipeline is implemented in Python and PyTorch, with no physics engine, FFT library, or convex decomposition. On multiple object categories, the method produces containers that are 11 to 32 percent smaller than time-matched DBLF and simulated-annealing baselines at N =100, while running in under 4 minutes per instance on a single consumer GPU.

---


### 373. [Patient-centered visualization of multistage cancer treatment trajectories](https://arxiv.org/abs/2606.16335)

**<font color=#1a73e8>作者：</font>** Laura Lackner, Marius Bill, Martin Bornhaeuser 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Effective communication of multistage cancer treatment trajectories remains a major challenge, particularly for patients with limited health literacy. We present a patient-centered visualization approach for representing complex, phase-based oncology treatments, integrating principles from information visualization, user experience (UX) design, and cognitive psychology. Using acute myeloid leukemia (AML) as a case study, we developed two timeline-based representations: a static, visually simplified trajectory emphasizing structure and hierarchy, and an interactive variant with layered information. We evaluated both approaches in a quantitative survey, measuring comprehension of treatment sequences, perceived confidence, and information quality. Results show that the static visualization significantly improves understanding and clarity, highlighting the importance of visual hierarchy, consistent encoding, and reduced complexity when communicating temporal medical processes compared to the baseline. In contrast, additional interactivity did not improve performance and introduced navigational overhead, suggesting that interaction must be carefully aligned with cognitive demands. Our findings contribute to visualization research by demonstrating how patient-centered design can improve the interpretability of multistage treatment trajectories. We derive design implications for temporal medical visualizations, emphasizing simplicity, structural clarity, and accessibility to support informed decision-making in clinical contexts.

---


### 374. [Filtered ANN as a Phase Transition: When Selectivity-Estimation Error Causes Plan Regret](https://arxiv.org/abs/2606.16341)

**<font color=#1a73e8>作者：</font>** Madhulatha Mandarapu, Sandeep Kunkunuru  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A filtered approximate-nearest-neighbor (ANN) query returns the k nearest vectors among those satisfying an attribute predicate P of selectivity s. The best execution strategy -- pre-filter, post-filter, or in-filter -- changes with s, so a system must estimate s and choose. We model this as an argmax over a landscape with phases (regions where each strategy wins) separated by boundaries, and show that selectivity-estimation error produces plan regret -- recall lost versus the oracle strategy -- only in the critical regions around those boundaries. The regret is a wedge of log-width equal to the multiplicative estimation error epsilon and height equal to the local cliff |V'(s*)| epsilon; the flip-margin 1/|V'(s*)| is the condition number of a sibling cardinality-estimation study reappearing as the local boundary theory. The two phase boundaries follow from independent mathematics: order statistics place the post-filter cliff at s ~ k/K, and site percolation places the in-filter cliff at s_c ~ 0.83/M for graph degree M (corpus-size independent). Criticality exists only under a constrained budget B < sqrt(k n). Under pre-registered decision rules we confirm, on synthetic sweeps and real SIFT1M, that regret concentrates ~290x at the boundary and that the regret curves obey a finite-size scaling collapse onto one universal wedge across two decades of corpus size. A real approximate index does not mis-locate the boundary, but a biased cost model opens a persistent miscalibration band that estimation-error robustness cannot fix. The contribution is a characterization, not a new index. Code and the full pre-registration are public.

---


### 375. [When the Past Matters: FlashBack Memory for Precipitation Nowcasting](https://arxiv.org/abs/2606.16342)

**<font color=#1a73e8>作者：</font>** Yuhao Du, Boxiao Huang, Chengrong Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate precipitation nowcasting is crucial for disaster mitigation and socio-economic planning, yet existing methods often struggle with false alarms, missed events, and long range dependency modeling at high spatiotemporal resolution. To address these challenges, we propose FlashBack Memory (FB), a module that dynamically retrieves key historical states and integrates them via an adaptive fusion gate, enhancing the spatiotemporal representation capability of recurrent-based models. We incorporate FB into PredRNN, PredRNNpp, MIM, MotionRNN, and PredRNN-V2, and evaluate on CIKM2017, Shanghai2020, and SEVIR datasets. Experimental results demonstrate that FB significantly improves MSE, MAE, SSIM, and CSI metrics, particularly for high-intensity rainfall and long-sequence predictions, while reducing false alarms and missed events and enhancing temporal consistency and spatial localization. The proposed method provides a general and efficient memory enhancement mechanism, improving the overall performance of recurrent-based precipitation nowcasting models.

---


### 376. [TMASC: Transmasculine Attitude and Speech Corpus](https://arxiv.org/abs/2606.16351)

**<font color=#1a73e8>作者：</font>** Sidney Wong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce the Transmasculine Attitudes and Speech Corpus (TMASC), a multimodal corpus of 196 transmasculine individuals, including questionnaire responses and 66 audio recordings. The questionnaire includes items exploring the vocal health of transmasculine individuals. The audio recordings include cough and throat-clearing samples, a reading passage, and additional session-specific questions. This paper outlines the development of this corpus and the data collection procedures. To illustrate the utility of this corpus, we present three case studies demonstrating how this crowd-sourced multimodal corpus can be used to support transmasculine individuals. These include the integration of perceptual and acoustic data, the identification of group-level characteristics, and the calibration of acoustic measurements.

---


### 377. [What Should a Streaming Video Model Remember?](https://arxiv.org/abs/2606.16353)

**<font color=#1a73e8>作者：</font>** Haonan Ge, Yiwei Wang, Hang Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding models must answer queries at any moment during an ongoing stream, using only what they have observed so far and under fixed memory and computation budgets. Existing methods address this by adding memory banks, retrieval modules, or visual token compression to preserve long-range history. However, strong recent-window baselines show that indiscriminate history injection can dilute current-scene perception, suggesting that the key challenge is not whether to use memory, but how to allocate it selectively. We formulate this as budgeted online latent evidence allocation and propose \textbf{SelectStream}, a selective latent-memory framework that keeps the current observation directly visible to a frozen VLM while exposing historical information only through a compact, query-conditioned evidence budget. Three coordinated mechanisms govern when to write, what to preserve, and how to retrieve: surprise-driven adaptive windowing, priority-preserving consolidation, and query-conditioned graph reasoning over a fixed-capacity latent memory graph. Retrieved evidence is calibrated and injected as latent tokens for answer generation, without replaying frames or growing the context with stream length. Experimental results show that SelectStream achieves strong online streaming performance and preserves general video understanding, reaching 82.67\% on StreamingBench, 67.03\% on OVO-Bench, and 74.4\% average accuracy on offline video benchmarks, while outperforming strong recent-window baselines and prior streaming memory methods.

---


### 378. [Simulation-Augmented Multi-Step Split Conformal Prediction for Aggregated Forecasts](https://arxiv.org/abs/2606.16356)

**<font color=#1a73e8>作者：</font>** Andro Sabashvili  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study uncertainty quantification for aggregated forecasting tasks such as annual totals and year-over-year growth rates. We propose SA-MSCP, a simulation-augmented multi-step split conformal method that generates future paths from cross-validated residuals using a block bootstrap and constructs prediction intervals from empirical quantiles. Experiments show that SA-MSCP improves empirical coverage over a simulated-path baseline for aggregated and growth-rate targets. Our results demonstrate that simulation-enhanced conformal calibration is an effective and general framework for uncertainty quantification in aggregated time-series forecasting.

---


### 379. [CacheMuon: Using Temporal Preconditioning To Approximate Polar Factor](https://arxiv.org/abs/2606.16371)

**<font color=#1a73e8>作者：</font>** Bishnu Dev, Sushil Bohara, Martin Takáč 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon is an optimizer that computes updates using the polar factor of the momentum matrix and has shown strong empirical performance across a range of training settings. A key component of Muon is the Newton-Schulz iteration used to compute this polar factor. Although this avoids the cost of an exact singular value decomposition, it remains expensive in practice because it is applied at every optimization step. At the same time, the momentum matrix changes smoothly over training, suggesting strong temporal correlation in the corresponding polar factors. In this paper, we exploit this structure and propose CacheMuon, a temporal preconditioning method that reuses information from previous optimization steps to approximate the polar factor at the current step. This reduces redundant orthogonalization computation across iterations. We analyze CacheMuon as an inexact Muon update, with error controlled by fresh-solver error and cache staleness. Empirically, CacheMuon provides a controllable quality-efficiency frontier: conservative thresholds closely match fresh Muon on language-model and vision training while reducing orthogonalization FLOPs, whereas more aggressive thresholds yield larger arithmetic savings at the cost of modest validation-quality degradation.

---


### 380. [MIPSBLEED: Uncovering Microarchitectural Timing Leaks in Pervasive Embedded Processors](https://arxiv.org/abs/2606.16372)

**<font color=#1a73e8>作者：</font>** Ahmed Najeeb, Billy Bob Brumley  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite their age, MIPS processors remain deeply embedded in routers, industrial controllers, and IoT systems, yet their security against modern side-channel attacks has received little attention. This paper exposes how Simultaneous Multithreading (SMT), a feature increasingly used to boost performance in these environments, creates powerful cross-core timing channels on MIPS-based platforms. We introduce MIPSBLEED, a systematic analysis and exploitation framework that uncovers leakage in three shared microarchitectural components: the L1 data cache, L1 instruction cache, and the execution engine. Through carefully crafted assembly-level probes and quantitative leakage assessment, we demonstrate practical, high-resolution timing attacks that operate without requiring privileged access. Our evaluation reveals significant information leakage across all three channels and culminates in a single trace key recovery attack on a real elliptic curve cryptographic toolkit. These results position MIPS as an overlooked yet critical target in the study of microarchitectural security and underscore the urgent need for lightweight isolation mechanisms in resource-constrained, SMT-enabled embedded systems.

---


### 381. [Mixtures of Subspaces for Bandwidth Efficient Context Parallel Training](https://arxiv.org/abs/2606.16384)

**<font color=#1a73e8>作者：</font>** Sameera Ramasinghe, Ajanthan Thalaiyasingam, Hadi Mohaghegh Dolatabadi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretraining language models with extended context windows enhances their ability to leverage rich information during generation. Existing methods split input sequences into chunks, broadcast them across multiple devices, and compute attention block by block which incurs significant communication overhead. While feasible in high-speed clusters, these methods are impractical for decentralized training over low-bandwidth connections. We propose a compression method for communication-efficient context parallelism in decentralized settings, achieving a remarkable compression rate of over 95\% with negligible overhead and no loss in convergence. Our key insight is to exploit the intrinsic low-rank structure of activation outputs by dynamically constraining them to learned mixtures of subspaces via efficient reparameterizations. We demonstrate scaling billion-parameter decentralized models to context lengths exceeding 100K tokens on networks as slow as 300Mbps, matching the wall-clock convergence speed of centralized models on 100Gbps interconnects.

---


### 382. [Robust Neural Tucker Factorization with Bias Correction and Adaptive Initialization](https://arxiv.org/abs/2606.16388)

**<font color=#1a73e8>作者：</font>** Yuchao Su, Yixin Ran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional incomplete (HDI) tensors are widely used in traffic and climate applications, but sparse observations make accurate completion difficult. The intrinsic non-linear dynamics and non-stationary variations across distinct multi-modal fields severely hinder the efficacy of conventional linear reconstruction frameworks. Neural Tucker factorization provides an effective framework for modeling high-order interactions among tensor modes. By parameterizing underlying structural characteristics into continuous latent spaces, neural representations circumvent the rigid low-rank constraints of classical algebra. However, its performance can still be affected by implementation-level choices, especially parameter initialization and the bias configuration of the final output mapping. Suboptimal initializations frequently lead to variance explosion across the cubically expanded interaction spaces, driving the subsequent non-linear activation boundaries into severe gradient saturation zones, while the omission of a dedicated translation parameter forces interaction weights to implicitly absorb global statistical deviations. This paper proposes a simple yet effective neural Tucker factorization model with Kaiming initialization and bias correction (KaBiN) for HDI tensor completion. The proposed model utilizes Kaiming uniform initialization for the embedding and Tucker linear parameters, and adopts a simple bias correction in output mapping. By elegantly decoupling global mean shifts from local structural representations, the framework provides a highly stable and well-conditioned optimization landscape. Experiments on three real-world HDI tensor datasets show that KaBiN achieves better performance than the original NeuTucF, while introducing minimal computational overhead.

---


### 383. [Towards UAV Image Dehazing: A UAV Atmospheric Scattering Model, Benchmark, and Geometry-Aware Deep Unfolding Network](https://arxiv.org/abs/2606.16392)

**<font color=#1a73e8>作者：</font>** Wenxuan Fang, Jiangwei Weng, Yu Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In UAV applications, haze significantly obscures distant details and weaken structural information, hindering the recovery of details. Current UAV scenarios still face two key challenges: (i) paired hazy/clean images from the real world are unobtainable, while the classical atmospheric scattering model is inadequate for modeling the spatially non-uniform haze in UAV imagery; (ii) existing dehazing methods struggle to remove the heavy haze accumulated in the upper regions of UAV images. To address these issues, we first propose a UAV Atmospheric Scattering Model (UASM), which explicitly incorporates flight altitude, viewing pitch, and extinction to characterize the non-uniform haze distribution in UAV imaging. Based on UASM, we develop a physics-driven dehazing framework, termed Geometry-aware Proximal Deep Unfolding Network (GP-DUN). Specifically, GP-DUN consists of three key modules: a Latent Geometry Estimator (LGE) that infers transmittance consistent with UAV imaging geometry, a Geometry-aware Gradient Descent Module (GeoGDM) that embeds UASM into the data-fidelity term and performs physics-consistent closed-form updates, and an Pooling-Expert Proximal Mapping Module (PE-PMM) that learns an implicit prior to restore textures and structures beyond the capability of explicit physical modeling. In addition, we further construct UASM-HazeSet, which provides controllable paired synthetic data together with 2,285 real UAV haze images for testing. Extensive experiments show that GP-DUN consistently outperforms existing methods on both UASM-HazeSet and real UAV haze benchmarks.

---


### 384. [MPX: A Unified Systolic Array for Matrix and Polynomial Multiplication](https://arxiv.org/abs/2606.16394)

**<font color=#1a73e8>作者：</font>** George Alexakis, Dimitrios Schoinianakis, Giorgos Dimitrakopoulos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Polynomial multiplication is a fundamental kernel in Fully Homomorphic Encryption (FHE) and post-quantum cryptography (PQC) and is commonly accelerated through Number Theoretic Transforms (NTTs). To avoid the cost of designing dedicated cryptographic accelerators, recent efforts have mapped NTT computations onto existing systolic matrix engines, enabling the reuse of AI hardware for cryptographic workloads. In this work, we take the opposite approach. We observe that the wavefront dataflow of systolic arrays naturally aligns with the accumulation pattern of polynomial multiplication and leverage this correspondence to design MPX, a dual-mode systolic array that supports both matrix multiplication and direct polynomial multiplication within the same hardware fabric. Experimental results show that extending a conventional systolic array with this dual-mode capability requires only 20% additional area and introduces negligible power overhead during matrix-multiplication execution. In polynomial-multiplication mode, MPX achieves more than 1.2x lower latency compared to NTT-based polynomial multiplication on systolic matrix engines.

---


### 385. [SP$^3$: Spherical Priors for Plug-and-Play Restoration](https://arxiv.org/abs/2606.16396)

**<font color=#1a73e8>作者：</font>** Sean Man, Ron Raphaeli, Matan Kleiner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce SP$^3$, a novel Plug-and-Play algorithm that accelerates maximum a posteriori image restoration by replacing denoisers with Spherical Encoders (SE) as generative priors. SP$^3$ approximates the intractable proximal prior step by utilizing the SE tightly structured latent space as a robust projection onto the natural image manifold. Alternating this projection with a closed-form data-consistency step, via Half-Quadratic Splitting, achieves stable convergence without requiring gradient computation during inference. This unique formulation unlocks "anytime" restoration capabilities, producing sharp, plausible images from the first iteration. Evaluations across a variety of image restoration tasks demonstrate that SP$^3$ achieves perceptual quality comparable to state-of-the-art zero-shot diffusion and flow methods while being $3$-$630\times$ faster.

---


### 386. [RGFVR: Reference-Guided Face Video Restoration with Flow Matching](https://arxiv.org/abs/2606.16401)

**<font color=#1a73e8>作者：</font>** Cem Eteke, Batuhan Tosun, Eckehard Steinbach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face video restoration from degraded observations is challenging, as it requires simultaneously recovering visual fidelity, temporal consistency, and subject identity. Existing approaches are often either reference-free, which can lead to identity loss when person-specific facial details are lost, or subject-specific, which limits generalization to unseen identities. We propose a subject-agnostic, reference-guided framework for identity-preserving face video restoration. Our method introduces bimodal perceptual-descriptive identity conditioning into a pretrained flow-based text-to-video generator and employs a two-stage training strategy to strengthen identity guidance during restoration. Experiments show that our approach improves restoration fidelity, temporal consistency, and identity preservation, achieving superior performance under challenging video degradations, including downsampling, blur, noise, and compression artifacts. The code is available under: this https URL.

---


### 387. [Not all Jensen-Shannon Divergence Estimators are Equal](https://arxiv.org/abs/2606.16411)

**<font color=#1a73e8>作者：</font>** Alba Garrido, Alejandro Almodóvar, Mar Elizo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Jensen-Shannon divergence is widely reported as a scalar measure of fidelity for synthetic tabular data. Yet, in practice, it is estimated from finite samples using protocols that are often underspecified. This creates a measurement problem. Although the population divergence is well defined, the empirical value depends on the estimator family, sampling protocol, calibration, dimensionality, and class balance. We show that different protocols can yield non-comparable values: marginal-based estimators ignore dependencies in the joint distribution and can severely underestimate divergence, while classifier-based estimators capture joint structure but exhibit strong estimator dependence. We systematically study this behavior across controlled settings with reference divergences and real-world synthetic tabular benchmarks. Our analysis reveals dependence blindness in marginal estimators, prior-shift bias under class imbalance, and estimator sensitivity in high dimensions. To address prior shift, we derive a closed-form posterior correction for classifier-based Jensen-Shannon estimation. Our results show that empirical Jensen-Shannon divergence values are inherently protocol-dependent, making explicit specification of the estimation procedure necessary for meaningful comparison. We provide practical guidelines and an open-source tool for estimator-aware Jensen-Shannon evaluation.

---


### 388. [Instance-Aware Knowledge Distillation for Semi-Supervised Learning of an On-Board Multi-Task Dense Prediction Model for Collision Avoidance System](https://arxiv.org/abs/2606.16414)

**<font color=#1a73e8>作者：</font>** Gyutae Hwang, Sang Jun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Collision avoidance systems have evolved toward camera-based deep learning approaches for driving scene understanding. However, deployment in edge environments such as country clubs is constrained by limited computational resources and unreliable communication infrastructure. Moreover, constructing large-scale datasets for the target domain involves substantial annotation cost. To address these limitations, we propose an instance-aware knowledge distillation framework for semi-supervised learning. Specifically, we generate pseudo labels that mitigate teacher bias by leveraging domain priors from the teacher and instance-centric knowledge from foundation models. The trained lightweight student is deployed in the proposed collision avoidance system and performs multiple dense prediction tasks in real-time. The system detects frontal obstacles and encodes their spatial information into controller area network messages for automated guided vehicle operation. To achieve this, we construct a large-scale country club dataset and perform field validation of the proposed system. Experimental results demonstrate that the student outperforms the large teacher in instance segmentation while mitigating performance degradation in monocular depth estimation. Compared with the teacher, the student reduces FLOPs by 22.68$\times$ and parameters by 14.33$\times$, achieving 6.46 FPS on a low-cost edge device.

---


### 389. [Posterior Twins: Distributional Behavioral Simulation for Enterprise Decisions](https://arxiv.org/abs/2606.16415)

**<font color=#1a73e8>作者：</font>** Ankit Das  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise behavioral simulation requires more than producing a plausible response. Many decisions depend on the shape of a population under a proposed action: which segments accept, defect, hesitate, or move into risk-sensitive states. This paper introduces Posterior Twins, a memory-grounded digital-twin approach that represents likely behavior as an updated distribution under a specific decision context. We evaluate a family of Twinning Labs behavioral-model operating points on a 226-example held-out behavioral-response benchmark and report both modal accuracy and Wasserstein-1 distance. The results show that modal accuracy and distributional fidelity identify different operating regimes. TL-Twin Alpha achieves the lowest observed Wasserstein-1 distance in the reported result set ($W_1 = 1.16$), while TL-Twin Delta and TL-Twin Gamma provide balanced operating points near the modal-accuracy frontier. The paper frames these results as a systems result: governed memory, behavioral model routing, scenario orchestration, distributional aggregation, and auditability are necessary for turning simulated behavior into reusable enterprise decision evidence.

---


### 390. [Beer-Lambert Guided Representation Learning for Unsupervised Anomaly Detection in Sub-THz Food Inspection Images](https://arxiv.org/abs/2606.16421)

**<font color=#1a73e8>作者：</font>** Gyutae Hwang, Sang Jun Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Food manufacturing requires reliable inspection systems to detect foreign material contamination and maintain product safety. Sub-THz transmission imaging provides material-dependent attenuation characteristics that are useful for detecting low-density contaminants in food products. However, existing unsupervised anomaly detection methods mainly rely on RGB-pretrained visual representations, which may not adequately capture the transmission behavior of Sub-THz images. This paper proposes a Beer-Lambert guided representation learning framework for unsupervised anomaly detection in Sub-THz food inspection images. The proposed method introduces an attenuation decomposition module as an auxiliary regularization module that constrains student representations through attenuation reconstruction during training. In addition to the conventional one-class setting, we introduce a Leave-One-Food-Out protocol to evaluate generalization capability under unseen food categories. Experimental results on the Inline-Food-Inspection-THz dataset show that the proposed method improves overall anomaly detection performance over the baseline method.

---


### 391. [LectūraAgents: A Multi-Agent Framework for Adaptive Personalized AI-Assisted Learning and Embodied Teaching](https://arxiv.org/abs/2606.16428)

**<font color=#1a73e8>作者：</font>** Jaward Sesay, Yue Yu, Siwei Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective personalized AI-assisted learning demands systems that can not only generate accurate learner-specific educational materials, but also dynamically adapt their instruction to diverse learners. However, existing educational agents have primarily focused on lecture content automation and simulations, which often fall short of modelling multimodal and embodied instructional methods tailored for the individual learner. To this end, we propose LectūraAgents - a multi-agent framework that enables personalized learning through end-to-end adaptive embodied teaching. At its core, LectūraAgents mirrors a professor-student relationship, in which a ProfessorAgent leads a collaborative team of specialized subordinate agents through research, planning, review, and embodied delivery of lecture contents that adapt to a learner's needs. The framework offers three main contributions: (1) a hierarchical multi-agent architecture for end-to-end personalized learning; (2) an adaptive embodied teaching mechanism, wherein the ProfessorAgent executes visible and pedagogically motivated teaching actions (e.g., handwrite, highlight, underline, etc.) over contents in a teaching environment; and (3) a Teaching Action-Speech Alignment (TASA) algorithm that employs salience-based heuristics and temporal semantic segmentation to generate coherent teaching action sequences aligned with learner profiles. We evaluate LectūraAgents on diverse courses at high school, undergraduate, and graduate levels using sample-specific rubric-based analysis; with generated lecture materials and teaching actions assessed and validated by expert educators. Experimental results show consistent gains in lecture content quality, embodied teaching quality, assessment, and personalization over existing approaches, positioning LectūraAgents as a pedagogically well-grounded framework for personalized learning at scale.

---


### 392. [Taylor-Calibrate: Principled Initialization for Hybrid Linear Attention Distillation](https://arxiv.org/abs/2606.16429)

**<font color=#1a73e8>作者：</font>** Zhongzhu Zhou, Qingyang Wu, Junxiong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hybrid linear attention models offer an appealing path to faster long-context inference: they reduce the quadratic cost and KV-cache burden of full softmax attention while retaining much of the quality of Transformer models. A practical way to obtain such models is to convert a pretrained Transformer instead of pretraining a new architecture from scratch, but this conversion is still brittle. Simply copying the teacher attention projections into a Gated DeltaNet (GDN) student does not specify the new recurrent decay, write, and output-gating dynamics. As a result, the converted model often starts in a poor dynamical regime and must spend many distillation tokens repairing initialization rather than learning the remaining teacher behavior. We propose Taylor-Calibrate, a lightweight initialization method for hybrid GDN students. The method uses Taylor-guided teacher attention statistics to set the value projection, memory timescale, write gates, and output gate, then applies a short per-layer alignment step to match each converted layer to the teacher output. Across four teacher settings and three retained-layer policies, Taylor-Calibrate gives substantially stronger zero-shot students, with up to an 88x improvement in a representative ablation, and reaches matched recovery targets with 4.9x--9.2x fewer training tokens than naive conversion.

---


### 393. [Autonomous End-to-End SOH Prediction Services for Battery Systems via Temporal-Contrastive Representation Learning](https://arxiv.org/abs/2606.16434)

**<font color=#1a73e8>作者：</font>** Junting Wen, Dan Li, Qihao Quan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate state of health (SOH) estimation is a critical diagnostic service for lithium-ion battery management. However, reliance on labor-intensive manual feature engineering and opaque black-box models hinders scalable industrial deployment. To address this, we introduce TC-SOH: a modular, plug-and-play service architecture for autonomous, end-to-end SOH prediction. TC-SOH employs a temporal-contrastive mechanism and a cross-window prediction pretext task to extract degradation-relevant representations directly from raw operational data. To improve transparency, we connect model efficacy with representation diagnostics: visualization, sensitivity analysis, redundancy analysis, bidirectional probing, future-SOH probing, and temporal shuffling show that learned features overlap with selected expert descriptors while retaining additional SOH-relevant variation, and that ordered temporal context improves subsequent-SOH prediction. Across four public datasets, TC-SOH outperforms the considered physics-informed and data-driven baselines, reducing MAPE by 1.91 times and RMSE by 2.13 times.

---


### 394. [Beyond Usability: A UX Case Study on Using "Withdrawal Design" to Challenge Engagement Metrics in Social Robotics](https://arxiv.org/abs/2606.16439)

**<font color=#1a73e8>作者：</font>** Yibo Meng, Qiuyu Long, Richard Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social robots for children with autism are often evaluated through engagement and interaction quality, assuming the robot acts as a social scaffold. We report a mixed-methods "withdrawal" study that tests a harder question: what changes when the robot is removed. In an 8-week home-based randomized controlled trial (N=40), children either retained a consumer social robot (Qrobot) or had it withdrawn after initial use. Quantitatively, continued access reduced anxiety (SCARED/RCADS), yet was associated with lower parent-reported social motivation and weaker gains in emotion recognition (SMS/RMET) compared to withdrawal. Interviews with guardians contextualized this divergence: removal sometimes prompted children to seek human interaction, while continued use could keep social behavior siloed within the child-robot dyad, despite exceptionally high usability (SUS). We synthesize a UXR point of view: for vulnerable users, "engagement" can mask ecological downsides. Success should be judged not by retention, but by designed separation that bridges back to human relationships.

---


### 395. [Hierarchical Fine-Grained Aerial Object Detection](https://arxiv.org/abs/2606.16448)

**<font color=#1a73e8>作者：</font>** Yan Zhang, Fang Xu, Wen Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained aerial object detection, driven by the intrinsic granularity of real-world object categories, is crucial for advanced scene understanding in remote sensing. Existing methods largely inherit the paradigm of coarse-grained object detection, relying solely on single-label supervision and thus struggling to distinguish model-level categories with subtle structural differences. However, for each specific model (e.g., Boeing 787), structured prior knowledge such as attributes and hierarchies offers discriminative semantics across multiple granularities. Motivated by this, we present ExpertDet, a scheme that incorporates expert-informed cues to enhance fine-grained aerial object detection. Specifically, we design Vision-aware Masked Attribute Modeling (VMAM), which aligns attribute semantics with visual structures by reconstructing randomly masked attributes from visual cues, enabling the detector to capture subtle structural distinctions. We further propose Hierarchical Visual Instance Promotion (HierVIP), which builds a visual prototype tree based on hierarchical relations and imposes taxonomy-aware constraints to preserve cross-level semantic continuity while enhancing category discrimination. Moreover, we curate a new fine-grained object detection benchmark for Precise recognition of model-specific Ships and Planes from aerial imagery, PSP, covering 106 ship classes and 30 airplane models, respectively, featuring the most extensive collection of model-specific categories among existing aerial object detection datasets to date. We benchmark state-of-the-art object detection algorithms on the PSP benchmark. Extensive evaluation demonstrates that ExpertDet consistently outperforms other fine-grained competitors across hierarchy levels. The dataset, benchmark, and code are available at this https URL.

---


### 396. [PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory](https://arxiv.org/abs/2606.16449)

**<font color=#1a73e8>作者：</font>** Shuai Yang, Bingjie Gao, Ziwei Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Consistent video generation under editing operations requires persistence: when edits modify scene appearance or layout, subsequent generations should remain coherent across time and viewpoints. However, existing memory designs struggle to maintain long-term consistency after such modifications, as stored contexts may become outdated or invalid. To address this, we propose PermaVid, a novel framework built upon a multi-modal context memory that disentangles spatial context into semantic appearance and geometric structure, together with an edit-aware memory update and retrieval strategy that keeps memory evolution aligned with subsequent observations. Specifically, we develop two complementary memory banks: an RGB context memory that captures appearance-aware observations while implicitly encoding geometry, and a depth context memory that preserves geometry-only structure disentangled from semantics. Building on this design, we introduce a memory-guided video generation model that performs multi-modal feature fusion under reference conditions drawn from mixed-modality memory contexts. Experiments demonstrate that our method maintains strong long-term semantic and structural consistency after edits, significantly outperforming state-of-the-art methods.

---


### 397. [SDS-LoRA: Overcoming Anisotropic Gradient Scaling in Low-Rank Adaptation](https://arxiv.org/abs/2606.16454)

**<font color=#1a73e8>作者：</font>** Junghun Oh, Sungyong Baik, Kyoung Mu Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) enables efficient adaptation of large pre-trained models to downstream tasks by parameterizing weight updates with low-rank matrices. In this paper, we investigate the limitations of the LoRA parameterization from a geometric perspective. Specifically, we show that when a full fine-tuning gradient is backpropagated to the low-rank matrices, it undergoes anisotropic scaling driven by their singular values. We argue that this phenomenon is undesirable because it distorts the full fine-tuning gradient by skewing it toward dominant singular directions while suppressing others. Our analyses demonstrate that anisotropic gradient scaling reduces the effective rank of the low-rank matrices' gradients and results in suboptimal alignment between the full fine-tuning gradient and its low-rank approximation in LoRA, thereby exacerbating the gap to full fine-tuning. To address these limitations, we propose a new low-rank parameterization, SDS-LoRA, which structurally decouples singular values from the backward pass. Our method ensures that the full fine-tuning gradient backpropagates only through the orthonormal bases of the low-rank matrices' subspaces, independent of their scales. Convergence analysis demonstrates that while LoRA's convergence rate degrades with the condition number of the low-rank matrices, SDS-LoRA remains independent of it. Experimental results across natural language and vision benchmarks show that SDS-LoRA improves loss convergence and reduces the gap to full fine-tuning, significantly enhancing adaptation performance.

---


### 398. [ResEdit: Residual embeddings for precise generative image editing](https://arxiv.org/abs/2606.16457)

**<font color=#1a73e8>作者：</font>** Ahmet Canberk Baykal, Valentin Deschaintre, Yannick Hold-Geoffroy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Conditional diffusion image generators can be repurposed for editing through inversion, without the need for large-scale paired fine-tuning data. However, producing high-quality, targeted edits while maintaining image identity and global consistency remains challenging, as weakly conditioned inversion often embeds conflicting image features into the noise. We demonstrate that incorporating a residual image encoding as additional conditioning enables both improved identity preservation and better editability. We optimize this residual encoding to provide a strong conditioning signal for reconstruction, thereby reducing the reliance on inversion and susceptibility to its aforementioned pitfalls. To ensure this residual does not interfere with desired edits, we incorporate a gradient reversal-based optimization strategy that disentangles the residual from the edited condition. We illustrate our method's ability to produce high-fidelity results across precise intrinsic-based editing and relighting, and show proof-of-concept text-guided manipulation.

---


### 399. [Learning aligned EEG representations with subject-specific encoders](https://arxiv.org/abs/2606.16462)

**<font color=#1a73e8>作者：</font>** Bruna J. Lopes, Gabriel Schwartz, Sylvain Chevallier 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cross-subject EEG decoding promises more training data, but it also exposes neural networks to strong inter-subject distribution shifts. We study whether task supervision and architecture alone can learn subject-aligned representations. We replace a shared EEG encoder with subject-specific encoders followed by a common classifier, and compare this hybrid model with standard EEGNet, AttentionBaseNet, and CTNet baselines with Euclidean Alignment (EA) on four motor-imagery datasets. EA improves shared encoders by recentering subject covariances, but the hybrid encoder largely internalises this role: validation-loss curves and latent-distance analyses change little when EA is removed. Subject-specific heads increase class distinctiveness and place each subject close to its own latent manifold, improving most subjects while leaving a method-sensitive subset. These results support subject-specific encoders as a learned alignment mechanism for EEG decoding and identify head selection for unseen subjects as the remaining bottleneck.

---


### 400. [When Agent Automation Becomes Profitable: Quantifying and Insuring Autonomous AI Risk through Trace-Economic Underwriting](https://arxiv.org/abs/2606.16465)

**<font color=#1a73e8>作者：</font>** Binyan Xu, Xilin Dai, Fan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can now take irreversible actions in operational systems, but agent-caused losses are still not clearly assigned, priced, or transferred. Providers often disclaim consequential damages, users are left with uncompensated losses, and default human review limits the efficiency gains of automation. We ask when autonomous AI deployment can become economically acceptable despite failure risk. Our answer is to quantify risk at the customer-task-trace episode level and transfer it through insurance. Automation is acceptable when its expected benefit exceeds the premium, control cost, and remaining risk. This requires a defined role with bounded permissions and comparable traces. We introduce trace-economic underwriting, which maps tool-use traces to customer exposure and claimable loss, then uses this representation for pricing, control, and risk transfer. It uses deterministic economic labels rather than an LLM judge. In our trace-to-loss testbed, trace-economic pricing reduces pricing MAE from $17.7K to $569 and removes regressive cross-subsidy. A 300-trace expert audit accepts 295 labels unchanged. On 1,000 real SWE-smith traces, trace-conditioned controls reduce CVaR95 by 72%. Theorem~1 gives a finite-sample scope condition. We release code, labels, and audit sheets.

---


> [!TIP]
> 当前位于：**351-400**（第 8/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-509](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
