# 🧠 大模型相关研究 | 2026年06月17日

> 本类共 **270** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**251-270**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-270**

---

### 251. [Robust Dual-Signal Fusion: Hybrid Neuro-Symbolic Gating with Compressed Chain-of-Thought Refinement for Irony Detection in Social Media Texts](https://arxiv.org/abs/2606.16845)

**<font color=#1a73e8>作者：</font>** Ankit Bhattacharjee, Krityapriya Bhaumik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) natively default to literal semantic interpretations, making zero-shot irony detection a persistent challenge. We introduce the Robust Dual-Signal (RDS) Fusion framework, a hybrid neuro-symbolic architecture that compresses Chain-of-Thought (CoT) reasoning trajectories without Supervised Fine-Tuning (SFT). Evaluated on a strictly held-out TweetEval test set (N=734), RDS achieves 78.1% accuracy and a Macro F1 of 0.777, matching the absolute performance ceiling of the fine-tuned BERTweet. On the heavily imbalanced iSarcasm dataset, the frozen CoT pipeline filters 22.5% of out-of-distribution hallucinations, yielding a zero-shot Macro F1 of 0.6726 and Ironic F1 of 0.4821, outperforming multiple heavily supervised SemEval transformer ensembles. A statistical ablation confirms this structural synergy: adding the symbolic prior to the neural baseline yields no significant gain (p = 0.242), and the marginal benefit of adding the CoT pipeline to that prior is heavily compressed (p = 0.149). Only the complete, concurrent fusion of all three signals achieves a statistically validated improvement over the baseline (p = 0.005).

---


### 252. [Follow the Latent Roadmap: Navigating Revocable Decoding for Diffusion LLMs with Anchor Tokens](https://arxiv.org/abs/2606.16847)

**<font color=#1a73e8>作者：</font>** Yizhen Yao, Qinglin Zhu, Runcong Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion Large Language Models (dLLMs) offer a promising avenue for parallel generation but face a trade-off between decoding speed and quality. While revocable decoding strategies attempt to mitigate errors by verifying and remasking tokens, they typically operate within a mixed-quality context. This leads to two critical failures: \textit{Error Propagation}, where new tokens absorb toxic information from erroneous context, and \textit{Local Error Reinforcement}, where errors mutually reinforce each other to evade detection. To alleviate these challenges, we propose ASRD (Anchor Supervised Revocable Decoding), a training-free framework that operates within the embedding space. ASRD explicitly decouples the decoding context into trusted \textit{Anchor Tokens}, which are identified via temporal consistency, and uncertain candidates. Leveraging a dynamic Anchor Tokens Cache, we introduce two complementary mechanisms: (1) Anchor-Guided Generation, which injects entropy-weighted anchor signals into masked positions to implicitly rectify attention toward the reliable global skeleton; and (2) Anchor-Perturbed Verification, which applies orthogonal perturbations to uncertain candidate tokens, destabilizing and remasking errors driven by fragile local consensus. Extensive experiments on math and coding benchmarks demonstrate that ASRD outperforms recent remasking baselines, achieving accuracy improvements of up to 6.4\% while accelerating inference throughput by up to 7.2$\times$.

---


### 253. [Revisiting the Systematicity in Negation in the Era of In-Context Learning](https://arxiv.org/abs/2606.16867)

**<font color=#1a73e8>作者：</font>** Hitomi Yanaka, Taisei Yamamoto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding the meaning of negated sentences remains one of the challenges for language models, even in the era of large language models (LLMs). We analyze systematicity regarding LLM understanding of negation from two perspectives: behavioral systematicity and representational systematicity. For behavioral systematicity, we confirm that through demonstrations and in-context learning, LLMs can recognize negation expressions and scope within sentences to some extent, but they fail to achieve perfect performance. In particular, the difficulty of the negation scope recognition for models varies depending on the output format. For representational systematicity, we analyze the extent to which function vectors can be robustly constructed from in-context examples for tasks that are essential to understanding negation. The experiments suggest that while function vectors can be composed for negation cue extraction tasks, extracting function vectors for recognizing scope is more challenging.

---


