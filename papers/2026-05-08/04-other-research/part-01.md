# 📦 其他研究 | 2026年05月08日

> 本类共 **270** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

---

### 1. [LCM: Lossless Context Management](https://arxiv.org/abs/2605.04050)

**<font color=#1a73e8>作者：</font>** Clint Ehrlich, Theodore Blackman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Lossless Context Management (LCM), a deterministic architecture for LLM memory that outperforms Claude Code on long-context tasks. When benchmarked using Opus 4.6, our LCM-augmented coding agent, Volt, achieves higher scores than Claude Code on the OOLONG long-context eval, including at every context length between 32K and 1M tokens.
LCM may be considered both a vindication and extension of the recursive paradigm pioneered by Recursive Language Models (RLMs). Our results demonstrate that recursive context manipulation can outperform not just conventional LLMs, but frontier coding agents with native file-system access.
LCM departs from RLM by decomposing symbolic recursion into two deterministic, engine-managed mechanisms: recursive context compression, in which a hierarchical summary DAG automatically compacts older messages while retaining lossless pointers to every original; and recursive task partitioning, in which engine-managed parallel primitives like LLM-Map replace model-written loops. This trade-off, analogous to the move from GOTO to structured control flow in program-ming language design, sacrifices maximal flexibility for termination guarantees, zero-cost continuity on short tasks, and lossless retrievability of all prior state.

---


### 2. [Endogenous Regime Switching Driven by Scalar-Irreducible Learning Dynamics](https://arxiv.org/abs/2605.04054)

**<font color=#1a73e8>作者：</font>** Sheng Ran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Achieving endogenous regime switching is crucial for the emergence of autonomous intelligence, yet remains a central challenge for existing machine learning frameworks, where such transitions are typically externally imposed. In this work, we introduce a classification that distinguishes scalar-reducible dynamics, which can be expressed as gradient flows driven by a scalar objective, from scalar-irreducible dynamics that cannot be reduced to such a form. While most existing machine learning systems operate within the scalar-reducible class, we demonstrate that scalar-irreducible dynamics naturally enable internally generated regime switching through feedback between fast dynamical variables and slow structural adaptation. Using a minimal dynamical model, we illustrate how this mechanism produces sustained endogenous regime transitions without external scheduling. Our results suggest a new dynamical paradigm for regime exploration and provide a potential route toward autonomous learning systems whose adaptive behavior is organized internally rather than externally prescribed.

---


### 3. [A Self-Attentive Meta-Optimizer with Group-Adaptive Learning Rates and Weight Decay](https://arxiv.org/abs/2605.04055)

**<font color=#1a73e8>作者：</font>** JiangBo Zhao, ZhaoXin Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive optimizers like AdamW apply uniform hyperparameters across all parameter groups, ignoring heterogeneous optimization dynamics across layers and modules. We address this limitation by proposing MetaAdamW - a new optimizer that integrates a self-attention mechanism to dynamically modulate per-group learning rates and weight decay. The modulation factors are produced by a lightweight Transformer encoder that operates on statistical features (gradient norms, momentum norms, correlations) extracted from each parameter group. To train the attention module, we introduce a meta-learning objective that combines gradient alignment, loss decrease, and generalization gap. A key novel contribution is the extension of homoscedastic uncertainty weighting (HUW) with task-specific priorities that directly scale the regularization terms - enabling domain knowledge to guide automatic loss balancing. Extensive experiments on five diverse tasks-time series forecasting (ETT), language modeling (WikiText-2), machine translation (Multi30k), image classification (CIFAR-10), and sentiment analysis (IMDB) - demonstrate that MetaAdamW consistently outperforms the standard AdamW baseline in terms of validation loss, accuracy, or perplexity. Depending on the task, MetaAdamW either reduces overall training time (by up to 17.11%) or improves performance (by up to 11.08%) while introducing only moderate overhead; in some cases, it can also mitigate issues of insufficient convergence caused by premature early stopping. Ablation studies validate the effectiveness of each component, including feature versions, grouping strategies, and the proposed priority-injected uncertainty weighting.

---


### 4. [Transformation Categorization Based on Group Decomposition Theory Using Parameter Division](https://arxiv.org/abs/2605.04056)

**<font color=#1a73e8>作者：</font>** Takayuki Komatsu, Yoshiyuki Ohmura, Yasuo Kuniyoshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representation learning seeks meaningful sensory representations without supervision and can model aspects of human development. Although many neural networks empirically learn useful features, a principled account of what makes a representation "good" remains elusive. We study unsupervised categorization of transformations between pairs of inputs under algebraic constraints. Classical disentanglement favors mutually independent factors and fails when factors are coupled. Our prior Galois-theoretic approach decomposes a group via normal subgroups by learning a product of two transformations with one factor constrained to a normal subgroup, covering both commutative and non-commutative cases. That method, however, relied on auxiliary assumptions (e.g., motion and isometry restrictions) not required by decomposition theory, and ablations did not separate theory-based from auxiliary effects. We propose parameter division for a single transformation: we split its parameter into components, impose homomorphism constraints mapping the full transformation to one component, and identify the normal subgroup as the set of transformations when that component is fixed to the identity. This formulation drops the previous auxiliary assumptions and applies more broadly. We evaluate on image pairs involving rotation, translation, and scale; ablations show that group-decomposition constraints drive appropriate categorization.

---


### 5. [Continual Distillation of Teachers from Different Domains](https://arxiv.org/abs/2605.04059)

**<font color=#1a73e8>作者：</font>** Nicolas Michel, Maorong Wang, Jiangpeng He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models continue to scale, with some requiring more storage than many large-scale datasets. Thus, we introduce a new paradigm: Continual Distillation (CD), where a student learns sequentially from a stream of teacher models without retaining access to earlier teachers. CD faces two challenges: teacher training data is unavailable, and teachers have varying expertise. We show that external unlabeled data enables Unseen Knowledge Transfer (UKT), allowing the student to acquire information from domains not present in the training data, while known to the teacher. We also show that sequential distillation causes Unseen Knowledge Forgetting (UKF) when transferred knowledge is lost after training on later teachers. To better trade off between UKT and UKF, we propose Self External Data Distillation (SE2D), a method that preserves logits on external data to stabilize learning across heterogeneous teachers. Experiments on multiple benchmarks show that SE2D reduces UKF and improves cross-domain generalization. The code and implementation for this work are publicly available at: this https URL.

---


### 6. [Lookahead Drifting Model](https://arxiv.org/abs/2605.04060)

**<font color=#1a73e8>作者：</font>** Guoqiang Zhang, Kenta Niwa, W. Bastiaan Kleijn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, a new paradigm named \emph{drifting model} has been proposed for mapping distributions, which achieves the SOTA image generation performance over ImageNet via one-step neural functional evaluation (NFE). The basic idea is to compute a drifting term at each training iteration and then push the output of the model towards the direction of the drifting term. In this paper, we propose a \emph{lookahead drifting model}. At each training iteration, we compute a set of drifting terms sequentially. Each drifting term is calculated by making use of previously computed ones as well as the positive samples and the output of the model. %One key step is to properly scale the drifting terms so that their magnitudes are in a comparable range. In principle, the drifting terms obtained at a later stage capture higher order gradient information towards the positive samples. At each training iteration, the model is optimized by pushing its output towards the direction of the (weighted) summation of the drifting terms. Experimental results on toy examples and CIFAR10 demonstrate the better performance of the new method than the baseline.

---


### 7. [Investigating Trustworthiness of Nonparametric Deep Survival Models for Alzheimer's Disease Progression Analysis](https://arxiv.org/abs/2605.04063)

**<font color=#1a73e8>作者：</font>** Jacob Thrasher, Kaitlyn Heintzelman, Peter Martone 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alzheimer's Dementia (AD) is a progressive neurodegenerative disease marked by irreversible decline, making reliable modeling of its progression essential for effective patient care. Progression-aware methods such as survival analysis are therefore crucial tools for the early detection and monitoring of AD. Recent advancements in deep learning have demonstrated remarkable performance in survival tasks, but alarmingly fewer studies have been conducted in the domain of AD. Further, the studies that do exist do not consider learned bias within the model itself, which could result in unfair and unreliable predictions toward certain marginalized groups. As such, we conduct a rigorous study of fairness in AD progression analysis along with a thorough feature importance study to determine the characteristics which are most important for reliable AD predictions. Furthermore, we propose two novel fairness metrics, called Time-Dependent Concordance Impurity and Kaplan-Meier Fairness, to quantify bias with respect to sensitive attributes such as sex, race, and education in nonparametric survival models. Our study demonstrates that while deep learning powered survival models are robust tools which can aid clinicians in AD care decisions, they often exhibit considerable bias, representing important avenues for future research.

