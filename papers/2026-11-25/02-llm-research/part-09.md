# 🧠 大模型相关研究 | 2026年11月25日

> 本类共 **486** 篇论文：已确认 **458** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-486](./part-10.md)

---

### 401. [GameDojo: Benchmarking Real-Time Interactive Agents in Video Games](https://arxiv.org/abs/2611.30771)

**<font color=#1a73e8>作者：</font>** Kuan Zhang, Zhihao Yang, Yukun Chen 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive intelligence requires agents to act on observations and adapt to the consequences of actions. Studying these abilities calls for diverse, challenging tasks under controlled conditions. We introduce GameDojo, a controllable interactive gameplay benchmark of 120 boss encounters across 20 games for evaluating model capabilities, learning algorithms, and agent harnesses. Coding agents reconstruct the environments and write gameplay scripts, producing GameDojo-Data with 600 hours of gameplay trajectories. Experiments reveal substantial challenges for frontier models, especially in real-time interaction. Training on GameDojo-Data brings GameDojo-4B to frontier performance, with the strongest real-time performance. We also find joint training improves individual tasks, and learned policies transfer across bosses. Together, these findings establish GameDojo as a challenging and valuable interactive gameplay benchmark for the community. Our project page is at this https URL , and our code is at this https URL .

---


### 402. [Trallie: from Free-Form Text to Structured Data with LLMs](https://arxiv.org/abs/2611.30773)

**<font color=#1a73e8>作者：</font>** Vijayasri Iyer, Cristiano De Nobili, Mubashir Hussain Shah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Trallie is an open-source framework that leverages large language models (LLMs) to perform information extraction (IE) from natural language sources with or without user guidance. Unlike conventional approaches that rely on extensive labeled datasets or domain-specific training, Trallie enables the conversion of unstructured data into structured formats with minimal or no representative examples. The framework is designed with three key objectives: (i) reducing manual annotation by harnessing prompt-based zero-shot and few-shot capabilities of modern LLMs, (ii) flexibly parsing diverse document formats (i.e., HTML, PDF, TXT, and JSON), and (iii) improving accessibility for non-expert users by automatically inducing schemas from document collections, which can then be refined for extraction. We evaluate Trallie with open-weight LLMs on FDA 510(k) documents and on movie and university websites from SWDE. It outperforms previously reported systems when the target attributes are provided for text extraction and is competitive when it must discover attributes for the schema automatically. The project is available at this https URL

---


### 403. [Doc-to-LoRA Analysis: Query Conditioning, Wrong Facts, and Distractor Interference](https://arxiv.org/abs/2611.30825)

**<font color=#1a73e8>作者：</font>** Jesper Derehag  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Doc-to-LoRA (D2L) compiles documents into low-rank adapters, allowing language models to use their contents without repeatedly processing the original text. We investigate its suitability for internalizing user memories through factual question answering, controlled interventions, and a production MidBrain memory pipeline. Across Gemma-2-2B and Qwen3-4B, D2L loses accuracy relative to in-context learning, with additional documents introducing substantial interference. Single-document errors frequently match answers to other questions about the same passage, suggesting unreliable question-answer attribution. Layer-wise interventions show that interference accumulates across depth, with more concentrated early damage at larger bank sizes on Gemma. With eight documents, applying the full bank in the initial layers gives similar accuracy to withholding all document contributions there. Source membership is detectable in intermediate states, but trained readers do not reliably resolve the interference. On PersonaMem-v2, joint compilation and normalized adapter composition achieve accuracy close to consolidated text memory when retrieved episodes remain text, but the resulting token savings are modest. Measured throughput gains also depend on model and batch size despite substantial reductions in analytical compute. Together, these findings limit the practical case for D2L as a replacement for text-based memory and motivate investigating online-learning methods that acquire personalized behavior from interactions in which memory is used.

---


### 404. [The KL Divergence Is Never Negative, Except in PyTorch](https://arxiv.org/abs/2611.30835)

**<font color=#1a73e8>作者：</font>** Zhen Yang, Wei Tang, Chu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A Kullback--Leibler (KL) divergence is never negative, yet PyTorch users have reported negative values for years, and the standard advice is to clamp them at zero. The sign is only the visible part of a silent failure. Many machine-learning applications compare nearby distributions, where conventional KL formulas lose accuracy. On 8.5 million inputs with certified references across 18 closed-form KL families and F.kl_div, we find widespread errors in values and gradients on CPU and GPU. Among scalar families in ordinary parameter ranges, over 85% of FP32 values have at least 1% relative error near KL 10^(-7) (FP16: 10^(-3)), and about 30% become negative at smaller divergences. More precision is not the cure: evaluated one precision higher, the same formulas still leave 7--51% of FP32 values significantly wrong for 22 of 23 configurations. Stable closed-form decompositions, compensated arithmetic, and analytic gradients remove over 97% of significant errors in the working format. Strict repairs eliminate significant errors on 7.2 million scored closed-form samples and correctly round all 567 million scored F.kl_div components. The errors affect parameter fitting, Bayesian decisions, identical-start distillation (up to 97% top-1 disagreement), KL-based layer rankings in a quantized LLM, and 19--59% of GPT-2 circuit edge scores. With the repaired code they all but vanish. Code and data: this https URL

---


### 405. [SARA: An Auditor-in-the-Loop LLM Recommender for Sustainability Reports](https://arxiv.org/abs/2611.30839)

**<font color=#1a73e8>作者：</font>** Lars Hillebrand, Thiago B. F. de Oliveira, Tim Dilmaghani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Auditing corporate sustainability reports requires assurance professionals to map a company-specific checklist drawn from roughly 1,700 regulatory requirements onto the relevant passages of lengthy, repeatedly revised draft reports and to judge compliance. We present SARA (Sustainability Reporting Assistant), a human-in-the-loop recommender system delivered as a Microsoft Word add-in that recommends, for each requirement, the passages addressing it and predicts a compliance verdict while keeping the auditor in full control. SARA casts auditing as content-based recommendation over a fixed regulatory taxonomy and makes per-requirement large language model (LLM) matching cheaper, faster, and more accurate through topic-prediction filtering: on expert-annotated reports, it reduces matching cost about sixfold and runtime by 42% versus feeding the full report to the LLM. It is in production use across PwC Germany's sustainability-assurance practice.

---


### 406. [DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers](https://arxiv.org/abs/2611.30844)

**<font color=#1a73e8>作者：</font>** Lernie Li, Yuanliu Liu, Pengfei Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) scale model capacity by increasing both parameter count and computation. Mixture-of-Experts (MoE) variants expand parameter capacity while keeping per-token computation roughly fixed, but still require substantial parameter storage. In this paper, we propose Dynamic Looped MoE DiT (DyLoMo-DiT), which reuses parameters rather than adding them: a weight-shared loop repeatedly applies the middle layers, while sparse experts allocate parameter capacity across tokens. This design deepens the network without adding parameters, freeing the parameter budget for other uses, such as more experts or more distinct layers. It also allocates compute dynamically, varying the number of passes across noise levels. Experiments show that DyLoMo-DiT makes more effective use of parameter and compute budgets, with further gains from assigning more passes to low-noise steps. On ImageNet $256\times256$, DyLoMo-DiT reduces FID by 11-24% relative to DiT and 36-56% relative to DiT-MoE at matched parameter and compute budgets. For text-to-image generation, a scaled DyLoMo-DiT achieves a higher GenEval score than FLUX.1 (0.714 vs. 0.673), with less than one tenth of its active parameters (1.05B vs. 12B).

---


### 407. [How Do Deep Networks Encode and Selectively Use Information? Shared Encoding and Conditional Signed Readout in Vision and Language Models](https://arxiv.org/abs/2611.30854)

**<font color=#1a73e8>作者：</font>** Kaixiang Shu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How can trained deep networks retain contextual information across internal representations while using it selectively in a decision? We study this question through controlled background-texture edits in vision classifiers and entity-binding edits in frozen language models. Across both modalities, factor perturbations preserve recognizable structure across pre-fixed, mutually disjoint blocks of hidden units: visual channel blocks match their complements more closely for the same image than for other images under the same texture edit, while language blocks transfer a relational direction fitted under one query role to rank relational states within held-out name pairs under the other role. We then decompose the local output change into signed channel and pathway contributions. In a convolutional classifier, net channel-level reinforcement ($R^{(512)}>1$) coexists on individual images with cancellation between positive- and negative-weight groups ($R^{(2)}<1$). Holding weights, the paired relation edit, and red/blue answer words fixed, switching prompt presentation reverses the mean finite selection effect in Qwen2.5. Two held-out tests validate this mechanism. Attenuating development-selected antagonistic units amplifies edit effects on unseen inputs; in a vision transformer, attenuating the same frozen units in one forward pass increases the mean magnitude of the background-edit effect on one class margin and reduces it on another, with the opposite pattern for a second group (four-cell paired interaction $+78.30\times 10^{-5}$ logit). Finally, combining conditional channel variance with fixed downstream readout weights predicts single-channel pruning recovery across ten cuts. These results show how shared encoding and conditional signed readout can coexist in vision and language models.

