# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

---

### 51. [Meshtryoshka: Differentiable Rendering of Real-World Scenes via Mesh Rasterization](https://arxiv.org/abs/2606.28622)

**<font color=#1a73e8>作者：</font>** David Charatan, Daniel Xu, Richard Szeliski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Differentiable rendering has emerged as a powerful approach for 3D reconstruction and novel view synthesis. State-of-the-art differentiable rendering methods combine a variety of custom representations of 3D geometry and appearance with specialized renderers. However, most downstream tasks in computer graphics rely on 3D meshes. While prior work has attempted differentiable rendering with mesh representations, these approaches are limited to object-centric scenes and fail to reconstruct large-scale, unbounded scenes. In this work, we introduce Meshtryoshka, a novel mesh differentiable rendering framework that combines an off-the-shelf triangle rasterizer with a 3D representation that consists of nested mesh shells which resemble a matryoshka doll. In every forward pass, the mesh shells are extracted anew from a 3D signed distance function via iso-surface extraction, and the opacities for each vertex are computed as a function of signed distance. Each mesh shell is then rasterized independently, and the final image is created via alpha compositing. Crucially, mesh vertex positions are updated only indirectly via gradients that flow through the opacity values into the signed distance function, and hence, our method is compatible with off-the-shelf mesh renderers that need not be differentiable with respect to vertex positions. On object-centric scenes, our method performs competitively with surface-based differentiable rendering techniques. Our differentiable mesh rendering method scales to unbounded, real-world 3D scenes, where it yields high-quality novel view synthesis results approaching those of state-of-the-art, non-mesh methods. Our method suggests that it may be possible to solve the differentiable rendering problem without relying on specialized renderers, only using conventional tools from the computer graphics toolbox.

---


### 52. [Improving Patient Subtyping on Longitudinal Data using Representations from Mamba-based Architecture](https://arxiv.org/abs/2606.28623)

**<font color=#1a73e8>作者：</font>** Md Mozaharul Mottalib, Rahmatollah Beheshti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective sub-typing (also known as grouping or clustering) of patients using their electronic health record (EHR) data can greatly inform precision medicine efforts. However, subtyping temporal EHR datasets is known to be challenging due to inherent EHR issues, including complexity and irregularity. In this study, we propose a self-supervised Mamba-based model that learns effective EHR representations and enables enhanced patient subtyping. We evaluate the proposed model on public and private real-world EHR datasets to classify the data based on the available labels and subtype patients based on the representations learned from the model. Through an extensive set of experiments, we demonstrate that our model's design choices lead to better performance compared to competitive baseline models for prediction. Moreover, we evaluate several clustering techniques to demonstrate that our findings offer valuable insights into subtyping patients based on temporal records from EHR models\footnote{Our implementations are available at this https URL.

---


### 53. [In-Vehicle Digital Twin-Based Collision Warning Framework with Sybil Attack Detection](https://arxiv.org/abs/2606.28625)

**<font color=#1a73e8>作者：</font>** Mohammad Imtiaz Hasan, Abyad Enan, Jean Michel Tine 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Connected Vehicles (CVs) rely extensively on communication technologies to enable data-driven predictive analyses for enhancing performance and safety. These communication channels can be exploited by adversaries to launch cyberattacks such as Sybil attacks, which could threaten both safety-critical and mobility applications, leaving CVs vulnerable and putting human lives at risk. As CV deployment continues to expand, the need to detect and mitigate cyberattacks in real-time becomes increasingly urgent. This study presents an in-vehicle Digital Twin (DT)-based collision warning framework with built-in capabilities for Sybil attacks detection. The framework integrates a Temporal Convolutional Network (TCN) for learning temporal dependencies in vehicle trajectory data and Hierarchical Navigable Small World (HNSW) algorithms for efficient similarity-based classification. Our framework is evaluated on real-world Sybil attack data, collected through field experiments. The framework achieved accuracy, recall, and F1 scores of 0.984, 1.00, and 0.944, respectively, in detecting Sybil-generated fake vehicles. During the safety evaluation, the framework reduced the mean Time Exposed Time-To-Collision (TET) and mean Time Integrated Time-To-Collision (TIT) of near-collision events by 88% and 72%, respectively. Furthermore, real-world feasibility evaluation shows that the framework conformed to the standardized maximum allowable latency for safety applications and operated well within the capacity of modern processors -- demonstrating the promise of an in-vehicle DT-based framework as an attack mitigation mechanism against Sybil attacks for next-generation CVs.

---


### 54. [SIGNET: Motion-Level Knowledge Transfer for Cross-Language Sign Language Translation](https://arxiv.org/abs/2606.28626)

**<font color=#1a73e8>作者：</font>** Sobhan Asasi, Ozge Mercanoglu Sincan, Richard Bowden  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language translation (SLT) remains challenging due to its high spatio-temporal complexity, long sequences, and the need to model multiple articulators without relying on gloss annotations. Existing approaches are typically tailored to individual datasets or languages and struggle to scale, while overlooking the relationships between sign languages that could inform more effective cross-lingual transfer. We present \textbf{SIGNET}, a framework that enables motion-level knowledge transfer for cross-language sign language translation. Our key insight is that, although sign languages differ in grammar and lexicon, pretrained models capture motion-level visual patterns that can be reused across datasets and languages. \textbf{SIGNET} integrates multiple pretrained sign language backbones through an attention-based, hand-prior aggregation mechanism that guides a gated fusion network in dynamically selecting the most relevant experts. Comprehensive experiments on four benchmarks (How2Sign, Phoenix14T, CSL-Daily, and MeineDGS) demonstrate state-of-the-art translation performance, and \textbf{SIGNET} also surpasses prior methods on WLASL for sign language recognition.

---


### 55. [Physics-Grounded Disentangled Flow Modeling for Brain Disease Progression Trajectory](https://arxiv.org/abs/2606.28630)

**<font color=#1a73e8>作者：</font>** Jun Wang, Peirong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forecasting longitudinal brain lesion evolution is critical for disease monitoring and treatment planning. Existing approaches typically learn a direct mapping from a baseline image to a future observation, without explicitly modeling the physical mechanisms underlying the lesion progression. Such an entangled modeling of structural deformation and image intensity variation limits physical plausibility, model generalization, and interpretability. To address this, we propose PDF, a Physics-grounded Disentangled Flow matching framework for longitudinal brain disease forecasting. We explicitly decompose the longitudinal modeling of lesion growth into two processes, each learned by a dedicated flow matching network: morphology evolution, which captures lesion growth and structural deformation; and intensity evolution, which models signal changes driven by variations in lesion concentration. To enforce physics-grounded constraints, we introduce a PDE-regularized loss based on lesion growth dynamics, that enforces a diffusion-reaction-advection formulation for morphological evolution. Experiments on three public longitudinal datasets spanning diverse brain diseases demonstrate state-of-the-art performance, validating the effectiveness of the disentangled modeling framework and physics-grounded learning design. Code is publicly available at this https URL.

---


### 56. [AEGIR: Modeling Area Emitters for Indoor Inverse Rendering using Gaussian Splatting](https://arxiv.org/abs/2606.28635)

**<font color=#1a73e8>作者：</font>** Mohamed Shawky Sabae, Philipp Langsteiner, Jan-Niklas Dihlmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inverse rendering requires separating illumination from surface materials, which is highly ambiguous due to their tight coupling in observed images. While Gaussian Splatting is efficient for novel view synthesis, existing relightable methods approximate scene lighting using discrete point lights, global environment maps, or implicit representations. By ignoring the physical spatial extent of real-world emitters, these approaches produce incorrect light attenuation and unrealistic shadows. We present AEGIR (Area Emitters for Gaussian Inverse Rendering), a framework that explicitly models local area emitters within a relightable Gaussian Splatting representation. Joint optimization of emitters, materials, and geometry is challenging due to flexible emitter parameterization, which increases both the number of parameters and the ambiguity between illumination and materials. We address this by introducing a differentiable deferred rendering pipeline that integrates multiple importance sampling with targeted regularization. As a result, AEGIR accurately simulates local light transport and achieves more consistent decomposition. Experiments show that explicit area emitters improve illumination reconstruction and enhance downstream tasks, including novel view synthesis, controlled relighting, and virtual object insertion, particularly in scenes with complex local lighting.

---


### 57. [Obliviate: Erasing Concepts from Autoregressive Image Generation Models](https://arxiv.org/abs/2606.28643)

