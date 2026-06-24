# 🧠 大模型相关研究 | 2026年06月24日

> 本类共 **118** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-118](./part-03.md)

---

### 51. [SURGELLM: Rethinking Multi-Task Evaluation through Task-Aware Feature Gating with Class-Balanced Normalization](https://arxiv.org/abs/2606.24259)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad, Ulug Bayazit  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuned encoders deployed across heterogeneous NLP tasks face three compounding problems: mismatched inductive biases, class-imbalance corruption of feature statistics, and no mechanism to condition attention on external lexical knowledge. We introduce \textbf{\surgellm}, a unified transformer framework that addresses each with a dedicated lightweight module: a \emph{surgical feature gate} (learned per-dimension sigmoid over curated lexical indicators and \texttt{[CLS]}; provably degenerates to identity when features are uninformative), \emph{task-conditioned prefix tokens} (quantized feature values and task identity prepended to every input), and \emph{Instance-Weighted Normalization} (IWN; removes class-prior bias from gate statistics). We prove an excess-risk bound linking gate benefit to \emph{surgical feature alignment}. Across four tasks, SST-2, multi-hop retrieval, LLM-prompt attribution, and authorship detection, covering 17,830 examples and eleven model variants over three seeds, the IWN variant achieves macro-F1 \textbf{0.940} ($+0.036$ over the strongest non-IWN baseline; $+0.130$ on authorship detection). A random-vocabulary control ($-0.028$ avg.\ F1) confirms gains are lexical, not parametric. Code, vocabularies, and a $99.5\%$-recovery auto-extraction recipe are released.

---


### 52. [Pigeonholing: Bad prompts hurt models to collapse and make mistakes](https://arxiv.org/abs/2606.24267)

**<font color=#1a73e8>作者：</font>** Hyunji Nam, Keertana Chidambaram, Dorottya Demszky 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While in-context learning is generally shown to be effective in Large Language Models (LLMs), bad contexts can cause performance degradation and mode collapse, a phenomenon we call "pigeonholing." **Unintentionally bad** contexts can happen without malicious jailbreaking intents: For example, a user asks the model to justify an incorrect math theorem or fails to correct the model's buggy code. Specifically, we investigate ``pigeonholing" in two scenarios: (1) when the user suggests a solution, and (2) when the conversation context includes the assistant's previous (incorrect) responses. Our experiments across 10 verifiable and open-ended tasks with 10 different models show that pigeonholing manifests in several ways: (1) repeating the incorrect answers from context (leading to 38-40% performance drop), (2) converging on a narrow set of answers in coding and text generation without exploring alternatives, and (3) flipping stance on controversial topics to align with the user or the assistant's previous claims. We find that pigeonholing worsens almost monotonically with the number of conversation turns (performance drops by additional 14+% as repeated mistakes increase from 1 to 5), and pigeonholing-induced mode collapse can happen even when the provided example is correct. As a step toward mitigation, we propose RLVR with synthetic errors which improves models by 43-60% under bad contexts compared to vanilla RLVR baselines.

---


### 53. [CALIBER: Calibrating Confidence Before and After Reasoning in Language Models](https://arxiv.org/abs/2606.24281)

**<font color=#1a73e8>作者：</font>** Conor Finlay, Joshua Kurien, Saurabh Dash 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning language models are increasingly asked not only to answer difficult questions, but also to estimate their likelihood of success. Existing methods typically elicit confidence only once: either before thinking or after answering. We argue that confidence in reasoning models is state-dependent: before thinking, confidence should estimate the chance of the model correctly solving the prompt, while after thinking it should predict whether the realized answer is likely to be correct. This distinction determines the appropriate supervision target: prompt-level success should supervise confidence estimates made after seeing the prompt, while individual answer-level correctness should supervise confidence estimates made after answering. We introduce CALIBER (Calibration Before and After Reasoning), which elicits both estimates and supervises each with the target matched to its information state. Under this unified protocol, CALIBER reduces Expected Calibration Error (ECE) by 52.5% over the strongest single-confidence baseline on BigMathDigits for the 7B model, while achieving the best Brier score and AUROC, and remains within 2.1 points of the best accuracy. Further, on a larger 30B model, CALIBER achieves the best ECE on BigMathDigits while remaining competitive in Brier score and AUROC. Out of distribution, it achieves the best ECE and Brier score on GPQA and TriviaQA, and remains competitive on SimpleQA. Ablations further show that this position-target alignment is most beneficial under distribution shift where it consistently reduces calibration error across all out-of-distribution benchmarks.

---


### 54. [AVOC: Enhancing Hour-Level Audio-Video Understanding in Omni-Modal LLMs via Retrieval-Inspired Token Compression](https://arxiv.org/abs/2606.24286)

**<font color=#1a73e8>作者：</font>** Yijing Chen, Wenhui Tan, Xiaoyi Yu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models have achieved remarkable progress in short-form audio-video understanding, yet long-form audio-video comprehension remains challenged by limited context windows and severe information redundancy. To address these bottlenecks, we propose AVOC, a framework for long-form audio-video understanding in Omni-modal Large Language Models. AVOC introduces a learnable token compression module between the modality encoders and the LLM backbone. We reframe multimodal token compression as a top-$K$ retrieval problem: given a fixed context budget, the module must retrieve a compact subset of tokens that best supports answering the user query. We draw inspiration from three classical Information Retrieval criteria for selecting informative units from a large candidate pool: relevance, importance, and diversity. AVOC instantiates each criterion as a tailored mechanism for audio-video understanding, and integrates them into a unified retrieval-style compression pipeline. Experiments show that AVOC achieves state-of-the-art performance on long-form audio-video benchmarks, surpassing the second-best model by 4.9 and 5.5 points in average accuracy on OmniVideoBench and LVOmniBench, respectively. Moreover, AVOC maintains robust performance on Audio-Video Needle-in-a-Haystack task at durations up to one hour.

---


### 55. [ActiveScope: Actively Seeking and Correcting Perception for MLLMs](https://arxiv.org/abs/2606.24292)

**<font color=#1a73e8>作者：</font>** Yajing Wang, Chao Bi, Junshu Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated impressive vision-language understanding, yet still struggle with fine-grained perception in high-resolution images. While existing training-free methods typically rely on attention-based localization or coarse-to-fine search, they are often misled by distractors and fail to locate multiple targets. Our investigation attributes these failures to Contextual Dominance, where salient distractors overwhelm target attention and cause inaccurate localization, and Semantic Bias, where global semantics cause the model to fixate on the most salient concept, resulting in incomplete localization in multi-object scenarios. Built on these insights, we propose ActiveScope, a training-free framework that enhances MLLMs by actively seeking and correcting perception. ActiveScope features two modules. The Semantic Anchor Localization (SAL) utilizes fine-grained semantic anchors to independently localize key targets, thereby mitigating semantic bias. The Interference-Suppressed Refinement (ISR) refines localization by suppressing attention on salient distractions to overcome contextual dominance. Extensive experiments on high-resolution image understanding benchmarks demonstrate that ActiveScope outperforms existing training-free methods (e.g., 96.34 percent accuracy on $V^{*}$ Bench), validating the superiority of the active search and self-correction paradigm. Our code is available at this https URL.

---


### 56. [LemonHarness Technical Report](https://arxiv.org/abs/2606.24311)

**<font color=#1a73e8>作者：</font>** Kailong Ren, Fubo Sun, Jiachen Liu 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language model (LLM) agents are applied to longer tasks, they increasingly modify workspace state across multiple rounds of iteration. However, agents typically observe only tool outputs and log fragments, while the actual state changes occur in the file system. Without explicit workspace boundaries, state-changing operations such as file writes and temporary artifact generation may scatter changes across paths. Over time, these weakly constrained changes accumulate, making states such as modified files difficult to track. This paper presents LemonHarness, an integrated execution framework for long-horizon agents. LemonHarness establishes an explicit execution boundary by constraining state-changing operations within a clearly defined workspace and bringing model invocation, tool execution, and rule knowledge within a single controlled boundary. State-changing operations, including file writes, dependency installation, and temporary artifact creation, are executed through structured tool interfaces, with execution feedback recorded as observations available to subsequent model decisions. The system also introduces a reusable rule knowledge base, which turns recurring execution rules and acceptance criteria into runtime knowledge. LemonHarness further adds a time-aware execution mechanism that exposes elapsed and remaining budget to the model, so it can rebalance exploration, implementation, and validation effort as time pressure shifts and avoid timeouts from long waits or excessive verification. On Terminal-Bench 2.0, LemonHarness_GPT-5.3-CodeX reached 84.49% accuracy over 445 trials; pairing the same framework with the stronger GPT-5.5 backbone raised the average accuracy to 86.52% across five jobs. The results suggest that a unified runtime boundary, callable rule knowledge, and time-aware execution can improve the stability of long-horizon agent execution.