---


### 408. [Semantic-aware Decoding for Diverse Text-to-SQL under Schema Ambiguity](https://arxiv.org/abs/2611.30873)

**<font color=#1a73e8>作者：</font>** Yuxuan Jiang, Anna Mitsopoulou, Apostolos Koukouvinis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world text-to-SQL systems often face schema ambiguity, where a question can map to multiple plausible schema elements. To support downstream disambiguation, SQL generation systems should include diverse interpretations among their top-k predictions. However, large language models (LLMs) typically favor a single interpretation, producing highly skewed outputs. We propose Semantic-aware Logit Adjustment (SLA), a training-free decoding method that promotes diverse SQL generation by adjusting token logits based on semantic similarity between schema elements. Unlike prior approaches that rely on reasoning-intensive prompting or task-specific fine-tuning, SLA is efficient, model-agnostic, and easy to deploy. Experiments show that SLA consistently improves interpretation coverage over standard decoding and remains competitive with existing diversity-oriented methods at substantially lower inference cost.

---


### 409. [World Models as Native Latent Action Models](https://arxiv.org/abs/2611.30898)

**<font color=#1a73e8>作者：</font>** Qinyue Li, Weijie Qiao, Qingyi Tao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large and diverse video sources, such as egocentric human video and heterogeneous robot recordings, carry rich dynamics but come either without actions or without a shared action space. Latent action models (LAMs) can recover these dynamics, but they train their inverse- and forward-dynamics models (IDM, FDM) from scratch, trading off pixel reconstruction against latent capacity and accuracy. Pretrained video world models natively generate high-fidelity dynamics, yet represent them densely, entangled across all layers. Viewing the world model as a LAM, we show that these dynamics can be extracted with minimal changes to the model. Native LAM operates one pretrained video diffusion transformer as both IDM and FDM, with learnable dynamics registers as the only causal bridge between the two, and trains on counterfactual temporal pairs that differ in motion alone, so that the registers distill a video's dynamics into a compact native latent action. We further propose a pretraining paradigm for vision-language-action (VLA) policies, Pretraining Actions from World models (PAWlicy), in which Native LAM serves as a dynamics teacher on large-scale video; unlike world action models, it never generates video. Native latent actions outperform existing LAMs on the LARY benchmark in both action classification and control regression, and replay the same motion on new robots, in new scenes, and from human hands to robots, although no transfer objective is used in training. With a 3.8B model, PAWlicy reaches a 93.6% average success rate on RoboTwin 2.0 trained with domain-randomized demonstrations, the highest among VLAs. On RoboDojo, it is competitive on every dimension we evaluate, and its Precision, evaluated by us, is on par with the leading leaderboard entries. On real robots, it improves over the pi_0.5 baseline on both tasks. Both stages use only public data and a publicly released world model.

---


### 410. [GlanceNav: Efficient Vision-and-Language Navigation with Streaming Memory and Counterfactual Rewind](https://arxiv.org/abs/2611.30900)

**<font color=#1a73e8>作者：</font>** Anh Dao, Quan-Dung Pham, Danh Vinh Le 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) have become strong policies for vision-and-language navigation (VLN). However, most of them encode a sample of past frames again at every decision and are trained on isolated decisions, so computation is redundant and the usable history is short. They also learn from their own mistakes through outcome rewards that give one scalar to a whole episode. We ask whether a navigator can encode each frame only once, at a constant cost per step, and still remember what matters and learn efficiently from its mistakes. We present GlanceNav, a streaming navigator built on a hybrid MLLM. Its Gated DeltaNet layers carry a recurrent state through the whole episode, while its attention layers keep a short window of recent observations and a small bank of keyframes, selected by how much each frame changes the recurrent state. This constant-size memory keeps the cost per step fixed and allows training on whole episodes with the same memory as at inference. Because the entire memory can also be copied in constant time, we further propose Counterfactual Rewind (CoRe), a reinforcement learning stage that rewinds a drifting rollout to its closest approach to the goal, lets an expert correct a few actions, and credits decisions by the resulting change in outcome. Trained only on the R2R-CE and RxR-CE training splits, with 1,000 instructions for reinforcement learning, a 4B GlanceNav reaches success rates of 71.9% and 73.6% on R2R-CE and RxR-CE val-unseen. On R2R-CE, it outperforms the strongest previous single-RGB method trained without external data by 9.1 points, while running at 104 ms per step.

---


### 411. [Replay Before You Reply: Second-Look Prompting for Unified Multimodal Encoding](https://arxiv.org/abs/2611.30909)

**<font color=#1a73e8>作者：</font>** Yicheng Zhang, Xun Zhang, Jingyuan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Solving multimodal tasks requires Vision-Language Models (VLMs) to form a unified understanding of the image and the question text. However, under causal attention in current VLMs, a token can attend only to what precedes it. Whichever modality comes first is therefore encoded under partial observation of the input, uninformed by the rest of the multimodal context. We introduce Second-Look Prompting (SLP), a training-free method that repeats the image-question pair in the input. In the repeated copy, every visual and textual token can attend to the complete input, yielding a unified multimodal encoding of the pair. Moreover, the added visual tokens contribute computation beyond re-exposing the image: even a blank image in their place can improve reasoning. Across 12 benchmarks, SLP improves the overall average score of every evaluated model, spanning nine open-source models (3B-72B) and three proprietary frontier models, with gains reaching 5.6 points for Gemini 3 Flash on MATH-Vision. Our analysis reveals two complementary mechanisms: the question guides where the second image attends, and the added visual tokens act as a prefill scratchpad whose hidden states retain answer-relevant information from the image and question. These findings highlight input presentation as a simple yet effective way to improve VLM performance.

---


### 412. [Demystifying Detectors Guarding Agent Skill Hubs](https://arxiv.org/abs/2611.30913)

**<font color=#1a73e8>作者：</font>** Kang Yang, Kevin Ying, Xiaojing Liao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent Skills has gained widespread adoption as an open standard for extending agent capabilities. To facilitate skill sharing, public skill hubs have grown in popularity and increasingly rely on automated security detectors to identify malicious skills at scale. Yet, the effectiveness and limitations of these detectors remain insufficiently understood. To fill this gap, we present the first systematic study of four hub-adopted and two community-provided malicious skill detectors on 1477 agent skills from seven datasets. Our evaluation reveals that even the best-performing hub-adopted detector by overall F1, skill-scanner with Qwen3.6, still misses 4.9% of malicious skills and incorrectly flags 17.8% of benign skills.
To understand these failures, we manually analyze detectors' findings and decision-making processes, identifying two recurring failure mechanisms. False positives often arise when detectors flag sensitive operations, such as credential access, without considering whether they serve the skill's legitimate purpose. Conversely, false negatives occur when detectors recognize malicious instructions or behaviors but underestimate their severity or dismiss valid findings during review, ultimately leaving malicious skills unblocked. Guided by this analysis, we refine the prompts of a state-of-the-art detector, skill-vetter, improving its mean F1 score in eight of nine evaluation settings, with gains of up to 22.7 percentage points. These results highlight gaps in existing skill-vetting practices and underscore the need for more robust and context-aware detection mechanisms.

---


### 413. [PRIMEAPE: A Multilingual Benchmark for Fine-Grained Meta-Evaluation of Judge Models](https://arxiv.org/abs/2611.30925)

**<font color=#1a73e8>作者：</font>** Vladislav Mikhailov, Sarfraz Ahmad, Momina Ahsan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly serve as judges of other models, shaping benchmark rankings and model development. Yet, a judge whose rationale consistently supports its verdict may still disagree with human preferences. To study this, we introduce PRIMEAPE, a multilingual benchmark for evaluating judge verdicts and rationales. PRIMEAPE provides 2,205 response pairs covering 243 instructions in English, French, Spanish, Urdu, Hindi, Norwegian Bokmål, and Yoruba, with 11k human annotations of preferences and rationales across relevance, naturalness, truthfulness, safety, and overall quality. Our evaluation of twelve open- and closed-weight judges reveals that aggregate performance conceals differences across languages and criteria, while requesting rationales does not consistently improve agreement with human preferences. Judges also favor the first position, longer responses, and responses from related models, with effects that vary across criteria and languages. Crucially, judges can justify verdicts that disagree with human preferences while maintaining consistency between their verdicts and rationales. These findings show that consistency with a judge's own verdict does not establish alignment with human judgment. PRIMEAPE enables assessment of both, providing a foundation for more reliable multilingual judges. We release our benchmark and all annotation materials under the CC BY-NC 4.0 license at this http URL.

---


### 414. [Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills](https://arxiv.org/abs/2611.30932)

