# 📦 其他研究 | 2026年05月06日

> 本类共 **511** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

---

### 1. [Synthetic Designed Experiments for Diagnosing Vision Model Failure](https://arxiv.org/abs/2605.00832)

**<font color=#1a73e8>作者：</font>** Krisanu Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current synthetic data pipelines for computer vision generate images without diagnosing what the downstream model actually needs. This open-loop paradigm treats synthetic data as cheap real data, randomly sampling the generator's output space and hoping to cover the model's failure modes. We argue this fundamentally misuses synthetic data's unique property: the controllable, independent variation of scene this http URL on the statistical theory of Design of Experiments (DoE), we propose Synthetic Designed Experiments for Representational Sufficiency (SDRS). SDRS treats the downstream model as a black-box system and the synthetic generator as an experimental apparatus. Using fractional factorial designs, SDRS efficiently audits a model's factor-sensitivity profile via ANOVA decomposition. It classifies failures into two actionable types: Type I gaps (coverage failures on underrepresented factor levels) and Type II gaps (reliance on spurious nuisance dependencies). The audit then prescribes targeted synthetic data to address each gap type. We validate SDRS on three experiments: (1) a controlled diagnostic on dSprites with planted biases, where the audit correctly identifies both gap types and targeted data improves accuracy from 49.9% to 79.0%; (2) a dense segmentation task on procedural scenes, where detecting background-complexity shortcuts and applying targeted data improves mIoU from 0.948 to 0.998; and (3) an entanglement detection experiment showing that the ANOVA audit identifies cross-factor contamination in imperfect generators. Finally, we show that per-factor invariance penalties can transfer sensitivity between factors, identifying an open problem for representation-level correction.

---


### 2. [Polynomial-Time Optimal Group Selection via the Double-Commutator Eigenvalue Problem](https://arxiv.org/abs/2605.00834)

**<font color=#1a73e8>作者：</font>** Mitchell A. Thornton  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The algebraic diversity framework replaces temporal averaging over multiple observations with algebraic group action on a single observation for second-order statistical estimation. The central open problem in this framework is $\textit{group selection}$: given an $M$-dimensional observation with unknown covariance structure, find the finite group whose spectral decomposition best matches the covariance. Naive enumeration of all subgroups of the symmetric group $S_M$ requires exponential time in $M$. We prove that this combinatorial problem reduces to a generalized eigenvalue problem derived from the double commutator of the covariance matrix, yielding a polynomial-time algorithm with complexity $O(d^2M^2 + d^3)$, where $d$ is the dimension of a generator basis. The minimum eigenvector of the double-commutator matrix directly constructs the optimal group generator in closed form, with no iterative optimization. The reduction is exact: the double-commutator minimum eigenvalue is zero if and only if the optimal generator lies in the span of the basis, and its magnitude provides a certifiable optimality gap when it does not. This problem does not appear in the standard catalogs of computational complexity (Garey and Johnson, 1979) and represents a new class linking group theory, matrix analysis, and statistical estimation. We establish connections to independent component analysis (JADE), structured matrix nearness problems, and simultaneous matrix diagonalization, and we show that the double-commutator formulation is the unique approach that is simultaneously polynomial-time, closed-form, and certifiable.

---


### 3. [Sparse Regression under Correlation and Weak Signals: A Reproducible Benchmark of Classical and Bayesian Methods](https://arxiv.org/abs/2605.00835)

**<font color=#1a73e8>作者：</font>** Hao Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Choosing between classical and Bayesian sparse regression methods involves a real trade-off: penalized estimators like Lasso run in milliseconds but give no uncertainty estimates,while Horseshoe and Spike-and-Slab priors produce full posteriors but need MCMC chains that take minutes per this http URL few studies compare these two families head-to-head under the conditions that actually make sparse regression hard -- correlated features, weak signals, and growing dimensionality. We benchmark six methods (OLS, Ridge,Lasso, Elastic Net, Horseshoe, Spike-and-Slab) on synthetic data with three covariance structures (rho up to 0.9), four SNR levels, and p in {20, 50, 100}, plus the Diabetes dataset,totalling over 2,600 experiments. The results are clear on some points and nuanced on others. Bayesian methods win on prediction error (MSE 72 vs. 108-267), and the Horseshoe delivers near-nominal 95% coverage (94.8%). But Spike-and-Slab,despite narrower intervals, under-covers at 91.9% -- its continuous relaxation likely plays a role. For variable selection, Lasso and Spike-and-Slab tie at F1 ~ 0.47, making Lasso the practical default when posteriors are not needed. Code and data are available at this https URL.

---


### 4. [From Euler to Dormand-Prince: ODE Solvers for Flow Matching Generative Models](https://arxiv.org/abs/2605.00836)

**<font color=#1a73e8>作者：</font>** Hao Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sampling from Flow Matching generative models requires solving an ordinary differential equation (ODE) whose computational cost is dominated by neural network forward passes. We derive four classical ODE solvers -- Euler, Explicit Midpoint, Classical Runge-Kutta (RK4), and Dormand-Prince 5(4) -- from first principles via Taylor expansion, implement them from scratch in PyTorch, and systematically benchmark their efficiency on Conditional Flow Matching tasks ranging from 2D toy distributions to MNIST digits. On the quantitative side, we use sliced Wasserstein distance to construct NFE-quality Pareto frontiers,finding that RK4 at 80 function evaluations achieves sample quality comparable to Euler at 200. Beyond reproducing known convergence rates, we report two empirical observations: (1) the Jacobian eigenvalue spectrum of the learned velocity field stiffens sharply near t=1, explaining why the adaptive Dormand-Prince solver automatically concentrates its step budget at the end of the trajectory; (2) the quality gap between low-order and high-order solvers widens for undertrained and smaller models, indicating that solver choice matters most when the model is imperfect. Code and all experiment scripts are publicly available.

---


### 5. [Fast Log-Domain Sinkhorn Optimal Transport with Warp-Level GPU Reductions](https://arxiv.org/abs/2605.00837)

**<font color=#1a73e8>作者：</font>** Hao Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Entropic regularized optimal transport (OT) via the Sinkhorn algorithm has become a fundamental tool in machine learning, yet existing implementations either suffer from numerical instability for small regularization parameters or incur significant overhead from deep learning frameworks. We present FastSinkhorn, a lightweight, native CUDA implementation of the log-domain Sinkhorn algorithm that combines warp-level shuffle reductions with shared-memory tiling to achieve high GPU utilization without sacrificing numerical stability. Our solver operates entirely in the log-domain, enabling robust computation for regularization parameters as small as epsilon = 10^{-4} where standard-domain methods fail. On dense OT problems with n = m = 8192, our implementation achieves 12x speedup over the widely-used POT library and 5.9x speedup over GPU-accelerated PyTorch baselines, while consuming only 256 MB of GPU memory. We validate our solver on image color transfer, 3D point cloud matching, and convergence analysis, demonstrating that native CUDA kernels with careful numerical treatment provide a practical and efficient foundation for large-scale optimal transport computation.

---


### 6. [2026 Roadmap on Artificial Intelligence and Machine Learning for Smart Manufacturing](https://arxiv.org/abs/2605.00839)

**<font color=#1a73e8>作者：</font>** Jay Lee, Hanqi Su, Marco Macchi 等 54 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The evolution of artificial intelligence (AI) and machine learning (ML) is reshaping smart manufacturing by providing new capabilities for efficiency, adaptability, and autonomy across industrial value chains. However, the deployment of AI and ML in industrial settings still faces critical challenges, including the complexity of industrial big data, effective data management, integration with heterogeneous sensing and control systems, and the demand for trustworthy, explainable, and reliable operation in high-stakes industrial environments. In this roadmap, we present a comprehensive perspective on the foundations, applications, and emerging directions of AI and ML in smart manufacturing. It is structured in three parts. The first highlights the foundations and trends that frame the evolution of AI in smart manufacturing. The second focuses on key topics where AI is already enabling advances, including industrial big data analytics, advanced sensing and perception, autonomous systems, additive and laser-based manufacturing, digital twins, robotics, supply chain and logistics optimization, and sustainable manufacturing. The third section explores non-traditional ML approaches that are opening new frontiers, such as physics-informed AI, generative AI, semantic AI, advanced digital twins, explainable AI, RAMS, data-centric metrology, LLMs, and foundation models for highly connected and complex manufacturing systems. By identifying both opportunities and remaining barriers across these areas, this roadmap outlines the advances needed in methods, integration strategies, and industrial adoption. We hope this roadmap will serve as a guide for researchers, engineers, and practitioners to accelerate innovation, align academic and industrial priorities, and ensure that AI-driven smart manufacturing delivers reliable, sustainable, and scalable impact for the future of manufacturing ecosystems.

