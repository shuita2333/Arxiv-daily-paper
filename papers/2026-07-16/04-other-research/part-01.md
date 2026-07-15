# 📦 其他研究 | 2026年07月16日

> 本类共 **203** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

---

### 1. [Optimal Adaptive Market Making: A Theoretical Framework for High-Yield Liquidity Provision in Perpetual Futures Markets](https://arxiv.org/abs/2607.11888)

**<font color=#1a73e8>作者：</font>** Minmin Zeng, Yi Liu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We develop a rigorous theoretical framework for optimal market making in perpetual futures markets with zero maker fees. We model the market maker's problem as a stochastic optimal control problem on a filtered probability space, where the controls are adaptive bid-ask spreads and inventory hedging decisions across two exchanges. Our contributions include: (i) a PnL decomposition theorem separating revenue into spread income, adverse selection loss, inventory carrying cost, hedging friction, and funding rate exposure; (ii) the Hamilton-Jacobi-Bellman equation for the joint spread-inventory-hedging control problem under CARA utility with a verification theorem; (iii) High-APY Regime Theorems characterizing profitable regions via five dimensionless parameters, culminating in a Master APY Formula; (iv) analysis of zero-fee economics on decentralized perpetual exchanges with optimal entry-exit thresholds; (v) optimal cross-exchange hedging policies with funding rate dynamics and a hedge regime trichotomy; (vi) a robustness margin quantifying parameter uncertainty tolerance; (vii) exponential drawdown probability bounds and a universal APY-VaR identity; (viii) ergodic inventory distribution under optimal control with Bayesian adaptive estimation; (ix) Kelly-optimal leverage with ruin boundaries; and (x) multi-pair portfolio allocation with diversification saturation results. Numerical analysis with twenty-three figures reveals phase transitions between profitable and unprofitable regimes. Our framework unifies and extends the Avellaneda-Stoikov, Gueant-Lehalle-Fernandez-Tapia, and Glosten-Milgrom paradigms for modern decentralized venue microstructure.

---


### 2. [G-SHARE: A Guideline-Based Structured Reasoning Framework for Human-Factor Event Diagnosis](https://arxiv.org/abs/2607.11892)

**<font color=#1a73e8>作者：</font>** Xingyu Xiao, Mao Du, Jiejuan Tong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human-factor event diagnosis is essential for learning from operational events in nuclear power plants, yet its quality depends strongly on expert interpretation of narrative reports and guideline-based this http URL data-driven or one-shot large language model approaches often lack structured reasoning, have limited alignment with formal diagnostic guidelines, and may generate logically inconsistent conclusions. To address this issue, this study proposes G-SHARE, a guideline-based structured reasoning framework that operationalizes the CNNP nine-step human-factor event diagnosis guideline into a multi-stage diagnostic this http URL framework consists of evidence extraction, stepwise diagnostic reasoning, and post-hoc consistency repair, enabling explicit use of report evidence, intermediate rationale generation, and logical validation of diagnostic outputs. A dataset of real human-factor event reports was constructed from Chinese nuclear industry sources, and a gold-standard subset annotated by domain experts was used for evaluation. Results show that G-SHARE substantially outperforms one-shot prompting and traditional machine learning baselines, with the strongest version achieving the best overall accuracy and macro-F1. Ablation results further indicate that structured reasoning and consistency enforcement are critical to robust diagnosis, especially under weak prompting conditions. The findings demonstrate the value of transforming expert diagnostic guidelines into auditable reasoning workflows, providing a practical pathway for intelligent human-factor analysis in safety-critical industries.

---


### 3. [Graph-Based Detection of Disinformation Narrative Diffusion between Russian and Ukrainian Telegram Channels](https://arxiv.org/abs/2607.11894)

**<font color=#1a73e8>作者：</font>** Yuliia Vistak, Viktoriia Makovska, Vera Schmitt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting disinformation narratives on social media is challenging due to the scale of amplification, rapid evolution, and linguistic variability of online content. We propose a graph-based framework for identifying and analyzing disinformation narratives in Telegram ecosystems by combining weak supervision with propagation graph analysis. The approach aggregates semantically related claims into narrative-level clusters and models their diffusion across interconnected channels. This enables the detection of coordinated narrative amplification that is difficult to capture through post-level analysis alone. Our results demonstrate that integrating textual signals with network structure provides a scalable method for detecting disinformation narratives and offers insights into how they propagate within large-scale messaging environments.

---


### 4. [OmniPMNet: Bridging discrete and gridded PM10 forecasts via omni-query neural processes](https://arxiv.org/abs/2607.11896)

**<font color=#1a73e8>作者：</font>** Shuangshuang He, Shuo Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecasting particulate matter (PM10) requires both station-scale accuracy and continuous spatial fields, especially during severe dust storms. Chemical transport models (CTMs) provide gridded forecasts but retain local biases, whereas graph neural networks (GNNs) track monitoring sites well at short lead times but do not produce gridded outputs. Here we present OmniPM-Net, a Convolutional Conditional Neural Process (ConvCNP)-based fusion model that reconciles these two forecast types within a shared spatial representation. A terrain-aware Gaussian set convolution lifts irregular GNN station forecasts onto a regular grid, where a multi-scale Spatial Source Attention (SSA) module blends them with Copernicus Atmosphere Monitoring Service (CAMS) forecasts; a shared omni-query readout then decodes this representation into consistent PM10 predictions at either stations or grid cells over a 108 h horizon. Evaluated across 1,618 air-quality monitoring stations throughout China over the full year of 2024, OmniPM-Net matches the station-level accuracy of the stronger GNN baseline (mean absolute error 21.14 versus 22.00 ug/m3) and reduces the CAMS mean absolute error by 30%, while simultaneously delivering the gridded fields that the discrete GNN cannot. Its clearest gains are in the high-concentration tail, where the 90th-percentile MAE falls by 9% relative to the GNN and 25% relative to CAMS, and during dust episodes, where it improves categorical detection skill while tracking the evolving spatial trajectory.

---


### 5. [Semidirect Fourier Delta Attention: Phase-Controlled Delta Memory with Constructive Chunk-WY Kernels](https://arxiv.org/abs/2607.11897)

**<font color=#1a73e8>作者：</font>** Tiantian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention replaces softmax attention's growing KV cache with a fixed recurrent state, but this compression limits exact state tracking and long-context memory. We introduce \emph{Semidirect Fourier Delta Attention} (SFDA), a phase-controlled generalization of Kimi Delta Attention that replaces real diagonal decay with block-rotational Fourier control: \[ S_t=(I-\beta_t k_tk_t^*)\Lambda_tS_{t-1}+\beta_tk_tv_t^*, \qquad \Lambda_t=\diag(\alpha_t\odot e^{i\theta_t}). \] Our main result is a constructive chunk-WY factorization for products \(A_t=\Lambda_t-u_tr_t^*\), giving \[ A_t\cdots A_1=\Gamma_t-Y_tM_tW_t^* \] with rank growth bounded inside fixed chunks. This yields an exact affine chunk transfer, formal stability and complexity bounds, and a compact characterization of phase-plus-low-rank memory. We verify the algebra numerically and show in toy state-tracking experiments that SFDA learns cyclic memory where the phase-disabled KDA baseline remains near chance. Fused kernels and large-scale language-model comparisons are left to future work.

---


### 6. [TAKE: Trajectory-Aware Knowledge Estimation for Text Dataset Distillation](https://arxiv.org/abs/2607.11898)

**<font color=#1a73e8>作者：</font>** Tri-Nhan Vo, Dang Nguyen, Sunil Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale text corpora have become a quiet bottleneck in modern NLP, not just in storage, but in the accumulated cost of training, fine-tuning, and continual learning. We propose a text dataset distillation framework that reduces corpora to as little as 0.1% of their original size while preserving downstream task fidelity. We approach distillation through the lens of influence functions, which quantify each sample's contribution to the downstream objective, a natural and principled basis for selection. We introduce Trajectory-Aware Knowledge Estimation (TAKE), which convolves the knowledge-based influence along the training trajectory into a single per-sample knowledge score, capturing informative samples. These scores serve as sample weights within a discrete Optimal Transport objective, guiding prototype selection from a synthetically generated candidate pool. We evaluate TAKE on downstream accuracy across text classification and natural language inference tasks at extreme compression (0.1% or 20 samples/class), showing that data efficiency is achievable without sacrificing task fidelity. The approach is theoretically grounded, with broader implications for coreset construction and data-centric AI. We release our source code at this https URL.

---


### 7. [In-Context Reinforcement Learning under Non-Stationarity: A Survey](https://arxiv.org/abs/2607.11906)

