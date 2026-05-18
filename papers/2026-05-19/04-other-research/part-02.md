# 📦 其他研究 | 2026年05月19日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

---

### 51. [Lagrangian Flow Matching: A Least-Action Framework for Principled Path Design](https://arxiv.org/abs/2605.15419)

**<font color=#1a73e8>作者：</font>** Shukai Du, Junzhe Zhang, Yiming Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching trains a neural velocity field by regression against a target velocity associated with a prescribed probability path connecting a simple initial distribution to the data distribution. A central design choice is the path itself. Existing constructions, including rectified and optimal-transport-based paths, transport samples along straight lines between coupled endpoints and thus cover only a narrow class of dynamics. We observe that this corresponds to the simplest case of the least-action principle in classical mechanics, in which the kinetic Lagrangian yields free-particle straight-line trajectories. Building on this observation, we propose Lagrangian flow matching, a physics-based framework in which the probability path and velocity field are determined by minimizing the action of a general Lagrangian subject to the continuity equation and the prescribed endpoints. We show that this dynamic problem admits an equivalent static optimal transport (OT) formulation, yielding a family of simulation-free training objectives that recover OT-based flow matching as the kinetic special case and the trigonometric variance-preserving diffusion path as the harmonic-oscillator case. More general Lagrangians give rise to new probability paths and velocity fields, and numerical experiments show that they induce meaningful changes in the learned dynamics while remaining competitive with existing conditional flow matching models.

---


### 52. [U-SEG: Uncertainty in SEGmentation -- A systematic multi-variable exploration](https://arxiv.org/abs/2605.15421)

**<font color=#1a73e8>作者：</font>** Michael Smith, Frank P. Ferrie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this study, we explore in depth a few under-studied topics at the intersection of uncertainty estimation and segmentation. Prior work has shown that the quality of uncertainty estimates can be very sensitive to a range of variables. As one of the main uses of uncertainty estimation is to help identify and deal with prediction errors in practical scenarios, any factors that affect this must be clearly identified. For example, do more challenging domains or different datasets and architectures result in worse performance when using uncertainty estimates? Can prior frames in a video sequence in fact provide useful uncertainty estimates comparable to other approaches? Is it possible to combine uncertainty estimation approaches, taking advantage of sample diversity, to get better estimates? Finally, when might it make sense to use an ensemble-based uncertainty estimate over a deterministic network? We address these questions by creating a framework for and executing a large scale study across many variables such as datasets, backbones, and downstream tasks, for both semantic and panoptic segmentation. We find that a) the more challenging task of panoptic segmentation usually results in worse performance while high performance variance between datasets and backbones indicates that generalization is not guaranteed, b) time series samples can be useful for specific configurations, but in many cases are not worth the cost, c) sample diversity shows the most promise in the downstream task of calibration, but otherwise fails to beat simpler alternatives, d) a deterministic approach is adequate for some downstream tasks, but ensembles allow for significant improvements if the right conditions can be achieved in deployment.

---


### 53. [DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts](https://arxiv.org/abs/2605.15422)

**<font color=#1a73e8>作者：</font>** Jiading Gai, Shuai Zhang, Xiang Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern RL post-training methods such as GRPO and DAPO train on $N$ response sequences of $R$ tokens sampled from a shared prompt of $P$ tokens, but standard FlashAttention replicates all $P$ prompt tokens $N$ times across both forward and backward passes -- duplicating compute and memory on identical hidden states. In large-rollout, long-context RL training ($N{\geq}16$, $P{\geq}8\text{K}$), this redundancy dominates the policy update cost. We observe that in decoder-only models, causal masking makes prompt representations invariant across sequences at every layer, so all per-token operations (norms, projections, MLP) and attention can process the prompt once -- a property not yet exploited at the kernel level for training. We propose \textbf{DualKV}, the first FlashAttention kernel variant that eliminates shared-prompt replication during RL training, via (1)~fused CUDA forward and backward kernels that iterate over two disjoint KV regions -- shared context and per-sequence response -- in a single kernel launch, and (2)~a data-pipeline redesign in veRL that repacks $N(P{+}R)$ tokens into $P{+}NR$ tokens per micro-batch, extending the token reduction from attention to the entire model by a factor $\rho = N(P{+}R)/(P{+}NR)$. DualKV is mathematically equivalent to standard attention and introduces no approximation. On Qwen3-8B GRPO training with 8$\times$H100 GPUs ($N{=}32$, 8K-context), DualKV achieves $1.63$--$2.09\times$ policy-update speedup, enables $2\times$ larger micro-batches, and raises MFU from $36\%$ to $76\%$. Similar gains hold for DAPO ($2.47\times$ speedup, $77\%$ MFU). At 30B MoE scale on 16$\times$H100, DualKV achieves $3.82\times$ policy-update and $3.38\times$ end-to-end step speedup over FlashAttention (which requires 4-way Ulysses sequence parallelism to avoid OOM).

---


### 54. [MR2-ByteTrack: CNN and Transformer-based Video Object Detection for AI-augmented Embedded Vision Sensor Nodes](https://arxiv.org/abs/2605.15423)

**<font color=#1a73e8>作者：</font>** Luca Bompani, Manuele Rusci, Luca Benini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern smart vision sensors need on-device intelligence to process video streams, as cloud computing is often impractical due to bandwidth, latency, and privacy constraints. However, these sensory systems typically rely on ultra-low-power microcontrollers (MCUs) with limited memory and compute, making conventional video object detection methods, which require feature storage or multi-frame buffering, unfeasible. To address this challenge, we introduce Multi-Resolution Rescored ByteTrack (MR2-ByteTrack), a Video Object Detection (VOD) method tailored for MCU-based embedded vision nodes. MR2-ByteTrack reduces computational cost by alternating between full- and low-resolution inference, while linking detections across frames via ByteTrack and correcting misclassifications through the Rescore algorithm, which applies probability union rules to aggregate detection confidence scores across frames. We apply our approach to both a CNN-based detector and a Transformer-based model, demonstrating its generality across architectures with fundamentally different spatial processing. Experiments on ImageNetVID demonstrate that MR2-ByteTrack maintains accuracy, achieving mAP scores of up to 49.0 for the CNN-based models and 48.7 for the Transformer, while reducing multiply-accumulate operations by as much as 53\% for the CNNs and 32\% for the Transformer. When deployed on GAP9, an ultra-low-power RISC-V multicore MCU, our method yields up to 55\% energy savings compared to processing only full-resolution images, enabling the first real-time Transformer-based VOD on an MCU-class embedded vision node. Code available at this https URL

---


### 55. [Social-Mamba: Socially-Aware Trajectory Forecasting with State-Space Models](https://arxiv.org/abs/2605.15424)

**<font color=#1a73e8>作者：</font>** Po-Chien Luan, Wuyang Li, Yang Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human trajectory forecasting is crucial for safe navigation in crowded environments, requiring models that balance accuracy with computational efficiency. Efficiently modeling social interactions is key to performance in dense crowds. Yet, most recent methods rely on attention mechanisms, which are effective at capturing complex dependencies, but incur quadratic computational costs that scale poorly with the growing number of neighbors. Recently, Selective State-Space Models have provided a linear-time alternative; however, their inherently sequential design is misaligned with the unstructured and dynamic nature of social interactions. To address this challenge, we propose Social-Mamba, a forecasting architecture that reformulates social interactions as structured sequential processes. At its core is the Cycle Mamba block, a novel module that enables continuous bidirectional information flow. Social-Mamba organizes agents on an egocentric grid and introduces social triplet factorization, which decomposes interactions into temporal, egocentric, and goal-centric scans. These are dynamically integrated through a learnable social gate and global scan to generate accurate and efficient trajectory predictions. Extensive experiments on five trajectory forecasting benchmarks show that Social-Mamba achieves state-of-the-art accuracy while offering superior parameter efficiency and computational scalability. Furthermore, embedding Social-Mamba into a flow-matching framework further enhances both accuracy and efficiency, establishing it as a flexible and robust foundation for future trajectory forecasting research. The code is publicly available: this https URL

---


### 56. [Spectral Priors vs. Attention: Investigating the Utility of Attention Mechanisms in EEG-Based Diagnosis](https://arxiv.org/abs/2605.15433)