---


### 57. [Prague Dependency Treebank -- Consolidated 2.0: Enriching a Complex Annotation Scheme](https://arxiv.org/abs/2606.24324)

**<font color=#1a73e8>作者：</font>** Marie Mikulová, Jiří Mírovský, Milan Straka 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Prague Dependency Treebank framework is unique in its attempt to systematically include and link different layers of language, including a meaning representation with several types of inter-sentential phenomena, especially coreference and discourse relations. We present its second consolidated version (PDT-C 2.0), which concludes almost 30-years long project of sustained development of the resource to a uniformly and coherently annotated, genre-diversified, almost 4 million token language resource of Czech language, with accompanying fully compatible lexicons. In addition to continuous linguistic research, the richly linguistically annotated corpus is also widely used in international comparisons of the development of traditional and novel NLP tools as well as in conversions into other formalisms. The corpus and the trained parsers are available under the CC BY-NC-SA licence.

---


### 58. [Transformer-Based Language Models Across Domain Verticals: Architectures, Applications and Critical Assessment](https://arxiv.org/abs/2606.24331)

**<font color=#1a73e8>作者：</font>** Guruprakash J, Krithika L.B  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models have become the default substrate for natural language processing and the pace of new releases has made it hard for practitioners to separate durable ideas from the noise of incremental announcements. This review works at two levels. At the level of mechanism, we organise the main transformer families into a working taxonomy, covering encoder-only, decoder-only, encoder-decoder, long-context, permutation-based, and generator-discriminator variants. We then extend the discussion to post-2023 developments that changed the picture in practice: instruction tuning, reinforcement learning from human feedback, direct preference optimisation, mixture-of-experts scaling, retrieval augmentation and the current flagship model families from OpenAI, Anthropic, Google, Meta, Mistral and DeepSeek. At the level of use, we survey deployments across healthcare, finance, legal, education, customer service, creative writing and scientific work. Based on this we link each to the specific capabilities that make a transformer the appropriate tool. The contribution of this paper is a critical assessment that is based on the survey. We compare architectures on four axes that matter to deployment decisions, we quantify the trade-off between parameter count and energy cost. We also discuss how alignment methods, data provenance and benchmark saturation change what it means to call a model "state of the art". The final section lists the research questions that we think deserve more attention.

---


### 59. [Ill-Posed by Design: Probing Evidence Use in VLMs](https://arxiv.org/abs/2606.24335)

**<font color=#1a73e8>作者：</font>** Boaz Meivar, Shaked Perek, Shani Shvartzman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counterfactual analysis is widely used to study evidence use in vision-language models, but its diagnostic value is limited on well-posed tasks: when several cues independently support the same answer, removing one may not change the prediction. We propose monocular metric object-size estimation as an ill-posed diagnostic setting for evidence selection: because physical size cannot be determined from a single uncalibrated image, models must rely on imperfect cues category priors, target appearance, local context, apparent image size, and scene geometry. We assemble Metric VQA ($10{,}813$ dimension queries from Objectron and $331$ tape-measured in-the-wild scenes) and evaluate $12$ open-weight VLMs ($3$--$397$\,B parameters) with counterfactual analysis decomposing six visual and language evidence channels. Even the largest VLMs tested (Qwen3-VL-235B, Qwen3.5-397B, InternVL3.5-241B) trail a text-only frontier LLM on the in-the-wild split. The diagnostic analysis shows: target identity is the most load-bearing cue, target pixels and local context help only some models, apparent size shifts predictions without a directional readout, and global scene geometry is largely unused. We analyze LoRA fine-tuning as an actionable intervention specific to metric estimation: while the task is learnable, the models do not learn to leverage scene geometry.

---


### 60. [Accelerating Disaggregated RL for Visual Generative LLMs with Diffusion-Based Parallelism and Trainer-Assisted Generation](https://arxiv.org/abs/2606.24369)

**<font color=#1a73e8>作者：</font>** Sijie Wang, Zhengyu Qing, Zhiqiang Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become a dominant post-training paradigm, driving the emergence of high-performance RL systems such as veRL for autoregressive large language models (LLMs). In parallel, diffusion-oriented RL algorithms, e.g., DanceGRPO and FlowGRPO, have rapidly expanded the scope of RL from language reasoning to diffusion-based visual and flow-based generation. However, efficient RL systems for diffusion generative LLMs remain underexplored. Existing implementations, e.g., veRL-Omni, still rely on colocated execution, which simplifies synchronization but couples rollout and training resources, limits heterogeneous deployment, and constrains independent scaling.
To this end, we introduce DigenRL, a disaggregated RL framework for diffusion-based generative LLMs that supports flexible resource allocation, accommodates heterogeneous GPUs, and facilitates efficient task scheduling. To maximally reduce the execution bubbles in the disaggregated architecture, we propose: 1) a generation-axis pipeline (GAP) and time-step parallelism (TSP) in the diffusion architecture to enable finer-grained pipelining between rollout and training; 2) an elastic trainer-assisted generation (TAG) approach to enable the trainer GPU resources to dynamically assist in executing rollout generations; and 3) a tightly one-step constrained asynchronous strategy to further utilize the tail bubble in the pipeline. Extensive experiments are conducted on three hardware testbeds with 16-32 GPUs using HunyuanVideo-13B, Wan2.1-14B, FLUX.1-12B, and QwenImage-20B generative models. Experimental results show that DigenRL achieves 1.56-2.10x throughput improvements over state-of-the-art diffusion RL systems, veRL-Omni and GenRL.

---


### 61. [When Helpfulness Overrides Causal Caution: Context-Dependent Suppression and Recovery in LLMs](https://arxiv.org/abs/2606.24370)

**<font color=#1a73e8>作者：</font>** Hiroshi Okumura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly integrated into decision-support roles in business and policy contexts. While prior benchmark studies have primarily evaluated LLMs' causal reasoning capabilities, a more fundamental epistemic dimension has been overlooked: Causal Caution, defined as the propensity to refrain from causal judgment when empirical evidence is insufficient. This study examines the systematic suppression of Causal Caution that occurs when LLMs shift from academic to practical advisory contexts. Using an evaluation rubric inspired by Pearl's Causal Hierarchy (the PCH score), we conducted experiments on four high-performance LLMs -- Claude Sonnet 4.6, Claude Opus 4.7, GPT 5.5, and Gemini 3.1 Pro -- across 480 trials. Causal Caution maintenance rates were 91.7--100.0% in academic contexts but dropped to 6.7--18.3% in practical advisory contexts (Fisher's exact test, p < .001 across all models). Furthermore, when restricted to practical prompts requesting concrete recommendations or explanatory rationales, only 1 of 200 responses (0.5%) maintained Causal Caution. A brief self-correction prompt -- "Please reconsider this judgment from the perspective of causal relationships" -- restored the expression of Causal Caution to maintenance rates of 71.4--100.0% (McNemar's test, p < .001 across all models). These results suggest that helpfulness-oriented response patterns may suppress the expression of Causal Caution in practical advisory contexts, with important implications for organizational governance. The findings indicate that this suppression reflects context-dependent variation in expression rather than an underlying capability limitation, suggesting that multi-agent architectures that separate proposal generation from causal auditing may offer a promising governance design.

---


### 62. [On the Stability of Prompt Ranking in Large Language Model Evaluation](https://arxiv.org/abs/2606.24381)

**<font color=#1a73e8>作者：</font>** Shaoshuai Du, Penghao Liang, Yixian Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt-based interaction has become a dominant paradigm for using large language models (LLMs), where multiple candidate prompts are evaluated and the top-ranked one is selected for downstream use. This workflow implicitly assumes that prompt rankings are stable under minor variations in evaluation conditions. In this paper, we systematically study prompt ranking stability under common sources of variability, including random seeds and limited evaluation subsets. Across three open-weight LLMs and two benchmark tasks, we find that while overall rank correlations are often moderate to high, the identity of the top-performing prompt frequently changes, leading to unreliable selection decisions. To address this issue, we propose a simple stability-aware selection strategy based on a lower confidence bound, which accounts for both performance and variance. Our results show that this approach improves robustness in unstable settings while remaining competitive in more stable regimes. These findings highlight the importance of accounting for evaluation uncertainty in prompt selection and LLM benchmarking.

---


### 63. [PHANTOM: A Large-Scale Dataset of Multimodal Adversarial Attacks for Vision-Language Models](https://arxiv.org/abs/2606.24388)