**<font color=#1a73e8>作者：</font>** A Run, Ziluo Ding  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The development of decision-pretrained transformers, algorithm distillation, long-context meta-RL, and retrieval-augmented agents has renewed interest in in-context reinforcement learning (ICRL): the ability of a pretrained or fine-tuned decision model to infer latent task rules and improve future behavior from interaction context, without test-time parameter updates. This line of work asks when trial-and-error evidence, rewards, transitions, demonstrations, feedback, or retrieved experience can make learning-like computation happen inside the context window. However, existing surveys of ICRL mainly organize the field around pretraining objectives, architectures, context formats, evaluation protocols, and theoretical mechanisms, while the non-stationary setting remains comparatively underexamined. In changing environments, accumulated context is not merely more evidence about a fixed task: the reward specification, transition kernel, observation channel, action interface, constraint model, or demonstration and memory distribution can fall out of alignment with the current regime. Previously useful context can therefore become stale, misleading, or useful again when an old regime returns. We survey non-stationary ICRL as the problem of adapting through context while deployed policy parameters remain fixed: the policy must infer both the current decision rule and which parts of its accumulated evidence still support that rule. We define non-stationary ICRL, relate it to meta-RL, decision sequence modeling, retrieval-augmented RL, value- and model-aware ICRL, and reward-feedback agents, and organize the literature along three questions: what changes, how the change unfolds, and how observable the change is to the agent.

---


### 8. [Repairing Shape-Prior Shortcuts in Long-Range Single-Shot Fringe Projection Profilometry](https://arxiv.org/abs/2607.11928)

**<font color=#1a73e8>作者：</font>** Adam Haroon, Cody Fleming, Beiwen Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-shot fringe projection profilometry (FPP) networks that regress depth directly can exploit a shape-prior shortcut, recovering depth from object boundaries rather than from fringe phase. On a photorealistic synthetic benchmark (15,600 fringe images, 50 objects at 1.5-2.1 m standoff), the best such UNet baseline plateaus at 14.54 mm object mean absolute error (MAE), and neither more data nor more capacity removes the shortcut, because neither changes the hypothesis space the optimizer searches. We introduce PhiCalNet, which outputs a wrapped-phase representation $(\sin\phi, \cos\phi)$ and maps it to depth through a fixed differentiable calibration layer, removing the shape-prior solution architecturally rather than by a loss penalty. Because the single-shot mapping is non-injective without fringe order, PhiCalNet takes the fringe order as auxiliary input, an assumption a sensitivity analysis shows tolerates realistic decoding error; a physics-informed (PINN) baseline with the same physics as a soft penalty yields no gain, isolating the architectural choice as the operative factor. PhiCalNet reduces object MAE 3.3x to 4.46 mm, its residual confined to 0.103% of pixels at the $\pm\pi$ wrap discontinuity, and a three-frame extension reaches 1.16 mm. Two checks agree: interpretability makes phase the most decodable internal feature, and pixel-wise conformal uncertainty quantification, to our knowledge the first for FPP, localizes error at the same discontinuity, where rejecting the top 5% of pixels by snapshot disagreement cuts root-mean-square error by 64% versus 3.5% for the baseline.

---


### 9. [Qubit-Efficient Quantum Search for Hyperdimensional Decomposition via Logarithmic Encoding](https://arxiv.org/abs/2607.11936)

**<font color=#1a73e8>作者：</font>** Sanggeon Yun, Hyunwoo Oh, Ryozo Masukawa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperdimensional Computing (HDC) represents symbols using high-dimensional hypervectors of dimension $D$. In hypervector decomposition, the objective is to recover $F$ constituent hypervectors, each drawn from a codebook of size $N$, from a bound target hypervector. This requires searching over $N^F$ candidate tuples, making the task computationally prohibitive at scale. Recent quantum approach provides a quadratic search advantage, but typically rely on qubit-inefficient $O(D)$-qubit hypervector representations. We propose a qubit-efficient quantum framework for HDC decomposition that reduces the representation cost to $O(\log D)$. The framework introduces logarithmic hypervector and binding encodings, together with a reversible hypervector lookup operator for circuit-level manipulation of dense hypervectors. Combined with a modified Dürr-Høyer search procedure, the method preserves $O(\sqrt{N^F})$ search complexity while substantially reducing qubit usage. Experimental results validate correct similarity computation, accurate decomposition in executable regimes, and significantly improved qubit scaling over baselines based on explicit $D$-qubit hypervector encodings, achieving up to $2{,}000\times$ fewer qubits.

---


### 10. [Mirror Horizon: Viable Path Entropy as a Measure of Bounded Reflection](https://arxiv.org/abs/2607.11937)

**<font color=#1a73e8>作者：</font>** Tiantian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mirror Theory proposes that an intelligent system should be studied not only by what it represents, but by what coherent continuations it can sustain under repeated reflection. We make this claim operational through \emph{viable path entropy} (VPE), a finite-budget measure of verified continuation capacity. Given a mirror state, a rollout protocol, a verifier, and a mode map, VPE decomposes bounded capability into two parts: the probability of reaching a viable continuation and the diversity of verified continuation modes reached among successful rollouts. This paper restores the full theoretical scaffold behind the measure: intuition as local underdetermining constraint, taste as invariant-selecting pressure, reflection as taste-guided resolution of underdetermination, and geometry as the learned structure that makes future reflection stable. We then instantiate the theory in language-model reasoning experiments on GSM8K. Across Qwen2.5-Instruct models, 32 sampled rollouts per problem, and two reflection horizons, increasing the token budget from 96 to 160 substantially expands verified reachability, reduces zero-reachability, increases verified-mode entropy, and improves smoothed VPE. At 160 tokens, Qwen2.5-1.5B realizes the strongest mirror horizon among the tested models, even though Qwen2.5-3B has more parameters. This shows that mirror horizon is not parameter count, but accessible verified continuation capacity under a bounded reflection protocol. The result supports Mirror Theory as a measure-level account: capability is the structure of viable continuations made reachable, not merely one-shot accuracy or pass@k.

---


### 11. [Mathematics of Data Science](https://arxiv.org/abs/2607.11938)

**<font color=#1a73e8>作者：</font>** Afonso S. Bandeira, Amit Singer, Thomas Strohmer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This book is about the mathematical foundations of data science.
1. Introduction
2. Curses, Blessings, and Surprises in High Dimensions
3. Singular Value Decomposition and Principal Component Analysis
4. Linear Regression and Regularization
5. Graphs, Networks, and Clustering
6. Nonlinear Dimension Reduction and Diffusion Maps
7. Linear Dimension Reduction via Random Projections
8. Optimization for Data Science
9. Classification
10. A Mathematical Introduction  to Deep Learning
11. Large Sample Limit of Graph Laplacians
12. Community
13. Concentration of Measure and Gaussian Analysis
14. Matrix Concentration Inequalities
15. Compressive Sensing and Sparsity
16. Low-Rank Matrix Recovery

---


### 12. [CARE-LoRA: Compressed Activation REconstruction for Memory-Efficient LoRA](https://arxiv.org/abs/2607.11940)

**<font color=#1a73e8>作者：</font>** Gengyu Zhang, Haiyin Ran, Zhengbao He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As the scale of large pre-trained models continues to grow, fine-tuning them under limited memory budgets has become increasingly challenging. Low-Rank Adaptation (LoRA), currently one of the most widely adopted parameter-efficient fine-tuning (PEFT) methods, mitigates this challenge by optimizing only low-rank adaptation matrices, thereby greatly reducing the number of trainable parameters. With the parameter overhead substantially reduced, the activations retained for backpropagation have emerged as the primary remaining memory bottleneck during LoRA fine-tuning. To address this, we propose CARE-LoRA, a data-aware Compressed Activation REconstruction framework. By exploiting the inherent projection structure of LoRA, CARE-LoRA replaces the full input activation with the low-rank compressed activation naturally produced by the LoRA branch. It further computes a lightweight reconstruction matrix during the forward pass with negligible additional computation cost, which is used during backpropagation to reconstruct the gradient signal, thereby keeping LoRA matrices fully trainable. Extensive experiments across diverse models and downstream tasks demonstrate that, while substantially reducing the overall memory footprint, CARE-LoRA achieves competitive or even superior performance compared with standard LoRA and representative LoRA variants. Our code is publicly available at this https URL .

---


### 13. [GenDiff: A Dose and Anatomy Aware Diffusion Model with Structural Prior Refinement for Low-Dose CT Reconstruction and Generalization](https://arxiv.org/abs/2607.11941)