---


### 7. [AI Agents for Sustainable SMEs: A Green ESG Assessment Framework](https://arxiv.org/abs/2605.00841)

**<font color=#1a73e8>作者：</font>** Viet Trinh, Tan Nguyen, Minh-Huyen Phan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study presents a novel, AI-driven framework for assessing Environmental, Social, and Governance (ESG) performance in European small and medium-sized enterprises (SMEs). An initial phase established expert-validated ESG baseline scores from a subset of the Flash Eurobarometer FL549 survey data. In the second phase, a scalable AI agent system, built on the n8n automation platform, applied these baselines to perform automated ESG classification and generate contextual recommendations using large language models (LLMs). The results demonstrate the AI system's high consistency with human-derived outputs, thereby supporting more effective monitoring and intervention strategies aligned with the European Green Deal.

---


### 8. [Latent Space Probing for Adult Content Detection in Video Generative Models](https://arxiv.org/abs/2605.00874)

**<font color=#1a73e8>作者：</font>** Alizishaan Khatri, Chiquita Prabhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of AI-powered video generation systems has introduced significant challenges in content moderation, particularly with respect to adult and sexually explicit material. Existing detection methods operate on either prompts or decoded pixel-space outputs. Therefore, both approaches are blind to the rich internal representations formed during generation. In this paper, we propose a novel latent space probing framework that intercepts the denoised latent representations produced by the CogVideoX video diffusion model during inference and attaches lightweight classifiers to perform real-time adult content detection. To support this work, we construct a large-scale binary dataset of 11039 ten-second video clips (5086 violating, 5953 non-violating) sourced from adult websites and YouTube respectively. We introduce two lightweight probing classifier architectures. We train and evaluate it on the dataset. Our work demonstrates that latent-space signals encode strong discriminative features for harmful content detection, achieving 97.29% F1 on our held-out test set with an overhead in the 4-6ms range. Our results suggest that probing the latent space results in improvements in both detection performance as well as cost.

---


### 9. [Visual Chart Representations for Cryptocurrency Regime Prediction: A Systematic Deep Learning Study](https://arxiv.org/abs/2605.00875)

**<font color=#1a73e8>作者：</font>** Dustin M. Haggett  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Technical traders have long relied on visual analysis of candlestick charts to identify market patterns and predict price movements. While deep learning has achieved remarkable success in image classification, its application to financial chart images remains underexplored. This paper presents a systematic study comparing different visual representations for cryptocurrency regime prediction. We evaluate three image encoding methods (raw candlestick charts, Gramian Angular Fields, and multi-channel GAF), five chart component configurations, four neural network architectures (CNN, ResNet18, EfficientNet-B0, and Vision Transformer), and the impact of ImageNet transfer learning. Through eight controlled experiments on Bitcoin, Ethereum, and S&P 500 data spanning 2018-2024, we identify optimal configurations for visual regime classification. Our results show that a simple 4-layer CNN on raw candlestick charts achieves 0.892 AUC-ROC, outperforming larger pretrained models. Surprisingly, simpler representations (price-only charts, 128x128 resolution) consistently outperform more complex alternatives. We provide interpretability analysis using GradCAM and demonstrate that transfer learning improves performance by 4-16% despite the domain gap between natural images and financial charts.

---


### 10. [Single Image Defogging Using a Fourth-Order Telegraph PDE Guided by Physical Haze Modeling](https://arxiv.org/abs/2605.00878)

**<font color=#1a73e8>作者：</font>** Manish Kumar, Rajendra K. Ray  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real-world scenarios, image defogging is an inverse problem due to unknown scene depth, atmospheric scattering, and the common absence of ground truth . To resolve the issue, we propose a hybrid defogging model that integrates a fourth-order nonlinear PDE with a physical haze formation model. We used Dark Channel Prior to estimate atmospheric parameters and to generate a guidance image, while the final restoration is performed via a fourth-order PDE-based evolution. A fourth-order PDE of the type telegraph is then evolved, incorporating an edge-adaptive diffusion coefficient and a fidelity term weighted by the transmission map. Fourth-order diffusion effectively suppresses haze while preserving structural details, and the hyperbolic formulation improves numerical stability and convergence behavior. We use relative error norm criteria for the convergence of our PDE. The proposed method is compared with Dark Channel prior, modified Dark Channel prior, and variational-based single-image defogging techniques. When we have ground truth available, we use MSE and SSIM for quantitative evaluation, whereas no-reference metrics, including FADE, Contrast Restoration Index, Average Gradient, and Entropy, are applied to real-world foggy images. Experimental results demonstrate that the proposed hybrid PDE-based method provides comparable visual quality and maintains structural details.

---


### 11. [Adversarial Flow Matching for Imperceptible Attacks on End-to-End Autonomous Driving](https://arxiv.org/abs/2605.00880)

**<font color=#1a73e8>作者：</font>** Xinyu Zeng, Xiangkun He, Lei Tao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving (AD) is evolving towards end-to-end (E2E) frameworks through two primary paradigms: monolithic models exemplified by Vision-Language-Action (VLA), and specialized modular architectures. Despite their divergent designs, both paradigms increasingly rely on Transformer backbones for complex reasoning, potentially causing a shared vulnerability: visually imperceptible perturbations can manipulate E2E AD models into hazardous maneuvers by targeting the Transformer module. Most existing adversarial attack approaches against AD systems operate under white-box or black-box settings; yet, they typically necessitate full model transparency, or suffer from either prohibitive query latency or limited attack transferability. In this paper, we propose Adversarial Flow Matching (AFM), a novel gray-box attack framework that exploits Transformer structural vulnerabilities in E2E AD models. AFM enables efficient one-step generation of adversarial examples via a neural average velocity field. Additionally, the proposed technique yields effective and visually imperceptible attacks by synergistically perturbing the generative latent space and the neural average velocity field. Extensive experiments demonstrate that AFM achieves a superior trade-off between attack effectiveness and imperceptibility: it substantially degrades the performance of both VLA and modular AD agents across various scenarios compared to baselines, while maintaining state-of-the-art visual imperceptibility. Furthermore, adversarial examples generated by AFM exhibit robust cross-model transferability, indicating that AFM closely approximates a black-box attack setting while requiring only the prior knowledge that the target AD model incorporates a Transformer-based module.

---


### 12. [Intervention-Based Self-Supervised Learning: A Causal Probe Paradigm for Remote Photoplethysmography](https://arxiv.org/abs/2605.00882)

**<font color=#1a73e8>作者：</font>** Zhiyi Niu, Xiaoguang Tu, Bo Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote Photoplethysmography (rPPG) enables convenient non-contact physiological measurement. Existing Self-Supervised Learning (SSL) methods commonly fall into a correlation trap: they tend to learn the most dominant periodic signals in the data, such as high-energy motion or illumination noise, rather than the faint, true rPPG signal, leading to poor model generalization. To address this, we propose a new SSL paradigm, Physiological Causal Probing (PCP), which treats the latent rPPG signal as the underlying physical source and the resulting pixel chrominance variations as its visual manifestation. Its core idea is to shift from passive correlation learning to active, precise intervention: it intervenes on the video based on a proposed rPPG hypothesis, and verifies whether the post-intervention changes match physical expectations. We propose the Interv-rPPG framework to implement PCP: an rPPG extractor named PhysMambaFormer hypothesizes the rPPG signal, while a Controllable Physiological Signal Editor conducts precise chrominance-domain interventions on videos based on this hypothesis. Interv-rPPG validates the physical realism of the hypothesis through `Falsifiability via Nulling' and `Axiomatic Equivariance'. Our editor achieves precise editing of the rPPG signal by intervening in the low-frequency chrominance components of the video. Our method improves both in-domain and cross-domain performance on challenging datasets such as VIPL-HR and MMPD. Furthermore, it surpasses the supervised baseline in complex cross-dataset settings, while remaining competitive on clean datasets where the intervention mechanism may introduce slight residual chrominance noise. Extensive experiments, including diagnostic analysis of nuisance sensitivity, demonstrate that the PCP paradigm effectively resists motion and illumination artifacts.