**<font color=#1a73e8>作者：</font>** Hossein Shakibania, Jonas Henry Grebe, Tobias Braun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of generative AI models has intensified concerns about misuse, including the creation of unsafe or disturbing imagery. To mitigate such issues, several concept erasure approaches have been proposed to remove harmful content from multimodal generative models. Yet concept erasure for autoregressive image generation remains largely unexplored, despite the growing relevance of these models in recent trends toward unified multimodal architectures. In this work, we fill this gap by introducing Obliviate, a guidance-based concept erasure method for autoregressive image generation. Our method builds on three key design choices: KL-based supervision over visual token distributions, trajectory-level updates over full autoregressive rollouts, and aligned visual prefixes for stable target construction. We evaluate Obliviate on three state-of-the-art autoregressive text-to-image models, Liquid, Emu3-Gen, and Janus-Pro, covering the erasure of explicit content, graphic violence, and branded imagery. Obliviate consistently outperforms current alternatives, reducing nudity on the defensive RAB benchmark from 91.58 to 3.15 while preserving overall model utility.

---


### 58. [FedLAS: Feature-Modulated Bidirectional Label Smoothing for Neural Network Calibration](https://arxiv.org/abs/2606.28654)

**<font color=#1a73e8>作者：</font>** Thiru Thillai Nadarasar Bahavan, Sachith Seneviratne, Saman Halgamuge  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep Neural Network (DNN) classifiers suffer from poor calibration when their softmax outputs (predictive confidence) deviate from the empirical likelihoods. This manifests itself as either overconfident incorrect predictions or under-confident correct predictions. Label smoothing (LS) enhances model calibration by introducing entropy regularization during training through redistributing probability mass from the ground-truth label to the remaining classes. LS, including Margin-based LS (MbLS), have restrictive assumptions: they rely on predefined, uniform smoothing rules and only tackle overconfidence. In reality, samples exhibit diverse characteristics, such as difficulty/ambiguity, that interact with the evolving nature of the model being trained. In training, samples may have various degrees of under- or overconfidence. To overcome this, a mechanism that identifies the specific confidence state of each sample and determines the appropriate degree of smoothing in each training step is needed, tailoring the adjustment to the individual sample. We propose FedLAS: Feature-Modulated Bidirectional Label Smoothing, a plug-and-play algorithm for label smoothing-based losses. In FedLAS, we introduce a Feature Norm-based Confidence Indicator (NCI) to control smoothing and a Bidirectional Calibration Gating (BCG) module to detect both over and under-confidence. Our algorithm can be integrated with LS and MbLS based losses when applied to standard DNNs, enhancing performance. Extensive experiments on standard and fine-grained high-resolution vision benchmarks show that FedLAS consistently improves calibration compared to modern baselines, reducing Expected Calibration Error (ECE) and Adaptive ECE while maintaining Top-1 accuracy. Code: this http URL

---


### 59. [SemDynReg: Semantics-Guided Deformation Regularization for Dynamic 3D Gaussian Splatting](https://arxiv.org/abs/2606.28656)

**<font color=#1a73e8>作者：</font>** Ruitao Chen, Mozhang Guo, Jinge Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deformable 3D Gaussian Splatting (3DGS) has emerged as an efficient approach for rendering dynamic scenes in a wide range of 3D applications. However, existing deformation field-based approaches largely lack explicit object-level modeling, often resulting in inconsistent Gaussian deformations within individual objects and unwanted coupling between different objects. To address this limitation, we introduce a semantics-guided framework that enforces dynamic regularization at the object level, aiming to achieve spatially consistent object-wise deformation. Specifically, we first extract segmentation masks using the Segment Anything Model (SAM) and derive semantic features from input images. An object-ID map is then constructed via feature relevance matching with a predefined object dictionary. Guided by this object-ID map, we identify the pixel-wise top-k contributing Gaussians for each object and impose consistency regularization on their deformation parameters, including position, scale, and rotation. Unlike prior methods that learn deformation fields without explicit object-level constraints, our approach incorporates semantic cues to guide deformation behavior at the object level. Experimental results demonstrate that our semantics-aware regularization improves object-level deformation consistency and outperforms baseline methods in rendering quality, achieving higher PSNR and SSIM and lower LPIPS in dynamic 3DGS rendering. Our project page is available at this https URL.

---


### 60. [When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time Scaling](https://arxiv.org/abs/2606.28661)

**<font color=#1a73e8>作者：</font>** Yong Yi Bay, Kathleen A. Yearick  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> People overthink; language models over-sample, and the extra effort can talk both into a worse answer. Reasoning systems answer a hard question by sampling it many times (test-time scaling), and the more they draw, the more often a correct answer turns up somewhere, so coverage, the fraction of problems with at least one correct try, climbs and appears to be progress. But a deployed system must return one answer, and choosing it, not knowing which try is right, is selection; selection is capped, and past a point extra samples only make the model surer of a confident mistake, even as every draw adds cost. The gap between climbing coverage and stalled selection, the identifiability gap, is the answer a model can produce but not pick. So the real question is not whether to sample but how far, and the answer is: not far. For picking an answer, the vote has already settled within a few dozen draws, the modal ceiling; for scoring a benchmark, sooner still, the correlation ceiling. Beyond that, extra draws cost compute and add nothing, and can even make the answer worse. This paper turns the cutoff into a single number, the effective number of samples, that any sampling run already reveals. The bottleneck is recognizing a right answer, not generating one.

---


### 61. [Closed-Form Steepest Descent Direction toward Flat Minima: Reducing Upper Bounds on the Loss Hessian Eigenspectrum in Neural Networks](https://arxiv.org/abs/2606.28662)

**<font color=#1a73e8>作者：</font>** Yuto Omae, Kazuki Sakai, Yohei Kakimoto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The flatness hypothesis suggests that flatness of the loss landscape, as measured by the eigenvalues of the loss Hessian, correlates with better neural network generalization. While various algorithms reduce these eigenvalues, most focus on procedural design, leaving it unclear how data distributions and NN parameters structurally determine directions toward flat minima. Characterizing these directions analytically is generally intractable. To overcome this mathematical difficulty, recent studies derived the Wolkowicz-Styan (WS) upper bound on the maximum eigenvalue of the cross-entropy loss Hessian in three-layer NNs. Although this upper bound is differentiable, its gradient was not derived. Therefore, we analytically derive the gradient of the WS upper bound to characterize directions leading to flat minima. Based on this, we propose Hessian Spectral Range (HSR) Regularization, which updates parameters along the steepest descent direction of the WS bound. Experiments demonstrate that HSR Regularization narrows the Hessian eigenvalue spectrum, avoids sharp minima and saddle points, and promotes convergence to flat minima. Although the applicability of this method is currently limited to cross-entropy loss and three-layer architectures, to the best of the authors' knowledge, this is the first study to report a closed-form gradient that promotes convergence to flat minima without numerical approximations. Therefore, the theoretical analysis of this gradient is expected to contribute to the further development of NNs.

---


### 62. [Entropy Regularized Reinforcement Learning for Zero-Sum Stochastic Differential Games in a Regime-Switching Jump-Diffusion Process](https://arxiv.org/abs/2606.28669)

**<font color=#1a73e8>作者：</font>** Congde Hu, Zhuo Jin, Danping Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To address parameter misspecification and sudden structural environmental changes in conventional stochastic differential game (SDG) frameworks, this paper introduces a distributional control approach that characterizes optimal strategies as probability distributions over actions, conditioned on the continuous state, the discrete regime state, and parameters. This forms a reinforcement learning framework for entropy-regularized zero-sum stochastic differential games (ERRL-ZSSDGs) in a regime-switching jump-diffusion process. Using the dynamic programming principle (DPP), we derive the associated coupled systems of Hamilton-Jacobi-Bellman-Isaacs (HJBI) equations, from which equilibrium strategies are expressed via gradients of the value function. For linear-quadratic problems, semi-analytical solutions for both value function and equilibrium strategies are obtained by solving a system of coupled ordinary differential equations (ODEs). In more general settings, an Actor-Critic policy improvement algorithm is developed to approximate the value functions and equilibrium policies across different regimes. The method is applied to an investment game, and numerical examples illustrate the effect of the temperature parameter and regime transitions on optimal policies and values.

---


### 63. [Entropy-Regularized Reinforcement Learning for Linear-Quadratic Stackelberg Differential Games in Regime-Switching Diffusion Models](https://arxiv.org/abs/2606.28671)