**<font color=#1a73e8>作者：</font>** Md Imam Ahasan, Guangchao Yang, A F M Abdun Noor 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computed tomography (CT) is a critical imaging modality for clinical diagnosis, but reducing radiation dose inevitably introduces severe noise and structured artifacts that degrade image quality. Existing deep learning-based low-dose CT (LDCT) reconstruction methods are typically optimized for fixed dose levels or specific anatomical regions, limiting their robustness and generalization in realistic clinical settings. We propose GenDiff, a generalizable diffusion-based framework for LDCT reconstruction that jointly models continuous radiation dose and anatomical information within a unified reconstruction network. The proposed framework integrates a Dose-Anatomy Encoder to learn acquisition-aware embeddings, a dose- and anatomy-conditioned cold diffusion backbone for iterative refinement, a physics-consistency update to enforce fidelity to the CT forward model, and a Structural Prior Refinement Module (SPRM) that preserves anatomical structures while suppressing dose-dependent artifacts. Extensive experiments on multi-anatomy clinical datasets, including unseen ultra-low-dose conditions as well as out-of-distribution phantom and animal datasets, demonstrate that GenDiff consistently outperforms state-of-the-art convolutional neural network and diffusion-based reconstruction methods. The proposed approach achieves superior reconstruction quality while maintaining strong robustness across different dose levels, anatomical regions, and acquisition domains, making it a promising solution for practical low-dose CT imaging.

---


### 14. [How Query Visibility Changes KV-Cache Compression Rankings: A Matched-Budget Audit](https://arxiv.org/abs/2607.11942)

**<font color=#1a73e8>作者：</font>** Daming Luo, Christy Liang, Junyu Xuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> KV-cache compression methods are predominantly evaluated with the query appended to the context before compression -- a query-aware protocol. Yet the economic case for a compressed KV cache is reuse: compress a document once, answer many future questions against it. In that deployment, compression must happen query-agnostic -- before any question is seen. We present a matched-budget audit of six published compression methods against three trivial baselines on three open 7-9B models (144,300 paired evaluations on RULER-8192; 40,800 on LongBench; 50,000-resample paired bootstrap throughout). Everything is held fixed -- model, compression ratio, instances, decoding -- except the scoring rule. Three findings. (1) Query visibility changes the rankings: under the agnostic protocol, of the five audited methods that share a common attention backend, only KeyDiff beats a best-of-3 trivial baseline consistently (31 of 36 cells), and the most widely deployed method, SnapKV, loses to "keep the start and the recent window" on average (-0.066). (2) The per-method drop between the two protocols is ordered consistently with how visible the question is to each method's scoring signal, legible in its source code: from Delta=+0.198 for SnapKV (the question sits inside its 64-token observation window) down to Delta=+0.011 for KeyDiff (its score contains no query term at all).

---


### 15. [BattVAE-GP: Generative Modeling of Long-Horizon Battery Degradation with Uncertainty Quantification](https://arxiv.org/abs/2607.11943)

**<font color=#1a73e8>作者：</font>** Raghvender Raghvender, Mahdi Abid, Ferran Brosa Planella 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon physics-based simulations of battery degradation provide mechanistic insight but remain computationally expensive, limiting their use for dense exploration of operating conditions over extended cycle life. Here, we propose a hybrid physics-probabilistic learning framework for surrogate modeling of lithium-ion battery degradation trajectories at unseen charging rates. Cycle-resolved degradation data generated with a DFN/P2D electrochemical model in PyBaMM are first transformed into capacity-aligned voltage and derivative features and encoded using a Variational Autoencoder (VAE). The resulting two-dimensional latent space organizes degradation trajectories according to both cycle progression and charging protocol. A sparse multitask Gaussian process (GP) is then trained in this latent space using cycle number and C-rate as input variables, providing continuous interpolation of latent degradation dynamics together with posterior uncertainty estimates. Under protocol-level holdout evaluation, the latent-space GP accurately recovers unseen C-rate trajectories and exhibits uncertainty behavior consistent with the support of the training data. When queried at unseen interior C-rates, the model generates latent trajectories that remain coherently positioned between neighboring simulated protocols. Decoding the GP-predicted latent states through the frozen VAE decoder yields smooth voltage-capacity evolution, while Monte Carlo propagation of the GP latent posterior through an auxiliary latent to State of Health (SOH) predictor provides uncertainty-aware SOH estimates. The proposed BattVAE-GP framework therefore offers a computationally efficient and uncertainty-aware surrogate for long-horizon degradation modeling, providing a structured basis for extending battery health prediction toward richer operating conditions and future simulation-experiment fusion.

---


### 16. [MAGE: Understanding Stability-Performance Trade-offs in Multi-component Prompt Optimization](https://arxiv.org/abs/2607.11944)

**<font color=#1a73e8>作者：</font>** Prateek Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do different components of iterative prompt optimization interact, and what happens when they are combined? We investigate this through MAGE (Memory-Augmented Goal-directed Prompt Evolution), a controlled analysis framework for studying component interaction in prompt optimization. MAGE is not proposed as a superior optimizer in absolute terms; it integrates episodic memory, multi-objective Pareto selection, and adaptive evaluation as a platform for controlled ablation. Our experiments uncover a previously unreported phenomenon, the Prompt Optimization Coupling Effect (POCE): when multiple stochastic optimization signals operate within a closed reflective loop, they interact in ways that simultaneously improve performance and amplify variance, behavior that cannot be predicted by analyzing components in isolation. Three main findings emerge. First, failure-grounded reflection is essential: methods relying only on scores (OPRO) or abstract critique (Self-Refine) fail to improve prompts. Second, MAGE achieves 46.4% versus GEPA's 34.0% on GSM8K-Hard (+12.4%, P(MAGE>GEPA)=0.998, 5 seeds on gpt-4o-mini), with comparable variance (7.3% vs. 7.0%). Third, increasing candidate diversity reveals the clearest POCE signal: expanding the candidate pool from n=3 to n=5 improves mean accuracy by +21.6% while increasing variance by 3.7x. We further validate on Llama 3.1 8B and show POCE is headroom-dependent: when the base model already achieves high accuracy, variance amplification disappears. Finally, in low-data regimes (Ntrain=30), well-designed fixed prompts outperform all reflective optimizers, indicating that scaffold choice dominates optimizer choice. Our results suggest prompt optimization systems behave as coupled stochastic processes and should be evaluated in terms of both performance and stability, not just peak accuracy.

---


### 17. [Hybrid Continual Learning for Low-Resource Australian Aboriginal Language Identification](https://arxiv.org/abs/2607.11946)

**<font color=#1a73e8>作者：</font>** Pravina Mylvaganam, Ting Dang, Eliathamby Ambikairajah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language identification is an important step toward integrating endangered Australian Aboriginal languages (AALs) into speech technologies supporting language revitalisation and digital inclusion. However, extreme data scarcity limits model performance. Transfer learning from high-resource languages shows promise but often suffers from catastrophic forgetting when adapting to new languages. Continual learning (CL) can mitigate this issue, though it remains challenging with very limited data. To address this, we propose two hybrid continual learning methods: Replay Augmented Elastic Weight Consolidation and Constraint Guided Knowledge Distillation to adapt pretrained speech models for AAL identification while preserving previously learned knowledge. Experiments on Warlpiri, Dalabon and Dharawal show that the proposed methods outperform fine-tuning and existing CL baselines, improving adaptation to multiple AALs while maintaining performance on previously learnt high-resource languages.

---


### 18. [Generalized Distribution-Free Semi-Supervised Learning with Risk Rewrite](https://arxiv.org/abs/2607.11947)

**<font color=#1a73e8>作者：</font>** Yushi Hirose, Hiroo Irobe, Takafumi Kanamori  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Typical semi-supervised learning (SSL) methods rely on distributional assumptions, and their performance degrades when these are violated. While PNU learning, a risk rewriting method, offers a distribution-free alternative, it is restricted to binary classification and its variance optimality remains unclear. In this paper, we propose a generalized framework that constructs unbiased risk estimators using linear combinations of component risks, subsuming PNU learning and extending to multiclass classification. We derive the minimum achievable variance, demonstrating our estimator can attain lower variance than PNU in asymmetric loss scenarios. Furthermore, we establish a generalization bound directly linking this variance reduction to improved learning performance. Based on these theoretical insights, we introduce two practical SSL methods that empirically match or outperform existing approaches on binary and multiclass benchmarks.

---


### 19. [Scale-Aware Attention for Scarce Neural Data: An RG-Flow Transformer on Sleep-EDF EEG](https://arxiv.org/abs/2607.11950)

**<font color=#1a73e8>作者：</font>** Dibakar Sigdel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Brain field potentials are scale-free: their power spectra follow a $1/f^{\beta}$ law whose aperiodic exponent $\beta$ tracks cortical state, and sleep depth in particular is a shift in $\beta$. We ask whether a transformer endowed with an explicit renormalization-group (RG) inductive bias -- the RG-Flow Transformer, which couples ordinary self-attention to a scale-aware stream with a learnable anomalous dimension $\gamma$, block-spin coarse-graining, and an entropy-gated synchronization bridge -- has an advantage over a parameter-matched vanilla transformer on \emph{real, scarce} EEG. Using the PhysioNet Sleep-EDF corpus with a strict leakage-free by-subject hold-out, we (i) benchmark RG-Flow against a param-matched vanilla transformer and a hierarchy-only ablation on 5-class AASM sleep staging, (ii) sweep the per-subject data budget to look for the inductive-bias crossover predicted when data are scarce, and (iii) test whether RG-Flow's learned $\gamma$ tracks the measured spectral exponent $\beta$ out-of-sample -- a quantity the vanilla model does not possess. Across $5$ subjects and $5$ seeds under leave-one-subject-out cross-validation, RG-Flow and the vanilla transformer are statistically indistinguishable on 5-class staging (77.3\% vs 77.0\% accuracy; paired $p=0.294$), and the predicted scarce-data crossover does not appear: vanilla is numerically ahead at every data-limited budget. What does separate the models is interpretability -- RG-Flow recovers the continuous spectral exponent out-of-sample ($\beta$-recovery $R^2 = 0.416$), a capability the vanilla architecture has no analogue for.