**<font color=#1a73e8>作者：</font>** Tawsik Jawad, Gowtham Atluri, Vikram Ravindra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalograph (EEG) timeseries signals are characterized by significant noise and coarse spatial resolution, which complicates the classification of neurodegenerative diseases. Even SOTA deep learning architectures struggle to distinguish between healthy controls and diseased subjects, or between different disease types, due to high intergroup similarity. In this paper, we show that a spectrally selective approach to feature construction enhances class separability. By isolating signal strengths within the primary brainwave bands, we transform high dimensional raw data into high value spectral features. Our results demonstrate that a) features derived from frequency and time frequency domain allow traditional machine learning models to match or exceed the performance of SOTA deep learning models, b) Attention mechanism is unable to distill the stable feature signatures that characterize healthy neural activity in both resting and task EEGs, and c) the limitations of attention based models in finding relevant spectral features appear to be fundamental in that providing frequency selective time domain input do not appreciably improve their performance. We validate our methodology across three open source resting EEG datasets and one task EEG dataset, providing robust empirical evidence for our claims.

---


### 57. [On the Stability of Growth in Structural Plasticity](https://arxiv.org/abs/2605.15435)

**<font color=#1a73e8>作者：</font>** Lute Lillo, Nick Cheney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard deep-learning pipelines usually choose the network architecture before training and keep it fixed throughout optimization. In contrast, a model can also be adapted by editing its structure during training, for example by pruning existing hidden-neuron units or growing new ones. Although growth is appealing for adaptive and continual systems, we show that it is not simply the inverse of pruning. Pruning selects among units that have participated in training from the start, whereas growth inserts new units into an already specialized optimization trajectory. We isolate this insertion problem and show that newborn units are often forward-active but backward-starved: they participate in the forward computation, yet receive much weaker gradient signal than incumbent units. This disadvantage is minor in small MLP benchmarks, but becomes clear in harder image-classification settings with a convolutional trunk. In these settings, \textsc{Grow} can achieve high final accuracy during the structural-editing procedure, while \textsc{Prune} is stronger when performance is averaged over the training trajectory or when the final sparse network is retrained from scratch. Interventions targeting optimizer state, insertion, selection, and trainability show that improving the integration of newborn units can improve adaptive performance, but does not automatically produce better final subnetworks. In continual-learning benchmarks stressing plasticity loss, \textsc{Grow} becomes competitive mainly when new units have enough time to integrate. Together, these results suggest that \textsc{Grow} should be evaluated not only as an architecture-search operator, but as a time-sensitive optimization process whose success depends on insertion stability.

---


### 58. [RIDE: Retinex-Informed Decoupling for Exposing Concealed Objects](https://arxiv.org/abs/2605.15450)

**<font color=#1a73e8>作者：</font>** Chunming He, Rihan Zhang, Dingming Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concealed Object Segmentation (COS) encompasses a family of dense-prediction tasks, including camouflaged object detection, polyp segmentation, transparent object detection, and industrial defect inspection, where targets are visually entangled with their surroundings through different physical mechanisms. Existing methods either operate directly on RGB images or employ \emph{heterogeneous} decompositions (\eg, Fourier, wavelet) that redistribute spatial evidence across scale/frequency coefficients, making pixel-aligned cues less direct. We introduce a fundamentally different perspective: \textbf{homogeneous image decomposition} via Retinex theory, which factorizes an image into illumination and reflectance components within the \emph{same} spatial domain. Our key insight is that visual entanglement enforces appearance matching in the composite space, but this does \emph{not} necessitate simultaneous matching in both component spaces, a phenomenon we formalize as the \textbf{Discriminability Gap Theorem}. Crucially, we show that across diverse COS sub-tasks, the underlying physical processes systematically anti-correlate illumination and reflectance differences, yielding theoretical guarantees that Retinex decomposition preserves or strictly improves total foreground--background discriminability across the full physical regime, with anti-correlation maximizing the gain. Building on this, we propose \textbf{RIDE} comprising: (i) a Task-Driven Retinex Decomposition module that learns segmentation-optimal factorizations end-to-end; (ii) a Discriminability Gap Attention mechanism that adaptively exploits where decomposition helps; and (iii) a Camouflage-Breaking Contrastive loss operating in reflectance feature space.

---


### 59. [Video Models Can Reason with Verifiable Rewards](https://arxiv.org/abs/2605.15458)

**<font color=#1a73e8>作者：</font>** Tinghui Zhu, Sheng Zhang, James Y. Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models have made rapid progress in perceptual realism and temporal coherence, but they remain primarily optimized for plausible generation rather than verifiable reasoning. This limitation is especially pronounced in tasks where generated videos must satisfy explicit spatial, temporal, or logical constraints. Inspired by the role of reinforcement learning with verifiable rewards (RLVR) in reasoning-oriented language models, we introduce VideoRLVR, a practical recipe for optimizing video diffusion models with rule-based feedback. VideoRLVR formulates video reasoning as the generation of verifiable visual trajectories and consists of an SDE-GRPO optimization backbone, dense decomposed rewards, and an Early-Step Focus strategy for efficient training. The Early-Step Focus strategy restricts policy optimization to the early denoising phase, reducing training latency by about 40% while preserving performance. We evaluate VideoRLVR on Maze, FlowFree, and Sokoban, three procedurally generated domains with objective success criteria. Across these tasks, VideoRLVR consistently improves over supervised fine-tuning baselines, with dense decomposed rewards proving especially important in low-success-rate settings. Our RL-optimized model also outperforms the evaluated proprietary and open-source video generation models on these verifiable reasoning benchmarks and out-of-domain benchmarks. These results suggest that verifiable RL can move video models beyond perceptual imitation toward more reliable rule-consistent visual reasoning.

---


### 60. [Don't Stop Me Yet: Sampling Loss Minima via Dissipative Riemannian Mechanics](https://arxiv.org/abs/2605.15459)

**<font color=#1a73e8>作者：</font>** Albert Kjøller Jacobsen, Leo Uhre Jakobsen, Johanna Marie Gegenfurtner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The minima of modern neural network loss functions are typically not isolated, rather they form connected components of reparameterization invariant solutions on the training data. Analytically characterizing these solutions is a hard problem, but sampling approaches are feasible. By construction, existing methods either spread over low-loss regions, and thus do not sample reparameterization invariant solutions exactly, or are inherently local, which limits exploration of other minima valleys. We propose sampling such reparameterization invariant models using a dynamical system based on kinetic energy, subject to a gravitational pull and a friction term that dissipates energy from the system. Our proposed sampler, DiMS, is guaranteed to sample exactly from the minimum level sets and depends on physically motivated hyperparameters which allows control over the exploration capabilities of the sampler. We consider uncertainty quantification in Bayesian inference as the motivating problem and observe improved performance compared to previously proposed approaches.

---


### 61. [DrugSAGE:Self-evolving Agent Experience for Efficient State-of-the-Art Drug Discovery](https://arxiv.org/abs/2605.15461)

**<font color=#1a73e8>作者：</font>** Yikun Zhang, Xiwei Cheng, Tianyu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Building state-of-the-art (SOTA) predictive models for drug discovery requires expensive search over tools, architectures, and training strategies. Current LLM-based agents can find SOTA solutions through extensive trial and error, but they do not retain the experience accumulated along the way and therefore pay the full search cost on every new task. We propose \method (Self-evolving Agent Experience), a framework that accumulates and reuses experience across tasks to build SOTA drug discovery models efficiently. \method maintains a cross-task memory of verified skills, statistical evidence about effective strategies, and a record of recurring errors and their fixes. In some cases, \method transfers a working solution directly without test-time search. In 33 molecular property prediction tasks, \method ranks first among nine SOTA agents in a single-task setting. With memory accumulated from 16 smaller tasks, \method achieves an averaged normalized score of 0.935 on 17 held-out tasks in a cross-task evaluation setting and outperforms all baseline agents by 10-30\% in a zero-test-time search regime. In summary, our work shows the advantage of cross-task memory for efficient SOTA model development in drug discovery.

---


### 62. [Layer-wise Derivative Controlled Networks](https://arxiv.org/abs/2605.15463)

