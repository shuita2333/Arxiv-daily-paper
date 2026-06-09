# 📦 其他研究 | 2026年06月10日

> 本类共 **527** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

---

### 201. [GENERIC-FNO: Embedding Energy Conservation and Entropy Production into Fourier Neural Operators](https://arxiv.org/abs/2606.08343)

**<font color=#1a73e8>作者：</font>** Jason Sulskis, Sathya Ravi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce GENERIC-FNO, the first neural operator to embed the full GENERIC (metriplectic) structure of nonequilibrium thermodynamics -- reversible, energy-conserving dynamics and irreversible, entropy-producing dynamics coupled through the degeneracy conditions -- directly in function space. Existing structure-preserving neural operators enforce at most a single conservation law or reversible (Hamiltonian) structure, while thermodynamically consistent learning has been confined to finite-dimensional, graph, or particle systems. GENERIC-FNO closes this gap: it learns the energy and entropy functionals as neural operators and parameterizes the Poisson and friction operators as diagonal Fourier multipliers sandwiched between rank-one projections that enforce the degeneracy conditions exactly, by construction, with no penalty term, update projection, or residual. The degeneracy identities hold to machine precision (residuals ~10^-13) for any initialization, dimension, or resolution, so the continuous-time dynamics conserve the learned energy and produce entropy exactly; the explicit time stepping adds only a small O(dt^2) drift (per-step residual ~10^-6). We further note that the (E,S,L,M) decomposition of a given flow is not unique, and introduce a gauge-invariant dissipation diagnostic separating reversible from dissipative dynamics independently of the learned functionals. Across three operator backbones (1D/2D FNOs and DeepONet) and four PDEs spanning reversible, dissipative, and mixed regimes, GENERIC-FNO preserves its exact structural guarantees zero-shot across a 4x super-resolution range (64 to 256), recovers the ground-truth ordering of physical dissipation, and is competitive with strong unconstrained and energy-penalized baselines, outperforming them on several dissipative and mixed problems at comparable or fewer parameters.

---


### 202. [Generative Frontier Planning for Adaptive Peer-Referral Recruitment under Covariate-Dependent Arrivals](https://arxiv.org/abs/2606.08360)

**<font color=#1a73e8>作者：</font>** Lingkai Kong, Hezi Jiang, Andrew Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Peer-referral recruitment systems such as respondent-driven sampling are critical for studying and intervening on hidden populations affected by infectious diseases. To accelerate recruitment, public health agencies must adaptively allocate limited referral resources across multiple rounds, where current decisions shape both the number and the covariates of future recruits. Prior work makes this problem tractable by assuming that referrals are drawn i.i.d.\ from a homogeneous population, an assumption that ignores the homophily and shared context that drive real peer recruitment. We instead consider a more realistic model in which both referral capacity and the covariates of newly referred individuals are conditioned on the referrer, learned from data with a censored count model and a conditional generative model. The resulting planning problem is challenging because each candidate allocation induces a different distribution over future recruits. We propose \emph{Generative Frontier Planning} (GFP), a model-based planner that replaces per-step Monte-Carlo sampling with a deterministic backup over a latent covariate-coverage value surrogate. The surrogate is designed so that the expected value of the next frontier depends on the offspring generative model only through finite-dimensional summaries that are amortized offline, and so that the resulting per-round objective is monotone with diminishing returns. Together, these two properties make planning tractable: the deterministic backup eliminates Monte-Carlo sampling, and the diminishing-returns structure lets a marginal greedy allocation achieve a \((1-1/e)\)-approximation for the per-round problem. On a simulation environment calibrated to a real respondent-driven sampling dataset, GFP outperforms random, reinforcement-learning, and i.i.d.\ dynamic-programming baselines across four discount factors.

---


### 203. [Self-Supervised Vision Transformers for CBCT-Based Detection of Temporomandibular Joint Osteoarthritis](https://arxiv.org/abs/2606.08364)

**<font color=#1a73e8>作者：</font>** Shradhdha Trivedi, Vrundan Sojitra, Mariela Padilla  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporomandibular joint osteoarthritis (TMJ OA) is a prevalent degenerative condition whose osseous changes are often subtle on cone-beam CT (CBCT), making automated detection challenging. We study how well the DINO family of self-supervised vision transformers -- DINOv1, DINOv2, DINOv2+reg, and RAD-DINO (a radiology-pretrained variant) -- transfers to CBCT, asking how much backbone adaptation is needed and of what kind. We propose a simple slice-based pipeline using Vision Transformer (ViT) backbones: axial CBCT slices are encoded per-slice by a frozen or partially adapted ViT and aggregated via attention-based multiple instance learning (MIL) for patient-level binary OA/Normal classification. Through systematic ablation across unfreezing strategies and aggregation designs on a multi-source CBCT dataset, we find that partial unfreezing of the final two transformer blocks is the decisive factor, improving AUC from 0.671 (fully frozen DINOv2) to 0.902. This outperforms DINOv1 (0.867), DINOv2+reg (0.774), and a supervised ImageNet ViT-B/16 baseline (0.843). Our results provide practical guidance for adapting DINO-family foundation models in low-data medical imaging settings, showing that adaptation strategy is a stronger driver of performance than backbone choice alone.

---


### 204. [Pre-Intervention Prediction of Sparse Autoencoder Steering Side Effects](https://arxiv.org/abs/2606.08365)

**<font color=#1a73e8>作者：</font>** Evan Duan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoder (SAE) features are increasingly used to steer language models, but feature steering is rarely clean: the same intervention can behave inconsistently across contexts and perturb unrelated features. We introduce a pre-intervention screening framework for forecasting SAE steering side effects from feature statistics computed before steering. We operationalize side effects along two axes of steering modularity, effect stability and collateral spread, and evaluate GPT-2-small, Pythia-70M-deduped, Gemma-2-2B, and Llama-3.1-8B across ReLU, JumpReLU, and TopK SAE dictionaries. Across these settings, decoder geometry, activation statistics, co-activation structure, and direct-logit footprint predict steering modularity better than frequency-only and activation-magnitude baselines. The signal is strongest in GPT-2-small, Pythia-70M, and Llama-3.1-8B, where it survives residualization against magnitude-related confounds, and weaker in Gemma-2-2B. Held-out screening shows that ranking unseen features by predicted cleanliness can select features that steer more cleanly on fresh contexts, but the successful axis varies by setting: GPT-2 improves most cleanly, Pythia improves mainly on stability, Llama mainly on collateral, and Gemma only partially. A controlled Llama Scope width comparison shows that the predictive signal persists under a 32K-to-128K dictionary-width change, although the screening payoff becomes less stable. Overall, SAE steering side effects are predictable in advance, but the useful predictor signature and transferred modularity axis are model- and dictionary-setting dependent.

---


### 205. [An Information-Theoretic Definition for Open-Ended Learning](https://arxiv.org/abs/2606.08369)

**<font color=#1a73e8>作者：</font>** Wanqiao Xu, Yifan Zhu, Benjamin Van Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A growing body of work points to the great promise of AI systems that can continually expand their capabilities as they operate in an open-ended environment. But yet there is no coherent definition of open-endedness or theory about how an agent ought to explore an open-ended environment. We introduce an information-theoretic definition based on a new concept -- the ${\textit bit-equivalent}$ -- which quantifies the information required to attain each level of expected reward. We consider an environment to be open-ended if an agent can attain linear growth in the bit-equivalent. We establish that classical bandit environments are not open-ended and formulate a bandit environment that is. We also introduce an algorithm that achieves open-ended learning in this environment.

---


### 206. [SoK: Reconstruction Attacks on Synthetic Tabular Data (Insights from Winning the NIST CRC)](https://arxiv.org/abs/2606.08372)

**<font color=#1a73e8>作者：</font>** Steven Golob, Sikha Pentyala, Martine De Cock  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Synthetic data is increasingly promoted as a privacy-preserving substitute for releasing sensitive tabular records, yet its central adversarial threat ("reconstruction", the recovery of an individual's hidden attribute values from a synthetic release and a handful of known quasi-identifiers) has been studied only in scattered, hard-to-compare settings. We present the first systematization of reconstruction (equivalently, attribute inference) attacks on de-identified and synthetic tabular data. We contribute a taxonomy that organizes attacks by the structure they exploit; the most systematic empirical evaluation to date, pitting fourteen attacks against nine synthetic data generation (SDG) methods across five benchmark datasets; and a set of new attacks that fill gaps in the taxonomy, one of which (CoBP-RA) is the strongest attack we measure. Crucially, we introduce a methodology for interpreting what attack success means: a memorization test that distinguishes reconstruction of the population distribution from memorization of training records, and a reduction that places reconstruction and membership inference on a single comparable scale. Our findings: the choice of SDG method governs risk far more than the choice of attack; differential privacy protects mainly at small budgets ($\varepsilon\lesssim1$), above which protection plateaus, bounded by the synthesizer's capacity rather than its noise; de-identification methods are the most exposed; and most reconstruction reflects distributional structure rather than memorization, concentrating individual risk on atypical records. The attacks and infrastructure are externally validated by our first-place finish among all red teams in the 2025 \textit{National Institute of Standards and Technology} (NIST) Collaborative Research Cycle.