### 254. [Compositional Reasoning Depth Predicts Clinical AI Failure: Empirical Evidence Consistent with Transformer Compositionality Limits in Electronic Health Record Question Answering](https://arxiv.org/abs/2606.16890)

**<font color=#1a73e8>作者：</font>** Sanjay Basu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aggregate accuracy benchmarks conceal a systematic structure in how large language models fail at electronic health record (EHR) question answering: questions requiring more inferential steps produce disproportionately more errors. Motivated by theoretical results on transformer compositionality limits, we introduce a pre-specified hop-count taxonomy -- the number of distinct reasoning steps required to answer a clinical question from an EHR -- as a principled predictor of model failure. We annotate 313 clinician-generated MedAlign EHR question-answer pairs across four hop levels and evaluate 301 questions in a within-model ablation (claude-sonnet-4-6, zero-shot vs. extended thinking) and cross-architecture replications (gpt-4o and gpt-5.4-2026-03-05, zero-shot). All three models, spanning two providers and two OpenAI generations (GPT-4 and GPT-5), show monotone accuracy decline with hop count: Claude Sonnet zero-shot falls from 30.6% (hop=1) to 17.6% (hop=4) (Cochran-Armitage z=-2.30, p=0.011; OR per hop 0.72, 95% CI [0.56,0.92], p=0.008); GPT-4o replicates this (37.8% to 14.7%; OR 0.58 [0.45,0.75], p<0.001); and gpt-5.4-2026-03-05 confirms it (37.8% to 23.5%; OR 0.80 [0.66,0.98], p=0.027). A pre-specified context-sufficiency audit shows higher-hop questions are not differentially disadvantaged by EHR truncation (answerability 93-95% at hops 2-4 vs. 79% at hop=1), so the decline reflects compositional reasoning difficulty. Extended thinking did not significantly flatten the accuracy-depth curve across three reasoning conditions, and thinking-token usage scaled with hop count (r=0.31, p<0.0001), consistent with the predicted O(k) computational requirement. Hop count is thus a theory-motivated, cross-architecture predictor of large-language-model error on EHR question answering, with direct implications for deployment risk stratification of clinical AI.

---


### 255. [Contrastive-Difference CKA Reveals Concept-Specific Structural Alignment Across Language Model Architectures](https://arxiv.org/abs/2606.16897)

**<font color=#1a73e8>作者：</font>** Xueping Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do different LLM architectures encode high-level concepts in structurally compatible ways? We systematically characterize a geometric-functional universality dissociation: across multiple concept domains and architectural families, moderate geometric convergence coexists with near-perfect functional transfer. Using contrastive-difference CKA (CKA_Delta), a training-free diagnostic that computes kernel alignment on per-sample contrastive differences, we isolate concept-specific convergence from generic similarity -- achieving significant discrimination where standard CKA cannot. The dissociation replicates across all six concept domains we test (five with p <= 0.017 geometric discrimination and safety as a converging-functional trend, p = 0.08), including two non-instruction concepts (code-vs-NL, reasoning-vs-recall) validated without system prompts; a single 70B--70B pair provides an observational note that universality may strengthen with scale, requiring replication with additional >=70B models. We position CKA_Delta as a practical regime classifier and architectural outlier detector (Gemma: d = 1.08, AUC = 0.79) rather than an absolute transfer-accuracy predictor, providing a training-free diagnostic for cross-architecture concept monitoring.

---


### 256. [Speaking the Language of Science: Toward a General-Purpose Generative Foundation Model for the Natural Sciences](https://arxiv.org/abs/2606.16905)