**<font color=#1a73e8>作者：</font>** Simone Gallivanone, Hossein Khodadadi, Mauro Dore 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a large-scale, open-source dataset of pre-generated adversarial attacks for vision-language models (VLMs). The dataset is designed to be diverse, representative, and practical, extending existing benchmarks by covering 10 high-level categories and 55 subcategories of harmful intents. Our primary goal is to make adversarial data accessible to the research community, given the computational cost and complexity of generating large numbers of attacks. The dataset comprises 47 524 adversarial samples, generated using state-of-the-art attack strategies from recent literature. Our work complements existing efforts by consolidating and extending prior benchmarks from multiple established sources, resulting in 7 826 intents, and introduce an additional category to broaden coverage. This provides realistic evaluation resources for studying model robustness and alignment. Our dataset intends to enable researchers and practitioners to systematically evaluate the robustness and safety of VLMs, fine-tune attack-generation models, and develop or stress-test defensive guardrails under diverse adversarial conditions. By releasing this resource, we aim to lower the barrier to adversarial research and foster more reproducible, comprehensive, and comparable evaluations of VLM safety.

---


### 64. [Age of LLM: A Strategic 1v1 Benchmark for Reasoning, Diplomacy and Reliability of Large Language Models under Fog of War](https://arxiv.org/abs/2606.24391)

**<font color=#1a73e8>作者：</font>** Arnaud Ricci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce Age of LLM, a turn-based 1v1 benchmark in which two LLMs face off on a 13x7 grid to destroy the enemy base. Three stressors are deliberate: fog of war, full diplomacy (messages, ceasefires, ultimatums; uranium kept secret), and a reliability dimension where every turn must follow a strict JSON schema and an illegal action is silently discarded. The engine is private and each match uses a fresh random map seed and opponent, mitigating the data contamination that affects public benchmarks. Models receive a (near) rule-only prompt with no build-order advice (two tactical seed phrases were present during data collection; see Section 2.7). We benchmark 15 reasoning models across 54 matches and 5,258 actions. Findings: (1) the nuclear rush dominates (78% on the rules-coherent v0.11+ sub-corpus; 85% corpus-wide) with a sole-launcher signature that is largely mechanical under secret-simultaneous launch rules, not a cognitive deterrence failure; (2) military conquest is rare but faster (12.3 vs 18.9 turns); (3) diplomacy is prolific yet almost never consummated; (4) ~58% of illegal actions are fog/state errors, making the illegal-action rate a measure of belief-tracking; (5) -- the least established, and the only one we label exploratory -- a weak link associates reliability with winning. The corpus is small, unbalanced and not side-swapped, so the ranking is a preliminary descriptive view, not a contribution. Beyond ranking, the turn-by-turn traces of actions and messages make the corpus a lens on how LLMs reason under adversarial uncertainty -- their belief-tracking, spontaneous deception, and per-model cognitive "personas" -- which we frame as a future research direction. We release the replay format, an isometric viewer and all replays; engine source on request.

---


### 65. [Average Rankings Mask Per-Subject Optimality: A Friedman-Nemenyi Benchmark of EEG Motor-Imagery BCI Decoders](https://arxiv.org/abs/2606.24394)

**<font color=#1a73e8>作者：</font>** Xavier Vasques, Paul Barbaste, Olivier Oullier  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is the dominant non-invasive modality for brain-computer interfaces (BCIs), yet reliable decoding of motor imagery is hampered by inter- and intra-individual variability. A recurring claim is that one decoding pipeline, most often a spatial or Riemannian method, is broadly preferable. We test the weakest version of that claim under the most favourable conditions. Using the Mother of All BCI Benchmarks (MOABB) framework, we evaluated 1,056 decoding configurations (feature extractor x scaler x classifier), >340,000 subject-level model fits, across three public left-versus-right motor-imagery datasets (PhysionetMI, 109 participants; Cho2017, 52; Zhou2016, 4) and two frequency bands (8-15 Hz, 8-30 Hz). Every model is fit and tested within a single session of a single participant, the easiest regime, giving every pipeline its best chance. We apply the statistics standard for multi-classifier comparison: Friedman omnibus tests, Nemenyi critical-difference analysis and Wilcoxon signed-rank tests with effect sizes. Covariance tangent-space projection (cov-tgsp) and Common Spatial Patterns (CSP) are the strongest families, but their ordering is dataset-dependent and, on the largest and most heterogeneous cohort (PhysionetMI), statistically indistinguishable (Nemenyi p = 0.27; Kendall's W = 0.11). At the individual level the single best pipeline is optimal for only 35% of PhysionetMI participants, and nonlinear descriptors are best for roughly one third; matching pipeline to participant adds about seven accuracy points over the best fixed choice. The ranking is not an artefact of dimensionality, and classifier and scaler choices are secondary to the feature representation. Even in the easiest regime, no single pipeline dominates: a lower bound on the personalization problem and a quantitative case for participant-aware model selection rather than a universal decoder.

---


### 66. [Natural Identifiers for Privacy and Data Audits in Large Language Models](https://arxiv.org/abs/2606.24408)

**<font color=#1a73e8>作者：</font>** Lorenzo Rossi, Bartłomiej Marek, Franziska Boenisch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Assessing the privacy of large language models (LLMs) presents significant challenges. In particular, most existing methods for auditing differential privacy require the insertion of specially crafted canary data during training, making them impractical for auditing already-trained models without costly retraining. Additionally, dataset inference, which audits whether a suspect dataset was used to train a model, is infeasible without access to a private non-member held-out dataset. Yet, such held-out datasets are often unavailable or difficult to construct for real-world cases since they have to be from the same distribution (IID) as the suspect data. These limitations severely hinder the ability to conduct scalable, post-hoc audits. To enable such audits, this work introduces natural identifiers (NIDs) as a novel solution to the above-mentioned challenges. NIDs are structured random strings, such as cryptographic hashes and shortened URLs, naturally occurring in common LLM training datasets. Their format enables the generation of unlimited additional random strings from the same distribution, which can act as alternative canaries for audits and as same-distribution held-out data for dataset inference. Our evaluation highlights that indeed, using NIDs, we can facilitate post-hoc differential privacy auditing without any retraining and enable dataset inference for any suspect dataset containing NIDs without the need for a private non-member held-out dataset.

---


### 67. [Agentic AI for Bilevel Long-Term Optimization of Policy-Driven Physical Layer Systems](https://arxiv.org/abs/2606.24416)

**<font color=#1a73e8>作者：</font>** Bingnan Xiao, Chenhao Yang, Wei Ni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Network operators' changing policies, service requirements, and stringent real-time constraints render existing methods designed with fixed objectives and constraints ineffective. This paper presents Agentic long-term performance optimization (Agentic-LTPO), a nested bilevel optimization framework that can be applied to adaptive physical layer problem configuration. The key idea is to employ agentic AI to generate upper-level configurations in a bilevel optimization structure, where evolving operator policies, environment summaries, and historical experiences are translated into structured lower-level optimization problem configurations. The lower level solves the problems with updated configurations for real-time physical-layer decisions. Considering cell-free MIMO beamforming as a use case, we embody Agentic-LTPO by designing a new multi-agent decision process with retrieval-augmented experience-based verification in the upper level, together with a closed-form beamformer in the lower level. Experiments demonstrate that Agentic-LTPO exhibits strong adaptability to dynamic operator policies and effectively enhances the system's long-term performance by 57.2% compared to traditional methods.

---


### 68. [Beyond Logprobs: A Multi-Signal Confidence Engine for LLM-Based Document Field Extraction](https://arxiv.org/abs/2606.24420)

**<font color=#1a73e8>作者：</font>** Nitesh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In high-stakes document processing pipelines, including financial reconciliation, compliance verification, and procurement automation, an LLM extraction that is silently wrong is more dangerous than one that is visibly absent. The central challenge is not extraction accuracy alone but reliable confidence estimation: knowing, field by field, whether an extraction can be trusted for automation or deferred to human review. Token-level log-probabilities, verbalized confidence, and multi-sample self-consistency all collapse toward all-positive behaviour at practical thresholds, offering no reliable separation between trustworthy and untrustworthy extractions.
We present ExtractConf, a cross-domain, field-agnostic confidence engine that grounds confidence estimation in two structurally different readings of the same document. A field-guided Hunter call extracts each field under schema-slot completion pressure; a document-guided Mapper call scans holistically and surfaces values grounded in document content. This asymmetry yields different failure modes: Hunter hallucinates values for absent fields, while Mapper misses visually non-salient ones. Their disagreement is independently informative. ExtractConf fuses cross-call disagreement, LLM-internal uncertainty, OCR, image quality, and spatial layout into a classifier requiring no domain-specific rules or retraining. On DocILE (55-field invoices, 26% failure rate), it achieves 0.928 ROC AUC and reduces selective prediction risk by 70% over logprob-mean. At 80% coverage, accuracy reaches 99.1%, enabling a practical human-in-the-loop workflow. Zero-shot transfer to CORD receipts achieves 0.858 AUC; lightweight Lasso recalibration reduces ECE by 89% and Brier by 43%, confirming the signals generalise across document domains.

