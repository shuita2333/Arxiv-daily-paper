# 📦 其他研究 | 2026年05月08日

> 本类共 **270** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-270](./part-06.md)

---

### 151. [Evidence-based anomaly detection in clinical domains](https://arxiv.org/abs/2605.04664)

**<font color=#1a73e8>作者：</font>** Milos Hauskrecht, Michal Valko, Branislav Kveton 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Anomaly detection methods can be very useful in identifying interesting or concerning events. In this work, we develop and examine new probabilistic anomaly detection methods that let us evaluate management decisions for a specific patient and identify those decisions that are highly unusual with respect to patients with the same or similar condition. The statistics used in this detection are derived from probabilistic models such as Bayesian networks that are learned from a database of past patient cases. We apply our methods to the problem of identifying unusual patient-management decisions in post-surgical cardiac patients.

---


### 152. [Feature importance analysis for patient management decisions](https://arxiv.org/abs/2605.04666)

**<font color=#1a73e8>作者：</font>** Michal Valko, Milos Hauskrecht  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The objective of this paper is to understand what characteristics and features of clinical data influence physician's decision about ordering laboratory tests or prescribing medications the most. We conduct our analysis on data and decisions extracted from electronic health records of 4486 post-surgical cardiac patients. The summary statistics for 335 different lab order decisions and 407 medication decisions are reported. We show that in many cases, physician's lab-order and medication decisions can be well predicted from a small subset of all features.

---


### 153. [ITBoost: Information-Theoretic Trust for Robust Boosting](https://arxiv.org/abs/2605.04671)

**<font color=#1a73e8>作者：</font>** Ye Su, Longlong Zhao, Diego Garcia-Gil 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient boosting remains a strong and widely used method for tabular data learning, but its performance often degrades when training labels are noisy. This behavior is largely related to the way boosting algorithms emphasize samples with large gradients, without explicitly accounting for whether such errors originate from informative hard cases or from unreliable labels. We address this issue by reconsidering how sample reliability is evaluated during boosting. Instead of relying on instantaneous error, we examine the evolution of each sample's residuals across iterations. Based on this insight, we propose Information-Theoretic Trust Boosting (ITBoost), which uses the Minimum Description Length principle to measure the complexity of residual trajectories. Samples whose residual patterns fluctuate in an irregular manner are treated as less trustworthy and are down-weighted during learning. Theoretically, we derive a tighter generalization bound for ITBoost under label noise. Empirical results on various tabular benchmarks indicate that ITBoost provides improved robustness in noisy environments over leading boosting and deep tabular models, while retaining best average performance on clean data.

---


### 154. [Physical Adversarial Clothing Evades Visible-Thermal Detectors via Non-Overlapping RGB-T Pattern](https://arxiv.org/abs/2605.04675)

**<font color=#1a73e8>作者：</font>** Xiaopei Zhu, Guanning Zeng, Zhanhao Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visible-thermal (RGB-T) object detection is a crucial technology for applications such as autonomous driving, where multimodal fusion enhances performance in challenging conditions like low light. However, the security of RGB-T detectors, particularly in the physical world, has been largely overlooked. This paper proposes a novel approach to RGB-T physical attacks using adversarial clothing with a non-overlapping RGB-T pattern (NORP). To simulate full-view (0$^{\circ}$--360$^{\circ}$) RGB-T attacks, we construct 3D RGB-T models for human and adversarial clothing. NORP is a new adversarial pattern design using distinct visible and thermal materials without overlap, avoiding the light reduction in overlapping RGB-T patterns (ORP). To optimize the NORP on adversarial clothing, we propose a spatial discrete-continuous optimization (SDCO) method. We systematically evaluated our method on RGB-T detectors with different fusion architectures, demonstrating high attack success rates both in the digital and physical worlds. Additionally, we introduce a fusion-stage ensemble method that enhances the transferability of adversarial attacks across unseen RGB-T detectors with different fusion architectures.

---


### 155. [Multi-Level Bidirectional Biomimetic Learning for EEG-Based Visual Decoding](https://arxiv.org/abs/2605.04680)

**<font color=#1a73e8>作者：</font>** Jingtao Liu, Peiliang Gong, Chuhang Zheng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> EEG-based visual neural decoding aims to align neural responses with visual stimuli for tasks such as image retrieval. However, limited paired data and a fundamental mismatch between high-fidelity digital images and biological visual perception - distorted by retinotopic mapping and subject-specific neuroanatomy - severely impede cross-modal alignment. To address this, we propose MB2L, a Multi-Level Bidirectional Biomimetic Learning framework that incorporates structured physiological inductive biases into representation learning. Specifically, we propose Adaptive Blur with Visual Priors to mitigate perceptual-structural mismatch by reweighting visual inputs according to retinotopic priors. We further propose Biomimetic Visual Feature Extraction to learn multi-level visual representations consistent with hierarchical cortical processing, enhancing subject-invariant encoding. These modules are jointly optimized via Multi-level Bidirectional Contrastive Learning, which aligns EEG and visual features in a shared semantic space through bidirectional contrastive objectives. Experiments show MB2L achieves 80.5% Top-1 and 97.6% Top-5 accuracy on zero-shot EEG-to-image retrieval, significantly outperforming prior methods and demonstrating strong generalization across subjects and experimental settings.

---


### 156. [HEXST: Hexagonal Shifted-Window Transformer for Spatial Transcriptomics Gene Expression Prediction](https://arxiv.org/abs/2605.04682)

**<font color=#1a73e8>作者：</font>** Keunho Byeon, Jin Tae Kwak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial transcriptomics offers spatially resolved gene expression profiling within tissue sections, but its cost and limited throughput hinder large-scale deployment. To extend this capability to routine practice, recent computational methods aim to infer spatial gene expression directly from ubiquitous hematoxylin and eosin-stained histology slides. However, most existing models assume Cartesian or geometry-agnostic locality, despite the hexagonal sampling of widely used spot-array platforms, and point-wise regression objectives often yield over-smoothed gene expression profiles, obscuring gene-specific spatial heterogeneity. To address these, we propose HEXST, a geometry-aligned Transformer for spatial gene expression prediction from histology. HEXST operates directly on hexagonal spot coordinates to enable efficient local-to-global contextual modeling via tailored shifted-window attention mechanism and hexagonal rotary positional encoding. To enhance gene-wise spatial contrast, HEXST complements point-wise regression with a contrast-sensitive differential objective and transcriptomic priors from a pretrained single-cell foundation model during training. Across seven spatial transcriptomics datasets, HEXST consistently outperforms state-of-the-art models, providing accurate and robust spatial gene expression predictions while preserving gene-wise contrast and spatial heterogeneity.

---


### 157. [Learning Time-Inhomogeneous Markov Dynamics in Financial Time Series via Neural Parameterization](https://arxiv.org/abs/2605.04690)

**<font color=#1a73e8>作者：</font>** Jan Rovirosa, Jesse Schmolze  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modeling the dynamics of non-stationary stochastic systems requires balancing the representational power of deep learning with the mathematical transparency of classical models. While classical Markov transition operators provide explicit, theoretically grounded rules for system evolution, their empirical estimation collapses due to severe data sparsity when applied to high-resolution, high-noise environments. We explore this statistical barrier using financial time series as a canonical, real-world testbed. To overcome the degeneracy of empirical counting, we introduce a framework that utilizes neural networks strictly as parameterization engines to generate explicit, time-varying Markov transition matrices. By constraining the neural network to output its predictions as a formal stochastic operator, we maintain complete structural interpretability. We demonstrate that these learned operators successfully capture complex regime shifts: the state-conditioned model achieves mean row heterogeneity $\bar{\rho} = 0.0073$ while the state-free ablation collapses to exactly zero, and operator row entropy correlates with realized variance at $r = -0.62$ ($p \approx 10^{-251}$), revealing that high-volatility regimes homogenize transition dynamics rather than diversify them. Furthermore, rather than enforcing the Chapman-Kolmogorov equations as a rigid structural requirement, we repurpose them as a localized diagnostic tool to pinpoint specific temporal windows where first-order memory assumptions break down. Ultimately, this framework demonstrates how neural networks can be constrained to make rigorous, classical operator analysis viable for complex real-world time series.

---


### 158. [Gray-Box Poisoning of Continuous Malware Ingestion Pipelines](https://arxiv.org/abs/2605.04698)