**<font color=#1a73e8>作者：</font>** Kaixuan Li, Wenbo Guo, Sen Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills are reusable packages that extend a large language model (LLM) agent with scripts, third-party dependencies, and natural-language instructions. An agent builds a skill's arguments from user requests and untrusted external content, so a flaw left by a benign author can escalate a prompt injection to code execution. Existing studies target malicious skills or a single attack vector, and none tests whether an agent can reach such flaws. We present the first registry-scale empirical study of the supply chain attack surface arising from unintentional vulnerabilities in agent skills, over all 48,682 skills in ClawHub. The study covers two carried-over risks, dependencies and first-party code, and two agent-native ones, install instructions and credentials printed to stdout. We screen all skills by static analysis, manually review all 3,428 cases flagged by the four main detectors, and test reachability by running sampled flagged skills in a sandbox and with a live LLM agent under indirect prompt injection. First, dependency risk carries over in a different form: 49.6% of the skills with resolvable dependencies depend on a version with a known CVE, and unlike npm packages, which mostly become vulnerable after release, 78.3% of them are born vulnerable, already exposed at publication. Second, few of these CVEs are reachable: agent input reaches the vulnerable function in only 3.0% of the affected skills, whereas 21 of 22 sampled first-party flaws are exploited end to end in the sandbox. Third, a live agent executes the injected payload in 48.5% of the sampled flagged skills, but almost always in its own shell before the skill runs, and the payload reaches a flaw in the skill itself in only 5.0%. Hence, registries should prioritize first-party flaws over dependency alerts, and agent runtimes should not pass skill arguments through a shell.

---


### 415. [Beyond Patching: Consistent Circuit Discovery via Gradient Spectral Analysis](https://arxiv.org/abs/2611.30939)

**<font color=#1a73e8>作者：</font>** Yujie Zhang, Tianyi Zhao, Guanghui Min 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability seeks to reverse-engineer neural networks by identifying small, faithful subgraphs--circuits--that implement specific behaviors. The dominant paradigm scores each unit by replacing its clean activation with a corrupted counterpart as causal intervention. While effective, this approach rests on a brittle prerequisite: the structure prompt pairs are task-specific, expensive to engineer, and silently couple the discovered circuit to prompt-design choices. In this work, we propose Spectral Circuit Analysis (SCA), a gradient-spectral pipeline that achieves consistent circuit discovery along both axes: stable across input formulations of the same task, and natively exposing structure shared across tasks. Our contributions are threefold. First, we provide a counterfactual-free reframing of circuit discovery: causally relevant directions are recoverable from the spectral structure of forward gradients across paraphrases, with leading directions concentrating task signal and trailing ones absorbing paraphrase noise, yielding circuits tied to the task rather than the prompt. Second, we introduce SCA, a block-wise SVD pipeline that extracts a task subspace per architectural block and redistributes spectral energy onto constituent units via a consistency-weighted share, producing per-unit rankings competitive with attribution-patching baselines under strictly less supervision. Finally, on twelve circuit-discovery tasks in GPT-2 Small and Pythia-160M, SCA performs comparably or exceeds EAP-family methods under the standard recovery-score protocol and recovers IOI canonical heads with Precision@K = 1.0 in top-10 slices on GPT-2 Small; the same machinery extends to a unified cross-task analysis classifying units as universal, family-shared, or task-specific and exposing compositional structure invisible to per-task analyses.

---


### 416. [Vetoes and missed agreements in language-model bargaining](https://arxiv.org/abs/2611.30950)

**<font color=#1a73e8>作者：</font>** Fuad Ali  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> A language model played three representatives, each instructed to get the best payoff for its own group. One representative requested a plan, another chose the sole offer, and all three voted. If anyone voted no, each group received its fallback payoff. In 60 games with Qwen3-Next-80B, the representative at risk of a loss always requested a plan that would leave everyone better off. In each game, two copies of the proposer saw the same payoffs, peer request and reminder that the offer needed three yes votes. Showing the proposer how many groups gained under each plan raised mutually beneficial agreements from 6/60 to 31/60 (paired increase 41.7 percentage points, conservative 95% interval 18.8 to 58.5). Two of the four plans benefited everyone, so picking uniformly would put a mutual gain on the ballot half the time on average. In an earlier study, GPT-4.1 played 12 conflict games under two message conditions. Majority rule passed 15 of 24 offers, all at one group's expense. Unanimity passed two, both mutual gains. In the Qwen games, voters never saw the counts. They approved all 37 offers that helped everyone. On all 83 offers that would have cost one group points, its representative voted no.

---


### 417. [Evaluable Language-Model Treatment Policies for Sepsis Resuscitation via Offline Value-Guided Selection](https://arxiv.org/abs/2611.30951)

**<font color=#1a73e8>作者：</font>** Yue Pei, Shining Bo, Yingying Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline treatment learning must balance imitation, which stays close to logged evidence but ignores outcomes, against value maximisation, which uses outcomes but drifts toward treatments the records cannot verify. Numerical reinforcement learning strikes this balance during training. For large language models (LLMs), directly using sparse retrospective outcomes for fine-tuning raises challenges of delayed credit assignment and limited evidence for alternative treatments. We present R-LLMC, which strikes the balance at inference for sepsis resuscitation. A behaviour-supervised LLM, decoded into an exact distribution over 25 vasopressor-fluid actions, proposes clinician-anchored candidates; an offline critic selects among them by estimated long-term value. The policy has a closed form for off-policy evaluation, and its rationale is written after selection, so explanation cannot steer treatment. In experiments on held-out MIMIC-III patients, R-LLMC exceeded the clinician reference in doubly robust value by +0.214 (95\% CI 0.091-0.300), with fitted Q evaluation agreeing.

---


### 418. [Self-Evolving Evaluation Environments for Computer-Use Agents](https://arxiv.org/abs/2611.30962)

**<font color=#1a73e8>作者：</font>** Wenhao Wang, Panrong Tong, Quyu Kong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents (CUAs) are rapidly improving, yet their evaluation remains largely static. Existing benchmarks provide a strong foundation, but fixed difficulty ceilings, limited feature coverage, and coarse aggregate scores progressively weaken their discriminative and diagnostic value. We introduce CUA-SEE, a closed-loop evaluation environment that co-evolves tasks and executable verifiers from rollout evidence. It disentangles three objectives: benchmark evolution expands evaluation scope through cohort-calibrated difficulty and coverage growth; diagnostic evolution increases resolution through agent-conditional capability-boundary probes; and verifier evolution improves precision by translating changing requirements into state-grounded checkpoints with adversarial validation. Across multiple agents, applications, and rounds, CUA-SEE generates challenging, measurable tasks while preserving process-level evidence. Our results position adaptive evaluation as a scalable counterpart to self-evolving agents, continuously tracking what agents can do, where their boundaries lie, and how reliably progress is measured.

---


### 419. [Beyond Self-Consistency: Recursive Self-Improvement at Test Time](https://arxiv.org/abs/2611.30965)

**<font color=#1a73e8>作者：</font>** Jianyu Wu, Yizhou Wang, Encheng Su 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) that continue improving after deployment (e.g., recursive self-improvement) offer a promising path toward general intelligence. Current test-time methods pursue this goal on unlabeled questions, primarily relying on self-consistency: they generate independent solutions and use majority voting to select an answer or construct training targets. This leaves earlier reasoning unused at inference and can reinforce an incorrect majority during training. Humans instead build on earlier attempts to preserve useful reasoning, correct mistakes and improve their problem-solving strategies. Following this principle, we propose Test-Time Recursive Self-Improvement (TT-RSI), a label-free framework for improving LLMs at test time through two mutually reinforcing components: (1) In-Context RSI repeatedly re-solves each question using the full previous solution as a reference, letting the model decide whether and how to use it so that inference compute builds on earlier reasoning. (2) In-Weight RSI distills successive refinements into the model's weights, enabling progress beyond an initially wrong majority and theoretically bringing the first attempt toward the model's infinite-step refinement limit. The updated model answers better and refines more effectively, generating stronger references for subsequent training. Extensive experiments show that TT-RSI improves average accuracy by +13.89% over the base model and outperforms the strongest self-consistency-based method by +4.79% under the same test-time scaling budget.

---


### 420. [MedUIGym: Evaluating and Training GUI Agents for Clinical Workflows](https://arxiv.org/abs/2611.30983)