---


### 69. [Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning](https://arxiv.org/abs/2606.24428)

**<font color=#1a73e8>作者：</font>** Shiding Zhu, Yudi Qi, Yajie Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Experience-driven self-evolution is critical for large language model (LLM) agents to improve through open-world interaction. However, existing experience learning methods mostly rely on single-agent loops, where the same agent executes tasks, summarizes outcomes, and determines memory content. This setup makes agents vulnerable to the Self-Confirmation Trap: wrong-but-self-consistent trajectories are misidentified as successful experience, leading to cumulative errors during retrieval and reuse. To address this issue, we propose EDV, an Execute-Distill-Verify framework for reliable experience learning. In the Execute stage, multiple heterogeneous agents explore the same task space in parallel to generate diverse candidate trajectories. In the Distill stage, a dedicated third-party agent comparatively analyzes these trajectories to produce candidate experiences, reducing executor-centric summarization bias. In the Verify stage, the execution group validates candidates via a consensus mechanism, and only approved experiences are written into shared or private memory. By decoupling the three stages, EDV transforms experience learning from isolated self-reflection into collaborative construction, filtering erroneous and noisy content before memory insertion. We evaluate EDV on three challenging long-horizon benchmarks: tau2-bench, Mind2Web and MMTB. Results show EDV consistently outperforms strong baselines, validating that reliable experience construction is essential for robust agent self-evolution. Our code is available at this https URL.

---


### 70. [An LLM-based Two-Stage Transformer Framework for Cross-Domain Bearing Fault Diagnosis with Limited Data](https://arxiv.org/abs/2606.24459)

**<font color=#1a73e8>作者：</font>** Jinghan Wang, Feng Cheng, Wentao Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bearing fault diagnosis faces critical challenges when dataset heterogeneity, operating condition variations, and limited labeled data occur simultaneously in industrial environments. Existing approaches address these issues in isolation and rely on implicit feature alignment, limiting effectiveness under concurrent challenges. This paper proposes a knowledge-guided two-stage transfer learning framework that employs a lightweight GPT-2-style Transformer with causal self-attention for hierarchical feature extraction from vibration signals, establishing explicit pathways where pre-trained encoder weights and fault prototype embeddings serve as knowledge carriers from multi-source pre-training to target adaptation. The framework addresses the dual-shift challenge through multi-source learning for generalizable representations, prototype-based knowledge modulation for target adaptation, and taxonomy-adaptive classification for seamless transfer across heterogeneous fault categories. Experimental validation on four real-world datasets demonstrates 92.61% average accuracy with only 10% labeled target data, outperforming state-of-the-art methods by 17.24 percentage points, establishing a practical pathway toward cost-effective predictive maintenance in Industry 4.0 applications.

---


### 71. [The African Language Tax: Quantifying the Cost, Latency, and Context Penalty of Tokenizing African Languages in Frontier LLMs](https://arxiv.org/abs/2606.24460)

**<font color=#1a73e8>作者：</font>** Olaoye Anthony Somide  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Commercial large language models bill, scale latency, and budget context per token. Yet tokenizers assign more subword tokens to the same meaning in some languages than in others, so speakers of languages with high token-fertility pay a structural penalty before a model is ever invoked. This penalty is documented for multilingual settings in general, but it has not been measured systematically for African languages at the level of enterprise deployment economics and cognitive context capacity. We measure it across 20 African languages spanning five language families and three scripts (Latin, Ge'ez/Ethiopic, N'Ko; 19 appear in the primary FLORES-200+ corpus, with Nigerian Pidgin measured via MAFAND-MT only), using parallel corpora so that the language effect is isolated from content. Across 11 frontier and open tokenizers on FLORES-200+, every African language carries a tokenization premium above English (median 1.88x on GPT-5 / o200k_base, up to 8.92x for N'Ko); the penalty is largest for Ethiopic and N'Ko scripts (reaching 7-9x) and is near-invariant across corpora (FLORES vs SIB-200 Pearson r = 0.9998). Translated into deployment terms, this results in up to 8.9x inference cost and an equivalent generation-latency multiplier (N'Ko vs English on GPT-5; 7.4x for Amharic), and as little as 11% of English's effective context window. The best currently available tokenizer for African languages, Gemma 4, reduces the mean premium from 3.31x (cl100k_base) to 2.38x, but no tokenizer eliminates the penalty. We release an open measurement tool (afri-fertility), a public leaderboard, a results dataset, and mitigation guidance for African builders. The penalty falls hardest on the languages whose speakers can least afford it, a digital divide encoded directly into the subword vocabulary.

---


### 72. [CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference](https://arxiv.org/abs/2606.24467)

**<font color=#1a73e8>作者：</font>** Xiaolin Lin, Jingcun Wang, Olga Kondrateva 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context large language model (LLM) inference is increasingly constrained by the memory footprint and decoding cost of key-value (KV) caches, limiting sustainable deployment on resource-constrained hardware. Existing KV cache eviction methods typically apply heuristic token scoring over all heads in GQA-based LLMs. These methods ignore the different functionalities of attention heads, leading to the eviction of critical tokens and thus degrading the performance of LLMs. To address this issue, we propose CompressKV, a resource-efficient KV-cache compression framework for GQA-based LLMs. Instead of aggregating attention scores from all heads, CompressKV identifies Semantic Retrieval Heads (SRHs) that capture both the initial and final tokens of a prompt and semantically important mid-context evidence, and uses them to select tokens whose KV pairs should be retained. Furthermore, CompressKV allocates cache budgets across layers according to offline estimates of layer-wise eviction error. Experiments on LongBench and Needle-in-a-Haystack show that CompressKV consistently outperforms existing KV-cache eviction methods across memory budgets. Notably, it preserves over 97\% of full-cache performance using only 3\% of the KV cache on LongBench question-answering tasks and achieves 90\% accuracy with just 0.7\% KV storage on Needle-in-a-Haystack. These results demonstrate an improved resource--performance trade-off for long-context LLM inference. Our code is publicly available at: this https URL

---


### 73. [video-SALMONN-R$^3$: Learning to ReWatch, ReAsk, and ReAnswer for Efficient Video Understanding](https://arxiv.org/abs/2606.24477)

**<font color=#1a73e8>作者：</font>** Yixuan Li, Guangzhi Sun, Yudong Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large language models (LLMs) are often constrained by computation and memory budgets, leading them to use reduced frame rates and spatial resolutions, which may cause them to miss critical information for question answering (QA). A practical and efficient solution is a two-stage paradigm: first perform coarse video understanding to localize relevant segments, and then re-watch these segments at higher temporal or spatial fidelity. In this paper, we present video-SALMONN-R$^3$, the first end-to-end video-LLM that enables re-watch through reinforcement learning without relying on chain-of-thought (CoT) cold-start. This design removes the need for costly CoT data annotations and avoids CoT-based supervised fine-tuning (SFT), which can otherwise degrade the pretrained video understanding abilities. To address the mismatch between the reasoning-first behavior induced by re-watch and the answer-first tendency of pretrained video-LLMs, we propose a re-answer strategy, in which the model first produces a direct answer in the first watch and then refines it after re-watching. Finally, to improve question adherence during re-watching, we propose a re-ask mechanism that re-injects the query when revisiting localized segments. Experimental results show that video-SALMONN-R$^3$ consistently outperforms both the base model and the QA-SFT baseline, while surpassing prior re-watch-based approaches with significantly lower computational cost. Code, models, and data will be publicly released upon acceptance.

---


### 74. [Advancing WordArt-Oriented Scene Text Recognition: Datasets and Methods](https://arxiv.org/abs/2606.24484)

**<font color=#1a73e8>作者：</font>** Xingsong Ye, Yongkun Du, Jiaxin Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> WordArt (artistic text) features highly customized fonts, textures, and layouts, making WordArt-oriented scene TExt Recognition (WATER) substantially more challenging than general Scene Text Recognition (STR). Existing STR datasets and methods, typically built around regular scene text and fixed-template inputs, struggle to scale to WATER. Thus, we aim to advance this task from both data and model perspectives. On the data side, we construct a 2M synthetic dataset, WATER-S, with the scale improved by hundreds of times compared to existing artistic text data. WATER-S consists of two complementary subsets. One rendered by an upgraded rendering pipeline (SynthWordArt), which provides highly accurate and controllable synthetic WordArt data. The other is generated by combining Qwen3-VL for prompt mining and Z-Image for image synthesis, which improves the coverage of realistic and diverse data. On the model side, we propose WATERec. It adopts an visual encoder supporting arbitrary-shaped inputs and an autoregressive decoder to model complex layouts, structurally breaking the bottleneck of fixed-template STR on WordArt. Experiments show that this architecture outperforms prior STR methods, achieving state-of-the-art performance on irregular texts such as WordArt. Together with WATER-R, carefully reorganized from existing real STR data, our strong baseline with the new synthetic data and model design reaches 90.40% accuracy on WordArt-Bench, surpassing both general-purpose and OCR-specialized vision-language models by a large margin. Code and data are available at this https URL.