**<font color=#1a73e8>作者：</font>** Jan Dolejš, Martin Jureček, Róbert Lórencz  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern malware detection pipelines rely on continuous data ingestion and machine learning to counter the high volume of novel threats. This work investigates a realistic gray-box poisoning threat model targeting these pipelines. Using the secml_malware framework, we generate problem-space adversarial binaries through functionality-preserving manipulations, specifically Import Address Table (IAT) and section injections. We evaluate the impact of these poisoned samples when ingested into a defender's training set for a LightGBM malware detection model. Our empirical results demonstrate that subtle IAT-based perturbations enable compact poisoning samples that significantly degrade detection recall. These findings illustrate the inherent challenge of developing low-visibility adversarial perturbations that maintain high poisoning efficacy within continuous learning systems. We further evaluate a defense mechanism based on a homogeneous ensemble, which successfully identifies and filters up to 95.6% of poisoning attempts while maintaining a high retention rate for legitimate data. These findings emphasize the necessity of robust pre-ingestion validation in production pipelines.

---


### 159. [FaithfulFaces: Pose-Faithful Facial Identity Preservation for Text-to-Video Generation](https://arxiv.org/abs/2605.04702)

**<font color=#1a73e8>作者：</font>** Yuanzhi Wang, Xuhua Ren, Jiaxiang Cheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-preserving text-to-video generation (IPT2V) empowers users to produce diverse and imaginative videos with consistent human facial identity. Despite recent progress, existing methods often suffer from significant identity distortion under large facial pose variations or facial occlusions. In this paper, we propose \textit{FaithfulFaces}, a pose-faithful facial identity preservation learning framework to improve IPT2V in complex dynamic scenes. The key of FaithfulFaces is a pose-shared identity aligner that refines and aligns facial poses across distinct views via a pose-shared dictionary and a pose variation-identity invariance constraint. By mapping single-view inputs into a global facial pose representation with explicit Euler angle embeddings, FaithfulFaces provides a pose-faithful facial prior that guides generative foundations toward robust identity-preserving generation. In particular, we develop a specialized pipeline to curate a high-quality video dataset featuring substantial facial pose diversity. Extensive experiments demonstrate that FaithfulFaces achieves state-of-the-art performance, maintaining superior identity consistency and structural clarity even as pose changes and occlusions occur.

---


### 160. [Vol-Mark: A Watermark for 3D Medical Volume Data Via Cubic Difference Expansion and Contrastive Learning](https://arxiv.org/abs/2605.04705)

**<font color=#1a73e8>作者：</font>** Jiangnan Zhu, Yuntao Wang, Shengli Pan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Today, advances in medical technology extensively utilize 3D volume data for accurate and efficient diagnostics. However, sharing these data across networks in telemedicine poses significant security risks of data tampering and unauthorized copying. To address these challenges, this paper proposes a novel reversible-zero watermarking approach, termed Vol-Mark, for medical volume data to protect their ownership and authenticity in telemedicine. The proposed Vol-Mark method offers two key benefits: 1) it designs a volume data feature extractor that leverages contrastive learning to efficiently extract discriminative and stable volumetric features, ensuring robustness against 3D attacks; 2) it introduces the cubic difference expansion (c-DE) technique, which leverages the 3D integer wavelet transform to embed watermark bits into neighboring voxels within cubes at low-frequency coefficients. The voxel differences within each cube are expanded to create embedding space, and a majority voting mechanism is employed during extraction to enhance reliability. The embedding process incurs low distortion and supports lossless removal, thereby preserving the integrity and diagnostic accuracy of medical volume data. Through these two benefits, Vol-Mark enables both integrity verification and ownership verification. Integrity verification is first performed, and ownership verification through hypothesis testing is further conducted to enhance reliability, particularly under data tampering or watermark removal attacks. Comprehensive experimental results show the effectiveness of the proposed method and its superior robustness against conventional, geometric, and hybrid attacks on medical volume data. In particular, through multiple tasks evaluations, Vol-Mark consistently achieves an ACC above 0.90 in most attack scenarios, outperforming existing methods by a clear margin.

---


### 161. [Differentiable Chemistry in PINNs for Solving Parameterized and Stiff Reaction Systems](https://arxiv.org/abs/2605.04708)

**<font color=#1a73e8>作者：</font>** Miloš Babić, Franz M. Rohrhofer, Stefan Posch  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> From neural ODEs to continuous-time machine learning, differentiable solvers allow physics, optimization, and simulation to become trainable components within deep learning systems. This has opened the path to a new generation of deep learning frameworks for scientific computing, with many promising applications still emerging. In this paper, we integrate a differentiable chemistry solver into a modified physics-informed neural network to solve parameterized reaction systems that are inherently stiff. The proposed framework introduces several key components required to overcome limitations of standard physics-informed neural networks. These include a differentiable chemistry solver, a network architecture for parameterized solutions, and residual weighting tailored to stiff reactions. We evaluate the framework on a set of differential equations related to hydrogen combustion, which include initial/boundary value problems, inverse parameter identification, and a parameterized partial differential equation. Our results highlight the ability of the proposed approach to extend physics-informed neural networks to stiff chemical systems that were previously inaccessible.

---


### 162. [ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC](https://arxiv.org/abs/2605.04709)

**<font color=#1a73e8>作者：</font>** Yurui Du, Pinhao Song, Yutong Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central challenge of visual control with model-based reinforcement learning (RL) is reliable long-horizon planning: long rollouts with learned latent dynamics exhibit branching futures and multi-modal action-value distributions. In addition, compounding model errors amplified by visual occlusions make deep imagination brittle. We present ELVIS, a latent model predictive controller (MPC) designed to make long-horizon planning practical. ELVIS plans in a Dreamer-style recurrent state space model (RSSM) and replaces standard unimodal model predictive path integral (MPPI) with a Gaussian-mixture MPPI that maintains multiple coherent hypotheses over long horizons, avoiding mode averaging under branching rollouts. In parallel, ELVIS stabilizes deep imagination with a shared uncertainty-aware lambda-return: an ensemble of latent critics defines an upper-confidence-bound (UCB) score that gates a time-varying lambda, adaptively trading off bootstrapping versus look-ahead to limit compounding error during planning. The same return is used both to train an actor-critic prior from imagined rollouts and to score candidate trajectories inside GMM-MPPI, aligning RL objectives with the planner's long-horizon optimization. On fourteen DeepMind Control Suite visual tasks, ELVIS establishes state-of-the-art performance compared with TD-MPC2 and DreamerV3. Finally, ELVIS transfers zero-shot to a real-world sand-spraying task with severe occlusions, improving surface-quality metrics and demonstrating robustness beyond simulation.

---


### 163. [Budget-aware Auto Optimizer Configurator](https://arxiv.org/abs/2605.04711)

**<font color=#1a73e8>作者：</font>** Kang Liu, Wei Peng, Jianchen Hu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optimizer states occupy massive GPU memory in large-scale model training. However, gradients in different network blocks exhibit distinct behaviors, such as varying directional stability and scale anisotropy, implying that expensive optimizer states are not universally necessary and using a global optimizer is often memory-inefficient. We propose the Budget-Aware Optimizer Configurator (BAOC) to reduce memory cost by assigning suitable optimizer configurations to individual blocks under given budgets. Specifically, BAOC samples gradient streams to derive statistical metrics that quantify the potential performance risk of applying cheaper configurations (e.g., low precision or removing momentum). It then solves a constrained allocation problem to minimize total risk under memory and time budgets, selecting a budget-feasible configuration for each block. Experiments across vision, language, and diffusion workloads demonstrate that BAOC maintains training quality while significantly reducing the memory usage of optimizer states. The code is available at this https URL.

---


### 164. [SPHERE: Mitigating the Loss of Spectral Plasticity in Mixture-of-Experts for Deep Reinforcement Learning](https://arxiv.org/abs/2605.04712)

**<font color=#1a73e8>作者：</font>** Lirui Luo, Guoxi Zhang, Hongming Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In deep reinforcement learning (DRL), an agent is trained from a stream of experience. In a continual learning setting, such agents can suffer from plasticity loss: their ability to learn new skills from new experiences diminishes over training. Recently, Mixture-of-Experts (MoE) networks have been reported to enable scaling laws and facilitate the learning of diverse skills. However, in continual reinforcement learning settings, their performance can degenerate as learning proceeds, indicating a loss of plasticity. To address this, building on Neural Tangent Kernel (NTK) theory, we formalize the plasticity loss in MoE policies as a loss of spectral plasticity. We then derive a tractable proxy for spectral plasticity, one expressible in terms of individual expert feature matrices. Leveraging this proxy, we introduce SPHERE, a practical Parseval penalty tailored for MoE-based policies that alleviates the loss of spectral plasticity. On MetaWorld and HumanoidBench, SPHERE improves average success under continual RL by 133% and 50% over an unregularized MoE baseline, while maintaining higher spectral plasticity throughout training.