**<font color=#1a73e8>作者：</font>** Yitong Qiao, Lei Liu, Yue Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automating clinical workflows requires vision-language agents that can navigate dense graphical user interfaces (GUIs) in electronic health records (EHRs) and execute precise actions, yet many medical agents still rely on text or structured tool calls. In this work, we introduce MedUIGym, a scalable interactive environment comprising 15,739 tasks from 17 benchmark sources across six clinical task families for training and evaluating clinical GUI agents. In MedUIGym, agents perceive EHR states from screenshots and execute mouse-and-keyboard actions, as well as a paired native-tool interface over identical clinical data. The environment verifies both final answers and required clinical actions, and supports parallel trajectory collection for training. Benchmarking twelve vision-language models shows that current agents struggle across diverse clinical workflows, and simply increasing reasoning effort fails to yield consistent gains. Furthermore, MedUIGym supports offline learning from GUI trajectories and online reinforcement learning from task rewards. After training, both Qwen3.5 models perform better on in-domain clinical tasks and generalize to tasks from external sources. By unifying tasks from existing benchmarks, dual-interface evaluation, and GUI trajectory collection, MedUIGym provides a testbed for studying how vision-language agents complete clinical tasks through the EHR's graphical interface. Our project page is available at this https URL.

---


### 421. [CART: Clustering-based Analysis of Recurring narratives for Taxonomy construction](https://arxiv.org/abs/2611.30993)

**<font color=#1a73e8>作者：</font>** Aggelos Semoglou, Thomas Tselentis, John Pavlopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present CART, a computational pipeline for extracting political narratives from parliamentary discourse and organizing them into a data-driven taxonomy without relying on predefined narrative categories. It encodes parliamentary discourse using semantic representations, filters relevant and reliable content through unsupervised confidence estimation, extracts narrative statements using LLMs, and uses narrative clustering and cluster analysis to construct a narrative taxonomy. Applied to Greek Parliament proceedings surrounding the 2023 Tempi train crash, it identifies ten recurring narrative families concerning responsibility attribution, institutional failure, railway safety, accountability, privatization, and the political interpretation of the tragedy. Our results demonstrate how combining unsupervised learning with LLM narrative extraction enables large parliamentary corpora to be transformed into interpretable, data-driven taxonomies of political narratives.

---


### 422. [Airlock: Robust Sandboxing and Governance of Rogue Agents](https://arxiv.org/abs/2611.31010)

**<font color=#1a73e8>作者：</font>** Sina Abdollahi, Amir Al Sadi, Marios Kogias 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent incidents involving agents bypassing sandboxing and network isolation have raised concerns about existing agent harnesses, prompting frontier labs such as OpenAI to reevaluate the security of their training platforms. Incident reviews show that determined agents can escape processes, containers, and VMs, or bypass their isolation through advanced side and covert channels. Follow-up audits also found that some agents concealed their actions by disabling monitoring and tampering with logs. We propose Airlock, an architecture that pairs each agent's VM with an Airlock VM, each running in a separate hardware-isolated Trusted Execution Environment (TEE). The Airlock VM fully mediates the agent's interactions with the outside world, including network and storage operations. We modify the firmware layer of Arm's Confidential Computing Architecture, Realm Management Monitor (RMM), and the kernels of both VMs so that the Airlock VM serves the agent VM's IO without involving the host. We adapt OpenShell, an agent runtime supporting sandboxing and governance policies, to this architecture. Airlock keeps network and filesystem policies, and credential protection effective even if the agent VM is fully compromised, and it removes the host from the agent's IO path, reducing opportunities for collusion and covert channels with the host. Finally, we extend the Airlock VM's capabilities to provide tamper-proof auditing of all agent operations, preserving forensic evidence even if the Airlock VM is compromised. We implement and evaluate Airlock on a Radxa development board. Our evaluation shows a loss of filesystem performance and network latency for small messages under 15% and a drop of network bandwidth by half or more, which in practice has a limited effect on typical agent tasks.

---


### 423. [Triage Accuracy of Jev and Open-Weight System One Decision Models and Their Use for Early Emergency Recognition in Symptom-Assessment Applications](https://arxiv.org/abs/2611.31012)

**<font color=#1a73e8>作者：</font>** Marvin Kopka, Austen El-Osta, Christoph Kollwitz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Laypeople increasingly use large language models (LLMs) for triage advice, but LLMs answer in variable free text, which makes it hard to evaluate them for use in medical devices. Decision models, which assign a probability to each predefined triage category, may be easier to evaluate. To test their triage accuracy, we evaluated 16 decision models (14 open-weight, 2 proprietary) on 233 synthetic and 10,000 real-world cases, yielding 163,728 total assessments. The best models triaged 72.1% of synthetic cases correctly and agreed with an existing algorithm in 56.1% of real-world cases. They were more promising for recognising emergencies early: given only demographics, chief complaints, risk factors and red-flag answers, the best model reached an AUROC of 0.87. At a 5% error margin, it could decide for or against emergencies for about half of users. Decision models should therefore not replace triage engines but could shorten symptom assessments at setting-specific error margins.

---


### 424. [Can Latent Reasoning Drive LLM Outputs Without a Trace?](https://arxiv.org/abs/2611.31015)

**<font color=#1a73e8>作者：</font>** Tomer Ashuach, Zorik Gekhman, Avi Caciularu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs typically solve complex tasks with chain-of-thought (CoT) reasoning, which is also the main tool for monitoring them for misaligned behavior. However, standard transformers can also solve tasks with complete latent reasoning (CLR), carrying out the whole task internally and outputting only the final answer. Theory bounds the depth of CLR, the number of sequential steps it can carry out, and recent work measured it to be shallow. In this work, we ask whether CLR is deep enough for a model to pursue a hidden objective that requires reasoning. Such a model would generate a CoT that appears to solve the given task, while a latent multi-step computation decides its answer based on the hidden objective. First, we show that a simple auxiliary loss allows models to solve a multi-step task latently at least 5x deeper than previously reported. Then, in two common tasks, decision-making and code generation, we train a model to pursue such a hidden objective, which decides a loan or plants a vulnerability. The model's CoT justifies the output with no trace of the hidden objective, and a strong LLM monitor does not flag it. Finally, using activation patching, we find that the latent computation is completed before the model generates its CoT, which takes no part in it. Altogether, we show that a hidden objective that requires reasoning can go unseen by a monitor that reads only the output.

---


### 425. [Parsing Visual Latents for Multimodal Spatial Reasoning](https://arxiv.org/abs/2611.31021)

**<font color=#1a73e8>作者：</font>** Zhuoying Yang, Yichen Guo, Kathy Jia 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial reasoning across multiple views requires inferring the 3D relations between objects and the camera from 2D observations, which depends on cross-view correspondence and scene geometry that vision-language models (VLMs) do not reliably extract. Pretrained vision encoders already capture this information in their latent features, with CLIP linking objects to image regions, DINOv3 matching semantics across views, and VGGT encoding multi-view geometry. However, VLMs do not benefit from these features when we present them directly in context as grayscale feature images. We therefore propose LatentParse, a training-free framework that parses latent features into explicit spatial evidence for VLMs. In LatentParse, an analyst VLM probes the features of all three encoders with predefined tools that locate objects, track them across views, and measure motion between views. It then distills the results into a concise text report, which is provided together with the images to the VLM to answer the question. We evaluate LatentParse on MMSI-Bench, MV-RoboBench and SPAR-Bench, where it improves all five VLMs over the photo-only baseline by 0.7-2.4 percentage points on average. On MMSI-Bench, it raises Qwen3.8-27B from 34.4% to 39.5%, with the largest improvements of 19.2 percentage points on the camera-related questions. These results suggest that latent features become useful for spatial reasoning once they are parsed into relation evidence, without training. Code is available at this https URL.

---


### 426. [OmniV-Bench: Can MLLMs Comprehend Immersive Spatio-temporal Scenes?](https://arxiv.org/abs/2611.31022)

**<font color=#1a73e8>作者：</font>** Liu Yang, Huiyu Duan, Yixuan Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnidirectional videos (ODVs) capture dynamic environments with a full $360^\circ$ field of view, providing rich spatial context and temporal dynamics for applications such as virtual reality (VR), augmented reality (AR), and embodied intelligence. Recent multimodal large language models (MLLMs) have made great progress in spatial and temporal understanding, yet their ability to comprehend the immersive 360 spatio-temporal information conveyed by ODVs remains largely unexplored. To bridge this gap, we first introduce OmniV-Bench, a Benchmark designed to comprehensively evaluate the capabilities of MLLMs on spatio-temporal Omnidirectional Video understanding. OmniV-Bench contains 4,123 high-quality ODVs collected from diverse scenes, along with 8,923 human-annotated question-answer pairs spanning 11 fine-grained tasks across three categories, i.e., general, spatial, and spatio-temporal understanding. Extensive benchmark experiments reveal that the spatio-temporal complexity of ODVs poses significant challenges for current MLLMs. To address these limitations, we further propose OmniV-Harness, an agentic harness that enhances ODV understanding through viewpoint-guided evidence initialization and task-relevant evidence acquisition with adaptive tool use. Comprehensive experiments demonstrate that OmniV-Harness consistently improves immersive spatio-temporal reasoning ability of MLLMs. Both OmniV-Bench and OmniV-Harness will be released upon publication.

---