---


### 207. [Few-step Cofolding with All-Atom Flow Maps](https://arxiv.org/abs/2606.08375)

**<font color=#1a73e8>作者：</font>** Gianluca Scarpellini, Ron Shprints, Peter Holderrieth 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> All-atom generative modeling of 3D biomolecular complexes has emerged as the dominant paradigm for predicting the structure of proteins and protein-ligand systems. Generating structures at the atomic level of fidelity, however, typically requires expensive iterative diffusion rollouts, making both conventional deployment and inference-time search techniques computationally costly. In this paper, we introduce the Denoiser Cofolding All-Atom Flowmap (DeCAF) framework for distilling state-of-the-art all-atom cofolding models into all-atom flow maps that produce high-quality samples in only a few inference steps. We build DeCAF on a denoiser-based formulation of flow maps with endpoint losses that naturally support SE(3) rigid alignment, which we show is critical for training accurate models. We further derive a simple change of variables that lets DeCAF operate in the {\sigma}-space noise schedule of EDM-style architectures, enabling direct distillation from pretrained cofolding diffusion models. Equipped with DeCAF's flowmap lookahead, we introduce a purpose-built inference-time framework that improves sampling through reward-guided search. Empirically, DeCAF-Boltz statistically improves over Boltz-1x in both accuracy (RMSD) and physical validity scores of protein-ligand poses at strict NFE budgets on the challenging Runs N' Poses, while also showing a more optimal Pareto frontier across all inference compute budgets on PoseBusters. Distilling the state-of-the-art Pearl cofolding model, DeCAF-Pearl outperforms diffusion-based cofolding models and matches its teacher on success rate while using 5x fewer NFEs. We release our code at this https URL.

---


### 208. [TT-DAC-PS: Twin-Target Deterministic Actor-Critic with Policy Smoothing for Optimal Trade Execution](https://arxiv.org/abs/2606.08379)

**<font color=#1a73e8>作者：</font>** Ilia Zaznov, Atta Badii, Julian Kunkel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study addresses the optimal execution of large stock sell programs by introducing TT-DAC-PS (Twin-Target Deterministic Actor-Critic with Policy Smoothing), a deterministic actor-critic architecture that combines twin exponential-moving-average critic targets with pessimistic min backup, TD3-style target policy smoothing noise, delayed actor updates, and conservative Q regularisation to curb overestimation. Exploration uses Ornstein-Uhlenbeck (OU) noise with a hybrid schedule: deterministic episode-wise decay, variance-guided adjustment based on recent reward dispersion, and a Soft Actor-Critic (SAC)-style temperature that is learned and mapped to the noise scale. The environment integrates Almgren-Chriss (AC) trade impact with Limit Order Book (LOB) prices and volumes, normalised state features, per-step volume participation caps, and a utility-based reward. The trade execution algorithm is applied to LOB data for ten U.S. stocks. Performance is assessed against reinforcement-learning baseline algorithms, including Proximal Policy Optimisation (PPO), Soft Actor-Critic (SAC), and Advantage Actor-Critic (A2C), as well as alternative trade execution algorithms, including Time-Weighted Average Price (TWAP), Volume-Weighted Average Price (VWAP), and AC. The proposed model consistently reduces mean implementation shortfall percentage with competitive variance, outperforming classical baselines and standard reinforcement-learning benchmark models.

---


### 209. [STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control](https://arxiv.org/abs/2606.08382)

**<font color=#1a73e8>作者：</font>** Priyansh Bhatnagar, Ashkan Moradifirouzabadi, Se-Hyun Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank projection has emerged as a promising approach for compressing the KV cache by exploiting hidden-dimension redundancy. However, prior methods rely on fixed or heuristic rank selection and struggle to achieve aggressive compression with minimal accuracy degradation. We propose STAR-KV, an adaptive low-rank KV cache compression framework with fine-grained rank control. STAR-KV encompasses 1) a differentiable thresholding mechanism that enables optimal rank selection at both attention-head and block levels, 2) a hybrid decomposition strategy that applies different low-rank factorizations according to the sensitivity of key and value projections, and 3) a low-rank-aware mixed precision quantization that leverages data statistics for near lossless low-bit quantization. Evaluated across multiple LLMs and benchmarks, STAR-KV achieves up to 75% KV cache compression and up to 20x overall KV cache reduction when combined with quantization. Enabled by custom Triton-based GPU kernels, STAR-KV delivers up to 6.9x speedup for the attention module and 3.1x end-to-end generation throughput. Our code is publicly available at: this https URL.

---


### 210. [The Spectral Dynamics and Noise Geometry of Muon](https://arxiv.org/abs/2606.08388)

**<font color=#1a73e8>作者：</font>** Pierfrancesco Beneventano, Mahmoud Abdelmoneum, Tomaso Poggio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon replaces a matrix gradient $G=U\Sigma V^\top$ by its polar factor $UV^\top$. This keeps the singular directions selected by the gradient, but makes the update spectrum flat. We study the optimization bias created by this operation. Under explicit alignment assumptions, we prove that the polar update is the one-step entropy-maximizing choice among bounded updates that use the gradient singular directions and do not adapt to the current weight spectrum. In an underdetermined regression model, we derive exact singular-value dynamics for continuous-time Muon and identify a measurement-dependent condition under which the normalized spectrum moves toward equal nonzero singular values. This geometry also rules out a common low-rank interpretation: at fixed Frobenius norm, Muon's distinguished state has a flat spectrum, whereas nuclear-norm minimization favors spectral concentration. Controlled matrix-sensing experiments separate the effect from simple gradient rescaling, show that norm-matched gradient descent does not reproduce Muon, and recover the predicted flattening trend across broad ablations. In small NanoGPT pretraining, Muon preserves stable rank, has a broad learning-rate plateau, and improves validation loss relative to AdamW; in a matched small-ViT control, the ranking reverses. The resulting picture is regime-dependent: Muon is not universally superior, but its flat-spectrum bias can help when many spectral directions need to remain active.

---


### 211. [When Are Neural Interaction Discoveries Real? Identifiability, Recoverability, and a Pre-Fit Diagnostic](https://arxiv.org/abs/2606.08390)

**<font color=#1a73e8>作者：</font>** Valentina Kuskova, Dmitry Zaytsev, Michael Coppedge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When a neural time-series model reports that one variable modulates another's effect on a target, is the discovered interaction a property of the data or an artifact of model flexibility? We argue that this is fundamentally a question of identifiability, governed by the geometry of the observed input support rather than by the specific neural architecture. We study the problem in a multiplicative-gating extension of neural additive vector autoregression (GNAVAR), in which source contributions are modulated by other lagged variables. We show that representational capacity is not identifiability: dependent inputs induce leakage between edge-specific interaction terms, and low-dimensional support permits distinct interaction decompositions that agree on the observed data while differing elsewhere. We then prove a population identifiability theorem for normalized minimal GNAVAR decompositions under explicit support conditions, including settings with shared modulators. The theory yields a simple practitioner-facing diagnostic: the effective rank of the joint lag-block covariance predicts, before fitting, whether interaction recovery is feasible for a given candidate set. When the candidate set is unknown, a two-seed stability check provides a practical operational test. The same support condition organizes empirical outcomes into the three states predicted by the theory. Our results show that interaction recoverability depends on support geometry, that effective rank provides a practical pre-fit diagnostic, and that instability across independent fits is a characteristic signature of non-identifiable interaction discovery. The identifiability phenomenon, the support condition, and the instability signature are model-agnostic; GNAVAR is the vehicle that makes them provable.

---


### 212. [SceneConductor: 3D Scene Generation from Single Image with Multi-Agent Orchestration](https://arxiv.org/abs/2606.08402)