---


### 165. [Not Every Subject Should Stay: Machine Unlearning for Noisy Engagement Recognition](https://arxiv.org/abs/2605.04713)

**<font color=#1a73e8>作者：</font>** Alexander Vedernikov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Engagement recognition datasets are typically subject-indexed and often contain noisy, subjective supervision, making post-hoc dataset revision a practical problem. Existing noisy-label and data-cleaning methods largely operate at the sample level before or during training, but do not directly address a different question: once a model has already been trained, can the influence of an entire problematic subject be removed without full retraining? We study this setting through subject-level machine unlearning as a post-hoc sanitization mechanism for engagement recognition. Starting from a baseline trained on all subjects, we rank candidate harmful subjects using a model-dependent proxy, apply a lightweight approximate unlearning update, and compare the result against an oracle model retrained from scratch on the retained subjects only. We instantiate this protocol on DAiSEE and EngageNet using Tensor-Convolution and Convolution-Transformer Network (TCCT-Net) as a fixed platform and evaluate three matched model states under the same removal scenario: baseline, unlearned, and oracle. In representative K=3 forget-set settings, the unlearned model recovers 89.3% and 92.5% of the oracle gain on EngageNet and DAiSEE, respectively, at roughly one quarter of retraining cost. Across the tested small-audit regimes, effectiveness is strongest at an intermediate forget-set size, indicating that approximate subject-level unlearning is a useful low-cost correction mechanism, but one whose benefit depends on subject selection quality and removal regime.

---


### 166. [Every Step Counts: Step-Level Credit Assignment for Tool-Integrated Text-to-SQL](https://arxiv.org/abs/2605.04719)

**<font color=#1a73e8>作者：</font>** Yaxun Dai, Baolin Sun, Junying Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool-integrated Text-to-SQL parsing has emerged as a promising paradigm, framing SQL generation as a sequential decision-making process interleaved with tool execution. However, existing reinforcement learning approaches mainly rely on coarse-grained outcome supervision, resulting in a fundamental credit assignment problem: models receive the same reward for any trajectory that yields the correct answer, even when intermediate steps are redundant, inefficient, or erroneous. Consequently, models are encouraged to explore suboptimal reasoning spaces, limiting both efficiency and generalization. To address this problem, we propose FineStep, a novel framework for step-level credit assignment in tool-augmented Text-to-SQL. First, we introduce a reward design with independent process rewards to alleviate the signal sparsity of outcome supervision. Next, we present a step-level credit assignment mechanism to precisely quantify the value of each reasoning step. Finally, we develop a policy optimization method based on step-level advantages for efficient updates. Extensive experiments on BIRD benchmarks show that FineStep achieves state-of-the-art performance and reduces redundant tool interactions, with a 3.25% average EX gain over GRPO at the 4B scale.

---


### 167. [Exact Dual Geometry of SOC-ICNN Value Functions](https://arxiv.org/abs/2605.04722)

**<font color=#1a73e8>作者：</font>** Kang Liu, Jianchen Hu, Wei Peng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Input Convex Neural Networks (ICNNs) are commonly used in a two-stage manner: one first trains a convex network and then minimizes it over its input in a downstream inference problem. Recent second-order-cone ICNNs (SOC-ICNNs) enrich ReLU-based ICNNs with quadratic and conic modules and admit an exact representation as value functions of second-order cone programs (SOCPs). This value-function structure enables an explicit convex-analytic treatment of SOC-ICNN inference. In this paper, we study the exact first-order and local second-order geometry of SOC-ICNNs from the dual viewpoint. We show that supporting slopes, subdifferentials, directional derivatives, and local Hessians can be recovered directly from optimal dual variables. These results provide the geometric primitives for white-box SOC-ICNN inference, going beyond black-box automatic differentiation. Numerical experiments validate the exact multiplier readout, the local Hessian formula, and the set-valued behavior at structurally degenerate inputs. We also provide a step-by-step tutorial showing how the readout mechanism instantiates a complete white-box inference loop. The code is available at this https URL.

---


### 168. [From Beats to Breaches:How Offensive AI Infers Sensitive User Information from Playlists](https://arxiv.org/abs/2605.04724)

**<font color=#1a73e8>作者：</font>** Stefano Cecconello, Mauro Conti, Luca Pajola 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The pervasive integration of AI has enabled Offensive AI: the exploitation of AI for malicious ends across the cyber-kill chain. A critical manifestation is the user attribute inference attack, where AI infers sensitive Personally Identifiable Information (PII) from innocuous public data. We explore how music streaming ecosystems, where users routinely release public playlists, can be exploited for Offensive AI. To quantify this threat, we developed musicPIIrate. This novel tool leverages deep learning architectures that utilize both standalone data representations and the structural information embedded in a user's playlist collection. Our design explores set-based approaches (e.g., Deep Sets) and methodologies modeling relationships between playlists (e.g., Graph Neural Networks), which we also combine to leverage both perspectives. Our approach addresses feature extraction from unordered, variable-length set data, enabling accurate PII prediction.
Empirical evaluation demonstrates that musicPIIrate achieves state-of-the-art inference accuracy. The tool successfully infers a wide array of attributes, including: Demographics (Age, Country, Gender), Habits (Alcohol, Smoke, Sport), and Personality Traits (OCEAN scores). musicPIIrate outperforms existing methods, beating baselines in 9 out of 15 attribute inference tasks. To counter this vulnerability, we propose JamShield, a lightweight defensive framework. JamShield strategically injects dummy playlists into an account to dilute the PII-carrying signal. Our analysis indicates that JamShield represents a promising defense, lowering inference F1-scores by an average of 10%. This work provides an initial Offensive-AI benchmark for playlist-based PII inference using architectures that leverage set- and graph-structured data and introduces a defense showing encouraging mitigation effects.

---


### 169. [Ensuring Reliability in Programming Knowledge Tracing: A Re-evaluation of Attention-augmented Models and Experimental Protocols](https://arxiv.org/abs/2605.04727)

**<font color=#1a73e8>作者：</font>** Jaewook Kim, Hyeoncheol Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Programming Knowledge Tracing (PKT) has recently advanced through hybrid approaches that integrate attention-based feature modeling for code representation with RNN-based sequential prediction. While these models report strong empirical performance, their reliability can be sensitive to subtle implementation and experimental design choices. This study revisits representative PKT models and shows that reported gains can be substantially influenced by model configuration and sequence construction practices. We identify issues in attention dimension settings that affect performance estimates, and demonstrate that improper ordering of student attempts, such as ignoring ServerTimestamp, can violate temporal causality and lead to overly optimistic results. To ensure consistent evaluation, hyperparameters are selected via grid search guided by a single designated fold and then fixed uniformly across all folds during cross-validation. We further analyze the role of assignment-wise characteristics and systematically explore the impact of maximum sequence length. Using this protocol, we re-evaluate PKT models on the CodeWorkout dataset. Our results show that, under controlled and consistent settings, the performance gap between attention-enhanced models and standard DKT is significantly reduced, and increased architectural complexity does not consistently translate into superior performance. Beyond individual model comparisons, this work provides practical guidance for reliable and comparable evaluation in programming knowledge tracing.

---


### 170. [Anny-Fit: All-Age Human Mesh Recovery](https://arxiv.org/abs/2605.04728)

**<font color=#1a73e8>作者：</font>** Laura Bravo-Sánchez, Matthieu Armando, Romain Brégier 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering 3D human pose and shape from a single image remains a cornerstone of human-centric vision, yet most methods assume adult subjects and optimize each person independently. These assumptions fail in real-world, all-age scenes, where body proportions and depth must be resolved jointly. We introduce Anny-Fit, a multi-person, camera-space optimization framework for all-age 3D human mesh recovery (HMR). Unlike existing per-person fitting methods, Anny-Fit jointly optimizes all individuals directly in the camera coordinate system, enforcing global spatial consistency. At the core of our approach is the use of multiple forms of expert knowledge -- including metric depth maps, instance segmentation, 2D keypoints, and, VLM-derived semantic attributes such as age and gender -- each obtained from dedicated off-the-shelf networks. These complementary signals jointly guide the optimization, constraining the depth-scale ambiguity characteristic of all-age scenes. Across diverse datasets, Anny-Fit consistently improves 2D reprojection accuracy (+13 to 16), relative depth ordering (+6 to 7), 3D estimation error (-9 to -29) and shape estimation (+25 to +82), producing more coherent scenes. Finally, we show that VLM-based semantic knowledge can be distilled into an HMR model via the pseudo-ground-truth annotations produced by Anny-Fit on training data, enabling it to learn semantically meaningful shape parameters while improving HMR performance. Our approach bridges adult-only and all-age modeling by enabling zero-shot adaptation of adult-trained HMR pipelines to the full age spectrum without retraining. Code is publicly available at this https URL.