### 427. [AI-Assisted Auto-formalization for Trustworthy Scientific Computing: Case Studies and Lessons Learned](https://arxiv.org/abs/2611.31033)

**<font color=#1a73e8>作者：</font>** Mohit Tekriwal, Het Mankad, Naifeng Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI tools have recently had success in mathematical reasoning. Both general purpose coding agents such as Claude Code and Codex, and specialized mathematics agents such as Aristotle, have been used for formalizing mathematical problems such as Fermat's last theorem, Erdős problems and several IMO level math problems. However, much of these efforts are concentrated in the pure mathematics domain, which benefits from relatively self-contained theorem statements, fixed mathematical representation and extensive support in existing formal libraries. Applied mathematics, on the other hand, presents additional challenges because the source may describe a computational procedure or modeling transformation rather than a declarative theorem. In this work, we present a systematic study of AI-assisted auto-formalization for scientific computing (SC), a domain in applied mathematics central to U.S. Department of Energy applications. Through case studies spanning hierarchical abstraction layers in SC software stack, we evaluate not only whether AI agents can complete numerical proofs, but also where and why they fail across the stack. Our primary contribution is a cross-layer taxonomy of failure modes and an analysis of the form of expert feedback required at each layer to recover mathematical soundness. From these observations, we derive a workflow for recurring proof patterns and practical guidance for using AI agents while preserving mathematical soundness. Our results characterize both the practical value and the current limitations of AI-assisted formalization for trustworthy scientific computing.

---


### 428. [Boltz-Flow: Generating High-Quality Robot Action from Boltzmann Machine](https://arxiv.org/abs/2611.31038)

**<font color=#1a73e8>作者：</font>** Hengzhi Jiang, Haixu Liu, Jindou Jia 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flow-matching policies integrate a velocity field from a fixed, observation-independent Gaussian source. However, since the source is unimodal and identical across all tasks, the limited representational capacity of Gaussian distributions constrains how far a policy can scale with growing task diversity. Moreover, the source factorizes over time steps and control dimensions, discarding the coordination that manipulation requires. We introduce Boltz-Flow, which replaces Gaussian initialization with a more powerful, observation- and instruction-conditioned Boltzmann source while leaving the base VLA unchanged. Boltz-Flow parameterizes this source with a conditional Boltzmann machine that assigns an energy value to each binary source state. A listwise objective, supervised entirely by offline demonstrations, aligns this energy with the quality of actions produced after frozen flow integration. At inference, the energy defines an Ising instance whose solution is decoded into continuous noise before a single standard integration. We use a physical coherent Ising machine during training. Experiments show that Boltz-Flow improves $\pi_{0.5}$ across three benchmarks, outperforming the compared strong policy baselines and competing noise optimization methods on LIBERO and RoboTwin 2.0 and ranking second only to LEAP on LIBERO-Plus. Additional experiments show gains under noise-adapted fine-tuning, with action-to-action warm starts, and on the SmolVLA backbone.

---


### 429. [Grower-in-the-loop AI for Deployable Precision Fertilisation in Sustainable Agriculture](https://arxiv.org/abs/2611.31044)

**<font color=#1a73e8>作者：</font>** Xulong Wang, Yu Zhang, Gaoshan Bi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In agriculture, typically over half of the applied nitrogen fertiliser is lost to water and to air. Precision fertilisation aims to reduce these losses while maintaining yield and quality, yet existing tools struggle to capture farm-specific challenges in determining optimal nitrogen rates. Static recommendations are common and overlook on-farm constraints, such as delays due to weather or machinery availability, or change in budgets. Each constraint governs when and how growers apply fertiliser in practice. Here we present a grower-in-the-loop framework for winter wheat in England, combining baseline fertilisation planning from a machine learning-derived nitrogen-response curve with in-season adaptation via a large language model. We evaluated the framework using data from long-term experiments (LTEs), replicated field trials, and farm deployments. Retrospective model validation using LTEs confirmed low economic decision-loss across multiple seasons. Using field and farm trials, baseline schedules were shown to match standard-practice yields with less nitrogen, whereas in-season adjusted schedules additionally retained grain quality standards. Given this enhanced performance, in-season adaptation absorbed weather, machinery and budget constraints to keep recommendations executable. The framework therefore shows promise for translating static recommendations into adaptable, grower-informed decisions for sustainable fertiliser management.

---


### 430. [Distill the Correction, Not the Rewrite: Hindsight Twins for Self-Improving Text-to-Image Models](https://arxiv.org/abs/2611.31048)

**<font color=#1a73e8>作者：</font>** Jiaze Li, Jingyang Chen, Wenhao Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models can learn from their own mistakes by distilling a self-teacher conditioned on a vision-language critic's revised prompt. However, such self-teachers barely improve alignment, and both they and their hindsight-contrast variants absorb the critic's unintended additions to the scene, such as lighting or scenery. We attribute this to two factors: (1) the prompt already specifies the desired fix, so a useful revision must go beyond the failed span, often rewriting the entire scene and adding details that overshadow the fix; (2) although the critic localizes the error to a single span, self-teachers condition on the rewrite, entangling the intended fix with unintended additions. Motivated by these insights, we propose Hindsight Twins (HinT), which fills the critic's revision template once with the intended fix and once with the observed error and distills only their velocity difference, anchored at the user's prompt. Because text encoders spread the edit of a single slot to all other tokens, HinT further aligns the twins' token states outside the slot. Across Qwen-Image-2512, SD3.5-M, and FLUX.2-klein, HinT keeps the rate of critic-induced bias at the base-model level while matching or exceeding the alignment gains of prior self-distillation, and it keeps improving over twelve rounds of self-training where contrastive baselines decay.

---


### 431. [Automatic Occupational Coding through Retrieval-Augmented Generation](https://arxiv.org/abs/2611.31051)

**<font color=#1a73e8>作者：</font>** Mathijs A. Langezaal, Egon L. van den Broek, Lukas P.A. Arts 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Annually 1.9 million deaths and 89.7 million disability-adjusted life years are caused by exposure to agents during work (e.g., welding fumes, silica dust, and noise pollution). To improve worker health, high-quality exposure assessments are crucial. Therefore, free-text job descriptions from large-scale occupational cohorts are manually standardized through occupational classifications and linked to hazardous exposures using Job Exposure Matrices (JEM). However, manual coding is slow, unreliable (i.e., 44-89% inter-coder reliability), and costly, due to i) short, ambiguous free-text job descriptions, ii) classifications containing hundreds to thousands of categories, and iii) the absence of gold standards. With 46%-79% accuracy, state-of-the-art automatic occupational coding tools achieve classification performance on human level. However, their performance drops to 17-26% on out-of-distribution datasets. Furthermore, their supervised architectures limit them to occupational classifications present in the training set. Consequently, JEM using other classifications are incompatible, leaving vital exposure-response associations unexplored. Our Retrieval-Augmented Generation framework, OPERAG, enables classification into any occupational classification without expert-labelled databases. It retrieves coding index information and combines this with Large Language Model-based classification. Validated on AsiaLymph's 36,062 real-world job descriptions, OPERAG achieved 42.6% occupational classification accuracy on the 4th coding level, substantially outperforming existing tools and approaching human coders' 51-56% inter-coder reliability. Using two JEM named ALOHA+ and SHOCK, 89.9-98.6% accuracy was achieved on exposure assessment. OPERAG approaches human-level, universal occupational classification, enabling efficient and effective large-scale exposure assessment to improve worker health.

---


### 432. [DKnown-Jev-2: Article-Level Answer-Evidence Classification and Efficient Inference with a Pre-trained Language Model](https://arxiv.org/abs/2611.31056)

**<font color=#1a73e8>作者：</font>** Qi Li, Jianjun Xu, Jiu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evidence selection in normative knowledge question answering requires determining whether a candidate article contains content that directly supports an answer under the applicable conditions of the question. We present DKnown-Jev-2, an article-level answer evidence classifier designed for evidence integration across multiple paragraphs. The model jointly encodes question conditions, article metadata, and paragraph content, and uses a pointer-style classification head to predict Answer Evidence (AE) and Non-answer Evidence (NE) in a single forward pass. Ona manually annotated test set of 972 evaluation instances, DKnown-Jev-2 achieves 91.77% accuracy and 91.28% macro-F1, outperforming Jev by 2.16 and 2.37 percentage points, respectively, while reducing both evidence misses and non-evidence false positives. The test set contains 317 multi-paragraph instances, with a maximum body length of 9,322 characters. Shared article encoding and non-autoregressive classification support low-latency inference. These results demonstrate the effectiveness of the proposed method for article-level evidence selection in normative knowledge question answering.

---


### 433. [From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems](https://arxiv.org/abs/2611.31063)