---


### 8. [SemiConLens: Visual Analytics for 2D Semiconductor Discovery](https://arxiv.org/abs/2605.04067)

**<font color=#1a73e8>作者：</font>** Kavinda Athapaththu, Shiwei Chen, Yuan Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The past few years have witnessed vibrant efforts in discovering new two-dimensional (2D) semiconductor materials from both academia and the industry, due to their promising potential in resolving the severe performance deterioration of traditional semiconductors resulting from condensed silicon thickness. However, existing methods (e.g., Density Functional Theory (DFT) or machine-learning-based approaches) suffer from various challenges such as small datasets, and reliability and trustworthiness issues. To bridge this gap, we propose SemiConLens, a visual analytics approach to combine human expertise with the power of ML to enable effective and reliable 2D semiconductor discovery. Specifically, we first develop a new Correlation Aware Multivariate Imputation (CAMI) method and use ML models like autoencoder, which can better learn from limited data and reveal uncertainty, to address the challenge of sparse data in semiconductivity prediction. Built upon this, our visualization module, consisting of three visualization views with linked interactions, allows material researchers to interactively filter, discover and compare 2D semiconductor candidates. A novel circular glyph design and a new cluster-aware layout optimization approach are proposed to effectively display all the user-configurable key attributes and possible prediction uncertainties of each semiconductor candidate, ensuring a reliable and trustable 2D semiconductor discovery. We assess SemiConLens through quantitative evaluations, expert interviews, and use cases. The results demonstrate SemiConLens's capability to help material researchers conduct effective discovery of desirable 2D semiconductors.

---


### 9. [Designing a double deep reinforcement learning selection tool for resilient demand prediction](https://arxiv.org/abs/2605.04068)

**<font color=#1a73e8>作者：</font>** Bilel Abderrahmane Benziane, Benoit Lardeux, Ayoub Mcharek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The use of artificial intelligence in supply chain forecasting has attracted many scientific studies for several decades. However, the process of selecting an appropriate forecasting solution becomes a daunting task. This complexity arises due to the distinct features inherent to each dataset. Research to tackle this issue has been performed since the eighties but recent development of demand forecasting has opened new perspectives. This research aims to enhance automatic forecasting model selection by proposing a novel architecture that acts as a double deep reinforcement learning agent, selecting automatically a forecasting model from the forecasting committee at the time of prediction. Moreover, a novel early-stopping approach based on average reward convergence has been introduced to expedite training time. To evaluate the model's performance, an empirical study was conducted utilizing grocery sales datasets and snack demands datasets. The experimental results demonstrate the robustness of the proposed approach when compared to state-of-the-art methods.

---


### 10. [LAWS: Learning from Actual Workloads Symbolically -- A Self-Certifying Parametrized Cache Architecture for Neural Inference, Robotics, and Edge Deployment](https://arxiv.org/abs/2605.04069)

**<font color=#1a73e8>作者：</font>** Gregory Magarshak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce LAWS (Learning from Actual Workloads Symbolically), a self-certifying inference caching architecture that builds a growing library of certified expert functions from deployment observations. Each expert covers a region of input space defined by a node in the Probabilistic Language Trie (PLT) of the base model and carries a formal error bound holding uniformly over all inputs. The central result is a self-certification theorem: for any input x, the LAWS approximation error is bounded by epsilon_fit + 2*Lambda(W)*C_E, where Lambda(W) is the model Lipschitz constant, C_E is the maximum embedding diameter, and epsilon_fit is the expert training error -- all checkable at deployment time without ground truth. We prove that LAWS generalizes both Mixture-of-Experts and KV prefix caching as special cases and is strictly more expressive than any fixed-K MoE or finite cache. Further results include a monotone hit rate theorem (any-match routing ensures coverage only increases), an expert library growth rate of O(2^H log N) where H is workload entropy, a fleet learning convergence theorem with Omega(K) speedup for K-unit fleets, and an over-the-air update bandwidth bound. We conjecture that LAWS is acquisition-optimal among stationary online caching algorithms and that the effective Lipschitz constant on the training distribution grows polynomially rather than exponentially in depth. Applications are developed for LLM inference, robotic control, and multi-agent edge deployment.

---


### 11. [Toward Human-AI Complementarity Across Diverse Tasks](https://arxiv.org/abs/2605.04070)

**<font color=#1a73e8>作者：</font>** Yuzheng Xu, Annya Dahmani, Matthew D. Blanchard 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Human-AI complementarity, the idea that combining human and AI judgments can outperform either alone, offers a promising pathway toward robust oversight of advanced AI systems. However, whether human-AI complementarity can be achieved on realistic tasks remains an open question. We investigate this through two approaches: hybridization and two AI assistance methods (top-2 assistance and subtask delegation), evaluated on a multi-domain dataset of 1,886 samples spanning knowledge, factuality, long-context reasoning, and deception detection. We find only modest complementarity gains. Baseline hybridization yields just +0.4 percentage points (pp) over AI alone (69.3\% vs 68.9\%), limited both by a small complementarity region (only 8.9\% of items where AI errs but humans do not) and the inability of confidence-based routing to identify it, since the model's confidence is similarly distributed across correct and incorrect predictions. Applied when AI has low confidence, top-2 assistance increases human accuracy from 28.4\% to 38.3\%, surpassing AI alone (37.7\%) -- but primarily because humans adopt correct AI suggestions, not because they successfully override AI errors. These findings suggest that the primary bottleneck is not human task accuracy per se, but the ability to route decisions to humans when it matters and to design assistance methods that enable humans to catch AI mistakes. Our quantitative and qualitative analyses pinpoint where and why each method succeeds or fails, offering concrete targets for future work. We will release our dataset and code upon request to support progress toward more effective human-AI collaboration for AI oversight.

---


### 12. [FlatASCEND: Autoregressive Clinical Sequence Generation with Continuous Time Prediction and Association-Based Pharmacological Testing](https://arxiv.org/abs/2605.04071)

**<font color=#1a73e8>作者：</font>** Chris Sainsbury, Feng Dong, Andreas Karwath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive models can predict clinical events, but generating patient-conditioned multi-step trajectories that respond to intervention tokens and testing whether those responses preserve known pharmacological associations has received limited attention. We present FlatASCEND, a 14.5M-parameter autoregressive clinical sequence model using flat composite tokens and a zero-inflated log-normal time head. Standard distributional metrics (Jaccard 0.889-0.954) do not distinguish FlatASCEND from trivial baselines; the model's value lies in conditional generation from patient-specific prefixes. A prompt-shuffle ablation shows patient-specific conditioning amplifies mechanistic pharmacological effects (2.0-2.2x for steroid to glucose, diuretic to potassium) while leaving confounding-driven associations unchanged (0.9x for insulin to glucose). An incident-user framework assesses directional consistency against prior pharmacological knowledge on MIMIC-IV (N=500 per comparison): 4/10 recover correct mechanistic directions, 2 reproduce treatment-context associations, 4 are incorrect (9/10 significant, Wilcoxon p<0.05). This pattern - partial recovery under residual confounding - is consistent with learned observational associations without causal distinction. Direct preference optimisation with surrogate reward destroys all correct associations (3/3 to 0/3), illustrating reward exploitation when reward and evaluation share an outcome domain. Generative evidence is strongest for short-horizon ICU data; outpatient temporal fidelity is weaker (median 10 vs 154 days on INSPECT), and zero-shot cross-site transfer degrades without adaptation.

---


### 13. [Sparse Autoencoder Decomposition of Clinical Sequence Model Representations: Feature Complexity, Task Specialisation, and Mortality Prediction](https://arxiv.org/abs/2605.04072)