---


### 171. [ULF-Loc: Unbiased Landmark Feature for Robust Visual Localization with 3D Gaussian Splatting](https://arxiv.org/abs/2605.04730)

**<font color=#1a73e8>作者：</font>** Yingdong Gu, Shaocheng Yan, Zhenjun Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual localization is a core technology for augmented reality and autonomous navigation. Recent methods combine the efficient rendering of 3D Gaussian Splatting (3DGS) with feature-based localization. These methods rely on direct matching between 2D query features and the 3D Gaussian feature field, but this often results in mismatches due to an inherent bias in the learned Gaussian feature. We theoretically analyze the feature learning process in 3DGS, revealing that the widely adopted $\alpha$-blending optimization inherently introduces bias into 3D point features. This bias stems from the entanglement between individual Gaussians and their neighboring Gaussians, making the learned features unsuitable for precise matching tasks. Motivated by these findings, we propose ULF-Loc, an unbiased landmark feature framework that replaces biased feature optimization with geometry-weighted feature fusion. We further introduce keypoint-consensus landmark sampling to select reliable Gaussians and local geometric consistency verification to reject mismatches caused by rendering artifacts. On the Cambridge Landmarks dataset, ULF-Loc reduces the mean median translation error by 17\% compared to the state-of-the-art, while achieving superior efficiency with only 1/10 the training time and 1/6 the GPU memory of STDLoc.

---


### 172. [Morphology-Guided Cross-Task Coupling for Joint Building Height and Footprint Estimation](https://arxiv.org/abs/2605.04731)

**<font color=#1a73e8>作者：</font>** Jinzhen Han, JinByeong Lee, Jisung Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building height (BH) and building footprint (BF) jointly describe the vertical and horizontal extent of the built environment and are required inputs for urban climate, disaster-risk, and population-mapping models. The two parameters are coupled through floor-area-ratio (FAR) constraints, yet remote-sensing approaches typically treat them as independent regression targets. We argue that explicitly encoding this cross-task coupling is more impactful than further refining individual encoders, and propose MorphoFormer, a joint BH/BF estimation framework built around two complementary mechanisms: (i) a BF-Guided Task Decoder (BGTD) that gates the height branch via cross-attention on a footprint-derived morphology context, and (ii) a Morphology Consistency Loss (MCL) that supervises a height-from-footprint surrogate against the ground-truth BH, indirectly forcing the BF feature to encode height-correlated structure. The encoder is a single-stage Swin backbone fed by Sentinel-1 SAR, Sentinel-2 multispectral, and DEM inputs, trained and evaluated on a geo-blocked split of 54 cities. Against a Swin-MTL baseline at identical receptive field, MorphoFormer reduces BH test RMSE from 3.39 to 3.15 m (R^2 improves 0.62 -> 0.67) with BF R^2 stable at 0.80. Controlled ablations at identical capacity attribute most of this 0.24 m improvement to the two proposed mechanisms: removing BGTD raises BH RMSE by 0.11 m and removing MCL raises it by 0.11 m, with the residual approximately 0.02 m falling within the noise floor of encoder-side variations. Because both mechanisms act on cross-task representations rather than pixels, the design carries no intrinsic dependence on input resolution.

---


### 173. [Using Common Random Numbers for Simulation-based Planning with Rollouts](https://arxiv.org/abs/2605.04732)

**<font color=#1a73e8>作者：</font>** Sandarbh Yadav, Frederic J Maliakkal, Harshad Khadilkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation-based planning with rollouts is a widely-deployed technique for decision making in stochastic environments. The primary instrument of simulation-based planning is a sampling model, which is repeatedly called to generate trajectories and estimate the utilities of available actions. Among the actions thus explored, one with the maximum estimated utility is then executed. In this paper, we examine the effect of using common random numbers in the simulation process. We obtain a simple recipe for (provably) reducing variance in relative utility when simulations invoke a rollout policy beyond some depth. Experiments on synthetic tasks confirm that our scheme improves task performance. The broader significance of our innovation is apparent from two practical applications: (1) single-step lookahead planning in a pension-disbursement task, and (2) a deployment of the well-known UCT algorithm for the game of Ludo.

---


### 174. [Hierarachical Multiagent Reinforcement Learning for Multi-Group Tax Game](https://arxiv.org/abs/2605.04741)

**<font color=#1a73e8>作者：</font>** Honglei Guo, Yuhan Zhao, Yexin Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has increasingly been used to study economic decision-making, such as taxation, public spending, and labour supply. However, most existing RL-based economic models focus on a single government--household group, thereby overlooking the strategic interactions that arise when multiple governments compete while managing their own populations. In practice, many economic systems (e.g., taxation) exhibit a multi-group structure, where each government must optimize its fiscal policy in response not only to household behaviour within its jurisdiction, but also to the policies of other competing governments. To capture this structure, we formulate taxation as a hierarchical multi-group game. Within each group, the interaction between the government and households is modelled as a leader--follower game; across groups, governments are modelled as players in a competitive game. This results in a hybrid hierarchical game that is difficult to solve using standard multi-agent reinforcement learning algorithms. We therefore propose a bi-level training framework built on multi-agent reinforcement learning, together with \textit{ Curriculum Learning} and a \textit{ Closed-Loop Sequential Update} strategy, to stabilize training and promote convergence. We instantiate this framework in a taxation game simulation environment grounded in classical economic models. The environment supports the evaluation of different taxation algorithms and provides multiple economic indicators for assessing policy performance. Experiments show that our approach can learn stable tax policies that benefit all participating groups. Compared with a two-group baseline without the proposed update mechanisms, our method avoids premature game collapse, extends the effective game duration by 60.92\%, produces more sustainable and robust tax policies, and reduces GDP disparities among governments by 44.12\%.

---


### 175. [MixINN: Accelerating Plant Breeding by Combining Mixed Models and Deep Learning for Interaction Prediction](https://arxiv.org/abs/2605.04744)

**<font color=#1a73e8>作者：</font>** Aike Potze, Fred van Eeuwijk, Ioannis N. Athanasiadis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Plant breeding underpins global food security through incremental, accumulating improvements in crop yield, quality and sustainability, achieved via repeated cycles of crop ranking, selection and crossing. Climate change disrupts this process by altering local growing conditions, thereby shifting the relative performance of crop genotypes. Predicting these relative changes in yield is critical for food security. Yet, this problem remains an open challenge in plant breeding, and relatively unexplored within the AI community. We propose MixINN, an approach that first isolates high-quality genotype-environment interaction labels using mixed models, and then predicts these interactions for new crop varieties in future environmental conditions with a deep neural network. We evaluate our method on a corn multi-environment trial across the continental United States and show improved prediction of genotype ranking over current plant breeding methods. MixINN demonstrated superior performance in identifying the 20% most productive corn genotypes, leading to a 5.8% higher average yield, which further improved to 7.2% when targeting specific growing environments. These are competitive results for real-world breeding programs, demonstrating the potential of AI research in accelerating the development of climate-adapted crops, and improving future food security under climate change.

---


### 176. [Knowledge-Free Correlated Agreement for Incentivizing Federated Learning](https://arxiv.org/abs/2605.04747)

**<font color=#1a73e8>作者：</font>** Leon Witt, Togrul Abbasli, Kentaroh Toyoda 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Knowledge-Free Correlated Agreement (KFCA) to reward client contributions in federated learning (FL) without relying on ground truth, a public test set, or distribution knowledge. Under categorical reports and an honest majority, KFCA is strictly truthful, addressing the label-flipping vulnerability of Correlated Agreement (CA). We evaluate KFCA on federated LLM adapter tuning and a real-world PCB inspection task, showing efficient real-time reward computation suitable for decentralized and blockchain-based incentive designs.

---