**<font color=#1a73e8>作者：</font>** Mingyang Li, Yurou Liu, Jieping Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this report, we present LOGOS (Language Of Generative Objects in Science), a scientific generative language model that unifies heterogeneous tasks across the natural sciences within a single autoregressive framework based on a shared scientific grammar. It encodes diverse scientific objects and their spatial interactions as token sequences over a common vocabulary. By representing spatial contact and constraint patterns as discrete tokens, the model captures complex structural interactions in a purely sequential manner, without relying on explicit coordinates or geometric neural networks. This unified representation enables a wide range of downstream tasks to be formulated consistently as next-token prediction in the same grammar space, creating strong alignment between continued multi-domain pre-training and downstream objectives. Across diverse tasks, LOGOS consistently matches or outperforms domain-specific baselines, providing preliminary evidence for the feasibility of "one model fits all" in the natural sciences. We train LOGOS models at different scales (1B, 3B, and 8B parameters) and find a consistent positive correlation between model size and performance. This suggests that the future of AI for Science (AI4S) may not lie in building an independent technical stack that is separated from large language models (LLMs). Instead, it may depend on deeply aligning scientific foundation models with LLMs through shared architectures, shared training paradigms, and shared inference infrastructure, so that LLMs can truly become a new entry point for AI4S. We release the model weights and associated resources to facilitate further research.

---


### 257. [LESS Is More: Mutual-Stability Sampling for Diffusion Language Models](https://arxiv.org/abs/2606.16908)

**<font color=#1a73e8>作者：</font>** Amr Mohamed, Guokan Shang, Michalis Vazirgiannis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) offer a promising alternative to autoregressive decoding by iteratively refining masked sequences, enabling parallel token updates and bidirectional conditioning. Their practical efficiency, however, is limited by sampling procedures that execute a fixed number of reverse denoising steps selected before decoding, spending computation on already-stable positions and sometimes committing unstable ones too early. We present \textsc{LESS}, a training-free, model-agnostic adaptive sampler that treats token commitment as an online stopping problem. \textsc{LESS} implements mutual-stability sampling through a joint stability rule that makes a masked position eligible for unmasking only when its top-1 prediction has high confidence, its top-1 token persists across recent reverse steps, and its predictive distribution is stable under top-$K$ inter-step Jensen--Shannon divergence. We evaluate \textsc{LESS} on Dream-7B, LLaDA-8B, and LLaDA-1.5-8B, covering full-sequence diffusion and semi-autoregressive blockwise sampling regimes, across seven benchmarks spanning general knowledge, math, and code. \textsc{LESS} improves average accuracy over strong training-free adaptive samplers while using $72.1\%$ fewer reverse steps than fixed-budget decoding. Since each reverse step requires a Transformer forward pass, these step-count reductions translate into fewer forward evaluations, lower measured wall-clock latency, and lower estimated inference compute.

---


### 258. [Demystifying Variance in Circuit Discovery of LLMs](https://arxiv.org/abs/2606.16920)

**<font color=#1a73e8>作者：</font>** Frank Zhengqing Wu, Francesco Tonin, Volkan Cevher  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Circuit discovery is a key technique in mechanistic interpretability to pinpoint the model components that are crucial for performing a given task. Although the current state-of-the-art method (EAP-IG) performs well on the metric of (un)faithfulness, it suffers from substantial variability. This includes resampling variance, where the circuit changes when we probe with a new batch of data from the same distribution; rephrasing variance, where the discovered circuit shifts when the prompts are rephrased; and sample-wise variance, where a circuit with low population unfaithfulness exhibits large fluctuations in unfaithfulness across individual samples.
This paper studies the roots of these variances. We demonstrate that CEAP, our new circuit discovery method that improves upon EAP-IG with a theoretical guarantee, can substantially lessen resampling variance. We further show that rephrasing variance arises because prompts with different templates tend to activate different circuits in the model. This leads us to argue that it may be challenging to find a comprehensive circuit that explains and controls the model's behavior on a task, which can be expressed in countless templates, suggesting that LLMs may be inherently hard to steer. We show that sparsity, which has been claimed to form more compact and interpretable task circuits, fails to solve this problem. Regarding sample-wise variance, we argue that it is largely benign: extremely poor unfaithfulness scores often stem from how unfaithfulness is defined, rather than from defects in the measured circuits. We show that the magnitude of unfaithfulness is affected by selective contribution scaling, a neural mechanism that accounts for the extremely poor scores sometimes observed.

---


### 259. [Exploring Extrinsic and Intrinsic Properties for Effective Reasoning with Code Interpreter](https://arxiv.org/abs/2606.16934)