---


### 13. [Towards High Fidelity Face Swapping: A Comprehensive Survey and New Benchmark](https://arxiv.org/abs/2605.00883)

**<font color=#1a73e8>作者：</font>** Qi Li, Weining Wang, Shuangjun Du 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face swapping has witnessed significant progress in recent years, largely driven by advances in deep generative models such as GANs and diffusion this http URL these advances, existing methods remain fragmented across different paradigms, and their evaluation is highly inconsistent due to the lack of standardized datasets and protocols. Moreover, prior surveys primarily focus on broader deepfake generation or detection, leaving face swapping insufficiently studied as a standalone problem. In this paper, we present a comprehensive survey and benchmark for face swapping. We provide a structured review of existing methods, organizing them into five major paradigms and systematically analyzing their design principles, strengths, and limitations. To enable fair and controlled evaluation, we introduce CASIA FaceSwapping, a high-quality benchmark with balanced demographic distributions and explicit attribute variations, and establish standardized protocols to assess the robustness of different face swapping methods. Extensive experiments on representative approaches yield new insights into the performance characteristics and limitations of current techniques. Overall, our work provides a unified perspective and a principled evaluation framework to facilitate the development of more robust and controllable face swapping methods. More results can be found at this https URL.

---


### 14. [LiteVLA-H: Dual-Rate Vision-Language-Action Inference for Onboard Aerial Guidance and Semantic Perception](https://arxiv.org/abs/2605.00884)

**<font color=#1a73e8>作者：</font>** Justn williams, Kishor Datta Gupta, Roy George 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models have shown strong semantic grounding and task generalization in manipulation, but aerial deployment remains difficult because drones require low-latency closed-loop guidance under strict onboard compute and communication constraints. We present LiteVLA-H, a compact 256M-parameter VLA system designed for dual-rate operation on an NVIDIA Jetson AGX Orin: a fast outer-loop guidance mode for short action-token outputs and a slower semantic mode for scene understanding, hazard description, and operator-facing narration. The central empirical observation is that, in this compact edge regime, end-to-end latency is dominated by multimodal pre-fill rather than by the marginal cost of decoding a few extra tokens. This motivates a scheduler that issues reactive action tokens at 50.65,ms (19.74,Hz) while still supporting sentence-level semantic outputs at 149.90--164.57\ms (6.08--6.67,Hz) on the same embedded platform. To specialize the model without collapsing its descriptive competence, we use a knowledge-preserving fine-tuning recipe that mixes reactive flight data, aerial semantic data, and generic caption/VQA supervision. Beyond reporting current latency measurements, we position the system against recent state-of-the-art architectures, including AnywhereVLA, FutureVLA, and ReMem-VLA, showing that the measured action branch reaches a higher edge inference rate under our deployment conditions while retaining periodic semantic awareness.

---


### 15. [Multi-Branch Non-Homogeneous Image Dehazing via Concentration Partitioning and Image Fusion](https://arxiv.org/abs/2605.00885)

**<font color=#1a73e8>作者：</font>** Yingming Zhang, Wuqi Su, Qing Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing single image dehazing methods have demonstrated satisfactory performance on homogeneous thin-haze images; however, they often struggle with non-homogeneous hazy images that exhibit spatially varying haze concentrations and abrupt density transitions across different regions. To address this fundamental limitation, we propose a novel multi-branch deep neural network framework, termed Concentration Partitioning and Image Fusion Network (CPIFNet), which decomposes the challenging non-homogeneous dehazing problem into a set of tractable homogeneous sub-problems. Our key insight is that a single non-homogeneous hazy image can be viewed as a composite of multiple local regions, each exhibiting approximately homogeneous haze characteristics. CPIFNet employs a two-stage architecture consisting of an Image Enhancement Network (IENet) stage and an Image Fusion Network (IFNet) stage. In the first stage, multiple IENet branches are independently trained on homogeneous haze datasets of different concentration levels, producing enhancement models that excel at restoring regions matching their respective haze densities. In the second stage, the IFNet intelligently aggregates the advantageous regions from all enhancement outputs through deep feature stacking and merging, yielding a unified high-quality dehazed result. Furthermore, we introduce a comprehensive loss function incorporating reconstruction, perceptual, structural, and color losses to jointly supervise both stages.

---


### 16. [Selective Attention-Based Network for Robust Infrared Small Target Detection](https://arxiv.org/abs/2605.00886)

**<font color=#1a73e8>作者：</font>** Yingming Zhang, Wuqi Su, Qing Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared small target detection (IRSTD) plays a pivotal role in a broad spectrum of mission-critical applications, including maritime surveillance, military search and rescue, early warning systems, and precision-guided strikes, all of which demand the precise identification of dim, sub-pixel targets amid highly cluttered infrared backgrounds. Despite significant progress driven by deep learning methods, fundamental challenges persist: infrared small targets occupy extremely limited spatial extents (often only a few pixels), exhibit low signal-to-clutter ratios, and are easily confused with structurally complex backgrounds that frequently induce false alarms. Existing encoder-decoder architectures suffer from two key limitations - an information bottleneck in early convolutional stages that undermines fine-grained target perception, and static skip connections that lack the dynamic adaptability required to discriminate between genuine targets and pseudo-target regions. To address these challenges, we propose SANet, a Selective Attention-based Network built upon the classical U-Net framework and augmented with two novel components: (1) a \emph{Dual-path Semantic-aware Module} (DSM) that integrates standard convolutions for local spatial detail preservation with pinwheel-shaped convolutions for expanded, direction-sensitive receptive fields, followed by a Convolutional Block Attention Module (CBAM) for fine-grained spatial-channel feature recalibration; and (2) a \emph{Selective Attention Fusion Module} (SAFM) that replaces conventional static skip connections with a spatially adaptive, learnable weighting mechanism to perform context-aware, cross-scale feature fusion.

---


### 17. [SparseContrast: Dynamic Sparse Attention for Efficient and Accurate Contrastive Learning in Medical Imaging](https://arxiv.org/abs/2605.00887)

**<font color=#1a73e8>作者：</font>** Paarth Prasad, Ruchika Malhotra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose SparseContrast, a new framework that merges dynamic sparse attention with contrastive learning for medical imaging, with a focus on chest X-ray disease detection in low-data settings. Traditional contrastive learning methods rely on dense attention mechanisms, which are computationally expensive and often process redundant regions in medical images. To resolve this, SparseContrast introduces a sparse attention mechanism that selectively concentrates on diagnostically pertinent areas, markedly decreasing computational burden without compromising accuracy. The framework adaptively trims attention maps in the training phase, directed by a compact saliency predictor which concurrently optimizes sparsity and feature quality. This method not only speeds up training and inference by as much as 40% relative to dense attention benchmarks but also boosts diagnostic accuracy by focusing on areas of clinical importance. Moreover, the approach remains indifferent to the selection of backbone architecture, which permits its application to both convolutional and transformer-based models. Experiments show SparseContrast attains comparable or better performance in disease identification tasks with greater efficiency relative to current approaches. The proposed framework delivers a practical approach for implementing contrastive learning in medical imaging settings with limited resources, where computational efficiency and diagnostic accuracy are paramount.

---


### 18. [Selective Correlation Based Knowledge Distillation for Ground Reaction Force Estimation](https://arxiv.org/abs/2605.00888)

**<font color=#1a73e8>作者：</font>** Eun Som Jeon, Jisoo Lee, Huisu Lim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wearable sensor-based human gait analysis holds great promise in healthcare, rehabilitation, clinical diagnosis and monitoring, and sports activities. Specifically, ground reaction force (GRF) provides essential insights into the body's interaction with the ground during movement and is typically measured using instrumented treadmills equipped with force plates. However, such equipment is expensive and restricted to laboratory environments. To enable a more portable solution, wearable insole sensors have been used to measure GRF. These sensors, however, are prone to noise and external interference, which reduces measurement accuracy. Deep learning methodologies could be adopted to address these issues, but they often require significant computing resources to achieve high accuracy, limiting their applicability for real-time analysis on portable devices. To overcome these limitations, we propose Selective Correlation Based Knowledge Distillation (SCKD) for estimating GRF from data collected by insole sensors. Our proposed method utilizes selected features considering temporal characteristics in the process of extracting correlation maps for knowledge transfer, enhancing interpretability and mitigating issues in high dimensional data processing. We demonstrate the effectiveness of the compact models generated by our distillation framework through comparison with existing methods. Various configurations of teacher-student architectures and training approaches are examined based on multiple evaluation criteria, utilizing data collected at different walking speeds and with different window sizes. Experimental results confirm that our approach outperforms existing methods in estimating GRF from wearable insole sensor data. Therefore, our approach offers a reliable and resource-efficient solution for human gait analysis.

