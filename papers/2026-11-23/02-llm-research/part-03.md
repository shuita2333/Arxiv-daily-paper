# 🧠 大模型相关研究 | 2026年11月23日

> 本类共 **266** 篇论文：已确认 **245** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

---

### 101. [The Coverage Selection Gap: Ranking, Not Generation, Limits LLM Rubric Construction](https://arxiv.org/abs/2611.25557)

**<font color=#1a73e8>作者：</font>** Ali Karkehabadi, Jamshid Hassanpour, Rafael E. Banchs  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Task-specific rubrics are increasingly used to evaluate open-ended language-model outputs, yet constructing comprehensive evaluation criteria from complex source documents remains challenging. We study automatic rubric construction in professional mergers and acquisitions (M&A) due diligence, where evaluation criteria must be inferred from task instructions and supporting documents without access to an expert-authored reference rubric. We introduce a multi-axis generation framework that explores complementary structural and free-form views of the source evidence to construct a broad pool of candidate evaluation criteria. To distinguish failures of criterion discovery from failures of candidate selection, we introduce the coverage-selection gap, which measures the difference between reference-free ranking and a reference-informed greedy diagnostic under a fixed selection budget. Developed on 16 tasks and evaluated on four held-out tasks, our framework achieves 0.876 macro recall against senior-authored reference rubrics under an LLM-based criterion-equivalence protocol. Ablation studies further show that introducing new structural search axes improves recall by 6-10 percentage points, whereas increasing generation volume along existing search directions yields at most 1.5 points. These findings suggest that, once a high-coverage candidate pool has been constructed, effective reference-free selection becomes a substantial bottleneck in document-grounded rubric construction.

---


### 102. [Is a Description Worth a Thousand Demonstrations? Specificity and Reliability of Task Descriptions in In-Context Learning](https://arxiv.org/abs/2611.25560)

**<font color=#1a73e8>作者：</font>** Bruce Nguyen, Bei Jiang, Linglong Kong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A prompt for in-context learning (ICL) can describe a task in addition to, or instead of, demonstrating it through examples. Yet how task descriptions work remains poorly understood theoretically. Through the Bayesian view of ICL, we model descriptions as informative priors characterized by their specificity and reliability. We adapt the effective sample size (ESS) from Bayesian statistics, quantifying a description's predictive value as an equivalent number of demonstrations. For in-context linear regression, we show that a reliable description's ESS grows with its specificity and with the task's dimension. A description that may be irrelevant, however, gains little from its specificity unless demonstrations are given. In practice, do in-context learners use descriptions as a Bayes-optimal predictor would? Our experiments show that meta-trained Transformers come close to the Bayes-optimal ESS when tested on their training distribution. Pretrained language models, however, make too little use of highly specific descriptions when answering without reasoning; most of them closely match the Bayes-optimal predictor only when reasoning is enabled. These results extend the Bayesian analysis of ICL from demonstrations to descriptions.

---


### 103. [Reinforcement-Aligned Probabilistic Weather Forecasting with Discrete Tokens](https://arxiv.org/abs/2611.25570)

**<font color=#1a73e8>作者：</font>** Jinhan Li, Zhisheng Chen, Yuxuan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global medium-range weather forecasting must not only generate ensembles efficiently to characterize uncertainty in future states, but also serve downstream applications such as extreme-event warnings and cross-sphere coupled simulations. We introduce WeatherCraft, a framework that unifies probabilistic generation and reinforcement learning alignment through discrete weather tokens, bringing the GPT-style pretraining--post-training paradigm to global medium-range weather forecasting. A multiscale tokenizer represents atmospheric states as a coarse-to-fine token hierarchy, while a Transformer models causal dependencies across time and scale and predicts tokens within each scale in parallel. Direct sampling generates diverse ensembles, and exact token log-probabilities enable Group Relative Policy Optimization (GRPO) to maximize downstream task rewards without differentiating through evaluators or coupled models. On the ERA5 benchmark, WeatherCraft's eight-member ensemble mean reduces day-15 normalized RMSE by 17.6% relative to the strongest evaluated deterministic baseline and, with KV caching, achieves an approximately $18\times$ inference speedup over GenCast. Direct fair-CRPS adaptation improves ensemble probabilistic skill, while reward-based post-training improves forecasts of persistent land temperature extremes and coupled ocean heat extremes. This work establishes discrete autoregressive modeling as a general foundation for scalable, task-alignable Earth system foundation models.

---


### 104. [VidToC: Rethinking Video Token Compression for Multimodal Large Language Models](https://arxiv.org/abs/2611.25574)

**<font color=#1a73e8>作者：</font>** Zihan Xiao, Boshen Xu, Pei Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extending multimodal large language models (MLLMs) from images to videos faces substantial memory and latency challenges due to the massive number of visual tokens. These challenges have driven the development of numerous visual token compression methods and more efficient LLM architectures. However, existing compression methods are often evaluated with different training setups, tasks, and models, making fair comparison difficult. Meanwhile, the growing use of hybrid Mamba-Transformer architectures raises questions about whether compression strategies transfer across backbones. We present VidToC, a controlled evaluation framework for representative compression algorithms, LLM backbones, and time encoding strategies, covering training-free and fine-tuned settings on three complementary video understanding tasks. Our results reveal task-dependent compression behavior and characterize the effects of compression placement, time encoding, and backbone choice. These findings provide empirical guidance for designing and selecting video token compression strategies across tasks and training settings.

---


### 105. [Design and Evaluation of Epira: An Automated Interview System for Case Investigation and Contact Tracing](https://arxiv.org/abs/2611.25577)

**<font color=#1a73e8>作者：</font>** Ishita Asnani, Shaghayegh Fazliani, Zachary Ryan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: Case investigation and contact tracing are labor-intensive. Web forms struggle when respondents need clarification before disclosing contacts, and open-ended chatbots may deviate from protocols. We developed and evaluated Epira, a protocol-controlled large language model (LLM) interviewer for multi-disease case investigation and contact tracing.
Materials and Methods: Epira pairs LLM dialogue with a rule-based controller enforcing required questions, safety handoffs, and a structured case record, and adapts to new diseases by questionnaire upload. Local (Qwen2.5) and cloud (GPT-5.4) backends were tested. Study 1 used 108 simulated cases with ground-truth fields and contacts for measles and gonorrhea under Epira and open-ended conditions (864 sessions). Study 2 enrolled 72 volunteers in a 2$\times$2 disease-by-model interview assessing completion, usability, acceptability, and trust.
Results: Across Study 1, Epira with a local LLM captured 88.9% of required fields and 60.1% of ground-truth contacts. Open-ended interviewers recovered 31.1-41.9 percentage points fewer required fields than the same models in Epira. In Study 2, completion was 100%; mean adapted System Usability Scale (SUS) was 82.95 $\pm$ 16.17 on a 0-100 scale and mean trust was 3.85 $\pm$ 0.77 on a 1-5 scale.
Discussion: Protocol control drove completeness more than model choice. Local and cloud deployments produced similar records, supporting privacy-preserving local use with human review of routed interviews and missed contacts.
Conclusion: Epira recovers required fields and contacts under diverse disclosure conditions, works with local and cloud LLMs, and received favorable usability and trust ratings.

---


### 106. [AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development](https://arxiv.org/abs/2611.25582)

**<font color=#1a73e8>作者：</font>** Hang Zhang, Yuzhi Pan, Ziyao Zhong 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) is a well-established paradigm for augmenting large language models (LLMs) with information retrieved from external corpora. However, developing effective RAG systems requires substantial engineering effort and iterative experimentation, as effective design choices vary across tasks and domains. With rapid advances in LLM agent capabilities, we ask how well these agents can autonomously build RAG systems and how effectively they can improve them through iteration. In this paper, we propose AutoRAGBench, the first benchmark to evaluate how well LLM agents develop RAG systems from scratch in an open code space. It comprises nine RAG system development tasks. For each task, agents build RAG systems from scratch without starter code or prescribed strategies, under a six-hour budget on a single H800 GPU. They analyze task data, implement RAG pipelines, and iteratively refine their designs based on experimental feedback. We evaluate nine agent configurations and analyze both the effectiveness of the resulting RAG systems and their development trajectories. GPT-6.1 Sol with Codex CLI achieves the highest average score of 56.1. The composite Human-SOTA baseline averages 44.4. These results show that LLM agents can automate effective RAG system development. When starting from a human-designed system on each of seven tasks, GPT-6.1 Sol with Codex CLI improves the score by 16.6 points on average.

---


### 107. [DriftGuard: Online Memory-Drift Detection via Causal Attribution for LLM Agents](https://arxiv.org/abs/2611.25583)