**<font color=#1a73e8>作者：</font>** Patomporn Payoungkhamdee, Napat Laosaengpha, Jenta Wonglertsakul 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning with a Code Interpreter (CI) has emerged as an effective paradigm for enhancing the reasoning capabilities of large language models (LLMs) through executable computation and iterative verification. Despite its growing adoption, the behavioral properties underlying effective code reasoning remain largely underexplored. In this work, we investigate code reasoning from two distinct perspectives inspired by prior studies of natural language reasoning: extrinsic properties, represented by crucial tokens, and intrinsic properties, represented by code-specific cognitive behaviors. Across multiple LLMs, we find that stronger CI reasoning models consistently exhibit a higher prevalence of crucial tokens and cognitive behaviors, particularly verification, backtracking, and backward chaining. Building on these observations, we examine how these properties can be leveraged during both inference and training. At inference time, appending code-specific crucial tokens improves performance on several reasoning capabilities, including mathematical, ordering, and optimization, while yielding limited benefits elsewhere. At training time, augmenting a state-of-the-art framework with code-specific cognitive behaviors improves supervised fine-tuning and reinforcement learning performance in two of three evaluated models. Further analysis shows that these behaviors reduce overthinking in incorrect responses and improve token efficiency, while also revealing factors that limit gains in a certain model. Our findings provide the first systematic characterization of effective reasoning with CI and demonstrate both the potential and limitations of leveraging key properties to improve CI-based reasoning.

---


### 260. [Scalable Circuit Learning for Interpreting Large Language Models](https://arxiv.org/abs/2606.16939)

**<font color=#1a73e8>作者：</font>** Naiyu Yin, Dennis Wei, Tian Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A prominent research direction in mechanistic interpretability is learning sparse circuits over LLM components to reveal how they jointly produce model behavior. However, raw neurons are polysemantic, making learned circuits hard to interpret. Sparse autoencoder (SAE) features alleviate this, but their high dimensionality makes existing intervention-based circuit learning methods computationally prohibitive. We propose CircuitLasso, a scalable circuit-learning approach based on sparse linear regression. CircuitLasso recovers circuits whose structural accuracy matches that of state-of-the-art intervention-based methods on the benchmark data, at a fraction of the computational cost. For interpretability, CircuitLasso efficiently uncovers relationships among SAE features, showing how human-interpretable semantic features propagate through the model and influence its predictions. Finally, we validate the utility of our learned circuits by leveraging their insights to achieve comparable performance at substantially lower cost on a domain-generalization task.

---


### 261. [Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification](https://arxiv.org/abs/2606.16987)

**<font color=#1a73e8>作者：</font>** Truong Thanh Hung Nguyen, Khanh Van Quynh Nguyen, Hoang-Loc Cao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate Harmonized Tariff Schedule (HTS) code classification is essential for customs clearance, duty assessment, trade statistics, and regulatory compliance in maritime logistics. However, exact HTS classification remains challenging because product descriptions are often short, incomplete, or ambiguous, while correct classification depends on hierarchical tariff structures, legal notes, and jurisdiction-specific rules. This paper proposes an agentic large language model (LLM) framework for Canadian 10-digit HTS code classification in smart-port and maritime logistics environments. The framework integrates multi-agent information retrieval, semantic retrieval over official tariff documents, evidence-grounded reasoning, consensus-based validation, element-wise voting across hierarchical code components, confidence estimation, and human-in-the-loop escalation. We evaluate the framework on a private dataset of 3,300 domain-expert-labeled product records collected from logistics and delivery contexts. Experimental results show that exact 10-digit classification remains difficult even for advanced LLMs, with performance decreasing from coarse chapter-level prediction to fine-grained tariff and statistical suffix assignment. These findings demonstrate the need for evidence-grounded, uncertainty-aware, and human-centered classification workflows rather than fully autonomous single-step prediction. The proposed framework supports more interpretable, accountable, and compliance-oriented HTS classification for maritime logistics and smart-port operations. Our code is available at this https URL.

---


### 262. [DreamX-World 1.0: A General-Purpose Interactive World Model](https://arxiv.org/abs/2606.16993)