---


### 20. [GRID: Grammar-Railed Decoding for Enterprise SQL Generation](https://arxiv.org/abs/2607.11951)

**<font color=#1a73e8>作者：</font>** Mohsen Arjmandi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can write SQL, but enterprise deployment demands more than plausible text: outputs must be syntactically valid, must respect per-role and per-schema policy, must carry provable (not best-effort) guarantees, must not slow down as generations grow, and must leave a compliance-grade record of every decision. We present GRID (Grammar-Railed Decoding), a grammar-constrained decoding engine that keys exact next-token masks on parser configurations (lexer scan state x LALR(1) stack) rather than on token sequences, and uses the incrementally advanced LALR(1) parser itself as a viable-prefix oracle. LLM tokens are bridged to grammar terminals by a byte-level trie walk with a context-independent/context-dependent split that makes cache-key soundness hold by construction. Role-based access control is compiled into the language: role projections subset the grammar's productions and schema lexicons restrict identifier terminals, so forbidden verbs and identifiers are unreachable at mask level. Four guarantees (soundness, completeness, termination, and near-constant per-token cost) are stated with explicit preconditions and each paired with a test or benchmark. Rust kernels bring the per-token mask to a 3.6-6.7 us median, ahead of llguidance at p50 and p90 on two tokenizers with zero false rejects; per-token guard cost is position-flat at n=16,000. On Spider, constrained decoding is worth +13 execution-accuracy points at 0.5B, and one checker-guided repair pass over the provably mask-unenforceable residue (column-level policy) lifts a 7B model to 94.5% executable. A hash-chained per-token audit trail replays bit-identically with 100% tamper detection. We state plainly what the mask cannot do (distribution faithfulness, column-level RBAC, non-LALR(1) languages) and where measured cost remains.

---


### 21. [When Does Reward Teach State? A Hidden-Automaton Instrument and the Group-Language Boundary](https://arxiv.org/abs/2607.11953)

**<font color=#1a73e8>作者：</font>** Jim Allchin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Does a reinforcement-learning agent that earns high reward represent its task's latent state, or only a reward-correlated shortcut? The question is usually unanswerable: the "true state" is undefined. We make it exactly answerable with a white-box instrument: express the task as a hidden deterministic finite automaton (DFA), let the agent observe a symbol stream and intermittently choose the next symbol under partial control, and grant one sparse terminal reward for acceptance. Knowing the automaton gives two things for free: the optimal return (so reward becomes an interpretable normalized score) and the exact latent state at every step (so we can probe the agent's representation without ever showing it). Reward success and latent-state learning thus become separately measured quantities whose coupling is governed by three controllable axes. Optimizer strength: under weak on-policy RL the agent earns reward with the state probe at chance for every architecture, tempting the conclusion that sparse RL cannot install latent state; a pre-registered control overturns it -- PPO+GAE recovers the state, but only partially and with high seed variance. Task structure: permutation (group-language) structure is a warning sign computable from the transition function before any training, and held out on 153 capacity-controlled fresh automata it flags perception gaps at precision 0.86 (89 of 103), in one direction only. Observation informativeness: a label-free auxiliary is vacuous when observations carry no state and recovers it in proportion to how much they reveal. The payoff is a distinction reward-only evaluation cannot make: a perception gap (latent state not linearly recoverable, though representable) versus a planning gap (state recoverable but unused). High reward is thus not evidence of task understanding; whether an agent recovers latent state is predictable in advance.

---


### 22. [Graph-Constrained Policy Learning for Extreme Clinical Code Prediction](https://arxiv.org/abs/2607.11954)

**<font color=#1a73e8>作者：</font>** Amritpal Singh, Sebastian Torres, Khawar Shakeel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical code prediction maps unstructured discharge summaries to ICD-10-CM leaf codes in a large, sparse, and deeply hierarchical label space. Most systems treat the task as flat multi-label classification, scoring codes independently and providing limited training signal for rare labels. We propose a graph-constrained traversal policy that formulates ICD prediction as a finite-horizon decision process over a pruned code hierarchy. A single language model descends the graph level by level, selecting valid child nodes until billable leaf codes are reached. This converts extreme multi-label prediction into sparse, hierarchy-aware subset decisions while guaranteeing structurally valid outputs.
On MIMIC-IV discharge summaries, our best supervised policy, SFT-1+, achieves 0.709 micro-F1 on a curated 50-code subset and 0.527 micro-F1 on the full 15,761-code space, outperforming flat baselines including CAML, LAAT, and PLM-ICD. In the full setting, SFT-1+ improves over the strongest flat baseline by 0.044 micro-F1 and 0.157 macro-F1, suggesting that graph-constrained decomposition mitigates the rare-code bottleneck. A controlled factorial study evaluates architecture, training algorithm, and data budget. Across both scales, one shared policy matches a three-specialist cascade while avoiding its context-window overflow on 28-32% of full-space test notes. Increasing supervised trajectory data is the only intervention that consistently improves performance, while GRPO reinforcement learning provides no benefit over supervised continuation with matched data. These results show that simple graph-constrained policy learning can outperform more complex flat, cascaded, and reinforcement-learning alternatives for extreme clinical code prediction.

---


### 23. [Exact and Certified Data Shapley for Weighted k-Nearest-Neighbor Regression and Soft-Label Prediction](https://arxiv.org/abs/2607.11956)

**<font color=#1a73e8>作者：</font>** Zongye Lyu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data Shapley is the standard principled answer to which training points are worth what, and its k-nearest-neighbor (KNN) specialization is the version deployed in practice: the exact estimator shipped by toolkits such as pyDVL and OpenDataVal. Exact algorithms are known for unweighted KNN and for weighted KNN classification, but weighted KNN regression and soft-label prediction have resisted: the only exact method is an O(N^K) brute force, exponential in neighborhood size K. The obstruction: the weighted regression prediction is a ratio of two coalition-dependent sums, whose normalization denominator breaks the additive, threshold, and duplication structures the prior polynomial algorithms rely on. We close this gap. We give (i) the first pseudo-polynomial-time exact algorithm (polynomial in N and K at fixed lattice precision) for weighted KNN-regression Data Shapley, a counting dynamic program over the joint integer state (sum of w, sum of w*y), verified against exhaustive enumeration with zero mismatch on 12,716 adversarial instances; (ii) a certified FPTAS for continuous weights and targets, with a machine-checkable per-value error certificate never violated across 86,400 checks; (iii) a complexity landscape, including an unconditional Omega(D_w) output-size lower bound and access-model hardness results; and (iv) a weighted soft-label multi-class extension. We release an open-source, CPU-only library and the first exact weighted-regression Data Shapley ground truth. On downstream mislabel detection our exact values are statistically equivalent to Monte-Carlo Data Shapley (dataset-level TOST, n=8, p<10^-4), the pre-registered outcome; the value of exactness is instead determinism, a certified error bound, and an exact reference for auditing estimators: Monte-Carlo did not reproduce the exact top-10% ranking at any budget tested, up to 3,000 permutations (~1.28e6 utility evaluations).

---


### 24. [Anomalous Frame Detection Using VLM-Based Description Comparison for Extracting Expert-Specific Actions and Contextual Decision-Making Scenes with Intra-Video Self-Similarity](https://arxiv.org/abs/2607.11957)

**<font color=#1a73e8>作者：</font>** Ryo Sakai, Kaname Yokoyama  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Maintenance of critical infrastructures, such as railways and power plants, is essential for ensuring operational safety and reliability. However, the declining number of skilled maintenance workers highlights the need to transfer expert know-how to less experienced workers. Previous studies have attempted to extract candidates of expert knowledge by comparing videos of manual-based work with those of expert workers, mainly focusing on differences in observable actions. However, expert know-how is often embedded not only in actions but also in contextual decision-making during task execution. This paper proposes a method that detects anomalous frames between two task videos to automatically extract candidate scenes containing expert-specific actions and contextual decision-making scenes. The method generates frame-wise visual descriptions using a vision-language model (VLM). Expert-specific actions are extracted based on frame similarities computed from description comparisons between two videos, while contextual decision-making scenes are extracted using segment similarities derived from intra-video self-similarity of the descriptions. In simulated distribution board maintenance experiments involving 27 task scenarios, the proposed method achieved extraction rates of 65% for action candidates and 61% for decision-scene candidates, improving over conventional methods that achieved 59% and 33%, respectively. These results demonstrate the effectiveness of the proposed approach in discovering candidate scenes containing expert know-how.