**<font color=#1a73e8>作者：</font>** Chris Sainsbury, Feng Dong, Andreas Karwath  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have been applied to large language models and protein language models, but not systematically to electronic health record (EHR) foundation models. We train TopK SAEs on FlatASCEND, a 14.5-million-parameter autoregressive clinical sequence model, at all 10 residual stream extraction points on INSPECT (outpatient) and MIMIC-IV (ICU). SAE decomposition reveals progressive abstraction across transformer depth: layer-0 features are near-perfect token detectors (45.7% singleton), while layer-6 features span approximately 30 token types across multiple clinical categories (0.5% singleton). Under full-sequence simple linear probes, SAE features outperform dense representations for discrete event prediction (mortality) while dense representations outperform for continuous magnitude prediction (length of stay) - a probe-level representational phenomenon that does not extend to clinically relevant leakage-safe windows, where dense representations match or exceed SAE features across all tested settings (eICU-CRD 48-hour AUC: SAE 0.871 versus dense 0.880; base model zero-shot, SAE dictionaries trained on eICU activations; MIMIC-IV: 0.836 versus 0.914; INSPECT 1-year/3-year: 0.697 versus 0.800). A delta-mode intervention method reduces SAE perturbation noise by 86x, enabling cleaner feature-level experiments, though the resulting perturbation effects are larger than random controls in 3 of 4 conditions but not formally significant. Feature reproducibility across random seeds is 21%, and individual features should be interpreted as illustrative rather than stable.

---


### 14. [Confronting Label Indeterminacy in Automated Bail Decisions](https://arxiv.org/abs/2605.04073)

**<font color=#1a73e8>作者：</font>** Cor Steging, Tadeusz Zbiegień  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bail decisions present a fundamental challenge for data-driven decision support systems. When bail is denied, the counterfactual outcome of whether the defendant would have appeared in court remains unobserved. As a result, historical bail data embed structural label indeterminacy: future decisions are influenced by past decisions whose outcomes are only partially knowable. Building automated systems on such data risks introducing bias and reinforcing feedback loops. This raises a core question for machine-learning systems intended to assist judicial actors: how should cases in which bail was denied be treated during model development? In a case study of bail decisions from the Unified Judicial System of Pennsylvania, we evaluate five contemporary approaches to handling label indeterminacy across three machine learning models, including a novel label imputation method motivated by the dynamics of bail decisions. Each method relies on unverifiable assumptions, yet all influence the models' predictive behaviour, sometimes even more so than the choice of model itself. Explainable AI analysis further reveals that these effects extend to the models' internal decision-making processes as well. Finally, we consider the notion of label indeterminacy from a legal perspective and assess the legitimacy of these approaches in the context of bail decision-making.

---


### 15. [A Regulatory Governance Framework for AI-Driven Financial Fraud Detection in U.S. Banking: Integrating OCC, SR 11-7, CFPB, and FinCEN Compliance Requirements for Model Development, Validation, and Monitoring Lifecycles](https://arxiv.org/abs/2605.04076)

**<font color=#1a73e8>作者：</font>** Mohammad Nasir Uddin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> U.S. financial institutions deploying AI-based fraud detection face a fragmented compliance landscape spanning four regulatory frameworks -- OCC Bulletin 2011-12, SR 11-7, the CFPB AI circular, and FinCEN BSA/SAR requirements -- with no integrated governance life cycle connecting these requirements to model development, validation, and monitoring practice. This paper presents the Regulatory Governance Framework for AI-Driven Financial Fraud Detection (RGF-AFFD), a three-tier governance architecture empirically anchored in a multi-study empirical program. Using the IEEE-CIS dataset (590,540 transactions) and ULB benchmark (284,807 transactions), we benchmark six architectures including an LSTM+XGBoost ensemble, and conduct ablation, temporal drift, SHAP interpretability, and BISG fairness analyses. The LSTM+XGBoost ensemble achieves ROC-AUC of 0.9289 (F1: 0.6360) with a benefit-cost ratio of 6:1. XGBoost demonstrates the strongest temporal stability (delta-AUC = -0.0017 versus -0.0626 for LSTM). The RDT-FG Regulatory Digital Twin meta-model translates metrics into four regulator-specific health scores and a composite Regulatory Fitness Index for continuous compliance monitoring. The RGF-AFFD is the first integrated deployment blueprint to simultaneously satisfy OCC, SR 11-7, CFPB, and FinCEN requirements, supported by a community bank implementation vignette and four evidence-based policy recommendations.

---


### 16. [Balanced Aggregation: Understanding and Fixing Aggregation Bias in GRPO](https://arxiv.org/abs/2605.04077)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zeng, Jiameng Huang, Zhangyue Yin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a central paradigm for improving reasoning and code generation in large language models, and GRPO-style training is widely adopted for its simplicity and effectiveness. However, an important design choice remains underexplored: how token-level policy gradient terms are aggregated within each sampled group. Standard GRPO uses sequence aggregation, while recent work has advocated token aggregation as a better alternative. We show that these two rules induce different optimization biases: token aggregation introduces sign-length coupling, while sequence aggregation implicitly downweights longer responses through sequence-level equal weighting. To address this tension, we propose \textbf{Balanced Aggregation (BA)}, a simple drop-in replacement that computes token-level means separately within the positive and negative subsets and then combines them with sequence-count-based weights. Experiments with Qwen2.5-Math-7B and Qwen3-1.7B on DAPO-17k and Polaris, evaluated on six reasoning and coding benchmarks, show that BA consistently improves training stability and final performance over standard token and sequence aggregation. Our analysis further shows that the relative effectiveness of token and sequence aggregation is largely governed by response-length variation and the positive-negative length gap, highlighting aggregation as a critical design dimension in GRPO-style RLVR.

---


### 17. [Connecting online criminal behavior with machine learning: Using authorship attribution to analyze and link potential online traffickers](https://arxiv.org/abs/2605.04080)

**<font color=#1a73e8>作者：</font>** Vageesh Kumar Saxena  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This research investigated how online criminal activities can be better understood and connected using data-driven machine learning methods. Many illegal activities, such as human trafficking and illicit trade, have moved to online platforms where offenders hide behind anonymous accounts and frequently change identities. This makes it difficult for authorities to understand how large these networks are and how different online profiles may be linked.
The research shows that people tend to maintain consistent patterns in how they write advertisements and present images online, even when they try to stay anonymous. By analysing these patterns across large collections of online advertisements, the research demonstrates how to link related accounts and identify repeated behaviour across illegal online markets.
In addition, the research also addresses how such methods should be used responsibly. It proposes clear guidelines to ensure that privacy, fairness, and transparency are respected when these tools are applied. Overall, the research provides practical ways to support law enforcement investigations while emphasising careful and ethical use.

---


### 18. [Time series causal discovery with variable lags](https://arxiv.org/abs/2605.04081)

**<font color=#1a73e8>作者：</font>** Bruno Petrungaro, Anthony C. Constantinou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal Bayesian Networks (CBNs) are a powerful tool for reasoning under uncertainty about complex real-world problems. Such problems evolve over time, responding to external shocks as they occur. To support decision-making, CBNs require a cause-and-effect map of the variables under consideration, known as the network's structure. Learning the graphical structure of a causal model from data remains challenging; learning it from time-series data is even harder because dependencies may arise at different time lags. Existing time-series causal discovery methods often assume a fixed lag window and do not explicitly optimise edge-specific lags. We propose a Tabu-based structure learning algorithm that searches for a time-ordered directed structure (i.e., where every edge respects time) while allowing edge-specific lags up to a specified maximum lag. The approach uses a decomposable BIC-based score with node-specific effective sample sizes and an explicit lag-length penalty encouraging parsimonious delay assignments while preserving efficient local score updates. We provide theoretical guarantees of validity and local optimality, and we also describe a parallel implementation for improved scalability. In simulations, the method recovered graph structure competitively and estimated lags accurately when true adjacencies were recovered. On a real-world UK COVID-19 policy dataset, the learnt structure was dominated by short delays while retaining a substantial minority of longer-lag dependencies, consistent with delayed behavioural and epidemiological effects.

---


### 19. [Enhancing the interpretability of spatially variable N2O model predictions with soft sensors during wastewater treatment](https://arxiv.org/abs/2605.04082)