**<font color=#1a73e8>作者：</font>** Rowan Martnishn, Sean Anderson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As machine learning models grow in complexity, they increasingly struggle with three conflicting demands: the need for high accuracy, the requirement for hardware efficiency, and the necessity of functional stability. Traditional architectures often achieve performance at the expense of spiky or unpredictable behavior, where small changes in input lead to massive swings in output -- a critical flaw for real-world deployment in sensitive environments. This paper introduces ChainzRule (CR), a novel neural architecture designed to harmonize these competing goals. ChainzRule replaces standard piecewise-linear activations with a Polynomial Engine governed by Differential Regularization (DREG). Unlike traditional methods that impose global, coarse-grained constraints on a model's Lipschitz constant, DREG acts as a targeted regularization on intermediate derivatives. This approach suppresses extreme sensitivity without attenuating the representational power inherent in the Polynomial Engine. In head-to-head "Fair Fight" benchmarks, ChainzRule outperformed standard models while using 15.5x fewer parameters. On the MNIST dataset, it reduced peak gradient volatility by an average of 23.1%, ensuring a smoother and more predictable manifold. On Yelp Full ordinal regression under explicit DREG regularization, ChainzRule achieves 70.17% accuracy, validating that derivative-aware regularization is compatible with competitive performance on realistic tasks. By embedding gradient awareness into the architecture via DREG, ChainzRule demonstrates that stability and accuracy need not be competing objectives.

---


### 63. [GreenZ: A Sustainable UX Framework for Complex Digital Systems](https://arxiv.org/abs/2605.15468)

**<font color=#1a73e8>作者：</font>** Trisha Solanki  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital systems have become simultaneously more powerful and more wasteful. Features accumulate that nobody uses. Data is collected that nobody analyzes. AI is deployed at significant energy and water costs for gains that a simpler approach could have achieved. And through all of it, the people who depend on these systems quietly absorb the consequences in cognitive load, lost time, and eroded trust. This paper introduces GreenZ, a three-layer Sustainable UX Framework for complex digital systems. Its three layers are a Philosophy Layer built around ten published principles, an Operational Frameworks Layer comprising five applied systems, and a Tools and Canvases Layer of practical audit instruments and decision models. Two contributions sit at the framework's core: a Digital Waste Taxonomy classifying eight distinct waste types, and an AI Sufficiency Decision Model that asks whether AI should exist in a given flow before any question of how to implement it. GreenZ v1 is theoretically grounded but empirically unvalidated. A practitioner expert review study is underway at the time of submission. The paper presents the framework's architecture, its conceptual foundations, its position relative to existing literature, and an honest account of what remains to be established.

---


### 64. [Njord: A Probabilistic Graph Neural Network for Ensemble Ocean Forecasting](https://arxiv.org/abs/2605.15470)

**<font color=#1a73e8>作者：</font>** Daniel Holmberg, Joel Oskarsson, Erik Larsson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ocean dynamics are inherently chaotic, yet existing machine learning ocean models produce only deterministic forecasts. We introduce Njord, a probabilistic data-driven model for ocean forecasting, applicable to both global and regional domains. Njord combines a deep latent variable framework with a graph neural network architecture, enabling sampling each forecast step in a single forward pass. We apply Njord globally at 0.25° resolution and regionally to the Baltic Sea at 2 km resolution. To scale to these large ocean grids we introduce K-means cluster meshes that adapt to irregular sea surface geometry. Experiments demonstrate strong performance on both domains compared to deterministic machine learning baselines, while also providing uncertainty estimates from the sampled ensemble forecasts. On the global OceanBench benchmark, Njord achieves the lowest errors on average across upper-ocean variables when evaluated against real-world observations, with the largest improvements in surface temperature prediction.

---


### 65. [Estimated Dynamic Equilibrium Model: Supply and Demand as a Sample Path of a Stochastic Process](https://arxiv.org/abs/2605.15472)

**<font color=#1a73e8>作者：</font>** Mikhail L. Arbuzov, Sisong Bei, Alexey Shvets  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We introduce the Estimated Dynamic Equilibrium Model (EDEM), an agent-based framework that treats supply and demand as a coupled stochastic process driven by heterogeneous, noisy agent valuations. The model's primary technical contribution is the identification of a generative mechanism for persistent disequilibrium: when market-clearing prices are sequentially sampled from the upper tail of noisy bid distributions and recycled as inputs for future valuations, expected prices drift upward despite strictly zero-mean estimation errors. We derive this order-statistic bias in closed form for i.i.d. uniform bids and use simulations to show that compounding this bias across epochs yields exponential price growth without requiring assumptions of investor optimism or irrationality. This framework extends Miller's divergence-of-opinion theory to a dynamic setting, recovering Walrasian equilibrium and Miller's static premium as limiting cases. Through controlled experiments and sensitivity analysis on a simulated real-estate neighborhood, we identify six distinct regimes-ranging from band-stability to runaway bubbles-emerging from a single agent ruleset. These results offer a potential explanation for the contradictory findings in the empirical divergence-of-opinion literature and suggest that machine-learning valuation algorithms may inadvertently amplify this inherent statistical bias.

---


### 66. [A Unified Non-Parametric and Interpretable Point Cloud Analysis via t-FCW Graph Representation](https://arxiv.org/abs/2605.15475)

**<font color=#1a73e8>作者：</font>** Haijian Lai, Bowen Liu, Man Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce an empowered transposed Fully Connected Weighted (t-FCW) graph representation to embed point clouds into a metric space. While original t-FCW has shown promising results for point cloud classification, the reasons behind its effectiveness and its broader applicability remained unclear. In this work, we analyze the properties that make the empowered and original t-FCW effective and design a network that uses the empowered t-FCW exclusively as feature extractors. From an interpretability perspective, we build memory banks for classification, part segmentation, and semantic segmentation using the empowered t-FCW. Our analysis reveals that the empowered t-FCW inherits robustness from surface descriptors, provides interpretability through dimension-wise relations. These properties enable a highly efficient and interpretable network, which processes the ModelNet40 classification problem in approximately 7 seconds on an NVIDIA RTX A5000 GPU. Importantly, empowered t-FCW can function both as a lightweight standalone baseline and as a complementary plug-in to existing deep models.

---


### 67. [Learning Normalized Energy Models for Linear Inverse Problems](https://arxiv.org/abs/2605.15487)

**<font color=#1a73e8>作者：</font>** Nicolas Zilberstein, Santiago Segarra, Eero Simoncelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative diffusion models can provide powerful prior probability models for inverse problems in imaging, but existing implementations suffer from two key limitations: $(i)$ the prior density is represented implicitly, and $(ii)$ they rely on likelihood approximations that introduce sampling biases. We address these challenges by introducing a new energy-based model trained for denoising with a covariance-based regularization term that enforces consistency across different measurement conditions. The trained model can compute normalized posterior densities for diverse linear inverse problems, without additional retraining or fine tuning. In addition to preserving the sampling capabilities of diffusion models, this enables previously unavailable capabilities: energy-guided adaptive sampling that adjusts schedules on-the-fly, unbiased Metropolis-Hastings correction steps, and blind estimation of the degradation operator via Bayes rule. We validate the method on multiple datasets (ImageNet, CelebA, AFHQ) and tasks (inpainting, deblurring), demonstrating competitive or superior performance to established baselines.

---


### 68. [SurvivalPFN: Amortizing Survival Prediction via In-Context Bayesian Inference](https://arxiv.org/abs/2605.15488)

**<font color=#1a73e8>作者：</font>** Shi-ang Qi, Vahid Balazadeh, Michael Cooper 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Survival analysis provides a powerful statistical framework for modeling time-to-event outcomes in the presence of censoring. However, selecting an appropriate estimator from the many specialized survival approaches often requires substantial methodological and domain expertise. We introduce SurvivalPFN, a prior-data fitted network that amortizes Bayesian inference for censored observations through in-context learning. SurvivalPFN is pretrained on a diverse family of synthetic, identifiable, and right-censored data-generating processes, enabling it to amortize survival analysis in a single forward pass during inference. As a result, the model adapts to the effective complexity of each dataset without task-specific training or hyperparameter tuning, avoids restrictive parametric assumptions, and produces calibrated survival distributions. In a large-scale benchmark spanning 61 datasets, 21 methods, and 5 evaluation metrics, SurvivalPFN achieves strong predictive performance and often improves upon established survival models. These results suggest that SurvivalPFN offers a principled and practical foundation model for survival analysis, with potential applications in high-impact domains such as healthcare, finance, and engineering (this https URL).

---


### 69. [AnyAct: Towards Human Reenactment of Character Motion From Video](https://arxiv.org/abs/2605.15497)