---


### 19. [On the explainability of max-plus neural networks](https://arxiv.org/abs/2605.00889)

**<font color=#1a73e8>作者：</font>** Ikhlas Enaieh, Olivier Fercoq, García Ángel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate the explanability properties of the recently proposed linear-min-max neural networks. At initialization, they can be interpreted as k-medoids with the infinity norm as a distance. Then, they are trained using subgradient descent to better fit the data. The model has been shown to be a universal approximator. Yet, we can trace the decision process because a single most activated neuron is responsible for the value of the output. Using this property, we designed a pixel fragility measure that determines whether changes to a single pixel may be responsible to a change in the classification output. Experiments on the PneumoniaMnist dataset show that this explanation for the output of the neural network compares favorably to SHAP and Integrated Gradient.

---


### 20. [Skeleton-Based Posture Classification to Promote Safer Walker-Assisted Gait in Older Adults](https://arxiv.org/abs/2605.00890)

**<font color=#1a73e8>作者：</font>** Sergio D. Sierra M., Monica Sinha, Marcela Múnera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Falls among older adults are a significant public health concern, leading to severe injuries, loss of independence, and increased healthcare costs. This study evaluates the effectiveness of various models, including a Geometric approach, XGBoost, SVM, and several deep learning architectures, in classifying walker usage, standing vs. sitting, and posture for smart walkers used. Geometric and XGBoost were the top performers. XGBoost achieved near-perfect training accuracy in binary classification tasks, with 99.84% for walker choice and 99.69% for standing vs. sitting. For posture classification, Geometric approach attained 89.9% accuracy for 8 postures, and XGBoost obtained 99.24% during training for 17 postures. Deep learning models such as the 4-layer CNN and Encoder-Decoder CNN also demonstrated strong performance in binary classification, with accuracies above 98%. This study underscores the potential of machine learning to enhance human-robot interaction in smart walkers, particularly for fall prevention.

---


### 21. [When To Adapt? Adapting the Model or Data in Federated Medical Imaging](https://arxiv.org/abs/2605.00892)

**<font color=#1a73e8>作者：</font>** Chamani Shiranthika, Parvaneh Saeedi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated learning enables collaborative model training across medical institutions without sharing raw data, but its performance is often limited by domain heterogeneity across clients. Existing approaches to address this challenge fall into two main paradigms: model-side personalization, which adapts model parameters to each client, and data-side harmonization, which reduces inter-client variation at the input level. Despite their widespread use, these strategies have not been systematically compared. In this work, we conduct a comprehensive study across six medical imaging settings-colon polyp, skin lesion, and breast tumor segmentation, and tuberculosis CXR, brain tumor, and breast tumor classification-covering diverse types of domain shift. We evaluate a broad set of state-of-the-art harmonization and personalization methods under a unified framework. Our results reveal a conditional trade-off driven by the nature of heterogeneity: harmonization is more effective when variation is primarily appearance-based (e.g., CXR classification), while personalization performs better when differences are structural (e.g., colon polyp segmentation). When inter-client variation is limited, both strategies perform similarly. These findings demonstrate that the effectiveness of adaptation in federated medical imaging depends on the type and magnitude of domain shift rather than the strategy alone. We provide practical guidelines for selecting between harmonization and personalization and highlight directions for future hybrid approaches that combine both paradigms. Code is available at this https URL.

---


### 22. [Retrieval-Guided Generation for Safer Histopathology Image Captioning](https://arxiv.org/abs/2605.00893)

**<font color=#1a73e8>作者：</font>** Md. Enamul Hoq, Wataru Uegami, Saghir Alfasly 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative vision-language models can produce fluent medical image captions but remain prone to hallucination, over-specific diagnostic claims, and factual inconsistency-serious issues in pathology. We investigate retrieval-guided generation (RGG) as a safer alternative, where captions are formed by summarizing expert text from visually similar cases rather than generated de novo. On the ARCH histopathology dataset, RGG improves semantic alignment with ground truth, achieving cosine similarity of $\approx$0.60 versus $\approx$0.47 from MedGemma, with non-overlapping confidence intervals indicating a robust gain. A pathologist-led qualitative review shows better preservation of morphology-relevant terminology and fewer unsupported diagnoses, while revealing failure modes such as concept mixing and inherited over-specific labeling. Overall, retrieval-guided captioning offers a more transparent and reliable approach with clearer opportunities for auditing than fully generative methods.

---


### 23. [Dino-NestedUNet: Unlocking Foundation Vision Encoders for Pathology Tumor Bulk Segmentation via Dense Decoding](https://arxiv.org/abs/2605.00894)

**<font color=#1a73e8>作者：</font>** Tianyang Wang, Ziyu Su, Abdul Rehman Akbar 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models (VFMs), such as DINOv3, provide rich semantic representations that are promising for computational pathology. However, many current adaptations pair frozen VFMs with lightweight decoders, creating a capacity mismatch that often limits boundary fidelity for infiltrative tumor bulk segmentation. This paper presents Dino-NestedUNet, a framework that couples a pre-trained DINOv3 encoder with a Nested Dense Decoder. Instead of sparse skip connections and linear upsampling, the proposed decoder forms a dense grid of intermediate pathways to enable continuous feature reuse and multi-scale recalibration, aligning high-level semantics with low-level morphological textures during reconstruction. We evaluate Dino-NestedUNet on three histopathology cohorts (multi-center CHTN, institutional OSU, and CAMELYON16) and observe consistent improvements over UNet++ and standard Dino-UNet variants, particularly under cross-domain shift. To further assess external generalization, we perform zero-shot evaluation by training on CHTN and directly testing on unseen TIGER WSIBULK and OSU CRC cohorts without fine-tuning. These results suggest that dense decoding is a key ingredient for unlocking foundation encoders in boundary-sensitive pathology segmentation.

---


### 24. [When Less Is More: Simplicity Beats Complexity for Physics-Constrained InSAR Phase Unwrapping](https://arxiv.org/abs/2605.00896)

**<font color=#1a73e8>作者：</font>** Prabhjot Singh, Manmeet Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Operational phase unwrapping is the primary computational bottleneck in InSAR-based volcanic and seismic monitoring. We challenge the industry trend of adopting high-complexity computer vision architectures, such as attention mechanisms, without validating their suitability for physics-constrained geophysical regression. We present the first large-scale architectural ablation study on a global LiCSAR benchmark (20 frames, 39,724 patches, 651M pixels). Our results reveal a significant "complexity penalty": a vanilla U-Net (7.76M parameters) achieves $R^2=0.834$ and RMSE $= 1.01$ cm, outperforming 11.37M-parameter attention-based models by 34% in $R^2$ and 51% in RMSE. Power Spectral Density (PSD) analysis provides the physical justification: while attention excels at capturing sharp semantic edges in natural images, it injects unphysical high-frequency artifacts ($>0.3$ cycles/pixel) into geophysical fields, violating the fundamental smoothness constraints of elastic surface deformation. With a 2.92ms inference latency (a $2.5\times$ speedup), the vanilla U-Net is the only candidate to comfortably meet the sub-100ms requirement for operational early-warning systems. This work bridges the "publication-to-practice" gap by proving that convolutional locality outperforms modern complexity for smooth-field regression, advocating for physics-informed simplicity in ML4RS. Code available at this https URL

---


### 25. [LatentDiff: Scaling Semantic Dataset Comparison to Millions of Images](https://arxiv.org/abs/2605.00899)

**<font color=#1a73e8>作者：</font>** James Flora, Kowshik Thopalli, Akshay R. Kulkarni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present LatentDiff, a scalable framework for semantic dataset comparison that operates directly in the latent space of pretrained vision encoders. By combining sparse autoencoder-based divergence testing with density ratio estimation, LatentDiff identifies interpretable semantic differences between datasets at a fraction of the computational cost of caption-based alternatives. We also introduce Noisy-Diff, a benchmark capturing realistic sparse distribution shifts that cause existing methods to struggle. Experiments demonstrate that LatentDiff achieves superior accuracy while remaining robust to settings where an extremely small fraction of images (from 5% to <1% ) differ semantically.