**<font color=#1a73e8>作者：</font>** Mohammad Raeisi Gahrouei, Pedram Ramin, Vincenzo A. Riggio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based solutions for nitrous oxide (N2O) emissions from wastewater treatment plants (WWTP) are informed by operational datasets designed to control nutrient levels in liquid waste, coupled with dedicated campaigns for N2O measurements. We analysed how machine learning (ML) models predict disturbances to WWT operation and spatially variable N2O emissions. A real dataset was investigated to validate the modelling framework from N2O emissions predicted by four ML models (R2 = 0.79 - 0.89). Monitoring campaigns for N2O were simulated with a plant-wide mechanistic model to include additional sensors, site-level N2O datasets, and wastewater disturbances (n = 16). ML models were highly accurate (0.97 +- 0.02, n = 80), but the feature importance depended on the model, the scenario and the N2O measurement scale (reactor vs. WWTP). We argue that N2O soft sensor model predictions are limited to the measuring location and the methodological uncertainty of the dataset, which affect the interpretability of the model. Lastly, the analysis of the mechanistic model structure exposed interactions between autotrophic and heterotrophic pathways over nitric oxide which can overestimate aerobic nitrite production and bias the N2O pathway contributions.

---


### 20. [Regularized Centered Emphatic Temporal Difference Learning](https://arxiv.org/abs/2605.04100)

**<font color=#1a73e8>作者：</font>** Xingguo Chen, Chaohui Wu, Jinguo Ye 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Off-policy temporal-difference (TD) learning with function approximation faces a structural tradeoff among stability, projection geometry, and variance control. Emphatic TD (ETD) improves the off-policy projection geometry through follow-on emphasis, but the follow-on trace can have high variance. We revisit this tradeoff through Bellman-error centering. Although centering naturally removes a common drift term from TD errors, we show that a naive centered emphatic extension introduces an auxiliary coupling that can destroy the positive-definiteness of the ETD key matrix. We propose \emph{Regularized Emphatic Temporal-Difference Learning} (RETD), which preserves the follow-on trace and regularizes only the auxiliary centering recursion, corresponding to lifting the lower-right block of the coupled key matrix from \(1\) to \(1+c\). We derive the RETD core matrix, prove convergence under a conservative sufficient regularization condition, and evaluate the method on diagnostic linear off-policy prediction tasks. The experiments show that RETD avoids the instability of naive centered emphatic learning, preserves favorable emphatic geometry, and exhibits a robust intermediate regime for the regularization parameter \(c\) across the diagnostics.

---


### 21. [HERCULES: Hardware-Efficient, Robust, Continual Learning Neural Architecture Search](https://arxiv.org/abs/2605.04103)

**<font color=#1a73e8>作者：</font>** Matteo Gambella, Fabrizio Pittorino, Manuel Roveri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) has emerged as a powerful framework for automatically discovering neural architectures that balance accuracy and efficiency. However, as AI transitions from static benchmarks to real-world deployment, the traditional focus on hardware-aware efficiency is no longer sufficient. We observe that modern NAS methods, especially those that target edge AI, are evolving to address a triple objective: Efficiency, Robustness, and Continual Learning. While efficiency ensures feasibility in resource-constrained environments, robustness guarantees reliability under environmental variabilities, and continual learning enables adaptation to sequential tasks without catastrophic forgetting. We propose a taxonomy of NAS approaches through this triple lens, distinguishing between methods targeting resource optimization, environmental resilience, and architectural plasticity. This unified perspective reveals that these axes, though often studied in isolation, are mutually reinforcing. Building on this taxonomy, we map the current landscape of these NAS methods into a new framework called Hardware-Efficient, Robust, and ContinUal LEarning Search (HERCULES). We define the desiderata, the twelve labours of HERCULES, addressing the non-trivial challenge of balancing an adequate search-space exploration with the immense computational costs of a multi-objective NAS, accounting for these crucial objectives of current AI systems. By identifying critical gaps in existing research, this survey outlines a roadmap toward integrated algorithmic, architectural, and hardware-software co-design for truly deployable, lifelong-learning AI systems.

---


### 22. [MuCALD-SplitFed: Causal-Latent Diffusion for Privacy-Preserving Multi-Task Split-Federated Medical Image Segmentation](https://arxiv.org/abs/2605.04108)

**<font color=#1a73e8>作者：</font>** Chamani Shiranthika, Hadi Hadizadeh, Parvaneh Saeedi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated Learning enables decentralized training by aggregating model updates across clients without sharing raw data, while Split Federated Learning further partitions the model between clients and a server to reduce computation and communication at the client side. However, decentralized medical institutions rarely operate on a single shared task, making standard Federated and SplitFed collaborations poorly aligned with real clinical workflows. Multi-task FL extends these frameworks by allowing clients to handle different tasks, but often introduces instability and privacy vulnerabilities. This study proposes \textbf{MuCALD-SplitFed}, a multi-task SplitFed framework that integrates causal representation learning and latent diffusion. Experiments show MuCALD-SplitFed consistently improves segmentation, while baseline SplitFed fails to converge. The proposed approach further reduces information leakage at split points, mitigating reconstruction-based and membership inference attacks. Additionally, MuCALD SplitFed outperforms state-of-the-art personalized FL and multi-task FL approaches. The code repository is: this https URL.

---


### 23. [Learning reveals invisible structure in low-rank RNNs](https://arxiv.org/abs/2605.04115)

**<font color=#1a73e8>作者：</font>** Yoav Ger, Omri Barak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning in neural systems arises from synaptic changes that reshape the representations underlying behavior. While low-rank recurrent neural networks (RNNs) have emerged as a powerful framework for linking connectivity to function, a theoretical understanding of their learning process remains elusive. Here, we extend the low-rank framework from activity to learning by deriving gradient-descent dynamics directly in a reduced overlap space. We formulate a closed-form, low-dimensional system of ODEs that governs learning in this space, exact for linear RNNs and asymptotically exact for nonlinear RNNs in the large-$N$ Gaussian limit. Central to our analysis is a distinction between two classes of overlaps: loss-visible overlaps, which fully determine network activity, output, and loss, and loss-invisible overlaps, which do not affect function but are required to describe learning. We illustrate the consequences of this decomposition through two phenomena. First, we show that learning can serve as a perturbation that exposes differences in connectivity between functionally equivalent networks. Second, we show that loss-invisible overlaps can act as memory variables that encode training history, and characterize the conditions under which this occurs. Finally, we present several testable predictions for biological learning experiments derived from our theory.

---


### 24. [Simultaneous CNN Approximation on Manifolds with Applications to Boundary Value Problems](https://arxiv.org/abs/2605.04126)

**<font color=#1a73e8>作者：</font>** Hanfei Zhou, Lei Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops convolutional neural network (CNN) methods for simultaneous approximation and elliptic boundary value problems on compact Riemannian manifolds. We establish simultaneous Sobolev approximation results for single- and multichannel CNNs, showing that manifold functions and their derivatives can be approximated with rates governed by the intrinsic dimension and the smoothness gap, rather than by the ambient dimension, thereby mitigating the curse of dimensionality. Building on this approximation theory, we propose a physics-informed CNN (PICNN) framework specially designed for boundary value problems. The main numerical issue is a boundary-norm mismatch: standard PINNs usually impose boundary data through low-order, often L2-type, penalties, whereas elliptic stability requires Sobolev trace control. We address this by introducing a spectral boundary loss based on the boundary Laplace-Beltrami operator, which represents trace errors as weighted frequency energies and relates truncation error to boundary eigenvalue decay. This avoids smooth auxiliary constructions required by exact boundary enforcement and singular double integrals arising in Sobolev-Slobodeckij penalties, while enabling implementations based on Fast Fourier Transforms (FFTs) or precomputed spectral bases on structured boundaries. Numerical experiments demonstrate improved accuracy, convergence, and stability over standard PINNs.

---


### 25. [Position: the Stochastic Parrot in the Coal Mine. Model Collapse is a Threat to Low-Resource Communities](https://arxiv.org/abs/2605.04127)

