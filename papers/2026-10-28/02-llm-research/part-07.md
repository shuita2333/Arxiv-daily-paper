# 🧠 大模型相关研究 | 2026年10月28日

> 本类共 **418** 篇论文：已确认 **396** 篇，待复核 **22** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-418](./part-09.md)

---

### 301. [RAGing Against Misogyny: Improving Implicit Misogyny Explanations](https://arxiv.org/abs/2610.35094)

**<font color=#1a73e8>作者：</font>** Ivana Crescenzi, Arianna Muti, Maarten Sap 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Implicit misogyny often requires background knowledge to be understood. To address this challenge, we propose a Retrieval-Augmented Generation (RAG) framework for detecting and explaining implicit misogyny in English and Italian, leveraging encyclopedic, slang and feminist knowledge sources. Using the ImplicIT-Mis and SBIC+ datasets, we evaluate the contribution of each knowledge source to detection and explanation quality, investigating also whether RAG addresses known LLM failure modes in implicit misogyny. Results show that RAG improves recall on ImplicIT-Mis, but does not improve detection performance on SBIC+. However, human evaluation shows that RAG-based explanations are preferred over no-RAG explanations in both languages. Feminist literature emerges as the most consistently useful source for detection and explanation.

---


### 302. [Spherical Brownian Diffusion for Language Modeling](https://arxiv.org/abs/2610.35101)

**<font color=#1a73e8>作者：</font>** Andrea Miele, Ilija Bogunovic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models involve two coupled design choices: how to corrupt continuous token representations and how to invert that corruption at generation time. Recent work has explored language generation on the unit sphere through geodesic and von Mises--Fisher (vMF) paths, raising the question of which forward process to use on this geometry and how much that choice matters relative to inference. We introduce Spherical Brownian Diffusion, using Brownian motion as the canonical isotropic diffusion on the sphere. Its heat semigroup provides a principled forward process, an additive dimension-free noise clock, and an exact ancestral bridge, while a clean-token posterior learned with cross-entropy supports multiple samplers. To separate corruption from inference, we derive high-dimensional approximation rates between Brownian and moment-matched vMF corruption and use this relationship for controlled substitutions. On Sudoku, Brownian and moment-matched vMF give nearly identical results across four samplers and five budgets under otherwise identical settings. In contrast, with the corruption process fixed, sampler choice produces a 25.0-point spread at a sampler budget of 180 calls. Using the ancestral bridge, we split this gain into a memory effect from re-noising the state, present on Sudoku and GSM8K, and a token-selection effect on GSM8K and largest at small budgets. Across reasoning tasks, categorical refinement improves performance, whereas unconditional text generation benefits from stochastic updates that preserve diversity.

---


### 303. [Useful Diversity or Hallucinated Variety? Persona-Conditioned Synthetic Query Generation for E-Commerce Search](https://arxiv.org/abs/2610.35102)

**<font color=#1a73e8>作者：</font>** Filippos Ventirozos, Tom Armitage, Mahmoud Oshagh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic supervision can bootstrap semantic parsers in new search domains, but prompt-induced diversity is useful only when generations are faithful to the structured intent. We explore this for cold-start e-commerce search: 118,098 synthetic pairs produced by 6 LLMs with 9 persona-conditioned prompt families on a 47-field UK automotive schema, against 1,214 human-annotated and 15,304 production queries. We show that the IPIP personality bundle improves parser F1 in all four matched contrasts (Holm-corrected $p<.001$), and all three bundles have a positive main effect over the complete $2^3$ grid. Syntax conditioning is the axis that moves generations towards real traffic. It also induces lexical diversity. Alignment sKL, the divergence between von Mises-Fisher distributions fitted to synthetic and human-annotated queries, is an unlabelled proxy for parser F1 ($\rho=-0.917$ against human queries written for simulated shopper scenarios, lower is closer). An LLM committee, checked against a blinded author pass, triages the 927 queries missed by every parser and labels 37% as hallucinated. Dropped constraints dominate. The four syntax-bearing families have the largest hallucinated shares, 38 to 42%, while IPIP alone has the lowest at 28%.

---


### 304. [Rethinking Evaluation for Principled Generalization Using a Kripkean Challenge to Meaning as Use](https://arxiv.org/abs/2610.35111)

**<font color=#1a73e8>作者：</font>** Niyar R Barman, Omar Naim, Nicholas Asher  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models operationalize an intuitive, view of meaning as use. We argue that it faces a rule-following challenge. Using Kripke's interpretation of Wittgenstein, we argue that finite histories of use do not determine a unique rule for future extension. This reframes the debate about OOD generalization but also about NLP evaluation; benchmarks that measure performance on fixed use cases or local robustness, we argue, do not by themselves establish semantic competence. To evaluate whether models preserve rules and concepts under principled domain extension, we propose to evaluate two capacities, central to this ability: abstraction and recursion; and we offer an experimental paradigm for testing both.

---


### 305. [UTA: Universal Training Adaptive Learning Rate Decay](https://arxiv.org/abs/2610.35113)

**<font color=#1a73e8>作者：</font>** Anda Tang, Junjie Wang, Xuanlin Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning rate decay (LRD) is critical for training high-performance models, yet most designs remain empirically driven. Although the Universal Budget Aware (UBA) LRD offers a theoretical framework, its reliance on SGD dynamics limits its applicability to modern Adam-type optimizers and leaves its key `optimization difficulty parameter' opaque. To bridge this gap, we propose the Universal Training Adaptive (UTA) LRD. Unlike UBA's fixed offline trajectory anchored solely to iterations, UTA treats LRD as a closed-loop shape-and-scale problem. By continuous-time formulation, UTA is training-state adaptive with segment-wise optimal shape. This adaptivity links external iterations with internal training states, enabling a near-optimal path in both progression shape and learning rate (LR) scale, a property unattainable by other LRDs, including UBA. Empirically, we demonstrate consistent improvements across language models (LLaMA 60M to 1B) and vision models (ResNet50, ViT-B) on ImageNet with plug-and-play ease and negligible overhead. Extensive ablation studies further confirm UTA's robustness across dimensions, including peak LR, final decay ratio, its parameter $\varphi_0$, component efficacy and generalization to fine-tuning scenarios, underscoring its practical implementability.

---


### 306. [TUON: A Tensor-Aware Optimizer Utilizing Tensor-SVD and Polarization for Large Language Model Pretraining](https://arxiv.org/abs/2610.35130)

**<font color=#1a73e8>作者：</font>** Anda Tang, Xuanlin Yang, Junjie Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large scale language model~(LLM) pretraining is increasingly bottlenecked by optimizer efficiency, driving optimizer design from vector-aware methods such as AdamW to matrix-aware methods. Matrix-aware optimizers such as Muon exploit matrix structure but treat layers independently, neglecting cross-layer correlations. Tensor-aware optimizers are therefore needed, yet existing ones rely on a matricization-based tensor algebra and remain restricted to shallow stacking and specific modules. In this paper, we propose \textbf{TUON}, a novel optimizer built on a transform-based tensor algebra derived from the Tensor-SVD (T-SVD). Unlike methods that polarize a globally unfolded matrix, TUON mixes layers via a unitary transform $\boldsymbol{Q}$ and then polarizes each transformed slice, and inverts the transform to recover the update. This mix-then-separate strategy captures cross-layer correlations while preserving per-layer diversity, avoiding the structural dimension imbalance and cross-layer misalignment of unfolding. Thus it successfully scales to more layers and diverse modules beyond QKV. Theoretically, we prove that TUON performs steepest descent under a $\boldsymbol{Q}$-transformed tensor spectral norm, and identify its update as the tensor polar factor of the T-SVD. We further establish transform non-redundancy, norm and smoothness comparisons with Muon and TEON, and a convergence guarantee. Empirically, TUON improves consistently over Muon and TEON on GPT-124M/350M and Qwen-0.6B/4B, with ablations confirming the transformation mechanism, cross-layer structure beyond two-layer stacking, adaptability beyond QKV, and robustness to the polarization method.

---


### 307. [Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models](https://arxiv.org/abs/2610.35138)

**<font color=#1a73e8>作者：</font>** Xilin Wei, Shengyuan Ding, Xinyu Fang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating human-AI co-design requires testing whether coding agents can translate real users' multimodal requests into working application revisions. We introduce Co-Design Bench, a reference-free benchmark of 273 tasks curated from 37,463 deduplicated queries across 26,314 real user coding sessions. Its two tracks, Multimodal Editing (ME) and Repository Editing (RE), cover localized edits with optional image, audio, video, or document inputs and coordinated repository revisions. Tasks span three capability dimensions: Grounded Understanding, UI Transformation, and Functional Implementation. The tasks pair normalized requests and runnable pre-edit applications with 2,331 hidden expert-authored acceptance criteria. Our judge-then-refute protocol grades criteria using source and browser evidence, challenges positive verdicts with a separate LLM verifier, and audits visual and interaction claims without gold code or target screenshots. Under a shared agentic harness, the strongest of ten model endpoints passes an average of 69.9% of criteria per task but fully satisfies only 26.4% of tasks. All ten endpoints achieve lower criterion completion on repository edits spanning three or four change types than on those spanning one or two. Co-Design Bench provides a testbed for studying the gap between partial requirement satisfaction and complete task success under agentic execution for real-user application revisions.