**<font color=#1a73e8>作者：</font>** DreamX Team, Yancheng Bai, Rui Chen 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DreamX-World 1.0 is a general-purpose interactive text/image-to-video world model for controllable long-horizon generation. It supports camera navigation, revisits to previously observed regions, and promptable events across photorealistic, game-style, and stylized domains. Our data engine combines camera-accurate Unreal Engine rendering, action-rich gameplay recordings, and real-world videos with recovered camera geometry. For camera control, we introduce E-PRoPE, a lightweight variant of projective positional encoding that retains PRoPE's projective camera geometry while applying camera-aware attention to spatially reduced tokens. We convert a bidirectional video generator into a few-step autoregressive world model using causal forcing, DMD-style distillation, and long-rollout training. Training on self-generated long-horizon contexts exposes the model to its own generated history and reduces the style and color drift that accumulates across autoregressive chunks. Memory-Conditioned Scene Persistence retrieves earlier views through camera-geometry-based retrieval, while residual recycling makes the conditioning path less sensitive to imperfect memory latents. Event Instruction Tuning adds composable event control, and reinforcement learning alignment recovers camera control and visual quality after distillation. With mixed-precision DiT execution, residual reuse, 75\%-pruned VAE decoding, and asynchronous pipeline parallelism, DreamX-World 1.0 reaches up to 16\,FPS on eight RTX\,5090 GPUs. On our 5-second basic evaluation, DreamX-World 1.0 achieves a camera-control score of 73.75 and an overall score of 84.76, outperforming HY-WorldPlay 1.5 and LingBot-World in overall score, which achieve 80.79 and 80.45, respectively.

---


### 263. [When in Doubt, Plan It Out: Committed Small Language Model Deliberation for Reactive Reinforcement Learning](https://arxiv.org/abs/2606.16995)

**<font color=#1a73e8>作者：</font>** Nathan Gavenski, Juarez Monteiro, Francisco Galuppo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) policies often degrade in unfamiliar environments because they lack explicit deliberation. We propose Plan, Align, Commit, Think (PACT), a hybrid architecture that combines a fast, reactive RL policy with a slow, deliberative Small Language Model (SLM) planner. PACT invokes the SLM asynchronously to generate and validate candidate action plans. Once a plan is verified through simulation as safe, feasible, and complete, it is executed directly, bypassing the RL policy without retraining or modifying it. Evaluated on three FrozenLake configurations of increasing difficulty, PACT outperforms all baselines while relying on a 2B-parameter SLM backbone, suggesting that deliberative planning and reactive execution are more powerful in concert than either is alone in these settings.

---


### 264. [TokenPilot: Cache-Efficient Context Management for LLM Agents](https://arxiv.org/abs/2606.17016)

**<font color=#1a73e8>作者：</font>** Buqiang Xu, Zirui Xue, Dianmou Chen 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM agents are deployed in long-horizon sessions, context accumulation drives up inference costs. Existing approaches utilize text pruning or dynamic memory eviction to minimize token footprints; however, their unconstrained sequence mutations alter layouts, introducing prefix mismatches and cache invalidation. This reveals a critical trade-off between text sparsity and prompt cache continuity. To address this, we present TokenPilot, a dual-granularity context management framework. Globally, Ingestion-Aware Compaction acts as a framework harness to stabilize prompt prefixes and eliminate open-world environmental noise at the ingestion gate. Locally, Lifecycle-Aware Eviction monitors the ongoing residual utility of context segments, enforcing a conservative batch-turn schedule to offload content segments only when task relevance expires. Experiments on PinchBench and Claw-Eval under both isolated and continuous modes demonstrate that TokenPilot reduces costs by 61% and 56% in isolated mode, and 61% and 87% in continuous mode, while maintaining competitive performance compared to prior systems. TokenPilot has been integrated into LightMem2 at this https URL.

---


### 265. [FusionRS: A Large-Scale RGB-Infrared Remote Sensing Dataset for Dual-Modal Vision-Language Foundation Models](https://arxiv.org/abs/2606.17020)