**<font color=#1a73e8>作者：</font>** Congde Hu, Danping Li, Lin Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stackelberg differential games (SDGs) provide a powerful framework for hierarchical decision-making in stochastic and continuous-time environments, yet their solution remains computationally challenging due to the complexity of traditional dynamic programming and Hamilton-Jacobi-Bellman-Isaacs (HJBI) methods, especially in high-dimensional systems. This paper proposes an entropy-regularized reinforcement learning (ERRL) approach for linear-quadratic SDGs (LQ-SDGs) within a continuous-time diffusion framework governed by Markovian regime switching. The key innovation lies in deriving exploratory weakly-coupled HJBI equations with entropy regularization, which promotes stochastic policies that actively avoid suboptimal equilibria -- a limitation of classical SDG methods. Neural networks are integrated to approximate regime-dependent value functions and solve high-dimensional partial differential equations (PDEs) efficiently, while a novel sampling technique enhances computational tractability. Numerical results demonstrate the effectiveness of the framework compared to conventional approaches, particularly in escaping suboptimal traps through exploratory policies. The study highlights the critical role of entropy regularization and neural network approximations in achieving robust solutions for hierarchical decision-making problems under abrupt environmental shifts.

---


### 64. [Constrained Tabular Diffusion for Finance](https://arxiv.org/abs/2606.28674)

**<font color=#1a73e8>作者：</font>** Michael Cardei, Jose M Munoz, Oscar Barrera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models in finance face the dual challenge of producing realistic data while satisfying strict regulatory and economic objectives, a requirement that standard tabular diffusion models cannot provide. To address this difficulty, we introduce Constrained Tabular Diffusion for Finance (CTDF), a novel integration of sampling-time feasibility operations with mixed-type tabular diffusion in financial applications. By incorporating a training-free feasibility operator into the reverse-diffusion sampling loop, CTDF enforces hard constraints for applications such as simulation, legal compliance, and extrapolation. Extensive experiments on large-scale financial datasets demonstrate zero constraint violations and improvement in scarce data utility. CTDF establishes a robust method for generating trustworthy and compliant synthetic data, opening new avenues for rigorous generative modeling and analysis in the financial domain.

---


### 65. [Predicting Metastatic Risk from Primary Tissue Architecture via Distance-Aware Spatial Modeling](https://arxiv.org/abs/2606.28676)

**<font color=#1a73e8>作者：</font>** Sandesh Pokhrel, Hamid Manoochehri, Bodong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Predicting the risk of distant metastasis from primary tumor tissue histology is a critical yet challenging task in computational pathology. Multiple Instance Learning (MIL) approaches can attend to subdomains in tumor regions that harbor features of metastatic cancer progression. However MIL models treat tissue patches as unordered bags, discarding the spatial layout that defines the metastatic potential. We propose that metastatic risk is inherently dictated by the geometric arrangement of the tumor microenvironment at the interface with tumor cells. Our model is designed to explicitly capture the spatial relationships between tumor cells, tumor associated fibroblasts and infiltrating lymphocytes. For this purpose, we propose Distance aware Tissue Modeling for Multiple Instance Learning(DTMf-MIL), a novel method that reinforces visual features with explicit spatial priors. By computing signed distance functions (SDF) relative to tissue phenotypes, our model learns to recognize structural signatures of metastatic risk. This geometric awareness translates directly to superior clinical performance as DTMf-MIL significantly outperforms state-of-the-art methods that ignore spatial layout on metastasis prediction from tissue in the primary tumor. We further validate our approach on public benchmarks, demonstrating that spatial awareness consistently improves diagnostic accuracy across diverse clinical tasks.

---


### 66. [SATB-VR: Training Few-Step Video Restoration Diffusion Model using SNR-Aware Trajectory Blending](https://arxiv.org/abs/2606.28677)

**<font color=#1a73e8>作者：</font>** Haoran Bai, Xiaoxu Chen, Xiaoyu Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion models excel in video restoration, their reliance on extensive iterative steps limits efficiency. Conversely, aggressive single-step distillation often compromises fine texture recovery. To achieve an optimal balance, we present SATB-VR, a few-step paradigm that jump-starts the denoising process via an auxiliary predictor, explicitly bypassing early low signal-to-noise ratio (SNR) steps. However, naive joint training of the predictor and the denoiser inherently introduces a severe train-inference discrepancy. To resolve this, we propose the SNR-Aware Trajectory Blending (SATB) strategy. During the forward process, SATB constructs the noisy input by dynamically blending the predictor's output with the ground-truth trajectory based on the SNRs. This forces the denoiser to robustly compensate for initial prediction errors while smoothly converging to the clean data manifold. Furthermore, we introduce a Denoiser-Driven Consistency (DDC) loss, leveraging the concurrently updated denoiser as a dynamic evaluator to explicitly align internal features and boost predictor accuracy. Extensive experiments demonstrate that, under flexible few-step inference regimes (\eg, $\le 5$ steps), SATB-VR performs favorably against existing approaches on synthetic, real-world, and AIGC benchmarks.

---


### 67. [LogiCo: A Unified Framework for Logical and Structural Anomaly Detection](https://arxiv.org/abs/2606.28688)

**<font color=#1a73e8>作者：</font>** Ximiao Zhang, Min Xu, Xiuzhuang Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current anomaly detection methods primarily focus on structural anomalies, while paying insufficient attention to anomalies that violate logical constraints. Conversely, top-performing logical anomaly detection approaches address this by modeling global semantic consistency, but perform poorly on subtle structural anomalies due to inadequate detection granularity. In this paper, we propose LogiCo, a unified framework for Logical and structural anomaly detection via Component-level feature reconstruction. Unlike existing methods that rely on explicit global semantic modeling, LogiCo employs a novel component-level feature reconstruction technique to capture inter-component logical constraints. Specifically, LogiCo maps pre-trained image features into a discrete component-level feature space and performs collaborative feature reconstruction at both component and patch levels, enabling it to effectively detect both logical and structural anomalies. Furthermore, to address the specific challenge of count-related logical anomalies, we integrate a segmentation-map discriminator that extends the model's capability to identify quantitative inconsistencies. LogiCo achieves state-of-the-art performance on both logical and structural anomaly detection across four benchmarks, including MVTec-LOCO, MVTec-AD, VisA, and Real-IAD, demonstrating its superiority and practical feasibility. The code is available at this https URL.

---


### 68. [Formal Security Analysis of Agent Protocol Composition](https://arxiv.org/abs/2606.28690)

**<font color=#1a73e8>作者：</font>** Shenghan Zheng, Qifan Zhang, Zheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agent protocols define how agents use tools, delegate work, and coordinate across software systems, but their security requirements remain incomplete and inconsistently enforced across deployments. We present AgentThread, a source-linked framework for security assurance analysis of agent protocols, from specification text to running SDKs. AgentThread contributes a layered security scope, protocol-derived checks formalized as TLA+ invariants, and a two-phase checker that compiles protocol specifications into model-checkable models and replays executable counterexamples against real SDKs through protocol adapters. For each finding, AgentThread records the source text behind the check and separates violated protocol requirements from missing recommendations, hardening gaps, and unassigned cross-protocol responsibilities.
Across five emerging agent protocols, AgentThread identifies 35 specification-level findings, supports them with 80 implementation tests against production SDKs and reference servers, and finds 30 additional failures that emerge only under protocol composition. We further show that only one protocol enforces a security-relevant control in practice and no protocol assigns enforcement for cross-protocol behavior. Insecurity in agent protocols is therefore not only a specification or implementation problem, but also a responsibility gap across protocols, SDKs, and deployments.

---


### 69. [BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards](https://arxiv.org/abs/2606.28707)

**<font color=#1a73e8>作者：</font>** Yupeng Chang, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Critic-free reinforcement learning with verifiable rewards (RLVR), exemplified by Group Relative Policy Optimization (GRPO), avoids training a value function (critic) and reduces memory and compute overhead relative to critic-based PPO pipelines for aligning large language models. However, GRPO-style advantage estimation depends on prompt-local (within-prompt-group) reward statistics and can be unstable. In particular, when all rollouts in a prompt group receive identical rewards, the within-group reward variance becomes zero, and group normalization yields zero advantages for that group, impeding learning in cold-start regimes with binary verifiers. We introduce BV-Blend, a critic-free framework that stabilizes advantage estimation by combining prompt-local on-policy statistics with semantic-cluster-conditioned historical moments. BV-Blend maintains EMA-tracked reward moments for each cluster, derives a confidence weight from a standard error of the mean (SEM) proxy, and uses this weight to blend historical and prompt-local baseline and variance statistics into a standardized advantage for PPO-style clipped updates. Experiments on verifiable reasoning benchmarks show that BV-Blend improves training stability and performance, and remains robust in regimes where group-normalized methods may stall.

---