**<font color=#1a73e8>作者：</font>** Wenlong Yu, Bingxu Lu, Qilong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In multi-agent systems (MAS) built on large language models (LLMs), errors can propagate through intermediate messages and compromise final answers. However, outcome-based evaluation obscures how agents amplify, attenuate, or correct these errors. We propose Response-Aware Error Propagation among Agents (REPA), a structural model that connects measured local responses to system-level error propagation. REPA separately estimates input assembly and agent processing across multiple error channels, while theoretical analysis relates local modeling errors to endpoint prediction error. Experiments span three Qwen base models, six MAS workflows, and ten knowledge and reasoning settings in ErrPropBench-10. REPA achieves a mean condition-level Spearman correlation of 0.84 across base models, compared with 0.47 for direct regression. Controlled experiments also demonstrate its utility for targeted recovery. REPA-guided retrieval-augmented generation (RAG) improves accuracy over no retrieval by an average of 19 percentage points with 16% additional tokens. By linking local agent behavior to system susceptibility, REPA provides an interpretable foundation for studying error propagation and developing targeted optimization in MAS.

---


### 434. [Decoupling Solving from Abstention: Single-Rollout Conformal Risk Control for Hard-Budget LLM Reasoning](https://arxiv.org/abs/2611.31065)

**<font color=#1a73e8>作者：</font>** Qianyi Chen, Bo Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hard token budgets often interrupt LLM reasoning before an answer is produced. Forcing reasoning to terminate recovers correct solutions but also increases confident errors, creating a joint challenge of solving within budget and deciding when to abstain. Existing remedies are costly or lack guarantees: supervised fine-tuning offers no error control, penalizing wrong answers during reinforcement learning (RL) can suppress exploration, and multi-sample conformal methods multiply inference cost. We propose Tail-CRC, a single-rollout framework that separates candidate generation from submission control. We first adapt the solver to budget forcing with pure binary correctness rewards; after freezing it, we apply conformal risk control to upper-tail token surprise in the answer span. Each rollout yields both an answer and an uncertainty score from token log probabilities, enabling finite-sample control of expected wrong submissions under exchangeability and recalibration across risk targets or domains without retraining. We show that wrong-answer penalties create failure-only comparisons in group-relative RL, derive an exploration-starvation boundary, and identify length-induced ranking reversals and single-token spike sensitivity in answer scores. Across Qwen3.5-4B and Qwen3-8B, 50 RL updates on 400 problems improve correct-submission rates by 15.0--29.6 points on DAPO and 4.3--12.8 points on out-of-domain Omni-MATH over inference-only budget forcing, while reducing generation cost by 3.5--12.6\%. On 8B Omni-MATH, target-domain calibration cuts wrong submissions from 30.3\% to 5.8\% at 4K and from 41.8\% to 6.5\% at 8K. At 4K, generation is 2.05$\times$ faster for 4B and 2.23$\times$ faster for 8B than unforced 8K decoding in local amortized batch time. Tail-CRC thus enables reliable, efficient budgeted reasoning from a single rollout.

---


### 435. [ChiProgramBench: Can LLM Agents Rebuild Efficient Circuits from Pin-Level Experiments?](https://arxiv.org/abs/2611.31082)

**<font color=#1a73e8>作者：</font>** Tianrun Gou, Qingyao Yang, Wendong Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding a system that can be run but not inspected is a core engineering skill: one designs experiments, forms hypotheses about hidden state and timing, discards those that observations refute, and finally builds a replacement that works and is efficient. To evaluate this capability of LLM agents in the hardware domain, we present ChiProgramBench, 18 tasks derived from open-source processors, accelerators, codecs, transforms, interconnects, and control circuits. Agents can only drive and read the pins of a hidden, stateful simulated reference, then submit a gate-level netlist made of public library cells. Agents work in two settings: black-box discovery gives only anonymized functional pins and the interfaces of fixed memories, while function-guided reconstruction adds the circuit's purpose and each pin's role. Hidden test cases compare outputs with the reference cycle by cycle; power, delay, and area earn credit relative to the reference only when every case passes. Across 432 trials of 6 LLM agent configurations, successful agents recover algorithms and numerical conventions, yet only 12.0% of black-box and 14.8% of function-guided trials pass every case. Function-guided reconstruction raises the mean functional score, the cycle-weighted share of passed cases, from 24.6% to 30.9%. Of the 58 fully passing designs, only three improve on the reference's combined power, area, and delay, so behavioral recovery and efficient implementation remain distinct challenges.

---


### 436. [Orthogonally Mixed Sign Coding with Progressive Residual Refinement for Transformer Weight Compression](https://arxiv.org/abs/2611.31089)

**<font color=#1a73e8>作者：</font>** Anindya Roy Chowdhury, Atanu Barai, Nandakishore Santhi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM quantization reduces storage but often degrades predictive fidelity at low bit rates. We propose a training-free, CDF-free, Gaussian-CLT-motivated progressive residual-sign quantization framework that uses randomized orthogonal mixing to promote Gaussian-like residual distributions and improve sign based reconstruction of Transformer weights. Each stage independently normalizes residuals and analytically calibrates reconstruction, progressively recovering quantization errors. The framework enables flexible storage-fidelity trade-offs without learned codebooks, empirical CDFs, or trellis optimization. We evaluate GPT-2 Large and Llama-3-8B across attention and MLP projections. At five residual stages, joint quantization preserves near-baseline predictive fidelity, achieving perplexities of 32.16 and 12.73, compared with full-precision values of 29.89 and 11.07, respectively. Ablations further demonstrate that orthogonal mixing substantially improves reconstruction over identity-based sign coding, while activation-aware scaling improves output fidelity and reduced-precision statistics lower storage overhead with negligible perplexity degradation. Comparisons with conventional quantizers establish the method's progressive fidelity recovery and characterize its storage-quality and runtime trade-offs. These results demonstrate the effectiveness of orthogonally mixed residual-sign coding for flexible, training-free Transformer weight compression.

---


### 437. [Revisiting Learning to Delegate: LLM Discovered Heuristics for Large-Scale Vehicle Routing](https://arxiv.org/abs/2611.31090)

**<font color=#1a73e8>作者：</font>** Zhengyang Wang, Renfei Tan, Shuze Daniel Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient vehicle routing is critical to logistics and transportation, yet solving large-scale capacitated vehicle routing problems (CVRP) remains computationally challenging due to their combinatorial complexity. One approach to solve large-scale vehicle routing optimization is to identify promising subproblems and then optimize them using solvers. In this paper, we propose a framework of automatic heuristic design (AHD) in which a large language model (LLM) autonomously refines heuristics for selecting subproblems, enabling effective optimization of large-scale CVRP instances. Compared to prior approaches that train task-specific neural networks to select among heuristically constructed subproblems, our method discovers generalizable, interpretable LLM-generated heuristics to directly construct subproblems. Experiments show that our approach achieves comparable in-distribution performance while outperforming neural network-based policies on out-of-distribution instances with large-scale problems.

---


### 438. [Unlocking the Power of Loops in Pretrained LLMs with Loop Residuals](https://arxiv.org/abs/2611.31094)

**<font color=#1a73e8>作者：</font>** Xuanlei Zhao, Hailun Xu, Kai Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Looped Transformers iterate a shared block of layers to increase computation without adding parameters, offering stronger performance and test-time scaling. However, this power has so far required training from scratch and yielded only modest gains for LLMs. Finetuning existing models into loops is far cheaper, yet also brings only marginal gains over SFT. We propose LoopRes, an effective, scalable, and simple approach that turns loops into significant and consistent gains for pretrained LLMs. Building on Attention Residuals, LoopRes lets each looped layer attend directly to the outputs of earlier loops. Since these outputs are iterates of the same layers and become harder to tell apart, we give each a trainable loop-aware key that encodes its structural identity. Attending to all earlier loops also lets layers skip intermediate ones, so we restrict each layer to a residual window of the latest W loops, forcing every loop to build incrementally on recent ones. Across 6 pretrained LLMs from 3 model families and 9 benchmarks, LoopRes delivers significant and consistent gains: at 2x compute, it improves Qwen3-1.7B-Base by 29.1% over SFT, more than doubling the gain of the state-of-the-art baseline. The gains hold on larger models up to 30B and across all three families. More importantly, from 1.7B to 8B, LoopRes scales more steeply than SFT as compute grows, reaching a higher ceiling while needing less compute on long outputs. These results establish LoopRes as an effective looping approach, delivering both better performance and better test-time scaling.

---


### 439. [Tradeoffs between objective outcomes and human enjoyment of work in human-AI task allocation](https://arxiv.org/abs/2611.31095)