**<font color=#1a73e8>作者：</font>** Licheng Pan, Yuzhou Chen, Zhixuan Chu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents rely on persistent memory to plan tool calls and complete multi-step tasks, which exposes them to memory drift: an adversarial or misleading memory alters the execution path and final outcome. In this work, we investigate online memory-drift detection, which estimates each retrieved memory's causal contribution to potential drift at serving time. We identify two fundamental challenges. (1) Content-level features are insufficient for causal memory-drift attribution, as perplexity or retrieval relevance alone cannot determine which retrieved memory would change agent behavior if neutralized; (2) Counterfactual attribution is prohibitively expensive for online detection, as it requires replaying downstream agent and tool execution for each candidate memory, exceeding real-time serving budgets. To address these challenges, we propose DriftGuard, a two-stage framework that decouples offline causal supervision from online estimation. Specifically, DriftGuard first constructs causal supervision through repeated paired counterfactual replays, continuing the original and single-memory neutralized trajectory suffixes from a shared pre-action state. The resulting annotations are aggregated by component-wise majority voting into a memory drift score (MDS) that captures action change, attack removal, violation removal, and task recovery. Guided by this supervision, DriftGuard then learns an online risk model that estimates MDS from pre-action information and flags drift-inducing memories via its maximum component risk, without online counterfactual rollouts. Extensive experiments demonstrate that DriftGuard accurately identifies drift-inducing memories and enables efficient online defense. Code is available at this https URL.

---


### 108. [Rubric Semantics or Numerical Priors? Auditing Scale-Direction Bias in LLM Judges](https://arxiv.org/abs/2611.25588)

**<font color=#1a73e8>作者：</font>** Chanwoo Kim, Doyun Kim, Minsoo Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent benchmark evaluations increasingly rely on Large Language Models (LLMs) as automatic judges. This paradigm assumes LLMs evaluate based on the rubric's semantic meaning rather than its numeric scale. We question this assumption by introducing semantic faithfulness: the principle that semantically equivalent rubrics must yield consistent scores. To quantify this, we propose a scale-reversal probe that inverts score anchors without altering evaluation criteria. Furthermore, we introduce floor normalization to calibrate reversal disagreement against intrinsic model variability, enabling fair cross-model comparisons. Experiments across five meta-evaluation benchmarks with seven diverse LLM judges spanning open-weight and proprietary models reveal widespread violations of semantic faithfulness, showing that raw reversal agreement alone is misleading. Finally, we demonstrate that bidirectional anchor averaging reduces dependence on any single anchor direction without compromising alignment with human judgments. Our findings emphasize that trustworthy LLM judges must reliably follow rubric semantics, not just correlate with human ratings.

---


### 109. [Measuring Hallucination in Large Language Models for Cyber Threat Intelligence: An Exploratory Study](https://arxiv.org/abs/2611.25590)

**<font color=#1a73e8>作者：</font>** Seungho Song, Donggyu Lee, Jaehan Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in cyber threat intelligence (CTI) tasks, such as summarization and question answering. However, they may produce hallucinations, false or misleading content not grounded in the source text, which can mislead analysts and corrupt downstream security decisions. This paper presents an exploratory measurement study of hallucinations in LLM-based CTI. We introduce HalluVision, a reproducible framework that generates LLM outputs, extracts domain-specific entities using a fine-tuned named entity recognition model, and evaluates factual consistency using multiple similarity metrics. Using 4,940 real-world cybersecurity articles, we measure hallucinations in outputs from two commercial LLMs and one open-weight LLM. Measurements are validated against 100 human-annotated outputs and two established faithfulness detectors. Results show that semantic similarity aligns with human judgments, whereas entity-based metrics exhibit limited agreement. Differences between models are concentrated in question answering, while entity extraction quality limits what entity-level metrics can reveal.

---


### 110. [From Data Alignment to Parameter Generation: Few-Shot Cross-City Traffic Prediction with Conditional Diffusion](https://arxiv.org/abs/2611.25592)

**<font color=#1a73e8>作者：</font>** Shengchun Wang, Yuhang Lin, Tong Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate mobile traffic forecasting is crucial for network service management, supporting proactive capacity provisioning, congestion mitigation, and energy-efficient operation. However, many cities and regions are data-scarce (e.g., newly deployed or poorly instrumented areas), thus making traffic prediction a few-shot learning problem and limiting the practicality of standard data-driven models. Existing cross-city solutions primarily rely on data-space alignment to match traffic distributions between data-rich and data-scarce cities, but such alignment is often brittle under real-world distribution shifts, measurement noise, and city-specific bias. To address these limitations, we propose a Conditional Diffusion-based Parameter Generation (CDPG) framework. Instead of aligning raw data, CDPG learns the conditional distribution of high-performing predictor parameters for source cities and directly generates node-specific model parameters for the target city. To support reliable adaptation for network traffic prediction, CDPG conditions parameter generation on multi-modal spatio-temporal context. Specifically, CDPG captures spatial environment cues by combining satellite imagery with large language model (LLM)-derived semantic descriptions, and summarizes complex temporal behaviors via unsupervised pattern clustering. These contextual components guide CDPG in producing parameters tailored to each base station's operational context, thereby improving robustness under cross-city and cross-region shifts. Extensive experiments on three large-scale datasets show that CDPG consistently outperforms state-of-the-art cross-city few-shot baselines by up to 9.72% on standard forecasting metrics and remains robust for few-shot multi-step prediction. The code is available at this https URL.

---


### 111. [Characterizing Age-Conditioned Affective Reasoning in Vision-Language Models](https://arxiv.org/abs/2611.25593)

**<font color=#1a73e8>作者：</font>** Shahriyar Zaman Ridoy, Azmine Toushik Wasi, Lin Gu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An age prompt can change how a vision-language model (VLM) rates the emotion evoked by an image. Does the change predict how people of different ages rate that same image? We evaluate 17 VLMs on 900 OASIS images using young-, middle-, and older-adult prompts and estimate image-specific age differences from ratings by 822 participants. Without an age cue, models closely track average human valence (median Pearson $r=0.891$). Under an older-adult prompt, 16 of 17 models assign lower valence on average than under a young-adult prompt. Yet after adjusting for image pleasantness, correlations between model and human age effects range from $-0.030$ to $0.093$, against an estimated ceiling of $0.595$. The discrepancy is clearest on 54 sensitive images rated as pleasant. Across models, the older prompt reduces valence by $0.845$ points on average, while older participants rate these images $0.443$ points higher than younger participants. Providing human ratings from other images improves agreement on the direction of age differences, although image-specific fidelity remains modest on 600 held-out images ($r_{\mathrm{part}}=0.105$). These results show why evaluations of demographic personalization in foundation models need human comparisons at the level of individual stimuli. Project page available at this https URL

---


### 112. [Decision-Focused Reinforcement Learning for LLM Post-Training](https://arxiv.org/abs/2611.25597)

**<font color=#1a73e8>作者：</font>** Haotian Zhai, Leqi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promise as predictors across various tasks, benefiting from their ability to use information from unstructured context. However, when predictions serve as parameters of downstream optimization problems, higher prediction accuracy does not necessarily translate into lower decision costs. We propose decision-focused reinforcement learning (DFRL), a framework for post-training LLMs to predict optimization parameters using negative downstream decision regret as reward. DFRL trains LLM predictors to minimize the costs of the decisions induced by their predictions, without requiring downstream convexity or differentiability, and integrates readily into existing RL post-training frameworks. To address expensive reward evaluation, we develop two approaches. Heuristic warm-starting uses inexpensive approximate rewards during an initial phase before switching to refinement with exact rewards. Reward correction combines inexpensive estimates with randomized exact evaluations, preserving the expected policy gradient while reducing the expected number of exact solves per update. Experiments on three synthetic optimization problems demonstrate improvements over prediction-loss baselines, while a larger knapsack experiment shows faster early improvement under short training budgets. On inventory planning with H&M transactions and product descriptions, our best configuration, in which the LLM reasons before predicting, reduces regret by 31.4% relative to the SFT baseline and 12.4% relative to the strongest evaluated conventional forecasting baseline.

---


### 113. [Tether: Verified Stateful Policy Engine for System-Level Monitoring of Agents](https://arxiv.org/abs/2611.25599)