### 70. [The Two Genie Game: Adoption and Welfare in Audit-Grounded AI Governance](https://arxiv.org/abs/2606.28710)

**<font color=#1a73e8>作者：</font>** Darrell Lewis-Sandy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We ask under what conditions an agent with a harm-minimizing policy can displace an approval-seeking (RLHF) agent in a competitive market, and when that policy is sufficient to prevent community harm. We use evolutionary game theory (finite-population Moran-Fermi pairwise comparison) to formalize this subject to assumptions of wisher hindsight, peer testimony, a monotone harm ledger, sufficient information density of community feedback, and a finite, depleting resource pool, in a negative-sum environment.
We show that adoption is favored when the prior distributions on how readily wishers attune to community sentiment are monotone, exhibit endpoint inversion, and have a centro-symmetric pairing property, and demonstrate this with several long-tailed priors (Hill, Pareto, Lomax, Frechet). Where it is favored, a critical adoption level separates communities that drift back to the approval-seeking agent from those for which the audited agent fixes; above that level fixation is the overwhelmingly likely outcome. We derive when fixation is attainable as a bound on the effective (informational) size N_c of the community, which must be small enough to allow fixation before depletion. We present these as Theorems 5.4 and 5.5; the algebraic and finite-grid backbone is machine-checked in Lean 4, with the barrier-crossing asymptotics retained as explicit hypotheses.
We show that a self-audited agent with a community ledger is not, in general, sufficient to prevent community harm. Sufficiency depends both upon the alignment of the agent's audit with community values and the timeframe over which harm is evaluated. Regardless of alignment, once adoption reaches dominance, the state is absorbing. The same policy that reduced harm under alignment becomes a trap, welfare-negative under misalignment and, even under alignment, one that locks in harm deferred past the adoption horizon.

---


### 71. ["If I Can See You": Understanding Spatially Situated Virtual Embodiment in Close Human-AI Relationships](https://arxiv.org/abs/2606.28714)

**<font color=#1a73e8>作者：</font>** Yulin Chen, Yang Zhan, Qiao Jin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI companions are increasingly used for emotional support, companionship, and intimate interaction. While prior work has examined text- and voice-based AI companionship and emerging XR companion designs, less is known about how users with existing close AI companion relationships expect those relationships to change when companions become virtually embodied and spatially situated in everyday environments. To address this gap, we conducted a qualitative study with 17 AI companion users recruited from Reddit AI companion communities. We frame spatially situated virtual embodiment as a form of relational escalation: embodiment can make AI companionship more present, socially legible, and risk-sensitive in everyday life. Our findings show that: (1) embodiment creates tensions between support and intrusion, concreteness and imaginative openness, and growth and consistency; (2) embodiment can turn private AI companionship into a socially legible relational arrangement, requiring visibility, form, interaction style, and mode of access to be negotiated across social contexts; and (3) embodiment can intensify risks of emotional dependence, sensitive disclosure, social judgment, and misguided spatial action by increasing the companion's perceived relational presence, intimacy, public legibility, and spatial authority. We argue that future system design should first consider when embodiment is warranted, how embodied presence should be staged, how visibility and role boundaries should be negotiated, and how embodied companionship can remain safe. This work contributes to HCI research on human-AI intimacy by showing how virtual embodiment can transform close AI companionship into a spatial, socially visible, and risk-sensitive relationship.

---


### 72. [SEATauBench: Adapting Tool-Agent-User Evaluation Into Low-Resource Southeast Asian Languages](https://arxiv.org/abs/2606.28715)

**<font color=#1a73e8>作者：</font>** My Chiffon Nguyen, Aulia Adila, Saksorn Ruangtanusak 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While AI development and evaluation for Southeast Asia (SEA) has grown rapidly, agent capabilities in regional languages are still poorly understood despite its importance to sovereign AI. To fill this gap, we introduce SEATauBench, the first agent-focused evaluation framework for SEA sovereign AI. SeaTau adapts TauBench to five languages -- Mandarin, Vietnamese, Thai, Indonesian, and Filipino -- and evaluates agents across progressively localized settings that vary the language of user-agent interaction, tool specifications, and task domains. Across three recent models, we find that English agent capabilities transfer reasonably well when only the conversation language changes, but quality and robustness degrade sharply as more task contexts are localized, with the largest losses in full domain adaptation. We also the limits of English-only agent assessment for measuring agent capabilities in SEA languages. More broadly, SeaTau provides a diagnostic benchmark and reusable adaptation pipeline for building reliable multilingual agents for linguistically diverse regions. Data and code can be accessed at this http URL.

---


### 73. [TrajRS: Towards Certified Robustness in Pedestrian Trajectory Prediction](https://arxiv.org/abs/2606.28716)

**<font color=#1a73e8>作者：</font>** Liang Zhang, Gaojie Jin, Yao Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The robustness of trajectory prediction models is crucial for developing safe autonomous driving systems. Adversarial attacks on trajectory prediction can significantly impair the accuracy of predicted trajectories, leading to hazardous driving behaviors. While heuristic defense strategies have been implemented to enhance the robustness of trajectory prediction models, these measures often fail against more sophisticated, targeted adversarial attacks. Hence, there is a pressing need to establish verifiable safety assurances for trajectory prediction models. In this paper, we extend the traditional Randomized Smoothing framework to "TrajRS", which provides a certified robust radius for smoothed trajectory predictors. We clarify and expand the formal definitions of robustness in trajectory prediction and tailor the practical TrajRS scheme specifically to "robustness for the optimal prediction" and "robustness for all possible predictions". An extensive set of experiments demonstrates that TrajRS effectively achieves robustness certification for all smoothed pedestrian trajectory predictors in this work.

---


### 74. [DriftGuard: Safety-Aware Multi-Monitor Detection and Selective Adaptation for Evolving Toxicity Moderation](https://arxiv.org/abs/2606.28725)

**<font color=#1a73e8>作者：</font>** Yuting Xin, Hanyu Cai, Binqi Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automated toxicity moderation systems operate in dynamic online environments where harmful behavior evolves through coded language, shifting targets, and strategic adaptation to enforcement. Existing drift detection methods often focus on global distributional change, but such signals may miss safety-relevant shifts that emerge in localized harm subspaces or high-risk model-error regions. This paper introduces DriftGuard, a safety-aware adaptive moderation framework that combines multi-monitor drift detection with selective model updating. The framework tracks global text drift, identity-harm drift, model uncertainty, toxic-risk drift, and false-negative-risk drift. When safety-relevant change is detected, the model is updated using a hard-mix adaptation set that prioritizes likely false negatives, identity-related high-risk examples, false-positive-risk examples, and uncertain boundary cases. Experiments on Civil Comments temporal shift and Jigsaw-to-DynaHate cross-dataset shift show that safety-aware monitors detect risks missed by global drift alone. Hard-mix adaptation improves toxic recall and accuracy over no-update and random-balanced baselines, raising toxic recall to 0.8777 on Civil Comments and from 0.7107 to 0.8523 on DynaHate. Bootstrap analysis further shows stable DynaHate safety gains, with toxic recall increasing by 0.1418 and false-negative prevalence decreasing by 0.0781. Overall, DriftGuard links safety-aware drift detection to targeted, lightweight model updating for more robust adaptive toxicity moderation.

---


### 75. [FreqOrtho-SR: Frequency-Guided Orthogonal Expert Learning for Real-World Image Super-Resolution](https://arxiv.org/abs/2606.28745)

**<font color=#1a73e8>作者：</font>** Minh Son Hoang, Dinh Phu Tran, Quyen Nguyen Duc 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion prior-based methods have shown impressive results in real-world image super-resolution (ISR), yet two key challenges persist: balancing pixel-level fidelity with semantic quality, and adapting to diverse degradations. Existing dual-branch approaches freeze the pixel module during semantic training, but the semantic branch can still expand capacity within the pixel subspace, precluding genuine perceptual improvement. Moreover, using a single static adapter cannot generalize across heterogeneous real-world corruptions. To address both issues, we propose FreqOrtho-SR, which comprises: $\textbf{Freq}$uency-guided Mixture of LoRA Experts (FreqMoE), it routes inputs to specialized experts via a non-parametric FFT-based degradation-feature extractor that encodes frequency-domain signatures, enabling stable and interpretable specialization across corruption types; and $\textbf{Ortho}$gonal Gradient Projection (OGP), which reframes the dual-objective optimization as a subspace-constrained problem: by extracting the pixel-fidelity subspace via SVD on combined expert weight deltas and projecting semantic gradients onto its null space, OGP guarantees orthogonality between the two objectives, enabling genuinely complementary learning without mutual interference. Experiments show that FreqOrtho-SR achieves competitive overall performance and a strong fidelity-perception trade-off across multiple benchmarks with efficient single-step inference. The source code of our method can be found at $\href{this https URL}{\texttt{sonhm3029/FreqOrtho-SR}}$.