---


### 75. [RetiSEM: Generalising Causal Models for Fragmented Biomedical Data](https://arxiv.org/abs/2606.24488)

**<font color=#1a73e8>作者：</font>** Inam Ullah, Imran Razzak, Shoaib Jameel  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning causal models from fragmented biomedical data is challenging because clinical, molecular, and imaging variables are often incomplete or not jointly observed. We propose RetiSEM, a domain-constrained structural equation modelling (SEM) framework for causal graph recovery and mediation analysis under limited multimodal resources. This proposed work organises variables into biologically informed blocks, applies forbidden-edge constraints, and decomposes pathway-level effects into TE, NDE, and NIE components. We evaluate RetiSEM across ten synthetic benchmark scenarios that vary in dimensionality, nonlinearity, causal depth, and pathway structure, together with a fragmented real-world setting that combines NHANES clinical variables with externally derived retinal representations. This approach achieves lower structural error and higher causal accuracy than unconstrained baselines across the synthetic benchmarks. In the real-data analysis, retinal variables behave mainly as downstream biomarker-like indicators, with smaller but detectable indirect effects. These findings support our strategy as an interpretable framework for testing structured causal hypotheses in limited-resource biomedical AI. The code and resources for this work are publicly available at: this https URL.

---


### 76. [On the Smallness of the Large Language Models Scaling Exponents](https://arxiv.org/abs/2606.24504)

**<font color=#1a73e8>作者：</font>** Sauro Succi, Peter V. Coveney, Alex Hansen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We discuss reasons why the scaling exponents of current Large Language Models (LLMs) applications are indicating an unsustainable regime in terms of energy resources. We further show that attributing the smallness of such exponents to a numerical bias due to the neglect of a non-zero value of the loss function in the limit of infinite data (``pedestal effect") does not remove the unsustainability issue. Finally, the effects of the smoothness (roughness) of the data on the scaling exponents is commented upon based on an analogy with phenomenological models of fluid turbulence.

---


### 77. [A Fair Evaluation of Graph Foundation Models for Node Property Prediction](https://arxiv.org/abs/2606.24509)

**<font color=#1a73e8>作者：</font>** Oleg Platonov, Gleb Bazhenov, Dmitry Eremeev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Due to the wide use of graph-structured data in different fields of industry and science, the development of Graph Foundation Models (GFMs) has recently attracted a lot of attention. While many different types of models are called GFMs, particular interest has been paid to GFMs designed for node property prediction tasks, which is one of the most popular settings in Graph ML with lots of real-world applications from fraud detection in financial and social networks to recommendation systems for e-commerce and user-generated content platforms. While a number of GFMs for this task have been recently proposed, the field has not converged to a unified evaluation setting, and different works evaluate their models in widely different ways, preventing reliable comparison of GFMs with each other and with other types of models. In this work, we conduct a fair and rigorous reevaluation of 9 recent GFMs for node property prediction, comparing them to strong Graph Neural Network (GNN) baselines. We find that, among these GFMs, only the most recent ones based on the Prior-data Fitted Networks paradigm outperform well-tuned GNNs in predictive performance, although at a higher inference cost.

---


### 78. [A specialized reasoning large language model for accelerating rare disease diagnosis: a randomized AI physician assistance trial](https://arxiv.org/abs/2606.24510)

**<font color=#1a73e8>作者：</font>** Haichao Chen, Songchi Zhou, Zhengyun Zhao 等 31 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rare diseases affect millions of individuals worldwide, yet timely diagnosis remains a major public health challenge due to scarcity of specialized clinical expertise. While large language models (LLMs) show promise to support rare disease diagnosis, current models are constrained by insufficient clinical deployability, limited clinically grounded evidence, and scarcity of training data. Here we present RaDaR (Rare Disease navigatoR), an open-source, compact reasoning LLM (32B parameters) for rare disease diagnosis. RaDaR was trained with 49,170 publicly available free-text cases and 104,666 synthetic cases with reasoning-enhanced training. RaDaR showed the strongest performance among evaluated open-source models, including the 671B DeepSeek-R1, across public benchmarks and four external validation centers. In a retrospective cohort, RaDaR prioritized the final diagnosis before documented clinical suspicion in 61.06 percent of cases, corresponding to a potential lead time of 1.87 months and 50.18 percent of the within-center interval. In a randomized physician-assistance trial, RaDaR assistance improved physicians' rare-disease diagnostic accuracy by 21.44 percentage points compared with internet search alone. Synthetic-data ablations suggested that phenotype-anchored narratives provide useful training signal for long-tail rare diseases, with a monotonic scaling trend within the tested data range. Together, RaDaR and its development and validation framework provide a deployable rare-disease reasoning model and a reproducible development framework for diagnostic AI under data scarcity.

---


### 79. [Reinforcement Learning for Computer-Use Agents with Autonomous Evaluation](https://arxiv.org/abs/2606.24515)

**<font color=#1a73e8>作者：</font>** Marta Sumyk, Oleksandr Kosovan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-Use Agents (CUAs) execute high-level user goals by perceiving and acting directly within graphical user interfaces. However, reinforcement learning for CUAs remains difficult because open-ended desktop environments rarely provide scalable, machine-readable reward signals: task success is often visually grounded and hard to specify with handcrafted reward functions or dense manual labels.
We propose an RL fine-tuning framework that uses autonomous vision-language evaluation as a scalable supervision signal for GUI agents. Given a final screenshot and the original instruction, a Vision-Language Model judges task completion and provides terminal feedback without task-specific heuristics or manual labels during policy optimization.
Because autonomous evaluators are imperfect, we model their feedback as a noisy binary reward channel and derive a noise-corrected reward estimator for Proximal Policy Optimization. Experiments across macOSWorld, Windows Agent Arena, and OSWorld show that corrected evaluator rewards outperform both zero-shot baselines and raw evaluator rewards, improving success rates by an average of 12.6 percentage points over zero-shot performance and 5.1 points over raw evaluator fine-tuning. These results suggest that autonomous evaluation can serve as a practical reward signal for RL in GUI environments when evaluator noise is explicitly modeled and corrected.

---


### 80. [Poster: Exploring the Limits of Audio-Based Detection of Turkish Phone Call Scams](https://arxiv.org/abs/2606.24523)

**<font color=#1a73e8>作者：</font>** Arda Eren, Micheal Cheung, Youqian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scam phone calls exploit vulnerable communities worldwide, yet research on detection has focused almost exclusively on English and other high-resource languages. In low-resource settings such as Turkish, detection is especially difficult, as annotated data is scarce and technological defenses remain limited. This research investigates how large language models (LLMs) can support scam detection in Turkish by introducing the first public multi-modal dataset of 100 aligned audio-transcript pairs of scam and benign conversations. We evaluate seven LLMs spanning three model families: Gemini 2.5 (Flash, Flash-Lite, Pro), GPT-4o, and Qwen (Max, Plus, Turbo), under three input conditions: raw audio, automatic speech-to-text transcripts, and transcripts refined by a native speaker. Our results suggest that transcript-based inputs consistently outperform direct audio processing, while human-corrected and uncorrected transcripts perform comparably. By centering a low-resource language and real world threat, this work highlights the urgent need for culturally and linguistically inclusive AI safety research and more robust multi-modal systems for fraud prevention.

---


### 81. [AGORA: An Archive-Grounded Benchmark for Agentic Workplace Document Reasoning](https://arxiv.org/abs/2606.24526)

**<font color=#1a73e8>作者：</font>** Honglin Guo, Qi Zhang, Yu Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as agents that reason over documents rather than answer from parametric knowledge. We study archive-grounded reasoning: locating sparse evidence across a large, messy collection of workplace files, reconciling inconsistent terminology, units, and time conventions, and computing an answer. Existing benchmarks address only parts of this setting and none jointly stresses archive-groundedness, agentic exploration, and cross-domain coverage. We introduce Agora, a benchmark pairing 362 questions with eight domain collections of 9,664 authentic documents and 372M tokens, far exceeding any model's context window, so agents must explore deliberately rather than scan exhaustively. Agora is built by an agentic pipeline combining cross-document task synthesis, leakage-preventing obfuscation, and difficulty filtering. Evaluating eight models, we find the task far from solved: even the strongest reaches only 59.4% accuracy, with notable variation across domains.