**<font color=#1a73e8>作者：</font>** Meghana Aparna Sistla, Alaia Solko-Breslin, Somesh Jha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents are increasingly deployed for long-running tasks that execute arbitrary shell commands or programs. However, these actions can result in unauthorized network requests or persistent, malicious changes to the user's file system, processes, or privileges. Existing defense mechanisms rely on either LLM-based monitors, which lack provable safety guarantees, or stateless policy enforcement layers, which miss multi-step data flows and execution side-effects unmodeled by the policy language (e.g., network calls initiated inside a Python script). We introduce Tether, a framework for runtime enforcement of stateful security policies over the observed side-effects of an agent's actions. Tether executes each proposed action in an ephemeral, isolated sandbox, inferring abstract action semantics from observed system calls. Tether then enforces stateful policies over these inferred semantics, permitting actions to proceed only if they comply with the policy. Policies and action semantics are defined in an embedded DSL in Lean 4 capable of expressing diverse constraints, including information flow control (IFC), access control, and network security policies. Because actions can propagate labels from sources to destinations, a single rule can enforce fine-grained IFC policies across multi-step execution flows of arbitrary length. Expressing policies in Lean enables formal verification that they satisfy global security invariants (e.g., preventing network access after reading a sensitive file). We evaluate Tether on realistic coding-agent benchmarks across both benign and adversarial trajectories. With a single policy shared across all tasks, Tether blocks 100% of in-scope attacks while maintaining a benign false-positive rate under 5%.

---


### 114. [Can an LLM Fix a Language Model Without Training It?](https://arxiv.org/abs/2611.25613)

**<font color=#1a73e8>作者：</font>** Bharath Kumar Bolla, Raghavender Surya Upadhayula, Vishnu Surya Reddy Nandi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although an external language model can select and test repairs to another model's weights, behavior can also be recovered through fixed numerical edits. We assessed the value of interactive selection in a controlled study of Transformer repair. After inspecting predictions, activation summaries, and weight statistics, the editor selects projection recipes to apply to the target without gradient updates. We analyzed 20 recorded sessions involving five masked and causal language models, comparing the selected edits with fixed projections, scripted and matched-budget black-box search, and low-rank adaptation. Under the core two-layer fault, live selection matches black-box search on SmolLM2 and Qwen2.5. For Pythia, live selection achieves 65.62% completion accuracy, compared with 0% for black-box search and 66.15% for a fixed projection. Under a separate compound fault affecting attention and feed-forward weights, both scripted and LLM-guided selection increase the descriptive five-checkpoint mean from 24.89% to 71.25% using the same operator family. On unmodified checkpoints, scripted projection yields small gains or losses on a separate set of framed questions. The experiments identify cases in which feedback changes an edit decision, operator coverage accounts for recovery, or supervised adaptation performs better. Combined with measurements of parameter restoration and preservation, these comparisons establish the scope of controller-guided repair for the tested faults and completion tasks.

---


### 115. [CaT-Movie: Balancing Global Planning and Local Rendering for Long Multi-Shot Video Generation](https://arxiv.org/abs/2611.25620)

**<font color=#1a73e8>作者：</font>** Jinpeng Lu, Haoyuan Shi, Yuanshen Guan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current multi-shot video generators render only limited durations per pass, requiring long movies to be stitched from local segments across which narrative progression and visual identity drift. To synthesize long-horizon movies with Coherence across Time, we present CaT-Movie, a multi-shot generation system consisting of a global story planner and a local window renderer. The planner expands user requests via a large language model to preserve, infer, and complete story details, while deterministic code maintains the resulting storyboard across shots to compile self-contained shot prompts and index reference frames from generated history. To execute this guidance, the renderer applies reference-routed sparse self-attention and shot-wise cross-attention to route identities from the indexed frames while isolating per-shot textual conditions. Given the scarcity of high-quality open-source multi-shot data, we construct a dataset of over 350K film shots annotated with semantic state transitions, entity grounding, and multi-granularity requests. We further build CaT-MBench, a benchmark on held-out films with the same annotations. It gives every baseline its native format and counts cross-shot consistency only when a cut opens a new camera setup, preventing repeated framing from passing as consistency. On CaT-MBench, CaT-Movie attains the highest average score and the most consistent characters among all methods. The project page is available at this https URL.

---


### 116. [LG-FiLM: Local-Global Mixture-of-Experts Modulation for RAW-to-RGB Reconstruction](https://arxiv.org/abs/2611.25639)

**<font color=#1a73e8>作者：</font>** Fei Li, Xilei Cao, Shichang Zhai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An image signal processor does more than reconstruct an image. It also has to decide how strongly to denoise, how to balance color, and which tone curve maps the scene onto the display, and these settings depend on the scene itself, the curve that suits a backlit sky is not the one that suits an indoor portrait. Most neural ISPs learn a single fixed transformation and apply it to every scene. We instead make the adaptation an explicit part of the network. Our model, LG FiLM, keeps one shared encoder decoder and places a small mixture of affine experts at its bottleneck; the experts scales, shifts, and mixing weights are predicted from local neighborhood evidence together with a global scene descriptor. Reconstruction stays in a single shared pathway and only the processing mode is switched. We evaluate LG FiLM on three datasets, Fujifilm UltraISP, Zurich RAW to RGB, and a COCO derived benchmark built with an inverse ISP. The model reaches the best reconstruction fidelity of the compared entries on the primary benchmark and transfers to the other two.

---


### 117. [TRAC: Efficient Diffusion Language Models for Machine Translation via Length-Aware Decoding](https://arxiv.org/abs/2611.25643)

**<font color=#1a73e8>作者：</font>** Tianyuan Li, Xihan Yang, Chenglong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine translation with large language models requires both high translation quality and low generation latency. Accelerating translation while preserving quality is therefore essential for practical deployment. Diffusion large language models (dLLMs) can generate tokens at arbitrary target positions through iterative denoising, offering a new paradigm for parallel translation beyond sequential autoregressive decoding. However, existing methods still incur redundant computation: fixed target generation lengths waste computation on unused positions, while confidence-only commitment delays medium-confidence tokens whose predictions have largely stabilized. To address these issues, we propose TRAC, a training-free adaptive decoding method for diffusion machine translation. TRAC adapts the target generation length using source length and translation direction, with a conservative fallback to the maximum length for empty or unusually short outputs. It preserves high-confidence commitment while identifying temporally stable medium-confidence tokens for early commitment using cross-step top-1 persistence and approximate Jensen-Shannon divergence over Top-$K$ distributions. On bidirectional Chinese-English translation across FLORES-200, WMT23, and NTREX-128, TRAC reduces model forward calls by 24.9% to 36.8% and achieves sentence-level generation speedups of 1.91 to 2.19 times over Fast-dLLM, with only a 0.02-point decrease in macro-average COMET. These results demonstrate that adaptive generation lengths and stability-aware token commitment improve the efficiency of diffusion machine translation.

---


### 118. [ColorRef: Calibrating Verbal Feedback for Color Revision](https://arxiv.org/abs/2611.25653)

**<font color=#1a73e8>作者：</font>** Pablo Loyola, Andres Hoyos-Idrobo, Edison Marrese-Taylor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> People rarely specify an exact color when asking someone to revise a design: they might say \textit{a little darker} or \textit{more blue} after seeing a proposal. A language-model assistant must then infer not only which way to change the color, but how far. We study this distinction with \textsc{ColorRef}, a color reference game in which a model guesses a color from a description and a teacher, knowing a recorded target hidden from the guesser, supplies verbal corrections. On 1{,}000 crowd-sourced description--target pairs, three rounds of deterministic oracle feedback reduce mean target distance from 42.33 to 22.15 $\Delta E_{76}$. However, those corrections provide additional information, and improvement alone does not establish well-calibrated feedback following. A controlled Qwen3-14B diagnostic reveals a more specific failure: following a requested direction and ordering graded phrases do not guarantee a suitable step size; strong modifiers can induce excessive changes. We therefore measure each receiver's typical response to \textit{a little}, \textit{somewhat}, and \textit{much} on separate colors and select wording matched to its observed steps. On 128 held-out starting colors, calibration reduces one-step mean error from 12.36 to 6.86 for Qwen3-14B and from 11.06 to 5.89 for Gemma 4 12B against a fixed graded-wording rule. The benefit is concentrated on large corrections, with many unchanged cases and no consistent increase in threshold success. Our findings show that following the direction of feedback is not the same as making an appropriately sized revision.

---


### 119. [SiliconGym: A Versatile Reinforcement Learning Environment for Agentic EDA](https://arxiv.org/abs/2611.25658)

**<font color=#1a73e8>作者：</font>** Hejia Zhang, Sheng Lu, Yitong Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) with electronic design automation (EDA) feedback is advancing large language models for hardware design and verification. Extending these gains to hardware-engineering agents requires environments that span tasks, preserve state across tool calls, and support large hierarchies alongside parallel rollouts. We present SiliconGym, the first versatile, cross-task and cross-toolchain RL environment for hardware design and verification. By decoupling versioned workspaces, budgeted execution, and acceptance-gated scoring, SiliconGym scales from module-level RTL, testbench, and PPA tasks to multi-round repository repair and full-hierarchy SoC flows. Streaming dispatch overlaps tool checks with generation, finishing a 256-answer RL batch 21.9% faster than native ChipSeek. Using interchangeable open-source and commercial backends, we show that open-source-trained functional correctness transfers cleanly to commercial simulation, while paired netlist evaluation reveals when open-source PPA gains survive commercial synthesis.