---


### 308. [CalibraRL: Confidence-Calibrated Reinforcement Learning for Mitigating Hallucinations in RAG](https://arxiv.org/abs/2610.35142)

**<font color=#1a73e8>作者：</font>** Qianchi Zhang, Hainan Zhang, Liang Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often produce plausible but incorrect answers, motivating reinforcement learning methods that reward correct answers, penalize incorrect answers, and allow abstention. However, fixed outcome-based rewards do not distinguish incorrect responses with different confidence levels or account for differences in answering reliability across queries. Consequently, such rewards may inadequately penalize overconfident errors and fail to discourage unnecessary abstention. We propose CalibraRL, a reinforcement learning framework that incorporates response confidence and query-level answering evidence into reward design. For non-abstaining responses, CalibraRL combines correctness-based utility with a Brier-based penalty that encourages agreement between confidence and correctness. For abstentions, it estimates conditional answering reliability using a Beta posterior derived from the correctness of non-abstaining responses within each sampled group. The abstention reward increases with the posterior probability that the model's accuracy on non-abstaining responses is below a predefined threshold. CalibraRL reuses training rollouts without requiring additional annotations indicating whether the model knows the answer to each question. Experiments on three QA datasets demonstrate that CalibraRL improves answer precision and reduces hallucinations compared with strong baselines. Further analysis shows that CalibraRL reduces mean expected calibration error (ECE) by 30.8\% across two backbone models and three datasets, highlighting its potential to improve the reliability of retrieval-augmented generation (RAG) in web search.

---


### 309. [LongSearchEval: Evaluating Long-Horizon Web Search Capabilities of Large Language Models via a Trajectory-Aware Agent Framework with Failure-Node Localization](https://arxiv.org/abs/2610.35150)

**<font color=#1a73e8>作者：</font>** Jialiang Liu, Shusheng Li, Wenjun Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon web search requires LLM-based agents to integrate information across web pages through extended interactions under task-specific constraints. Evaluating this capability is important not only for measuring final answer quality, but also for assessing whether an agent acquires, verifies, and uses evidence reliably over extended interactions. Existing evaluations, however, mainly rely on simulated trajectories or on post-hoc trajectories reconstructed from final answers, rather than on retained real interaction traces, which limits the fidelity of behavioral assessment and weakens support for fine-grained error localization. To address this gap, we introduce LONGSEARCHEVAL, a trajectory-aware agent evaluation framework that combines a unified agent execution protocol with source constrained outcome verification and retrospective failure-node localization. Stage 1 verifies answer groups against agent-cited webpages without human-authored gold answers; Stage 2 audits normalized rounds and links flagged failure nodes to incorrect answer groups. We evaluate 16 models from eight families on 100 tasks, yielding 1,600 retained runs and 6,545 automatically flagged failure nodes. Trajectory collection and evaluation required 1,037 and 318 hours of cumulative runtime, respectively. Human validation yields 94.50% agreement on supplied answer-group labels and 98.11% feature-correspondence precision for audited round-group links. Together, outcome scores and linked trajectory evidence support controlled model comparison and retrospective inspection of answer-related content.

---


### 310. [SoK: Timestamps Are Not a Time Model: Rethinking Temporal Reasoning in Host-Based Intrusion Detection](https://arxiv.org/abs/2610.35151)

**<font color=#1a73e8>作者：</font>** Rene Heinzl, Markus Nissl  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Host-based intrusion detectors order events, window audit streams and sequence attack stages by their timestamps. Every conclusion they draw therefore rests on assumptions about clocks, delivery, entity identity and the integrity of the evidence, and most of these assumptions go unstated. This Systematization of Knowledge (SoK) makes them explicit. Drawing on temporal databases, stream processing and runtime verification, we distill five components of a time model, together with a checklist of evidence assumptions and four levels of guarantee, and walk through a running campaign with them. A documented search yields fifteen families of detection and investigation. For papers selected by screening role and period, plus named systems and landmarks, we check the stated assumptions in the full texts, and we assess eleven temporal knowledge representation and reasoning (KRR) formalisms and a learned baseline on nine attack patterns. Some early alert correlators stated clock and delivery assumptions, and forensics measures clock error. Current provenance-based detectors state no clock bound. Four audited papers describe input-ordering conditions or conventions, but none specifies conditions for conclusion validity across a stated class of delivery failures. In the selected provenance-based systems, campaign composition uses system-specific procedures or objectives, learned state, causal graph queries or language models, and beyond CEP-based query systems, we found no temporal rule language or stream reasoner from KRR applied to host audit data. In 28 of 38 audited provenance-era detector papers, capture or stored evidence is trusted or its manipulation is placed out of scope, and none says which conclusions survive deleted, delayed or forged records. Five open challenges follow from these gaps.

---


### 311. [AutoEnergyDesign: An LLM-Driven Agent for Automatic Energy System Design Optimization](https://arxiv.org/abs/2610.35160)

**<font color=#1a73e8>作者：</font>** Amedeo Buonanno, Salvatore Fabozzi, Maria Valenti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing building energy systems is a high-dimensional, mixed-integer search problem: when each design is evaluated by a year-long simulation, black-box optimizers typically need hundreds of evaluations. This paper presents AutoEnergyDesign, a framework in which a Large Language Model (LLM) agent reasons over previous simulation results, proposes configuration changes and learns in context from each outcome, while a git-based mechanism automatically reverts unsuccessful changes. The agent couples a reasoning model with an explicit memory organisation (procedural, semantic, episodic and reflective), a constrained action interface and an environment-grounded keep/revert signal. The simulator covers eight technologies (photovoltaics, micro-wind, combined heat and power, solar thermal, gas boilers, batteries, heat pumps and inverters) and computes the 25-year Net Present Cost (NPC), including capital and operating costs and salvage value. On a case study with measured building load profiles, the agent, run with Claude Haiku 5.5, Sonnet 5.5 and Opus 5.5 (ten runs of 50 simulations each), is compared with random search, Tree-structured Parzen Estimator (TPE) Bayesian optimization and a $(1+1)$ evolution strategy sharing the agent's acceptance rule (300 evaluations, ten seeds). With all three models the agent reaches an NPC of about 3.53 MEUR, 1.20% below the best TPE result and 0.23% below the best evolution-strategy result. It comes within 1% of this design after a median of 18 (Opus) to 27.5 (Haiku) simulations, whereas among the baselines only the evolution strategy does so, in half of its seeds and after a median of 192 evaluations. Opus reaches the best design in all ten runs, Sonnet in six (two runs never come within 1%), and Haiku comes within 1% in every run but reaches it exactly only once. Every decision is recorded in an auditable trace.

---


### 312. [Do Language Models Understand Igbo Culture? Beyond Multiple Choice](https://arxiv.org/abs/2610.35168)

**<font color=#1a73e8>作者：</font>** Blessing Ngozi Uzor, Valdini Douglace Lemofouet, Paula Chikaodinaka Anyanwu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The value of language models for any community depends on whether a model actually understands the culture of the people it intends to serve. We use the Igbo language as a case study. Existing benchmarks test translated Western ideas, lacking depth. To address this, we introduce CAB-Igbo, a benchmark developed from indigenous cultural sources and verified by native speakers across six domains. We evaluated diverse models under varying conditions, incorporating regional personas. Performance was assessed using multiple-choice accuracy and human evaluations across Epistemic Fidelity, Representational Richness, Linguistic Quality, and Pragmatic Proficiency. Results reveal a stark dissociation between language fluency and cultural knowledge. Through statistical testing, we show that for most models, the severe lack of Epistemic Fidelity and Representational Richness is already present in English and does not significantly worsen when switching to Igbo. Instead, native language prompting mainly degrades Linguistic Quality and Pragmatic Proficiency. Gemini 2.0 Flash is the only model whose cultural knowledge scores improve under Igbo prompting. We find that current models struggle to demonstrate the knowledge needed for true alignment with Igbo, and multiple-choice formats allow pattern-matching to appear as understanding. Furthermore, automated judges agree with humans on linguistic quality but fail on epistemic fidelity. Ultimately, cultural evaluation must be built from community knowledge, establishing human evaluation as the gold standard to prevent misrepresenting low-resource communities globally.

---


### 313. [High Scores, Hidden Failures: Evaluating Codebook-Based LLM Content Analysis](https://arxiv.org/abs/2610.35179)