### 177. [VC-FeS: Viewpoint-Conditioned Feature Selection for Vehicle Re-identification in Thermal Vision](https://arxiv.org/abs/2605.04750)

**<font color=#1a73e8>作者：</font>** Yasod Ginige, Ransika Gunasekara, Darsha Hewavitharana 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identification of less-articulated objects using single-channel images, such as thermal images, is important in many applications, such as surveillance. However, in this domain, existing methods show poor performance due to high similarity among objects of the same category in the absence of color information (overlooking shape information) and de-emphasized texture information. Furthermore, variability in viewpoint adds more complexity as the features vary from side to side. We address these issues by constructing viewpoint-conditioned feature vectors and area-specific feature comparisons in separate feature spaces. These interventions enable leveraging the advancements of existing RGB-pre-trained ViT feature extractors while effectively adapting them to address the challenges specific to the thermal domain. We test our system with RGBNT100 (IR) vehicle dataset and a thermal maritime dataset acquired by us. Our results surpass the state-of-the-art methods by 19.7% and 12.8% for the above datasets in mAP scores, respectively. We also plan to make our thermal dataset available, the first of its kind for maritime vessel identification.

---


### 178. [Hybrid Congestion Classification Framework Using Flow-Guided Attention and Empirical Mode Decomposition](https://arxiv.org/abs/2605.04752)

**<font color=#1a73e8>作者：</font>** Eugene Kofi Okrah Denteh, Blessing Agyei Kyem, Joshua Kofi Asamoah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate traffic congestion classification requires models that jointly capture roadway scene context and non-stationary traffic motion, yet most prior work treats these requirements in isolation. Vision-based methods often depend on appearance cues with standard temporal pooling, which can bias predictions toward static infrastructure, whereas signal-based approaches characterize temporal dynamics but lack the spatial context needed for scene-level localization. These complementary limitations motivate a unified framework that links motion evidence to spatial feature selection while preserving data-adaptive temporal characterization. This study therefore proposes FLO-EMD, a hybrid approach that couples motion-guided attention with empirical, data-driven temporal decomposition. Dense optical flow guides channel and spatial attention so that RGB features are refined toward motion-relevant regions. In parallel, aggregated flow statistics form compact motion traces that are decomposed using Empirical Mode Decomposition (EMD) to extract intrinsic temporal components. The resulting EMD embedding is fused with learned spatiotemporal representations to classify light, medium, and heavy congestion. Experiments on 1,050 five-second clips from four surveillance networks show that FLO-EMD achieves 97.5% overall test accuracy (weighted F1 = 0.9742), outperforming established baselines and remaining robust across diverse environmental conditions; ablation and sensitivity analyses further quantify the contributions of EMD, the number of intrinsic mode functions, and the selected motion descriptors.

---


### 179. [AFL-ICP: Enhancing Industrial Control Protocol Reliability via Specification-Guided Fuzzing](https://arxiv.org/abs/2605.04760)

**<font color=#1a73e8>作者：</font>** Jiaying Meng, Xuewei Feng, Qi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Industrial Control Protocols (ICPs) are critical to the reliability and stability of industrial infrastructure, yet their security is fundamentally compromised by a specification-blindness bottleneck. Modern fuzzers, constrained by observation-driven inference, struggle to penetrate deep protocol states or detect subtle semantic deviations. In this paper, we present AFL-ICP, an autonomous fuzzing framework that pioneers a specification-driven paradigm. AFL-ICP features a context-aware specification formalization pipeline to transform complex specifications into rigorous machine-executable grammars. Building on this formalized specification, AFL-ICP leverages LLMs to enable automated protocol adaptation and seed generation, allowing for rapid extension to new protocols with minimal manual effort. Additionally, it includes an LLM-powered differential checker that cross-references implementation outputs with specification requirements to detect subtle semantic and logic bugs that existing fuzzers cannot detect. We implement AFL-ICP and evaluate it on four widely used ICPs, including both open-source and closed-source variants. Results show that AFL-ICP significantly outperforms state-of-the-art fuzzers in coverage and uncovers 24 previously unknown vulnerabilities, for which we have received acknowledgments from affected vendors (e.g., FreyrSCADA). Specifically, the identified vulnerabilities include 16 semantic and logic bugs that can silently disrupt industrial operations and degrade service availability.

---


### 180. [Gaze4HRI: Zero-shot Benchmarking Gaze Estimation Neural-Networks for Human-Robot Interaction](https://arxiv.org/abs/2605.04770)

**<font color=#1a73e8>作者：</font>** Berk Sezer, Ali Görkem Küçük, Erol Şahin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While zero-shot appearance-based 3D gaze estimation offers significant cost-efficiency by directly mapping RGB images to gaze vectors, its reliability in Human-Robot Interaction (HRI) settings remains uncertain. Existing benchmarks frequently overlook fundamental HRI conditions, such as dynamic camera viewpoints and moving targets in video. Furthermore, current cross-dataset evaluations often suffer from a complexity gap, where methods trained on diverse datasets are tested on significantly smaller and less varied sets, failing to assess true robustness. To bridge these gaps, we introduce Gaze4HRI, a large-scale dataset (50+ subjects, 3,000+ videos, 600,000+ frames) designed to evaluate state-of-the-art performance against critical HRI variables: illumination, head-gaze conflict, as well as the motion of camera and gaze target in video. Our benchmark reveals that all evaluated methods fail in at least one condition, identifying steeply-downward gaze as a universal failure point. Notably, PureGaze trained on the ETH-X-Gaze dataset uniquely maintains resilience across all other conditions. These results challenge the recent focus in the literature on complex spatial-temporal modeling and Transformer-based architectures. Instead, our findings suggest that extensive data diversity, as exemplified by the ETH-X-Gaze dataset, serves as the primary driver of zero-shot robustness in unconstrained environments, while resilience-enhancing frameworks, such as PureGaze's self-adversarial loss for gaze feature purification, provide a substantial further improvement. Ultimately, this study establishes a rigorous benchmark that provides practical guidelines for practitioners as well as reshaping future research. The dataset and codes are available at this https URL.

---


### 181. [Long-Term Risks of IoT Devices: The Case of the Smart Fridge](https://arxiv.org/abs/2605.04787)

**<font color=#1a73e8>作者：</font>** Erik Buchmann  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Replacing conventional devices with smart ones has many advantages, e.g., a seamless integration of physical objects into the users digital environment or improved modes of use. However, if a conventional device is replaced by a smart device, its IT components can cause risks, that shorten the life of the device. Such risks stem from different life cycles of embedded soft- and hardware, libraries and protocols used, and the IT ecosystem required. This is problematic, because many conventional household appliances, say, a fridge or TV, have a much longer life span than typical IT equipment. In this paper, we use a systematic approach to identify long-term risks for the operational life span of a smart fridge. In particular, we identify 8 different use cases of three typical smart fridges, e.g., cooling or managing "best before" dates. We model the IT ecosystem needed to run these use cases, and we inspect each asset in this ecosystem for potential long-term risks. We found that even cooling, the most basic use case, is at risk in the long run. This is because the setting cooling parameters may depend on parts of the IT ecosystem that are not under the users control. On the other hand, we did not find any risk that may lead to harm of the category "threatening". Our findings on the smart fridge can be generalized to other smart devices easily.

---


### 182. [Bilinear Mamba-Koopman Neural MPC for Varying Dynamics](https://arxiv.org/abs/2605.04793)

**<font color=#1a73e8>作者：</font>** Matan Pagi, Zohar Sorek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Koopman-based neural MPC models generate time-varying dynamics from historical data, but preserve convexity by enforcing that the system operator is independent of the current control input. This conditional independence constraint limits adaptation to changing dynamics within a single MPC horizon, particularly under time-varying conditions and under stale-plan execution.
We propose Bilinear Mamba-Koopman Neural MPC, a minimal extension that introduces control-dependent coupling in the latent dynamics, allowing the effective operator to adapt to the current input. The resulting model is a strict generalization of the standard linear, conditional-independence formulation, adds less than 1% parameters through a low-rank structure, and admits exact model Jacobians that enable efficient Sequential Convex Programming (SCP) with monotone-descent and KKT convergence results under standard trust-region assumptions.
Across CartPole and RSCP benchmarks in time-invariant and time-varying regimes, the proposed model matches or improves forecasting accuracy on every cell when training noise is averaged out, with strict gains where control-state coupling is structurally present. Its main closed-loop gains appear in the RSCP TV task, where iterative SCP improves adaptation within the horizon and substantially stabilizes training; in CartPole TV, the gains are modest but consistent. In delayed re-planning experiments on the time-varying variants, the bilinear model degrades more gracefully under stale-plan execution, maintaining a consistent advantage on CartPole TV and a substantially larger robustness margin on RSCP TV. These results show that control-dependent latent dynamics provide a simple and effective mechanism for robust MPC under varying conditions.