**<font color=#1a73e8>作者：</font>** Devon Jarvis, Richard Klein, Benjamin Rosman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model collapse, the degradation in performance that arises when generative models are trained on the outputs of prior models, is an increasing concern as artificially generated content proliferates. Related critiques of large language models have highlighted their tendency to reproduce frequent patterns in training data, their reliance on vast datasets, and their substantial environmental cost. Together, these factors contribute to data degradation, the reinforcement of cultural biases, and inefficient resource use. In this position paper we aim to combine these views and argue that model collapse threatens current efforts to democratize AI. By reducing training efficiency and skewing data distributions away from the tails of their support, model collapse disproportionately impacts low-resource and marginalized communities. We examine both the environmental and cultural implications of this phenomenon, situate our position within recent position papers on model collapse, and conclude with a call to action. Finally, we outline initial directions for mitigating these effects.

---


### 26. [Quantum-Resistant Networks: A Review of Primitives, Protocols and Best Practices](https://arxiv.org/abs/2605.04129)

**<font color=#1a73e8>作者：</font>** Elisa Bertino, Ramana Kompella, Ashish Kundu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large-scale quantum computers threaten the public-key cryptographic foundations underpinning today's network security infrastructures. While significant progress has been made in standardizing post-quantum cryptographic (PQC) primitives and adapting individual protocols such as TLS and SSH, far less attention has been paid to the broader architectural consequences of the post-quantum transition for networked systems. In particular, many real-world deployments such as mobile networks, industrial control systems, IoT environments, and regulated infrastructures cannot assume the universal availability, deployability, or desirability of PQ public-key infrastructures. This paper presents the first comprehensive systematization of PQ-resistant network architectures, focusing on key distribution and management as a system-level design problem rather than a protocol-local substitution. We introduce a unified taxonomy spanning cryptographic foundations (symmetric-only, PQ-PKI, hybrid, and information-theoretic multi-path), key-distribution architectures (centralized, hierarchical, replicated, threshold, MPC-backed, and serverless), trust and threat models, key-management lifecycle, and deployment environments. Using this framework, we analyze the security, scalability, and operational trade-offs of a wide range of architectures under realistic PQ adversary assumptions, including harvest-now, decrypt-later attacks and partial infrastructure compromise. Our study highlights fundamental gaps in existing approaches, clarifies when PQ-PKI is necessary or avoidable, and identifies promising research directions for building cryptographically agile, quantum-resilient network infrastructures.

---


### 27. [Constrained Extreme Gradient Boosting for Adapting Reduced-Order Models](https://arxiv.org/abs/2605.04130)

**<font color=#1a73e8>作者：</font>** Melika Baghi, Xiao Liu, Kamran Paynabar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-fidelity simulations, such as computational fluid dynamics and finite element analysis, are essential for modeling complex engineering systems but are often prohibitively expensive for tasks including parametric studies, optimization, and real-time control. Projection-based reduced-order models (ROMs) alleviate this cost by projecting the governing dynamics onto low-dimensional subspaces. However, their performance can deteriorate under parameter variation, motivating the need for adaptive basis construction. In this work, we propose a constrained ensemble learning framework, termed Constrained Extreme Gradient Boosting (cXGBoost), for predicting Proper Orthogonal Decomposition (POD) bases as functions of system parameters. The approach leverages a geometric representation of subspaces on the Grassmann manifold, which are mapped to a Euclidean space to enable efficient regression using gradient boosting trees. A norm constraint is imposed during training to ensure the validity of the inverse mapping and preserve the geometric structure of the predicted subspaces. The proposed method is evaluated on four numerical examples, including fluid dynamics and wave propagation problems, demonstrating its ability to accurately predict parameter-dependent bases while maintaining robustness across nonlinear regimes. These results highlight the potential of combining geometric learning with constrained ensemble methods for scalable and reliable reduced-order modeling of high-dimensional parametric systems.

---


### 28. [Model synthesis and identifiability analysis of stiff chemical reaction systems with inVAErt networks](https://arxiv.org/abs/2605.04134)

**<font color=#1a73e8>作者：</font>** Sreejata Dey, Guoxiang Grayson Tong, Jonathan F. MacArt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the problem of learning data-driven replicas for stiff systems of ordinary differential equations arising in chemical kinetics that can be evaluated with high computational efficiency. We first focus on training emulators for families of reaction equations under varying reaction rates, using conditional residual networks or long-short term memory architectures. We then apply a recently proposed data-driven framework known as ``inVAErt networks'' to address the ill-posed inverse problem of inferring reaction rates, integration time, and possibly initial conditions from a target set of species concentrations - a problem that has received relatively little attention in the literature. The proposed approach is demonstrated on chemical systems with reversible and irreversible kinetics, spanning 2 to 20 differential equations, 3 to 20 chemical species, and 3 to 25 reaction rate parameters. Relative root mean squared errors produced by the proposed emulators range from $10^{-5}$ for lower-dimensional systems to $10^{-4}$ and $10^{-3}$ for an air pollution model and a hydrogen-air reaction system, respectively. Manifolds of non-identifiable reaction rates recovered by the proposed approach can be analytically verified for simple systems and are consistent with local identifiability analysis in higher dimensions.

---


### 29. [Enabling Real-Time Training of a Wildfire-to-Smoke Map with Multilinear Operators](https://arxiv.org/abs/2605.04164)

**<font color=#1a73e8>作者：</font>** Zachary Morrow, Joseph Crockett, John D. Jakeman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wildfires are a major producer of fine particulate matter, impacting human health and the electrical grid. Accurately forecasting smoke impacts over long time scales incorporates fuel treatment strategies, natural fuel succession, and stochastic events like lightning strikes. However, predicting smoke for each fuel distribution with a forward simulation of a coupled fire-atmosphere model is computationally infeasible. Moreover, relatively simple fire models are tractable to run in many long-time scenarios but do not capture smoke transport. We use data-driven multilinear operators to predict a smoke concentration field from knowledge of the time since ignition for two quantities of interest: aerosol optical depth and smoke detection. Our method first computes the principal components of time-since-ignition and smoke concentration fields and then learns a map from powers of the input coefficients to the output coefficients. We apply our learned operator to smoke prediction in the Upper Rio Grande Watershed. After collecting training data, learning the approximation weights on a CPU takes less than 30 seconds, and each forward call takes less than 1 ms. On a proxy for aerosol optical depth, we obtain equal accuracy to Monte Carlo sampling with fewer than half as many coupled model calls. For smoke detection, we obtain an intersection-over-union (IoU) of 65% and an area under the receiver operating characteristic curve (AUC) of 0.95 on holdout data. Our method is significantly more accurate than the most similar published smoke classifier, which obtains an IoU and AUC of 0.15 and 0.61, respectively, on a 2015 bushfire in Australia.

---


### 30. [FlowEval: Reference-based Evaluation of Generated User Interfaces](https://arxiv.org/abs/2605.04165)

**<font color=#1a73e8>作者：</font>** Jason Wu, Priyan Vaithilingam, Eldon Schoop 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) and coding agents are often applied to user interface (UI) development, developers find it difficult to reliably assess their proficiency in visual and interaction design. Existing evaluations either rely on human experts, who can accurately assess usability by testing critical flows but are slow and costly, or on automated judges, which are scalable but less accurate and opaque. We present FlowEval, a reference-based framework that measures whether a generated UI supports realistic interaction flows by comparing navigation traces from real websites to traces from generated analogs using reference-based similarity metrics (e.g., dynamic time warping). In a small-scale study with expert UI evaluators, we show that reference-based metrics strongly correlate with human judgments, suggesting that they can provide scalable yet trustworthy evaluation for UI generation systems.

---


### 31. [Actionable Real-Time Modeling of Surgical Team Dynamics via Time-Expanded Interaction Graphs](https://arxiv.org/abs/2605.04169)

**<font color=#1a73e8>作者：</font>** Vincenzo Marco De Luca, Antonio Longa, Giovanna Varni 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Surgical team performance arises from complex interactions between technical execution and non-technical skills, including communication and coordination dynamics. However, current surgical AI systems predominantly model visual workflow signals, lacking structured representations of intraoperative team interactions over time. We propose a real-time actionable approach for modeling surgical team dynamics using time-expanded interaction graphs, where team members are modeled as time-indexed nodes and communication exchanges define directed edges. This spatio-temporal expansion enables dynamic interaction modeling, while allowing efficient inference with a static graph neural network. The model predicts procedural efficiency as the deviation from the expected duration and supports real-time deployment. Beyond prediction, we perform a counterfactual analysis to identify minimal changes in communication structure and interpretable behavioral variables associated with improved predicted outcomes. Experiments on recorded surgical procedures show that structured modeling of team interactions improves early identification of prolonged interventions and provides coherent, actionable explanations. This work advances surgical AI toward real-time, team-aware, and actionable decision support in the operating room.