**<font color=#1a73e8>作者：</font>** Liuhan Chen, Lei Zhong, Jiewei Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the problem of directly deriving an initial human reenactment from a monocular video of a non-human character. Our goal is not to reconstruct the source character itself but to reinterpret its motion as a plausible and editable human performance for downstream animation authoring. This task is challenging because existing video-based motion capture methods are largely restricted to human-centric structural spaces, while motion retargeting methods typically require structured 3D source motions and known source topologies. Our key insight is that sparse local articulated motion cues can preserve essential dynamics across large structural differences, providing a stable bridge from character video to human reenactment. Based on this observation, we propose AnyAct, which formulates character-video-driven human reenactment as conditional human motion generation from transferable sparse local 2D articulated motion. To make this practical, we introduce three key designs: human-motion-only supervision via augmented 3D-to-2D projection, progressive 3D-to-2D training to alleviate conditioning ambiguity, and global-local motion decoupling for reliable local motion control. We further construct a benchmark primarily covering diverse non-human character videos. Experiments on the benchmark show that AnyAct produces high-fidelity initial human reenactments that preserve the essential dynamics of the characters in reference videos, and further ablation studies validate the effectiveness of its core designs.

---


### 70. [Learning with Conflicts of Interest](https://arxiv.org/abs/2605.15504)

**<font color=#1a73e8>作者：</font>** Nischal Aryal, Arash Termehchy, Ali Vakilian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial, social, and political factors often prevent the interests of the owners of ML systems and services and their users from being perfectly aligned. ML systems often produce biased information that can influence users to make decisions that are not in their best interest. Current solution approaches require ML systems to implement protocols to mitigate their biases. However, ML system owners usually do not have any incentive to implement these protocols and often argue that it limits their freedom of expression or business. We believe that a successful solution to this problem must recognize the conflict of interest between the ML systems and their users, and use this information to protect users against information that adversely influences their decisions while allowing users to safely benefit from these systems. To this end, we propose a game-theoretic framework that models the interaction between ML systems and users with conflicts of interest. We present scalable algorithms with theoretical guarantees that maximize the amount of desired information and actions and minimize the amount of biased and manipulative actions in interaction with ML systems.

---


### 71. [X-SYNTH: Beyond Retrieval -- Enterprise Context Synthesis from Observed Human Attention](https://arxiv.org/abs/2605.15505)

**<font color=#1a73e8>作者：</font>** Guruprasad Raghavan, George Nychis, Rohan Narayana Murthy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In enterprise operations, the context required for an AI agent task is scattered across systems of record, static information stores, and communication channels. What is stored is system state, a lossy representation of the work that actually happened [2, 52]. The prevailing approach [17, 31, 34, 36] retrieves by matching request content to what is stored; for narrow requests this works well. But synthesis quality depends on knowing what to surface and how to interpret it: knowledge specific to each organization, team, and individual [5, 57, 61], present in behavioral patterns, absent from any retrieval index. For complex agentic tasks it breaks down: True Lead Rate is low, False Lead Rate is high, and the model has no mechanism to improve. We present X-SYNTH, a framework for enterprise context synthesis grounded in human attention, the digitally observable interaction signatures of each worker, encoding not just what they did but the sequence in which they did it, along with implicit reward signals. Behavioral traces preceding positive outcomes are distinguishable from those that did not, without external labeling. X-SYNTH models each individual's behavioral baseline as a Digital Twin Signature (DTS) and selects among seven qualitatively distinct attention filters: Proportional, Inverse, Differential, Recurrent, Comparative, Sequential, and Collective, per individual and per query, to identify causally relevant activity signatures. A four-stage pipeline assembles ranked context grounded in behavioral patterns rather than query embeddings. On a sales lead identification task, a frontier model unaided achieves 9.5% True Lead Rate (TLR) with 90.5% False Lead Rate (FLR). Augmented with X-SYNTH, TLR rises to 61.9% (6.5x) while FLR falls to 18.8%. Enterprise context synthesis is not a retrieval problem. It is a relevance problem, and human attention is its most reliable ground truth.

---


### 72. [parallelcbf: A composable safety-filter and auditability framework for tensor-parallel reinforcement learning](https://arxiv.org/abs/2605.15509)

**<font color=#1a73e8>作者：</font>** Yijun Lu, Zilei Yang, Yuyin Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While Isaac Lab provides massive parallel UAV simulation, OmniSafe and safe-control-gym provide constrained-RL benchmarks, and CBFKit provides control-barrier-function synthesis tooling, no existing framework unifies these capabilities for end-to-end safety-constrained training. ParallelCBF is the first framework to unify (i)~tensor-parallel UAV environments, (ii)~hard-gate CBF safety filters, (iii)~sharded BC-to-RL pipelines, and (iv)~first-class operational auditability -- pre-registration, watchdog registries, failure forensics, and dataset audits as composable APIs rather than user-implemented scripts. We release ParallelCBF v0.1.0 under Apache~2.0 with a four-layer composable API, a CPU PyTorch reference implementation of a dual-barrier (squared / linear-predictive) CBF, property-based safety invariance tests across vectorized batch sizes that complete in 1.67~s for the full 39-test suite, and a 31{,}415-episode behavior-cloning collection campaign whose curriculum mix, per-bucket yields, and dataset SHA-256 are auditable through the framework's own \texttt{ops} primitives. We report a representative end-to-end pipeline execution in which the framework's auditability layer halted a downstream training stage that did not meet pre-registered convergence criteria, preventing silent propagation of a degraded checkpoint -- an architectural property we argue is necessary, not merely useful, for reproducible empirical robotics research. The framework is installable via \texttt{pip install parallelcbf}; source and release artifacts are available at this https URL.

---


### 73. [OgBench: A Framework for Evaluating Graph Neural Networks on Omics Data](https://arxiv.org/abs/2605.15511)

**<font color=#1a73e8>作者：</font>** Louisa Cornelis, Johan Mathe, Louis Van Langendonck 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have become the dominant framework for inductive graph-level learning. Yet most benchmarks focus on the regime $n \gg p$, where the number of graphs $n$ greatly exceeds the number of nodes per graph $p$. This overlooks biological domains such as omics, which operate in the opposite $n \ll p$ regime, characterized by large graphs of genes, transcripts, or proteins across few patient samples. This raises the question: \textit{how do GNNs perform in this low-sample, high-node omics setting?} We introduce \texttt{OgBench} (Omics-Graph Bench), the first benchmarking platform for graph-level prediction in the $n \ll p$ regime characteristic of omics data. We provide a standardized, end-to-end modular infrastructure from raw omics data to families of featured graphs with varied structural properties. We benchmark classical GNNs, as well as GNNs designed for large graphs and omics applications, alongside MLPs and machine learning baselines to establish reference performances. Our results show that widely used GNNs often do not outperform simple MLPs and classical baselines. These findings challenge the prevailing assumption that graph structure inherently adds value in this domain, fostering a critical reassessment of current learning paradigms. Ultimately, by exposing these limitations, OgBench provides the open-source ecosystem necessary for the community to develop and validate novel architectures explicitly tailored for biological graphs. The code is available at this https URL.

---


### 74. [RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably](https://arxiv.org/abs/2605.15514)

**<font color=#1a73e8>作者：</font>** Yufeng Du, Phillip Harris, Minyang Tian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We identify intrinsic limitations of Rotary Positional Embeddings (RoPE) in Transformer-based long-context language models. Our theoretical analysis abstracts away from the specific content of the context and depends only on its length. We prove that as context length increases, RoPE-based attention becomes unpredictable and loses two properties that are central to its effectiveness. First, it loses its locality bias: RoPE is no more likely to favor nearer positions than substantially farther ones. Second, it loses consistency in token relevance: a key vector that receives a higher attention score than an alternative at one position may receive a lower score at another. In both cases, the probability of failure approaches 0.5, no better than random guessing. We further prove that the attention score can remain unchanged when a key token is moved to a different position, or even replaced by a different token, indicating a failure to distinguish positions or tokens. Adjusting the RoPE base trades off distinguishing positions against distinguishing tokens but cannot preserve both at the same time. Increasing the RoPE base hyperparameter, a common practice in today's long-context models, helps distinguish different tokens, but inevitably sacrifices the ability to distinguish positions. Our empirical analysis shows that multi-head, multi-layer architectures are insufficient to overcome these limitations. Our findings suggest that fundamentally new mechanisms for encoding position and token order may be needed in future Transformer long-context language models.

---


### 75. [DiffVAS: Diffusion-Guided Visual Active Search in Partially Observable Environments](https://arxiv.org/abs/2605.15519)