---


### 26. [RA-CMF: Region-Adaptive Conditional MeanFlow for CT Image Reconstruction](https://arxiv.org/abs/2605.00901)

**<font color=#1a73e8>作者：</font>** Md Shifatul Ahsan Apurba, Md Selim, Jin Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The use of CT imaging is important for screening, diagnosis, therapy planning, and prognosis of lung cancers. Unfortunately, due to differences in imaging protocols and scanner models, CT images acquired by different means may show large differences in noise statistics, contrast, and texture. In this study, we develop a novel conditional MeanFlow pipeline for CT image reconstruction. We introduce a conditional MeanFlow network that models the enhancement trajectory by predicting image-conditioned flow fields given intermediate image states. The image enhancement network is trained with a MeanFlow consistency loss along with the image reconstruction loss. In order to provide an adaptive refinement process in terms of spatial location of enhancements, we integrate a regional reinforcement learning-driven policy network into our approach. The policy network receives information about the MeanFlow rollouts and provides predictions in terms of tile-wise refinement budgets, stopping criteria, and total budget allocation of enhancement processes. Our policy network is trained through reinforcement learning in a policy gradient framework, where the goal of the training reward is to maximize improvement of enhancements while minimizing unnecessary computations and avoiding instabilities. In this way, our approach combines conditional flow-based enhancement with reinforcement learning-based spatial enhancement control. This allows our approach to focus more attention on enhancing difficult areas while stabilizing areas already showing sufficient quality. Our results show high accuracy in the tumor ROI, with the average radiomic feature CCC being 0.96, an average PSNR of 31.30 $\pm$ 4.16, and average SSIM of 0.94 $\pm$ 0.07. Moreover, there is an improvement in the overall quality of images, with an average PSNR of 34.23 $\pm$ 1.71 and average SSIM of 0.95 $\pm$ 0.01.

---


### 27. [A Light Weight Multi-Features-View Convolution Neural Network For Plant Disease Identification](https://arxiv.org/abs/2605.00903)

**<font color=#1a73e8>作者：</font>** Muhammad Kaleem Ullah Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agriculture is a key sector of the economies of developing countries. It serves as a primary source of income and employment for rural populations. However, each year, a large portion of crops is wasted because of pests and diseases. Well-timed prediction of plant diseases is crucial to sustainable, high-quality agricultural production. Detection of plant diseases through conventional methods is both labour-intensive and time-consuming. Researchers have developed image classification based automated techniques for this purpose. Most accurate methods are based on deep convolutional neural networks, which are computationally intensive, with many layers and millions of trainable parameters. In resource-constrained settings, especially in rural areas, it is difficult to deploy deep convolutional neural network models for efficient plant disease identification. To address these issues, an efficient and light-weight Multi-View Convolutional Neural Network is proposed. These additional features aid the proposed model to identify the plant diseases accurately and efficiently with less number of parameters. The proposed model is tested on a benchmark Plantvillage dataset and achieves an improvement of $ 2.9\%$ in classification accuracy compared to the baseline convolutional neural network model, which was trained only on Red, Green, and Blue (RGB) plant images. Compared with state-of-the-art deep convolutional neural network models, the proposed model is less computationally expensive and achieves comparable accuracy for plant disease identification on the PlantVillage dataset.

---


### 28. [Robustness of Transformer-Based Fluence Map Prediction Under Clinically Realistic Perturbations](https://arxiv.org/abs/2605.00904)

**<font color=#1a73e8>作者：</font>** Ujunwa Mgboh, Rafi Ibn Sultan, Joshua Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning-based fluence map prediction offers a fast alternative to iterative inverse planning in intensity-modulated radiation therapy (IMRT), but its robustness under realistic distribution shifts remains unclear. We study a two-stage transformer pipeline that maps anatomy (CT and contours) to dose and then to beamlet fluence maps. We compare fluence-stage transformer backbones with hierarchical, global, and hybrid attention, trained with a physics-informed loss enforcing energy consistency. Robustness is evaluated under geometric perturbations, radiometric noise, reduced training data, and domain shifts using a prostate IMRT dataset, with additional evaluation of the dose stage on public datasets. Results show smooth degradation under moderate perturbations but sharp failures under severe rotations and noise. Hierarchical transformers (e.g., SwinUNETR) exhibit slower growth in upper-quartile energy error, indicating improved robustness. We further show that SSIM alone fails to capture clinically relevant errors, highlighting the need for physics-informed evaluation.

---


### 29. [DIAGRAMS: A Review Framework for Reasoning-Level Attribution in Diagram QA](https://arxiv.org/abs/2605.00905)

**<font color=#1a73e8>作者：</font>** Anirudh Iyengar Kaniyar Narayana Iyengar, Tampu Ravi Kumar, Manan Suri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diagram question answering (Diagram QA) requires reasoning-level attribution that links each question-answer pair to all visual regions needed to derive the answer, rather than only the region containing the final response. Creating such structured evidence across diagrams, charts, maps, circuits, and infographics is time-consuming, and existing annotation tools tightly couple their interfaces to dataset-specific formats. We present DIAGRAMS, a lightweight, schema-driven review framework that decouples interface logic from dataset-specific JSON structures through an internal meta-schema and dataset adapters. Given an image and QA pair with optional candidate regions, the system performs QA-conditioned evidence selection and proposes the regions required for reasoning. When QA pairs or candidate regions are missing, it generates them and supports human verification and refinement. Across six Diagram QA datasets, model-suggested evidence achieves 85.39% precision and 75.30% recall against reviewer-final selections (micro-averaged). These results indicate that the review-first framework reduces manual region creation while maintaining high agreement with final reasoning-level attributions. We release a public demo and installable package to support dataset auditing, grounded supervision creation, and grounded evaluation.

---


### 30. [Comparative Evaluation of Convolutional and Transformer-Based Detectors for Automated Weed Detection in Precision Agriculture](https://arxiv.org/abs/2605.00908)

**<font color=#1a73e8>作者：</font>** Alcides Toledo Espinosa, Gerardo Antonio Álvarez Hernández, Ángel Eduardo Zamora-Suárez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a comparative evaluation of convolutional and transformer-based object detection architectures for early weed detection in realistic scenarios. Representative models from each paradigm are considered, including YOLOv26-nano, a recent variant of the YOLO family, and transformer-based approaches such as RTDETR and RF-DETR. Experiments were conducted on the GROUNDBASED_ WEED dataset, allowing performance to be evaluated in terms of detection accuracy and computational efficiency using metrics such as precision, recall, average precision, and inference speed. The results highlight a clear trade-off between efficiency and contextual modeling: CNN-based detectors achieve high performance at a lower computational cost, while transformer-based approaches offer better global context capture at the expense of higher resource demands. These results provide practical criteria for model selection in precision agriculture applications.

---


### 31. [Accelerating battery research with an AI interface between FINALES and Kadi4Mat](https://arxiv.org/abs/2605.00909)

**<font color=#1a73e8>作者：</font>** Giovanna Tosato, Leon Merker, Monika Vogler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The time-consuming formation process critically impacts the longevity of sodium-ion coin cells and End Of Life (EOL) performance. This study aims to optimize formation protocols for duration efficiency, targeting high-performance outcomes while minimizing the number of experiments to reduce resource consumption and accelerate discovery. Specifically, we consider two potentially competing objectives: minimizing formation time and maximizing EOL performance. Beyond this application focus, we also present a methodological contribution: a framework designed to enable interoperability between the FINALES and Kadi RDM ecosystems, which we employ to tackle our optimization problem. In this setup, the FINALES framework orchestrates experiment planning and execution on the POLiS MAP, while an active-learning agent implemented within Kadi4Mat guides experiment selection, using multi-objective batched Bayesian optimization to efficiently explore the parameter space. This interoperability enhancement enables coordinated, distributed collaboration across automated systems and human-operated workflows, bridging multiple research centers. Using this approach, we iteratively explore the trade-off between formation time and EOL performance and identify candidate solutions approximating the Pareto front. The resulting workflow demonstrates the capability of interoperable infrastructures to facilitate data-driven optimization in battery research, and establishes a transferable framework applicable to diverse materials science and engineering optimization tasks.

---


### 32. [Object-Level Explanations for Image Geolocation Models: a GeoGuessr use-case](https://arxiv.org/abs/2605.00912)