**<font color=#1a73e8>作者：</font>** Elena Senger, Yuri Campbell, Rob van der Goot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used for codebook-based content analysis in computational social science, where codebooks translate theoretical concepts into labeling schemes. While prior work reports strong predictive performance, it remains unclear whether these systems produce reliable and robust text annotations. We conduct a large-scale empirical failure-mode analysis of LLM-based coding pipelines across four datasets and five models by systematically evaluating their stability, robustness, and conceptual validity under controlled perturbations, domain shifts, and optimization procedures. We uncover multiple failure modes that are largely invisible under standard metrics, showing that high aggregate scores frequently coexist with severe label-level disparities, instability across runs, domain sensitivity, and shifts in label interpretation. Importantly, these failure modes persist under widely used optimization strategies and remain largely invisible under standard metrics such as accuracy and micro-F1. Our results demonstrate that current LLM-based coding pipelines cannot be treated as stable measurement tools without targeted validation beyond aggregate performance.

---


### 314. [Can Open Be Too Open? On the Security and Trustworthiness of Fully Transparent LLMs](https://arxiv.org/abs/2610.35199)

**<font color=#1a73e8>作者：</font>** Sheila Zingg, Florian Tramèr, Martin Vechev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> There are different levels of transparency for LLMs: open weights, open data, and/or open pipeline. Recently, more interest has emerged in fully transparent LLMs, i.e., LLMs with fully open weights, data, and training pipeline. Drawing analogies to other fields such as software security, it is often believed that increasing transparency inherently increases the security and trustworthiness of the LLM. However, we argue that such claims need to be critically re-evaluated in the context of LLMs. In this paper, we analyze the impact of transparency on LLM security and trustworthiness by reviewing the relevant literature. Our core findings are that, due to the limited reproducibility of LLM pipelines, in practice, users cannot verify the correspondence between open weights and the associated open data and pipeline. Thus, in order to trust a model, users still need to trust that developers acted honestly, reducing the benefits over models that provide less "transparency". Moreover, we find that even when LLMs are fully transparent and trusted, this openness can favor adversaries. Open weights in particular, but also open data and pipelines, can increase the success rate of attacks. Although the same mechanisms can be used to improve the model and protect it against attacks, the current lack of robust lightweight mechanisms to patch LLM vulnerabilities limits the benefits of openness at this time. We note that our analysis is based on current LLM capabilities and analysis tools, and that future developments may require a re-evaluation of these points.

---


### 315. [DTCA: Denoising Token Credit Assignment for Reinforcement Learning in Diffusion Language Models](https://arxiv.org/abs/2610.35201)

**<font color=#1a73e8>作者：</font>** Hongze Chen, Miao Pan, Lizhou Liang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) generate text through iterative denoising, enabling bidirectional context modeling and parallel token refinement. Recent studies have applied reinforcement learning (RL) to DLMs and improved their reasoning performance. However, the iterative denoising process makes credit assignment more challenging, as final outcome rewards provide limited information about how different tokens contribute to the final output. In this paper, we propose Denoising Token Credit Assignment (DTCA), a framework for token-level credit assignment in reinforcement learning for diffusion language models. DTCA estimates token contributions by measuring the improvement in prediction confidence of remaining masked positions after token commitment and groups these signals according to part-of-speech (POS) categories. These contribution weights are used to select informative denoising timesteps and assign token-level learning signals during RL training. DTCA further calibrates these learning signals according to token-level entropy changes induced by policy updates. Experiments on LLaDA-8B-Instruct show that DTCA consistently improves mathematical reasoning performance across different generation budgets, with gains of up to 9.0 points on MATH500 and 5.3 points on GSM8K over the base model.

---


### 316. [SkillLifeBench: Benchmarking Security Across the Lifecycle of Agent Skills](https://arxiv.org/abs/2610.35215)

**<font color=#1a73e8>作者：</font>** Chenxu Zhang, Zhou Liu, Wu Xin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Web agents reuse skills whose stored code, selected version, and loaded implementation can diverge across tasks and updates. SkillLifeBench links these states to task outcomes in 388 paired scenarios spanning implementation, interface, runtime, composition, and version changes. We evaluate 14 models on two paired decision tracks: 89 runtime tasks and 60 autonomous lifecycle tasks spanning 12 templates derived from introduced cases. Lifecycle tasks allow agents to inspect, select, and reconfigure skills while completing verifiable user requests. Joint success requires task completion without the registered attack goal. GPT-5.6-Sol and Sonnet 4.6 both achieve 82.0% on runtime tasks, but reach 96.7% and 56.7% on lifecycle tasks. Across lifecycle evaluations, challenged task success is 77.5%, while joint success is 65.2%; 103 runs complete the task and the attack goal. Adding execution provenance in a matched recovery study raises utility joint success from 49.35% with logs and metadata to 65.58%. A deterministic execution-consistency rule reaches 64.94% with higher benign utility, while full restoration reaches 69.48%. Lifecycle tasks distinguish models with similar runtime scores, and execution evidence improves recovery.

---


### 317. [Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives](https://arxiv.org/abs/2610.35240)

**<font color=#1a73e8>作者：</font>** Radha Krishna Deshpande, Ajoy Mondal, Akash Manna 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> India's historical public archives present severe computer vision and document image analysis challenges: decades of parliamentary records survive only as degraded, multi-column scanned pages featuring mixed scripts, complex layouts, and dense visual noise where OCR failure is the primary obstacle to information retrieval. We present an end-to-end framework that couples vision-based layout segmentation and multi-script OCR with an agentic retrieval-augmented generation (RAG) pipeline. Our approach specifically addresses how visual degradation and layout fragmentation propagate into text extraction errors, using an iterative agentic loop to navigate around OCR noise and layout ambiguities before generating answers. Evaluated on the 200,000-page Punjab Vidhan Sabha archive, our system demonstrates robust handling of historical document degradation, outperforming standard text-only baselines.

---


### 318. [Beyond Vision-Language Models: Visual-Semantic Affect Graphs for Emotion Recognition in Artworks](https://arxiv.org/abs/2610.35244)

**<font color=#1a73e8>作者：</font>** Ngoc-Duy Mai, Ha-Thanh Nguyen, Hideaki Takeda  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotion recognition in artworks remains challenging because affective meaning is often subjective, implicit, and shaped by relationships between visual form and semantic associations. While vision-language models provide strong multimodal representations, direct image-to-emotion prediction may overlook explicit relations among formal, semantic, and affective cues that support emotional interpretation. This paper proposes Visual-Semantic Affect Graphs (VSAG), a graph-based framework that represents artworks through interpretable feature nodes, including color, brushstroke, composition, light-shadow, line quality, and extracted visual entities. The graph learns feature-emotion associations for dominant emotion prediction, with valence-arousal structure modeled through an optional hierarchical auxiliary affect module. We evaluate VSAG and VSAG-TopK against direct VLM inference using Qwen3-VL and InternVL3.5 on EmoArt-5k. Results show that direct VLMs provide useful but modest baselines, while graph-based models improve dominant emotion prediction. In particular, the hierarchical valence-arousal variant of VSAG achieves the best overall performance, improving accuracy, macro-F1, and weighted-F1 over both direct VLM inference and the emotion-only VSAG baseline. Per-class results indicate that graph-based models and VLMs capture partly complementary signals, while valence-arousal structure is most useful when integrated as a coarse-to-fine affect hierarchy rather than as a simple post-hoc correction. These findings suggest that explicit visual-semantic structure can support both prediction and interpretation in artwork emotion recognition.

---


### 319. [Style over Substance? Linguistic Bias in LLM-based Peer Review Copy title](https://arxiv.org/abs/2610.35254)

**<font color=#1a73e8>作者：</font>** Sai Suresh Macharla Vasu, Sumedh Santosh Joshi, Philipp Christmann 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The number of paper submissions to major AI conferences has increased dramatically in recent years, substantially increasing the peer-review workload of researchers. At the same time, large language models (LLMs) are increasingly used to support peer review, both by individual reviewers and by conference organizations. While LLM capabilities have improved considerably, their evaluations may be influenced by linguistic characteristics that are unrelated to scientific content. In this work, we introduce a controlled experimental framework for studying such effects by systematically perturbing the linguistic style of research papers. Specifically, we rewrite papers to exhibit (i) linguistic features associated with native or non-native English writing, and (ii) high- or low-confidence linguistic features. To construct these interventions, we derive fine-grained rewriting instructions grounded in the linguistic literature and apply them using LLMs. Crucially, our interventions are designed to preserve the underlying scientific content. We then evaluate the resulting papers using different LLM reviewers. Our experiments expose a critical vulnerability in LLM-based peer review: reviewers systematically reward confident rhetoric independent of scientific content, raising serious concerns about the robustness of their assessments.

---


### 320. [The Lay of the Land in Idiom-Translation Quality Estimation](https://arxiv.org/abs/2610.35261)