**<font color=#1a73e8>作者：</font>** Anindya Sarkar, Srikumar Sastry, Aleksis Pirinen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual active search (VAS) has been introduced as a modeling framework that leverages visual cues to direct aerial (e.g., UAV-based) exploration and pinpoint areas of interest within extensive geospatial regions. Potential applications of VAS include detecting hotspots for rare wildlife poaching, aiding search-and-rescue missions, and uncovering illegal trafficking of weapons, among other uses. Previous VAS approaches assume that the entire search space is known upfront, which is often unrealistic due to constraints such as a restricted field of view and high acquisition costs, and they typically learn policies tailored to specific target objects, which limits their ability to search for multiple target categories simultaneously. In this work, we propose DiffVAS, a target-conditioned policy that searches for diverse objects simultaneously according to task requirements in partially observable environments, which advances the deployment of visual active search policies in real-world applications. DiffVAS leverages a diffusion model to reconstruct the entire geospatial area from sequentially observed partial glimpses, which enables a target-conditioned reinforcement learning-based planning module to effectively reason and guide subsequent search steps. Extensive experiments demonstrate that DiffVAS excels in searching diverse objects in partially observable environments, significantly surpassing state-of-the-art methods on several datasets.

---


### 76. [Neural Point-Forms](https://arxiv.org/abs/2605.15524)

**<font color=#1a73e8>作者：</font>** Bruno Trentini, Jacob Hume, Vincenzo Antonio Isoldi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Point cloud learning often rests on the premise that observed samples are noisy traces of an underlying geometric object, such as a manifold embedded in a high-dimensional feature space. Yet much of this geometry is not captured directly by coordinates, pairwise distances, or learned graph neighborhoods alone. In the smooth setting, differential forms are devices to encode higher order tangency information. In this work, we introduce a new family of principled learnable geometric features for point clouds called neural point-forms (NPFs). In the absence of a natural tangency structure, we instead use Laplacian-based techniques from Diffusion Geometry to build a discrete model for comparing differential forms on point clouds via inner products. In the continuum, submanifolds of a shared ambient feature space are represented as comparison matrices, whose entries describe how pairs of feature forms interact with extrinsic tangency information. We make this intuition precise by proving the long-run consistency of comparison matrices under standard sampling, bandwidth, density, and manifold-hypothesis assumptions. This yields a compact, efficient and permutation-invariant neural layer whose output is a learned form-comparison matrix. Across synthetic and biologically relevant experiments, we show that NPFs provide a competitive, and interpretable representation, with the strongest benefits appearing when labels depend on sampling density, manifold-like structure, or response-relevant population geometry.

---


### 77. [Process Rewards with Learned Reliability](https://arxiv.org/abs/2605.15529)

**<font color=#1a73e8>作者：</font>** Jinyuan Li, Langlin Huang, Chengsong Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Process Reward Models (PRMs) provide step-level feedback for reasoning, but current PRMs usually output only a single reward score for each step. Downstream methods must therefore treat imperfect step-level reward predictions as reliable decision signals, with no indication of when these predictions should be trusted. We propose BetaPRM, a distributional PRM that predicts both a step-level success probability and the reliability of that prediction. Given step-success supervision from Monte Carlo continuations, BetaPRM learns a Beta belief that explains the observed number of successful continuations through a Beta-Binomial likelihood, rather than regressing to the finite-sample success ratio as a point target. This learned reliability signal indicates when a step reward should be trusted, enabling downstream applications to distinguish reliable rewards from uncertain ones. As one application, we introduce Adaptive Computation Allocation (ACA) for PRM-guided Best-of-N reasoning. ACA uses the learned reliability signal to stop when a high-reward solution is reliable and to spend additional computation on uncertain candidate prefixes. Experiments across four backbones and four reasoning benchmarks show that BetaPRM improves PRM-guided Best-of-N selection while preserving standard step-level error detection. Built on this signal, ACA improves the accuracy--token tradeoff over fixed-budget Best-of-16, reducing token usage by up to 33.57% while improving final-answer accuracy.

---


### 78. [Rethinking Neural Network Learning Rates: A Stackelberg Perspective](https://arxiv.org/abs/2605.15530)

**<font color=#1a73e8>作者：</font>** Sihan Zeng, Sujay Bhatt, Sumitra Ganesh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks are typically trained with a single learning rate across all layers. While recent empirical evidence suggests that assigning layer-specific learning rates can accelerate training, a principled understanding of the conditions and mechanisms under which non-uniform learning rates are beneficial remains limited. In this work, we investigate non-uniform learning rates through the lens of Stackelberg optimization. Specifically, we demonstrate that training neural networks with a smaller learning rate for the body layers and a larger learning rate for the final layer can be interpreted as a two-time-scale alternating gradient descent algorithm applied to a Stackelberg reformulation of the original objective. We establish finite-time convergence guarantees for the algorithm under broad conditions that accommodate constraint sets and non-smooth activation functions. Beyond convergence, we identify two mechanisms by which non-uniform learning rates can outperform uniform learning rates: (i) we show that certain problem instances induce a Stackelberg objective with stronger optimization structure than the original objective, yielding faster convergence to globally optimal solutions, (ii) our numerical analysis reveals that the Stackelberg objective can exhibit substantially sharper local curvature, especially in early training, which leads to more informative gradients and learning acceleration. Experiments in supervised learning and reinforcement learning support our findings.

---


### 79. [Tuning-free Instruction-based Video Editing Via Structural Noise Initialization and Guidance](https://arxiv.org/abs/2605.15533)

**<font color=#1a73e8>作者：</font>** Song Wu, Xinyu Chen, Qian Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video editing poses a significant challenge. While a series of tuning-free methods circumvent the need for extensive data collection and model training, they often underutilize the rich information embedded within noisy latent, leading to unsatisfactory results. To address this, we propose a \textit{tuning-free, instruction-based} video editing framework. We approach video editing from the perspective of noisy latent: we design a Structural Noise Initialization Strategy (SNIS) to secure a superior editing starting point by assigning higher noise levels to edited regions (to facilitate content change) and lower noise levels to unedited regions (to maintain content consistency). We introduce a Noise Guidance Mechanism (NGM), which leverages the video prior in the generative model and effectively integrates rich information within the noisy latent to guide the denoising process, thereby preserving unedited content and overall visual coherence. Experiments show that our proposed method achieves better visual quality and state-of-the-art performance.

---


### 80. [Learning Dynamic Structural Specialization for Underwater Salient Object Detection](https://arxiv.org/abs/2605.15535)

**<font color=#1a73e8>作者：</font>** Lin Hong, Chenhui Wang, Linan Deng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater salient object detection (USOD) has attracted increasing attention for underwater visual scene understanding and vision-guided robotic applications. However, existing USOD methods still struggle with underwater image degradations, which often lead to inaccurate object localization, fragmented salient regions, and coarse boundary prediction. To address these challenges, this paper proposes DSS-USOD, a novel RGB-based USOD method built upon dynamic structural specialization. DSS-USOD extracts a shared base representation from a single underwater image, decomposes it into boundary-sensitive and region-coherent structural features, and dynamically coordinates their contributions according to local structural context. Specifically, the extracted shared base representation is decomposed into a boundary-sensitive branch for modeling fine-grained boundary details and a region-coherent branch for capturing region-level structural consistency. A spatial coordination module is then introduced to adaptively regulate the relative contributions of the two branches according to local structural context. Moreover, cooperative structural supervision is introduced to promote branch specialization and stabilize spatial coordination, enabling DSS-USOD to better balance boundary precision and region coherence under degraded underwater conditions. Extensive experiments show that DSS-USOD achieves superior performance on benchmark datasets. Finally, real-world deployment on an underwater robot validates the practical effectiveness of DSS-USOD for underwater object inspection.

---


### 81. [3DTMDet: A Dual-Path Synergy Network of Transformer and SSM for 3D Object Detection in Point Clouds](https://arxiv.org/abs/2605.15546)