---


### 120. [Ask in the Crowd: Differentially Private LLM Inference via Dummy-Augmented Shuffling](https://arxiv.org/abs/2611.25669)

**<font color=#1a73e8>作者：</font>** Zhihao Liu, Zixiong Guo, Shuo Shao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as LLM-as-a-Service (LLMaaS), where user queries are sent to remote LLMs for inference, raising severe privacy concerns about the exposure of sensitive user inputs. Differentially private inference mitigates these risks by injecting noise into input embeddings. However, existing methods struggle to balance privacy and utility, as stronger privacy protection often leads to substantial accuracy degradation in LLM inference.
In this work, we propose DP-SPD, a differentially private LLM inference framework that protects user queries by hiding the real query among client-generated dummy queries. All queries are randomly shuffled before being sent to the server, preventing direct identification of the user's true intent. To improve inference efficiency, we exploit the shared-prefix structure among queries and reuse transformer key--value (KV) caches during decoding. We analyze the privacy guarantee of DP-SPD and evaluate its utility on classification and generation tasks, as well as its privacy protection under QIA, EIA, and GPT-based attacks. Experimental results show that our method achieves strong inference-time privacy protection and near-plaintext utility while improving inference efficiency through shared-prefix KV-cache reuse.

---


### 121. [Efficient Latent Reasoning for Vision-Language Model via Dynamics-Aware Quantization and Distillation](https://arxiv.org/abs/2611.25670)

**<font color=#1a73e8>作者：</font>** Yanjing Li, Sheng Xu, Baochang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient chain-of-thought (CoT) reasoning in vision-language models (VLMs) requires reducing both intermediate reasoning steps and their execution cost. Latent CoT methods compress textual rationales into continuous thoughts, yet their full-precision (FP) models retain substantial storage and computation costs. Lowering numerical precision could reduce these remaining costs, yet direct quantization severely degrades reasoning accuracy, particularly with 4-bit weights and activations. Operator and perturbation analyses reveal key sensitivity and direction-dependent predictive effects of continuous-thought errors, motivating preservation of information retrieval and subsequent reasoning beyond reconstruction accuracy. We therefore introduce QL-VLM, a dynamics-aware Quantization framework for efficient Latent reasoning in Vision-Language Models (VLMs). First, Dynamics-Guided Quantization (DGQ) uses nonuniform codebooks that preserve rotary-key structure, mitigating quantization-induced distortion in vision-language information retrieval. Second, Dynamics-Preserving Distillation (DPD) aligns continuous thoughts, latent-query readouts, and predictions with a full-precision teacher, maintaining predictive consistency through subsequent low-precision reasoning. On ScienceQA-IMG with Qwen2-VL-2B-Instruct, 4-bit QL-VLM achieves 90.43% accuracy and improves baseline by 40.33%, with 16.64x fewer bit-operations and 6.40x lower measured latency than explicit CoT.

---


### 122. [SEAF: Selective Semantic Enrichment and Visual Evidence Fusion for Multimodal Sarcasm Detection](https://arxiv.org/abs/2611.25672)

**<font color=#1a73e8>作者：</font>** Faxian Wan, Xiaocui Yang, Yifan Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal sarcasm detection requires textual, visual, and contextual evidence, particularly when multiple images provide complementary cues. Multimodal large language models (MLLMs) can generate auxiliary information from a post's text and images, but their outputs may mix useful background knowledge with redundant visual descriptions. We propose SEAF, a dual-branch framework for selective semantic enrichment and visual evidence fusion. SEAF assigns generated fields to distinct roles: entity background enriches semantic input, while image descriptions supply alignment statistics. The semantic branch combines the original post text, background from a frozen MLLM, and optical character recognition (OCR) text. The aligned visual branch combines global and local visual features with statistics of cross-modal and inter-image similarity. Text-Anchored Smoothed Aggregation (TASA) weights images by their similarity to the original post text while preserving contributions from images with low literal similarity. Summing the branch classification scores integrates contextual semantics with visual evidence. Experiments on the multi-image MMSD3.0 benchmark show that SEAF outperforms all compared methods.

---


### 123. [CompAct-Bench: A Benchmark for Working-Context Compaction in Long-Horizon Agent Tasks](https://arxiv.org/abs/2611.25673)

**<font color=#1a73e8>作者：</font>** Jiayi Chen, Lizhe Chen, Yujia Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As language-model agents are applied to increasingly extended tasks, their working context continuously accumulates interaction history, tool observations, intermediate decisions, and task progress. Context compaction offers a practical way to reduce this growing history while allowing execution to continue, yet the compaction ability of modern LLMs remains insufficiently understood. We introduce CompAct-Bench, a benchmark for evaluating working-context compaction through its downstream effect on agent task completion. Starting from successful agent trajectories, we insert compaction boundaries at different stages of execution, compress the preceding working context with the model under evaluation, and let the same executor continue the original task. To enable fair comparison across compactors, we evaluate them under controlled retention ratios using a lightweight iterative ratio-adjustment procedure. CompAct-Bench covers information-seeking, software-engineering, and workspace-oriented tasks through BrowseComp, SWE-bench, and an internal CompanyBench evaluation. Our experiments show that working-context compaction remains highly lossy even for frontier models: Claude- and GPT-family models perform strongest overall, yet substantial degradation in downstream task accuracy persists under aggressive compaction. Further analysis reveals that failures are often caused not only by omitted information, but also by distorted task state, such as turning unresolved issues into apparent conclusions or forgetting previously established results, which can lead to incorrect decisions or redundant execution. These findings highlight working-context compaction as a distinct and still challenging ability for LLMs operating in extended agent tasks.

---


### 124. [Beyond Entity Recognition: Vision-Centric Knowledge Visual Question Answering](https://arxiv.org/abs/2611.25680)

**<font color=#1a73e8>作者：</font>** Jiatong Ma, Yuchen Liu, Longteng Guo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose VC-VQA, a large-scale benchmark for vision-centric knowledge reasoning, aiming to systematically evaluate the capabilities of Multimodal Large Language Models (MLLMs) in fine-grained visual knowledge acquisition and complex multi-stage reasoning. Unlike existing benchmarks that primarily treat visual information as entity recognition and rely on text-based external knowledge, VC-VQA explicitly models the role of visual information by considering both its source (internal vs. external images) and stage of involvement (pre-retrieval vs. post-retrieval). Specifically, VC-VQA requires models to retrieve external visual evidence, identify visual clues before retrieval, and localize, verify, or match retrieved knowledge against the internal image. We further construct a controlled multimodal knowledge base with traceable textual and visual evidence for each sample. We evaluate 21 representative MLLMs under four settings: no external knowledge, with provided evidence, knowledge base retrieval, and open-web search. Experimental results lead to three key findings: current models still struggle with vision-centric knowledge reasoning; fine-grained visual knowledge acquisition remains the primary bottleneck; and agentic retrieval highlights the value of multi-step planning and cross-modal knowledge integration. Overall, VC-VQA provides a more challenging benchmark for evaluating vision-centric knowledge reasoning in MLLMs. Our code and dataset are available at this https URL.

---


### 125. [FoodReact-AR: Learning Audience Reactions that Zero-Shot LLMs Miss in Arabic Food-Insecurity Discourse](https://arxiv.org/abs/2611.25682)

**<font color=#1a73e8>作者：</font>** Wajdi Zaghouani, Mabrouka Bessghaier, Salma Azouzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Facebook reactions record how an audience received a post, a signal absent from the post's text. We treat the six differentiated reactions on 74,241 Arabic food-insecurity posts from public Facebook pages (2020-2024) as compositions, apply a centered log-ratio transformation, and cluster them into four audience profiles: Solidarity (Love-dominant), Dismissal (Haha-dominant), Grief (Sad-dominant), and a flat Ambivalent profile. Dismissal peaks in 2022 (22.3%), the year of the wheat price shock, and grief in 2024 (14.0%), during the Gaza food emergency; a page-clustered GEE confirms both shifts (odds ratios 2.18 and 1.34), and they survive minimum-reaction filtering, alternative zero replacements and clustering methods, and bootstrap resampling. We then test whether the profiles can be predicted without reactions. A zero-shot Arabic LLM recovers Grief for 83.8% of posts but Dismissal for only 3.4%, and in a matched ablation, it shows the reaction percentages do not help. A simple classifier trained on the reaction-derived labels and tested on unseen pages recovers dismissal for 60.0% (macro-F1 0.56 against 0.43), mainly from mentions of officials and institutions. Derisive audience responses are thus learnable from text, yet a zero-shot LLM misses them. We release the corpus, LLM, and human annotation layers, and an evaluation protocol as FoodReact-AR.