**<font color=#1a73e8>作者：</font>** Emilie Durrieu, Christophe Hurter, Philippe Muller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When humans play geolocation games such as GeoGuessr, they rely on concrete visual cues, such as road markings, vegetation, or architectural details, to infer where an image was captured. Whether image geolocation models rely on similar object-level evidence remains difficult to determine, as attribution methods like Grad-CAM typically highlight diffuse regions rather than coherent visual entities, making it difficult to link model predictions to specific objects or perceptible patterns. In this work, we propose an object-centric analysis pipeline to investigate the visual evidence used by geolocation models. Starting from attribution maps, we extract salient regions and segment them into object-like elements. We evaluate their predictive relevance through deletion and insertion tests, comparing attributionguided crops to randomly selected regions with similar coverage. Experiments on a three-country benchmark show that attribution-guided crops consistently retain more information for the model's prediction than random crops. These results suggest that attribution maps can be decomposed into interpretable, perceptible elements, providing a step toward object-level analysis of geolocation models.

---


### 33. [Rethink MAE with Linear Time-Invariant Dynamics](https://arxiv.org/abs/2605.00915)

**<font color=#1a73e8>作者：</font>** Zice Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Standard representation probing for visual models relies on mathematically permutation-invariant operations like Global Average Pooling (GAP) or CLS tokens, treating patch representations as an unstructured bag-of-words. We challenge this paradigm by demonstrating that token order is a critical, exploitable dimension in frozen visual representations (e.g., MAE, BEiT, DINOv2, and ViT as CLS-ablation extreme). We propose SSMProbe, a probing framework driven by a State Space Model (SSM). Operating as discrete Linear Time-Invariant (LTI) dynamical systems, SSMs act as permutation-sensitive probes where sequence order strictly dictates the final state due to inherent memory decay. Formulating token ordering as an information scheduling problem, we compare fixed scan heuristics against a differentiable soft permutation (Sinkhorn-based) learned from downstream supervision. Evaluations on standard and fine-grained classification benchmarks reveal a striking order gap: while fixed scans fail dramatically on highly localized patch features, our learned soft permutation successfully extracts highly competitive performance from otherwise heavily localized patch sequences. We find that pre-training objectives fundamentally shape token structure: DINOv2 concentrates global semantics in optimized CLS tokens leaving patches hyperspecialized, pure MAE preserves distributed representations with heterogeneous patch informativeness, and ViT represents a supervised CLS-dominated extreme. BEiT occupies middle ground. This heterogeneity is order-dependent -- meaning the SSM probe's performance depends critically on which tokens are placed at which temporal positions -- and is not merely a topological property of the spatial grid. SSMProbe's learned routing effectively discovers and exploits this heterogeneity, offering a powerful new diagnostic lens for visual representation analysis.

---


### 34. [SAMamba3D: adapting Segment Anything for generalizable 3D segmentation of multiphase pore-scale images](https://arxiv.org/abs/2605.00916)

**<font color=#1a73e8>作者：</font>** Rui Zhang, Xianzhi Song, Linqi Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable segmentation of multiphase pore-scale X-ray images of rocks is necessary to quantify fluid saturation, connectivity, and interfacial geometry. However, current 3D segmentation methods are typically dataset-specific, requiring retraining or extensive fine-tuning whenever rock type, fluid pattern, scanner, or acquisition conditions change. Foundation models such as the Segment Anything Model (SAM) provide strong 2D boundary priors, but they are not directly applicable to 3D data.
We present SAMamba3D, a parameter-efficient framework that adapts a largely frozen SAM encoder to generalizable 3D pore-scale segmentation by coupling it with Mamba-based volumetric context modeling and progressive cross-scale feature interaction. For sandstone and carbonate datasets, with different fluids, wettability, and scanning conditions, SAMamba3D matches or outperforms current 3D baselines while reducing the need for case-specific retraining. The resulting segmented images preserve physically meaningful descriptors, including fluid saturation, connectivity, and interface morphology, enabling more reliable and rapid analysis of large 3D multiphase images.

---


### 35. [Linking spatial biology and clinical histology via Haiku](https://arxiv.org/abs/2605.00925)

**<font color=#1a73e8>作者：</font>** Yan Cui, Jacob S. Leiby, Wenhui Lei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrating molecular, morphological, and clinical data is essential for basic and translational biomedical research, yet systematic frameworks for jointly modeling these modalities remain limited. Here we present Haiku, a tri-modal contrastive learning model trained on multiplexed immunofluorescence (mIF). It comprises 26.7 million spatial proteomics patches from 3,218 tissue sections across 1,606 patients spanning 11 organ types, with matched hematoxylin and eosin (H&E) histology and clinical metadata aligned in a shared embedding space. Haiku enables three-way cross-modal retrieval, improves downstream classification and clinical prediction tasks over unimodal baselines, and supports zero-shot biomarker inference through fusion retrieval conditioned on clinical metadata-only text descriptions. Across tasks, Haiku outperforms competing approaches, achieving cross-modal retrieval (Recall@50 up to 0.611 versus near-zero baseline), survival prediction (C-index 0.737, +7.91% relative improvement), and zero-shot biomarker inference (mean Pearson correlation 0.718 across 52 biomarkers). Furthermore, we introduce a counterfactual prediction framework in which modifying only clinical metadata while fixing tissue morphology surfaces niche-specific molecular shifts associated with breast cancer stage progression and lung cancer survival outcomes. In a lung adenocarcinoma case study, the counterfactual analysis recovers niche-specific shifts characterized by increased CD8 and granzyme B, reduced PD-L1, and decreased Ki67, broadly consistent with patterns reported for favorable outcomes. We present these counterfactual results as exploratory, hypothesis-generating signals rather than mechanistic claims. These capabilities demonstrate that tri-modal alignment via Haiku enables integrative analysis of spatial biology, bridging molecular measurements with clinical context for biological exploration.

---


### 36. [A Review of the Receiver Operating Characteristic Curve and a Proof About the Area Beneath It](https://arxiv.org/abs/2605.00926)

**<font color=#1a73e8>作者：</font>** Steven Redolfi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Receiver Operating Characteristic (ROC) curve of a binary classifier has often been utilized to measure the performance of the classifier. The area beneath this curve is used in particular because of its quoted probabilistic interpretation as being equal to the probability that the classifier will rank a random positive observation above a random negative observation. This paper formalizes this claim, produces a bound on how far away from the truth it is if a hypothesis is not met, and gives a small literature review of the ROC curve.

---


### 37. [PhaseNet++: Phase-Aware Frequency-Domain Anomaly Detection for Industrial Control Systems via Phase Coherence Graphs](https://arxiv.org/abs/2605.00929)

**<font color=#1a73e8>作者：</font>** Raviteja Bommireddy, Varshith Bandaru, Lohith Pakala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series anomaly detection in ICS has attracted growing attention due to the increasing threat of cyber-physical attacks on critical infrastructure. State-of-the-art methods model inter-sensor relationships from raw time-domain amplitude values, using graph neural networks, Transformers. However, these methods discard the phase spectrum produced by time frequency transformations, We argue that phase information constitutes a complementary and previously overlooked detection modality for ICS anomaly detection. We present PhaseNet++, a frequency-domain autoencoder that operates on the Short-Time Fourier Transform (STFT) of sliding sensor windows, retaining both magnitude and phase spectra. A Phase Coherence Index (PCI), inspired by the Phase Locking Value from neuroscience, summarizes pairwise phase consistency across frequency bins into a continuous adjacency matrix. This matrix guides a graph attention network that propagates information preferentially among phase-synchronized sensors. A sensor-token Transformer encoder captures system-wide structure, and a dual-head decoder reconstructs magnitude and phase jointly via circular and coherence-aware objectives. Evaluated on the Secure Water Treatment (SWaT) benchmark, PhaseNet++ achieves an F1-score of 90.98%, ROC-AUC of 95.66%, and average precision of 91.51%. Ablation studies show that the phase-aware front-end and PCI graph module together add only 264,816 parameters, demonstrating that the phase inductive bias is lightweight. While the absolute F1-score is second best than that of all recent raw-value methods evaluated under different protocols, we position this work as the first systematic study of phase-domain anomaly detection for ICS.

---


### 38. [Hierarchical Federated Learning for Networked AI: From Communication Saving to Architecture-Aware Design](https://arxiv.org/abs/2605.00931)