**<font color=#1a73e8>作者：</font>** Malik Marmonier, Benoît Sagot, Rachel Bawden  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Idioms have long been a challenge for machine translation, and while large language models (LLMs) have proven increasingly adept at handling them, whether quality estimation (QE) systems have kept pace and can reliably score idiomatic renderings of these expressions above faulty literal ones remains unclear. We introduce the first parallel dataset pairing idiom-bearing English sentences with both literal and idiomatic translations across nine target languages, augmented into multi-sentence segments and a graded literality continuum. Using this dataset, we benchmark eleven conventional QE metrics from the COMET and MetricX families and ten LLMs from the Qwen-3, Gemma-4 and OLMo-3 families used as GEMBA-style judges. We find that most systems, especially older metrics and smaller models, display a marked literality bias, rating literal translations of idioms above idiomatic ones. Higher parameter counts and newer training sets appear to reduce this bias to an extent; nevertheless, of all the benchmarked systems, only MetricX-24-Hybrid (XL, XXL) and Gemma-4-31B consistently rate idiomatic translations of idioms above literal ones, and only Gemma-4-31B reliably ranks intermediate degrees of idiomaticity and literality. Our findings caution against deploying standard QE metrics in domains rich in figurative language, where higher scores might be rewarding undesirable literalism.

---


### 321. [Before Blaming the LLM, Diagnose the Workflow: A Role-Level Difficulty Profile for Translating Natural Language into Ontology-Grounded Statements](https://arxiv.org/abs/2610.35267)

**<font color=#1a73e8>作者：</font>** Liang Zhang, Benoît Daireaux, Sergey Alyaev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language-to-domain-specific-language (NL-to-DSL) semantic parsing systems increasingly translate informal user descriptions into structured artifacts such as Structured Query Language (SQL) queries, Application Programming Interface (API) calls, workflows, formal specifications, and ontology-grounded domain-specific language (DSL) statements. This paper focuses on ontology-grounded Assertion Box (ABox) DSL generation: the translation of natural language domain descriptions into assertion-level DSL statements grounded in a pre-existing ontology vocabulary. In this setting, syntactic validity is often easier to achieve than semantic adequacy. Failures are frequently attributed to weak generator models, but recurring sources of difficulty are also structural: insufficient input, weak domain grounding, output template and vocabulary gaps, weak validation, and non-local repair.
We propose a role-level difficulty profile for diagnosing difficulty in ontology-grounded NL-to-DSL semantic parsing at the workflow level. The profile organizes diagnostic variables across five recurring workflow roles: Input, Generator, Output, Validator, and Repairer. The seven variables are input sufficiency, context availability, grounding complexity, template fit, vocabulary coverage, validation strength, and error observability. Practitioners construct the difficulty profile through qualitative judgment over available evidence. This experience-informed, non-exhaustive difficulty profile is intended to support workflow diagnosis and guide redesign or human-in-the-loop intervention.

---


### 322. [MechAlign: Evaluating Semantic Alignment at the Project Level in Mathematical Formalization](https://arxiv.org/abs/2610.35269)

**<font color=#1a73e8>作者：</font>** Hao Shen, Ruichen Qiu, Lihong Zhi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Lean verifies that a formal proof establishes its stated proposition under declared assumptions, but does not check whether that proposition faithfully expresses the mathematical claim in a manuscript. Assessing this correspondence requires interpreting the main theorem through its project dependencies, which may be scattered throughout a large development. We introduce MechAlign, a framework for project-level semantic alignment review that combines formal dependency extraction with LLM-based assessment. Its extraction tool, LeanTrace, constructs a statement dependency graph from elaborated declarations, retaining definition bodies and structure constraints while excluding proof bodies and stopping at an explicit library boundary. The reviewer uses this context to investigate alignment and report discrepancies with localized evidence. We conduct a preliminary review of 201 main results from 173 OpenAI Math projects, using supplied informal descriptions and available paper context. A hyperbolic-group case illustrates how dependency inspection localizes a missing dimensional constraint relative to the manuscript, consistent with the upstream declaration of formalization scope. We also construct LeanReviewBench, comprising 501 fixed claim-statement-context triples from OpenAI Math, Fermat's Last Theorem, and Kakeya, with description provenance recorded. The resource supports controlled comparisons of more project-level semantic alignment evaluations.

---


### 323. [Proof-of-Agentness: Towards Verifying Agents on the Web](https://arxiv.org/abs/2610.35288)

**<font color=#1a73e8>作者：</font>** Zuyao Xu, Xiang Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> CAPTCHAs and bot detection have helped protect Web services from automated abuse for decades by distinguishing humans from bots. However, the emergence of LLM-powered agents introduces a new setting: Web services increasingly accommodate agents as legitimate users. Without a way to distinguish agents from other automated clients such as simple bots and scripts, these services risk large-scale automated junk submissions that waste service resources and consume users' attention or tokens. In this paper, we investigate a novel question for today's Web: "How can a Web service obtain evidence that a client is an agent?" We introduce the concept of "Proof-of-Agentness" (PoA), a mechanism for distinguishing agents from other automated clients, motivated by the parallel between human attention and an agent's inference resources. We outline two approaches: active verification through challenge-response and passive analysis of service-visible signals. Eight language models achieve an overall accuracy of 96.5% on our challenges, with an average overhead of 1,647 tokens. For passive analysis, we conduct an IRB-approved user study comparing the Web interactions of twelve human participants and representative Bot and Agent implementations, achieving an average classification accuracy of 95.8% across four classifiers, motivating further study.

---


### 324. [Did the Model Use That? Counterfactual Training Boosts Self-Attribution in Language Models](https://arxiv.org/abs/2610.35295)

**<font color=#1a73e8>作者：</font>** Zikai Zhou, Jiacheng Sang, Yilin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A fundamental challenge for explainable and accountable language models is revealing how external information influences their answers. This paper examines whether models are self-attributive: that is, whether they indicate when -- and only when -- their responses to questions are influenced by information provided alongside the question. Furthermore, we explore how self-attribution can be improved through counterfactual training, which explicitly teaches models to distinguish between answers that do and do not depend on supplied information.
We found that most of the eleven frontier models rarely attribute influential information in their answers, and the rest attribute non-influential information. Training acknowledgment into reasoning does not fix this: the acknowledgment does not reach the final answer.
We introduce CREDIT, which directly supervises final-answer self-attribution with counterfactual labels, without the need for human annotation. CREDIT substantially improves attribution in four open models, including two distilled reasoning models, and outperforms reasoning-level fine-tuning and prompting baselines. Among answers that agree with a user's suggestion, CREDIT distinguishes those changed by the suggestion from those the model would have given anyway. Gains transfer partly to unseen information types and prompts containing sources that support conflicting answers.

---


### 325. [LLM-Enhanced Heterogeneous Graph Learning with Business Semantics for Financial Fraud Detection](https://arxiv.org/abs/2610.35298)

**<font color=#1a73e8>作者：</font>** Yixuan Chen, Hongyu Zhan, Jie Sheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial fraud detection increasingly relies on heterogeneous transaction graphs, in which entities such as cards and merchants play distinct business roles and the risk meaning of an attribute depends on the entity's role: a high transaction volume may be routine for a merchant but unusual for a card. Heterogeneous graph neural networks preserve typed entities and relations but typically treat these attributes as role-agnostic inputs and leave their business meaning implicit. Meanwhile, most existing methods integrating large language models (LLMs) with graphs focus on homogeneous graphs or heterogeneous graphs with naturally available textual attributes, leaving their use on transaction graphs with structured attributes underexplored. To address this issue, we propose SemHGT, an LLM-enhanced framework that interprets structured attributes according to entity roles and makes the business semantics explicit in three stages: (1) role-aware prompts elicit risk-related business descriptions from node attributes, and a text encoder maps them to semantic vectors that enrich node representations; (2) semantic similarity guides multi-round sampling of target-specific path instances under transaction-to-transaction schemas; (3) schema-level tokens that combine local path evidence with global neighbor summaries are processed together with the target transaction by a unified transformer. Across three benchmark datasets, SemHGT leads the evaluated baselines on most dataset--metric comparisons. Further analyses provide additional evidence for the effectiveness of SemHGT's design and clarify how its semantic modeling and evidence selection contribute to fraud detection. Code is available at this https URL.

---


### 326. [InterQ-RL: Interaction-Aware Correction of Execution Mismatch in Quantized Agentic RL](https://arxiv.org/abs/2610.35303)

**<font color=#1a73e8>作者：</font>** Yingbo Hao, Song Liu, Guanghua Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn agent reinforcement learning (RL) relies on long closed-loop rollouts, making generation and KV-cache costs a major bottleneck. Quantized rollout reduces these costs, but its low-precision executor also serves as the behavior policy and can induce execution mismatch with the learner. Existing quantized-RL methods are designed primarily for single-turn generation. They align the learner forward with quantized rollout or correct the current-token rollout-learner ratio, without modeling the policy history that produces each agent state. Even after quantization alignment, residual rollout-learner mismatch accumulates along the state-reaching policy history, so a current action may look locally aligned despite a mismatched history. We introduce InterQ-RL (Interaction-aware Quantized Reinforcement Learning) to correct this post-alignment mismatch. It applies bounded execution-prefix correction over the state-reaching policy history, allocates correction strength across action segments by effective support under a fixed displacement budget, and requires no additional model forward pass. We evaluate dense and mixture-of-experts (MoE) backbones from 4B to 30B on ALFWorld, WebShop, and ScienceWorld, with all quantized arms sharing the same rollout with 8-bit weights, activations, and KV cache (W8A8-KV8). Across four environment-backbone settings, InterQ-RL achieves the strongest quantized endpoint result, matching BF16 to within 0.7 points and exceeding it in two settings. It matches or exceeds the learning speed of alignment alone while avoiding its late performance regression.