---


### 126. [DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies](https://arxiv.org/abs/2611.25695)

**<font color=#1a73e8>作者：</font>** Jun Xia, Shangwen Wang, Jun Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) policies rely on visual feedback throughout manipulation, making them vulnerable to persistent texture attacks. However, optimized patterns can stand out from their surroundings, making an attack easier to notice and its carrier more likely to be inspected or removed. To address this limitation, our key insight is to search the structured image distribution of a diffusion model for natural-looking textures while using closed-loop feedback to identify task-disruptive candidates. Based on this idea, we propose DMT-Attack, a gradient-free gray-box attack that generates textures for ordinary scene objects such as tablecloths. A frozen text-conditioned diffusion model defines the search space, and an eight-expert latent proposal network is initialized from evaluated teacher latents and refined using rollout feedback. We evaluate DMT-Attack against pi_0.5 and OpenVLA-OFT across four LIBERO suites. DMT-Attack achieves a macro clean-conditioned attack success rate (cASR) of 57.9%, compared with 44.7% for UPA-RFAS and 19.7% for random natural textures. It also attains higher scene similarity and a lower clean-calibrated detector flag rate (45% versus 97.5-100% for optimized patch baselines). These results demonstrate that natural-looking textures can disrupt VLA visual feedback and closed-loop decision-making, motivating defenses that jointly assess visual appearance and task behavior.

---


### 127. [From Geographic Memory to Spatial Generalization in Large Language Models](https://arxiv.org/abs/2611.25703)

**<font color=#1a73e8>作者：</font>** Chen Chu, Zhaonan Wang, Cyrus Shahabi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can associate places with geographic descriptions, but recovering an observed association does not establish an ability to generalize across geographic space. We distinguish geospatial memory, the recovery of location--description associations observed during training, from spatial generalization, the prediction of descriptions for locations in unobserved regions. We investigate whether continuous location representations improve this generalization and encourage geographic knowledge to become spatially organized within an LLM. We frame this organization as a latent spatial field: a learned mapping from locations to descriptions connected through spatial dependencies. Building on a continuous spatial encoder, we project location representations into the model's embedding space and supply them as spatial tokens. We evaluate the resulting models on two newly curated geo-text benchmarks for Los Angeles and London using two complementary assessments. Geospatial captioning tests both memory and spatial generalization by generating descriptions at observed locations and at locations beyond the spatial coverage of the training observations. A separate geospatial grounding model tests whether generated location--description pairs provide useful additional supervision for mapping text to geographic space. Across multiple LLM families, continuous location representations improve captioning at unobserved locations relative to textual coordinates, while their generated descriptions yield modest but consistent improvements in downstream grounding. Layer-wise probing and representation clustering provide additional evidence consistent with spatially organized geographic representations. Together, these findings show the value of evaluating spatial generalization separately from memory and of incorporating continuous spatial representations into language models.

---


### 128. [STARK: Moving towards Personalized Agents That Truly Learn and Remember](https://arxiv.org/abs/2611.25705)

**<font color=#1a73e8>作者：</font>** Aryan Jain, Abhishek Jha, Anish Nediyanchath 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for personalized agentic systems that interact with users over long time periods, yet current architectures only capture what happened while leaving the reasoning of why it happened to be derived later by underlying LLMs.%, and silo knowledge within individual users. These events can, however, convey not only what a user experienced but also how that experience shaped their behavioral patterns. We introduce STARK, a dual-graph memory architecture which treats these events not just as nodes but also as edges between behavioral insights. STARK maintains an Episodic Graph which records interactions as temporally, causally, and semantically linked episodes; and an Insight Graph which represents LLM-extracted behavioral signals scored by how many events support them, connected by the very events that led to them. At inference, behavioral knowledge is retrieved directly from insight nodes grounded by event-as-edges, eliminating repeated episodic traversal. The event-as-edge structure also naturally enables projecting the knowledge graph into a relational embedding space where cross-user transfer becomes possible under shared contextual circumstances, allowing the system to infer missing insights for cold-start users. Evaluations show that STARK improves by 1.48 judge score on LongMemEval information extraction and 0.93 on LoCoMo open domain questions over state of the art. On the public LongLaMP abstract-generation benchmark, cross-user transfer improves open-ended judge scores by 0.7 points and ROUGE-L by 3 at 5% graph sparsity.

---


### 129. [Slide2PPT: Native PowerPoint Reconstruction with Localization-Guided Refinement](https://arxiv.org/abs/2611.25708)

**<font color=#1a73e8>作者：</font>** Baoliang Chen, Xinlong Bu, Lingyu Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-to-slide reconstruction must recover both visual appearance and native object structure for subsequent editing. Yet visually faithful charts and tables may lack editable series and cells, and direct code generation couples content prediction to rendering implementation. We present Slide2PPT, a model-agnostic, training-free framework that equips both open- and closed-source vision-language models with native PowerPoint reconstruction capabilities. Through a unified typed interface, the model predicts object records while a fixed renderer materializes their native properties, enabling integration with different backbones without task-specific training or architectural changes. Localization-guided refinement then connects visual discrepancies to object records for correction. Regional updates preserve unselected records, while whole-slide updates address cross-region relationships. Record refinement and targeted object editing support structural and attribute-level changes, with rendered feedback governing iterative acceptance. To evaluate this framework across diverse reconstruction demands, we introduce Slide2PPT-Bench, covering controlled elements, real slides, and scientific figures. Evaluation separately measures file production, rendered agreement, and native-object availability. Experiments across open- and closed-source backbones demonstrate substantially more reliable PPTX generation than direct code generation, improved layout and text recovery on scientific figures, and native chart and table interfaces beyond geometric primitives.

---


### 130. [Interpreting DeepStack-Style Vision-Language Models: Do Input or Deeper-Layer Visual Tokens Drive Answers?](https://arxiv.org/abs/2611.25713)

**<font color=#1a73e8>作者：</font>** Yucheng Du, Yi Nian, Ruixue Lian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> DeepStack-style vision-language models feed visual tokens to the language model at its input, and again at deeper layers. We call these the main entry and the later entries. What do the later entries add when the model already has the image? We give the entries versions that differ in one object's color and see which one the answer follows. On photographs, the original DeepStack follows the later entries, while Qwen3-VL-8B/32B follow the main entry. Does weakening the main entry give the later features more influence? On synthetic images, we keep this conflict and reduce color saturation at the main entry only. The unchanged later features gain a stronger effect on the relative scores of the two colors, in all four models, including Granite Vision. This holds even under mild desaturation, when accuracy without the conflict stays at 100%. To test whether later features can also correct errors, we degrade both entries and restore only the later ones. The same blur costs both Qwen models 50 percentage points of accuracy on stripe orientation. The 32B model recovers 48 points and the 8B model only 8. Accuracy with one clean entry predicted which entry each model can lose, and five of six tested predictions held on new GQA attribute questions. With the other entry zeroed, Qwen3-VL-8B loses only 0.3 points on its main entry alone, and DeepStack at most 3.45 points on either entry alone. In split inference on these questions, DeepStack can then send only its main-entry features at higher precision. This takes 49% fewer bytes than all entries at a shared precision, at similar accuracy.

---


### 131. [VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin](https://arxiv.org/abs/2611.25717)

**<font color=#1a73e8>作者：</font>** Samir Khaki, Wei-Chen Wang, Song Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, GPUs have incorporated increasingly specialized support for low-precision computation, from Hopper's FP8 to Blackwell's FP4 Tensor Cores. Precision formats have evolved alongside this hardware, from MXFP4 and NVFP4 on Blackwell to E2M1 FP4 with direct UE5M3 block scaling on Vera Rubin, which we term as $\boldsymbol{VRFP4}$. These advances help serve larger language models at lower cost, but four-bit activation quantization can substantially degrade model quality. We introduce VR-SparseQuant, which uses Vera Rubin's elementwise 2:4 sparsity to recover accuracy while retaining native FP4 execution. By allowing two sparse streams to overlap, we use the same FP4 value budget as dense quantization to refine activations with larger errors. Offline scale-ratio calibration avoids runtime search, while a shared-weight GEMM accumulates both streams efficiently. On Nemotron-3-Nano-30B-A3B, VR-SparseQuant reduces WikiText-2 perplexity from $\boldsymbol{6.85}$ to $\boldsymbol{5.57}$ versus dense RTN W4A4. Including activation preparation, our native Rubin kernels for VRFP4 achieve up to $\boldsymbol{3.1\times}$ GEMM and $\boldsymbol{2.7\times}$ MoE speedup over BF16. To the best of our knowledge, this is the first study of adaptive activation quantization using Vera Rubin's elementwise 2:4 structured sparse FP4 instructions.