---


### 32. [A Provably Convergent and Practical Algorithm for Gromov--Wasserstein Optimal Transport](https://arxiv.org/abs/2605.04175)

**<font color=#1a73e8>作者：</font>** Ling Liang, Lei Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gromov--Wasserstein optimal transport (GWOT) aligns metric measure spaces by matching their within-domain relational structures, but large-scale GWOT remains challenging because its objective is nonconvex and projection onto the transport polytope is often solved only approximately in practice. This leads to a gap between practical projected-gradient implementations and convergence theory, which typically assumes exact projections. For squared-loss GWOT, we propose an inexact projected-gradient framework with a verifiable feasibility-residual-based inexact condition for the projection subproblem. This condition is directly computable and avoids unknown quantities such as the exact projection point. Under this implementable condition, we prove subsequential convergence to stationary points and, with a mild tolerance-decay condition, convergence of the whole sequence. The resulting method retains the simplicity and sparsity of projected-gradient schemes while providing rigorous convergence guarantees, turning projected-gradient methods into a principled and scalable approach for GWOT with provable reliability.

---


### 33. [Constraint-Enhanced Reinforcement Learning Based on Dynamic Decoupled Spherical Radial Squashing](https://arxiv.org/abs/2605.04185)

**<font color=#1a73e8>作者：</font>** Qijun Liao, Zhaoxin Yu, Jue Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When deploying reinforcement learning policies to physical robots, actuator rate constraints -- hard limits on how fast each joint can move per control step -- are unavoidable. These limits vary substantially across joints due to differences in motor inertia, power bandwidth, and transmission stiffness, creating pronounced heterogeneity that existing methods fail to handle geometrically: the per-joint feasible region forms a high-dimensional box in action-increment space, yet QP projection and spherical parameterization methods impose isotropic ball-shaped constraints, exponentially under-covering the true feasible set as heterogeneity grows. This paper proposes Dynamic Decoupled Spherical Radial Squashing (DD-SRad), which resolves this mismatch by computing a position-adaptive radius independently for each actuator, achieving tight alignment with the true per-joint feasible region. DD-SRad satisfies per-step hard constraints with probability~1, preserves well-conditioned gradients throughout training, and admits exact policy gradient backpropagation with zero runtime solver overhead. MuJoCo benchmark experiments demonstrate the highest task return at zero constraint violation -- matching the unconstrained upper bound -- with 30%--50% improvement in constraint-space coverage over spherical baselines. High-fidelity IsaacLab simulations with Unitree H1 and G1 humanoid robots confirm end-to-end optimality parameterized directly from official joint specifications, validating a systematic pathway from hardware datasheets to safe deployment.

---


### 34. [Exploring the Output of Software Testing Tools through a Visual Comparative Analysis](https://arxiv.org/abs/2605.04189)

**<font color=#1a73e8>作者：</font>** Brandon Lit, Anthony Maocheia-Ricci, Thomas Driscoll  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Software testing is a fundamental process of software development, and prior work has shown that visualizations of test results support testers' decision-making. However, Human-Computer Interaction research on software testing has yet to explore and understand the shared interface elements and patterns in visualization of testing outputs. To address this, we conducted a visual comparative analysis of the output of 50 software testing tools and harnesses (44 with CLI output, 6 with GUI output) across four popular programming languages. Our analysis reveals the common interface elements in software testing tools, how these tools display and visualize test results, as well as the specific make-up of the output. Our findings provide insight on how visual testing output is formatted and how colour is used across both CLI and GUI environments, identifying trends that can be applied by developers of testing tools.

---


### 35. [ANDRE: An Attention-based Neuro-symbolic Differentiable Rule Extractor](https://arxiv.org/abs/2605.04193)

**<font color=#1a73e8>作者：</font>** Iman Sharifi, Peng Wei, Saber Fallah  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inductive Logic Programming (ILP) aims to learn interpretable first-order rules from data, but existing symbolic and neuro-symbolic approaches struggle to scale to noisy and probabilistic settings. Classical ILP relies on discrete combinatorial rule search and is brittle under uncertainty, while differentiable ILP methods typically depend on predefined rule templates or inaccurate fuzzy operators that suffer from vanishing gradients or poor approximation of logical structure when reasoning over probabilistic predicate valuations. This paper proposes an Attention-based Neuro-symbolic Differentiable Rule Extractor (ANDRE), a novel ILP framework that learns first-order logic programs by optimizing over a continuous rule space with attention-based logical operators. ANDRE replaces both rule templates and logical operators with fully differentiable, attention-driven conjunction and disjunction operators that approximate logical min-max semantics, enabling accurate, stable, and interpretable reasoning over probabilistic data. By softly selecting, negating, or excluding predicates within each rule, ANDRE supports flexible rule induction while preserving symbolic structure. Extensive experiments on classical ILP benchmarks, large-scale knowledge bases, and synthetic datasets with probabilistic predicates and noisy supervision demonstrate that ANDRE achieves competitive or superior predictive performance while reliably recovering correct symbolic rules under uncertainty. In particular, ANDRE remains robust to moderate label noise, substantially outperforming existing differentiable ILP methods in both rule extraction quality and stability.

---


### 36. [The Impact of Vocabulary Overlaps on Knowledge Transfer in Multilingual Machine Translation](https://arxiv.org/abs/2605.04196)

**<font color=#1a73e8>作者：</font>** Oona Itkonen, Jörg Tiedemann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge transfer, especially across related languages, has been found beneficial for multilingual neural machine translation (MNMT), but some aspects are still under-explored and deserve further investigation. A joint vocabulary is most often applied to form a uniform word embedding space, but since the impact of a disjoint vocabulary on model performance is far less studied, there is no consensus on how much knowledge transfer is mainly due to vocabulary overlap. In this paper, we present systematic experiments with joint and disjoint vocabularies, and auxiliary languages related and unrelated to the source language. We design this experiment in an out-of-domain setup in order to emphasize transfer and the impact of the auxiliary language. As expected, we yield better results with more extensive vocabulary overlaps typical for related languages, but our experiments also show that domain-match and language relatedness are more important than a joint vocabulary.

---


### 37. [Deep Wave Network for Modeling Multi-Scale Physical Dynamics](https://arxiv.org/abs/2605.04198)

**<font color=#1a73e8>作者：</font>** Alexander I. Khrabry, Edward A. Startsev, Andrew T. Powis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Performance of deep learning models is strongly governed by architectural capacity, with width and depth as primary controls. However, in physical-science applications, models are often compared at a single fixed size or by separating accuracy and computational cost, which can be misleading since architectures exhibit different accuracy-cost scaling as width and depth vary. This issue is particularly relevant for U-Net-type encoder-decoder models, widely used for multi-scale gas, fluid, and plasma dynamics due to their ability to represent features across spatial scales. A U-Net constructs a multi-resolution representation via an encoder that progressively reduces spatial resolution, followed by a decoder that restores it for prediction. Skip connections link corresponding encoder and decoder features, preserving fine-scale information and improving optimization. In practice, U-Net width is routinely tuned, while depth is typically kept fixed (a set number of down/up-sampling stages with few convolutions per stage), limiting systematic exploration of depth for improving the accuracy-cost trade-off. We address this limitation by increasing effective depth through stacking multiple encoder-decoder "waves" in series, with skip connections both within and across waves to enable progressive cross-scale refinement. We call this architecture a Deep Wave Network (DW-Net). Training data, optimization, and schedules are kept identical across models. Instead of evaluating single configurations, we train multiple width variants of each architecture and compare accuracy vs. GPU time Pareto fronts. Across several 2D and 3D flow benchmarks, DW-Net models consistently improve the Pareto frontier over single-wave U-Nets, achieving higher accuracy at matched cost or similar accuracy at reduced cost, and reaching low-error regimes with up to 3x less training time under identical training settings.

---


### 38. [Topology-Constrained Quantized nnUNet for Efficient and Anatomically Accurate 3D Tooth Segmentation](https://arxiv.org/abs/2605.04201)