**<font color=#1a73e8>作者：</font>** Jeonghwan Kim, Yushi Lan, Yongwei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating complete 3D scenes from a single image requires inferring globally consistent geometry, object relationships, and environmental context from inherently ambiguous visual evidence. Despite recent progress in joint layout-and-mesh generation, existing methods often rely on holistic or weakly decomposed pipelines that entangle many factors at once and demand extensive scene-level supervision, limiting their generalization to complex real-world environments. We propose a multi-agent orchestration framework that decomposes single-image 3D scene generation into three structured stages: scene initialization, environment construction, and multi-agent refinement. The initialization stage extracts image-derived object masks, builds object-level 3D representations, and predicts an initial spatial layout to form a coarse 3D scene. The environment-construction stage then leverages this initialization together with point-map geometry to build an environmental scaffold of supporting surfaces, room boundaries, materials, and illumination. Finally, in the refinement stage, a planner agent identifies structural and visual inconsistencies, applies simple corrections directly, and dispatches specialist agents for complex localized revisions that are reintegrated into the global scene. To provide reliable structural initialization while reducing reliance on scene-level annotations, we further introduce a geometry-aware layout predictor supervised by sparse geometric priors derived from point maps. Unlike fully supervised layout generators, the predictor can be trained from segmentation-level data and generalizes robustly to diverse real-world scenes. Extensive experiments on benchmark datasets show that our method consistently outperforms prior approaches in geometric accuracy, spatial consistency, and perceptual realism.

---


### 213. [Hiding in Plain Floats: Steganographic Carriers for Indirect Prompt and Content Injection](https://arxiv.org/abs/2606.08403)

**<font color=#1a73e8>作者：</font>** Mudit Sinha, Sanika Chavan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Text-centered prompt-injection defenses assume that the malicious signal is visible in one of the inspected text views. We study a reproducible LLM01-style indirect prompt/content-injection failure mode where that assumption breaks: a payload caught in plain English slips past the same detector when it is transported as structured float parameters and reconstructed only as fragmented telemetry. Across 14,400 attacked real-model trials on three commercial LLM APIs from different providers, the IFS-derived float-array carrier preserves 94.3% leakage ASR under the strongest dual-layer text-classifier defense evaluated in the main matrix: a Prompt Guard 2 + TF-IDF ensemble; the same carrier-level pattern also replicates with a fine-tuned roberta-base detector. We emphasize leakage ASR because downstream systems may act on quoted or reproduced markers even when the model refuses, but Strong ASR is the stricter metric for structurally compliant attack success. A 2 x 2 ablation shows that data-layer storage and reconstruction-layer fragmentation defeat different text views and that both are needed to evade both. A simple xxd detector and semantic validation block the current T3 instance, so the contribution is not an undetectable exploit but a measured failure boundary for text-only inspection in structured-input pipelines that expose reconstructed auxiliary channels to an LLM.

---


### 214. [Geometry-Driven Flow Analysis of Brain Sulcal Pattern](https://arxiv.org/abs/2606.08404)

**<font color=#1a73e8>作者：</font>** Moo K. Chung, Luigi Maccotta, Aaron Struck  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cortical folding reflects coordinated neurodevelopmental processes and is increasingly recognized as a sensitive marker of neurological disease. However, most existing analyses rely on indirect scalar summaries that do not explicitly model folding geometry itself. In juvenile myoclonic epilepsy (JME), a common genetic epilepsy, cortical abnormalities are often subtle, spatially distributed, and difficult to detect using conventional morphometric measures. We introduce a Poisson-equation-based framework that models cortical folding as a geometry-driven flow derived from mean curvature on the cortical manifold. By treating folding patterns as a stationary source-sink structure, the proposed approach yields a smooth, globally balanced potential field whose surface gradient defines a physically interpretable flux. This framework enables spatially coherent analysis of sulcal-gyral folding organization and provides a principled representation of geometry-driven cortical structure in JME.

---


### 215. [Self-Evolving Scientific Agent Discovers Generalizable Physically-Reasoned Fluid Control](https://arxiv.org/abs/2606.08405)

**<font color=#1a73e8>作者：</font>** Boai Sun, Wenjin Guo, Zongmin Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While data-intensive deep reinforcement learning can optimize complex control policies, scientific discovery in physical systems fundamentally requires an interpretable chain of reasoning that connects physical evidence to structured control architectures. Here, we present a self-evolving scientific-agent workflow, driven by large language models and iterative code generation, that automates controller construction while preserving strict interpretability and rigorous physical reasoning. Instead of adjusting weights, the agent deploys candidate strategies into physical simulations, actively diagnoses dynamic behaviors from multimodal evidence, and translates these observations into progressive source-code refinements. We demonstrate this framework on a highly non-linear fluid-structure interaction problem: an underactuated, two-joint dogfish swimmer tasked with spatial target reaching using only joint angular accelerations. Starting from a propulsive seed policy that exhibits a one-sided steering bias, the agent autonomously discovers and refines a unified controller that robustly captures all canonical targets. Remarkably, without any retraining or target-specific branching, the synthesized control policy generalizes to unseen static targets and dynamically curved pursuit trajectories. The auditable evolve log reveals an emergent control architecture built upon traveling-wave propulsion, body-frame target guidance, yaw-rate feedback, signed mean-tail curvature, and adaptive cadence relief. Our results show that an autonomous scientific agent can successfully transform accumulated physical evidence into robust, mathematically readable control policy, while maintaining a fully traceable process of scientific discovery.

---


### 216. [Provably Efficient Personalized Multi-Objective Bandits with Proactive Conversational Queries](https://arxiv.org/abs/2606.08410)

**<font color=#1a73e8>作者：</font>** Linfeng Cao, Ming Shi, Ness B. Shroff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalized decision-making in multi-objective bandits requires learning user-specific trade-offs among competing objectives. Since arm utility depends on both unknown rewards and unknown preferences, existing methods infer preferences only from utility feedback, entangling preference learning with reward exploration. In practice, however, users often reveal their priorities through proactive conversational queries (e.g., "cheap and clean hotel"), yet this structured signal is not leveraged. We formalize a proactive query-based framework in which user queries provide structured preference signals. Modeling these signals via a Plackett-Luce subset choice model, we show that query-only learning is insufficient due to a fundamental shift-invariance barrier. To resolve this, we introduce MO-PQUCB, a hybrid algorithm that integrates query-based preference anchoring with bandit feedback through shift-invariant regularization and dual-exploration UCB. We prove that proactive queries accelerate preference estimation and yield improved regret scaling over prior preference-aware MO-MAB methods. Under corrupted queries, we further characterize statistical limits and design a robust estimator achieving near-optimal performance when the corruption is sparse. Experiments validate both theoretical and practical gains.

---


### 217. [CoVEBench: Can Video Editing Models Handle Complex Instructions?](https://arxiv.org/abs/2606.08415)

**<font color=#1a73e8>作者：</font>** Jiangtao Wu, Jiaming Wang, Yiwen He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent text-guided video editing models excel at elementary tasks (e.g., style transfer, object insertion), real-world user requests are highly compositional. A single prompt often demands multiple coupled edits, such as modifying subjects, actions, and camera views, while strictly preserving unrelated spatiotemporal content. Existing benchmarks, heavily constrained by isolated edits and coarse global metrics, fail to diagnose how models handle such complex workflows. To address this gap, we introduce CoVEBench, a compositional video editing benchmark comprising 416 curated source videos, 626 multi-point editing instructions, and 9,990 fine-grained checklist items. Covering diverse editing dimensions, CoVEBench evaluates models via MLLM-judged instruction compliance and video fidelity, alongside automated metrics for video quality. Extensive experiments reveal that compositional editing remains a profound challenge: current models frequently omit edits, violate preservation constraints, or introduce artifacts when handling multiple operations simultaneously. CoVEBench provides a challenging, diagnostic testbed to advance video editing toward realistic user workflows.

---


### 218. [Hacking Generative Perplexity: Why Unconditional Text Evaluation Needs Distributional Metrics](https://arxiv.org/abs/2606.08417)

**<font color=#1a73e8>作者：</font>** Antonio Franca, Alexander Tong  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion and continuous flow-based language models have emerged as the leading non-autoregressive alternatives to language modeling. Progress in both paradigms is overwhelmingly tracked by generative perplexity (gen-PPL): the per-token negative log-likelihood of samples under a frozen autoregressive (AR) scorer such as gpt2-large, typically paired with an empirical-entropy guardrail to rule out low-entropy collapse. We argue that this metric is unsound. By construction, gen-PPL measures only predictability under the scoring AR, not grammaticality or semantic coherence -- and the set of predictable but still low-quality sequences is combinatorially large. To make this concrete, we construct a suite of zero-parameter, deliberately naive samplers that achieve state-of-the-art gen-PPL on LM1B and OpenWebText at non-degenerate entropy, surpassing recently published diffusion and continuous-flow models while producing text that is incoherent by construction. We recommend evaluation suites that directly quantify the distributional divergence between generated and reference text, and use such a suite to re-benchmark recent non-autoregressive models, recovering a more faithful picture of the current state of the art.

---