---


### 25. [Constructed Reality, Contested Priors: Decoupling and the Architecture of Cognitive Relapse Under the Free Energy Principle](https://arxiv.org/abs/2607.11958)

**<font color=#1a73e8>作者：</font>** MD Ibrahim Hossain Ridoy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Under the free energy principle, a predictive system does not observe reality directly; it maintains a generative model of the world and experiences that model's best current hypothesis. Can a synthetic environment be made consistent enough that a predictive system's own inference machinery adopts it as this default hypothesis, permanently displacing the environment that first shaped it? We call this state ontological inversion. Because inducing and monitoring such a transition in a nervous system is neither ethical nor technically feasible, we study the underlying computational problem through a controlled proxy: a convolutional variational autoencoder paired with a recurrent latent predictor, whose evidence lower bound objective is mathematically identical, up to sign, to variational free energy itself. The network is trained first on a baseline visual domain, then on a mixed stream in which a swept rehearsal ratio r controls how much baseline content persists during transition to a target domain. Representational capacity, what the latent space can discriminate, is tracked separately from default behavior, what the system generates when left unconstrained. Across a full sweep of 90 runs, the two diverge sharply: representational accuracy stays near ceiling, 0.97 to 0.998, regardless of r, while default behavior spans nearly the system's entire range depending on r alone, a decoupling of learning from acceptance. More strikingly, at intermediate r the system's default output rises toward the target domain, then partially reverts toward the baseline while training continues unchanged, a structural failure we term cognitive relapse. Resistance to reality-adoption is not reducible to learning speed; it is a structural property with its own distinct failure modes, established here as a computational existence proof and nothing further.

---


### 26. [Calibration-First Reward-Component Auditing for Reinforcement Learning Control in Smart Greenhouses](https://arxiv.org/abs/2607.11959)

**<font color=#1a73e8>作者：</font>** Yuhui Bie, Guowei Xu, Yaojun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Greenhouse reinforcement learning can test climate-control ideas at a speed and scale that is difficult to achieve with crop experiments alone. For smart-greenhouse control, however, a single simulator return is not enough: a grower or control engineer also needs to know when the policy heats, enriches CO2, vents, manages humidity, deploys screens, or uses this http URL propose a reproducible calibration-first reward audit framework that keeps named greenhouse-control reward components comparable across simulator training, facility-adapted rollouts, logged Autonomous Greenhouse Challenge records, and actuator-rule distillation. In GreenLight-Gym, the framework decomposes the scalar reward into conditional temperature, CO2, humidity and vapor-pressure-deficit, screen, and actuation-proxy terms; adapts GreenLight to the second Autonomous Greenhouse Challenge logged climate traces; and scores the same components on logged greenhouse data.

---


### 27. [Contrastive Joint-Embedding Prediction for Representation Learning in Structural MRI](https://arxiv.org/abs/2607.11962)

**<font color=#1a73e8>作者：</font>** Fabian Mager, Lars Kai Hansen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning offers a compelling approach for medical imaging, where labeled data are scarce and acquisition costs are high. We present COJEPA, a self-supervised framework for volumetric brain MRI that combines a joint-embedding predictive architecture (JEPA) with a contrastive loss (CO), targeting two complementary properties: local predictivity and global discriminability. The model is trained without labels on T1-weighted structural MRI from two cohorts (HCP-YA and AABC, $N{=}2286$, ages 22 to 90), extending I-JEPA to 3D with foreground-aware block masking, a hierarchical convolutional patch embedding, and world-space sinusoidal positional encodings. We evaluate all three objectives across zero-shot twin retrieval, brain tumor segmentation (BraTS 2024), and age regression (OpenBHB). COJEPA achieves the best monozygotic twin recall at rank@1 (0.84), the best finetuning age MAE (2.55 years on OpenBHB 3.0T), and matches CO on BraTS whole-tumor Dice, demonstrating that the combined objective yields representations that are simultaneously discriminative and locally structured.

---


### 28. [Evaluating Reliability in Machine Learning Models for Early Chronic Kidney Disease Prediction: A Systematic Review of Data Leakage and Predictor Stability](https://arxiv.org/abs/2607.11963)

**<font color=#1a73e8>作者：</font>** Mashrul Hossain, Nafesa Kibria, Fahim Shahriar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The early detection of Chronic Kidney Disease using machine learning has attracted significant interest in healthcare-related computer science. Despite rapid advancements in this field, many reported studies remain inconsistent and potentially misleading. A significant drawback is the lack of organized evaluation regarding methodological concerns. Key issues include data leakage, limited access to temporal patient records and inconsistency in reported clinical indicators. This research offers a systematic literature review of existing CKD prediction studies using interpretable machine learning techniques, where nineteen relevant studies were selected via systematic searches across major academic databases. To assess methodological reliability, this study introduces a structured taxonomy of information leakage and a quantitative leakage scoring framework to systematically evaluate reliability across CKD prediction studies. The analysis reveals a strong relationship between leakage and inflated performance. Here, High leakage-studies report an average accuracy of 95.48%, compared to 80.2% for leakage-free studies, reflecting an increase of approximately 15.28%. Furthermore, a cross-study feature stability analysis shows that only a small subset of predictors is consistently reproducible, with over 80% lacking reliability. Overall, the findings suggest that many reported performance improvements stem from methodological limitations rather than true predictive capability.

---


### 29. [LIDAR-AD: A Decoder-Free Latent-Interaction Dreamer with Action-Residual Chains for Autonomous Driving](https://arxiv.org/abs/2607.11964)

**<font color=#1a73e8>作者：</font>** Yongzhi Liu, Yang Xiao, Zhong Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autonomous driving requires long-horizon closedloop decision making in dynamic traffic environments. Latent world models offer an effective framework for this problem by enabling imagination-based decision making in compact latent spaces. However, multi-source observations contain controlirrelevant redundancy, whereas reliable driving decisions rely on risk-relevant relations, future dynamics, and continuous action adjustments. This mismatch makes observation reconstruction and absolute action modeling suboptimal for learning decisionrelevant latent dynamics. We propose LIDAR-AD, a decoderfree Latent-Interaction Dreamer with Action-Residual Chains for autonomous driving. LIDAR-AD replaces observation reconstruction with redundancy-reduced latent alignment, encouraging compact representations of risk-relevant relations in multi-source driving inputs. It further models vehicle control as residual action updates and uses residual-action sequence contrastive learning to align multi-step residual-driven rollouts with future latent states. A deterministic analysis shows that the latent-tanh residual parameterization preserves interior action reachability while representing smooth long-horizon control as compact local updates. Together, these designs improve risk-aware state abstraction, continuous-control modeling, and long-horizon dynamics prediction. Extensive experiments across diverse simulated driving scenarios demonstrate that LIDAR-AD consistently outperforms world-model baselines, achieving the highest reward and the best success rate among learning-based methods. Evaluations on nuPlan-derived log-reconstructed scenarios further demonstrate the transferability of LIDAR-AD under real-world traffic layouts.

---


### 30. [Beyond Coordinate Gauge: An Audited Protocol for Detecting Donor-Specific Functional Fingerprints after Neural Collapse](https://arxiv.org/abs/2607.11967)

**<font color=#1a73e8>作者：</font>** Truong Xuan Khanh, Phan Thanh Duc  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Independently trained neural networks have no shared neuron-index reference frame, so comparing them requires accounting for coordinate freedom. Neural Collapse sharpens this problem: networks converge toward a shared, low-dimensional geometry, raising the question of whether trajectory-specific functional variation remains distinguishable after convergence. We distinguish three claims - detectability, transplantability, and causal persistence - and address the first. Using five independently trained networks reconstructing Neural Collapse on MNIST, we apply a verified affine-correct alignment mapping donor heads into recipient coordinates. Donor-specific functional fingerprints remain distinguishable after recipient-level baseline correction: all 20 ordered donor-recipient pairs are correctly identified, with an exact permutation p=0.0083, robust to a leakage audit. These findings establish detectability under the test used here, but not transplantability or causal persistence. The study shows how alignment, ambiguity diagnostics, and leakage control combine to test cross-network variation in a controlled setting; whether this generalizes beyond it is open.

---


### 31. [Learning to Discretize: Diffusion-Based Adaptive Mesh with Spectral Guidance](https://arxiv.org/abs/2607.11974)