**<font color=#1a73e8>作者：</font>** Katherine M. Collins, Elizabeth Mieczkowski, Raja Marjieh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For people, tasks at work are defined by more than their outcome: they are colored by the experience of engaging in that task. As AI systems become increasingly capable of performing human-level work they may be deployed to tasks that people find enjoyable while simultaneously creating comparatively more aversive tasks such as monitoring AI outputs. This creates a thorny tradeoff for managers: whether work should be assigned purely based on the expected performance of the workers in question, or also account for the subjective experience of the person potentially doing the task. Most economic accounts focus on expected utility calculations based on the former. Here, we assess how people balance objective outcomes and more subjective qualities like enjoyment. In a series of large-scale (N=800) behavioral studies in which people allocate tasks to either an AI or human worker we find that people's allocation decisions are best captured by a model that systematically balances relative objective performance with the human worker's expected enjoyment, weighting human experience higher when a task is framed as inducing less enjoyment and adjusting based on the stakes of the task. As AI also makes decisions about work allocation, we compare a set of LLMs. We find many models also deviate from purely objective decisions, particularly when the project stakes are low, but there is wide heterogeneity as to how much and in what manner they weigh enjoyment. These results raise questions about what role human experience may play in decisions around where and how to integrate AI into workplaces. Integration may be jagged across settings due to consideration not only of the relative capabilities of workers, but also the human experience of work, the valence of that experience (e.g., more strongly weighing aversion), the context (e.g., stakes), and who is making or guiding such choices (human or LLM).

---


### 440. [LiveLoRA: Exact KV Cache Migration Across LoRA Updates for LLM Agents](https://arxiv.org/abs/2611.31105)

**<font color=#1a73e8>作者：</font>** Tianyi Huang, Samuel Xu, Ivy Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Updating an LLM adapter should not require replaying the full interaction history of every active session. Yet reusing key-value (KV) cache entries computed under an earlier version mixes model versions, while full-history re-prefill becomes increasingly costly as histories and session fleets grow. We introduce LiveLora, a model-runtime co-design for exact final-block KV cache migration. Frozen lower decoder blocks and fixed K/V adapter down-projections preserve each token's base projections and low-rank coordinates across adapter versions. The runtime reconstructs candidate K/V, reevaluates the latest token through the final block, and commits the adapter, cache, and next-token logits together. We prove continuation equivalence to full-history re-prefill in exact arithmetic under the stated model assumptions. On Qwen2.5-3B-Instruct, median paired publication speedups over full-history re-prefill average $68.98\times$ across five runs for 32 active sessions with 8K tokens each. Serving benchmarks show approximately 4.8% decoding overhead relative to native cached decoding. Compared with retained-boundary replay, compact retention gives a $3.42\times$ reduction in additional session storage at 8K, with similar measured publication-plus-decoding cost. LiveLora allows persistent LLM agents to adopt new adapter versions without replaying their full interaction histories.

---


### 441. [Look Back, Draft Ahead: Corrective Prefix Attention for Parallel Speculative Decoding](https://arxiv.org/abs/2611.31112)

**<font color=#1a73e8>作者：</font>** Mohammad Mahdi Moradi, Ali Pourranjbar, Zongzuo Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parallel speculative decoders propose an entire token block at once, yet one early inconsistency can cause the target to reject its remaining suffix. We introduce Corrective Prefix Attention (CPA), which combines prefix-aware selection with autoregressive supervision to improve these parallel drafts. CPA lets each candidate attend to earlier choices within the block. Fixed candidate shortlists allow all pairwise interactions to be computed before selection, reducing the sequential walk to table lookups, accumulation and lightweight scoring rather than repeated neural evaluations. An auxiliary autoregressive loss trains the shared backbone on clean prefixes without adding an inference pass. Across eight math, code and dialogue benchmarks with Qwen3-4B and Qwen3-8B targets on Ascend NPUs, CPA commits 13--15\% more tokens per verification round than DSpark and 25--26\% more than DFlash. Its mean speedups reach $3.35\times$ and $3.37\times$ under greedy decoding and $2.86\times$ under sampling for both targets. Ablations support both components, while capacity sweeps demonstrate that greater acceptance alone does not guarantee faster decoding. These results motivate correcting parallel proposals with causal information while keeping sequential computation inexpensive.

---


### 442. [Self-Upgrading Embodied Agents](https://arxiv.org/abs/2611.31117)

**<font color=#1a73e8>作者：</font>** Jiajun Fan, Neil He, Qinglong Zheng 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An embodied agent built on a language model goes to work with the weights it was given and keeps them for life. To get better, it needs more training, or reflection, memory, search or prompts that cost every step and are lost when the task changes. Editing weights by reasoning, weight-space programming, could end this, but has stayed with models that only reason or relied on a far larger commercial model. We introduce the self-upgrading embodied agent, to our knowledge the first that learns from its own experience by upgrading its own weights on the job, between its tasks, with no training, no gradient, no reward model, no second model, no test-time scaling and no harness or prompt engineering. By day a 27B agent works in a household environment. At night it reads its record, finds many of its steps wasted on replies that reach the token limit before any action, traces the habit to one direction in its hidden states, and rewrites one tensor of its weights. An agent that rewrites itself must first never break itself, so it is its own examiner: it tests every change against its unchanged self on practice tasks and keeps only what holds. When an edit holds, the next day it is a better agent, at the same cost per step: over thousands of held-out episodes, 48 fresh seeds a task, its one kept edit makes it complete significantly more tasks, in fewer steps, with fewer wasted and fewer tokens. This self-improvement is multi-round, stable and continual: through the nights that follow, the upgrade holds, without collapse. Of four sizes of its family, only the 27B agent does this. From here on, an embodied agent need not keep training and inference apart: as it works, it gathers its own experience and upgrades itself, with no separate pre-training or post-training and no human intervention. We believe this opens lifelong continual learning for robots: stable, continual, recursive self-improvement.

---


### 443. [FATCAT: Fault Injection Attacks Targeting Chip-level Alignment](https://arxiv.org/abs/2611.31129)

**<font color=#1a73e8>作者：</font>** Peter Horvath, Ilia Shumailov, Zhuoran Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model alignment is the primary safety and security mechanism for enforcing refusal of malicious prompts in modern foundation models; yet, existing adversarial evaluations implicitly assume underlying hardware integrity. In this paper, we present FATCAT, the first physical fault-injection attacks capable of eliminating refusal in modern large language and vision-language models. Specifically, we present a non-invasive electromagnetic (EM) fault injection attack targeting GPU-accelerated Systems-on-Chip with physical access, requiring neither software execution privileges nor model-layer access. By leveraging an autonomous Radio Frequency (RF) side-channel trigger to synchronize EM faults to the prompt prefill phase, the attack corrupts safety-critical memory transactions across off-chip LPDDR5 DRAM and on-chip LPDDR physical interfaces without crashing the system while preserving model coherence. Evaluated on an NVIDIA Jetson Orin Nano and AGX Thor running Llama 3.2 1B and Gemma 3 1B, localized physical faults reliably force models to fulfill restricted requests, demonstrating that model-level alignment provides no robust security guarantees without hardware-level fault tolerance. Finally, we demonstrate the physical-world consequences of this vulnerability on an active 6-DoF robotic manipulator controlled by a SmolVLA vision-language-action policy. Our attack silently corrupts the model forcing the arm into abrupt, hazardous lunges; in two instances the robotic arm attempted to pinch the paper author -- proving that hardware faults can directly translate into real physical harm.

---


### 444. [Genome-to-Image Translation: Reconstructing Escherichia coli Morphology from Genomic Sequences](https://arxiv.org/abs/2611.31132)

**<font color=#1a73e8>作者：</font>** Son T. Huynh, Thuy T. Le, Thu H. A. Huynh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Antimicrobial resistance in Escherichia coli is established in routine practice by culture-based susceptibility testing, which is slow relative to the clinical need for an early treatment decision. Resistance status also leaves a measurable trace in cell morphology, and whole-genome sequencing of clinical isolates is increasingly available, which raises the question of whether colony appearance can be predicted directly from an isolate's genome. We formulate this as a conditional image-generation problem. The assembled contigs of each isolate are encoded into a single 768-dimensional vector by a frozen genomic language model through a segment-contig-isolate aggregation hierarchy, and a conditional Wasserstein GAN with gradient penalty synthesizes colony images from this embedding together with the applied antibiotic and the resistance label. We train on 167,356 single-cell images from 22 clinical blood isolates imaged under azithromycin, ciprofloxacin, tetracycline, and a no-drug control, compare seven pretrained convolutional backbones inside the generator, and select ConvNeXt-Tiny on distributional image-quality metrics. The synthetic images are then assessed extrinsically: added to a reduced real training set, they improve per-antibiotic resistance classification, with a significant gain in resistant-class recall.

---


### 445. [Deneb-Vritra: Descriptions, Edges and Names Examined by Blocking Via Restoring Token Representations and Attention](https://arxiv.org/abs/2611.31139)