**<font color=#1a73e8>作者：</font>** Jiaju Han, Ben Zhang, Xuemeng Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing vision-language models have advanced Earth observation understanding, but most existing work remains centered on RGB imagery, leaving the complementary information in infrared data underexplored. Infrared images provide distinctive cues, including thermal intensity structures, object boundaries, and illumination-invariant scene features, which can enrich visual-language learning beyond conventional RGB observations. However, a large-scale RGB-infrared-text dataset for remote sensing vision-language modeling is still absent. To address this gap, we introduce FusionRS, the first large-scale RGB-infrared-text dataset designed for dual-modal vision-language learning in remote sensing. FusionRS is constructed by translating diverse public RGB remote sensing images into infrared-style counterparts, forming aligned RGB-IR image pairs. Each pair is associated with conventional scene captions and IR-aware captions that explicitly describe infrared-specific visual properties while preserving semantic content. Based on FusionRS, we train dual-modal vision-language foundation models for RGB-IR joint understanding. We first train CLIP-style models for RGB-IR-text alignment, and then fine-tune generative VLMs for dual-modal RGB-IR captioning. Experiments show that FusionRS improves RGB-IR alignment, infrared-to-text retrieval, and dual-modal captioning over RGB-only and non-IR-aware training settings. Ablation studies further verify that IR-aware captions are crucial for strengthening infrared-language alignment, highlighting the importance of modality-specific textual supervision for more scalable RGB-infrared remote sensing vision-language representation learning.

---


### 266. [ExpRL: Exploratory RL for LLM Mid-Training](https://arxiv.org/abs/2606.17024)

**<font color=#1a73e8>作者：</font>** Violet Xiang, Amrith Setlur, Chase Blagden 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse reward reinforcement learning (RL) has become a standard tool for improving LLM reasoning, but its success depends critically on the coverage present in the base model. In practice, models are often primed for RL through \emph{mid-training} on curated reasoning traces that teach useful primitive skills such as decomposition, verification, or self-correction. Although effective, this strategy requires manually specifying what the model should learn, and it remains unclear whether such primitive coverage is enough for much harder problems, which require combining these skills into broader solution strategies. We study a more automated approach: \emph{RL-based mid-training} using large corpora of human-written question-answer data. Rather than treating reference solutions as targets to imitate, our method, ExpRL, uses them as \emph{reward scaffolds}: references are hidden from the policy and used only to construct problem-specific grading rubrics for judging on-policy reasoning traces. The policy samples from the original problem prompt, while an LLM judge compares the sampled reasoning trace against the reference solution and assigns outcome-level or process-level dense rewards. This lets ExpRL reinforce partial progress, useful intermediate reductions, and productive reasoning behaviors that sparse final-answer rewards often fail to upweight. On challenging math reasoning tasks, ExpRL yields stronger RL priming than SFT, sparse-reward GRPO, and self-distillation, and provides a better initialization for subsequent sparse-reward RL. Additional mixed-domain experiments further suggest that ExpRL can extend beyond the original math-only setting.

---


### 267. [Qwen-RobotWorld Technical Report: Unifying Embodied World Modeling through Language-Conditioned Video Generation](https://arxiv.org/abs/2606.17030)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Xiaoyue Chen, Anzhe Chen 等 38 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Qwen-RobotWorld, a language-conditioned video world model for embodied intelligence. With natural language as a unified action interface, it predicts physically grounded future visual trajectories from current observations across robotic manipulation, autonomous driving, indoor navigation, and human-to-robot transfer. This unified formulation provides three promising application directions: synthetic data generation for policy training augmentation, scalable virtual environments for policy evaluation, and language-guided planning signals for downstream robot control. This is achieved through a three-part design: a) Double-Stream MMDiT with MLLM Action Encoding, where a 60-layer double-stream diffusion transformer couples frozen Qwen2.5-VL semantics with video-VAE latents through layer-wise joint attention; b) Embodied World Knowledge (EWK), an 8.6M video-text corpus (200M+ frames) with action-language mapping over 20+ embodiments and 500+ action categories; and c) General+Expert Progressive Curriculum, a two-stage training strategy that first learns general visual priors and then injects embodied specialization under a shared language interface. Extensive results show strong competitiveness: ranks 1st overall on EWMBench and DreamGen Bench, outperforms all open-source models on WorldModelBench and PBench. Additional zero-shot analyses on RoboTwin-IF benchmark further support robust generalization and multi-view consistency.