**<font color=#1a73e8>作者：</font>** Bingwen Qiu, Yuan Liu, Junqi Bai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A fundamental challenge in point cloud object detection lies in the conflict between the extreme sparsity of distant points and the need for remote context understanding. The existing methods typically use 1D serialization to expand the receptive field, which inevitably discards already scarce local geometric details and reduces detection of distant and small objects. To address this issue, we propose 3DTMDet, a novel detection network that synergistically combines state space models (Mamba) with Transformers. The core idea is to utilize SSM's linear complexity and advantages in long sequence modeling to effectively capture global interactions between sparse and distant points, while using Transformer modules with local attention to encode fine-grained geometric structures in local point sets, preserving accurate shape information. We propose the 3D Hybrid Mamba Transformer (3DHMT) block, which uses an SSM-Attention-SSM pipeline to balance global context understanding and local detail preservation, effectively alleviating the tension between receptive field enlargement and geometric preservation in remote detection. In addition, we introduced a voxel generation block inspired by LiDAR physics, which diffuses features along the sensor observation direction to reconstruct the complete object structure of occlusion and distant areas. Extensive experiments conducted on the KITTI and ONCE datasets have shown that 3DTMDet outperforms state-of-the-art detectors. The code is available at this https URL.

---


### 82. [CTF4Nuclear: Common Task Framework for Nuclear Fission and Fusion Models](https://arxiv.org/abs/2605.15549)

**<font color=#1a73e8>作者：</font>** Stefano Riva, Carolina Introini, Antonio Cammi 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The demand for clean energy is ever increasing, with new nuclear technologies presenting a complementary solution to renewable energies. However, designing and operating these systems is exceptionally difficult, given the complexity of the physical phenomena that interact to form the system dynamics. While high-fidelity simulations help to understand the non-linear, multi-physics interactions within a reactor, they are computationally expensive and rarely suitable for real-time applications. Furthermore, model-based approaches are inherently sensitive to simplifying assumptions required to derive their governing equations and parameters, leading to inevitable discrepancies with real-world measurements. In contrast, Machine Learning (ML) methods have the potential to generate reliable surrogate models which may be able to quickly predict the system's behaviour. However, the number of data-driven methods that can potentially be used for this task is large and diverse. In a safety-critical setting such as nuclear engineering, a fair comparison of different ML methods, and a clear understanding of their advantages and limitations, is of paramount importance. To address this, we introduce a Common Task Framework (CTF) for ML in nuclear engineering, building upon previous efforts in dynamical systems and seismology. This CTF considers a curated set of datasets from different nuclear and nuclear-adjacent systems. The CTF evaluates the performance of a method on 12 established metrics, alongside a new paradigm focused on system monitoring from sparse measurements only. We illustrate the framework by benchmarking standard ML baselines against these datasets, revealing current method limitations. Our vision is to replace ad hoc comparisons with standardized evaluations on hidden test sets, raising the bar for rigour and reproducibility in scientific ML for the nuclear industry.

---


### 83. [Characterizing Learning in Deep Neural Networks using Tractable Algorithmic Complexity Analysis](https://arxiv.org/abs/2605.15551)

**<font color=#1a73e8>作者：</font>** Pedram Bakhtiarifard, Sophia N. Wilson, Mahmoud Afifi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training large-scale deep neural networks (DNNs) is resource-intensive, making model compression a practical necessity. The widely accepted ''learning as compression'' hypothesis posits that training induces structure in network weights, which enables compression. Measuring this structure through Kolmogorov-Chaitin-Solomonoff (KCS) complexity is appealing, but existing estimators based on the Coding Theorem Method (CTM) and the Block Decomposition Method (BDM) are limited to small binary objects and do not scale to modern DNNs. We introduce the Quantized Block Decomposition method (QuBD), which extends algorithmic complexity estimation to any $k$-ary object. QuBD first quantizes the network weights to a finite alphabet, then estimates the KCS complexity by aggregating per bit-plane CTM estimates. We show theoretically that QuBD yields a strictly tighter estimation gap with respect to true KCS complexity than binarization-based methods. Using QuBD, we study how the algorithmic complexity of neural network weights evolves during training, showing that it decreases as models learn, scales with data budget, increases during overfitting, follows the delayed generalization observed during grokking, and correlates with generalization performance. We further show that algorithmic information resides predominantly in the most significant bit-planes, which can serve as a practical diagnostic for determining appropriate post-training quantization levels. This work offers novel insights into learning mechanisms in DNNs by providing the first scalable, tractable estimates of KCS complexity for large, non-binary objects such as DNN weights.

---


### 84. [When Latent Geometry Is Not Enough: Draft-Conditioned Latent Refinement for Non-Autoregressive Text Generation](https://arxiv.org/abs/2605.15557)

**<font color=#1a73e8>作者：</font>** De Shuai Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion and flow models are attractive for non-autoregressive text generation because they can update all positions in parallel. A major difficulty is the interface between continuous latent states and discrete tokens. This report studies a draft-conditioned latent refinement model built from a frozen BERT encoder, a parallel decoder, a denoising DraftPrior, a local FlowNet, and a learned diagonal MetricNet. Early Gaussian-start experiments showed that good latent-space metrics, such as scale matching or cosine similarity, do not guarantee good decoding. Generated latents can be close to real encoder latents but still produce high-entropy, biased, or repetitive token distributions. We therefore frame the task as controlled local refinement rather than full generation from noise. On ROCStories, using the first two sentences as prompt and the last three as target, full 768-dimensional BERT latents recover tokens much better than compressed 256-dimensional latents. With 768-dimensional latents, DraftPrior target-token probability is 0.938 for clean drafts, 0.613 for 3% token dropout, 0.483 for 5% dropout, and 0.272 for 10% dropout. Local flow refinement and fused decoder-aware readout give modest additional gains, while metric learning and OT-style alignment improve geometry but do not close the decoder gap. The main result is a diagnostic one: latent geometry alone is not enough. Continuous latent text generation should be evaluated by decoder recoverability, the quality of the start distribution, and whether refinement preserves decoder-readable structure.

---


### 85. [RoiMAM: Region-of-Interest Medical Attention Model for Efficient Vision-Language Understanding](https://arxiv.org/abs/2605.15561)

**<font color=#1a73e8>作者：</font>** Jiayan Yang, Zhuoyu Wu, Wenqi Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) facilitate medical visual question answering (MedVQA) by jointly interpreting images and text. However, existing models typically depend on large architectures and closed-set answers, which limits their efficiency and potential clinical applicability. To overcome these shortcomings, we introduce RoiMAM, an efficient VLM. It integrates a training-free ROI Generation Module with Semantic Selective Suppression to focus on lesion-relevant regions, alongside a Text Prompt Enhancer module that provides modality-specific context without introducing training parameters. Compared to the widely used MedVInT-TD model, our design achieves efficient and accurate diagnosis at less than 20\% of the model size, while improving accuracy by approximately 2% on SLAKE and 4.6% on PMC-VQA.

---


### 86. [CrystalBoltz: End-to-End Protein Structure Determination via Experiment-Guided Diffusion for X-Ray Crystallography](https://arxiv.org/abs/2605.15564)

**<font color=#1a73e8>作者：</font>** Minseo Kim, Huanghao Mai, Jay Shenoy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative models trained on public databases of protein structures, most of which have been determined by X-ray crystallography, now provide powerful priors for structure prediction. However, they are not readily conditioned on the measurements from a new crystallographic experiment, limiting their use for X-ray structure determination. In crystallography, the measured structure-factor amplitudes do not by themselves determine an electron density map or atomic structure because the associated phases are unobserved and must be inferred. Structure determination therefore remains an inverse problem in which candidate models must be both structurally plausible and consistent with measured diffraction data, often requiring substantial manual refinement by human experts. Emerging methods aim to incorporate experimental information more directly into predictive and refinement workflows. We present CrystalBoltz, a generative framework that casts crystallographic refinement as Bayesian inference over atomic structures and operates directly on structure-factor amplitudes. CrystalBoltz moves from unguided generation with a pre-trained prior over protein structures to experiment-guided posterior sampling, followed by atomic coordinate and B-factor refinement. Across multiple protein crystallography datasets, CrystalBoltz attains lower coordinate RMSD and lower R-factors than the strongest baselines considered, while reducing runtime by a factor of 33 relative to existing experimentally guided refinement.

---


### 87. [Position: Artificial Intelligence Needs Meta Intelligence -- the Case for Metacognitive AI](https://arxiv.org/abs/2605.15567)

**<font color=#1a73e8>作者：</font>** Sergei Chuprov, Richard D. Lange, Leon Reznik 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues for metacognition as a general design principle for creating more accurate, secure, and efficient AI. The metacognitive solution involves systems monitoring their own states and judiciously allocating resources depending on each problem instance's difficulty or cost of mistakes. Drawing inspiration both from past work on resource-rational AI and from well-documented metacognitive strategies in psychology and cognitive science, we identify specific challenges in embedding these strategies into AI design and highlight open theoretical and implementation problems. We showcase these principles through a tangible example of improved learning efficiency, effectiveness, and security in a Federated Learning (FL) case study. We show how these principles can be translated into practice with a novel software framework developed specifically to allow the community to design, deploy, and experiment with metacognition-enabled AI applications.