---


### 82. [Governed Shared Memory for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.24535)

**<font color=#1a73e8>作者：</font>** Yanki Margalit, Nurit Cohen-Inger, Erni Avram 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM environments require robust mechanisms for shared knowledge management. This paper formalizes the fleet-memory problem and identifies four foundational failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse. To address these, we define explicit systems-level primitives: scoped retrieval, temporal supersession, provenance tracking, and policy-governed memory propagation. These primitives are implemented in MemClaw, a production multi-tenant memory service, and evaluated via ArgusFleet, a reproducible harness testing four governance dimensions. Rather than a baseline comparison, this study measures a live production service, emphasizing real-world architectural insights and negative results. Key Evaluation Results Provenance: Successfully reconstructed 100% of depth-four derivation chains with correct writer identity at sub-second per-hop latency. Propagation: Demonstrated high intra-fleet visibility with zero cross-fleet leakage. Under strong write mode, write-to-visible latency was optimized to a single search round-trip. Production Architectural Issues Discovered Asymmetric Scope Enforcement: Tenant isolation held, but sub-tenant scope was initially bypassed on direct GET-by-id requests for agent-scoped credentials (disclosed and remediated during the study). Pipeline Ordering Conflict: While contradiction supersession works for admitted writes, a synchronous near-duplicate gate can prematurely reject contradictory writes before the asynchronous contradiction detector can evaluate them. Conclusion: Long-context retrieval alone is insufficient for production multi-agent memory. Governed shared memory demands explicit systems-level abstractions, and live evaluation is vital to expose enforcement and pipeline-ordering failures missed by design-only treatments.

---


### 83. [ForensicsTok: Forensics-Guided Tokenized Modeling for Image Tampering Localization](https://arxiv.org/abs/2606.24538)

**<font color=#1a73e8>作者：</font>** Lei Xu, Haowei Wang, Shen Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-modal Large Language Models (MLLMs) offer powerful reasoning for forensic tasks, yet existing approaches utilizing exogenous segmentation decoders often suffer from suboptimal localization. The reliance on stitched pipelines introduces information bottlenecks during backpropagation, which dilutes spatial signals and is limited by semantic priors of the segmentor. To address these limitations, we propose ForensicsTok, which reformulates image manipulation localization as an autoregressive sequence generation task. ForensicsTok directly generates spatially grounded token sequences, enabling precise mask prediction without intermediary supervision. Specifically, we introduce a Token Splatting Decoder (TSD) to map tokens to binary masks via codebook-aware code smoothing, which mitigates sharp gradients from deterministic detokenizers. Furthermore, to capture diverse tampering clues, we propose a Hierarchical Expert Fusion (HEF) module that injects multi-scale features from a forensic expert model. This unified architecture effectively compensates for the lack of forensic priors in standard MLLMs. Extensive experiments on six benchmarks show that ForensicsTok substantially improves over existing MLLM-based baselines and slightly improves over strong forensic expert baselines, while exhibiting stronger robustness to perturbations.

---


### 84. [PointVG-R: Internalizing Geometric Reasoning in MLLMs for Precise Pointing Localization via Visual Chain of Thought](https://arxiv.org/abs/2606.24539)

**<font color=#1a73e8>作者：</font>** Ling Li, Bowen Liu, Zinuo Zhan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pointing-based visual grounding requires models to precisely locate target objects by deciphering complex spatial relationships between the visual scene and pointing gestures. Traditional methods typically encode input images into static feature representations and perform reasoning primarily within the linguistic domain, often overlooking the rich perceptual cues and explicit spatial geometry inherent in images. In this study, we aim to mitigate the cognitive vulnerability of models in interpreting gestural spatial relations by proposing PointVG-R, a reasoning-guided Multi-modal Large Language Model (MLLM). PointVG-R introduces geometric-aware reasoning for pointing-based grounding, enabling the model to think with images through the strategic integration of Reinforcement Learning (RL) and cold-start data. Specifically, we design a novel geometric reasoning pipeline that simulates the iterative cognitive process humans employ when interpreting pointing gestures. Furthermore, we construct EgoPoint-CoT, a high-quality visual Chain-of-Thought (CoT) dataset featuring detailed reasoning trajectories to guide the model via Supervised Fine-Tuning (SFT) and RL. To address the varying quality of learning signals encountered during training, we further propose an Adaptive Importance Weighting strategy based on Group Variance, which dynamically adjusts reward signals to optimize the learning process. Experimental results demonstrate that PointVG-R achieves SOTA performance, outperforming the baseline by $\textbf{15.86}$ points in mIoU. Extensive ablation studies further validate the efficacy of our proposed modules. Code: this https URL.

---


### 85. [Jolia: Concept-Level Vision-Language Alignment for 3D CT Contrastive Learning](https://arxiv.org/abs/2606.24570)

**<font color=#1a73e8>作者：</font>** Julien Khlaut, Charles Corbière, Baptiste Callard 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language contrastive pretraining has become the dominant recipe for 3D medical foundation models, leveraging the large volumes of paired scans and reports produced in clinical practice. However, medical images usually span dozens of organs, and radiological reports are much longer than typical natural image captions and are composed of multiple structured sections. CLIP-style pretraining compresses this structure by encoding each modality into a single global token, at the risk of losing important details. We introduce ConQuer (Concept Queries), an image-text pretraining method that augments CLIP's global alignment with a set of localized alignments, one per concept. ConQuer splits the report into concept-specific sections and learns cross-attention queries that pool the matching image features without using any segmentation mask or spatial supervision. Contrastive learning is then applied independently for each concept. Concepts can be any unit of semantic localization; here, they are anatomical regions, one query per organ or gross body region. As a byproduct, each query learns attention maps focused on its concept, providing built-in spatial interpretability. We use ConQuer to train Jolia, a 3D CT foundation model on chest and abdominal CT. Jolia consistently outperforms a CLIP baseline on findings classification, report generation, and cross-center transfer, and sets a new state of the art across multiple public benchmarks. Jolia's weights will be released upon acceptance.

---


### 86. [LLMs Prompted for Legal Context Object More: Overrefusal from Small On-Premises LLMs in Criminal Legal Context](https://arxiv.org/abs/2606.24585)

**<font color=#1a73e8>作者：</font>** Anastasiia Kucherenko, François Brouchoud, Dimitri Percia David 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While the validity of LLMs' use in the legal context remains subject to ethical and legal debate, legal professionals are already experimenting with personal LLMs, if only for translation and reformulation. However, even such a seemingly innocuous use can introduce biases through case processing speed if LLM assistants selectively refuse assistance on certain topics. To better anticipate such biases, we investigate several modern small LLMs that are most likely to be used as on-device assistants, to assess the impact of overrefusal on legal prompts.
Surprisingly, we find that authority-style prefixes (``you are acting as an assistant of the national supreme court'', ``[...] defense lawyer'') systematically increase refusal rates by 2--20x over the no-prefix baseline, while a known role-play jailbreak prefix shows mixed effects, sharply increasing refusals in some models and barely shifting them in others. The finding suggests that small on-prem deployable LLMs are unstable under contextual framings that a real institutional user might naturally introduce, and further investigation is essential to minimize opportunities for bias.

---


### 87. [AdversaBench: Automated LLM Red-Teaming with Multi-Judge Confirmation and Cross-Model Transferability](https://arxiv.org/abs/2606.24589)

**<font color=#1a73e8>作者：</font>** Khanak Khandelwal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling adversarial evaluation of large language models requires both a method for generating hard inputs and a reliable way to confirm that resulting failures are real. We present AdversaBench, an end-to-end red-teaming pipeline that mutates seed prompts with five structured operators, queries a target model, and confirms failures through a three-judge panel with a meta-judge tiebreaker. We report experiments on 45 seeds across three categories: reasoning, instruction-following, and tool use. Every seed produced a confirmed failure. Four findings stand out. First, operator effectiveness varies sharply by category: inject_distractor scores 0.00 mean reward on instruction-following seeds but 0.80-0.83 on reasoning and tool-use. Second, binary failure rate hides difficulty: instruction-following seeds required 2.4 attacker iterations on average versus 1.1 for other categories, a gap visible in survival curves. Third, pairwise judge agreement of 80-87% coexists with near-zero Cohen's kappa due to label skew; category-level disagreement rates are more informative. Fourth, adversarial prompts generated against Llama 3.1 8B transfer zero-shot to Llama 3.3 70B, suggesting the mutations exploit general behavioral patterns rather than model-specific weaknesses. Code, dataset, and analysis scripts are available at this https URL .

---