---


### 268. [Benchmarking LLM Agents on Meta-Analysis Articles from Nature Portfolio](https://arxiv.org/abs/2606.17041)

**<font color=#1a73e8>作者：</font>** Anzhe Xie, Weihang Su, Yujia Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Meta-analysis is a demanding form of evidence synthesis that combines literature retrieval, PI/ECO-guided study selection, and statistical aggregation. Its structured, verifiable workflow makes it an ideal substrate for evaluating systematic scientific reasoning, yet existing benchmarks lack ground truth across the full retrieval-screening-synthesis pipeline. We introduce MetaSyn, a dataset of 442 expert-curated meta-analyses from Nature Portfolio journals. Each entry pairs a research question with PI/ECO criteria, a retrieval corpus of 140k PubMed articles, verified positive studies, hard negatives that are topically similar but PI/ECO-ineligible, and complete search strategies and date bounds.
Benchmarking twelve pipeline configurations (nine RAG variants and a protocol-driven agent) reveals a critical screening bottleneck: despite a retrieval ceiling of 90.9% recall at K=200, no system recovers more than 52.7% of ground-truth included literature. Current LLMs fail to reliably separate eligible studies from PI/ECO-failing distractors in pools of comparable topical relevance. Stage-attributed metrics capture where systems succeed and fail; a single end-to-end score does not.

---


### 269. [Context-Aware RL for Agentic and Multimodal LLMs](https://arxiv.org/abs/2606.17053)

**<font color=#1a73e8>作者：</font>** Peiyang Xu, Bangzheng Li, Sijia Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often fail when answering requires identifying a small but decisive piece of evidence within a long or complex context, such as a single line in a tool trace or a subtle detail in an image. We propose ContextRL, a context-aware reinforcement learning (RL) method that improves long-horizon reasoning and multimodal performance through an \emph{indirect} auxiliary objective. Instead of supervising only the final answer, ContextRL presents the model with a query, an answer, and two highly similar contexts, and rewards it for selecting the context that supports the query--answer pair, thereby encouraging fine-grained grounding. We construct contrastive context data in two domains: for coding agents, trajectories serve as contexts, yielding 1k pairs built via condition filtering; for multimodal reasoning, images serve as contexts, yielding 7K pairs built via generative editing and similarity search. ContextRL achieves average gains of +2.2% over standard GRPO on 5 long-horizon benchmarks, and +1.8% across 12 diverse visual question answering benchmarks. To disentangle the effect of the proposed objective from that of additional data, we compare against data-augmentation baselines that repurpose the same contrastive contexts as standard query--context--answer examples. These baselines provide little to no improvement, showing that the gains arise from the proposed context-selection objective rather than from the contrastive data alone.

---


### 270. [The Value Axis: Language Models Encode Whether They're on the Right Track](https://arxiv.org/abs/2606.17056)

**<font color=#1a73e8>作者：</font>** Nick Jiang, Isaac Kauvar, Jack Lindsey  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate whether language models internally track the value of their current trajectory, defined as the likelihood that their ongoing strategy will achieve their goals. Using synthetic, in-context reinforcement learning data, we construct a "value" axis for Qwen3-8B. We find that activations along this axis distinguish between high vs. low verbalized confidence, rollouts without and with backtracking, and correct vs. corrupted code. Steering towards high value causally suppresses self-correction and reduces explanatory verbosity, while steering towards low value induces backtracking and exploration. We demonstrate that direct preference optimization (DPO) can increase the internal value of rewarded behaviors (e.g. use a certain word), causing the model to act more confidently after exhibiting them. Finally, we apply the value axis to study in-the-wild settings. For example, we find that Qwen assigns low value to politically sensitive chat queries after post-training and that supervised fine-tuning increases internal confidence within the training domain. Our results suggest that language models linearly encode an estimate of expected goal success that modulates their confidence in pursuing a direction.

---


> [!TIP]
> 当前位于：**251-270**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-270**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