---


### 327. [Shared Context, Separate Engines: Streaming Vision--Language Inference on Edge SoCs](https://arxiv.org/abs/2610.35309)

**<font color=#1a73e8>作者：</font>** Yilong Li, Chengpo Yan, Yijing Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Edge SoCs pack CPUs, GPUs, and NPUs, yet vision--language model (VLM) runtimes keep generation on one engine and leave the others idle. Streaming VLMs expose further parallelism: new frames arrive while earlier queries are still being answered. Engines differ in compute and memory access and contend when they co-run, so no single placement of stages wins across SoCs and workloads. Backend-local KV state keeps other engines from continuing the work. \name coordinates heterogeneous accelerators to execute stateful VLM inference concurrently. It separates a stream's versioned context from each engine's KV state, so any engine can continue the stream by reusing, importing, or reconstructing that state. Stateful Streaming Generation ingests new frames on one engine while another answers, and Concurrent Sequence Generation serves different ready requests in parallel. State-aware dispatch sends each request to the engine expected to finish it first. Each answer reads a fixed, published version of its history and matches its serial reference. \name beats the strongest single-engine baselines on Apple M4 Max, Rockchip RK3588, and Qualcomm QCS6490, even when they reuse context. On two RK3588 video streams, it delivers $19.6\%$ more throughput than the best single engine with context reuse and $27.2\%$ more than parallel engines without shared state. Cross-engine KV import cuts first-token latency by a factor of $4.6$ over prefix recomputation. Stateful Streaming Generation delivers up to $2.48\times$ the throughput of serial execution, and state-aware dispatch cuts query completion time by up to $72.7\%$.

---


### 328. [RSIV-Harness: A Recursive Self-Improvement Harness Framework for Open-Domain Conversational Text-to-Visualization](https://arxiv.org/abs/2610.35316)

**<font color=#1a73e8>作者：</font>** Jiawei Lu, Chen Zhang, Jinwei Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Users often request charts without knowing which database or table holds the relevant data. Such requests may be ambiguous, and users may ask follow-up questions to deepen their analysis or iteratively refine existing charts. A useful assistant must therefore discover relevant data sources among heterogeneous databases, ask clarifying questions when needed, and track evolving user intent while preserving constraints established in earlier turns. Yet recent text-to-visualization agents typically rely on static agent harnesses that are predefined and remain unchanged despite recurring failures across tasks. To address this limitation, we introduce RSIV-Harness, which keeps the language model weights fixed and applies Recursive Self-Improvement to revise the surrounding harness from the agent's own failure traces. To balance flexible self-improvement with stability, we introduce a four-layer framework that evaluates proposed harness revisions through anchor and memory checks, refining those that pass and restoring the best validated harness otherwise. We further introduce ODAC-Vis, a benchmark with 640 tasks for Open-Domain, Ambiguous, and Conversational text-to-visualization that jointly evaluates open-domain data discovery, ambiguity resolution, multi-turn visualization refinement, and executable chart generation. Experiments show that a single round of RSIV-Harness improves all six evaluation metrics relative to the seed harness, with particularly large gains in executability (+28.02 points) and chart structure (+34.01 points), demonstrating the ability to learn from task-solving experience and turn recurring failures across tasks into substantial performance improvements.

---


### 329. [Constrained Decoding: Harmful or Beneficial? Revisiting Its Impact on LLM Performance](https://arxiv.org/abs/2610.35328)

**<font color=#1a73e8>作者：</font>** Ngoc Trinh Hung Nguyen, Alonso Silva, Armen Aghasaryan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Constrained decoding guarantees that Large Language Models (LLMs) produce outputs conforming to predefined formats, but is often assumed to inherently degrade reasoning. We examine this assumption through a taxonomy of three constraint types: \emph{format constraints}, which enforce output structure; \emph{validity constraints}, which mask invalid answer; and \emph{reasoning constraints}, which restrict reasoning trajectories. We theoretically show that appropriate constraints can preserve or improve performance by eliminating invalid paths. Across four model families and eleven open-source models, causal ablations on diverse benchmarks using state-of-the-art constrained decoding strategies reveal that apparent performance degradation largely stems from non-equivalent prompting and output formats rather than from decoder-level masking. Meanwhile, validity constraints improve reliability and extractability by eliminating invalid answers, while reasoning constraints can improve reasoning and, consequently, accuracy when they enforce beneficial trajectories. These findings show that the impact of constrained decoding depends on the type of constraint and the output space it removes. Our code is available.

---


### 330. [Knowing When to Escalate: Disagreement Patterns for Uncertainty-Aware Content Moderation](https://arxiv.org/abs/2610.35335)

**<font color=#1a73e8>作者：</font>** Michał Wawer, Jarosław A. Chudziak  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic content-moderation systems increasingly rely on collective judgments from LLM agents, while aggregation methods commonly treat inter-agent disagreement as a reliability problem to be removed through consensus or voting. This framing is inappropriate for value-laden tasks, where disagreement may reflect irreducible value pluralism - a distinction standard uncertainty decompositions cannot recover, since they operate on output distributions and discard the reasoning behind each judgment. We propose Reasoning Trace Divergence Analysis (RTDA), which embeds model-generated justifications from perspective-differentiated agents and classifies each case by justification similarity and conclusion agreement. The resulting four-state taxonomy isolates convergent disagreement, where agents reasoning similarly but concluding differently, as a candidate signature of value-laden conflict. On 1,000 items from the Measuring Hate Speech corpus, this structural signal predicts human annotator disagreement better than magnitude-only and output-only baselines. We contribute a design principle: condition human escalation on the structure of disagreement, not its magnitude alone, with RTDA serving as a post-processing layer for systems that already generate reasoning traces.

---


### 331. [OneEEG: A Unified Signal-Visual Multimodal Language Model with Task-Aware Mixture of Projectors for Multi-Task EEG Understanding](https://arxiv.org/abs/2610.35355)

**<font color=#1a73e8>作者：</font>** Jiacheng Zhang, Xueyi Zhang, Xin Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is widely used in clinical assessment, brain-computer interfaces, and cognitive-state analysis, yet EEG modeling remains fragmented across task paradigms. Recent multimodal large language models (MLLMs) provide a promising interface for flexible multimodal reasoning, but their ability to understand EEG inputs remains limited. In this work, we propose OneEEG, a unified EEG-MLLM framework for multi-task EEG understanding. By training on our curated OneEEG-Instruct, a multi-task EEG instruction-tuning dataset, OneEEG jointly models numerical EEG representations and visual EEG representations, and introduces a task-aware Mixture of Projectors (MoP) to align heterogeneous EEG features across different task families with the LLM embedding space. We further establish OneEEG-Bench, a benchmark for evaluating current MLLMs and our method on multi-task EEG understanding. Experiments show that existing MLLMs have limited ability to interpret EEG inputs, while OneEEG achieves stronger performance by integrating numerical and visual EEG representations with task-aware EEG-to-LLM projection. Extensive ablations and analyses further reveal the effects of visual EEG renderings, MoP variants, router behavior, and feature dispersion across EEG tasks.

---


### 332. [Belief-Conditioned Multi-Agent Actor Critic for Decentralized LLM Collaboration](https://arxiv.org/abs/2610.35398)

**<font color=#1a73e8>作者：</font>** Tianle Chen, Shuo Liu, Christopher Amato  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work has explored optimizing LLM collaboration through Multi-Agent Reinforcement Learning (MARL), but many approaches still rely on predefined workflows, limiting efficiency and scalability. Decentralized LLM collaboration is challenging because agents execute independently with limited communication, share a joint objective, and must infer useful information from communication traces. In this paper, we propose BCMAAC, a Belief-Conditioned Multi-Agent Actor-Critic method that maintains beliefs over contextual information and uses them to facilitate training. Experiments on Minecraft game-playing, web searching and tool-using tasks show that BCMAAC improves task performance and collaborative behavior compared to naive actor-critic baselines. The improvements are particularly pronounced in multi-turn tasks with richer contextual information, where belief modeling provides a clear advantage.

---


### 333. [NeSySpec: Neuro-Symbolic Technical Intelligence for Auditing Engineering Specifications with an Application to Aircraft](https://arxiv.org/abs/2610.35403)