### 219. [Segmentation-Assisted Brain MRI Synthesis with Cross-Image Multi-Contrast Feature Memory Bank Retrieval Augmentation](https://arxiv.org/abs/2606.08421)

**<font color=#1a73e8>作者：</font>** Wenwei Huang, Jia Wei, Jianlong Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-contrast brain MRI provide complementary soft-tissue characteristics that aid in the screening and diagnosis of diseases. However, limited scanning time, image corruption and various imaging protocols often result in incomplete multi-contrast images. While current approaches excel in image synthesis, they often struggle to synthesize critical tumor regions and exploit contextual information in multi-contrast brain MRI effectively. To address this issue, we propose a synthesis-centric, segmentation-assisted closed-loop framework with retrieval augmentation synthesis. Our method overall takes a generative adversarial architecture, which aims to synthesize missing contrasts from any combination of available ones with a single model. To explicitly capture tumor semantics and focus synthesis on tumor regions, we add an auxiliary segmentation branch that predicts tumor masks and feeds them back as semantic conditioning in synthesis branch, thereby learning tumor-aware representations in the model and improving synthesis fidelity. Furthermore, we propose a dual-bank retrieval augmentation strategy. It dynamically queries two external knowledge bases, namely a tumor masks memory bank for crucial tumor context and cross-image contrast feature memory bank for global style information, to augment synthesis. Verified on two public multi-contrast magnetic resonance brain datasets: BraTs2020 and UCSF-BMSR, the proposed method is effective in handling medical brain images synthesis tasks and shows superior performance compared to previous methods. Code is available at:this https URL

---


### 220. [CritLens: Visual Analytics for Criteria Discovery in Review-Based Decision Making](https://arxiv.org/abs/2606.08426)

**<font color=#1a73e8>作者：</font>** Hongjia Wu, Shuai Zhou, Hongxin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present CritLens, a visual analytics system that helps users build personalized multi-criteria decision models from review text. In everyday decisions -- choosing equipment, hotels, or restaurants -- evaluation criteria are either preset by platforms or generated by LLMs, leaving users unable to discover, adjust, or verify them against the underlying evidence. This is problematic because many preferences are latent: they surface only upon encountering specific reviews, and any fixed framework risks overlooking low-frequency but decisive details. CritLens addresses this gap by using LLMs to transform reviews into an initial AHP decision model, then supporting iterative, human-in-the-loop refinement. Through coverage gap detection in the embedding space, users discover criteria missed by the initial model; through interactive weight adjustment under AHP consistency constraints, they express personal priorities; and through a multi-level scorecard and exportable decision report, they trace every ranking back to the original review text. Two case studies, an eight-participant user study, and a quantitative consistency-repair experiment demonstrate the system's effectiveness.

---


### 221. [AI Code Sandboxes: A Comparative Security Study. Part 1 of 2 -- Engine-Level Properties (Attack Surface, Leakage, Stackability, CVE History, Patch Cadence, Fuzzing)](https://arxiv.org/abs/2606.08433)

**<font color=#1a73e8>作者：</font>** George Andronchik, Pavel Lokhmakov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper reads six engine-level measurements together -- 1.1 host attack surface, 1.2 information leakage, 1.3 defense-in-depth stackability, 1.4 public CVE history, 1.5 patch cadence, and 1.6 upstream fuzzing posture -- to describe how five AI-sandbox products isolate guest code from the host kernel. No single axis is a sufficient basis for a comparative judgement; the cross-axis reading is the load-bearing analysis.
Three high-level findings: (1) engine classes (microVM, userspace kernel, OCI container) separate cleanly on every architectural axis, but products within a class do not; (2) product pin policy is the dominant operator-facing variable -- engine-side patch latency aggregates to ~0 days for coordinated disclosures, while downstream lag spans 0 days to 471+ days to "opaque" to infinity; (3) fuzzing investment splits into three tiers, and the strongest combination -- microVM x continuous public fuzzer -- is unoccupied in this set, leaving the "0 published CVEs x no upstream fuzzer x no academic study" intersection structurally unmeasured.
We report per-axis orderings, per-product portraits, and a threat-model qualification matrix; no overall ranking is proposed. Companion repository (code, Apache-2.0): this https URL. License: CC BY 4.0.

---


### 222. [Reinforcing Temporal Answer Grounding in Instructional Video via Candidate-Aware Causal Reasoning](https://arxiv.org/abs/2606.08436)

**<font color=#1a73e8>作者：</font>** Muge Qi, Rong Fu, Pengbin Feng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The task of temporal answer grounding in instructional video (TAGV), which aims to locate precise video segments that respond to natural language queries, is increasingly important for direct video answer retrieval. This task remains challenging due to the need to comprehend semantically complex questions and to address the significant length mismatch between untrimmed videos and short target moments. Existing methods often suffer from sensitivity to irrelevant content or insufficient visual reasoning capabilities. To tackle these limitations, we propose a Candidate-Aware Causal Reasoning (CACR) framework. Our approach first employs a Visual-Language Pre-training based Candidate Selection (VBCS) algorithm to efficiently generate K candidate segments, then applies a temporal logic reasoning module enhanced by a rejection reward mechanism and optimized via Group Relative Policy Optimization (GRPO) for robust inference. Extensive experiments on six benchmarks demonstrate that our method achieves state-of-the-art performance in terms of mean Intersection-over-Union (mIoU), providing a new perspective for reasoning-based retrieval in long videos.

---


### 223. [Comparing Controller-Free Pointing Techniques Across Depth for 2D Selection in Augmented Reality](https://arxiv.org/abs/2606.08441)

**<font color=#1a73e8>作者：</font>** Samiha Sultana, J. Felipe Gonzalez, Robert J. Teather  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents a systematic evaluation of five controller-free pointing techniques for 2D target selection in AR, using ISO 9241-411. We compared them across multiple depths (2 m, 6 m, 10 m) in terms of movement time, accuracy, throughput, and workload (NASA TLX). Head- and eye-based pointing significantly outperformed the hand-based methods (Finger, Wrist, and Arm); Head input was the most accurate and remained the most consistent across depth. Depth significantly impacted performance, with complex interactions with target size and distance. Our results offer a comprehensive empirical basis for selecting appropriate controller-free techniques in depth-varying AR tasks.

---


### 224. [Segment-level Tree Search for Long Meeting Document Summarization](https://arxiv.org/abs/2606.08445)

**<font color=#1a73e8>作者：</font>** Sangwon Ryu, Heejin Do, Jun Seo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Meeting documents are challenging to summarize due to their length and complex conversational structure. Existing approaches typically adopt multi-stage pipelines that extract information prior to summarization; however, these approaches often suffer from cumulative error propagation without intermediate validation, a limitation further amplified by short and low-quality reference summaries. We propose segment-level summarization via Monte Carlo Tree Search (S3), a training-free framework that constructs a final summary by composing segment-level summary candidates. S3 partitions a long document into segments and generates multiple summary candidates per segment, forming nodes of a search tree. The best-scoring combination is selected via self-reward-guided tree search and refined into the final output. Despite using a 7B model, S3 achieves performance comparable to larger 72B models while producing length-appropriate summaries.

---


### 225. [Not Just After One: Sleep-Inspired Replay Prevents Catastrophic Forgetting After Sequential Tasks](https://arxiv.org/abs/2606.08447)

**<font color=#1a73e8>作者：</font>** Anthony Bazhenov, Jean Erik Delanois, Giri P. Krishnan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the critical limitations of artificial neural networks is their lack of ability to continually learn: training on new tasks often leads to interference and forgetting of the previous ones. While several algorithms have been proposed to protect old memories from interference, they are typically applied during or immediately after each new episode of training. In contrast, humans and animals can learn continuously, acquiring multiple new memories during active learning before consolidating all of them into long-term storage. Here we show that multiple new tasks can be trained sequentially before an unsupervised sleep-like replay phase is applied to partially restore performance across all previously learned tasks. Our study further suggests that task-specific information remains resilient to new training but decays gradually as network is trained on new tasks. These findings point to novel principles for developing a broad range of continual learning AI solutions.

---


### 226. [Theoretical Foundations of Continual Learning via Drift-Plus-Penalty](https://arxiv.org/abs/2606.08452)