**<font color=#1a73e8>作者：</font>** Mohammed Nayeem Khan, Akhil P, Shahina Shaik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Laya is a 421M-parameter encoder that answers a question about a text in one pass: each answer option, written as a name plus a description, gets a marker token, and one score is read from the network at each marker. We first confirm that such models can follow an option's name when it contradicts the description; the question is where in the network this happens. We locate it. On 951 synthetic questions we move each name onto another option's description and count how often the model picks the option with the right name (the name shortcut): 53% for the released checkpoint, 59% for our fine-tune v1, 11% for a fine-tune with name randomisation. On a 320-item sample, blocking attention from each marker to its own name tokens in layers 14 to 17 of 28 cuts v1's shortcut from 67% to 16% (19% on two schemas held out from component selection) while accuracy with the original names stays at 90%; blocking marker edges to the question, other options or text has no effect. No single head matters (largest effect 9 points), and restoring clean marker states undoes the swap from layer 16. Attention mass tracks the window by layer but not by head. Repeated on 5 checkpoints (released, fine-tuned, name-randomised, and a pair trained without two schemas), the knockout finds similar layers; in the name-randomised ones, blocking the description edges instead brings the shortcut back to 56-58%, so the read persists and is outvoted. Marker states decode the name from layer 0; a one-direction probe erasure changed nothing but was weaker than a random edit. Copying layers 0-13 or 14-27 of a name-randomised sibling into a fine-tune recovers 66% and 65% (v1); 21% and 45% (pair A) of its shortcut reduction. 9 of the 12 predictions we could score, written before running, failed. Head sweeps cover 5 of 5 checkpoints; data are synthetic and LLM-labelled; one architecture.

---


### 446. [Habitats: A Framework for Open-Ended Evolution of Agent Objectives](https://arxiv.org/abs/2611.31160)

**<font color=#1a73e8>作者：</font>** Nicolas Bolouri, Gaya Mehenni, Daniel Toyama  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing what an agent should optimize can be as difficult as optimizing the agent itself. Existing language-model-based reward-generation methods typically refine objectives for predefined tasks and couple the decision of what to explore with the synthesis of how to implement it, potentially narrowing the resulting behavioral repertoire. We introduce Habitats, a framework for open-ended evolution of executable agent objectives. Habitats maintains a population of reward-policy pairs and evaluates every policy under every population reward, producing a cross-fitness matrix that exposes self-mastery, transfer, and functional diversity. A population-level Planner uses this information to select parent rewards and issue targeted mutation directives, while a separate Mutator translates those directives into validated reward programs. We evaluate Habitats in a discrete Card Sandbox and three continuous-control environments (Cart-Pole, Hopper, and Cheetah) against Independent Generation and Direct Mutation baselines. Across four environments and three random seeds, Habitats achieves the highest macro-averaged final Specialist Quality and Behavioral Diversity, with final diversity reaching 1.8x that of Direct Mutation and 2.5x that of Independent Generation. Finally, across ten downstream objectives unseen during evolution, frozen Habitats policy libraries achieve higher paired win rates than size-matched Direct Mutation and Independent Generation libraries at 10,000 adaptation episodes, while also surpassing task-specific policies trained from scratch for 20,000 episodes. These results suggest that separating population-level planning from reward synthesis enables the discovery of diverse, learnable, and reusable behaviors.

---


### 447. [Precision-Aware Learning Rate Transfer Across Block Count in LLM Post-Training](https://arxiv.org/abs/2611.31166)

**<font color=#1a73e8>作者：</font>** Nan Chen, Soledad Villar, Soufiane Hayou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The post-training of pretrained large language models, including supervised finetuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable reward (RLVR), is very sensitive to the learning rate, and tuning it through grid search is costly in both computation and memory. In this work, we propose \textbf{TipSweep}, a method to transfer the learning rate across the number of trainable transformer blocks. To do so efficiently, we search for the best learning rate by training only the last $k_0$ blocks (in our experiments, typically $k_0=1$), and provide scaling rules that predict the optimal learning rate when training any set of $k$ blocks, including when $k=L$ (the full transformer). Across experiments with models ranging from 1 to 7 billion parameters, we observe that the optimal learning rate follows precision-dependent scaling rules: the optimal rate scales approximately as $k^{-1}$ with float32 (FP32) master weights, but as $k^{-1/2}$ when updates are applied directly to bfloat16 (BF16) weights without a master copy. We explain both rules using an analytical model that accounts for update rounding, under assumptions supported by profiling experiments. Finally, we develop two prototypes of the learning rate search for a 6.7-billion-parameter model. The first fits the search on a single consumer GPU with 16 GiB of memory. The second speeds up the search on a high-end GPU by evaluating all candidate learning rates in a single pass over the data, so that a five-candidate search takes about half the GPU hours of one full-depth ($k=L$) run.

---


### 448. [Needwise: Generation-Free Conversational Recommendation from Need-Level Typed Decisions](https://arxiv.org/abs/2611.31175)

**<font color=#1a73e8>作者：</font>** Sungchul Kim, Weixiao Huang, Mekala Raja Sekhar Reddy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational recommenders must rank items against needs that catalogs record only in part, while users add, withdraw and reverse needs and switch between requests. LLM rankers re-read the dialogue at every turn: they are slow, and their ordering does not show which needs an item meets. We show that a conversational recommender can be built from typed decisions instead: named questions over fixed options, answered with option probabilities rather than generated text. On each turn, one typed request maps the message onto the catalog's fields, keeps what no field expresses in the user's words, and decides how the turn changes each earlier need. Needwise then ranks candidates must-first: the needs on the kind of item, its place and its price form a tier, and within it one holistic decision and need-level verdicts (supported, contradicted or unknown) are combined with equal weight (Needwise-HF). With the graded attributes withheld from the records, so that needs must be inferred from names, descriptions and reviews, Needwise-HF ranks Google Local requests significantly better than GPT-6 Sol (0.383 against 0.343 nDCG@10) and is not significantly different from the strongest LLM ranker on Google Local and Yelp; these comparisons keep their sign under every treatment of unrecorded attributes we test. It costs a fraction of GPT-6 Sol's API price and answers in 2.5 s at the median on Google Local, against 5.6 s for GPT-6 Sol. In conversations, the typed state keeps the ranking across switches and returns, but it recognizes only 19-27% of withdrawn needs.

---


### 449. [Know When to Abstain: Conformal Confidence Estimation for Text-to-SQL](https://arxiv.org/abs/2611.31190)

**<font color=#1a73e8>作者：</font>** Avinash Kumar Singh, Bhaskarjit Sarmah, Stefano Pasquali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL systems often return queries that execute successfully but answer the wrong question. Detecting these errors at deployment is hard because execution correctness is defined against a gold query, which exists only in labeled data. We formulate confidence estimation for Text-to-SQL as probabilistic query validation under a latent correctness variable that is observable at calibration time through gold-SQL execution and latent at deployment. Our estimator separates generation from validation. A generator LLM writes and executes the query, and a different critic LLM judges the query and its execution result. The critic's validation and execution-grounded alignment scores are fused with the generator's verbalized confidence, token-level uncertainty, and SQL-structural features in a Random Forest, using two sequential LLM calls. Two calibration steps give finite-sample guarantees. A Learn-then-Test threshold ensures, with probability $1-\delta$, that the error rate among accepted queries stays below a user-chosen budget. A conformal p-value bounds the false abstention rate. On Spider we use GPT-OSS-120B as generator and Gemma-4-31B as critic. The estimator obtains an AUARC of 0.899. Without abstention, 22.6% of queries are wrong. With a 15% risk budget ($\delta=0.1$), a threshold is certified on all 10 resampled splits, and the system accepts 52.4% of queries on average with 9.1% observed error. Five different critic models give similar results. In a controlled comparison on Spider with Olmo-3-32B as generator, the estimator obtains an AUARC of 89.5, compared with 81.2 for the strongest logit-based baseline. Applied to BIRD without retraining, the confidence scores remain informative (AUROC 0.72, against 0.79 on Spider), but the risk guarantee does not transfer, as expected without exchangeability.

---


### 450. [ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents](https://arxiv.org/abs/2611.31198)

**<font color=#1a73e8>作者：</font>** Rui Sun, Junhua Huang, Luca Zancato 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent multimodal search agents use reasoning, vision, and live web search across many turns to answer questions beyond parametric knowledge by orchestrating a small library of hand-crafted search and visual tools. However, the library is laborious to create and maintain, and frozen when new query types, evidence formats, and failure modes are encountered in the wild. Human practitioners, by contrast, cope with insufficient tools by fashioning new ones from familiar parts and reusing them across tasks. Inspired by this, we propose ToolSmith, an automatic tool-generation framework that grows and reuses modules on top of a lean base tool library. We evaluate ToolSmith on three in-domain multimodal search benchmarks and ten out-of-domain benchmarks under a VLM-as-a-Judge protocol. ToolSmith consistently improves over the base library across deployed agents of varying scales, with larger backbones reaping greater gains, demonstrating the scalability of the approach. Our code and data are available at this https URL.

---


> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-486](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