**<font color=#1a73e8>作者：</font>** Seyed Mohammad Azimi-Abarghouyi, Mehdi Bennis, Leandros Tassiulas  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is fundamentally a distributed optimization problem executed by communicating agents with local data, local computation, and partial system visibility. Once FL is viewed through that lens, hierarchy is not merely a scalability mechanism. It becomes the natural place to rethink how distributed optimization should be organized over real multi-tier networks. This article argues that hierarchical federated learning (HFL) should move beyond its common framing as a communication-saving protocol and instead be viewed as an architecture-aware design framework for networked AI. The framework is organized around three coupled design axes: architectural parameters, layer-wise optimization decomposition, and layer-wise communication realization. The first axis determines the coordination geometry of learning through hierarchy depth, layer asymmetry, and layered connectivity. The second determines how the global FL objective is decomposed across layers and highlights modular multi-layer optimization as a major opportunity beyond one dominant method everywhere. The third determines how the distributed optimization is physically realized under heterogeneous communication regimes, from interference-limited lower tiers to reliable upper tiers. A central message is that, in HFL, convergence becomes architecture-dependent: it is directly shaped by the chosen hierarchy, the assigned optimization roles, and the communication mechanisms that connect them. We develop this viewpoint using large-scale wireless edge intelligence as a flagship networked AI setting, then provide a comparative perspective on flat FL, two-tier HFL, and deep HFL together with a regime-oriented design map. The resulting perspective positions HFL as a practical methodology for designing future networked AI systems.

---


### 39. [CGM-JEPA: Learning Consistent Continuous Glucose Monitor Representations via Predictive Self-Supervised Pretraining](https://arxiv.org/abs/2605.00933)

**<font color=#1a73e8>作者：</font>** Hada Melino Muhammad, Zechen Li, Flora Salim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous Glucose Monitoring (CGM) can detect early metabolic subphenotypes (insulin resistance, IR; $\beta$-cell dysfunction), but population-scale deployment faces two coupled problems. First, the same physiological state appears through multiple views (CGM time series, venous OGTT, Glucodensity summaries), so single-view representations fail to transfer when deployment shifts the modality or setting. Second, baselines perform inconsistently across these shifts. Both problems point to one remedy: representations that abstract away from any single view to capture higher-level temporal and distributional structure. We propose CGM-JEPA, a self-supervised pretraining framework which predicts masked latent representations rather than raw values, yielding abstraction that transfers across modalities. X-CGM-JEPA adds a masked Glucodensity cross-view objective for complementary distributional information. We pretrain on $\sim$389k unlabeled CGM readings from 228 subjects and evaluate on two clinical cohorts ($N=27$ and $N=17$ public-release subsets) across three regimes (cohort generalization, venous-to-CGM transfer, home CGM) under 20-iteration $\times$ 2-fold cross-validation. X-CGM-JEPA ranks first or second on AUROC for both endpoints across all three regimes while no baseline does, exceeding the strongest baseline by up to $+6.5$ pp in cohort generalization and $+3.6$ pp in venous-to-CGM transfer (paired Wilcoxon, $p<0.001$). Under modality shift, it matches mean AUROC while redistributing toward weaker subgroups (ethnicity AUROC gap shrinks 25-54%); on sparse in-domain venous data, the distributional view lifts label-aware clustering (ARI $+39\%$, NMI $+40\%$). Code and weights: this https URL

---


### 40. [Structured Analytic Coherent Point Drift for Non-Rigid Point Set Registration](https://arxiv.org/abs/2605.00934)

**<font color=#1a73e8>作者：</font>** Wei Feng, Haiyong Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Analytic-CPD, a structured analytic variant of coherent point drift for non-rigid point set registration. The method retains the CPD posterior correspondence layer, but replaces the point-indexed Gaussian-kernel displacement-field M-step with a finite-dimensional structured analytic mapping estimator. Posterior probabilities from the Gaussian mixture model are condensed through a barycentric identity into weighted soft target points, converting the CPD pairwise soft-correspondence objective into a weighted analytic fitting problem. The deformation is represented by a truncated multivariate Taylor mapping of a vector-valued function, so the number of deformation parameters is controlled by the ambient dimension and the analytic order rather than by an M-by-M kernel system over the moving points. A degree-continuation strategy is further introduced to stabilize large-deformation registration by progressively activating higher-order analytic modes. Experiments on two-dimensional analytic deformations and three-dimensional smooth non-analytic deformations show that Analytic-CPD achieves lower final errors and faster convergence than standard CPD in representative large-deformation settings. The results suggest that CPD-style probabilistic correspondences and structured analytic mappings provide a compact and interpretable alternative to kernel-based non-rigid registration. Code is available at this https URL.

---


### 41. [Watch Your Step: Information Injection in Diffusion Models via Shadow Timestep Embedding](https://arxiv.org/abs/2605.00935)

**<font color=#1a73e8>作者：</font>** An Huang, Junggab Son, Zuobin Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become the foundation of modern generative systems, with most research focusing primarily on improving generation efficiency and output quality. The timestep embedding component is a crucial part of the diffusion pipeline, which provides a temporal conditioning signal to the denoising network, enabling it to adapt its predictions across different noise levels throughout the process. Despite their potential to contain substantial information, timestep embeddings remain underexplored in current research, especially for security risks and reliable provenance. To fill this gap, we introduce Shadow Timestep Embedding (STE), a novel mechanism that investigates the underutilized temporal space for malicious information injection into diffusion models. In particular, when zooming in on the timestep embedding space, we find that different timesteps exhibit distinct representational capabilities that can encode side-channel information. Moreover, such encoded information can be utilized for attack and defense purposes through the scheduler interface. We present a theoretical analysis of timestep embeddings as position-encoding mappings and derive a mutual coherence evaluation that explains the separability of disjoint timestep intervals. Our findings reveal the diffusion model's timestep as a powerful side channel for carrying dedicated information, motivating new directions for adversarial generative modeling by understanding the temporal dimension.

---


### 42. [EventADL: Open-Box Anomaly Detection and Localization Framework for Events in Cloud-Based Service Systems](https://arxiv.org/abs/2605.00936)

**<font color=#1a73e8>作者：</font>** Luan Pham, Victor Nicolet, Joey Dodds 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection and localization (ADL) is critical for maintaining reliability and availability in cloud systems. Recent ADL developments focus on metric and log data, leaving event data unexplored. To address this gap, we propose EventADL, the first open-box event-based ADL framework for cloud-based service systems. To motivate the design of our framework, we conduct a systematic analysis on 520 real-world incidents, and provide insights into how anomalies and their root causes manifest through event data. EventADL has three phases: offline training, online anomaly detection, and root cause localization. During the training phase, EventADL first learns Event Semantic Patterns (ESPs), which capture normal interactions between system entities using historical event data, and then learns Event Frequency Patterns (EFPs), which capture the normal frequency of known ESPs. In the online anomaly detection phase, any data in the event stream that deviates significantly from either pattern is identified as anomalous. For localization, EventADL constructs an Intervention Graph that models the relationships between recent system interactions and the detected anomalies for automatic root cause localization. The framework is designed to operate efficiently with unlabeled data and to produce interpretable anomalies with their corresponding root causes. Our evaluation on three real cloud service systems and two real-world incidents demonstrates that EventADL outperforms existing methods, achieving F1-scores of at least 90% for anomaly detection and 100% top-3 accuracy in root cause localization.

---


### 43. [Fusing Urban Structure and Semantics: A Conditional Diffusion Model for Cross-City OD Matrix Generation](https://arxiv.org/abs/2605.00938)

**<font color=#1a73e8>作者：</font>** Bin Chen, Zhuoya Meng, Fang Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate modeling of commuting flows is important for urban governance, traffic planning, and resource allocation. However, the combined influence of individual intentions, geographic constraints, and social dynamics leads to considerable heterogeneity in commuting patterns, making it difficult to develop generation models that generalize across cities. To address this issue, we propose SEDAN, a Structure-Enhanced Diffusion model conditioned on Attributed Nodes for generalizable OD matrix generation. SEDAN models a city as an attributed graph. Each region is treated as a node with demographic and point-of-interest features, and commuting flows are modeled as weighted edges. Adjacency and distance matrices are incorporated to characterize spatial structure. Based on this representation, we design a fusion mechanism within SEDAN to jointly model semantic information and spatial information. Regional semantic attributes are used to model latent travel demand through graph-transformer-based node interactions, while spatial structure is injected into the generation process as explicit constraints. The adjacency matrix guides attention weights to strengthen interactions between neighboring regions. Meanwhile, the distance matrix serves as a diffusion condition to capture spatial proximity and travel impedance. The fusion of urban semantics and spatial constraints enables SEDAN to generate OD matrices that are both behaviorally plausible and geographically coherent. Experiments on real-world OD datasets from U.S. cities show that SEDAN achieves a 7.38\% improvement in RMSE over the state-of-the-art baseline, WEDAN. It also remains robust across heterogeneous urban scenarios and varying structural patterns. Our work provides an effective and generalizable solution for commuting OD matrix generation. The code is available at this https URL.