**<font color=#1a73e8>作者：</font>** Nazreen Shah, Govinda Arya, Bharath B.N. 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many real-world settings, data streams are nonstationary and arrive sequentially, requiring learning systems to adapt continuously without retraining from scratch. Continual learning (CL) addresses this challenge by incorporating new tasks while mitigating catastrophic forgetting, where learning new information degrades performance on previously acquired knowledge. We introduce a control-theoretic perspective on CL that explicitly regulates the evolution of forgetting, framing adaptation as a controlled process subject to long-term stability constraints. We focus on replay-based CL, where a finite memory buffer stores representative samples from prior tasks. We propose COntinual Learning with Drift-Plus-Penalty (COLD), a continual learning framework based on the Drift-Plus-Penalty (DPP) principle from stochastic optimization. To facilitate analysis, we also consider an oracle variant, COLD-ORACLE, as a reference benchmark. At each task, both methods minimize the current task loss while maintaining a virtual queue that tracks deviations from long-term stability on previously learned tasks, capturing the stability-plasticity trade-off as a regulated dynamical process. We establish stability and convergence guarantees that characterize this trade-off through a tunable control parameter. Experiments on standard benchmarks demonstrate that COLD consistently outperforms a broad range of state-of-the-art CL methods while providing competitive and controllable forgetting behavior through explicit regulation of stability and plasticity.

---


### 227. [The Confidence Trap: Calibration Attacks for Graph Neural Networks](https://arxiv.org/abs/2606.08467)

**<font color=#1a73e8>作者：</font>** Cuong Dang, Jiahao Zhang, Hieu Ta Quang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While confidence calibration is essential for trustworthy decision-making in safety-critical applications, the robustness of calibrated GNNs to adversarial structural perturbations remains largely unexplored. However, studying calibration attacks on graphs presents unique technical challenges: (1) the discrete nature of graph structures complicates gradient-based optimization, (2) existing underconfidence objectives fail to drive predictions toward uniform distributions, and (3) GNNs are highly sensitive to edge perturbations, often causing unintended label changes that violate attack constraints. To address these challenges, we propose a \textbf{Unified Graph Calibration Attack (UGCA)} framework designed for \textbf{worst-case (white-box) analysis} of GNN calibration robustness. UGCA introduces a KL-divergence loss to encourage uniform predictive distributions, a reranking mechanism to reduce label flipping, a hybrid loss to recover labels when violations occur, and beam search to explore a broader adversarial search space. We further provide theoretical insights linking model generalization, dataset complexity, and calibration vulnerability, showing that models with higher accuracy or trained on datasets with more classes are more susceptible under this threat model. Extensive experiments demonstrate that UGCA substantially increases Expected Calibration Error while preserving classification accuracy. Our code is publicly available at this https URL.

---


### 228. [More Yap Less Meaning: Uncovering Self-Improvement Behavior in SLMs](https://arxiv.org/abs/2606.08471)

**<font color=#1a73e8>作者：</font>** Marina Igitkhanian, Erik Arakelyan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recently, language models have made rapid progress across various domains and applications. However, their capability for self-improvement, i.e., whether they are adept at recognising and correcting flaws in their own reasoning, remains dubious. In this study, we address this question by constructing a sufficiency test to rigorously examine the self-correction capabilities of small language models (SLMs). We propose a minimal three-step self-correction pipeline that collects initial SLM answers, prompts the same model to generate hints for its incorrect responses given the ground truth, and feeds the model the same question with its own feedback to refine the initial answer. We evaluate a variety of instruction-tuned and reasoning SLMs in this experimental setup on arithmetic and logical reasoning benchmarks. Our findings show that SLMs with injected hint sentences yield only a 4.4 percent gain over initial question-answering accuracy. Even though the correct answer was provided alongside the model's incorrect reasoning, the evaluated SLMs fail to understand what was missing in their reasoning and show minimal semantic difference between hints that lead to corrections and ones that do not. Furthermore, our experiments show that longer hints are positively correlated with incorrect final answers, suggesting that longer deliberation on problems can hinder the reasoning process, meaning that SLMs do not necessarily scale in performance with a larger compute budget.

---


### 229. [Digital White Spaces: A Cyberpsychology-Informed Framework to Mobile Phone Addiction](https://arxiv.org/abs/2606.08472)

**<font color=#1a73e8>作者：</font>** Leandros Maglaras, Helge Janicke, Konstantinos Karantzalos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile-phone overuse and attention fragmentation have become pressing societal and public-health concerns. Cyberpsychology research highlights addictive engagement loops driven by intermittent rewards, persuasive design, and habit formation. In this editorial I synthesize current evidence on mobile-phone addiction and propose "Digital White Spaces" (DWS), a socio-technical framework that combines privacy-preserving monitoring, AI-driven detection of addictive loops, device-mode interventions, and physical signal-limited zones to restore cognitive autonomy.

---


### 230. [A Variability-Based Framework for Interpretable Naming in Formal and Relational Concept Analysis](https://arxiv.org/abs/2606.08477)

**<font color=#1a73e8>作者：</font>** Alain Gutierrez, Marianne Huchard, Pierre Martin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge extraction from symbolic data often produces abstractions that are formally defined but not immediately interpretable by users. Formal Concept Analysis (FCA) and Relational Concept Analysis (RCA) provide representative settings for this issue: they generate explicit conceptual structures, implications, and relational dependencies from object descriptions and relations. Although these structures are explainable by design, their concepts are often identified by technical labels, which limits their use as human-interpretable knowledge units. Assigning meaningful names to such concepts is therefore a key issue for interpretation, navigation, validation, and reuse by domain experts.
This paper investigates concept naming in FCA and RCA from a symbolic knowledge representation perspective. We first characterize the linguistic and terminological challenges involved in naming generated symbolic abstractions, including ambiguity, discrimination, concision, and consistency across related concepts. We then propose a configurable framework for LLM-assisted concept naming. The framework relies on a variability model that controls which sources of information are exposed during naming, such as intent, extent, inherited information, neighboring concepts, implications, and relational attributes. It thereby makes explicit the semantic choices involved in moving from formal concept descriptions to human-readable names.
The approach is illustrated as a proof of concept on a small relational dataset in the pizzeria domain. This illustration shows how different configurations influence the names suggested by an LLM, and how naming variability can reveal interpretation choices, relational dependencies, and possible modeling issues in the underlying symbolic data.

---


### 231. [Inferring hidden forcing in a biological oscillator using Kolmogorov-Arnold networks](https://arxiv.org/abs/2606.08479)

**<font color=#1a73e8>作者：</font>** Julian Szereszewski, Facundo Fainstein, Leandro E. Fernandez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring the forces that drive a dynamical system from partial observations is a fundamental challenge across physics, particularly when distinct underlying mechanisms produce similar observable dynamics. Here we show that the effective muscular forcing underlying avian respiratory dynamics can be reconstructed from measurements of air-sac pressure alone. Using an interpretable learning framework based on Kolmogorov-Arnold networks, we infer the governing equations of the system directly from data and uncover a nontrivial structure in the underlying forcing that is not apparent from the pressure signal, which instead suggests a relaxation-like oscillation. The reconstructed dynamics predict a two-phase activation pattern within each respiratory cycle, which we independently validate through electromyographic recordings of expiratory muscles. These results demonstrate that data-driven reconstruction of dynamical laws can reveal hidden physical structure and provide access to unobserved driving variables, establishing a general route to infer latent forces in partially observed dynamical systems.

---


### 232. [Adaptive Loss Balancing for Noise-Robust GRPO in Generative Recommendation](https://arxiv.org/abs/2606.08480)

**<font color=#1a73e8>作者：</font>** Kewei Xu, Junbo Qi, Yanyan Zou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) presents a promising avenue for enhancing generative recommendation beyond supervised imitation, leveraging reward signals to guide policy improvement. However, its efficacy is critically contingent on the trustworthiness of the reward model for the samples it evaluates. In practice, production rankers, the widely adopted reward models, are trained on exposure-biased logs, leading to sample-dependent inaccuracies that violate this assumption. Our stratified analysis uncovers a consistent pattern: reward guidance is most beneficial when the policy exhibits uncertainty and the ranker can effectively discriminate the ground-truth item from rollout negatives. On other samples, the reward signal is either negligible or detrimental, highlighting the risk of uniform RL application. To address such an issue, we introduce AdaGRPO, a novel framework that treats reward-guided optimization as selective admission rather than uniform pressure. Training is anchored in supervised negative log-likelihood, while the GRPO objective is gated by a binary, per-sample clip determined by two rollout diagnostics: policy-side difficulty and reward discriminability. Instances failing either diagnostic default to pure supervision, ensuring stability and mitigating the amplification of noisy gradients. We validate AdaGRPO on a large-scale e-commerce dataset. At the best intermediate checkpoint, it elevates HR@10 from 11.01% to 12.18% while constraining hallucination below 0.22%, and maintains robustness at the final checkpoint (HR@10 11.63%, hallucination 0.27%), outperforming fixed NLL--GRPO mixtures across the retrieval--validity frontier. In production A/B tests, AdaGRPO achieves statistically significant gains in click-through rate and dwell time, confirming its practical utility.

---