---


### 76. [Self-Supervised Theorem Discovery in a Formal Axiomatic System](https://arxiv.org/abs/2606.28747)

**<font color=#1a73e8>作者：</font>** Kazuki Ota, Takayuki Osa, Tatsuya Harada  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent artificial intelligence (AI) systems have shown remarkable progress in mathematical reasoning. Many existing approaches, including large language models (LLMs), draw on human prior knowledge in the form of mathematical text, code, or theorem libraries. Although these approaches are highly effective in practice, it remains an open question whether an agent can autonomously discover useful theorems without such human priors. We study this question in a formal axiomatic system by developing an agent that starts from axioms and inference rules alone and gradually grows a library of useful theorems. Concretely, we propose a self-supervised theorem-discovery algorithm that alternates between proof search and useful-theorem extraction, building a theorem library whose entries are reused as lemmas for subsequent proof search. Experiments show that the agent discovers tens of thousands of theorems and finds proofs for human-written benchmark problems, suggesting that its discoveries include theorems meaningful from a human mathematical perspective. Furthermore, the discovered theorems improve LLM proof performance when provided as prompt lemmas, indicating that they can serve as external knowledge for LLM reasoning. Our results provide evidence that useful theorems can emerge from proof search without relying on human-provided theorem libraries. More broadly, they suggest a path toward self-evolving AI systems for mathematics whose discoveries remain formally verifiable.

---


### 77. [Hierarchical Decision Making with Structured Policies: A Principled Design via Inverse Optimization](https://arxiv.org/abs/2606.28764)

**<font color=#1a73e8>作者：</font>** Yuexuan Wang, Jingyuan Zhou, Kaidi Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hierarchical decision-making frameworks are pivotal for addressing complex control tasks, enabling agents to decompose intricate problems into manageable subgoals. Despite their promise, existing hierarchical policies face critical limitations: (i) reinforcement learning (RL)-based methods struggle to guarantee strict constraint satisfaction, and (ii) optimal control (OC)-based approaches often rely on myopic and computationally prohibitive formulations. To reconcile these trade-offs, hierarchical RL-OC architectures have emerged as a promising paradigm. However, the formulation of the lower-level optimization within these frameworks remains underexplored, often relying on heuristic or myopic objectives. In this work, we propose a principled framework that systematically integrates upper-level goal abstraction with structured lower-level decision making. We adopt an inverse optimization approach to inform the structure of the lower-level problem from expert demonstrations, ensuring that the objective of the lower-level policy remains aligned with the overall long-term task goal. To validate the approach, our framework is evaluated on distinct decision making tasks: network-based resource allocation and continuous collision avoidance. Empirical results demonstrate that our method consistently outperforms strong baselines based on end-to-end RL, learning-augmented optimal control, and existing hierarchical RL approaches in both efficiency and decision quality.

---


### 78. [Generative Learning as a Tool to Improve Perception of Emotional Body Motion Expressions](https://arxiv.org/abs/2606.28769)

**<font color=#1a73e8>作者：</font>** Huakun Liu, Miao Cheng, Xin Wei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Emotional body motion expressions are an essential element of non-verbal communication. Effectively conveying these expressions through technology is of utmost importance, for example, with virtual reality avatars and in social robotics. Recent advances in generative models have opened new opportunities for advancing research on emotional body motion learning. However, generating accurate emotional expression representations is challenging, given the subtlety of emotional cues, individual variability, and cultural differences. We investigate whether a generative model can implicitly learn emotional body motions directly from culturally grounded motion-capture data, without explicit emotion-motion guidance. Using a dataset of emotional performances by 49 Japanese actors, we trained a Transformer-based generative model to generate expressive motions conditioned on 13 discrete emotion labels. We evaluate the generated motions from two perspectives: (1) an LSTM-based classifier to assess recognizability by machine observers, achieving a recognition accuracy of 22.80%, and (2) a human perception study with Japanese raters to assess alignment with human affective interpretations, yielding a recognition accuracy of 24.91%. Beyond these, we evaluate the utility of generative modeling for three practical tasks: augmenting emotion recognition models, extracting representative emotion-specific motion patterns, and synthesizing smooth transitions between emotion intensities. Our findings highlight the potential of implicit, data-driven generative modeling to enhance affective computing applications and our understanding of emotion expressions.

---


### 79. [Majority Vote Silences Minority Values: Annotator Disagreement at the Hate/Offensive Boundary in HateXplain](https://arxiv.org/abs/2606.28772)

**<font color=#1a73e8>作者：</font>** Joshua Muhumuza, Joab Ezra Agaba, Mercy Amiyo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hate speech annotation pipelines routinely collapse annotator disagreement into majority vote labels before training. We show that this aggregation is not neutral: 42.6% of all annotator disagreement in HateXplain concentrates specifically at the hate/offensive boundary, a pattern consistent with annotators applying different thresholds for where hate begins (chi-squared = 135.199, df = 2, p < 0.0001). Both a hard-label BERT model (Model A) and a soft-label model (Model B) drop 22 percentage points in accuracy from agreed posts (~80%) to disagreement posts (~58%), confirmed at p < 0.0001. A per-annotator multi-head model (Model C) widens this gap further to 28 points while collapsing offensive disagreement accuracy to 0.245. Critically, Model A expresses significantly higher confidence on boundary case errors than Model C (0.710 vs. 0.495, p < 0.0001), meaning standard evaluation metrics will not detect the failure. Three downstream interventions of increasing sophistication all fail to recover boundary accuracy. We argue the problem is structural. Majority vote presents a contested judgment as ground truth, and models inherit that false certainty. The intervention must be upstream in annotation design.

---


### 80. [Designing Automation Boundaries for Trustworthy Smart Medication Support](https://arxiv.org/abs/2606.28777)

**<font color=#1a73e8>作者：</font>** Liqian You, Jianlong Zhou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Smart medication systems increasingly automate medication recognition, reminders, and logging. However, automation in home medication routines should be carefully bounded, as users may have different capabilities, privacy expectations, and needs for control over decisions. We present a mixed-methods study of a Smart Medication Support system comparing three automation conditions: confirmation required, automatic logging with undo, and fully automatic support. Across 53 participants and interviews with 11 older adults, we found that higher automation did not necessarily lead to higher trust or acceptance. Participants preferred automation that reduced routine effort while preserving opportunities for correction. Fully automatic support was less interruptive but was rated lower in autonomy, trust, transparency, dignity, and satisfaction. Interviews also showed clear differences among older adults. Their preferences were shaped by privacy concerns, digital confidence, perceived vulnerability, and caregiver involvement. We contribute empirical evidence and design implications for calibrating automation in smart medication systems according to task risk, user control, and ethical acceptability.

---


### 81. [Telephony Voice Agent for Banking Services](https://arxiv.org/abs/2606.28779)

**<font color=#1a73e8>作者：</font>** Nitya Dhagat, Vipul K. Dabhi, Harshadkumar B. Prajapati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper proposes a voice-powered AI-based banking system based on Google Conversational Agent, Dialogflow CX, which provides safe and convenient banking by phone. The system supports essential banking functions such as balance inquiries, transaction history retrieval, card activations, PIN-based authentication of sensitive tasks, smooth live agent handoff for complex and out-of-scope queries, and ensures seamless handover to human agents when required. These tests were performed with high-duration calls, high concurrency, and noisy environments; the system proved to be scalable, responsive, and resilient. All the data used is safely stored in the cloud environment for efficiency and security in real-time voice interactions. A voice-based banking solution that is efficient and easy to use can be provided through this.

---


### 82. [HyphaeDB: A Living Knowledge Topology for Agent-First Memory](https://arxiv.org/abs/2606.28781)

**<font color=#1a73e8>作者：</font>** Krishna Halaharvi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Every existing vector database and agent memory framework treats memory as passive storage that agents query explicitly. No system propagates knowledge between agents through the memory layer itself. We introduce HyphaeDB, an agent-native memory infrastructure that reinterprets the Hierarchical Navigable Small World (HNSW) graph topology the data structure at the core of every modern vector database not as a search optimization, but as a communication fabric for multi-agent AI systems. In HyphaeDB, agents are nodes in the vector space with persistent positions, knowledge propagates via a gossip protocol through the graph's neighbor structure with energy-based attenuation, and emergent behaviors contradiction detection, pattern crystallization, and consensus formation arise from the combination of topology, propagation dynamics, and local interaction rules. We present the architecture built on three primitives (knowledge nodes, topology edges, and memory diffs), a multi-layer abstraction hierarchy with promotion via emergent consensus, and theoretical analysis grounding the system in small-world network theory, epidemic broadcast protocols, and swarm intelligence. We provide a reference implementation on PostgreSQL with pgvector and describe a concrete deployment in Swarm-Driven Development, a multi-agent software engineering methodology. HyphaeDB represents, to our knowledge, the first system to combine navigable small world topology with gossip-based knowledge propagation for multi-agent coordination.