**<font color=#1a73e8>作者：</font>** Zixuan Shen, Bingchuan Wang, Zhi Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most neural partial differential equation (PDE) surrogates learn how fields evolve after a grid has already been chosen. However, before any operator is applied, the grid has already determined how modeling capacity is allocated across space, resolution, and spectral bandwidth. We argue that this hidden design choice should itself be learnable, leading to a question different from standard operator learning: can a surrogate learn where resolution should exist before predicting field evolution? We formulate adaptive discretization as a physics-constrained conditional generation problem over valid mesh displacements. The success of diffusion models in PDE field prediction suggests their potential for learning adaptive discretizations under similar structured constraints. This leads to a two-stage diffusion framework: Stage 1 learns an r-adaptive displacement mesh conditioned on the observed dynamics, while Stage 2 predicts the solution evolution from the mesh-informed representation. The mesh generator is regularized by physics-aware proxy channels, geometric validity constraints, and local spectral concentration so that adaptation remains physically interpretable and numerically legal. Across five PDE regimes, the results show that diffusion-based learned discretization is competitive with adaptive-mesh and reduced-order baselines, with particularly strong gains in regimes where fixed or handcrafted allocation is insufficient. The main conclusion is not that there exists a universal optimal mesh rule, but that discretization should be learned in a regime-dependent manner: different spatial and spectral structures favor different allocation behaviors. This reframes adaptive meshing for neural PDE solvers from a solver-specific heuristic into a generative representation-learning problem.

---


### 32. [Signal-Guided Optimization for Machine Unlearning](https://arxiv.org/abs/2607.11975)

**<font color=#1a73e8>作者：</font>** Xujia Li, Dan Li, Jian Lou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Current machine unlearning methods predominantly rely on global, coarse-grained intervention strategies. They lack precise pilot signals to guide the unlearning process and fail to provide differentiable guidance across different unlearning tasks. Due to the varying memorization strengths of samples during original training, such a uniform strategy leads to two problems: some samples are over-unlearned, which harms model utility; while others are under-unlearned, leaving residual information that can be exploited by privacy attacks. In this paper, we propose GSUO, a guidance-signal-aware unlearning optimization framework that designs task-specific fine-grained guidance signals to steer the unlearning process and is applicable to both random-subset and class-wise forgetting tasks. Extensive experiments demonstrate that GSUO outperforms 14 baselines in terms of both unlearning effectiveness and generalization, while achieving high efficiency and significant speedups, validating its effectiveness for reliable machine unlearning.

---


### 33. [LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention](https://arxiv.org/abs/2607.11976)

**<font color=#1a73e8>作者：</font>** Ziqi Yin, Jianyang Gao, Peiqi Yin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Indexer-TopK, the operation to compute the scores and select the top-k candidates, is widely used by sparse attention kernels in large language models and vector retrieval in recommendation systems and vector databases. However, existing GPU-based Indexer-TopK kernels like DeepSeek Sparse Attention (DSA) remain inefficient due to excessive global memory traffic, costly synchronization, and prohibitive memory overhead. In this work, we exploit the curse of dimensionality in high-dimensional spaces, where distances between high-dimensional vectors tend to concentrate within a narrow range, to design LITETOPK, a novel and efficient fused Indexer-TopK kernel. LITETOPK first samples a small subset of data to estimate query-data score ranges, then uses these estimates to partition candidate results into bins online. This organization allows the LITETOPK kernel to maintain a tight approximate threshold, write back only promising candidates, reduce unnecessary I/O, substantially lower memory overhead, and still preserve exact Top-k correctness. Experimental results show that LITETOPK accelerates the prefill stage of GLM 5.2 by 1.2x in real-world deployment scenarios while incurring lower memory overhead.

---


### 34. [Optimization Is Not All You Need](https://arxiv.org/abs/2607.11977)

**<font color=#1a73e8>作者：</font>** Minh Hua, Rita Raley  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In 2019, OpenAI released two million GPT-2 outputs-ungrammatical, half broken-to aid the detection of machine-generated text. The alignment that produced their more fluent successors is usually regarded as an engineering achievement; we read it instead as the newest expression of optimization culture: the conviction, older than the technology, that measurable improvement along predefined axes exhausts the question of value. Tracing that conviction through the stack-pretraining, decoding, preference tuning, benchmarking, interface-and back through its genealogy in the audit society, we arrive at the limit: an optimization procedure can measure how improbable a piece of generated text is; it cannot tell whether that unlikelihood is error or invention. A procedure that cannot make that distinction has nonetheless, within half a decade, assumed the authority to set the protocols of legitimate language. Held for centuries by academies and schoolrooms, grammars and examiners, this authority has been given over to loss functions, reward models, benchmarks, and system prompts: an apparatus that executes the office of judgment with no capacity for judging.

---


### 35. [Gene Expression-Informed Jointly Controlled Generative Modeling for Precision Molecular Design](https://arxiv.org/abs/2607.11978)

**<font color=#1a73e8>作者：</font>** Hang Yuan, Chen Li, Wenjun Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Precision molecular design aims to discover personalized drug candidates through joint control of multiple conditions, such as biological relevance and molecular design strategies. Biological relevance reflects cellular functional states under disease or perturbation conditions, while molecular design strategies provide complementary guidance in terms of structural intentions and property optimization. In this study, we propose JoPMol, a jointly controlled precision molecular generative model that integrates biological states encoded by gene expression profiles with molecular structure information expressed in text, and chemical properties quantified by numerical values within a unified modeling framework. This formulation enables coordinated generation and optimization of candidate molecules under joint condition control. Experimental results show that JoPMol outperforms state-of-the-art methods across multiple evaluation metrics. Moreover, JoPMol demonstrates strong generalization ability in both transfer tasks and biologically grounded simulation scenarios, validating its effectiveness for precision molecular design. The source code is publicly available at this https URL.

---


### 36. [LP Mining with LP2Graph: A Use Case for Railway Rescheduling](https://arxiv.org/abs/2607.11980)

**<font color=#1a73e8>作者：</font>** Jörn Maurischat, Nikola Bešinović, Michael Färber  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Like many optimization-driven domains, railway rescheduling relies on Mixed-Integer Linear Programming (MILP), yet the field's modeling knowledge is scattered across hundreds of papers in incompatible notations, and narrative surveys organize it subjectively: they classify models by vocabulary rather than by structure, and reproduce neither. We present LP Mining with LP2Graph, a method that mines the structure of published LP and MILP formulations into a reproducible dataset and an induced taxonomy. Its core, LP2Graph, represents each formulation admitted by its canonical grammar as a typed variable--equation graph derived from a single canonical model; once a source is extracted into that model, everything downstream is deterministic. Each source is parsed into this model, homologized, and clustered bottom-up (over variables, then constraints and the objective, then whole-model structure) and, separately, by application domain and solution approach; the resulting groups are labeled by a rule-seeded, self-updating classifier. We validate the representation rather than assume it: per-cluster representatives are regenerated as independent LaTeX and re-solved across CBC, HiGHS and Gurobi against the optimum reported in the source paper. The outcome is an objective, repeatable taxonomy of variables, constraints and model types: the principled foundation on which our raiLPminer line of automated railway-rescheduling model development builds.

---


### 37. [Evaluating Nonuniform Dependability Across Response Conditions: A Conditional Generalizability Framework Illustrated in Automated Essay Scoring](https://arxiv.org/abs/2607.11981)

**<font color=#1a73e8>作者：</font>** Yi Gui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aggregate reliability estimates can obscure heterogeneity in measurement-design burden across response conditions, so a single G- or D-study may mischaracterize a design's adequacy for particular strata. This study introduces a conditional generalizability framework with three components. First, automated scoring configurations -- the encoder architectures and scoring-head families admissible within a fixed pipeline -- are treated as a universe of admissible measurement conditions rather than incidental modeling choices. Second, analytical D-study projections are compared with empirical configuration sweeps over a finite scoring pool, yielding two estimands of design adequacy whose agreement or divergence diagnoses the realized configuration universe. Third, evidence is conditioned on entropy-defined response strata, treating entropy as an operational stratification variable, not a construct claim about writing quality. Whereas recent generalizability-theory extensions address AI-generated item variants on the response side, this framework addresses the analogous scoring-side problem: AI-mediated scoring configurations. Demonstrated with automated essay scoring of timed L2 writing, the realized design was dependable in aggregate (Phi approx 0.76). Re-estimated within entropy strata, dependability stayed high but declined modestly and robustly (Phi = 0.88, 0.87, 0.84) -- a gradient implying different decision-study requirements, the highest-entropy stratum requiring the most crossed conditions. The framework offers a portable workflow for evaluating nonuniform dependability.

---


### 38. [SpikeDS: Dual Sparsity Spikformer for Perineural Invasion Prediction in 3D MRI](https://arxiv.org/abs/2607.11986)