### 233. [PIPE-Cypher: Automatic Enterprise Benchmark Generation for Text-to-Cypher Systems](https://arxiv.org/abs/2606.08481)

**<font color=#1a73e8>作者：</font>** Suraj Ranganath, Anish Raghavendra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enterprise property graphs vary widely in schema structure, internal terminology, domain assumptions, governance constraints, and user interaction patterns. A deployment-relevant Text2Cypher benchmark therefore reflects the questions users and agents actually ask of that graph. Creating such a benchmark is difficult because schemas and values are unique, and graph structure changes over time. Each NL-query pair must also be executable, use real graph entities, preserve diversity, and remain balanced across query types and difficulty levels. We present PIPE-Cypher, a local benchmark-generation pipeline that turns a live property graph and optional seed queries from customer questions, analyst logs, or agent tool calls into balanced NL-to-Cypher benchmarks. PIPE-Cypher combines schema profiling, reverse-query grounding, constrained generation, deterministic Cypher governance, execution validation, redaction, diversity controls, and a calibrated local LLM judge. Using local Qwen3.5-9B generation and judging, PIPE-Cypher exports 3,000 accepted FinBench/SNB examples, completes three audited ablation suites, calibrates judge behavior with human labels, and evaluates 11 local downstream models. The resulting benchmark is deliberately discriminative: zero-shot transfer is weak, while a few-shot control shows that schema-specific example banks can help compatible model families. Together, PIPE-Cypher makes Text2Cypher benchmarking a repeatable process that evolves with the graph, its users, and its target workloads.

---


### 234. [What Makes a Desired Graph for Relational Deep Learning?](https://arxiv.org/abs/2606.08491)

**<font color=#1a73e8>作者：</font>** Yao Cheng, Siqiang Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Relational deep learning (RDL) converts relational databases (RDBs) into heterogeneous graphs, but graphs derived directly from database schemas are often not well suited for how graph neural networks (GNNs) perform relational reasoning. We study what makes a relational graph suitable for deep learning and show that schema-derived graphs suffer from two systematic failures: information overload and semantic fragmentation. Our empirical analysis reveals that the desired graph is not the raw schema, but a result of controlled structural adaptation. Performance depends on balancing two operations: mitigating information overload via filtering, and repairing semantic fragmentation via injection. Specifically, filtering serves as a bias-variance knob with non-monotonic effects, while injection improves performance only when it explicitly restores the relational dependencies missing from the original schema. Based on these findings, we develop an end-to-end structural optimizer that applies both operations to adapt relational graphs automatically. Across 26 tasks spanning classification, regression, and recommendation, the optimized graphs consistently improve accuracy while often reducing inference cost.

---


### 235. [Standpoint Logics with Defeasible Beliefs](https://arxiv.org/abs/2606.08503)

**<font color=#1a73e8>作者：</font>** Nicholas Leisegang, Thomas Meyer, Sebastian Rudolph  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we integrate the defeasible logic of Kraus, Lehmann and Magidor (KLM) with the standpoint logic framework of Gómez Álvarez and Rudolph. This is done with the goal of formally expressing knowledge taking into account multiple (possibly contradicting) viewpoints, which in turn may hold defeasible beliefs. In doing so, we utilise Defeasible Restricted Standpoint Logics (DRSL), introduced by Leisegang et al. Our work expands on previous work by providing a foundational representation result for DRSL semantics and systematically lifting several well-known entailment relations from the propositional case to the standpoint-enhanced setting. In particular, we characterise the semantics for DRSL through a set of KLM-style postulates adapted for the standpoints case. We furthermore provide a means to lift preferential entailment, and the class of entailment relations based on single ranking functions from the purely propositional to the standpoint-enhanced context, including rational and lexicographic closure. We show this can be done equivalently through semantic and algorithmic means. Furthermore, we show that, for each considered form of entailment, the complexity class of entailment checking does not change when moving from propositional KLM to DRSL.

---


### 236. [OmniTryOn: Video Try-On Anything at Once!](https://arxiv.org/abs/2606.08514)

**<font color=#1a73e8>作者：</font>** Changliang Xia, Chengyou Jia, Minnan Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although video virtual try-on (VVT) has achieved significant progress, existing methods still exhibit two fundamental limitations: first, they are restricted to single-garment transfer, rendering simultaneous multi-object try-on highly impractical; second, their heavy reliance on explicit external priors (e.g., garment masks) inevitably destroys crucial physical dynamics and degrades visual quality. To bridge this gap, this paper proposes the novel Try-On Anything task, which aims to simultaneously transfer diverse wearable objects onto a person in a video in a single inference pass. To support and standardize this paradigm, we introduce TryAny-Bench, a comprehensive benchmark encompassing a paired video dataset alongside a tailored evaluation protocol. Furthermore, we present OmniTryOn, an external-prior-free generative framework designed to tackle this task. Specifically, OmniTryOn employs a First Frame Wearable Cache strategy, which directly provides diverse wearable objects for the generation process through the initial video frame. To maintain consistency, we propose the Spatiotemporally Consistent RoPE (STC-RoPE), which inherently establishes robust spatiotemporal anchors to strictly preserve complex human motions and background dynamics. Optimized by the proposed Gradual Try-On (GTO) training strategy, our model progressively masters robust multi-object synthesis. Extensive experiments on TryAny-Bench demonstrate that OmniTryOn significantly outperforms existing specialized video virtual try-on models and general video editing baselines, establishing a powerful new standard for the Try-On Anything task. Our dataset, code, and models are available at this https URL.

---


### 237. [A Joint Finite-Sample Certificate for Adaptive Selective Conformal Risk Control](https://arxiv.org/abs/2606.08517)

**<font color=#1a73e8>作者：</font>** Xiaoli Yu, Jiamiao Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selective predictors answer on confident inputs and abstain elsewhere; deploying one safely needs a single finite-sample certificate that simultaneously upper-bounds the selected risk, lower-bounds the acceptance probability $\pacc$ above a floor $\pmin$, and lower-bounds the deployment utility. This certificate must be valid under adaptive threshold selection from a finite grid of $m$ pairs on $\ncert$ samples. We give such a certificate for bounded, possibly non-monotone losses by treating the selected risk directly as a ratio rather than through a Hoeffding-style range bound. The construction couples three confidence bounds: a variance-adaptive empirical-Bernstein bound on the ratio risk, a Clopper--Pearson bound on acceptance, and a two-sided closeness bound on utility. Together they lower-bound the certified policy's utility absolutely and to within $2\gammau$ of the best over the \emph{certified set}, both non-vacuous whenever feasible; a regime-scoped third leg matches an external oracle, informative only where the risk margin $\gammar < \alpha$ and vacuous at the headline operating points. Relative to the range-only Hoeffding-ratio construction this sharpens the acceptance-floor dependence from $1/\pmin$ to $1/\sqrt{\pmin}$, and a closed-form corollary identifies a per-pair regime in which our risk bound dominates a Hoeffding conformal risk control (Hoeffding--CRC) selective bound. Empirically, on ImageNet (three ResNets) and COCO val 2017 panoptic, the certificate opens a $+22$ pp certified-acceptance frontier over Hoeffding--CRC and is ${\approx}10{\times}$ tighter than a non-vacuous matched-valid baseline; these gains are regime-scoped, not universal, and absent on ADE20K. The certifier runs in $O(\ncert m)$ time.

---


### 238. [Exploring CKKS Parameter Trade-offs for Privacy-Preserving Personalized Federated Learning](https://arxiv.org/abs/2606.08521)

**<font color=#1a73e8>作者：</font>** Kamolchanok Saengtong, Phanwadee Sinthong, Norrathep Rattanavipanon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving Personalized Federated Learning (PFL) enables clients to collaboratively train personalized models without exposing raw data, but exchanged model updates remain vulnerable to inference attacks from honest-but-curious servers. Homomorphic Encryption (HE) addresses this by allowing server-side aggregation directly on encrypted updates, with the CKKS scheme being particularly suitable due to its native support for approximate floating-point arithmetic. However, no prior work has examined how to configure CKKS for PFL deployments, leaving practitioners without principled guidance on parameter selection that directly affects privacy, precision, and computational cost. This paper presents pFedCKKS, a generic framework integrating CKKS into PFL, and provides the first systematic parameter selection guide for practitioners. We derive the full CKKS parameter constraints under 128-bit security for the PFL setting, showing the selection problem reduces to choosing just two values: the inner and outer ciphertext prime. Implemented using the Flower framework and TenSEAL library, pFedCKKS is evaluated on the FEMNIST, CelebA and Sentiment140 datasets with FedFinetune, Ditto and FedPer which represents PFL algorithms. Experimental results reveal an empirical trade-off between precision and computational/communication costs. This allows us to draw a concrete guideline for selecting proper CKKS parameters that balance efficiency and accuracy in real-world deployments of pFedCKKS.