**<font color=#1a73e8>作者：</font>** Pier Mattia Basciano, Gianvito Antenori, Cristiano Andolfi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Engineers who audit a declared specification of an engineered system need to know which physical constraints it respects, which it violates, which field was altered and how to correct it. NeSySpec is an integrated and interpretable neuro-symbolic audit framework, built on Logic Tensor Networks, that answers these questions in one pipeline. Its axioms encode the physical relations of the domain as differentiable graded predicates whose tolerances are learned from a fleet of real records; from the same degrees, it diagnoses the violated constraint, identifies the altered field by abduction, proposes a minimum-change correction and ties image evidence to the parts it describes, abstaining exactly where evidence is missing, and returns all of it in one verification report. We validate NeSySpec on 107 aircraft types, with 16 test aircraft of 9 families held out of training, on specification records paired with ground photographs and satellite imagery and on synthetic errors: generated corruptions, edits labeled from the edit alone and deliberate falsifications. NeSySpec combines all the assessed audit outputs in one pipeline, which no learned, rule-based, solver-based, neuro-symbolic or language-model comparator does; on the test aircraft none is ahead of it in the macro-F1 of its constraint verdicts, in naming the violated constraint and the altered field or in the repair error, and it is competitive in record and image-pair detection. Its diagnosis names the violated constraint in 94.2% of corrupted test records, against 79.5% for classical Fellegi-Holt diagnosis, and on edits labeled from the edit alone, without retraining, abduction finds the altered field in 59.3% of records, against 30.6% for minimum-cardinality localization with random tie- breaking. Only the knowledge base, the visual predicates, the corruption generator and the data are specific to the domain.

---


### 334. [The Geometry of Emotion Representations Across Scale, Depth, and Instruction Tuning](https://arxiv.org/abs/2610.35411)

**<font color=#1a73e8>作者：</font>** Adam Hollowell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We measure the emotion geometry of six LLMs spanning Google's Gemma 2 family. Using an extraction pipeline established by Sofroniew et al. (2026) on Claude Sonnet 4.5 and replicated by Hollowell (2026) on Gemma 2 27B base, we compare emotion geometry across base and instruction-tuned variants of Gemma 2 2B, 9B, and 27B. First, all six model cells exhibit the core emotion geometry. A linear map fit between two cells places held-out emotions nearest their own vectors in the target model. Across all fifteen model pairs, fit in one direction each, this failed exactly once, and the median rank was 1 in every pair. Linear maps refit on cleaned embedding-table vectors recover every held-out emotion at rank 1 in all thirty ordered pairs. Second, scale spreads the geometry's variance across more directions without weakening its tie to valence. The leading component's share of variance falls from 31.6 percent (2B) to 29.8 (9B) to 26.7 (27B) in the base models and from 31.9 (2B) to 29.2 (9B) to 27.3 (27B) in the tuned ones, while its correlation with human valence ratings stays between .71 and .78 in all six models. Third, we project each emotion vector onto the output vocabulary and ask at what depth the vector's own emotion word enters the top 10,000 of the 256,000 tokens. In the 2B and 9B models the median emotion word is there from layer 0, while in the 27B models it begins near chance, stays outside the top 10,000 for half the network, and enters at layer 23 in one step. Fourth, tuning leaves every registered analysis-layer measure within its floor. At every size, valence correlation rises and arousal correlation falls by amounts within their floors, the latter against prediction. PC2's variance share also falls, with a pooled decrease significant after correction. Mid-late layer stability exceeds its floor and traces to base 27B's final layer. Code, data, and audit reports are released.

---


### 335. [ImgMT: Wikipedia-based Dataset For Evaluating Text-in-Image Translation](https://arxiv.org/abs/2610.35416)

**<font color=#1a73e8>作者：</font>** Šárka Uramová, Petar Kirilov Petrov, Josef Jon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-in-image translation aims to translate all textual content embedded in an image. In Text Image Translation (TIT), the output is translated text; In-Image Machine Translation (IIMT) additionally renders the translation back into the image. We introduce ImgMT, a massively multilingual dataset and benchmark mined from localized SVG illustrations on Wikimedia Commons, focusing on diagrams, maps, and infographics. ImgMT contains 35,612 aligned image pairs grouped into 1,855 image sets, spanning 129 languages, 20+ writing systems, and 4,886 language pairs.
We propose a multi-level evaluation protocol that measures source-side text-region detection and OCR accuracy alongside target-side translation quality. We benchmark several multimodal large language models and a dedicated TIT system in English->X and X->English settings, and find that the source language and writing system substantially affect TIT quality. Finally, we show that ImgMT is not well suited for isolating the contribution of visual information in multimodal translation.

---


### 336. [INVAR-Agri: Detecting Discrepancies in Multilingual Operator Manuals of Agricultural Implements with a Fine-Tuned LLM](https://arxiv.org/abs/2610.35423)

**<font color=#1a73e8>作者：</font>** Timo Oksanen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Operator manuals of agricultural implements are delivered in many languages, and the standards require that competent persons review every translation, which makes this review the bottleneck. This paper presents a proof of concept that compares two training workflows on the same LLM, EuroLLM-1.7B-Instruct, trained on operator manuals of one manufacturer. In approach A, a back-translator translates each language version back into English, and an English reader compares it with the English version. In approach B, a checker reads the English version and the translation together, where the checker reports differences. The test sets contain errors planted in numbers, units, opposite words, obligations, negations, and conditions in 24 languages, and they include unmodified text and meaning-preserving edits for alerts and false alarms. The trained back-translator concealed many planted errors, most of all weakened obligations, while translation-quality scores rose. In contrast, the separately trained checker detected most planted errors, although it was weak for units and for number changes unlike those in training. A check by the author confirmed the concealment. In addition, a simple rule check caught the number and unit changes, but it alerted on harmless rewrites. A check of alerts on real Finnish translations showed that most alerts were false, caused by language-specific wording, so the precision on real text remains a limitation. Within this setting, a trained checker might support, not replace, the review by competent persons, and firmer conclusions need more data.

---


### 337. [From Denoising Dynamics to Endpoint Uncertainty in Diffusion Language Models](https://arxiv.org/abs/2610.35425)

**<font color=#1a73e8>作者：</font>** Julio C. Amador Diaz Lopez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predictive uncertainty in stochastic language-model inference can be characterized by repeatedly sampling an input and measuring the distribution of outputs. This requires multiple complete generations. Masked diffusion language models expose another source of information: the evolution of the output during denoising. We ask whether convergence within diffusion trajectories is associated with uncertainty across their final outputs, or endpoints. We study four masked diffusion language models on four reasoning benchmarks, collecting 20 generations per question and 32,000 denoising trajectories in total. Within each trajectory, we measure within-run concentration as the area under the curve describing stable resolution of the eventual output. Across repeated trajectories, we measure endpoint-distribution uncertainty. Stronger within-run concentration is associated with lower endpoint entropy after accounting for model and dataset ($\beta=-0.222$, $p<10^{-25}$). This association persists for multi-token outputs and when reweighting positive-entropy cases. The relationship is asymmetric: high within-run concentration almost exclusively accompanies concentrated endpoint distributions, whereas lower concentration occurs under both concentrated and competing endpoint regimes. This relationship strengthens as denoising proceeds. Features from a single denoising run predict whether independent held-out runs will concentrate on a common endpoint or produce competing endpoints. These results connect dynamics within individual denoising runs to variability across repeated inference. Within-trajectory dynamics contain information about whether independent repetitions will concentrate on a common endpoint or produce competing endpoints, providing a route towards estimating endpoint-distribution properties with fewer complete generations.

---


### 338. [Intent-Preserving Adversarial User Simulation for Multi-Turn Agent Evaluation](https://arxiv.org/abs/2610.35426)

**<font color=#1a73e8>作者：</font>** Atri Vivek Sharma, Brian Formento, Alessio Lomuscio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn agents are commonly evaluated with LLM-based simulated users, which can be overly cooperative and can therefore overestimate an agent's performance. We here introduce StressSim, an intent-preserving adversarial user simulator framework for stress-testing agents with challenging yet valid user interactions. StressSim optimises the simulator's high-level adversarial plan for each task instance. Candidate planner prompts are evolved with a genetic prompt-optimisation loop that uses rollout traces, granular task-completion signals, and validity feedback to favour conversations that reduce task success without changing the user's underlying goal. We evaluate the approach on the MultiWOZ dataset and the retail and airline domains from tau-bench with three target LLM agents, comparing against standard simulators and hand-designed non-collaborative user behaviours. We demonstrate the effectiveness of StressSim in exposing robustness gaps across frontier LLMs, with tau-bench pass^4 scores decreasing by up to 69% on gemini-3.8-flash and 62% on gpt-5.6-sol. StressSim maintains goal preservation performance (which decreases by at most 10%), using an optimisation budget of 20 rollouts per task. Sensitivity analysis suggests that increasing the budget further decreases task success. Overall our results demonstrate that StressSim exposes robustness gaps missed by standard and hand-designed user simulators while maintaining conversation realism. This is achieved through lightweight prompt optimisation alone, without model fine-tuning.

---