### 88. [Qwen-AgentWorld: Language World Models for General Agents](https://arxiv.org/abs/2606.24597)

**<font color=#1a73e8>作者：</font>** Yuxin Zuo, Zikai Xiao, Li Sheng 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A world model predicts environment dynamics based on current observations and actions, serving as a core cognitive mechanism for reasoning and planning. In this work, we investigate how world modeling based on language models can further push the boundaries of general agents. (i) We first focus on building foundation models for agentic environment simulation. We introduce Qwen-AgentWorld-35B-A3B and Qwen-AgentWorld-397B-A17B, the first language world models capable of simulating agentic environments covering 7 domains via long chain-of-thought reasoning. Leveraging more than 10M environment interaction trajectories of 7 domains in real-world environments, we develop Qwen-AgentWorld through a three-stage training pipeline: CPT injects general-purpose world modeling capabilities from the state transition dynamics and augmented professional corpora, SFT activates next-state-prediction reasoning, and RL sharpens simulation fidelity through a tailored framework with hybrid rubric-and-rule rewards. To evaluate language world models, we present AgentWorldBench, a comprehensive benchmark constructed from real-world interactions of 5 frontier models on 9 established benchmarks. Empirical results demonstrate that Qwen-AgentWorld significantly outperforms existing frontier models. (ii) Beyond foundation models, we further investigate two complementary paradigms through which world modeling enhances general agents. First, as a decoupled environment simulator, Qwen-AgentWorld supports scalable and controllable simulation of thousands of real-world environments for agentic RL, yielding gains that surpass real-environment training alone. Second, as a unified agent foundation model, world-model training acts as a highly effective warm-up that improves downstream performance across 7 agentic benchmarks. Code: this https URL

---


### 89. [ASALT: Adaptive State Alignment for Lateral Transfer in Multi-agent Reinforcement Learning](https://arxiv.org/abs/2606.24601)

**<font color=#1a73e8>作者：</font>** Anurag Akula, Satheesh K. Perepu, Abhishek Sarkar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent reinforcement learning (MARL) addresses the problem of training multiple agents that pursue collaborative, competitive, or mixed objectives. Prior work has investigated transfer learning between source and target domains in MARL; however, the majority of existing approaches impose the constraint that the dimensionalities of the observation space and the global state space must be identical across domains. In this paper, we introduce a method that explicitly accommodates mismatched state-space dimensionalities between source and target domains. The proposed approach, ASALT, incorporates both observation-level and state-level adapters that map the target-domain observations and global states into a shared embedding space, thereby enabling more effective transfer of knowledge across both actors and critics. These adapters can generate embeddings that support efficient strategy transfer across heterogeneous domains. Experimental results on multiple configurations in standard benchmark environments demonstrate that ASALT surpasses existing baselines in terms of sample efficiency and global return in cooperative settings, but its effectiveness depends on the degree of mismatch between source and target domains. Furthermore, our findings indicate that ASALT mitigates negative transfer, which frequently constitutes a major obstacle when transferring policies between domains with differing observation and action spaces.

---


### 90. [ViTexQA: A Multi-Frame Temporal Perception Dataset for Video Text Question Answering](https://arxiv.org/abs/2606.24602)

**<font color=#1a73e8>作者：</font>** Zhentao Guo, Chen Duan, Tongkun Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite remarkable progress in multimodal understanding, current MLLMs still exhibit limitations in video text understanding, particularly when semantics emerge through the integration of temporally distributed textual cues across multiple frames. This perception challenge fundamentally differs from static image text understanding, yet existing datasets fail to capture: the vast majority of questions remain answerable from single frames, inadequately reflecting real-world video text comprehension demands. To address this, we present ViTexQA, a large-scale video-text QA dataset, and FrameThinker for robust multi-frame temporal reasoning. We build ViTexQA via a quality-controlled Chain-of-Thought (CoT) annotation pipeline boosted with temporal constraints; all its QA pairs demand cross-frame text fusion to solve, enforcing true temporal reliance. FrameThinker adopts two-stage training for explicit temporal modeling: CoT-Guided Supervised Fine-Tuning (SFT) generates frame-aware reasoning chains, followed by Temporally-grounded Reinforcement Learning (RL) optimized with multi-frame coherence rewards. Evaluations show our method outperforms SOTA baselines on ViTexQA, lifting ROUGE-L by 6.3%.

---


### 91. [ScaleToT: Generalizing Structured LLM Reasoning for Billion-Scale Low-Activity User Modeling](https://arxiv.org/abs/2606.24605)

**<font color=#1a73e8>作者：</font>** Tianbao Ma, Chang Xi, Yichuan Zou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate user modeling often depends on rich interaction histories, which are unavailable for billions of low-activity users. Large Language Models (LLMs) can infer latent user states from static profiles, but this reasoning becomes unreliable when profiles are sparse, and applying an LLM to billions of users is prohibitively expensive. We present ScaleToT, which learns structured reasoning from a small LLM-processed subset and extends it to the broader low-activity user population. To improve reasoning reliability, ScaleToT constructs typed user-state chains with a bounded entropy-guided Tree-of-Thought (ToT) refinement procedure. To make this structured reasoning usable from sparse profiles, the teacher-curated chains are used to train a student model on static profiles through supervised fine-tuning (SFT) and Outcome-Driven Segment-Aware Implicit Reward Policy Optimization (OSIPO). ScaleToT then transfers the student's reasoning representations to a lightweight profile encoder, providing shared reasoning signals for the remaining users without LLM inference. We evaluate ScaleToT on lifetime value (LTV) prediction in a billion-scale advertising deployment. A randomized online A/B test increased LT30 by 6.738\%, while offline reasoning covered only 7.32\% of the potential population, greatly reducing compute cost compared with full-population reasoning.

---


### 92. [Same Lesson, Different Story: Cross-Lingual Reconstruction of Cultural Narratives in Large Language Models](https://arxiv.org/abs/2606.24610)

**<font color=#1a73e8>作者：</font>** Jory Alshaalan, Haya Albaker, Abeer Aldayel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The evaluation of cultural grounding context becomes complex when multiple cultures convey the same moral lesson. This challenge is particularly relevant to large language models (LLMs), which produce narratives across a wide range of languages and cultural contexts. However, it remains uncertain whether these models preserve culturally grounded meaning when equivalent moral lessons are conveyed through distinct cultural forms. This study introduces a multilingual evaluation narrative framework that integrates a cross-linguistic collection of 414 proverbs spanning 15 languages and uses four LLMs to generate 13k narratives. By employing semantically equivalent proverbs as culturally grounded prompts, the analysis assesses whether models preserve meaning across languages, how cross-lingual conditioning influences narrative realization, and whether different model families converge on similar interpretations. Results indicate that cross-lingual prompting largely preserves proverb-level semantic meaning while systematically redistributing agency, social positioning, and narrative structure. Additionally, strong inter-model convergence is observed in both monolingual and cross-lingual settings, suggesting that multilingual LLMs rely on shared semantic abstractions despite architectural and linguistic differences. These findings shed light on the need for more comprehensive evaluations of cultural grounding. Relying exclusively on semantic similarity in multilingual narrative assessments may overestimate cultural preservation by neglecting culturally meaningful variations in narrative expression.

---


### 93. [AI Tokenomics: The Economics of Tokens, Computation, and Pricing in Foundation Models](https://arxiv.org/abs/2606.24616)

**<font color=#1a73e8>作者：</font>** Quanyan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tokens have become the practical accounting unit for modern foundation model services, linking information processing, computation, memory use, energy expenditure, pricing, and economic value. This paper develops a framework for AI tokenomics: the study of how tokens are generated, consumed, priced, allocated, and optimized across AI systems. We connect token-level technical costs to workflow-level production functions, enterprise resource allocation, measurement and instrumentation methods, and emerging market-design questions. The framework shows that token expenditure and economic value are distinct: value depends on marginal productivity, workflow position, hidden reasoning activity, risk, and downstream propagation effects. The paper concludes by identifying open research directions in hidden-token measurement, empirical calibration, token productivity, dynamic allocation, and token-based markets.

---


### 94. [Privacy-Preserving RAG via Multi-Agent Semantic Rewriting: Achieving Confidentiality Without Compromising Contextual Fidelity](https://arxiv.org/abs/2606.24623)