---


### 183. [DecodingTrust-Agent Platform (DTap): A Controllable and Interactive Red-Teaming Platform for AI Agents](https://arxiv.org/abs/2605.04808)

**<font color=#1a73e8>作者：</font>** Zhaorun Chen, Xun Liu, Haibo Tong 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly deployed across diverse domains to automate complex workflows through long-horizon and high-stakes action executions. Due to their high capability and flexibility, such agents raise significant security and safety concerns. A growing number of real-world incidents have shown that adversaries can easily manipulate agents into performing harmful actions, such as leaking API keys, deleting user data, or initiating unauthorized transactions. Evaluating agent security is inherently challenging, as agents operate in dynamic, untrusted environments involving external tools, heterogeneous data sources, and frequent user interactions. However, realistic, controllable, and reproducible environments for large-scale risk assessment remain largely underexplored. To address this gap, we introduce the DecodingTrust-Agent Platform (DTap), the first controllable and interactive red-teaming platform for AI agents, spanning 14 real-world domains and over 50 simulation environments that replicate widely used systems such as Google Workspace, Paypal, and Slack. To scale the risk assessment of agents in DTap, we further propose DTap-Red, the first autonomous red-teaming agent that systematically explores diverse injection vectors (e.g., prompt, tool, skill, environment, combinations) and autonomously discovers effective attack strategies tailored to varying malicious goals. Using DTap-Red, we curate DTap-Bench, a large-scale red-teaming dataset comprising high-quality instances across domains, each paired with a verifiable judge to automatically validate attack outcomes. Through DTap, we conduct large-scale evaluations of popular AI agents built on various backbone models, spanning security policies, risk categories, and attack strategies, revealing systematic vulnerability patterns and providing valuable insights for developing secure next-generation agents.

---


### 184. [Tree-based Credit Assignment for Multi-Agent Memory System](https://arxiv.org/abs/2605.04811)

**<font color=#1a73e8>作者：</font>** Marina Mao, Alexandr Liu, Pengbo Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Memory systems are widely adopted to enhance LLMs for long-horizon tasks, and are commonly organized as multi-agent pipelines with memory building, summarizing, and retrieval agents. To empower this system, existing RL-based methods either apply final downstream task rewards (e.g., QA accuracy) for all agents uniformly, which are coarse and ambiguous, or design task-specific rewards for agents on different subtasks, which require costly annotations (e.g., key evidence) and are difficult to define reliably. To address these limitations, we propose Tree-based Credit Assignment for Multi-Agent Memory Systems (TreeMem), which derives agent-specific credit from the final reward without task-specific annotations. Specifically, TreeMem extends the multi-agent pipeline (builder--summarizer--retrieval) into a tree structure, where each agent's outputs are expanded into multiple subsequent branches. The contribution of each agent is estimated via Monte Carlo averaging over its subsequent branches, capturing how intermediate agent actions may influence the final reward. This converts the coarse final reward into agent-specific optimization signals. These signals are then used to update all agent policies simultaneously, helping heterogeneous agents specialize effectively. Experiments on long-horizon benchmarks show that TreeMem improves memory system performance over strong baselines, validating the effectiveness of tree-structured credit assignment for the multi-agent memory system.

---


### 185. [A Biased Nonnegative Block Term Tensor Decomposition Model for Dynamic QoS Prediction](https://arxiv.org/abs/2605.04813)

**<font color=#1a73e8>作者：</font>** Wenjing Liu, Yujia Lei, Qu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the rapid development of cloud computing and Web services, Quality of Service (QoS) has become a key criterion for service selection and recommendation. Tensor latent feature analysis provides an effective way to model multidimensional QoS data, and most existing QoS prediction methods are mainly based on Canonical Polyadic (CP) decomposition or Tucker decomposition. However, constrained by their inherent structural properties, these methods cannot accurately capture the complex and dynamic dependencies in user-service interactions, which limits their prediction performance. To address this issue, this paper proposes a dynamic QoS prediction framework based on the Biased Nonnegative Block Term Tensor Decomposition Model, termed BNBT. Specifically, the proposed framework is developed from three aspects: (1) block term tensor decomposition is employed to enhance the representation capability of latent feature learning; (2) linear bias terms are incorporated to further improve prediction accuracy; and (3) a tensor-oriented single-element-dependent nonnegative multiplicative update algorithm, called SLF-NMUT, is designed for efficient parameter estimation. Extensive experiments on real-world QoS datasets demonstrate that the proposed BNBT framework consistently outperforms several state-of-the-art QoS prediction methods in terms of prediction accuracy.

---


### 186. [Building AI Companions that Prioritise Learning over Performance](https://arxiv.org/abs/2605.04816)

**<font color=#1a73e8>作者：</font>** Hassan Khosravi, Dragan Gasevic, Shazia Sadiq 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are rapidly transforming knowledge work by improving the quality and efficiency of tasks such as writing, coding, and data analysis. However, their growing use in education has exposed a learning-performance paradox: while they can enhance short-term task performance, they may also undermine genuine learning, including cognitive growth, knowledge transfer, and metacognitive development. This paper addresses the question of how artificial intelligence should be designed and used to support learning rather than merely improve immediate outputs. We introduce the concept of AI learning companions, defined as adaptive, pedagogically informed, LLM-powered agents designed for integration into learning environments. We propose a framework for their design built on three interrelated foundations: a pedagogical foundation focused on how students learn with AI, an adaptive foundation focused on how AI learns about students, and a responsible design foundation ensuring systems remain transparent, accountable, inclusive, and secure. The framework is illustrated through five case studies spanning diverse educational contexts, levels, and tool designs, revealing both the promise and current limitations of existing tools. We conclude that there is a necessary shift away from LLMs designed for task-oriented performance, and beyond simply prompting them to act as tutors, toward deliberately developed AI learning companions that are pedagogically sound, adapt to their learners, and foster durable understanding, metacognitive growth, and learner agency.

---


### 187. [Unsat Core Prediction through Polarity-Aware Representation Learning over Clause-Literal Hypergraphs](https://arxiv.org/abs/2605.04819)

**<font color=#1a73e8>作者：</font>** Zhenchao Sun, Shuai Ma, Ping Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks have been widely used in Boolean satisfiability (SAT) tasks to learn structural information from SAT formulas. The goal of these studies is to solve SAT instances or to enhance SAT solvers, including tasks such as unsat-core prediction. However, most existing approaches model a SAT formula as a bipartite graph or a directed acyclic graph, which are less expressive in capturing higher-order interactions among literals and clauses. Moreover, these approaches are limited in modeling intrinsic polarity-related properties of SAT, such as the complementary relationship between the positive and negative literals of a variable. To address these limitations, we propose a polarity-aware representation learning framework over clause-literal hypergraphs. We model SAT formulas as clause-literal hypergraphs augmented with a clause incidence graph to capture higher-order structural interactions. We then introduce a polarity-aware decomposed mechanism that separates variable representations into polarity invariant and equivariant components, explicitly modeling the relationship between positive and negative literals, with the resulting literal representations propagated along the hypergraph structure. We further incorporate a polarity-inversion consistency regularization to reinforce polarity-consistent representations during training. Experimental results on multiple SAT datasets demonstrate the effectiveness of the proposed approach.

---


### 188. [Trustworthy Federated Label Distribution Learning under Annotation Quality Disparity](https://arxiv.org/abs/2605.04827)

**<font color=#1a73e8>作者：</font>** Junxiang Wu, Zhiqiang Kou, Hongwei Zeng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Label Distribution Learning (LDL) models supervision as an instance-wise probability distribution, enabling fine-grained learning under inherent ambiguity, but its success relies on high-fidelity label distributions that are costly to obtain and thus often noisy. Motivated by privacy-sensitive applications, we study Federated Label Distribution Learning (Fed-LDL), where data isolation further induces heterogeneous annotation quality across clients, making local updates unevenly reliable and breaking sample-size-based aggregation (e.g., FedAvg). To address this trust dilemma, we propose FedQual, a quality-aware Fed-LDL framework with two coupled mechanisms: (i) quality-adaptive client training guided by a global semantic anchor that calibrates low-quality clients while preserving high-quality autonomy, and (ii) reliability-aware server aggregation that reweights client contributions by effective reliable information rather than raw sample size. To enable rigorous evaluation, we construct four new Fed-LDL benchmarks (FER-LDL, FI-LDL, PIPAL-LDL, and KADID-LDL) with controlled annotation quality disparity. We further provide a theoretical guarantee showing that under heterogeneous supervision quality, client-specific calibration is strictly better than any uniform calibration. Extensive experiments on the proposed benchmarks demonstrate the effectiveness of FedQual.