**<font color=#1a73e8>作者：</font>** Paarth Prasad, Ruchika Malhotra  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a topology-constrained quantized nnUNet framework for efficient and anatomically accurate 3D tooth segmentation, addressing the challenges of spatial distortion introduced by quantization in deep learning models. The proposed method integrates a novel tooth-specific topological loss into quantization-aware training, preserving critical anatomical structures such as tooth count, adjacency relationships, and cavity integrity while maintaining computational efficiency. The system employs an 8-bit quantized nnUNet backbone, where weights and activations are dynamically calibrated to minimize precision loss during inference. Furthermore, the topological loss combines connected-component analysis, adjacency consistency, and hole detection penalties, ensuring anatomical fidelity without modifying the underlying network architecture. The joint optimization objective harmonizes cross-entropy loss, quantization regularization, and topological constraints, enabling end-to-end training with gradient approximations for persistent homology terms. Experiments demonstrate that our approach significantly reduces topological errors compared to conventional quantized models, achieving clinically plausible segmentations on dental CBCT scans. The method retains the hardware efficiency of integer-only inference, making it suitable for deployment in resource-constrained clinical environments. This work bridges the gap between computational efficiency and anatomical precision in medical image segmentation, offering a practical solution for real-world dental applications.

---


### 39. [Sequential Strategic Classification with Multi-Stage Selective Classifiers](https://arxiv.org/abs/2605.04202)

**<font color=#1a73e8>作者：</font>** Ziyuan Huang, Lina Alkarmi, Mingyan Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Strategic classification studies the problem where self-interested individuals or agents manipulate their response to obtain favorable decision outcomes made by classifiers, typically turning to dishonest actions when they are less costly than genuine efforts. Prior works have demonstrated a fundamental inability to get out of this conundrum by only focusing on the design of a classifier. We note that prior work also heavily focuses on either one-shot settings or repeated interaction with the same classifier. Real-world decision making is often multi-stage, involving a sequence of potentially different classifiers as an agent progresses. This paper introduces a sequential, stochastic, multi-stage model of strategic classification, by capturing how agents adapt their behavior, through improvement actions (enhancing both observable features and true attributes) and gaming actions (enhancing only observable features), over multiple levels of classification with increasing difficulty as well as reward. For each level, we adopt a selective classifier that can abstain from making a prediction at low confidence. Consequently, a positive (resp. negative) outcome leads to promotion (resp. demotion) of the agent to the next higher (resp. lower) level, while abstention keeps the agent at the same level. We fully characterize the agent's optimal instantaneous action under selective classifiers and compare the long-term properties and utility of the agent repeatedly following an optimal myopic policy of either no-improvement (never choose the improvement action) or no-gaming (never choose the gaming action). We further examine design principles over the sequence of classifiers that yield higher long-term utility for the latter policy, thereby effectively incentivizing genuine effort in the long run.

---


### 40. [Climate-based Pre-screening of Self-sustaining Regreening Opportunities in Drylands: A Case Study for Saudi Arabia](https://arxiv.org/abs/2605.04206)

**<font color=#1a73e8>作者：</font>** Katja Froehlich, Jonathan Klein, Ibrahim S. Elbasyoni 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale restoration in drylands is widely promoted to address land degradation and biodiversity loss, yet many efforts rely on long-term irrigation, limiting sustainability in water-scarce regions. A key challenge is identifying locations where native vegetation can persist without intensive management while minimizing costly field campaigns. A scalable pre-screening framework is presented that integrates climate and remote sensing data to enable cost-efficient site selection in arid environments using Saudi Arabia as a case study. A Climate Suitability Score (CSS), derived from machine learning models trained on expert-curated reference sites, captures complex climatic dependencies on vegetation persistence. Using multi-year ERA5-Land data for Saudi Arabia, national-scale prediction maps are generated and combined with vegetation indices to identify areas where climate is favorable, but vegetation remains underdeveloped. Multi-criteria screening reduces candidates to thirteen priority locations. Climatically analogous intact ecosystems provide benchmarks for restoration targets and indicate that an average 2.5 fold increase in vegetation coverage is a realistic target for restoration efforts. Overall, this approach narrows the search space, reduces costs, and supports resilient ecosystem recovery planning in water-limited regions.

---


### 41. [Undetectable Backdoors in Model Parameters: Hiding Sparse Secrets in High Dimensions](https://arxiv.org/abs/2605.04209)

**<font color=#1a73e8>作者：</font>** Sarthak Choudhary, Atharv Singh Patlan, Nils Palumbo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present Sparse Backdoor, a supply-chain attack that plants a \emph{provably undetectable} backdoor in pre-trained image classifiers, including convolutional networks and Vision Transformers. The attack injects a structured sparse perturbation along a randomly chosen direction into a small subset of columns at each fully connected layer, propagating a trigger signal to an adversary-chosen target class, and masks the perturbation with an independent isotropic Gaussian dither. The dither serves a single technical purpose: it induces a clean reference distribution anchored at the pre-trained weights, against which undetectability can be formalized. Under a mild margin condition on the pre-trained classifier, we show that the dithered reference is functionally equivalent to the original classifier. We prove that distinguishing the backdoor-injected model from this reference is at least as hard as Sparse PCA detection, which is computationally infeasible under standard hardness assumptions. The guarantee holds against any probabilistic polynomial-time distinguisher with white-box access to the parameters.

---


### 42. [Jordan-RoPE: Non-Semisimple Relative Positional Encoding via Complex Jordan Blocks](https://arxiv.org/abs/2605.04217)

**<font color=#1a73e8>作者：</font>** Yaobo Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Relative positional encodings determine which functions of query-key lag can enter the primitive attention logit. RoPE supplies a rotary phase, while ALiBi supplies an additive distance bias. Motivated by group-theoretic views of linear translation-invariant positional encodings, we study a non-semisimple case in which a complex rotary eigenvalue and a nilpotent response live in the same defective Jordan block. The resulting relative operator generates oscillatory-polynomial features such as $e^{-\gamma d}\cos(\omega d)$, $e^{-\gamma d}\sin(\omega d)$, $d e^{-\gamma d}\cos(\omega d)$, and $d e^{-\gamma d}\sin(\omega d)$, for causal lag $d=i-j\geq 0$. Thus the construction realizes a distance-modulated phase basis $d e^{i\omega d}$, rather than merely adding a separate distance channel to RoPE.
We formulate Exact Jordan-RoPE as a non-semisimple one-parameter representation, give its real block form, and specify the contragredient query action required by non-orthogonal positional maps. We also distinguish this exact representation from stabilized variants whose bounded shear improves numerical behavior but breaks the exact group law. Kernel-level diagnostics and a Jordan-friendly synthetic language-model task show that the coupled Jordan basis is useful when the target contains distance-modulated phase interactions. On a small WikiText-103 byte language model, a scaled-exact variant improves over RoPE and direct-sum baselines within the Jordan family, while RoPE+ALiBi remains strongest overall. The evidence is structural rather than a broad performance claim.

---


### 43. [ARMATA: Auto-Regressive Multi-Agent Task Assignment](https://arxiv.org/abs/2605.04225)

**<font color=#1a73e8>作者：</font>** Yazan Youssef, Aboelmagd Noureldin, Sidney Givigi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Coordinating multi-agent systems over spatially distributed areas requires solving a complex hierarchical problem: first distributing areas among agents (allocation) and subsequently determining the optimal visitation order (routing). Existing methods typically decouple these stages ignoring inter-stage dependencies or rely on decentralized heuristics that lack global context. In this work, we propose a centralized, fully end-to-end auto-regressive framework that jointly generates allocation decisions and routing sequences. The core contribution of our approach is a multi-stage decoding mechanism that unifies high-level allocation and low-level routing in a single autoregressive pass while maintaining a centralized global state. This enables the model to implicitly balance workload distribution with routing efficiency, avoiding local optima common in decentralized methods. Extensive experiments demonstrate that our method significantly outperforms diverse baselines, achieving up to a 20\% improvement in solution quality over industrial solvers such as Google OR-Tools, IBM CPLEX, and LKH-3, while reducing computation time from hours to seconds.

---


### 44. [Capabilities of Auto-encoders and Principal Component Analysis of the Reduction of Microstructural Images; Application on the Acceleration of Phase-Field Simulations](https://arxiv.org/abs/2605.04229)