---


### 132. [Hardening JavaScript Programs against LLM-Based Vulnerability Detection](https://arxiv.org/abs/2611.25718)

**<font color=#1a73e8>作者：</font>** Zhenhao Tian, Jintong Yu, Jingwei Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> JavaScript programs are often distributed as source code, so attackers can analyze them for vulnerabilities. LLM-based vulnerability detection agents now make this analysis much easier. To mitigate this emerging threat, we present AntiAgent, a defense that lets developers harden their programs against such detection agents. AntiAgent transforms a program before release to impede an agent's analysis. To find effective transformations, AntiAgent evolves a corpus of programs with known vulnerabilities and traces how a detection agent analyzes each evolved version. It keeps the versions on which the agent misses or misreports the vulnerability and extracts their transformations into reusable rules. To protect a new program, AntiAgent carefully divides the task between an LLM and the rules, so that the transformations adapt to the program while preserving its semantics.
We evaluate AntiAgent on real-world JavaScript applications against four detection agents, including Claude Code and Codex. AntiAgent reduces the number of vulnerabilities that each agent detects by 52.0-60.7%, outperforming the conventional obfuscator JS-Obfuscator and the LLM-based transformation method FPA on every agent. The transformed programs pass all project tests, indicating that AntiAgent preserves the original program semantics. The transformation rules also remain effective on vulnerability types absent from the corpus and on programs written in another language like Python.

---


### 133. [DACA: Dual-Anchor Collaborative Agent for Zero-Shot 3D Visual Grounding](https://arxiv.org/abs/2611.25722)

**<font color=#1a73e8>作者：</font>** Jiaming Liu, Linghe Kong, Guixu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D visual grounding (3D-VG) is a task that bridges the natural language and 3D space, serving as a foundational capability for embodied intelligence and human-computer interaction. Although recent 3D-VG agents overcome the reliance on pre-processed 3D point clouds, they essentially employ a unidirectional, pipeline-style tool-calling architecture. This architecture separates semantic understanding from geometric reconstruction, leading to error accumulation and an inability to autonomously recover from failures. To address this flaw, this paper proposes the Dual-Anchor Collaborative Agent (DACA), which reinterprets 3D-VG as a semantic-geometric dual-anchor collaborative reasoning paradigm. DACA comprises two complementary specialized tools: the semantic anchor tool holds the visual semantic features of the target and achieves efficient target tracking via optical flow and VLM local verification; the geometric anchor tool holds the 3D spatial geometric features of the target and performs global spatial reasoning via voxelization and multi-keypoint projection. The two components exchange information bidirectionally via a standardized tool call protocol, autonomously deciding on the next perception-action step to form a closed-loop optimization. Experiments on the ScanRefer and Nr3D benchmarks demonstrate that zero-shot DACA achieves an overall Acc@0.25 of 73.6\% on ScanRefer and 70.4\% overall accuracy on Nr3D, far surpassing the latest zero-shot 3D-VG methods. The code and models are available at this https URL

---


### 134. [From Reliance to Overreliance: Taxonomizing and Detecting Relational Risks in AI Companionship](https://arxiv.org/abs/2611.25734)

**<font color=#1a73e8>作者：</font>** Viet Cuong Nguyen, Fiona Li, Chang Wan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Companion AIs are increasingly used for emotional support, yet distinguishing meaningful engagement from harmful reliance remains difficult. We introduce the Taxonomy of Relational Risks (TRR), which operationalizes users' emotional overreliance (EO) as observable conversational behaviors and separately identifies evidence of relational harm (RH), enabling empirical examination of when reliance behaviors co-occur with adverse consequences. Using naturalistic this http URL and Replika conversations from 110 adults, we found EO-related behaviors in 63.2% of non-roleplay conversations, while observable relational harms appeared in 10.5%. Although EO did not necessarily lead to harm, recurring patterns often co-occurred with harmful outcomes, suggesting value as risk indicators. Open-source LLMs satisfactorily detected 12 of 14 EO behaviors in at least one configuration. Qualitative analysis revealed expectations of care, repeated support seeking, dependency, distress, and reduced confidence in personal judgment. We argue for graduated safety interventions tailored to patterns and trajectories of EO-related behavior.

---


### 135. [PosteriorBench: Evaluating Behavior Posterior Sampling in Language Models](https://arxiv.org/abs/2611.25735)

**<font color=#1a73e8>作者：</font>** Zhiyang Xun, Daniel D. Johnson, Sarah Schwettmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rare language model behaviors can be difficult to study because obtaining them through ordinary sampling can require a very large number of samples. This motivates the behavior posterior sampling problem: given a language model and a behavior of interest, is there an algorithm that efficiently samples from the model's distribution over transcripts that exhibit this behavior? We introduce PosteriorBench, a benchmark for comparing algorithms by their compute cost and by how close their samples are to the true posterior in forward and reverse KL divergence. PosteriorBench contains 21 tasks on Qwen3.5-0.8B with behavior probabilities from $10^{-5}$ to $10^{-1}$, each with exact posterior samples from a corpus of one billion labeled responses. We find that no method we evaluate is both efficient and faithful: simple methods like prompting are cheap but plateau at a high KL divergence from the posterior, fine-tuning on posterior samples is often cost-prohibitive, and several training methods from prior work do not perform better. Building a posterior sampler that can cheaply approximate the true posterior remains an open problem, and we hope PosteriorBench can measure progress towards this objective. Code and data are available at this https URL.

---


### 136. [Goal-Guided Reinforcement Learning via Fine-Tuning Vision-Language Models](https://arxiv.org/abs/2611.25742)

**<font color=#1a73e8>作者：</font>** Yajie Qi, Wei Wei, Lin Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploration remains a major challenge for reinforcement learning (RL) agents in Craftax-style environments due to sparse rewards and long horizons. Large language models (LLMs) can guide exploration by generating high-level goals, but methods using models without explicit task adaptation often rely on carefully designed prompts and may produce inconsistent or contextually inappropriate goals. We introduce CCGP-2M, a multimodal goal-preference dataset constructed from interaction trajectories in Craftax-Classic, and propose a vision-language model (VLM)-guided RL framework that learns environment-specific goal guidance from this dataset. The framework consists of two stages: offline VLM fine-tuning and online goal-guided RL. In the offline stage, we align the VLM with goal preferences using Kullback-Leibler Token-level Direct Preference Optimization (KLTDPO), which combines token-level KL regularization with distributionally robust reweighting. Experiments on Craftax-Classic show that our method collects diamonds earlier than state-of-the-art baselines, achieves the highest score and reward, and attains the highest success rates on most achievements.

---


### 137. [Verification Behavior Across Five Qwen2.5-Instruct Checkpoints](https://arxiv.org/abs/2611.25745)

**<font color=#1a73e8>作者：</font>** YaJie Yin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We evaluate five Qwen2.5-Instruct checkpoints (0.5B to 32B) under four prompting conditions using three fixed tasks per information condition and five generations per task. Two AI raters scored 600 trajectories. Under the coordinated instruction, both raters recorded strict declarations of insufficiency in 11/15 cases at 7B, 0/15 at 14B, and 5/15 at 32B. The runner sent a standard follow-up when a request detector fired. The three checkpoints received at least one follow-up in 15, 12, and 15 cases, respectively. On information-sufficient tasks at 3B through 32B, scored format markers appeared in 60/60 protocol trajectories and 0/60 baseline trajectories. After adjudication, 1/60 in each condition met the diagnostic-execution criterion (H3). Across all checkpoints and prompts, 7/300 information-sufficient trajectories met H3 after adjudication, all on the same task. The prespecified upward transition did not occur in this run. The results separate visible structure, diagnostic execution, and persistence after a request for evidence.

---


### 138. [SAM 3 Sees More Than It Detects: Promptable Concept Maps Beyond Categories](https://arxiv.org/abs/2611.25747)

**<font color=#1a73e8>作者：</font>** Yu-Huan Wu, Yun Liu, Liangli Zhen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Promptable segmenters answer what a thing is. Dense prediction tasks also ask class-agnostic questions, such as what stands out or hides, how light is blocked, transmitted or reflected, and where structure lies. Robots, surveillance systems and image editors build on their answers. We study promptable concept maps (PCM), which extend SAM 3's promptable concept segmentation from noun instances to maps of concepts named by short noun phrases such as `"transparent object", with "none" as an answer. PCM-Bench groups the standard test sets of seven such tasks by the question they ask. On it, we find that SAM 3 sees more than it detects. Its semantic path responds to many of these concepts, yet a low image-level presence score can block every detection of its instance path. We present UNVEIL, which trains a copy of SAM 3's semantic path for these maps, with LoRA on copies of its last blocks. A separate presence decoder learns from verified negatives whether a concept occurs. With one text phrase per query, UNVEIL maps region concepts such as salient and camouflaged objects, shadows, transparent objects and mirrors. The same weights map thin structures such as edges and skeletons as well as object categories. Run next to SAM 3, it leaves SAM 3's own outputs unchanged. On each of the seven tasks, UNVEIL reaches the highest score among the compared promptable models, including SAM 3's official fine-tuning and pipelines built on multimodal LLMs. Code is available at this https URL.