**<font color=#1a73e8>作者：</font>** Induk Um, Youngung Han, Kyeonghun Kim 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perineural invasion (PNI) is associated with poor prognosis in cholangiocarcinoma (CCA). However, its detection from 3D MRI remains challenging due to the subtle and spatially heterogeneous imaging signatures at the tumor periphery. Capturing such spatially sparse cues necessitates volumetric analysis of 3D MRI, but existing deep learning approaches incur prohibitive computational costs on volumetric medical images, limiting their clinical deployment. We propose Dual Sparsity Spikformer (SpikeDS), a spiking neural network architecture that jointly exploits activation sparsity from binary spike communication and spatial sparsity from window pruning based on firing rates. SpikeDS introduces Dual Sparsity Spiking Attention (DSSA), which combines two complementary mechanisms. The first is Window-based Expert Mixture Spiking Attention (W-EMSA), which selectively applies attention only to salient windows identified by their firing rates. The second is Cross-Window Spiking Self-Attention (CW-SSA), which enables global context exchange through an asymmetric scheme in which pruned windows still contribute as key-value sources. Evaluated on a clinical cohort of 139 CCA patients via 5-fold cross-validation, SpikeDS achieves an AUC of 0.753 while consuming only 14.4 mJ, surpassing the best baseline in both AUC and energy efficiency. These results suggest that dual sparsity provides an effective hardware-aware strategy for improving the efficiency of 3D spiking transformers without compromising diagnostic performance.

---


### 39. [Anatomy-Privileged Distillation with Token Routing for MRI-Based Prediction of Perineural Invasion](https://arxiv.org/abs/2607.11987)

**<font color=#1a73e8>作者：</font>** Hyunsu Go, Youngung Han, Kyeonghun Kim 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perineural invasion (PNI) is associated with poor postoperative outcomes in intrahepatic cholangiocarcinoma, but it is confirmed by surgical pathology. Existing preoperative imaging models often rely on radiologist-defined variables, contrast-enhanced imaging, or manual annotations. We propose an anatomy-privileged teacher--student framework for patient-level PNI prediction from T2-weighted MRI. During training, the teacher uses MRI with tumor and liver masks to learn dense token routing, and the student distills this guidance to retain and aggregate informative tokens under a fixed budget. Anatomical supervision is restricted to training, and the deployed model does not require masks at inference. In 155 patients, the proposed method achieved the highest mean AUROC of 0.750 among matched MRI-only baselines evaluated under the same protocol, with 1.43 GFLOPs and 8.02 ms per case on a Jetson Orin Nano Super Developer Kit.

---


### 40. [Sparse Inter-Layer Dependencies of Transformer FFN Neurons](https://arxiv.org/abs/2607.11990)

**<font color=#1a73e8>作者：</font>** Johannes Knittel, Hanspeter Pfister  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feedforward network (FFN) blocks account for a large fraction of the parameters and computation in Transformer architectures, yet their internal structure remains difficult to interpret due to the additive superposition induced by the residual stream. We examine whether the activation of an FFN neuron can be explained by a sparse set of preceding neuron activations and attention outputs. We introduce a training-free attribution method that estimates the relative influence of upstream neurons and attention outputs on a target neuron's activation. Empirically, across models and layers, we find that small subsets of preceding activations and attention outputs suffice to preserve neuron activations with high fidelity when all remaining inputs are masked with their average values. Effective sparsity is even greater when accounting for the inherent activation sparsity of upstream layers. Moreover, applying the neuron-specific masks in all layers simultaneously, such that the induced deviations propagate through the network, leaves model perplexity largely unchanged at moderate sparsity levels. These results demonstrate that, despite dense parameterization, FFNs exhibit sparse and structured inter-layer dependencies at the neuron level. Our method provides a practical, scalable tool for circuit-level interpretability and identifies candidate sparse pathways with potential implications for efficient inference.

---


### 41. [Mitigating The Effect of Class Imbalance in Data with Hierarchical and Dependable Structure](https://arxiv.org/abs/2607.11994)

**<font color=#1a73e8>作者：</font>** Bipin Chhetri, Deepika Giri, Avishek Kadel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifying cybersecurity vulnerabilities using the Common Weakness Enumeration (CWE) taxonomy is challenging due to extreme class imbalance and strong hierarchical dependencies among weakness categories. Although oversampling techniques such as Synthetic Minority Oversampling Technique (SMOTE) and Adaptive Synthetic Sampling (ADASYN) are widely adopted to mitigate class imbalance, their effectiveness for hierarchical CWE text classification remains largely unexplored. This paper proposes a Hierarchy-Aware RoBERTa framework that explicitly incorporates CWE structural information through learnable parent-class embeddings, preserving taxonomic consistency. Our experiments demonstrate that synthetic interpolation in high-dimensional embedding spaces violates the inherent parent-child constraints of the CWE hierarchy, offering only marginal benefits for classical ML models while consistently degrading deep learning architectures. Evaluated on a CWE Research Concept dataset, the proposed model achieves a weighted F1-score of 0.76 without data augmentation, outperforming all baselines with notable gains on minority classes, including the Class category whose F1-score improved from 0.40 to 0.60 over the BERT baseline. Our results suggest that hierarchy-aware representation learning is a more principled alternative to oversampling for structured vulnerability classification.

---


### 42. [MetaView: Monocular Novel View Synthesis with Scale-Aware Implicit Geometry Priors](https://arxiv.org/abs/2607.12000)

**<font color=#1a73e8>作者：</font>** Yufei Cai, Xuesong Niu, Hao Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current visual generation models are capable of producing high-quality content, yet they lack a coherent perception of the spatial structure. Existing generative novel view synthesis methods typically introduce explicit geometry priors, which enforce spatial consistency but inherently restrict generalization in large view changes. In contrast, recent interactive generative methods favor implicit scene modeling, offering greater flexibility at the cost of precise camera control and geometry consistency. In this paper, we propose MetaView, a diffusion-based monocular novel view synthesis framework that enables rendering under large view changes from a single image. Our key insight is to combine implicit geometry modeling with minimal yet essential explicit 3D cues: we incorporate implicit geometry priors from a feed-forward geometry perception network to regularize structure without imposing restrictive reconstruction pipelines, while leveraging metric depth to anchor the generation to a metric scale. This design allows MetaView to achieve both geometry consistency and precise controllability. Extensive experiments demonstrate that, under challenging monocular large viewpoint changes, MetaView significantly outperforms existing methods and exhibits superior generalization. Our code is publicly available at this https URL.

---


### 43. [An Empirical Analysis of Continual Learning for Heterogeneous Medical Visual Question Answering](https://arxiv.org/abs/2607.12048)

**<font color=#1a73e8>作者：</font>** Mai A. Shaaban, Tausifa Jan Saleem, Alaa Mohamed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying medical visual question answering (MedVQA) systems in real-world clinical settings requires models that adapt to new clinical tasks without forgetting previously acquired knowledge. Continual learning (CL) provides a practical framework for this setting. Despite rapid progress in medical vision-language models, the behavior of CL methods when training these models across heterogeneous MedVQA tasks remains underexplored. This work presents a systematic evaluation of CL for MedVQA across diverse clinical objectives, including classification, multi-label classification, detection, cell counting, and report generation. Specifically, we explore (1) the ability of existing CL methods to mitigate catastrophic forgetting; (2) their sensitivity to task ordering, analyzing how different task sequences influence performance retention and forgetting; and (3) the evolution of low-rank adaptation parameters as new tasks are learned, revealing patterns of weight drift under different CL methods. Our findings suggest that existing CL methods struggle to maintain stability-plasticity balance when tasks with different objectives and supervision formats are interleaved. Code and full experimental setup will be publicly available.

---


### 44. [Representation and Reference Selection in Training-Free Synthetic Image Attribution](https://arxiv.org/abs/2607.12052)

**<font color=#1a73e8>作者：</font>** Meiling Li, Pietro Bongini, Benedetta Tondi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic image attribution aims at identifying the generator responsible for a given AI-generated image. Training-free reference-based attribution methods are easily scalable, since newly emerging generators can be incorporated by adding source-specific references rather than retraining a task-specific classifier. Their performance depends on two coupled factors: the representation space used for comparison and the way source-specific references are constructed. However, the interaction between these two factors remains largely unexplored. In this paper, we provide a controlled analysis of this interaction using references and off-the-shelf pretrained representations. We study representations extracted from different layers of CLIP and DINOv2, along with three reference selection methods with varying semantic constraints: arbitrary, semantically aligned, and resynthesis-based references. Our results show that attribution accuracy consistently peaks at intermediate representation levels, indicating that source-discriminative cues are more accessible before strong semantic abstraction dominates. We further show that intermediate representations are not completely semantically neutral, making reference selection critical: semantically constrained references reduce query-reference mismatch and improve attribution, especially under limited reference budgets. Resynthesis is most useful in low-reference regimes, while semantically aligned references provide a better accuracy-cost trade-off when a moderate-sized reference pool is available. Our findings show that training-free reference-based attribution should be understood as the interaction between where images are compared, how the reference set is constructed, and how many references are available.

---


### 45. [Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability](https://arxiv.org/abs/2607.12056)