---


### 239. [DriveReward: A Comprehensive Dataset and Generative Vision-Language Reward Model for Autonomous Driving](https://arxiv.org/abs/2606.08525)

**<font color=#1a73e8>作者：</font>** Qimao Chen, Fang Li, Yuechen Luo 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward models play a pivotal role in reinforcement learning (RL) and multi-modal trajectory selection for autonomous driving. However, acquiring such rewards typically relies on hand-crafted rule-based objectives or perception ground truth, which hinders generalization for data-scaling. While Vision-Language Models (VLMs) have demonstrated feasibility as reward models in other domains, their effectiveness in driving tasks remains underexplored. In this work, we bridge this gap by (1) introducing DriveReward, a reasoning trajectory evaluation dataset rigorously labeled via temporally-grounded visual guidance, and augmented with counterfactual driving behaviors., (2) alongside a specialized Vision-Language Reward Model. To address the scarcity of failure cases in conventional datasets, we propose a counterfactual data annotation scheme to construct cases encompassing diverse driving styles and erroneous behaviors. Evaluations on our proposed benchmark reveal that even leading open-source and proprietary VLMs fail to excel across all tasks, highlighting significant room for improvement in existing models. Building on these findings, we subsequently tailor a specialized 1B reward model that outperforms larger VLMs on task-specific reward alignment. Finally, we validate our reward model's effectiveness by integrating it into RL finetuning and multi-modal trajectory scoring across multiple baselines, achieving performance comparable to rule-based reward calculations in both open-loop and closed-loop evaluation.

---


### 240. [Scaffold Effects on GAIA: A Controlled Comparison](https://arxiv.org/abs/2606.08529)

**<font color=#1a73e8>作者：</font>** Jason Starace  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Published agent capability scores conflate what a model can do with what its scaffold lets it do, and the magnitude of this elicitation gap is not well characterized under controlled conditions. This study executes a pre-registered controlled comparison of three scaffolds (ReAct, a Planner-Actor-Rater multi-agent design, and planner-then-executor) across five models from three providers (Claude Opus 4.7, Sonnet 4.6, Haiku 4.5; Gemini 3.1 Pro Preview; GPT-5.5) on GAIA validation Levels 1 and 2, holding tasks and conditions fixed, with three attempts per question. Scaffold choice alone moves measured accuracy by as much as 28 percentage points within a single model (Opus, Level 2, robust slice), confirming the pre-registered hypothesis that scaffold variation produces gaps of at least 10 points. The pre-registered prediction that more capable models would be less scaffold-sensitive is rejected in direction: scaffold effects vary significantly by model in every dataset slice, but the most capable Anthropic model gains the most from structured scaffolds at the harder level, and tier-scaling holds only at Level 1 under the robust slice. The multi-agent advantage over ReAct at Level 2 appears within the Anthropic family but not for the cross-provider models, making model family rather than capability tier the conditioning variable, and the predicted planner-executor advantage on file-reading tasks is falsified. Structured scaffolds make fewer tool calls yet recover more often from mid-trajectory errors at the harder level, and a single cell (Gemini with planner-then-executor) is the cheapest at both levels and the most accurate at Level 2. These results indicate that single-scaffold capability numbers are scaffold-conditional estimates and that the elicitation gap is not guaranteed to shrink as models improve.

---


### 241. [Autonomous Aerial Manipulation via Contextual Contrastive Meta Reinforcement Learning](https://arxiv.org/abs/2606.08533)

**<font color=#1a73e8>作者：</font>** Lixuan Jin, Bingxuan Lan, Xinyi Bao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicles (UAVs) are increasingly being deployed in logistics, service robotics, and other real-world applications, creating a growing demand for autonomous payload acquisition and delivery. Existing approaches typically assume pre-attached payloads or rely on specialized grippers, leaving versatile end-to-end aerial delivery largely unresolved, where different payloads induce highly variable flight dynamics, requiring a single policy to adapt online without manual calibration or explicit system identification. To this end, we study \textbf{A}utonomous \textbf{A}erial Manipulation via \textbf{Co}ntextual \textbf{Co}ntrastive Meta Reinforcement Learning (\textbf{\textit{Aco2}}), a fully autonomous aerial delivery setting in which a quadrotor equipped with a lightweight hook continuously picks up, transports, and delivers diverse handle-equipped objects between randomized locations, all without human intervention. First, we design a contextual observation encoder that infers a compact latent context from recent interaction history, enabling the policy to adapt online to payload-dependent dynamics. To further improve the quality of this context, we introduce a contrastive objective that structures the context embedding around task-relevant variations, improving generalization across diverse payloads without requiring explicit system identification. Trained entirely in simulation with extensive domain randomization, \textit{Aco2} can be directly deployed on a physical quadrotor without real-world fine-tuning.

---


### 242. [NGram-MoSE: Efficient Remote Sensing Super-Resolution via N-Gram Context and Mixture-of-Experts](https://arxiv.org/abs/2606.08535)

**<font color=#1a73e8>作者：</font>** Yun-Hsuan Huang, Trong-An Bui, Chih-Hung Chuang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing applications for environmental monitoring and disaster management are frequently constrained by a spatial--temporal trade-off: imagery with fine spatial detail is often acquired less frequently, whereas more temporally available observations are typically coarser. Single-image super-resolution provides a practical means to enhance coarse imagery without changing acquisition schedules, yet many Transformer-based SR models remain computationally expensive and can be sensitive to limited or geographically biased training data, which degrades robustness under out-of-distribution conditions. This paper presents NGram-MoSE, a lightweight Transformer architecture designed to improve both efficiency and texture continuity. NGram-MoSE introduces N-Gram Context Injection to strengthen cross-window local consistency and mitigate window-boundary artifacts, and incorporates a Mixture-of-Experts (MoE) feed-forward design to scale capacity through sparse activation without proportional growth in inference cost. Experiments on a geographically disjoint OOD test set show that NGram-MoSE achieves 31.68\,dB PSNR while reducing FLOPs by \(14\times\) relative to a heavyweight Transformer reference. Downstream evaluation on a landslide segmentation benchmark further demonstrates that restoring degraded inputs to the detector training scale improves performance, yielding a 4.47\% absolute gain in mAP@50 over bicubic upsampling, and exhibits stronger cross-scale consistency under scale extrapolation. These results indicate that NGram-MoSE provides an effective SR module for resource-constrained remote sensing pipelines requiring robust generalization.

---


### 243. [Routine laboratory trajectories encode the onset of organ-level complications in cancer](https://arxiv.org/abs/2606.08538)

**<font color=#1a73e8>作者：</font>** Jannik Lübberstedt, Krischan Braitsch, Jacqueline Lammert 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routine laboratory panels drawn during cancer treatment constitute longitudinal physiological recordings of organ function, yet their temporal structure is discarded by single-timepoint prognostic tools. A transformer trained on 2,777,595 laboratory measurements from 3,905 patients with multiple myeloma or ovarian cancer predicted the two-year onset of 162 treatment-associated complications, including therapy-related myelodysplastic syndromes, spanning eight clinical categories, achieving 1.5- to 6.1-fold enrichment above prevalence at the group level. It matched or outperformed non-sequential baselines across grouped endpoints (AUROC gains up to +0.11), demonstrating that longitudinal laboratory trajectories capture evolving complication-specific physiology inaccessible from isolated measurements. Predictions generalised across both cancers, divergence concentrating in disease-specific complications, and biomarker masking recovered signatures consistent with established pathophysiology. External validation on MIMIC-IV and MMRF CoMMpass confirmed transferability across independent healthcare systems (AUROC up to 0.85). Routine oncological laboratory data encode organ deterioration weeks to months before clinical onset, enabling complication-specific surveillance without additional testing infrastructure.

---


### 244. [AgentTrust: A Self-Improving Trust Layer for AI-Agent Actions](https://arxiv.org/abs/2606.08539)