---


### 88. [Response-Conditioned Parallel-to-Sequential Orchestration for Multi-Agent Systems](https://arxiv.org/abs/2605.15573)

**<font color=#1a73e8>作者：</font>** Nurbek Tastan, Alex Iacob, Lorenzo Sani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems can solve complex tasks through collaboration between multiple Large Language Model agents. Existing collaboration frameworks typically operate in either a parallel or a sequential mode. In the parallel mode, agents respond independently to queries followed by aggregation of responses. In contrast, sequential systems allow agents to communicate via a directed topology and refine one another step by step. However, both modes are inadequate for achieving the desired objectives of minimizing communication and latency while simultaneously maximizing the accuracy of the final response. In this work, we introduce a hybrid paradigm called Nexa, a trainable response-conditioned policy that bridges the gap between the two modes. Nexa begins with a parallel execution stage, embeds the resulting responses into a shared semantic space, and then predicts a sparse directed acyclic communication graph. If the graph is empty, the system remains purely parallel; if it is non-empty, the system performs one sequential message propagation. The policy is a lightweight transformer model, and the method avoids the need for external LLM judges or reward models, as well as hand-crafted test-time topology search. We formalize this hybrid execution problem, show that the resulting graph is acyclic by construction, and that the framework strictly subsumes pure parallel execution, and present a training procedure based on policy-gradient optimization. Results demonstrate that the response-conditioned policy learned by Nexa under one setting can be reused when the number of agents, the task, or the underlying agent changes, thus emphasizing the generalizability of the learned communication policy.

---


### 89. [MI-CXR: A Benchmark for Longitudinal Reasoning over Multi-Interval Chest X-rays](https://arxiv.org/abs/2605.15574)

**<font color=#1a73e8>作者：</font>** Sunghwan Steve Cho, Yunseok Han, Jaeyoung Do  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Longitudinal chest X-ray (CXR) interpretation requires reasoning over disease evolution across multiple patient visits, yet most existing medical VQA benchmarks focus on single images or short-horizon image pairs. We introduce MI-CXR, a benchmark for standardized evaluation of Multi-Interval longitudinal reasoning over multi-visit CXR sequences, without requiring free-form report generation or additional clinical context. MI-CXR comprises five-way multiple-choice questions over five-visit patient timelines and instantiates three complementary task families: Temporal Event Localization, Interval-wise Change Reasoning, and Global Trajectory Summarization, which assess clinically grounded visual reasoning over time. Evaluating 14 state-of-the-art vision-language models (VLMs) shows low overall performance, with an average accuracy of 29.3%, only modestly above random guessing. Using stage-wise diagnostic probing, we find that models often produce locally plausible interval descriptions but fail to enforce temporal constraints or compose evidence into globally consistent decisions over the full timeline. These findings reveal key limitations of current VLMs and establish MI-CXR as a principled benchmark for longitudinal medical reasoning. The benchmark is available at this https URL

---


### 90. [Gaussian Relational Graph Transformer](https://arxiv.org/abs/2605.15575)

**<font color=#1a73e8>作者：</font>** Zezhong Ding, Jin Li, Xugang Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relational graph learning models relational databases as graphs and has demonstrated superior performance on a wide range of relational predictive tasks. However, existing methods struggle to capture long-range dependencies due to information decay in their message-passing mechanisms, and recent relational graph transformers remain limited in jointly modeling structural, semantic, and temporal information. In this paper, we propose GelGT, a Gaussian relational graph transformer that explicitly addresses these challenges. GelGT introduces a structure-semantic collaborative sampling strategy to preserve structural connectivity while filtering irrelevant semantic information, and incorporates a Gaussian graph attention mechanism with a learnable Gaussian bias on the sampled subgraphs to dynamically encode temporal dependencies. Extensive experiments on various real-world datasets demonstrate that GelGT achieves state-of-the-art downstream task performance, with up to a 13.8% improvement in predictive performance.

---


### 91. [LDGuid: A Framework for Robust Change Detection via Latent Difference Guidance](https://arxiv.org/abs/2605.15582)

**<font color=#1a73e8>作者：</font>** Jiaxuan Zhao, Ali Bereyhi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern deep learning models for change detection (CD) often struggle to explicitly represent task-relevant semantic differences. This paper proposes the Latent Difference Guidance (LDGuid) framework that explicitly learns and injects semantic differences into CD models. LDGuid deploys adversarial autoencoding to implement a difference embedding (DE) module. The DE module is pretrained via the information bottleneck method, restricting it to learn only task-relevant differences between pre- and post-event samples. The learned latent difference is then used as an explicit guidance signal in the CD model. We validate LDGuid by integrating it into U-Net, BIT, and AERNet baselines for CD and evaluating it on LEVIR-CD, WHU-CD, SVCD, and CaBuAr datasets. Experimental results show that LDGuid enhances segmentation performance across all benchmarks, with particularly remarkable gains in challenging settings affected by spectral noise. The results further highlight the ability of LDGuid in incorporating domain knowledge, such as task-specific spectral indices. Our findings suggest that semantic difference learning can drastically enhance the robustness of CD in remote sensing.

---


### 92. [Unsupervised 3D Human Pose Estimation via Conditional Multi-view Ancestral Sampling](https://arxiv.org/abs/2605.15583)

**<font color=#1a73e8>作者：</font>** Ryohei Goto, Takuya Fujihashi, Shunsuke Saruwatari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a method of estimating a 3D human pose from a single view without 3D supervision. The key to our method is to leverage the 2D diffusion priors of motion diffusion models (MDMs) pre-trained on large 2D human pose datasets. Specifically, we extend multi-view ancestral sampling of diffusion models to the task of 2D-3D lifting of human pose. To this end, we newly propose a conditional multi-view ancestral sampling (cMAS) that optimizes the 3D pose such that its multi-view projections follow the manifold in 2D MDM noise space, while conditioning the 3D pose to match the given 2D poses and anatomical constraints of humans. Experiments on the Yoga dataset demonstrate that our method achieves better cross-domain performance compared to state-of-the-art supervised and unsupervised 3D pose estimation methods, including extreme human poses where 3D supervision is unavailable. Code is available at: this https URL.

---


### 93. [See Before You Code: Learning Visual Priors for Spatially Aware Educational Animation Generation](https://arxiv.org/abs/2605.15585)

**<font color=#1a73e8>作者：</font>** Yuejia Li, Ke He, Junheng Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can generate executable code for educational animations, but the resulting renders often exhibit visual defects, including element overlap, misalignment, and broken animation continuity. These defects cannot be reliably detected from the code alone and become apparent only after execution. We formalize this problem as render-feedback-aware constrained code generation: given a natural language specification, the model must generate executable code whose rendered output satisfies structured quality criteria that can be evaluated only after rendering. To address this problem, we introduce OmniManim, a render-feedback-aware educational animation generation framework built around a shared scene state, explicit visual planning, structured post-render diagnostics, and localized repair. Within OmniManim, the Vision Agent is a task-specific visual planning module: it predicts sparse keyframe layouts with coarse-to-fine bounding-box denoising and optimizes an interpolation-aware objective to reduce intermediate-frame failures induced by downstream animation interpolation. We further construct two datasets, ManimLayout-1K and EduRequire-500, and provide a reproducible evaluation protocol covering executability, instructional quality, visual quality, and efficiency. On EduRequire-500, OmniManim improves measured render quality over both single-model baselines and existing multi-agent frameworks. Systematic ablation studies further verify that explicit visual planning, especially its coarse spatial prior, bounding-box refinement, and interpolation-aware optimization, is central to these gains.

---


### 94. [Embracing Biased Transition Matrices for Complementary-Label Learning with Many Classes](https://arxiv.org/abs/2605.15586)