**<font color=#1a73e8>作者：</font>** Said Elnaffar, Farzad Rashidi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Online shopping is increasingly shifting toward a model in which AI agents independently search for products, compare options, evaluate constraints, and carry out parts of the purchasing process for users. Website design must now support both human and agent-mediated interaction. This paper introduces the agent-ready website, a design framework for enhancing the readability, interpretability, verifiability, and actionability of e-commerce platforms for AI agents. Existing web design, SEO, and generative engine optimization (GEO) metrics do not fully assess a website's capacity for agent-mediated interaction. The proposed framework is structured around three dimensions agent interpretability, agent executability, and agent decision reliability supported by features such as machine readability, semantic clarity, agent actionability, and contextual decision-reliability signals. The framework is evaluated through a controlled experiment comparing a human-oriented baseline and an agent-ready version of an identical website prototype, with identical catalogs, pricing, stock, and shopping workflows. The evaluation involved five tasks, three browser-agent models (GPT-4.1, Gemini-2.5 Flash, and Grok-4 Fast), and 300 runs, measuring PASS,PARTIAL,FAIL outcomes, strict and functional success rates, error patterns, step counts, and token consumption. The agent-ready website achieved 134 PASS runs out of 150 versus 74 out of 150 for the baseline (strict success rates of 89.3% vs. 49.3%), with the largest gains in product detail extraction, comparison, and multi-constraint selection. It also reduced PARTIAL outcomes from 43 to 3 and lowered the average step count from 9.31 to 6.49. These results provide preliminary evidence that enhanced structural clarity, action cues, evidence signals, and temporal validity indicators can substantially improve the reliability and efficiency of AI browser agents.

---


### 46. [Learning from Complementary Ultrasound Representations for Liver Disease Classification](https://arxiv.org/abs/2607.12062)

**<font color=#1a73e8>作者：</font>** Sabahattin Mert Daloglu, Gokce Bekar, Ceren Coskun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Differentiating non-alcoholic steatohepatitis (NASH) from non-alcoholic fatty liver disease (NAFLD) using ultrasound remains challenging due to subtle tissue alterations and the limited information available in conventional B-mode imaging. In this work, we investigate whether complementary ultrasound representations derived from the same acquisition can improve NASH versus NAFLD classification. Specifically, we combine conventional B-mode ultrasound with physics-guided and local phase-based image representations and evaluate their effectiveness using self-supervised masked autoencoders (MAEs) and graph convolutional networks (GCNs). Experiments were conducted on a multi-site Mayo Clinic cohort consisting of 2,547 liver ultrasound scans from 125 patients. Compared with conventional B-mode ultrasound alone, complementary ultrasound representations consistently improved classification performance, yielding gains of up to 32.4% in accuracy and 91.2% in F1-score. Furthermore, performance improvements were consistently observed across age groups, sex, race, ethnicity,and acquisition sites.

---


### 47. [Institutional Equity Holdings Prediction Using Node Affinities of Dynamic Graphs](https://arxiv.org/abs/2607.12067)

**<font color=#1a73e8>作者：</font>** Emad Izadifar, Zahed Rahmati  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Institutional equity holdings disclosed in SEC Form 13F filings provide a rich temporal record of portfolio decisions by large investment managers. However, forecasting future allocations and modeling future demand remains challenging due to disclosure lags, reporting noise, and strong persistence in institutional behavior. We introduce the first benchmark for these tasks using temporal graph machine learning, framing holdings prediction as node affinity prediction -- i.e., forecasting portfolio weights -- on a discrete-time temporal bipartite graph of managers and securities extracted from preprocessed filings. On a sampled dataset comprising 99 managers and the S\&P 500 index (503 securities, 209,351 temporal edges across 48 quarters from 2013--2025), Node Affinity prediction model using Virtual State (NAVIS) achieves a state-of-the-art test Normalized Discounted Cumulative Gain (NDCG) of 0.9127 with features (0.9121 without), outperforming all dynamic graph representation learning competitors by a substantial margin, and outperforming all heuristic methods. Remarkably, a simple Exponential Moving Average baseline achieves 0.8882, surpassing all dynamic graph models except NAVIS and all heuristics except Persistent Forecast (0.8891), highlighting the strong smoothness and persistence of institutional portfolios. Domain-specific node features provide only marginal gains (<1.2\%), indicating that temporal and structural signals in the 13F ownership graph already capture most of the predictable information. By benchmarking a suite of Temporal Graph Benchmark (TGB) models under the node affinity prediction setting, both with and without features, on real-world 13F data, this work provides a reproducible foundation for temporal graph machine learning in holdings prediction and portfolio allocation.

---


### 48. [Beyond Parallel Tracking: Interactive Multi-Feature Fusion Drives Semantic Reconstruction from Non-invasive Brain Recordings](https://arxiv.org/abs/2607.12071)

**<font color=#1a73e8>作者：</font>** Boda Xiao, Xiran Xu, Songyi Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous semantic reconstruction from non-invasive neural recordings remains limited by the representational mismatch between semantic feature spaces and neural coding patterns, which severely impedes cross-modal alignment between high-noise neural signals and target semantic features. Prior semantic decoders have predominantly relied on static lexical representations or dynamic contextualized representations in isolation. This single-dimension approach inevitably leads to severe information loss, as it fails to account for the human brain's capacity to integrate stable word attributes and dynamic contexts this http URL bridge this gap, this study introduces a multi-feature fusion framework for non-invasive semantic reconstruction, systematically benchmarking two integration approaches: linear Naive Concatenation and non-linear Multi-Head Cross-Attention. Within this framework, our approach complements static lexical representations (W2V) with dynamic contextual representations (GPT) via an interactive gating mechanism to facilitate cooperative processing during language this http URL through extensive semantic reconstruction and text generation experiments, our framework reveals a robust performance hierarchy: Cross-Att > Concat > GPT > W2V. Crucially, the non-linear cross-attention fusion method achieves state-of-the-art performance, demonstrating that neural language decoding benefits from simulating the collaborative modulation between contextual information and core lexical attributes rather than depending on isolated individual features, while also offering a viable non-invasive brain-to-text decoding method.

---


### 49. [NEEDL-Bench: Dataset for Swiss Needle Cast and Stomata Detection in Microscopy Images](https://arxiv.org/abs/2607.12076)

**<font color=#1a73e8>作者：</font>** Benjamin Blake, Declan McIntosh, Jürgen Ehlting 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present NEEDL-Bench, a microscopy detection benchmark for Swiss Needle Cast (SNC), a fungal disease of Douglas-fir trees. Douglas-fir is a keystone species of major ecological and economic importance as a softwood timber resource, and SNC affects productivity by forming sexual reproductive structures (pseudothecia) that emerge through the gas exchange pores (stomata) of the needles, thereby blocking gas exchange and compromising needle function. To date, there is no dataset for automatic computer vision detection of these structures, despite computer vision being well poised to standardize and viably scale severity measurements. To address this, we present NEEDL-Bench, a dataset of 3250 annotated images from 1082 Douglas-fir needles, annotated for both keypoints and bounding-box detectors. This dataset exhibits a challenging collection of features, including blur, poor object contrast, small objects of interest, and occlusions. To better capture both the nominal distribution of the data and the full breadth of rare structures, we present two distinct evaluation splits: either random sampling from the collected images or sequential sampling to maximize structural diversity. We evaluate multiple popular keypoint and bounding box methods for detection on this dataset as a baseline and observe a maximum F1 score of 0.8479, suggesting significant potential for gains from future development on this problem. Further, we find that larger models generally do not show commensurate gains in performance on this dataset, indicating that improvements on this problem will not come from scaling laws but rather from domain-specific inductive biases.

---


### 50. [Graph Feedback Controls Consensus and Clique Formation in Open-Weight Language-Model Populations](https://arxiv.org/abs/2607.12077)

**<font color=#1a73e8>作者：</font>** Samer Saab Jr, Chaouki Abdallah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent language-model systems increasingly route local interactions, yet the runtime interaction graph is often treated as an implementation detail. We study convention formation in open-weight LM populations spanning 1.1B-32B parameters with a naming-game protocol. Restricted first-token scores over tokenizer-safe labels let us measure prompt-conditioned score-state distributions, construct state-similarity graphs, and separate sampled-label agreement from latent state-space consensus. Across controlled interventions, in the main open-weight repair grids, retained partner-label evidence is necessary but not sufficient: homophilous threshold-similarity routing deletes cross-basin exposure and amplifies fragmentation, while bridge-seeking routing often repairs fragmentation when memory is available. In a three-seed mixed four-model grid, threshold-similarity produces no final behavioral or state consensus in 189 setting-seed runs, whereas state-component and label-disagreement bridges recover final behavioral consensus in 14/18 retained-memory runs. Across homogeneous model populations, retained history generally shifts fragmented dynamics toward consensus; the clearest case is Qwen2.5-32B, which reaches stable behavioral and final state consensus in all 18 retained-history well-mixed settings, while threshold-similarity reaches neither form of consensus in 189 settings. Robustness over state thresholds, population size, and vocabulary size preserves the qualitative ordering, and early-window graph-energy features provide useful within-grid diagnostics.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-203](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