---


### 189. [Concurrence of Symmetry Breaking and Nonlocality Phase Transitions in Diffusion Models](https://arxiv.org/abs/2605.04830)

**<font color=#1a73e8>作者：</font>** Yifan F. Zhang, Fangjun Hu, Guangkuo Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models undergo a phase transition in a critical time window during generation dynamics, with two complementary diagnoses of criticality. The symmetry breaking picture views the critical window as when trajectories bifurcate into different semantic minima of the energy landscape, whereas the nonlocality picture views the critical window as when local denoising fails. We study whether two notions of such phase transitions are concurrent in modern diffusion transformers. By evaluating the dynamics and outcomes of the generation trajectory, we observe a near-simultaneous occurrence of the non-locality and symmetry breaking critical times. Our work is the first to unify the two notions of phase transitions in practice: it provides a concrete diagnostic for when and why diffusion models rely on conditioning and global denoising, enabling principled evaluation of model efficiency and guiding the design of architectures and sampling schemes that avoid unnecessary computation.

---


### 190. [StoryAlign: Evaluating and Training Reward Models for Story Generation](https://arxiv.org/abs/2605.04831)

**<font color=#1a73e8>作者：</font>** Haotian Xia, Hao Peng, Yunjia Qi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Story generation aims to automatically produce coherent, structured, and engaging narratives. Although large language models (LLMs) have significantly advanced text generation, stories generated by LLMs still diverge from human-authored works regarding complex narrative structure and human-aligned preferences. A key reason is the absence of effective modeling of human story preferences, which are inherently subjective and under-explored. In this work, we systematically evaluate the modeling of human story preferences and introduce StoryRMB, the first benchmark for assessing reward models on story preferences. StoryRMB contains $1,133$ high-quality, human-verified instances, each consisting of a prompt, one chosen story, and three rejected stories. We find existing reward models struggle to select human-preferred stories, with the best model achieving only $66.3\%$ accuracy. To address this limitation, we construct roughly $100,000$ high-quality story preference pairs across diverse domains and develop StoryReward, an advanced reward model for story preference trained on this dataset. StoryReward achieves state-of-the-art (SoTA) performance on StoryRMB, outperforming much larger models. We also adopt StoryReward in downstream test-time scaling applications for best-of-n (BoN) story selection and find that it generally chooses stories better aligned with human preferences. We will release our dataset, model, and code to facilitate future research. Related code and data are available at this https URL.

---


### 191. [Replay-Based Continual Learning for Physics-Informed Neural Operators](https://arxiv.org/abs/2605.04832)

**<font color=#1a73e8>作者：</font>** Yizheng Wang, Mohammad Sadegh Eshaghi, Xiaoying Zhuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators generally demonstrate strong predictive performance on in-distribution (ID) problems. However, a critical limitation of existing methods is their significant performance degradation when encountering out-of-distribution (OOD) data. To address this issue, this work introduces continual learning into physics-informed neural operators, with particular emphasis on neural operators built upon the Transolver architecture, and proposes a simple yet effective replay-based continual learning strategy. The proposed method is fully physics-informed and does not require labeled data, relying solely on input fields together with physical constraints for training. When new OOD data become available, a small number of past data are incorporated through a distillation-based constraint to preserve previously acquired knowledge and alleviate catastrophic forgetting. Meanwhile, a transfer learning LoRA is employed to enable rapid adaptation to the new data. The proposed framework is systematically validated on three representative physical problems, including the Darcy flow problem in fluid mechanics, a two-dimensional hyperelastic brain tumor problem in biomechanics, and a three-dimensional linear elastic Triply Periodic Minimal Surfaces problem in solid mechanics. The results demonstrate that the proposed method effectively mitigates catastrophic forgetting on previously learned data while maintaining fast adaptability to new data. Compared with conventional joint training strategies, the proposed method significantly improves training efficiency while reducing additional memory usage and computational cost.

---


### 192. [QuadBox: Accelerating 3D Gaussian Splatting with Geometry-Aware Boxes](https://arxiv.org/abs/2605.04844)

**<font color=#1a73e8>作者：</font>** Xinze Li, Bohan Yang, Pengxu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has emerged as an advanced technique for real-time novel view synthesis by representing scene geometry and appearance using differentiable Gaussian primitives. However, efficiently computing precise Gaussian-tile intersections remains a critical task in the rasterization pipeline. To this end, we propose QuadBox, a method that leverages four axis-aligned bounding boxes to tightly encapsulate projected Gaussians in a discrete manner. First, we derive a geometry-aware stretching factor that enables the construction of a tile-aligned QuadBox, which covers the elliptical projection and largely excludes irrelevant tiles. Second, we introduce QPass, a single-pass tile traversal algorithm that exhaustively exploits the discrete nature of QuadBox, ensuring that the tile intersection check is performed with simple interval tests. Experiments on public datasets show that our method accelerates the rendering speed of 3DGS by 1.85$\times$. Code is available at \href{this https URL}{this https URL}.

---


### 193. [Quantile-Free Uncertainty Quantification in Graph Neural Networks](https://arxiv.org/abs/2605.04847)

**<font color=#1a73e8>作者：</font>** Soyoung park, Hwanjun Song, Sungsu Lim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification (UQ) in graph neural networks (GNNs) is crucial in high-stakes domains but remains a significant challenge. In graph settings, message passing often relies on strong assumptions such as exchangeability, which are rarely satisfied in practice. Moreover, achieving reliable UQ typically requires costly resampling or post-hoc calibration. To address these issues, we introduce Quantile-free Prediction Interval GNN (QpiGNN), a framework that builds on quantile regression (QR) to enable GNN-based UQ by directly optimizing coverage and interval width without requiring quantile inputs or post-processing. QpiGNN employs a dual-head architecture that decouples prediction and uncertainty, and is trained with label-only supervision through a quantile-free joint loss. This design allows efficient training and yields robust prediction intervals, with theoretical guarantees of asymptotic coverage and near-optimal width under mild assumptions. Experiments on 19 synthetic and real-world benchmarks show QpiGNN achieves average 22\% higher coverage and 50\% narrower intervals than baselines, while ensuring efficiency and robustness to noise and structural shifts.

---


### 194. [Hybrid Iterative Neural Low-Regularity Integrator for Nonlinear Dispersive Equations](https://arxiv.org/abs/2605.04853)

**<font color=#1a73e8>作者：</font>** Zhangyong Liang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose HIN-LRI, a hybrid framework that augments a classical numerical solver with a neural operator trained to correct the solver's structured truncation error. A base low-regularity integrator provides a consistent first-order approximation to nonlinear dispersive PDEs, while a lightweight neural network, operating on a low-dimensional latent manifold, learns the residual defect that analytical methods cannot close. An explicit time-step scaling on the neural correction ensures that its Lipschitz contribution remains $\mathcal{O}(\tau)$, yielding a Gronwall stability factor bounded uniformly in the step size and independent of the spatial resolution. The network is trained end-to-end through a solver-in-the-loop objective that unrolls the full iteration and penalises trajectory error in a Bourgain-type norm, aligning learning with multi-step solver dynamics rather than isolated one-step targets. Under stated assumptions, the global error satisfies $C(\varepsilon_{net}+\delta)\,\tau^\gamma\ln(1/\tau)$, where $\varepsilon_{net}$ measures the network approximation quality and $\delta$ the training shortfall. Experiments on three dispersive benchmarks with rough data show that HIN-LRI improves accuracy over analytical integrators, splitting methods, and neural PDE surrogates, with stable spatial refinement, effective out-of-distribution transfer, and modest online overhead.

---


### 195. [3D Ultrasound-Derived Pseudo-CT Synthesis Using a Transformer-Augmented Residual Network for Real-Time Operator Guidance](https://arxiv.org/abs/2605.04856)