**<font color=#1a73e8>作者：</font>** Seifallah Fetni, Thinh Quy Duc Pham, Truong Vinh Hoang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, a data-driven framework based on Phase-Field simulations data is proposed to highlight the capabilities of neural networks to ensure accurate low dimensionality reduction of simulated microstructural images and to provide time-series analysis. The dataset was indeed constructed from high-fidelity Phase-Field simulations. Analyses demonstrated that the association of auto-encoder neural networks and principal component analyses leads to ensure efficient and significant dimensionality reduction: 1/196 of reduction ratio with more than 80% of accuracy. These findings give insight to apply analyses on data from the latent dimension. Application of Long Short Term Memory (LSTM) neural networks showed the possibility of making next frame predictions; that makes possible the acceleration of Phase-Field simulation without the need of high computing resources. We discussed the application of such a framework on various areas of research. Different methods are proposed from the conducted analyses, in order to ensure dimensionality reduction, including auto-encoders, principal component analysis and Artificial Neural Networks, and time-series analysis, including LSTM and Gated Recurrent Unit (GRU).

---


### 45. [Layerwise LQR for Geometry-Aware Optimization of Deep Networks](https://arxiv.org/abs/2605.04230)

**<font color=#1a73e8>作者：</font>** Simon Dufort-Labbé, Pierre-Luc Bacon, Razvan Pascanu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geometry-aware optimizers such as Newton and natural gradient can improve conditioning in deep learning, but scalable variants such as K-FAC, Shampoo, and related preconditioners usually impose structural approximations early, often discarding cross-layer interactions induced by the network computation. We introduce Layerwise LQR (LLQR), a framework for learning structured inverse preconditioners under a global layerwise optimal-control objective. The starting point is an exact equivalence: the steepest-descent step under a broad class of divergence-induced quadratic models--including Newton, Gauss-Newton, Fisher/natural-gradient, and intermediate-layer metrics--can be written as a finite-horizon Linear Quadratic Regulator (LQR) problem. This formulation serves as a reference that exposes the layerwise dynamics and cost matrices encoding the original dense geometry. We then derive a scalable relaxation that learns diagonal, (E-)Kronecker-factored, or other structured inverse preconditioners by minimizing the LQR objective and reusing them across iterations. The resulting optimizer wraps standard methods while retaining a principled connection to second-order geometry, without forming or inverting the global curvature matrix. Experiments on ResNets and Transformers show that LLQR improves optimization dynamics and often translates these gains into improved final test performance, while adding only modest wall-clock overhead. It establishes LLQR as a practical framework for geometry-aware second-order methods and a reference for evaluating scalable approximations.

---


### 46. [Anatomy of a failure: When, how, and why deep vision fails in scientific domains](https://arxiv.org/abs/2605.04231)

**<font color=#1a73e8>作者：</font>** Ji-Hun Oh, Dou Hoon Kwark, Kianoush Falahkheirkhah 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mirroring its ubiquity in popular media and all human activities, the use of deep learning (DL) is rapidly growing in scientific imaging modalities. However, unlike everyday RGB pictures, pixels encode precise physicochemical properties in scientific imaging across potentially thousands of channels. While DL is well validated on human-centric RGB perceptual tasks, its effectiveness for scientific imaging remains uncertain. Here, we show that the naive application of DL frameworks to scientific images can lead to critical failures. We evaluate the use of DL for pathology, comparing RGB images of stained tissue with the quantitative and information-rich biochemical signatures of infrared (IR) imaging. Despite this informational advantage, DL models trained on IR data paradoxically underperform. We investigate this discrepancy to find that IR data priors interact poorly with the simplicity bias of DL, causing models to collapse to one-dimensional predictions. This constitutes a catastrophic DL failure because the model's representational capacity remains largely unused, while furthermore raising AI safety concerns and undermining the advantages of such scientific modalities. Notably, this problem persists even with state-of-the-art DL robustification strategies, which are primarily designed and validated for RGB imagery and thus inherit the same prior-bias mismatch. This work establishes a framework for understanding the limitations of generic DL in science and advocates for the study of modality-specific failure modes to guide the development of specialized, safe AI algorithms.

---


### 47. [Disentangled Learning Improves Implicit Neural Representations for Medical Reconstruction](https://arxiv.org/abs/2605.04234)

**<font color=#1a73e8>作者：</font>** Qing Wu, Xuanyu Tian, Chenhe Du 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit neural representations (INRs) have emerged as a powerful paradigm for medical imaging via physics-informed unsupervised learning. Classical INRs optimize an entire network from scratch for each subject, leading to inefficient training and suboptimal imaging quality. Recent initialization-based approaches attempt to inject population priors into pre-trained networks, yet they rely on high-quality images and often suffer from catastrophic forgetting during fine-tuning. We present DisINR, a novel INR framework that explicitly disentangles shared and subject-specific representations. DisINR introduces a shared encoder-decoder pair and subject-specific encoders, whose features are jointly decoded for image reconstruction. By integrating differentiable forward models, it pre-trains the shared modules directly from limited raw measurements, removing the need for pre-acquired high-quality images. During test-time adaptation, only the subject-specific encoder is optimized, while the shared pair remains frozen, effectively preserving learned priors. Extensive evaluations on three representative medical imaging tasks show that DisINR significantly outperforms state-of-the-art INRs in both reconstruction accuracy and efficiency.

---


### 48. [Road Risk Monitor: A Deployable U.S. Road Incident Forecasting System with Live Weather and Road-Level Tiles](https://arxiv.org/abs/2605.04242)

**<font color=#1a73e8>作者：</font>** Anton Ivchenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nationwide road-incident forecasting is a systems problem before it is a modeling problem. A usable service must connect historical incident archives, historicalandliveweather,nationalroadgeometry, offline model training, tile generation, web serving and runtime handoff. This paper presents Road Risk Monitor, a U.S.-wide road-safety stack that combines a nationwide H3 baseline trained on FARS fatal-crash data with a road-segment forecasting pipeline trained from TIGER/Line geometry and US-Accidents events, then serves predictions through live APIs, raster tiles, JSON road tiles, and a public web application.

---


### 49. [Physics-Guided Regime Unmixing](https://arxiv.org/abs/2605.04247)

**<font color=#1a73e8>作者：</font>** Paula Pacheco, Pablo Granitto, Juan B. Cabral  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Linear Mixing Model (LMM) dominates spectral unmixing for its simplicity, but fails under multiple scattering; existing nonlinear models compensate by applying a fixed regime uniformly across entire scenes. We propose Physics-Guided Regime Unmixing (PGRU), which estimates a pixel-wise scalar $\xi_i \in [0,1]$ from observable physical features to activate nonlinear mixing only where justified. Residuals from the Generalized Bilinear Model (GBM), the Post-Nonlinear Mixing Model (PPNM), and Hapke are combined via learned attention, yielding interpretable regime maps. Experiments on Samson, Jasper Ridge, and Urban show consistent improvements over baselines, with physical coherence $\rho > 0.90$.

---


### 50. [Towards a Zero-Trust Supply-Chain Assurance Rubric for ORAN RIC Applications](https://arxiv.org/abs/2605.04249)

**<font color=#1a73e8>作者：</font>** Chun Yin Chiu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open RAN enables third-party xApps and rApps to be onboarded and updated at operational cadence, creating a software supply chain that spans developers, CI systems, registries, onboarding pipelines, and runtime enforcement points. This preprint proposes a zero-trust supply-chain assurance rubric for O-RAN RIC applications. It makes three contributions: first, an app-centric lifecycle threat model for RIC applications across build, signing, publication, onboarding, runtime, and update or rollback stages; second, a WG11-aligned threat-control-evidence mapping that relates lifecycle threats to O-RAN security baselines and complementary supply-chain evidence; and third, an operator-facing assurance profile that combines secure software development practices, SBOM transparency, and SLSA-style provenance into incremental onboarding levels. Analytical case-study walkthroughs and a minimal evidence-checking workflow illustrate how the rubric can support explicit Accept, Escalate, or Block decisions during RIC app onboarding. The evaluation is intended to assess applicability rather than deployment-scale performance; empirical measurements of operational overhead, decision consistency, and detection coverage are left for future work.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-270](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