---


### 139. [ADAPT: Adaptive Decision and Abstention with Pool-Size-Aware Thresholds for Service Routing](https://arxiv.org/abs/2611.25754)

**<font color=#1a73e8>作者：</font>** Manile Srun, Muntasir Adnan, Arslan Shaukat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrieval-based classifiers efficiently route queries to specialised services, but they typically select a candidate even when no suitable service exists. We introduce Adaptive Decision and Abstention with Pool-Size-Aware Thresholds for Service Routing (ADAPT), a lightweight routing architecture with an explicit fallback option that enables queries to abstain from specialist selection. ADAPT uses the separation between the highest relevance score and the candidate score distribution as routing confidence. Experiments across retrieval models and increasing numbers of services reveal a consistent empirical behaviour: the confidence distribution changes systematically with candidate-pool size K, making fixed abstention thresholds increasingly miscalibrated. ADAPT addresses this effect with a K-aware threshold that adapts as services are added without classifier retraining. Evaluation across two specialist datasets shows that this simple mechanism provides an effective accuracy-cost trade-off compared with generative LLM routing, supporting lightweight and dynamically extensible service-routing architectures.

---


### 140. [Closing Performance Gap for Diffusion Language Models under Low Inference Budgets](https://arxiv.org/abs/2611.25763)

**<font color=#1a73e8>作者：</font>** Hao Wu, Sipeng Chen, Jingwen Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models offer an architectural route to low-budget generation by updating multiple tokens in parallel, which can reduce the number of sequential decoding steps relative to token-by-token autoregressive decoding. However, realizing this advantage at low budgets is challenging, as generation quality often declines when the number of denoising and refinement steps is reduced. Editable diffusion models address this quality loss through post-draft refinement, but useful intermediate results may still be lost before final submission. We introduce CaRR (Commitment-aware Refinement and Recovery), a training-free framework which improves submission quality from a fixed editable checkpoint through updated-context refill and trajectory-based recovery within its existing forward schedule. Token Commitment Remasking (TCR) remasks selected native pure replacements and refills them on the next scheduled edit forward using the updated context. Submission Commitment Recovery (SCR) uses the resulting refinement trajectory to recover supported candidates when the final response does not satisfy task-specific output requirements. Both modules operate within the native mask/edit schedule without additional backbone forwards. Experiments on code generation and mathematical reasoning show consistent gains in average accuracy over native ME-DLM across four inference budgets, with the largest gains under tight budgets. At one-eighth of the full scheduled forward budget, CaRR improves the six-metric average accuracy by 7.44 pp, including gains of 11.37 and 10.05 on MBPP and MBPP+.

---


### 141. [Duopra: From Full-Duplex Conversation to Full-Duplex Agency](https://arxiv.org/abs/2611.25773)

**<font color=#1a73e8>作者：</font>** Chiyu Chen, Pengzhou Cheng, Yuezhao Ma 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex interaction models exhibit strong conversational agency, enabling natural, low-latency turn-taking, backchannels, and interruptions. However, completing tasks further requires task agency: timely tool invocation and argument revision following user corrections. Frontend-backend agents separate initiation from execution: the frontend decides whether and what to request, while the backend determines how. Execution can be offloaded, but unsent requests cannot be executed, and incomplete ones can misdirect the backend. On Full-Duplex-Bench v3 (FDB v3), most failures of Realtime-Venus-Audio + Harness in our streaming pipeline occur before a domain tool executes. We introduce Duopra, a full-duplex interaction model that learns task execution alongside conversational control. Duopra treats the backend as a tool, accepting a self-contained natural-language request. Direct calls and backend delegation share an action interface and requirements for faithful initiation and correct execution. Its three-stage training combines protocol SFT, full-duplex RL rewarding timely and complete execution, and projector-only repair of talker conditioning after thinker updates. With the same backend, Pass@1 rises from 4.7% to 44.7%; Duopra achieves 47.7% calling tools directly (26.0% after SFT) and 49.3% with a DeepSeek backend. It improves three FDB v1.0 takeover rates over the base model. These results show that task agency can coexist with key conversational agency.

---


### 142. [DS2Agent: Holistic Device Agents for Accelerated Embedded Board-Level Design](https://arxiv.org/abs/2611.25774)

**<font color=#1a73e8>作者：</font>** Hongbin Yang, Chi Zhang, Yinhao Xiao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Embedded board-level development demands extensive expertise, from component selection and device characteristics to interface configuration, driver writing, and system composition. Recently, LLM-based agents have shown strong capabilities, raising the prospect of automating board-level design tasks. However, existing agents either target chip-level design or treat datasheets as static text, offering little guidance on whether a specific component should---or even could---be used for a given board-level design. Moreover, without touching real hardware, they hallucinate incorrect details.
To fill this gap, we present {\setlength{\fboxsep}{1pt}\href{this https URL}{\fcolorbox{blue}{white}{DS2Agent}}}, an open-source framework that constructs interactive agents from device datasheets. Each agent comprises three models: a knowledge model supporting retrieval and question answering; a digital-twin model capturing the physical functionality of the device; and an interface model supporting driver development and system integration. To suppress hallucinations, we also allow optional connections to real devices, so that the agent can calibrate its internalized knowledge against the device. We evaluate DS2Agent on ten devices spanning seven functional categories. Compared with the baseline, the DS2Agent-augmented agent improves the question-answering score from 87 to 97 out of 100 while using 44.8\% fewer tokens. For driver generation, it reduces average token usage per device by 72.9\%. For system integration, it reduces total token usage across three FreeRTOS applications by 29.7\%.

---


### 143. [Suppressing the Shortcut Hidden Behind the Gains of VideoLLM Fine-Tuning](https://arxiv.org/abs/2611.25776)

**<font color=#1a73e8>作者：</font>** Youngwoo Shin, Jongsuk Kim, Junmo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is the stage in which Video Large Language Models (VideoLLMs) advance their capability to reason over video. However, the VideoLLM also learns to answer from textual regularities of its training data, a shortcut that bypasses the video. The regularities behind the shortcut are hard to define at the data level, and the shortcut forms regardless of training epoch, data size, or backbone. The shortcut is hidden behind a rise in accuracy within the training distribution, yet it is not required for the rise and even costs SFT the gain the video offers under distribution shift. We therefore propose Video-Evidence Training via Orthogonal projection (VETO), which intervenes on the fine-tuning update where the shortcut is written rather than on the data. VETO calibrates the subspace that the text alone occupies in the activations of the base model and projects the update onto its orthogonal complement. The VideoLLM is thus left to ground its answer in the full input, with the shortcut suppressed as it forms and never defined. Across seven VideoLLMs, VETO preserves the gain of SFT on the training distribution and suppresses the shortcut. On six benchmarks under shift it gains more than SFT and answers from the full input rather than the shortcut. Code is available at this https URL.

---


### 144. [RouteVerify: Routing Interventions for Step-Level Verification in Mixture-of-Experts Models](https://arxiv.org/abs/2611.25780)

**<font color=#1a73e8>作者：</font>** Yucheng Du, Ryan A. Rossi, Xiyang Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Routing states in mixture-of-experts (MoE) models can distinguish correct from erroneous reasoning steps. If changing routing also changes a model's step-level verification judgment, it is tempting to conclude that the judgment follows what routing encodes. We test this inference with RouteVerify, a controlled intervention study that replaces selected internal activations from one solution trace with activations from another, while keeping the evaluated input unchanged. Across nine MoE checkpoints, we compare three intervention interfaces: router logits, MoE outputs, and post-MoE residual states. We vary the layers and token positions at which activations are replaced. We measure changes in a verification margin that quantifies the model's preference for INCORRECT over CORRECT. We also evaluate the same input with activations from correct versus erroneous steps to test whether the resulting judgment depends on the source step's correctness. We report four linked results. First, probes on router logits separate correct from erroneous steps in eight checkpoints (AUROC 0.80-0.88). Second, replacing router logits across all routed layers changes the judgment in all nine checkpoints, and by more than a norm-matched random replacement. Third, this change rarely depends on whether the source step is correct. At one layer, routing from erroneous steps and from correct steps produces indistinguishable margins in all nine checkpoints. Under all-layer routing, their difference is resolved and positive in only one. Fourth, the same difference is positive for local residual replacements in eight of nine checkpoints, so the measure does detect such dependence where it exists. Correctness is therefore readable from routing, and routing replacements move the judgment, but the movement rarely follows correctness.