**<font color=#1a73e8>作者：</font>** Sapna Sachan, Amulya Kumar Mahto  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) is indispensable for clinical diagnosis and image-guided interventions but exposes patients to ionizing radiation, motivating the development of safer imaging alternatives. Ultrasound (US) is non-ionizing and widely accessible; however, it is highly operator dependent and lacks quantitative tissue characterization, often leading to diagnostic uncertainty and unnecessary CT examinations. This work presents a 3D ultrasound-derived pseudo-CT (UD-pCT) framework that generates CT-like anatomical reference volumes inferred from US, without aiming to reproduce physically accurate Hounsfield Units. Paired 3D kidney US and CT volumes from the TRUSTED dataset are first spatially aligned using a landmark-based multimodal registration pipeline, creating high-quality paired inputs for supervised training of an adversarial framework. The proposed Bottleneck Transformer Residual U-Net3D (BT-ResUNet3D) model employs a 3D residual encoder-decoder generator augmented with a transformer bottleneck, enabling effective modeling of fine-grained local anatomical structures as well as long-range volumetric dependencies, while a 3D Conditional PatchGAN discriminator enforces local structural realism in the synthesized pseudo-CT volumes. Quantitative evaluation using PSNR and SSIM demonstrates that the proposed method outperforms established baselines in structural fidelity and perceptual image quality. The UD-pCT volumes provide real-time anatomical reference for operator guidance, potentially reducing acquisition variability and unnecessary CT use. A limitation of this study is the relatively small paired dataset, which may limit the generalizability of the proposed model.

---


### 196. [Assessing Cognitive Effort in L2 Idiomatic Processing: An Eye-Tracking Dataset](https://arxiv.org/abs/2605.04857)

**<font color=#1a73e8>作者：</font>** Eduardo Santos, Juliana Carvalho, César Rennó-Costa  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the development and validation of an eye-tracking dataset designed to investigate how second-language (L2) learners process idiomatic expressions. While native speakers often rely on direct retrieval of figurative meanings, L2 speakers frequently adopt a literal-first approach, which incurs measurable cognitive costs. This resource captures these costs through ocular metrics recorded from Portuguese L1 speakers of English across all CEFR proficiency levels (A1-C2). Although the study uses entry-level 60 Hz hardware (Tobii Pro Spark), we demonstrate that this sampling rate provides sufficient data density to detect macro-cognitive events such as fixations and regressions in reading. Preliminary analysis validates the dataset by revealing a strong inverse correlation between language proficiency and regressive eye movements. Integrated into the MIA (Modeling Idiomaticity in Human and Artificial Language Processing) initiative, this dataset serves as a cognitively grounded benchmark for evaluating both human processing models and the alignment of large language models with human-like figurative understanding.

---


### 197. [Not All Scaffolds Are Equal: How Initiation Mode Determines EMME Effectiveness in Debugging](https://arxiv.org/abs/2605.04868)

**<font color=#1a73e8>作者：</font>** Anahita Golrang, Kshitij Sharma, Halszka Jarodzka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Adaptive learning technologies increasingly rely on real time physiological analytics to trigger instructional support automatically yet how system driven decisions interact with learners ongoing problem solving processes remains poorly understood. Eye Movement Modeling Examples have shown promise as attention guidance tools but have been studied predominantly as static instructional materials rather than as adaptive scaffolds whose timing and initiation control can vary. This study investigates whether scaffold initiation mode shapes EMME effectiveness in novice programmers debugging and specifically whether automated triggering based on a single physiological indicator of low mental effort is a viable basis for adaptive scaffold delivery. A between subjects experiment was conducted with 120 undergraduate computer science students randomly assigned to one of four conditions: teacher initiated, learner initiated, automated or no scaffold control. Participants completed ten Python debugging tasks while eye tracking data, video interaction logs and performance scores were recorded. All EMME conditions outperformed the control. However human mediated initiation whether teacher or learner consistently produced higher performance than automated triggering and more integrative engagement with the EMME material. Automated triggering based on sustained low pupillary activity was associated with disruptive behavioral patterns suggesting mistimed delivery. EMME also eliminated the performance advantage of prior programming knowledge across all initiation modes. These findings establish scaffold initiation timing and control as critical design variables for EMME and adaptive learning technologies more broadly and demonstrate that a single low effort physiological threshold is insufficient as a trigger criterion for complex problem solving support.

---


### 198. [Measuring Psychological States Through Semantic Projection: A Theory-Driven Approach to Language-Based Assessment](https://arxiv.org/abs/2605.04873)

**<font color=#1a73e8>作者：</font>** Maria Luongo, Davide Marocco, Nicola Milano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in natural language processing have enabled increasingly accurate estimation of psychological traits from language. However, most existing approaches rely on supervised models trained to predict questionnaire scores, limiting interpretability and generalizability across contexts. The present study introduces a theory-driven and fully unsupervised framework for measuring psychological states directly from natural language using semantic projection. Psychological constructs were operationalized as interpretable semantic axes derived from lexical anchors and items from validated clinical scales assessing depression, anxiety, and worry. Participants textual responses were embedded using Sentence-BERT and projected onto these axes to generate continuous psychological scores across multiple response formats, including selected words, generated words, phrases, and free-text responses. Projection scores were evaluated through correlations with standardized clinical measures , split-half reliability analyses, attenuation corrections, distributional similarity using Wasserstein distance, and comparisons with lexicon-based sentiment analysis (VADER). Results showed strong associations between projection scores and clinical measures, particularly for structured formats such as selected words, written words, and phrases. Free-text responses produced weaker results when analyzed as whole texts, but performance improved substantially when sentence-level aggregation strategies were applied. These findings support semantic projection as an interpretable and scalable alternative to supervised language models for psychological assessment and highlight the importance of response format and text-processing strategies in language-based mental health measurement.

---


### 199. [A Comparative Study of PyCaret AutoML and CNN-BiLSTM for Binary Hate Speech Detection in Indonesian Twitter](https://arxiv.org/abs/2605.04885)

**<font color=#1a73e8>作者：</font>** Tanty Widiyastuti, Mayada, Adisty Syawalda Ariyanto 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper compares a PyCaret AutoML branch and a CNN-BiLSTM branch for binary hate speech detection on Indonesian Twitter using the HS label from the corpus of Ibrohim and Budi. Both branches share the same preprocessing pipeline so that the comparison reflects modelling differences rather than inconsistent data preparation. The conventional branch uses TF-IDF with a lexicon-based abusive-word count, whereas the neural branch learns dense token representations and captures both local phrase patterns and bidirectional context. The benchmark is built from the released 13,130-row annotation table, whose HS label yields a 58:42 class ratio. On the held-out split, CNN-BiLSTM achieves the best result with 83.8% accuracy, 79.8% precision, 82.7% recall, and 81.2% F1-score. Within the PyCaret branch, Random Forest is the strongest conventional model with 77.2% accuracy and 77.0% F1-score. The neural branch therefore improves accuracy by 6.6 points and F1-score by 4.2 points. Exploratory corpus analysis, learning curves, and confusion matrices show that the dataset is short-text, moderately imbalanced, and still difficult because many decisions depend on local lexical cues plus short contextual composition. The study concludes that PyCaret AutoML is an effective conventional benchmarking framework, whereas CNN-BiLSTM is the stronger end model for the reported benchmark setting.

---


### 200. [Sentiment Analysis and Customer Satisfaction Prediction on E-Commerce Platforms Based on YouTube Comments Using the XGBoost Algorithm](https://arxiv.org/abs/2605.04887)

**<font color=#1a73e8>作者：</font>** Ridho Benedictus Togi Manik, Muhammad Aqil Ramadhan, Ihsan Maulana Yusuf 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The exponential expansion of digital commerce in Indonesia has significantly shifted consumer interactions toward video-centric social networks, particularly YouTube. Consequently, the sheer volume of unstructured, multi-contextual comments poses a tremendous challenge for manual sentiment tracking. This study investigates and constructs a predictive model for customer satisfaction leveraging the Extreme Gradient Boosting (XGBoost) architecture coupled with Term Frequency-Inverse Document Frequency (TF-IDF) vectorization. By utilizing a secondary dataset of YouTube comments retrieved from e-commerce review videos, the raw text underwent rigorous preprocessing to generate normalized numerical features. The experimental results demonstrate that the PyCaret-optimized machine learning framework delivers superior classification resilience. Beyond standard performance metrics, lexical evaluations and feature-importance mapping uncover a notable phenomenon: e-commerce discourse is heavily infiltrated by socio-political terminologies, which ultimately influence the polarity of audience satisfaction.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