---


### 44. [From Flat Facts to Sharp Hallucinations: Detecting Stubborn Errors via Gradient Sensitivity](https://arxiv.org/abs/2605.00939)

**<font color=#1a73e8>作者：</font>** Yee Zhing Liew, Andrew Huey Ping Tan, Anwar P.P Abdul Majeed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traditional hallucination detection fails on "Stubborn Hallucinations" -- errors where LLMs are confidently wrong. We propose a geometric solution: Embedding-Perturbed Gradient Sensitivity (EPGS). We hypothesize that while robust facts reside in flat minima, stubborn hallucinations sit in sharp minima, supported by brittle memorization. EPGS detects this sharpness by perturbing input embeddings with Gaussian noise and measuring the resulting spike in gradient magnitude. This acts as an efficient proxy for the Hessian spectrum, differentiating stable knowledge from unstable memorization. Our experiments show that EPGS significantly outperforms entropy-based and representation-based baselines, providing a robust signal for detecting high-confidence factual errors.

---


### 45. [Interpretable experiential learning based on state history and global feedback](https://arxiv.org/abs/2605.00940)

**<font color=#1a73e8>作者：</font>** Anton Kolonin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A new interpretable experiential learning model based on state history and global feedback is presented. It is capable of learning a behavioral model represented by a transition graph between sets of states, with transitions attributed with utility and evidence count. This model is expected to be suitable for solving reinforcement learning problem in resource-constrained environments. The model was thoroughly evaluated on the OpenAI Gym Atari Breakout benchmark, demonstrating performance comparable to some known neural network-based solutions.

---


### 46. [Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching](https://arxiv.org/abs/2605.00941)

**<font color=#1a73e8>作者：</font>** Jiarui Xing, Song Wang, Jian Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching has become a leading framework for generative modeling, but quantifying the uncertainty of its samples remains an open problem. Existing approaches retrain the model with auxiliary variance heads, maintain costly ensembles, or propagate approximate covariance through many integration steps, trading off training cost, inference cost, or accuracy. We show that none of these trade-offs is necessary. We prove that, for any pre-trained flow matching velocity field, the trace of the posterior covariance over the clean data given the current state equals, in closed form, the divergence of the velocity field, up to a known time-dependent prefactor and an additive constant. We call this the \emph{divergence-uncertainty identity} for flow matching. The matrix-level form of the identity is similarly closed-form, depending solely on the velocity Jacobian. Because the identity is exact and post-hoc, it is computable on any pre-trained flow matching model, with no retraining and no architectural modification. For one-step generators such as MeanFlow, the same identity yields the exact end-to-end generation uncertainty in a single forward pass, eliminating the multi-step variance propagation required by all prior methods. Experiments on MNIST confirm that the resulting per-pixel uncertainty maps are semantically meaningful, concentrating on digit boundaries where inter-sample variation is highest, and that the scalar uncertainty score tracks actual prediction error, all at roughly 10,000$\times$ less total compute than ensembling or Monte Carlo dropout.

---


### 47. [Breaking the Communication-Accuracy Trade-off: A Sparsified Information Diffusion Framework for Multi-Agent Collaborative Perception](https://arxiv.org/abs/2605.00946)

**<font color=#1a73e8>作者：</font>** Jirong Zha, Chenyu Zhao, Nan Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The growing relevance of multi-agent systems has drawn increasing focus on communication-efficient filters for collaborative perception to alleviate the system's communication burden. While the event-triggered (ET) mechanism can improve communication efficiency in collaborative state estimation, an inevitable trade-off exists between estimation accuracy and communication cost in ET filters. This paper proposes a fast and accurate ET diffusion-based filter for real-time multi-agent collaborative target tracking, aiming to reduce the system's data transmission without compromise in tracking performance. The proposed filter achieves improved tracking accuracy, reduced data transmission, and accelerated convergence using an error-minimized ET cubature information filter (CIF) for local estimation, and a correlation-aware diffusion strategy for global fusion. The experimental results confirm the scalability of the proposed EDC-CIF algorithm and demonstrate its efficacy in simultaneously reducing estimation error and computation time while significantly enhancing communication efficiency.

---


### 48. [Graph Rewiring in GNNs to Mitigate Over-Squashing and Over-Smoothing: A Survey](https://arxiv.org/abs/2605.00951)

**<font color=#1a73e8>作者：</font>** Hugo Attali, Nathalie Pernelle, Davide Buscaldi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks are powerful models for learning from graph-structured data, yet their effectiveness is often limited by two critical challenges: over-squashing, where information from distant nodes is excessively compressed, and over-smoothing, where repeated propagation makes node representations indistinguishable. Both phenomena stem from the interaction between message passing and the input topology, ultimately degrading information flow and limiting the performance of GNNs. In this survey, we examine graph rewiring techniques, a class of methods designed to modify the graph topology to enhance information propagation in GNNs. We provide a comprehensive review of state-of-the-art rewiring approaches, delving into their theoretical underpinnings, practical implementations, and performance trade-offs.

---


### 49. [Energy-Based Constraint Networks: Learning Structural Coherence Across Modalities](https://arxiv.org/abs/2605.00960)

**<font color=#1a73e8>作者：</font>** Chirag Shinde  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce energy-based constraint networks -- a modality-agnostic architecture that learns structural coherence from contrastive pairs. The system processes frozen encoder embeddings through a state-space model with dual-head attention, producing a scalar energy measuring structural consistency alongside per-position energy scores that localize violations. Multiple independently trained branches detect different violation types and compose at inference without interference.
We demonstrate the framework in two domains. In text, the system achieves 93.4% accuracy on trained corruption types and 87.2% on 9 unseen types, using frozen BERT and 7.4M trainable parameters. In vision, the same architecture achieves competitive deepfake detection: 0.959 AUC on FaceForensics++ Deepfakes and 0.870 on Celeb-DF without any Celeb-DF training data, using frozen DINOv2 and 3.6M parameters per branch.
The framework supports flexible training: branches learn from designer-specified corruptions, real-world paired data, or both. Composable branches require representation compatibility -- a finding validated through extensive experimentation where five incompatible approaches failed before the compatible one succeeded. The architecture is encoder-agnostic and domain-agnostic: changing the domain requires only new corruption strategies; changing the encoder requires only a new input projection layer. To our knowledge, this is the first architecture to learn within-modality structural coherence as an explicit energy landscape with per-position decomposition, and to demonstrate that the same architecture transfers across modalities via corruption respecification alone.

---


### 50. [Composable Post-Quantum Security for FADEC-Coupled Dual-Spool Turbofan Cyber-Physical Systems](https://arxiv.org/abs/2605.00961)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Taylan Alpay  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We develop a unified mathematical formulation for post-quantum authenticated telemetry and actuation in FADEC-coupled dual-spool turbofan cyber-physical systems. The formulation integrates lattice-based key establishment under LWE/SIS-style assumptions, PUF-derived attestation entropy, authenticated encryption, radar-altimeter integrity, avionics-bus timing, and Kalman residual monitoring in a stochastic hybrid model. Within this model, plant evolution, communication latency, leakage, adversarial channel quality, and cryptographic state evolve under a common filtration. We show that channel uncertainty tightens admissible key-renewal periods, that ciphertext expansion enters bus-level schedulability constraints, and that sensing and actuator limits shape integrity thresholds and allowable control delay. We further relate PUF smooth min-entropy to distinguishing advantage and connect innovation statistics to conservative alarm design. Overall, the results characterize how post-quantum security, real-time schedulability, and closed-loop stability interact in safety-critical aerospace control architectures within a defensive analytical treatment that does not provide operational guidance for interference with real platforms.

---


> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-511](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