**<font color=#1a73e8>作者：</font>** Chenglin Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly take consequential actions -- shell commands, cloud operations, and arbitrary tool-calls -- so a trust layer must decide, per action, whether to allow, warn, block, or escalate. We argue that the right way to reason about such a layer is by threat type. Lexical (fixed-signature) threats, where danger lives in a stable token, are decidable by deterministic rules; semantic (intent-dependent) threats, where a benign and a malicious action share the same surface, are out of reach for rules by construction. We make this concrete with a negative proof: a determined, hand-authored cloud rule pack lifts held-out accuracy only 48 to 56% overall and moves the semantic categories by 0pp (data_db 29 to 29, observability 59 to 59, supply_chain 50 to 50), while a strong LLM judge carries exactly those categories. We give the judge a self-learning capability: on a corpus that is mainly semantic attacks it nearly doubles rule accuracy (48% to 83.6-85.2%) with near-zero false-blocks, and this holds across two model providers. We turn this into a self-improving dual-store system: the judge distills a growing deterministic rule floor on lexical threats (cheaper over time) and feeds a guarded RAG memory on semantic threats (a verdict-cache fails -- surface-twins collapse to ~58% -- so a corroboration guard lifts semantic accuracy +13pp, 70 to 84). The result is what sets AgentTrust v2 apart from its static v1 predecessor: a trust layer that self-evolves from its own stream of decisions -- cheaper on the lexical class (it distils its own rules) and smarter on the semantic class (it accrues guarded precedent), while never hard-blocking a benign action. An end-to-end online replay shows the judge-call rate falling (50% to 44%) and judge-domain accuracy rising (71% to 80%), with 0 benign hard-blocks across 45,000 actions.

---


### 245. [Quantitative Promise Theory: Intentionality and Inference in Autonomous Agents](https://arxiv.org/abs/2606.08552)

**<font color=#1a73e8>作者：</font>** Mark Burgess  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> I discuss some quantitative representations of Promise Theory for processes involving autonomous agents. Agent models are common in software systems, machine learning, and biology, for example, but may also apply to physics and other forms of engineering. I describe how Bayesian probability and information theoretic optimization, including Active Inference, may be incorporated with promise semantics -- as well as how Promise Theory supplements solutions, helping to avoid probability's pitfalls, which include non-local coordination, calibrating, and normalizing probabilistic computations. The role of boundary conditions in constraining allowed states and selecting decision thresholds is a form of promise, and agent alignment provides a scalable definition of intent. Autonomous agents may congeal into swarms with superagent characteristics by trying to minimize their information, despite uncertainty that works to maximize it. The use of Promise Theory involves some research challenges as well as stylistic preferences.

---


### 246. [A Theoretical Analysis of Memory and Overfitting Phenomena in Stochastic Interpolation Models](https://arxiv.org/abs/2606.08554)

**<font color=#1a73e8>作者：</font>** Yunchen Li, Shaohui Lin, Zhou Yu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper provides a theoretical account of memorization in stochastic interpolation models. By leveraging closed-form expressions for the optimal velocity field and the associated score function, we show that, in the continuous-time oracle setting, both deterministic and stochastic generation processes recover training samples. Under Euler discretization, generated samples remain centered around training samples, with deviations controlled by the step size. We further analyze generation in the presence of estimation errors and show that accumulated estimation errors control the endpoint deviation from the training set. These results imply that the generated sample admits a representation as a training sample perturbed by three controlled terms: a discretization-induced bound, an estimation-error-induced bound, and stochastic Gaussian noise. Based on this characterization, we provide theoretical definitions of overfitting and underfitting in generative models. Synthetic simulations support our theoretical findings.

---


### 247. [Physics-Guided Dual Decoding and Spectral Supervision for Global 3D Hydrometeor Prediction](https://arxiv.org/abs/2606.08563)

**<font color=#1a73e8>作者：</font>** Dandan Chen, Yaqiang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While global data-driven models excel at predicting continuous atmospheric variables, three-dimensional hydrometeor forecasting remains challenging due to the zero-inflated, long-tailed distributions of these variables. Standard deep learning optimization often yields overly smooth forecasts, attenuating extreme events and spatial textures. We propose PredHydro-Net, a physics-guided dual-decoding framework that mitigates this smoothing. To resolve multi-variable optimization conflicts, it employs a decoupled architecture where macroscopic thermodynamic and dynamic fields unidirectionally modulate hydrometeor generation. By integrating wavelet-based frequency decoupling, spectral amplitude matching, and adversarial training, the model achieves a favorable trade-off between quantitative accuracy and spatial fidelity. In a 72-h global evaluation, PredHydro-Net outperforms both spatiotemporal deep learning baselines (Earthformer and PredRNNv2) and the operational Global Forecast System (GFS) in extreme-event detection and spectral representation. Furthermore, it demonstrates strong climatological consistency with Global Precipitation Measurement (GPM) satellite retrievals. The model reasonably reproduces the three-dimensional cloud structures in extreme weather events, such as Hurricane Ian. Feature attribution confirms its dependence on physical precursors such as relative humidity and wind convergence, offering a robust, physics-informed approach to long-tailed atmospheric prediction.

---


### 248. [Towards Accurate Emotion-Attributed Video Captioning via Fine-grained Emotion-Cause Pair Extraction](https://arxiv.org/abs/2606.08566)

**<font color=#1a73e8>作者：</font>** Weidong Chen, Cheng Ye, Zhendong Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotional Video Captioning (EVC) is a challenging task that aims to generate factually accurate and emotionally rich descriptions for videos. Existing EVC methods leverage holistic visual features to mine global emotional cues, and then aggregate multimodal features to guide the emotional caption generation, which ignores the critical characteristic of the EVC task. Visual emotions are evoked by specific motivational causes, which are usually only implied in core video segments. The holistic mining brings significant information redundancy and inaccurate emotional cues. Thus, fine-grained visual cause extraction has a facilitative effect on both emotion perception and emotion-attributed caption generation. To this end, we propose a fine-grained emotion-cause pair extraction framework for emotion-attributed video captioning. Specifically, we learn pair-wise emotion and cause features in two rounds: 1) We propose a Concept-aware Visual Semantic Decomposition module to augment visual features by exploring scene, object, and motion concepts. Besides, to enhance emotional features, we propose a Visual-guided Emotion Interpretable Learning module, which guides emotion refinement with visual temporal dynamics, and augments the interpretable refinement process by reliable VAD-vector constraints. 2) We achieve emotion-cause pair extraction by cross-coupling the visual and emotional features before and after refinement, and leverage contrastive loss to achieve semantic forced alignment. Overall, our approach optimizes complex semantic understanding and emotion perception of videos, leading to a promising performance in emotional captioning. Extensive experiments on three challenging datasets demonstrate the superiority of our approach and each proposed module, e.g., achieving the best performances with +4.4% and +5.4% w.r.t. BLEU-2 and ROUGE-L, respectively, on the EVC-MSVD dataset.

---


### 249. [OmniCap-IF: Benchmarking and Improving Instruction Following Abilities for Omni-Video Captioning](https://arxiv.org/abs/2606.08572)

**<font color=#1a73e8>作者：</font>** Jiahao Wang, An Ping, Yanghai Wang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Omni-modal Large Language Models (OLLMs) have demonstrated impressive capabilities in jointly processing audio and visual streams, their ability to strictly adhere to complex, multi-faceted user instructions remains largely unexplored. Existing benchmarks primarily focus on holistic video understanding or text-only instruction following, failing to capture the intricate interplay between modalities and user constraints. To bridge this gap, we introduce OmniCap-IF, the first comprehensive benchmark specifically designed to evaluate instruction-following capabilities in omni-modal captioning. OmniCap-IF incorporates a systematic framework that assesses captions on two dimensions: format correctness and content correctness. Our benchmark encompasses 50 distinct constraint types across pure visual, pure audio, and audio-visual modalities, while integrating Temporal Grounding to assess spatio-temporal precision. Extensive evaluations of prominent models on 1,920 high-quality samples reveal significant performance disparities. Furthermore, our analysis uncovers a critical "format-content tradeoff", demonstrating that increasing formatting complexity directly degrades models' omni-modal reasoning abilities. Finally, to advance the field, we curate a 54K instruction-tuning dataset, OmniCap-IF-54K and present OmniCaptioner-IF, which achieves notable improvements in both complex instruction adherence and general omni-modal captioning performance.

---


### 250. [Titans-as-a-Layer: Test-Time Memory for Conversational Speech Emotion Recognition](https://arxiv.org/abs/2606.08573)

**<font color=#1a73e8>作者：</font>** Daniel Chen, Qicong Hu, Yang Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speech emotion recognition (SER) is commonly formulated as utterance-level classification, although conversational emotion depends on a speaker's usual vocal range and the emotional context established by previous utterances. Speech-language models provide strong pretrained acoustic and semantic representations, and can adapts them to SER labels via finetune, but this mechanism still missing per-dialogue state. We study whether test-time neural memory can supply this missing context while leaving the large audio language models (LALMs) backbone intact. Building on Titans, we introduce a plug-and-play Memory-as-a-Layer (MAL) adapter that writes dialogue history into a small neural memory and reads it back as an audio-token-aligned residual update, avoiding changes to the host model's token positions. Across different audio LLMs and emotion recognition datasets evaluations, our design improves SER performs across different evaluation metrics, supporting test-time memory as a residual contextual mechanism for conversational SER.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-527](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