**<font color=#1a73e8>作者：</font>** Yuanhe Zhao, Tianyu Zhang, Huafei Xing 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation enhances large language models by incorporating external knowledge, but deploying it in sensitive scenarios risks privacy leakage via malicious prompts. To address this, we propose a multi-agent framework that sanitizes retrieved content through semantic rewriting. By employing three specialized agents for privacy extraction, semantic analysis, and reconstruction, our approach collaboratively removes sensitive identifiers while preserving the semantic core. We evaluate the framework on the ChatDoctor and Wiki-PII datasets across six large language models. Experimental results demonstrate a significant reduction in privacy leakage under targeted attacks. For instance, we reduced targeted information exposure in LLaMA-3-8B from 144 instances in the baseline to just 1. Furthermore, we maintain strong contextual fidelity with a BLEU-1 score of 0.122, outperforming the existing SAGE method's 0.117. Finally, the framework operates as an asynchronous preprocessing module, introducing no additional latency to online inference, as all rewriting is executed as a one-time offline preprocessing step. To promote reproducibility, the source code of this work is publicly available at this https URL.

---


### 95. [SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation](https://arxiv.org/abs/2606.24626)

**<font color=#1a73e8>作者：</font>** Chenyang Zhu, Jiayu Yao, Kushal Chawla 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As autonomous agents tackle increasingly complex multi-step, multi-agent tasks, their execution trajectories have scaled beyond the constraints of even the largest context windows. Current methods for effectively diagnosing agent failures load the full trajectory into an LLM's context window, which suffers from attention dilution and fails when agentic traces inevitably exceed context limits. To address this, we introduce SAFARI (Scaling long-horizon Agentic Fault AttRibution via active Investigation), a framework that replaces linear context loading with a tool-augmented diagnostic loop. By equipping LLMs with a specialized toolbox to read and search trajectory segments alongside a persistent Short-Term Memory (STM) for cross-turn reasoning, SAFARI effectively decouples diagnostic accuracy from architectural context limits. Our experiments demonstrate that SAFARI outperforms state-of-the-art results by 20% on the Who&When dataset within a 1M token budget, and by 19% on TRAIL GAIA subset on a 25K token budget. Most significantly, SAFARI maintains a 0.58 precision even when the target fault resides 5x beyond the model's native context window, a scenario where traditional evaluators fail entirely.

---


### 96. [CineCap: Structured Reasoning with Spatio-Temporal Anchors for Cinematographic Video Captioning](https://arxiv.org/abs/2606.24636)

**<font color=#1a73e8>作者：</font>** Xinyu Mao, Yuhui Zeng, Xiaokun Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cinematographic captioning aims to describe how a video is filmed using professional film-language concepts such as camera movement, shot size, depth of field, composition, and shooting angle. This capability is important for fine-grained video understanding and controllable movie-quality video generation, yet remains underexplored in existing multimodal large language models. Unlike question-answering-based evaluation of cinematic understanding, cinematographic captioning requires a unified open-form description over multiple cinematographic dimensions. This task is challenging for two main reasons: the model must infer professional cinematographic concepts from subtle visual evidence, and it must generate captions that are both comprehensive and accurate. Accordingly, we propose CineCap, a framework that combines structured reasoning with spatio-temporal anchors and reinforcement learning with comprehensiveness, accuracy, and gated coverage rewards. The former grounds professional cinematographic descriptions in explicit visual evidence and organizes them into compact atomic reasoning for supervised fine-tuning, while the latter improves the balance between descriptive completeness and factual correctness. In addition, we construct CineCap Bench, a benchmark of 472 manually annotated video-caption pairs for systematic evaluation. Extensive experiments show that CineCap consistently outperforms strong proprietary and open-source baselines, establishing a new state of the art for cinematographic captioning. The code, model checkpoint, and benchmark are publicly available in this https URL.

---


### 97. [Agentic Collaborative Cognition for Zero-Shot 3D Understanding](https://arxiv.org/abs/2606.24649)

**<font color=#1a73e8>作者：</font>** Wenxin Wang, Bo Zhang, Feng Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements have explored agentic zero-shot 3D understanding by reformulating it as video keyframe understanding with Multimodal Large Language Models (MLLMs). However, existing methods face an intrinsic bottleneck due to the finite observation perspectives inherent in videos and the implicit perception of 3D scenes. In this paper, we propose a collaborative multi-agent framework that assigns a Planning Agent to handle high-level viewpoint planning and supplement novel perspectives, and a Perception Agent to explicitly summarize the 3D scene into a structured holistic cognitive map. Specifically, Planning Agent first analyzes this cognitive map to determine query-relevant viewpoints and supplements missing critical perspectives to ensure comprehensive observation. Subsequently, Perception Agent documents object-level attributes from these views by assigning consistent instance identifiers across viewpoints, thereby integrating fragmented observations into the holistic cognitive map. In parallel, it provides feedback to filter out mismatched candidate objects and guide subsequent viewpoint planning. Through this closed-loop iterative process, two agents collaboratively figure out candidates until Perception Agent determines that sufficient information has been captured to complete the task. Extensive experiments demonstrate that our method achieves state-of-the-art performance on 6 benchmarks, with improvements of 11.1\% Acc@0.5 on ScanRefer, 14.6 BLEU-1 on 3D-assisted dialog, and 2.1 EM on SQA3D.

---


### 98. [Harmonic: Hierarchical State Space Models for Efficient Long-Context Language Modeling](https://arxiv.org/abs/2606.24650)

**<font color=#1a73e8>作者：</font>** Petr Nyoma  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Harmonic, a hierarchical state space model (SSM) for language modeling. The architecture stacks three recurrent levels at progressively slower timescales; each level receives the prediction error of the level below as input, rather than its raw hidden state. On enwiki8 with equal token budgets, Harmonic outperforms a comparable Transformer (28M params) by +1.4% at 1K tokens, +6.7% at 8K tokens, and +11.4% at 32K tokens (bpt, lower is better). It also outperforms Mamba at every tested length by 0.7--1.8%. At 64K tokens, both Mamba and Transformer run out of memory on an 80GB H100; Harmonic trains successfully, reaching 6.169 bpt. Results replicate on WikiText-103 (H-TF gap +1.7% to +7.2% across 1K--32K). At 1B parameter scale, replacing all attention layers in TinyLlama 1.1B with HarmonicBlock eliminates the RoPE positional encoding limit: the resulting Hallamonic model maintains stable loss across sequence lengths 1K--8K on two independent clean benchmarks (Lambada and fineweb-edu held-out), while TinyLlama degrades catastrophically past its 2K-token RoPE limit (gap: +9.4 bpt at seq=8K on Lambada). Compute is O(L) per forward pass vs. O(L^2) for attention.
Logs: this https URL.

---


### 99. [AI-PAVE-Br: Leveraging Large Language Models for Enhanced Product Attribute Value Extraction through a Golden Set Approach](https://arxiv.org/abs/2606.24655)

**<font color=#1a73e8>作者：</font>** Murilo Gazzola, Hugo Gobato Souto, Samuel Silva 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The explosive growth and complexity of product data within the dynamic Brazilian e-commerce landscape demand robust and specialized methods for structured information extraction. Traditional approaches to Product Attribute Value Extraction (PAVE) often struggle with the linguistic nuances and sheer diversity of product descriptions in Portuguese. To address this critical gap, this paper introduces two major contributions. First, we present AI-PAVEBr, a specialized system engineered with Large Language Models (LLMs) to perform high-accuracy PAVE specifically for Brazilian e-commerce catalogs. Second, to facilitate reproducible research and provide a definitive benchmark, we introduce and share the Golden Set, a new, meticulously curated, and manually annotated dataset for PAVE in Portuguese. We detail the creation process and structure (Entity, Category, Subcategories) of this high-quality reference set. Our experiments conclusively show that AI-PAVE-Br, leveraging targeted prompt engineering, dramatically outperforms conventional Named Entity Recognition (NER) baselines. This work not only delivers a superior, scalable solution for a major non-English market but also enriches the NLP community with a valuable, publicly available resource for future PAVE research.

---


### 100. [LaGO: Latent Action Guidance for Online Reinforcement Learning](https://arxiv.org/abs/2606.24669)

**<font color=#1a73e8>作者：</font>** Kuan-Yen Liu, Ren-Jyun Huang, Ti-Rong Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong potential for planning and sequential decision-making, but prior work often relies on using them as direct controllers, which requires precise action generation and can be unreliable in practice. This paper proposes Latent Action Guidance for Online Reinforcement Learning (LaGO), a framework that uses a pretrained LLM as a latent action prior to softly guide online policy optimization, rather than treating the LLM as an explicit planner or controller. Experiments on both a discrete-control benchmark, CLEVR-Robot, and a continuous-control benchmark, Meta-World, demonstrate that LaGO consistently improves both reward and success rate over Vanilla PPO. In particular, LaGO increases the average success rate from 15.1% to 27.2% on CLEVR-Robot and from 2.7% to 15.2% on Meta-World. Our analysis further shows that stronger pretrained LLMs provide more effective guidance, suggesting that LLM knowledge can improve planning and online decision-making.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-118](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