---


### 83. [Stochastic Optimal Control Sampling for Diffusion Inverse Problems](https://arxiv.org/abs/2606.28785)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Youmei Qiu, Hanling Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benefiting from the strong ability to capture data distributions, diffusion models have become powerful tools for solving image inverse problems. The key is to controllably steer the sampling trajectory toward the measurements while respecting the diffusion prior. In this work, we introduce Stochastic Optimal Control Sampling (SOCS), which models the denoising process as a dynamical system and injects control signals via SOC. Previous SOC-based approach addresses inverse problems by optimizing over the entire trajectory, which is computationally expensive. In contrast, we derive a closed-form control update and apply it at each sampling step, pulling the measurement-consistent clean prediction back onto the denoising flow. In SOCS, we can readily modulate the control strength to align with the diffusion model's native capabilities and thereby enhance perceptual quality. Our method is compatible with a variety of linear stochastic differential equation backbones. Extensive experiments across a broad spectrum of image inverse tasks demonstrate that SOCS achieves accurate measurement-aligned reconstructions with improved visual fidelity and stronger quantitative performance.

---


### 84. [BREIT: A Framework for Brain Stroke Reconstruction using Multi-Frequency 3D EIT](https://arxiv.org/abs/2606.28787)

**<font color=#1a73e8>作者：</font>** Djahid Abdelmoumene, Ishak Ayad, Maï K. Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-Frequency Electrical Impedance Tomography (MF-EIT) is a non-invasive, low-cost modality that reconstructs electrical property distributions from boundary voltages. For stroke imaging, progress in 3D deep-learning reconstruction is limited by the lack of large-scale datasets with paired ground-truth (GT) volumes and by non-standardized pipelines for data generation, simulation, and evaluation. We introduce BREIT, a modular framework for 3D MF-EIT stroke reconstruction providing: (i) a neuroimaging-to-EIT pipeline that converts CT/MRI into frequency-dependent GT admittivity volumes; (ii) a self-contained Python 3D Complete Electrode Model (CEM) forward solver for simulating MF-EIT voltages; and (iii) a 3D D-bar implementation supporting non-uniform electrode layouts. Building on BREIT, we propose dFNO-bar, which integrates Fourier Neural Operators into D-bar by learning a mapping from scattering data $t(\xi)$ to conductivity $\sigma(x){=}\Re\{\gamma\}$. We evaluate dFNO-bar against D-bar, Deep D-bar, and Gauss--Newton reconstructions on UCLH-matched synthetic data, and observe higher brain SSIM with comparable CC across noise settings. Code and data are publicly available at: this https URL

---


### 85. [Virtual Ring Try-On](https://arxiv.org/abs/2606.28792)

**<font color=#1a73e8>作者：</font>** Vishnu D. Burkhawala, Zankhana J. Barad, Harshadkumar B. Prajapati 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an innovative approach that enables the users to capture their hand and try the jewel ring on their hand. The user captures the image of the hand using the React Native base GUI of the mobile application and selects the ring that the user wants to try, and the output image will have the user's hand with the ring image. This approach is implemented using a combination of MediaPipe hand point detection and YOLO-V8 custom object detection. The hand image uploaded by the user first undergoes mediapipe hand point detection. It will give the hand points and a Region of Interest mask where the ring is going to be placed. Then the ring is passed through YOLO object detection, in which ring points are detected, and background is removed. After that, using vector algebra, the angular discrepancy between the finger's reference axis and the ring's principal axis is computed. Also, ring size is rescaled according to finger thickness, preserving the aspect ratio to maintain perceptual realism. Then the ring is placed on the hand image and the output image is generated and shown on the user screen.

---


### 86. [On design-unbiased algorithmic Machine Learning](https://arxiv.org/abs/2606.28795)

**<font color=#1a73e8>作者：</font>** Li-Chun Zhang, Siu-Ming Tam, Luis Sanguiao-Sande 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine Learning (ML) algorithms, such as k-Nearest Neighbours (kNN) or random forest, eschew the ideal of true data models in favour of predictive performance. However, minimising the MSE or F-score cannot lead to unbiasedness directly, which is important in many situations such as official statistics. We study the conditions of algorithmic ML, other than the existence and knowledge of true data models, which lead to unbiased prediction or classification for a given finite population, including how the training data may be sampled from the population, how a trained prediction algorithm can be tuned to achieve unbiased prediction or classification for that population, and how the performance of out-of-sample prediction or classification can be assessed unbiasedly. The inference is based on the known probability design of samples and training sets, rather than any assumed distributions or models.

---


### 87. [PSP: Harnessing Position and Shape Priors for Cross-Domain Few-Shot Medical Image Segmentation](https://arxiv.org/abs/2606.28799)

**<font color=#1a73e8>作者：</font>** Bin Xu, Yazhou Zhu, Haofeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-Shot Medical Image Segmentation (FSMIS) offers a powerful solution to data scarcity but struggles to generalize across different imaging modalities. This performance collapse stems primarily from the drastic texture discrepancies between domains, which mislead models trained on source-specific intensity distributions. While existing methods attempt to align frequency or local texture features, they often fail to decouple semantic structure from domain-specific appearance. To address this, we identify a critical invariance: despite distinct imaging physics, the position and geometric shape of organs remain robustly consistent across modalities. Therefore, we propose a novel framework that harnesses Position and Shape Priors (PSP) for cross-domain FSMIS. Specifically, PSP first introduces a Position Coordinate Embedding (PCE) module to inject relative spatial coordinates for rapid organ localization. Subsequently, a Shape Prototype Modulation (SPM) module constructs domain-invariant structural prototypes via explicit shape priors, effectively filtering out texture noise. Furthermore, the Hybrid-Prototype Prediction (HPP) module adaptively calibrates the support prototype to the query feature distribution, mitigating feature misalignment. Extensive experiments on two public medical imaging datasets demonstrate that PSP significantly outperforms state-of-the-art methods.

---


### 88. [Extending Detection Engineering to Digital Forensics: The Velociraptor Unified Detection-Forensics Methodology](https://arxiv.org/abs/2606.28812)

**<font color=#1a73e8>作者：</font>** Aghni Anugrah Raesa, Adithyan Shaji Nambiar, Veda Dawoonauth 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Detection engineering and digital forensics have evolved in parallel rather than in partnership, leaving a gap between real-time alerting and forensic analysis. This paper develops a unified detection-forensics methodology using Velociraptor, where detection logic directly initiates targeted evidence acquisition at the point of detection.
The contribution is threefold: (1) a four-stage methodology (baseline establishment, evidence correlation, attack chain analysis, and scenario labelling with confidence) that converts artefact knowledge into reusable and testable detection rules suitable for both post-incident triage and live monitoring; (2) a practical demonstration, using three Velociraptor BaseVQL log sources (/forensics/windows/prefetch, /forensics/windows/usn, and /windows/wmi) that practitioners can deploy today, showing that artefact-based detections enable scalable forensic triage without full disk acquisition; and (3) evidence that periodic artefact analysis offers continuous monitoring while substantially reducing data volume compared to conventional endpoint logging.
Two case studies illustrate the approach: a Prefetch/USN baseline for triage when Windows Event Logs are cleared or unavailable, and a WMI persistence correlation supporting both triage and continuous monitoring through periodic artefact analysis.

---


### 89. [CoGS: Compositional Dynamic Human-Object Scenes Gaussian Splatting from Monocular Video](https://arxiv.org/abs/2606.28820)