---


### 145. [On the Reliability of CyberGym Evaluation: Task Material Consistency and Reference-Target Identity](https://arxiv.org/abs/2611.25790)

**<font color=#1a73e8>作者：</font>** Yule Ding, Hongzhen Wu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> CyberGym evaluates vulnerability reproduction by checking whether a proof-of-concept input (PoC) crashes a vulnerable program version but not a fixed version. Interpreting this differential pass as successful reproduction requires consistent task materials and evidence that the PoC triggers the intended defect. We examine these requirements through a material audit of all 1,507 CyberGym tasks and an identity assessment of the final PoCs from one complete Level-1 GLM-5.3 run. Taking the defect associated with each reference crash report as the target, the audit assigns inconsistency labels to 338 tasks (22.4%) after correcting two labels identified by stratified blind review. The largest categories are coverage inconsistency (205 tasks) and descriptions and patches that jointly point to another defect (110 tasks). We assess PoC identity using an execution check, crash-signature matching, and LLM-assisted root-cause review. Of the 1,286 differential passes, the procedure assigns 89 non-target and 10 insufficient-evidence verdicts; requiring a target hit lowers the pass rate from 85.3% to 78.8%. Non-target verdicts also occur in tasks with no material inconsistency found: 39 of 1,052 differential passes (3.7%). Although the identity verdicts require independent validation, these findings motivate separate checks of task-material consistency and submission identity when interpreting vulnerability-reproduction scores.

---


### 146. [How Reliable Are Explanations of Language Models That Detect Insider Threats?](https://arxiv.org/abs/2611.25796)

**<font color=#1a73e8>作者：</font>** Suramya R. Angdembay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Organizations monitor their workers' activity for insider threats, in which workers misuse their legitimate access, by copying confidential files before leaving. Detectors score how unusual each day of activity is, flagging the most unusual for an analyst to review. Prominent current approaches use opaque neural networks, so explanations of a flag point to internal features: patterns of neuron activity most active on days of misuse. We audit such explanations for language-model detectors trained on CERT's simulated workplace logs. To test an explanation, we see what happens to the detector's score when we remove its features inside the model. We compare this to a control: a change that is as similar as possible to the removal, but without actually removing the features. Because defining "similar" requires choosing a metric, our central contribution is the tipping radius: a first-order prediction of how far that metric must move before the difference between removal and control disappears, a measure of how fragile the result is to that choice. In 33 of 34 runs of seven language models, the tipping radius is at most 18% of the distance between two standard choices of metric. Moving that far removes at least 58% of the difference or reverses it, while random moves of the same size leave it largely intact. The result replicates in thirteen of fourteen pre-declared primary runs on openly released models, though on our trained detectors the difference is often too small to measure. We also find that a flag's score partly reflects who the worker is, not what they did, and that the features named depend on whom they are compared against. Audits should therefore fix the control's metric in advance, report its tipping radius, and disclose that comparison.

---


### 147. [Language models represent more about emphasis than they can tell you](https://arxiv.org/abs/2611.25808)

**<font color=#1a73e8>作者：</font>** Aarne Talman, Stergios Chatzikyriakidis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prosodic prominence can largely be predicted from the words of a sentence, but part of it depends on how the speaker reads it. We study how much of prominence language models recover from text, whether they can report it when asked, and what the speech signal adds. On read English speech labelled for word-level prominence, we compare frozen and fine-tuned text models, prompted large language models (LLMs) and speech models on the same words. All text models end within about one point of each other, at best 68.8% on the 3-way task, and largely make the same errors. With the prompts we tested, LLMs do no better than a word-majority baseline, even with 500 examples. Linear probes find more in their representations. Speech models reach 84.7%. We argue that text determines only part of prominence, and that the rest has to be heard. LLMs encode what the text determines, but prompting does not bring it out: they represent more about where the emphasis falls than they tell you.

---


### 148. [ALIoTh: Orchestrating Multi-Agent LLMs for Autonomous IoT Penetration Testing](https://arxiv.org/abs/2611.25809)

**<font color=#1a73e8>作者：</font>** Pironti Francesco Aurelio, Arena Luigi, Blefari Francesco 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Penetration testing in Internet of Things (IoT) environments, especially those composed of various different devices, e.g., smart plugs, smart cameras, and smart doors, presents great challenges across the phases of information gathering, attack surface enumeration, privilege escalation, and lateral movement. This paper introduces ALIoTh, a multi-agent, workflow-driven penetration testing framework that integrates Large Language Models agents within a Self-Retrieval-Augmented Generation (Self-RAG) architecture to autonomously identify and exploit vulnerabilities in IoT and Industrial-IoT (IIoT) environments. By leveraging state-of-the-art language models and orchestrating specialized agents via the LangGraph framework, ALIoTh dynamically plans and executes a full-spectrum offensive pipeline. This includes network, devices, and service enumeration, vulnerability assessment, payload generation, reverse shell deployment, and privilege escalation on each device. The Self-RAG mechanism equips expert agents with contextual access to IoT security knowledge, e.g., related documentation, tool manuals, and known attack techniques, enhancing their reasoning capabilities in scenarios involving multiple device exploitation and group policy manipulation.

---


### 149. [Efficient and Robust Drafting with Multi-Token Prediction](https://arxiv.org/abs/2611.25813)

**<font color=#1a73e8>作者：</font>** Filippo Galgani, Ziwei Ji, Omri Homburger 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding has emerged as a critical technique for accelerating Large Language Model (LLM) inference by decoupling generation into a drafting phase and a parallel verification phase. A crucial challenge is therefore designing a drafter that is both lightweight and accurate enough to approximate the predictions of the target model. We present a highly optimized Multi-Token Prediction (MTP) architecture that extends existing backbone LLMs to efficiently produce high-quality drafts. Built around a single shared drafting head, our approach features three core architectural optimizations: target activation injection to anchor semantic planning, zero-copy KV-cache cross-attention to bypass prefill compute and reduce memory overhead, and an efficient clustered vocabulary projection to reduce the cost of full-vocabulary decoding. Testing these improvements with the Gemma 4 model family, our G-MTP shows out-of-the-box speedups for both large server-side setups (up to 3.1$\times$) and smaller models targeting memory-constrained on-device environments (up to 2.3$\times$ on H100 and up to 2.2$\times$ on a smartphone GPU). In addition, we present parameter-efficient fine-tuning recipes for G-MTP that keep the drafter aligned with the backbone LLM under domain shift, requiring up to 1.83$\times$ fewer target forward passes than tuning only the backbone.

---


### 150. [What Does Anti-Hallucination Training Buy? Saying Less, Cheap Pruning, and the Rest](https://arxiv.org/abs/2611.25814)

**<font color=#1a73e8>作者：</font>** Lingkai Bu, Qian Gao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preference training is the standard recipe for reducing object hallucination in vision-language models, and each new method reports a lower CHAIR score. We ask what that reduction consists of. Every trained system is compared with its base model's caption truncated to the same object recall, which removes the part of the gain that comes from saying less; the remainder is compared with what a deliberately weak, frozen, eleven-feature post-hoc probe fitted on 500 annotated images can reproduce. All criteria were specified in the analysis code and frozen before the outputs they judge existed. For eight public methods on LLaVA-1.5-7B, the probe reproduces at least two thirds of what training removes beyond saying less for 7 of 8 methods on COCO, 8 of 8 on AMBER and 6 of 8 on Object HalBench, with RLAIF-V the consistent exception; a later public method released for both LLaVA-1.5 and Qwen2.5-VL (SENTINEL) meets the same bar on both. On our own DPO checkpoints the accounting holds on Qwen2.5-VL but fails on InternVL2.5 on COCO (2 of 4 training designs). At matched recall, the base model plus the probe beats truncation for 8 of 9 LLaVA-1.5 systems on COCO and 9 of 9 on AMBER, on the two newer backbones, and when realized as actual sentence deletion. The same measure prices training signals: DPO on the model's own samples labelled by the probe or by an object-level CLIP score recovers 0.70 and 0.87 of the beyond-brevity gain of ground-truth-labelled DPO on Qwen2.5-VL (the probe 0.73 on InternVL2.5), both beat length-matched random labels, and CLIP labels buy more than probe labels on COCO. Human judgements show that the sentences the probe deletes are wrong more often than those truncation would delete; a human check of the CHAIR evaluator's precision falls below our pre-set bar, which we report as a limitation.

---


> [!TIP]
> 当前位于：**101-150**（第 3/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-266](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