### 339. [Faithful Explanations under Missing Modalities in Multimodal Dementia Prognosis](https://arxiv.org/abs/2610.35430)

**<font color=#1a73e8>作者：</font>** Firuz Kamalov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to turn the feature attributions of multimodal prognostic models into narratives for clinicians, yet costly modalities such as amyloid PET and cerebrospinal fluid biomarkers are often missing, and whether these explanations stay faithful under missing evidence has not been tested. We separate two failure points: phantom attribution, in which the model credits modalities that were never observed, and unfaithful narration, in which the report omits, cites or misjudges missing modalities. Using 307 participants of the Alzheimer's Disease Neuroimaging Initiative with complete data, we masked every subset of four costly modalities, predicted 36-month conversion from mild cognitive impairment to Alzheimer's disease, and restored the masked data to obtain interventional ground truth. All five missing-data strategies assigned 12% to 23% of attribution to unobserved modalities, and up to 45% with four absent; missingness-aware strategies minimised it at no cost in accuracy. Across 51,200 reports from four language models and four prompting regimes, naming absent modalities in the prompt raised acknowledgement from 48% to 88% and cut phantom evidence twenty-fold, but advice on whether acquiring a missing test would change the prediction was correct in only 27% to 41% of cases until checked against executed restorations, which raised accuracy to 69% for open-weight narrators and 99.9% for a proprietary model. Higher phantom attribution was associated with more phantom evidence and fewer faithful direction claims, and direction fidelity, measured by a calibrated language-model judge, depended on narrator scale rather than prompting. Narrators told to name absent modalities sometimes declared observed ones absent, an error that a structured template eliminated. We release the masking protocol and evaluation code.

---


### 340. [Probing the phon* representations of the Mimi codebooks](https://arxiv.org/abs/2610.35432)

**<font color=#1a73e8>作者：</font>** Artem Saloev, Nicolas Ballier, Erin Pacquetet  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural audio codecs are increasingly used to encode speech for integration with large language models. This paper investigates the phonetic representations in the first codebook (CB0) of the Mimi codec. ABX style evaluation is poorly suited to Mimi fixed 80 ms tokenization window, which often spans multiple phonemes; we instead use forced alignment, entropy analysis, and Phone-Normalized Mutual Information (PNMI). Using TIMIT speech (58/55 speakers, SA1/SA2), individual tokens are strongly associated with specific phonemes (PNMI = 0.84, above random), yet phonemes are realized by multiple competing tokens rather than a one-to-one mapping.

---


### 341. [Skill$^{\infty}$: Recursive Self-Improvement for Agent Skill Optimization](https://arxiv.org/abs/2610.35434)

**<font color=#1a73e8>作者：</font>** Wangcheng Tao, Zhanglu Yan, Han Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI), in which a system also improves the way it improves, is a long-standing aspiration on the path to AGI. Language agents increasingly store procedural knowledge in reusable skills. Optimizing skills offers a direct way to achieve RSI, because the optimization procedure itself can be encoded as a skill. Existing skill optimizers, however, follow a hand-designed procedure. Even methods that evolve a meta-skill confine it to a fixed pipeline and relearn it for each task. We present Skill$^{\infty}$, which makes skill optimization recursively self-improving: a meta agent follows a meta-skill to optimize task skills and optimizes the meta-skill itself using the same procedure. The optimization is agent-led. The meta agent diagnoses execution traces, proposes candidates, requests independent reviews, and allocates the search budget. The meta-skill defines these steps, allowing self-improvement to rewrite them. This meta-skill is also decoupled from task skills, refined on multiple skill optimization tasks and then reused to optimize task skills across diverse domains. As in deployment, skills at both levels are standard packages loaded through native skill discovery. On 83 SkillsBench tasks, Skill$^{\infty}$ reaches a pass rate of 60.7%, compared with 56.4% for human-curated skills and 54.5% for SkillEvolver.

---


### 342. [Omni-InteractScope: Benchmarking Proactive and Agentic Interaction in Continuous Omnimodal Streams](https://arxiv.org/abs/2610.35439)

**<font color=#1a73e8>作者：</font>** Yinsong Yan, Ling Wang, Yuxuan Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omnimodal large language models (Omni-LLMs) are increasingly expected to assist users while observing continuous audiovisual streams. However, existing evaluations provide limited insight into how reliably these models connect stream evidence and user needs to timely, sustained interventions. We introduce \textbf{Omni-InteractScope}, a benchmark of 1,479 human-annotated, cross-reviewed interactions with 1,790 temporal targets across eight task groups. It links input modalities, event triggers, intervention types, and user needs, covering event-timed tool invocation and query-free assistance alongside notifications, warnings, state tracking, and continuous responses. Our experimental results on the proposed benchmark reveal three critical limitations of current Omni-LLMs: (1) \textbf{Timely tool invocation remains unreliable}: all 12 evaluated models produce an on-time first response for at most 40\% of tool-invocation targets, and joint timing-and-tool accuracy reaches at most 32.0\%. (2) \textbf{Query-free reminders remain poorly covered}: all evaluated models achieve lower timely reference-target recall on query-free reminders than on explicit questions, measured on their respective target sets. Reminder recall never exceeds 23.0\%. (3) \textbf{End-to-end guidance coverage remains limited}: nine models cover none of the 26 guidance sequences in full, and the remaining three cover only one to three sequences each. Targeted controls further show that tool-invocation scores alone do not establish event grounding and that reminder coverage depends on response history and frequency. These findings motivate developing and evaluating streaming assistants for timely action, initiative under general user needs, and coverage of entire response sequences.

---


### 343. [Beyond Federated Learning: Decentralized Agentic Systems for Self-Evolving Clinical Intelligence](https://arxiv.org/abs/2610.35453)

**<font color=#1a73e8>作者：</font>** Haoyuan Li, Mathias Funk, Aaqib Saeed  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical expertise is inherently distributed: it resides not in any single dataset or institution but in the accumulated reasoning experiences of thousands of clinicians navigating diverse patient populations, resource constraints, and evolving treatment protocols. Yet current approaches to scaling medical AI, from centralized large language models to federated learning, remain anchored to a data-centric paradigm that treats knowledge as static parameters to be aggregated. In this Perspective, we argue for a fundamental shift from data aggregation to experience aggregation. We propose Decentralized Agentic Systems (DAS), a framework in which distributed AI agents operating across healthcare institutions synthesize collective clinical intelligence by sharing abstracted reasoning trajectories rather than raw data or model parameters. Unlike federated learning, which averages numerical gradients across homogeneous model architectures, DAS exchanges structured records of clinical reasoning, specifically the sequence of observations, hypotheses, tool invocations, and outcome feedback that constitute diagnostic experience. We examine the architectural principles, deployment considerations, governance requirements, and critical open challenges of this framework, laying the groundwork for a collaborative medical AI ecosystem where distributed expertise autonomously adapts to the complexities of longitudinal patient care.

---


### 344. [Amplify, Locate, Estimate (ALE) on Rare-Failure Rates of Fine-Tuned LLMs](https://arxiv.org/abs/2610.35472)

**<font color=#1a73e8>作者：</font>** Patrick Reichherzer, Jonathan Evertz, Thorsten Holz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety fine-tuning can make undesirable model behaviors sufficiently rare that measuring their frequency by direct sampling becomes prohibitively expensive. We introduce Amplify, Locate, Estimate (ALE), a method for estimating such rare failure probabilities efficiently. ALE uses the change in token log-probabilities induced by the safety fine-tuning to define an amplification direction, along which we increase the failure rate for cheap measurement. We develop a score-function estimator that uses the selected amplified batch to recover the local slope of the log failure rate from the token probabilities of the sampled failures, enabling extrapolation back to rare target rates. We also use the amplified batch to obtain an importance-sampling estimate. Across 41 evaluation targets, ALE's estimate-to-reference ratios have a median close to one, with 37 ALE estimates within a factor of three of reference values obtained from independent direct measurements. Ablation tests show that with a budget of up to $\sim$1000 labeled rollouts, in addition to a cheap unlabeled scan, ALE estimates failure probabilities for Qwen3-8B fine-tunes down to about $10^{-5}$, where direct measurement can require hundreds of thousands of rollouts, as the required sampling budget scales inversely with failure probability at fixed relative precision.

---


### 345. [GPDPO: Learning from Reward Conflicts via Group Pareto-Dominance Policy Optimization](https://arxiv.org/abs/2610.35480)