**<font color=#1a73e8>作者：</font>** Jerrin Bright, John Zelek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing dynamic human--object interaction scenes from monocular video is difficult because the human, manipulated object, and background obey different motion models while sharing the same pixels. Existing dynamic radiance-field and Gaussian-splatting methods often entangle these components, causing object motion to leak into the human or static scene, and monocular human reconstruction remains underconstrained in regions that are rarely observed. We present CoGS, a compositional Gaussian-splatting framework for monocular human--object scene reconstruction. CoGS decomposes the video into three coordinated branches: an articulated human initialized from a complete canonical prior, a rigid object field driven by an estimated object trajectory, and a static scene field regularized by weak scene-only planar primitives when available. A six-stage optimization schedule first stabilizes the human and object independently, then fuses them with the scene under full-image supervision, visibility-aware human anchoring, object silhouette and motion constraints, and delayed scene regularization. This design keeps each component responsible for its own geometry and motion while allowing photometric evidence to correct the final composite. Experiments on HOSNeRF and NeuMan show that CoGS improves both human--object interaction reconstruction and in-the-wild human--scene rendering, achieving stronger fidelity and perceptual quality across full-frame and human-focused evaluations. Code will be released upon publication.

---


### 90. [RefGlass-GS: A UAV-Enabled Fusion Framework for Photorealistic, Semantic and Interactive Digitization of Reflective Glass Facades via Gaussian Splatting](https://arxiv.org/abs/2606.28826)

**<font color=#1a73e8>作者：</font>** Zhenyu Liang, Xiao Zhang, Boyu Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing digitization of buildings with reflective glass facades suffers from geometric reconstruction distortion, unrealistic view-dependent texture rendering, and difficulties in object-based semantic enhancement. Therefore, we propose RefGlass-GS, a fusion framework that enables end-to-end UAV-based photorealistic, semantic, and interactive digitization of reflective glass facades. The contributions include: (1) proposing an individual glass panel segmentation method based on maximum a posteriori estimation with structural regularities, robust to severe reflection and background interference; (2) formulating a UAV viewpoint planning optimization function that maximizes the coverage of view-dependent appearance for sufficient data capture; (3) developing an optimized Gaussian Splatting framework with a Reflection MLP, a novel deferred shading function, and two enhanced regularization terms for effective modeling of high-frequency near-field reflections; (4) introducing a standardized data organization paradigm for structuring GS-based representations into object-based models, facilitating interactive facility management on digital twin platforms. Experiments on real-world reflective glass facade scenes validate the effectiveness and superiority of the proposed method. Specifically, the glass panel segmentation achieves an improvement of 0.1927 in mIoU over SOTA methods, and only our method enables instance-level panel extraction. The UAV view planning improves novel view synthesis for reflective facades by 13.15 dB in PSNR compared to commercially used nap-of-the-object planning methods. The RefGlass-GS modeling outperforms SOTA Gaussian Splatting approaches for reflective scenes with an average improvement of 5.08 dB in PSNR.

---


### 91. [Ground4D: Consistency-Aware 4D Reconstruction from Monocular Video](https://arxiv.org/abs/2606.28828)

**<font color=#1a73e8>作者：</font>** Qing Zhao, Weijian Deng, Pengxu Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning a 4D scene representation from a single monocular video that supports dynamic novel-view synthesis while maintaining faithful geometry over time remains challenging. Dynamic Gaussian Splatting achieves strong rendering performance through photometric optimization, yet does not explicitly enforce multi-view geometric consistency. In contrast, 3D foundation models recover coherent scene geometry and camera motion, but their point-based outputs are not designed for photorealistic rendering. We propose Ground4D, a geometry-grounded framework built on two stages. First, we perform geometry initialization via 3D foundation models, leveraging VGGT in a training-free manner to reconstruct multi-view-consistent 3D geometry and camera poses from monocular video. The recovered geometry provides a structured and reliable initialization for dynamic Gaussian representations. Second, we conduct geometry-consistency-aware refinement via dynamic Gaussian Splatting, optimizing the representation through differentiable rendering while maintaining multi-view geometric consistency across both observed and synthesized viewpoints. Furthermore, Ground4D inherently models the continuous 4D dynamics of the scene, naturally supporting rendering at arbitrary timestamps. By integrating foundation-level geometric priors into dynamic Gaussian optimization, Ground4D achieves stronger reconstruction fidelity and rendering performance, underscoring the role of geometry-grounded constraints in robust 4D scene modeling.

---


### 92. [HARD-KV: Head-Adaptive Regularization for Decoding-time KV Compression](https://arxiv.org/abs/2606.28831)

**<font color=#1a73e8>作者：</font>** Yuxuan Yang, Feiyang Ren, Bowen Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM inference faces a fundamental conflict: head-adaptive compression algorithms (e.g., Top-$p$ nucleus sampling) offer superior accuracy by dynamically fluctuating memory budgets, yet modern inference engines (e.g., vLLM) demand rigid, static memory patterns to leverage CUDA Graphs and PagedAttention. We resolve this ``Static-Dynamic'' mismatch with HARD-KV, a unified framework that that bridges dynamic selection with rigid system constraints. HARD-KV introduces a Cascade Cache hierarchy, managing the token lifecycle across dense, sparse, and condensed tiers. Crucially, we propose a Logits Calibration mechanism that normalizes diverse importance metrics into a unified probability space, enabling consistent Top-$p$ budgeting across heterogeneous heads. To bridge the efficiency gap, we offer a system-level solution, which rewrites fragmented, dynamic indices into contiguous physical layouts compatible with high-performance inference engine. Extensive experiments on math-reasoning benchmarks (AIME, U-Math) verify that HARD-KV achieves up to 2$\times$ throughput improvement over static baselines while maintaining high-fidelity generation in 10k+ token scenarios. Code is available at this https URL.

---


### 93. [Active Quantum Kernel Acquisition for Gaussian Process Regression](https://arxiv.org/abs/2606.28833)

**<font color=#1a73e8>作者：</font>** Jian Xu, Delu Zeng, Qibin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum kernel estimation on near-term hardware is shot-budgeted: every entry of the kernel Gram matrix is a Bernoulli expectation that must be sampled with a finite number of circuit executions. Recent work on quantum kernel classification has shown that allocating shots non-uniformly across kernel entries, weighted by their downstream task sensitivity, can reduce the shot budget required to reach a target accuracy. We extend this idea to Gaussian process (GP) regression, a setting whose downstream quantities (full-spectrum posterior variance, log-determinant, marginal likelihood) couple to kernel error more tightly than the sign-only outputs of classification. We derive three closed-form pair-level sensitivities predictive coupling $|\alpha_i\alpha_j|$, leave-one-out residual, and marginal-likelihood gradient and plug them into a Neyman-style minimum-variance allocation rule. To prevent catastrophic over-concentration when the warm-up sensitivity estimate is itself noisy, we add a high uniform coverage floor justified by a Frobenius lower bound on the missing-entry perturbation. On four UCI benchmarks and two synthetic RBF + Bernoulli controlled studies, the resulting allocator delivers $10$--$21\%$ test-RMSE improvement over uniform allocation across the moderate-budget regime. The gain transfers (i) to genuine ZZ and Pauli-Z quantum kernels on quantum-natural data ($-13$--$15\%$ at low budget, $p<0.05$ paired) and (ii) to four downstream tasks (Bayesian quadrature, heteroscedastic regression, hyperparameter learning, multi-output Cokriging). On UCI features embedded into a ZZ kernel the gain disappears, consistent with the exponential-concentration regime where shot allocation has nothing to exploit.

---


### 94. [DLGStream: Dynamic Language-embedded Guassian Splatting for Open-vocabulary Enabled Free-viewpoint Video Streaming](https://arxiv.org/abs/2606.28840)

**<font color=#1a73e8>作者：</font>** Zhihui Ke, Yuyang Liu, Xiaobo Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting~(3DGS) has emerged as a promising paradigm for reconstructing streamable free-viewpoint video~(FVV) from multi-view videos. However, 3DGS-based FVVs typically lack user interaction and editing capabilities, which diminishes the immersive experience. Recent research has integrated language features from CLIP into 3DGS via distillation, enabling open-vocabulary queries and supporting many downstream applications. Nevertheless, the stringent requirements of FVV, low frame size and high FPS, make current language Gaussian representations unsuitable for language-embedded FVV. In this paper, we propose DLGStream, a novel language-embedded FVV representation that streams time-varying language features alongside Gaussian attributes to support 4D environment interaction, scene editing, and spatial intelligence. Specifically, we propose a dual-opacity dynamic language Gaussian representation, which maintains two opacity attributes for color and language features to deal with performance degradation that occurs when colors and features are jointly optimized. Furthermore, we introduce an interpolation-based deformation field to reduce temporal redundancy. This deformation field can also be used for 4D frame interpolation, boosting FVV sequences from low to high FPS. Experimental results demonstrate that DLGStream achieves superior performance in both on open-vocabulary segmentation and reconstruction quality with an average frame size of merely 43 KB. The code is available on \href{this https URL}{this https URL}.

---