**<font color=#1a73e8>作者：</font>** Tan-Ha Mai, Chao-Kai Chiang, Han-Hwa Shih 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complementary-label learning (CLL) is a weakly supervised paradigm where instances are labeled with classes they do not belong to. Despite a decade of research, CLL methods remain competitive mainly on 10-class classification, with scaling to large label spaces continuing to be an enduring bottleneck. This limitation stems from the common assumption of uniform label generation in traditional methods, which fatally dilutes the learning signal in many-class settings. In this paper, we demonstrate that this long-standing barrier can be overcome by deliberately designing a biased (non-uniform) generation process that restricts complementary labels to a subset of classes. This finding motivates us to propose Bias-Induced Constrained Labeling (BICL), a principled framework spanning data collection to training that leverages this bias. BICL enables effective learning on CIFAR-100 and TinyImageNet-200, achieving more than sevenfold accuracy improvements over traditional methods. Our findings establish a new trajectory for making CLL feasible for many classes in real-world applications.

---


### 95. [Efficient Image Synthesis with Sphere Latent Encoder](https://arxiv.org/abs/2605.15592)

**<font color=#1a73e8>作者：</font>** Tung Do, Thuan Hoang Nguyen, Hao Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step image generation has seen rapid progress, with consistency and meanflow-based methods significantly reducing the number of sampling steps. Despite their low inference cost, these approaches often suffer from training instability and limited scalability. Sphere Encoder is a recent alternative that produces high-quality images in only a few steps; however, it requires repeated transitions between the pixel space and latent space during inference while jointly optimizing reconstruction and generation within a single architecture. This design leads to computational inefficiency and objective conflict between reconstruction and generation. To address these limitations, we decouple the framework into a fixed pretrained image encoder and a separate latent denoising model trained entirely in a spherical latent space. Our approach eliminates repeated pixel-space operations during training and inference, improving efficiency and allowing reconstruction and generation to specialize independently. On Animal-Faces, Oxford-Flowers and ImageNet-1K datasets, our method significantly outperforms Sphere Encoder in both generation quality and inference speed, while achieving competitive results against strong few-step and multi-step baselines.

---


### 96. [Pretraining Objective Matters in Extreme Low-Data FGVC: A Backbone-Controlled Study](https://arxiv.org/abs/2605.15599)

**<font color=#1a73e8>作者：</font>** Alexander Hackett, Srikanth Thudumu, Ginny Fisher 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extreme low-data fine-grained classification is common in expert domains where labeling is expensive, yet practitioners still need principled guidance for selecting pretrained encoders. We study emerald inclusion grading with a custom dataset of labeled images across three classes and ask: under matched backbone capacity, how does pretraining objective affect downstream representation quality? We compare four frozen ViT-B/16 encoders trained with supervised classification, contrastive learning (SigLIP2), masked reconstruction (MAE), and self-distillation (DINOv3), and evaluate them with leave-one-out cross-validation using linear and nonlinear probes. To control statistical noise in the low-N regime, we use permutation testing (N=1000) on macro one-vs-rest AUC. Supervised and contrastive encoders provide the strongest linear separability (logistic AUC: 0.768 and 0.735; SVM AUC: 0.739 and 0.697), while MAE improves under nonlinear probes (XGBoost AUC: 0.713). We find that DINOv3 underperforms across probe families in this domain. These results support a practical recommendation for extreme low-data FGVC: prioritize margin-enforcing pretraining objectives when data scarcity restricts probing to linear decision rules, and consider reconstruction-style encoders when nonlinear classifiers are feasible given dataset constraints.

---


### 97. [Offline Reinforcement Learning with Universal Horizon Models](https://arxiv.org/abs/2605.15603)

**<font color=#1a73e8>作者：</font>** Hojun Chung, Junseo Lee, Songhwai Oh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (RL) offers a compelling approach to offline RL by enabling value learning on imagined on-policy trajectories. However, it often suffers from compounding errors due to repeated model inference on self-generated states. While geometric horizon models (GHM) alleviate this issue through direct prediction over a discounted infinite-horizon future, they remain challenged in accurately modeling distant future states. To this end, we introduce universal horizon models (UHM), a generalization of GHM that directly predicts future states under arbitrary horizons. Leveraging this flexibility, we propose a scalable value learning method that employs a winsorized horizon distribution to stabilize training by capping excessively large horizons. Experimental results on 100 challenging OGBench tasks demonstrate that the proposed method outperforms competitive baselines, particularly on tasks with highly suboptimal datasets and those requiring long-horizon reasoning. Project page: this https URL

---


### 98. [VSPO: Vector-Steered Policy Optimization for Behavioral Control](https://arxiv.org/abs/2605.15604)

**<font color=#1a73e8>作者：</font>** Xuechen Zhang, Zijian Huang, Kai Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern language models often need to optimize a primary accuracy objective while also accommodating secondary behavioral preferences, such as verbosity, agreeableness, or the level of technical expertise in its response. In practice, a base model may exhibit a desired behavior very rarely or not at all. Thus, endowing the model with a target behavior creates a sparse behavioral reward bottleneck. To address such multi-objective problems, we introduce Vector-Steered Policy Optimization (VSPO) which employs a steering vector associated with the target behavior to control the behavior intensity of the generated rollouts. VSPO is obtained by modifying GRPO to sample rollouts with varying steering intensities. This process can be interpreted as an on-policy latent self-distillation procedure where the model internalizes its steering vector. By varying steering intensities, VSPO upsamples rare behaviors and enriches rollout diversity, which alleviates the sparse reward issue and provably accelerates the policy optimization. Through comprehensive theory and experiments, we establish that VSPO has favorable properties compared to vanilla reward shaping and other alternative approaches. Specifically, under a bandit abstraction, VSPO provably achieves better iteration complexity than reward-shaped GRPO when the steering-induced distributions are sufficiently aligned with the target behavior. We evaluate VSPO across multiple reasoning benchmarks, including MATH and MMLU-Pro, for four target behaviors: explanation expertise, confidence expression, robustness to misleading context, and response verbosity. Our results show that VSPO consistently improves the control along target behavior while maintaining or improving task accuracy compared with reward shaping, teacher-trace distillation, and guidance-based baselines.

---


### 99. [Transformer-like Inference from Optimal Control](https://arxiv.org/abs/2605.15608)

**<font color=#1a73e8>作者：</font>** Aditya Kudre, Heng-Sheng Chang, Prashant G. Mehta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoder-only transformers compute the conditional probability of the next token from a sequence of past observations. This paper derives, from first principles, inference architectures that solve the same prediction problem - and in doing so, recovers transformer-like layer operations as a consequence of optimal control theory. The framework is developed for two model classes: a nonlinear model of discrete-valued processes, directly motivated by the transformer, and a linear Gaussian model as a tractable baseline. For both model classes, the prediction objective is reformulated as an optimal control problem whose solution yields an explicit inference algorithm, the dual filter, with a layer structure that mirrors the layer structure of a decoder-only transformer. Numerical experiments provide a comparison of the optimal control to attention weights from a trained transformer. These experiments reveal that when the embedding dimension is insufficient, the transformer implicitly exploits non-Markovian structure.

---


### 100. [TopoEvo: A Topology-Aware Self-Evolving Multi-Agent Framework for Root Cause Analysis in Microservices](https://arxiv.org/abs/2605.15611)

**<font color=#1a73e8>作者：</font>** Junle Wang, Xingchuang Liao, Wenjun Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Root cause analysis (RCA) in microservices is challenging due to (i) noisy and heterogeneous multimodal observability (metrics, logs, traces), (ii) cascading failure propagation that amplifies downstream symptoms, and (iii) non-stationary topology drift induced by autoscaling and rolling updates. Recent LLM-based RCA agents can generate tool-grounded explanations, yet they often remain topology-agnostic and suffer from \emph{symptom-amplification bias}, misattributing the root cause to salient downstream victims. We propose \textbf{TopoEvo}, a topology-aware self-evolving multi-agent framework that couples graph representation learning with structured, topology-constrained reasoning. TopoEvo first introduces \emph{Metric-orthogonal Multimodal Alignment} (MOMA), which decomposes metric embeddings into complementary subspaces and contrastively aligns logs and traces to reduce modality redundancy and sparsity, yielding stable node representations for graph encoding. It then applies \emph{Vector Quantization} (VQ) to discretize topology-enhanced states into auditable \emph{symptom tokens} with a symptom lexicon, enabling reliable retrieval and token-level evidence grounding. On top of these discrete topology cues, TopoEvo performs a multi-agent \emph{Hypothesis--Evidence--Test} (HET) workflow to explicitly verify propagation-consistent explanations and separate initiating anomalies from amplified downstream symptoms. Finally, a \emph{Self-Evolving Mechanism} refreshes hierarchical incident memory and performs conservative test-time adaptation with high-confidence pseudo-labels to maintain robustness under drift.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