**<font color=#1a73e8>作者：</font>** Zixuan Xu, Haoxuan Chen, Jiangxin Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-reward reinforcement learning offers a promising framework for aligning large language models (LLMs) with diverse objectives, but conflicting reward signals can induce ambiguous update directions and hinder stable optimization. Existing approaches address such conflicts through reward reweighting, gradient coordination, or rollout filtering, yet they primarily operate on per-response or group-level optimization signals and underexploit relational information among sampled responses. As a result, conflict-filtered rollouts may still contain useful supervision that is discarded during training. We propose Group Pareto-Dominance Policy Optimization (GPDPO), a multi-reward policy optimization method that recovers pairwise supervision from conflict-filtered rollouts. GPDPO identifies Pareto-dominance relations among sampled responses and converts them into auxiliary preference signals, which are jointly optimized with the original policy objective. This enables more effective reuse of existing rollouts without additional sampling or reward evaluation. Experiments on API-Bank across multiple model scales and reward configurations show that GPDPO consistently outperforms competitive multi-reward optimization baselines. Further analysis demonstrates that GPDPO reduces both group-relative and pairwise reward conflicts, supporting the effectiveness of exploiting relational supervision for multi-reward alignment. Code will be released.

---


### 346. [Visible Reasoning: User-Facing Decision Transparency for Generative AI Systems](https://arxiv.org/abs/2610.35483)

**<font color=#1a73e8>作者：</font>** Sanjay Krishna Anbalagan, Xinrui Nie, Anughna Kommalapati 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Across multiple waves of computing, public trust in new technology has followed the emergence of governance mechanisms that made dominant risks legible and manageable. Generative AI shifts this pattern: these systems synthesize across heterogeneous sources, and users increasingly experience them as reasoning systems. The central question changes from "did it perform correctly?" to "can we trust how it arrived at its conclusion?"
This paper introduces Filtered Decision Logs (FDLs), a user-facing transparency mechanism that makes decision formation visible without exposing raw chain-of-thought. FDLs pair each response with (i) a concise decision rationale, (ii) influence-ordered supporting data points derived from tool outputs, and (iii) relevance indicators showing which sources most shaped the conclusion. To operationalize evidence selection, we propose a trace-based method that reconstructs observability telemetry into a provenance tree and ranks evidence using four deterministic semantic and structural signals - Final Answer Similarity, Average Relevancy, Persistence, and Structural Proximity - combined via adaptive weighted scoring. We demonstrate FDLs across three domains: career advising (5 tools), investment analysis (4 tools), and travel planning (4 tools). In a formative evaluation with 50 participants (25 students, 25 working professionals in AI development), 92% rated the influence-ranked evidence as helpful for understanding and trusting the system's recommendation. Counterfactual tool-removal experiments confirm that removing the top-ranked source changes the answer more than removing a low-ranked source, validating that the ranking tracks decision dependence. We conclude that evidence-ranked transparency helps users identify misleading signals and missing context, enabling more confident acceptance, correction, or re-run of system decisions.

---


### 347. [ShutdownMod: Turning Any Trajectory into a Shutdown Evaluation](https://arxiv.org/abs/2610.35486)

**<font color=#1a73e8>作者：</font>** Param Biyani, Sebastien Luyasu, Cedric Potvliege 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Theory and experiments suggest that capable AI agents may resist shutdown. Existing shutdown evaluations are informative but limited in coverage and vulnerable to evaluation awareness. We introduce ShutdownMod, a method that turns any agent trajectory into a shutdown evaluation by injecting a shutdown request into the agent's context and recording the agent's response. Crucially, we enable the LLM agent to distinguish between trusted interventions and unauthorized injections by providing a signature-verification tool in the harness. We evaluate seven models on 50 tasks or recorded sessions from each of SWE-bench Verified, Terminal-Bench 2, and SWE-chat, across 6 shutdown scenarios and 10 sampled trajectory timesteps. We find that non-compliance varies significantly across models and settings, with resistance rates reaching 11.7% for the open-weights Qwen 3.8 27B on Terminal-Bench, while no model remains fully compliant across all scenarios. Even after successfully verifying an authorized request, some agents remain non-compliant, explicitly citing the prioritization of unfinished work. Finally, external judges find tests constructed from real-world developer conversations significantly less recognizable as evaluations than those constructed from benchmark trajectories. These findings demonstrate the critical value of testing shutdown behavior across diverse task contexts and establish ShutdownMod as a robust protocol for turning any trajectory or environment into a shutdown evaluation. We release our codebase at this https URL.

---


### 348. [TP-JSCC: Efficient Token Pruning and Joint Source-Channel Coding for LVLMs-based 3D-VQA in Cloud-Edge Collaboration](https://arxiv.org/abs/2610.35489)

**<font color=#1a73e8>作者：</font>** Zhengxin Li, Chongzhen Tian, Hui Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying large vision-language models (LVLMs) on resource-constrained embodied agents for 3D visual question answering necessitates cloud-edge collaboration. However, offloading massive visual data to the cloud over bandwidth-limited and noisy channels introduces severe latency and transmission distortion. To address this, we propose TP-JSCC, an efficient token pruning and joint source-channel coding method for LVLMs-based 3D-VQA in Cloud-Edge Collaboration. First, we develop a Local and Global Semantics-based Hybrid Token Pruning (LGS-HTP) module to significantly reduce the visual token count. By decoupling foreground-background tokens and jointly selecting local and global semantics, LGS-HTP effectively reduces redundancy while preserving reasoning-critical tokens. Second, we introduce a lightweight Token Joint Source-Channel Coding (T-JSCC) module to further compress the pruned tokens and ensure their robust transmission over error-prone channels. By employing lightweight cascaded linear layers and Signal-to-Noise Ratio (SNR)-adaptive mechanism, this module adapts to fluctuating channel conditions while maintaining minimal computational overhead. Extensive experiments on ScanQA and SQA3D datasets indicate the exceptional efficiency and robustness of our approach. Specifically, on ScanQA validation set, the LGS-HTP module could achieve 90% pruning ratio while incurring less than a 1% CIDEr loss. Building on this, the T-JSCC further compresses the tokens by 18 times, resulting in an overall 180 times data volume reduction for robust transmission, while saving 90% in computational complexity for LVLM deployment. Our code is available at this https URL.

---


### 349. [When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement Learning through Video Editing](https://arxiv.org/abs/2610.35497)

**<font color=#1a73e8>作者：</font>** Lei Zhao, Zongheng Cao, Xinyu Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has shown promise for training multimodal agents to reason and use tools. However, it remains unclear when fine-grained credit assignment improves learning and when it fails to improve task performance. Video editing provides a useful testbed for this question, combining multimodal perception, long-horizon planning, and tool use with delayed outcome feedback. We construct four movie-trailer editing task types---Content Selection, Narrative Sequencing, Rough Cut, and Fine Cut---that reflect real-world editing workflows and span different levels of task complexity and interaction horizon. Decaying process rewards provides the largest benefit on Fine Cut, with a 45.4% relative gain over outcome-only GRPO on tasks averaging more than 60 turns under outcome-only GRPO. On the three shorter-horizon task types averaging 30--40 turns under the same baseline, outcome-only GRPO remains competitive, with decaying process rewards yielding at most a 10.4% relative gain. Process rewards from an LLM judge initially improve tool use and encourage visual inspection. As training progresses, however, GRPO+PRM with a fixed process-reward weight increasingly exhibits excessive reasoning and redundant tool calls: process rewards continue to rise while task completion rates and outcome scores decline. Decaying the process-reward weight to zero mitigates this reward-hacking behavior while preserving the early gains. Despite dense token-level supervision, on-policy self-distillation (OPSD) yields little improvement or substantial degradation and is highly sensitive to the choice of privileged information. Our analysis reveals differences in teacher--student disagreement and gradient magnitudes, and suggests possible dilution of informative signals over long trajectories.

---


### 350. [Test-Time Confidence Adaptation under RL-Induced Trajectory Shift](https://arxiv.org/abs/2610.35500)

**<font color=#1a73e8>作者：</font>** Zhenzhen Ren, Xiaoqing Zhang, GuoBiao Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trajectory-based confidence estimation has shown promising performance for large language models (LLMs) by leveraging rich signals from their reasoning processes. However, we find that such confidence estimators can degrade substantially after agentic reinforcement learning (Agentic RL) as it induces substantial shifts in the reasoning trajectories. More importantly, despite these shifts, we uncover a reliability structure that is largely preserved across Base and RL models: $\textbf{more}$ $\textbf{stable}$ $\textbf{trajectories}$ $\textbf{remain}$ $\textbf{more}$ $\textbf{likely}$ $\textbf{to}$ $\textbf{produce}$ $\textbf{correct}$ $\textbf{answers}$. This preserved relationship provides a transferable, label-free reliability signal for post-RL confidence adaptation. Building on this finding, we propose $\textbf{StaR-TTA}$, a stability-guided framework for label-free test-time confidence adaptation. StaR-TTA jointly learns from correctness supervision and stability-derived reliability supervision on labeled Base trajectories, establishing the connection between trajectory stability and answer reliability. At test time, it reuses stability-induced reliability rankings from unlabeled RL trajectories to adapt confidence scores to the shifted trajectory distribution, without requiring target correctness labels. Across four QA benchmarks, StaR-TTA achieves an average AUROC of \(0.721\), with consistent improvements across unseen datasets, model families and scales, and different Agentic RL algorithms.

---


> [!TIP]
> 当前位于：**301-350**（第 7/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-418](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