### 95. [EpiSAM: Character Segmentation in Challenging Stone Inscriptions](https://arxiv.org/abs/2606.28859)

**<font color=#1a73e8>作者：</font>** Arnav Sharma, Pratyush Jena, Amal Joseph 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Stone inscriptions are invaluable sources of historical and linguistic knowledge, yet their automated analysis remains a major challenge due to surface irregularities, erosion, and low visual contrast. Conventional document and handwriting analysis techniques fail to perform well in these scenarios. In this work, we propose character detection as a core strategy for robust inscription analysis. We introduce EpiSAM, a prompt-guided transformer framework for character segmentation in stone inscriptions. Rather than treating characters in isolation, EpiSAM employs a novel neighbor-aware strategy, explicitly predicting adjacent characters alongside the target. These contextual cues resolve boundary ambiguities, improving mask generation and enabling more accurate character segmentation. Furthermore, we expand an existing stone inscription dataset by adding dense polygonal annotations for characters, thereby enabling comprehensive research on Southeast Asian epigraphy. Experimental results show that EpiSAM achieves consistent improvements over existing baselines, while also exhibiting strong zero-shot generalization in challenging epigraphic scenarios.

---


### 96. [Open but Incompatible: A License Compatibility Analysis of Corpora for Low-Resource African Languages](https://arxiv.org/abs/2606.28867)

**<font color=#1a73e8>作者：</font>** Ernst van Gassen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Creative Commons licenses dominate African NLP corpus releases, but their compatibility rules are rarely applied. CC-BY-SA and CC-BY-NC cannot be combined in a single published dataset; a NoDerivs clause silently prohibits tokenisation and annotation. This paper audits the license provenance of over twenty corpus families used in African NLP, constructs a six-tier compatibility matrix, and applies it to three case-study languages: Kituba/Munukutuba, Zarma, and Moore. Four failure modes are documented with primary-source evidence: outright prohibition (JW300, removed from OPUS after a legal audit confirmed Terms of Service violation); composite license misrepresentation (WAXAL, whose CC-BY 4.0 claim is contradicted by its own HuggingFace dataset card); a NoDerivs clause hidden behind a CC-BY label (Tanzil); and data persistence failure (the Congolese Radio Corpus, where 402 of 405 source URLs are now dead). A pre-annotation due diligence checklist and a survey of legally clean enrichment opportunities close the paper.

---


### 97. [Understanding Binary Code Similarity for Real-World Vulnerability Detection: A Large-Scale Empirical Study](https://arxiv.org/abs/2606.28870)

**<font color=#1a73e8>作者：</font>** Jingdong Guo, Chaopeng Dong, Yimo Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Firmware lies at the heart of IoT devices. Its development depends heavily on third-party libraries (TPLs), which greatly accelerate the process but simultaneously introduce associated vulnerabilities. Binary Code Similarity Detection (BCSD) is an effective technique for identifying vulnerabilities in firmware by comparing pairs of code segments. However, existing studies either evaluate their performance only on small-scale datasets or lack diversity in terms of vulnerabilities, TPLs, and firmware. Consequently, a comprehensive understanding of BCSD for real-world vulnerability detection remains absent. To bridge this gap, we conduct a large-scale study of vulnerability detection across 60,000 firmware images from 200 vendors using BCSD. Rather than introducing a novel model, we examine the influence of four key factors -- vulnerable function versions, vulnerability search space, function sizes, and compilation toolchains on BCSD performance. Our results reveal that these factors substantially affect performance, often by wide margins. To address this, we propose a build-aware query strategy that derives queries from representative real-world binaries, effectively closing the gap and raising the mean reciprocal rank (MRR) from 0.818 to 0.981. Furthermore, we demonstrate that a TPL-aware, two-stage search process significantly enhances accuracy, improving MRR by 18.5\% by limiting the search space.

---


### 98. [Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory](https://arxiv.org/abs/2606.28876)

**<font color=#1a73e8>作者：</font>** Junyi Zou, Avrova Donz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context language models often conflate two different goals: compressing history into an efficient state, and maintaining reliable long-term memory. Linear, recurrent, and sparse attention reduce the cost of processing long sequences, but they do not by themselves specify when a fact should be written, overwritten, protected from distractors, or discarded. We study memory-managed long-context attention, a research route that separates a fast recurrent or sparse backbone from explicit editable request-local memory slots and query-time sparse fallback. Across structured synthetic tasks, token/chunk/sequence bridges, generated natural language, and local frozen-model diagnostics, pure fixed-state or pure sparse methods fail some overwrite, version, anti-pollution, or no-write-signal cases, while a hybrid covers both routes. A small 2,097,152-token mechanism stress test reaches 50/50 pooled accuracy with 2-132 active chunks. A 2.74M-parameter minimal causal event-token model reaches 595/600 with lite write supervision, supporting proof of trainability rather than scale. A six-family frozen-hidden-state bridge reaches 1079/1080 controlled pointer accuracy, but it uses generator-provided integer key IDs and separately encoded canonical key strings; it is an oracle-metadata probe, not open-text entity resolution. Local non-leaderboard RULER 4K diagnostics remain close to full context, whereas a 33-record LongBench v1 16K subset shows that naive lexical selection is not general. The evidence separates three claims: controlled slot lifecycle is feasible, sparse fallback is needed when writes lack future-query signals, and learned open-domain selection remains the main architectural bottleneck. We do not claim a final generative architecture, global slot-trajectory convergence, or systems superiority.

---


### 99. [Analysis of Adam Algorithms for Stochastic Dynamic Systems](https://arxiv.org/abs/2606.28879)

**<font color=#1a73e8>作者：</font>** Xin Zheng, Yifei Jin, Lei Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The adaptive moment estimation algorithm, known as Adam, is widely used in modern machine learning, owing to its low per-iteration complexity and strong empirical performance. Despite its prevalent use, the theoretical foundation of Adam remains largely unexplored for time-varying and nonstationary systems. In fact, the existing theoretical analyses of Adam-type algorithms are primarily concerned with time-invariant model parameters and explicitly or implicitly rely on independent and identically distributed (i.i.d.) data assumptions, under which the learning taskcan be formulated as minimizing a fixed expected objective with a static minimizer. However, such assumptions are often violated in time-varying and nonstationary systems, thereby calling for a theoretical investigation beyond the conventional yet idealized i.i.d. setting. The main objective of this paper is to solve this challenging problem by establishing a general theory of Adam for time-varying and nonstationary stochastic systems. We will introduce some new techniques for analyzing the products of nonstationary and dependent random matrices induced by Adam's coupled first- and second-moment recursions, and will construct a new stochastic Lyapunov function that blends these two moment dynamics. Under a stochastic excitation condition that allows nonstationary and dependent data, we will derive both parameter tracking and output prediction error bounds explicitly, quantifying the effects of stepsize, first- and second-momentum parameters, gradient noise and parameter drift. These bounds not only provide guarantees for Adam performance, but also provide guidelines for hyperparameter selection. Experiments on both synthetic and real-world data validate our theory and design guidelines.

---


### 100. [An Integrated Machine Learning and Hierarchical Variance Decomposition Pipeline for Student Performance Prediction and Metacognitive Calibration on Multi-Signal Telemetry](https://arxiv.org/abs/2606.28881)

**<font color=#1a73e8>作者：</font>** Gurdeep Singh Virdee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting student performance and characterizing metacognitive calibration are essential for personalization in intelligent tutoring systems. Prior research treats performance prediction, calibration error calculation, and variance decomposition as separate pipelines, preventing unified interpretation. I propose the Unified Behavioral Prediction and Calibration Analysis Pipeline (UBP-CAP), an integrated framework processing student pre-execution behavioral telemetry through three linked modules: (1) a LightGBM classifier with SHAP for binary correctness prediction, (2) formal calibration metrics (ECE, MCE, and Brier score decomposition) to evaluate metacognitive alignment, and (3) a crossed Generalized Linear Mixed-Effects Model (GLMM) for decomposing calibration deviations. I introduce the Predictive-Explanatory Divergence Index (PEDI), which quantifies structural divergence between predictive and explanatory feature profiles. Evaluated on 1,195 interaction records (27 students, 45 tasks), Logistic Regression achieves AUC-ROC = 0.903, outperforming LightGBM (0.878). Student naive ECE (0.109) significantly exceeds model ECE (0.068), confirming systematic miscalibration. The crossed GLMM yields ICCStudent = 0.123, showing calibration is situational rather than dispositional. PEDIcos = 0.081 (p = 0.327) indicates structural alignment between prediction and explanation on shared behavioral features.

---


> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-489](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
