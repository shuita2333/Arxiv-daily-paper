# 🧠 大模型相关研究 | 2026年10月21日

> 本类共 **548** 篇论文：已确认 **507** 篇，待复核 **41** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

---

### 251. [NeuroAct: Advancing EEG Analysis and Decoding via Dual-Loop Autonomous Research](https://arxiv.org/abs/2610.25211)

**<font color=#1a73e8>作者：</font>** Wei Xiong, Jiangtong Li, Han Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG analysis and decoding underpin brain-computer interfaces, cognitive assessment, and sleep monitoring. Fixed pipelines and reward-driven search do not explicitly determine how signal structure, representations, predictor behavior, and training dynamics contribute to performance or generalization gaps, leaving intervention choice underdetermined. We introduce NeuroAct, an autonomous research agent framework for EEG analysis and decoding. NeuroAct implements dual-loop autonomous research across EEG foundation models, task-specific predictors, and model combinations. In an inner loop, research, development, and review roles use evidence on signal structure, representations, predictor behavior, and training dynamics to test hypotheses, select analyses or interventions, and refine candidates using performance, stability, and cost feedback. An outer loop distills outcomes into conditional, testable recommendations with task and model conditions, then validates and revises them on subsequent this http URL evaluate four settings: (A) EEG General Analysis, (B) Cross-task Model Optimization, (C) Single-task Open Research, and (D) Collaborative Prediction. In Setting A, NeuroAct's 80.88 macro-average exceeds BrainAgent's 63.13 by 17.75 points. In Setting B, NeuroAct raises EEGPT's mean balanced accuracy (BA) by 7.34 points and HBN Pearson's (r) from 0.6894 to 0.7362; in Setting C, it improves ADFTD BA by 16.33 points; and in Setting D, it raises Workload BA from 79.69% to 85.02%. Experience reuse raises BCIC-IV-2a BA from 34.66% to 50.81% while reducing LLM tokens by 64.02%, indicating recommendations improve cross-task performance. NeuroAct enables evidence-guided EEG research improved by cross-task experience.

---


### 252. [Calibration-Free Early Stopping for Chain-of-Thought Reasoning via E-processes](https://arxiv.org/abs/2610.25212)

**<font color=#1a73e8>作者：</font>** Dong-Jae Lee, Gyojin Han, Junmo Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning large language models (LLMs) benefit from test-time scaling, motivating adaptive policies that spend tokens when they help and stop early otherwise. Existing rules halt when a confidence or stability signal crosses a threshold, but such thresholds rarely transfer across models and datasets, and validation-calibrated rules lose their guarantee under shifts in test-time horizon or signal dynamics. We reframe adaptive stopping as sequential evidence accumulation along the reasoning trajectory rather than threshold calibration on held-out data. Our framework runs two e-processes on a shared per-chunk signal: a commit stream tracks the signal's position relative to its slow trend, and an abstain stream tracks its signed velocity, making the two anti-correlated by construction. Under signal-level nulls on the per-chunk increments, Ville's inequality yields an anytime-valid signal-level false-alarm bound at user-specified significance levels, with no held-out calibration. Across various model--dataset combinations, the framework matches or exceeds calibration-based stopping on the token--accuracy Pareto front using zero calibration data, and the same significance level transfers unchanged across cells where calibration becomes infeasible.

---


### 253. [Hidden Cartographer: Hidden State Guided Data Selection for Dual Budgeted Instruction Tuning](https://arxiv.org/abs/2610.25215)

**<font color=#1a73e8>作者：</font>** Zixuan Qin, Qi Qin, Erbo Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Given the high cost of expert annotation and limited fine-tuning resources, effective data selection from large unlabeled pools under strict budgets has become a crucial step in adapting LLMs to specialized domains. Existing label-dependent methods risk distorted selection when using pseudo-labels, while traditional active learning methods do not explicitly characterize instruction-tuning dynamics. To address these limitations, we propose Hidden Cartographer (HC), a two-stage framework that uses hidden states to guide annotation and exact training dynamics to select the final training subset. The first stage is Progressive Candidate Expansion, which utilizes the proxy to iteratively select top unlabeled candidates for expert annotation, merging them to recompute training dynamics and update the proxy until the annotation budget is exhausted; the second stage is Exact Cartography Pruning, which ranks these annotated candidates by their exact dynamics scores to isolate a compact subset under the final training budget. Experiments across the medical, legal, and financial domains demonstrate that HC achieves the highest average accuracy among all budgeted baselines, requiring annotation for only 20--30% of the original pool and fine-tuning on just 10--15%.

---


### 254. [Evaluating Cloud and Self-Hosted OCR Systems for Arabic, English, and French Documents: Bounding Box Detection, Text Recognition, and Mathematical Expression Recognition](https://arxiv.org/abs/2610.25235)

**<font color=#1a73e8>作者：</font>** Jumana Alsubhi, Ahmed Alhusayni, Abdulrahman Gharawi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Choosing an OCR system for a multilingual archive requires balancing accuracy against deployment constraints. This study compares cloud and self-hosted systems on three tasks: bounding box detection on 48 Arabic, English, and French pages, text recognition on 315 pages across nine document types, and mathematical expression recognition on 83 English and Arabic samples. Detection was assessed by page-level visual grades, text by character error rate (CER) against a Gemini-generated reference transcription, and mathematics by scores against known answers. Main estimates are accompanied by 95% intervals and paired comparisons. Google Document AI and Surya produced Good line boxes on 47 of 48 (98%) and 46 of 48 (96%) pages. Datalab, Azure Document Intelligence, and Document AI had mean CERs of 0.145-0.152, with no difference detected in unadjusted paired comparisons. Surya had the lowest mean CER among self-hosted systems (0.199). No mathematical test had a statistically clear leader. Strict checks showed that near-perfect page scores could conceal a replaced Arabic variable or Eastern Arabic digits rewritten in Western form. Reliable evaluation therefore requires uncertainty estimates, structural checks, and notation-specific tests in addition to aggregate recognition scores.

---


### 255. [It's Complicated: Factors Influencing the Effectiveness of LLM-Generated Feedback in a Live Programming Course](https://arxiv.org/abs/2610.25244)

**<font color=#1a73e8>作者：</font>** Tsvetomila Mihaylova, Arto Hellas, Bita Akram 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We report on three iterations of an LLM-generated feedback system deployed in a live web development course, spanning three underlying models and three feedback formats. We ask how feedback presence and its characteristics (length, complexity, format) relate to student performance, whether prior feedback exposure is associated with final-project performance, and how performance changes after first exposure. Feedback was associated with more favorable immediate outcomes in several comparisons, but the pattern varied by outcome and period. In pooled models, longer feedback was associated with lower next-submission correctness, more remaining attempts, and longer resubmission time. Prior same-part feedback was associated with lower final-project solve probability. Student-level comparisons found differences on final-project steps begun before exposure, while within-student changes across steps were uncertain. These comparisons do not identify the causal effect of feedback. Changes on standard exercises were more favorable among exposed students, but the groups' different course-stage splits limit causal interpretation. Bounded message length and student choice of format are directions for experimental evaluation. Our final-project analysis captures follow-up performance rather than directly measuring learning or understanding.

---


### 256. [Visual Scaffolding: Toward Native Multimodal Reasoning](https://arxiv.org/abs/2610.25247)

**<font color=#1a73e8>作者：</font>** Run Shao, Zhaoyang Zhang, Ziyu Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The success of chain-of-thought (CoT) in complex reasoning can be attributed to a textual scaffolding effect: explicit intermediate results can be examined, reused, and composed to support subsequent reasoning, much as scaffolding supports a building under construction. However, mainstream multimodal LLMs lack an equivalent scaffold for visual distinctions that are difficult to express in concise verbal descriptions. We therefore ask: Can native visual representations become first-class citizens alongside language, providing a visual scaffold for reasoning? We define native multimodal reasoning as reasoning in which native visual representations and language jointly carry reusable intermediate states. As a concrete implementation, the visual scaffolding mechanism we proposed lets the MLLM autonomously initiate a retrieval action at any reasoning step. A lightweight retriever selects native visual features, which are then incorporated directly into the evolving CoT and remain available to subsequent steps. To evaluate this mechanism under controlled visual demands, we introduce NMR-Bench, comprising Burden Counting and Path Tracing. With 88M added parameters (approximately 2%) on Qwen3-VL-4B-Thinking, our model achieves 66.43% and 72.50% accuracy, respectively, surpassing the evaluated GPT-5.5 and Gemini 3.1 Pro baselines. Controlled interventions show that changing selected visual content affects task accuracy and can redirect subsequent visual selection even when intervening text is held fixed. These findings show that native visual states can function as intermediate reasoning material and point toward reusable scaffolds for additional modalities.

---


### 257. [Persistent Representational Misalignment Induces Vision-Language Model Failures](https://arxiv.org/abs/2610.25252)

**<font color=#1a73e8>作者：</font>** Yonatan Gideoni, Yoav Gelberg, Tim G. J. Rudner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) fail at some tasks that are simple for humans---but why? We hypothesize that many such failures stem from VLMs' difficulties translating between vision and language representations, a misalignment the Platonic Representation Hypothesis predicts should disappear with scale. This paper is composed of two parts: in the first, we show that existing vision and language representations are linearly unalignable. This misalignment is an inherent property of the data and hence expected to persist regardless of either scale or the alignment's complexity. In the second, we demonstrate how this misalignment both leads to a predictably induced generalization failure and correlates with existing failure modes, where more representationally aligned VLM backbones accordingly exhibit fewer failures. Overall, these results imply representations will not become aligned simply given sufficient scale, providing evidence against a strong version of the Platonic Representation Hypothesis.

---


### 258. [BatchParScale: Sparse Batch-Mixing for Sequence Models](https://arxiv.org/abs/2610.25254)

**<font color=#1a73e8>作者：</font>** Hans Peter Lyngsøe Raaschou-jensen, M. Onurcan Kaya, Desmond Elliott  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent test-time scaling methods improve model performance by increasing inference-time compute. One practical form of this is parallel scaling, where a model samples multiple independent reasoning streams and aggregates their answers using methods like voting, reranking, or verification. While effective, this approach leaves the streams uncoordinated, and a discovery made in one rollout cannot influence any other. Multi-Sequence Verifiers jointly score candidate answers after generation, but the reasoning streams remain independent during inference. ParScale takes a step toward model-internal parallel scaling by learning to aggregate multiple forward passes, but its streams still do not exchange information while processing a sequence. We introduce BatchParScale, an attention mechanism that allows parallel streams to exchange information through a small set of communication positions. We evaluate BatchParScale on a new Parallel Needle-in-a-Haystack retrieval benchmark and in pretraining, fine-tuning, and cooperative multi-agent reinforcement learning. Across these settings, BatchParScale outperforms ParScale on language-model loss and remains competitive on coordination-sensitive MARL tasks. Masked pretraining runs beat an unmasked single-sequence baseline despite local sequence corruption, and LoRA fine-tuning shows the mechanism can be added to a pretrained Transformer. At the same time, fact retrieval performance for pretrained and finetuned BatchParScale models remains unclear.

---


### 259. [SPARC: Spoken Profile Authorship Recognition Corpus](https://arxiv.org/abs/2610.25265)

**<font color=#1a73e8>作者：</font>** Efthymios Tsaprazlis, Bowen Yi, Tiantian Feng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech anonymization has focused on the acoustic signal, leaving open how much speaker information the transcribed words themselves retain. In this work, we study pairwise speaker and demographic-attribute verification from transcribed speech. We introduce SPARC (Spoken Profile Authorship Recognition Corpus), a benchmark built from two podcast corpora comprising over 12,500 speakers, 1.5M quality-filtered utterances, and speaker-level inferred or source-provided labels for sex, age, and accent, and evaluate five attribution models and three LLMs on identity- and attribute-verification trials with episode- and metadata-based topic proxies. LLM adversaries distinguish same-speaker pairs from text alone. Attribute-label agreement is harder to verify, but LLMs perform sex- and accent-label verification above chance. Finally, releasing only short probe texts (50 words) degrades the strongest adversaries the most, offering a partial reduction in observed linkage.

---


### 260. [EG-GRPO: Evidence-Guided Step-level Credit Assignment for Deep Search Agents](https://arxiv.org/abs/2610.25269)

**<font color=#1a73e8>作者：</font>** Sijia Luo, Mengjie Gao, Yuxiao He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based search agents demonstrate strong capabilities in long-horizon information seeking and reasoning, typically trained via reinforcement learning. However, existing approaches predominantly rely on trajectory-level outcome rewards, providing limited supervision for complex search and reasoning processes. Although step-level credit assignment offers a promising solution, obtaining reliable and task-grounded supervision for open-ended search remains challenging. In this paper, we propose Evidence-Guided Group Relative Policy Optimization (EG-GRPO), a framework that derives step-level supervision from the evidence annotations available in synthetic deep search data. EG-GRPO identifies the first supporting citation for each required evidence claim and uses the newly acquired evidence to construct step-level process rewards. By representing the accumulated evidence as an evolving knowledge state, EG-GRPO further performs state-conditioned relative advantage estimation and combines the resulting step-level signal with the standard trajectory-level outcome advantage. Experiments on five challenging deep search benchmarks show that EG-GRPO generally outperforms standard GRPO and existing reward-enhanced and step-level RL baselines across different model scales. These results demonstrate that task-grounded evidence annotations can provide effective process supervision for credit assignment in deep search RL.

---


### 261. [GeoART: Geometry-Aware Refinement via Test-Time Scaling for Camera-Conditioned Video Diffusion](https://arxiv.org/abs/2610.25273)

**<font color=#1a73e8>作者：</font>** Liudi Yang, Ziyuan Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Camera-conditioned video diffusion models often suffer from inaccurate camera control and geometric inconsisten- cies because camera constraints and estimated geometry are only weakly enforced during denoising. Existing reme- dies often require costly geometry-aware fine-tuning or ad- ditional 3D supervision. We introduce GeoART, a training- free self-refinement framework that improves camera con- trollability through geometry-aware test-time scaling. At selected denoising steps, GeoART generates multiple can- didates within the Predict-and-Perturb cycle and eval- uates them using a geometry prior, without directly modify- ing the denoising trajectory. A confidence gate suppresses unreliable geometric evidence, while rank-calibrated prob- abilistic selection combines score magnitude and relative rank to choose the next refinement state. Experiments demonstrate consistent improvements in camera controlla- bility, multi-view consistency, and visual quality over exist- ing sampling and self-refinement methods, without training or modifying the pretrained video diffusion model

---


### 262. [Bridging Concepts: Multi-Agent Reasoning over Scientific Concept Graphs for High-Impact Research Prediction](https://arxiv.org/abs/2610.25281)

**<font color=#1a73e8>作者：</font>** Donggyu Yoon, Minsung Hwang, Juneha Baek 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Within a research community, new topics often emerge when previously unconnected concepts are first studied together. We construct scientific concept graphs (SCGs)--domain knowledge graphs whose nodes are fine-grained research concepts extracted from paper text by LLMs and whose edges capture their co-occurrence in papers--and study the task of forecasting high-impact concept pairs, i.e., discovering concept pairs that are currently unconnected but will have high impact when connected. To this end, we introduce new benchmark datasets constructed from CIKM, KDD, and SIGIR conference papers, with varied prediction settings, including impact forecasting for emerging concepts unseen during training. We propose MiroGraph, a Multi-agent reasoning framework with scientific concept Graphs, in which a feature designer agent designs predictive features for a given concept pair from structural, semantic, and trend perspectives, and then three LLM agents compute the actual feature values from the enclosing subgraph of the concept pair. Using these feature values, a classifier designer agent constructs a classifier that predicts the final impact labels. MiroGraph outperforms various impact forecasting and temporal link prediction methods.

---


### 263. [MotionShift: Environment-Compatible Motion Transfer via Planner-Evaluator Synergistic Adaptation](https://arxiv.org/abs/2610.25290)

**<font color=#1a73e8>作者：</font>** Yanchen Liu, Junyao Gao, Yanan Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing motion transfer methods excel at exact, rigid motion replication from reference videos to target scenes, whereas they often fail to account for the compatibility between the transferred motion and the target scene environment in accordance with physical laws. In this work, we propose MotionShift, a novel motion transfer framework that achieves high-fidelity motion transfer while ensuring physical compatibility with the target scene. In particular, we design a planner--evaluator iterative motion adaptation mechanism, in which a Large Language Model (LLM) acts as the planner to generate motion trajectories by leveraging its strong semantic reasoning capabilities, while a Vision-Language Model (VLM) serves as the evaluator to rectify the motion based on its superior visual perception and scene understanding. Through this planner--evaluator synergistic reasoning process, the motion is adapted to the target scene in a training-free manner. The adapted motion is then used as a generative condition for an image-to-video (I2V) model to render videos in the target scene. Extensive experiments demonstrate that MotionShift achieves high-fidelity and physically compatible motion transfer across diverse and complex scenes. Moreover, we show that MotionShift can be readily integrated into existing trajectory-conditioned I2V models, endowing them with realistic motion transfer capabilities.

---


### 264. [Aligning Language Models with Indigenous Community Cosmovision through Constitutional AI](https://arxiv.org/abs/2610.25298)

**<font color=#1a73e8>作者：</font>** Silvia Fernández-Sabido, Jorge Reyes-Magaña, Jesús Adrián Chay Tun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are predominantly trained on corpora that reflect Western, anglophone worldviews. This asymmetry is not neutral: when a model answers questions about territory, community authority, or the relationship with nature, it does so from assumptions that may be alien to the communities using the system. This paper presents a system for aligning language models with the ethical principles of Indigenous communities in Latin America. Drawing on interviews with five Indigenous leaders and defenders, we built an operational cultural constitution grounded in an Indigenous cosmovision, with 12 principles. On this basis, we implemented a Constitutional AI (CAI) pipeline in two phases: supervised fine-tuning (SFT) and direct preference optimization (DPO). The base models were Qwen2.5-7B-Instruct and Qwen2.5-1.5B-Instruct. With only 24 preference pairs, improvements were modest but detectable in intergenerational transmission, linguistic caution, and consultation and consent. Qualitative analysis reveals that the SFT phase was responsible for the primary shift in alignment, while DPO refined specific categories. The system was deployed in a conversational interface with retrieval-augmented generation (RAG) that allows communities to feed the knowledge base, turning alignment into a participatory cycle. We argue the architecture is functional and will scale qualitatively once the corpus is expanded and computing constraints are resolved. The work constitutes a first iteration of an epistemic justice mechanism for value alignment in the Global South.

---


### 265. [Atoms, Not Knowledge: What Production-Scale Addressed-Memory Writes Deposit](https://arxiv.org/abs/2610.25317)

**<font color=#1a73e8>作者：</font>** Wei Gao, Cheng Tian, Duan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deterministic hash-addressed conditional memory permits local post-hoc knowledge injection. Extending arXiv:2610.21553's bounded-feasibility audit rejecting under-specified generality claims with repaired probes and training-dose/capacity axes, we give, to our knowledge, the first production-scale write-content verdict. We test 124M-7B self-trained/publicly pretrained beds, Qwen3.8-Flash-Next-FP8 (176.95B; 320,001,536 FP8 rows), and DeepSeek-V4.1-Flash. Write coverage requires a sufficiently trained backbone prior, full-width readout, trainable gates; undertrained-bed intervention confirms a threshold, not a slope. At fixed budget, coverage falls from 98% (50 facts) to 12.7% (1,000); table size is not binding. Two-hop composition does not exceed the independent single-hop baseline (26% observed vs 25% expected; 15% lexical-distortion floor). Synergy remains absent across dose/load in two independent bed families. A 28-percentage-point in-context gap (given vs recalled intermediates) localizes failure to retrieval-for-reasoning, not gate access. Writes are independently retrievable, precisely addressable, reversible atoms, not composable into reasoning. A layered protocol, the first, to our knowledge, to cover compositionality in behavioral memory evaluation, separates baseline, synergy and distortion floor. Any addressed/key-value memory must report coverage, synergy ratio and distortion rate before deployment claims. Composition must be system-orchestrated; multi-constraint queries should explicitly chain written atoms. In-context controls show given intermediate entities are exploited at twice the implicit rate. Production load fits exponential interference ($R^2=0.98$); its mechanism, between budget dilution and write interference, remains open. All numbers are recomputed from archived raw logs/JSON; a fresh 52-target production rerun gives 52/52, exactly matching archived baselines.

---


### 266. [Where and Why Search-Augmented LLMs Fail When Reasoning over Rapidly Evolving Knowledge](https://arxiv.org/abs/2610.25323)

**<font color=#1a73e8>作者：</font>** Tianyi Hu, Bhavyajeet Singh, Niket Tandon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As the world changes, new information is published while older records remain online. This complicates reasoning for large language models (LLMs), which must retrieve evidence and resolve conflicts to determine which information remains valid. Existing evaluations treat information seeking as a black box, revealing little about where and why LLMs fail. To address this gap, we introduce TREK, a suite of three components: TREKTRACE is a plug-and-play framework that attributes failures to specific stages of retrieval and reasoning. We apply it to TREKBENCH-WILD, a meta-benchmark of real-world questions that require complex reasoning over rapidly evolving knowledge. Surprisingly, the main bottleneck is post-retrieval reasoning rather than retrieval: frontier models are often misled by conflicting evidence even after retrieving all the information needed to answer. To study this bottleneck, we build TREKBENCH-CTRL, a controlled benchmark with distractors spanning temporality, relevance, and trustworthiness, and show that benchmarks dominated by outdated distractors substantially underestimate task difficulty. Together, TREK provides a testbed for diagnosing and improving reasoning over rapidly evolving knowledge.

---


### 267. [UnexpectedParrots: Iterating Behavioral Experiment Design with In-Silico Simulations](https://arxiv.org/abs/2610.25343)

**<font color=#1a73e8>作者：</font>** Sanchaita Hazra, Bodhisattwa Prasad Majumder, Pao Siangliulue 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Running behavioral experiments is expensive, slow, and prone to design flaws, often detectable after collecting data. We introduce UnexpectedParrots to iteratively refine behavioral study designs before a researcher recruits costly human participants. UnexpectedParrots relies on reasoning traces in addition to responses from LLM participants to uncover diagnostic critiques of structural errors and missed opportunities in existing study designs. When evaluated against a human-pilot or a no-simulation design-only baseline, UnexpectedParrots adds most value, producing unique, high-quality critiques. In a moderated user study with 12 proficient researchers, we find UnexpectedParrots useful, time-saving, and thought-provoking. Critiques provided by UnexpectedParrots often converge on issues researchers identify only during independent human pilots or additional formative interviews, even when the fidelity of the simulated populations remains questionable. Our users deem UnexpectedParrots useful not only as a tool to conduct early pilot studies and identify errors but also as an ideation tool to expand one's research horizon.

---


### 268. [Local Evidence, Global Failure: Diagnosing Speech-Vision Temporal Composition in Audio-Visual Language Models](https://arxiv.org/abs/2610.25352)

**<font color=#1a73e8>作者：</font>** Jaehong Myung, Seunghun Oh, Unsang Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual large language models (AV-LLMs) can fail at full-video speech-vision decisions even when useful visual evidence is locally recoverable. We introduce Temporal Evidence Decomposition (TED), a training-free diagnostic framework that separates local visual verification from speech-relative aggregation. Automatic speech recognition supplies a transcript and utterance interval. TED queries audio-free windows with the transcript for Temporal Alignment and Forecasting, or answer candidates for Cross-Modal Temporal Binding, then aggregates evidence relative to that interval. Across four frozen AV-LLMs on SVHalluc, Temporal Forecasting accuracy rises from 29.3-33.7% under full-video questioning to 79.3-82.2% with TED. Query replacement reduces recovery; the observed anchor remains beneficial when temporal-region availability is held fixed. Physical-isolation and timing-shortcut controls test alternative explanations. The findings distinguish locally recoverable evidence from successful full-video decisions, motivating explicit separation of narration content, utterance timing, and time-indexed visual evidence.

---


### 269. [CHSM8: A Chess Transformer that Follows Natural-Language Style Prompts](https://arxiv.org/abs/2610.25356)

**<font color=#1a73e8>作者：</font>** Ilia Badanin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present CHSM8, a 210M-parameter chess transformer that plays moves conditioned on a free-text description of a playing style, e.g. "go for the Sicilian Defense", "solid, safe, risk-free chess" or "You are Magnus Carlsen in his prime". The model is pretrained without search on 1.07B filtered Lichess games, using a factorized move representation and legal-move masking. It reaches 1837 Elo against a strength-limited Stockfish and, in 1,000-game matches, beat every other public model we tested that was likewise trained without preference tuning, rewards or search, including one with 13 times as many parameters. We then fine-tune it to follow text on a synthetic dataset: Gemma-4-31B describes the playing style of 3M game sides, a 1B Gemma-3 model distilled from the 2.4M of those descriptions that contradict nothing on the board labels the rest, and every one of 30M selected game sides gets five descriptions. Supervised fine-tuning attaches a frozen text encoder through gated cross-attention, and direct preference optimization (DPO) uses the same moves under a mismatched description as the rejected sample. After DPO, style adherence rises on every prompt we test (for example, queens traded early 53% -> 67%, pawn moves 29% -> 32% of all moves, queenside castling 97.3% -> 99.7%), and strength without a prompt stays within noise of SFT (1792 vs. 1797 Elo). Design choices at every stage were made by fixed-budget automated search loops on top of standard architectures and training recipes. We document the full pipeline and the decisions behind it, report the ablations that failed, and evaluate the models across many style prompts and kinds of games, with 1,000 games per setting. The work is fully open source and reproducible: weights, datasets with all training labels, prompts, configurations, inference code and playable demos are public and free to build on.

---


### 270. [CD-OPD: Contextual Digest for On-Policy Distillation](https://arxiv.org/abs/2610.25359)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Yucheng Li, Xiaxia Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Teacher takeover in on-policy distillation (OPD) can produce incorrect responses even when the student and teacher independently answer the same problem correctly, a failure we quantify using Collaboration Failure Rate (CFR). To address it, we propose Contextual Digest for On-Policy Distillation (CD-OPD). CD-OPD structures the earlier context of teacher guidance through a teacher-generated dependency graph, curating the required problem conditions and preceding reasoning as node summaries alongside the unchanged guidance in a Contextual Digest before student continuation. We further develop online meta-reweighting, which compares Digest segment gradients with a task gradient from independent student responses to improve student-only performance, favoring updates predicted to reduce task loss. Across eight benchmarks, CD-OPD improves average accuracy by 1.32--7.05 percentage points over representative existing OPD methods. It also reduces CFR by 27.4\%--56.4\% relative to existing takeover-based OPD methods.

---


### 271. [Aligning Cultural Behaviors in Arabic Language Models via Preferences](https://arxiv.org/abs/2610.25362)

**<font color=#1a73e8>作者：</font>** Junhong Liang, Daniil Orel, Saeed Almheiri 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Arabic LLMs have improved rapidly, but aligning them with country-specific cultural behavioral preferences remains underexplored. Previous work has focused primarily on instruction-tuning for factual knowledge, overlooking nuanced cultural behaviors. We propose ArabPref, which to our knowledge is the first large-scale pan-Arab preference data set for the alignment of cultural behavior conditioned on the country. Our contribution includes two resources in English and Modern Standard Arabic: a culturally grounded preference dataset for training and evaluation, and a multiple-choice benchmark designed to assess culturally aligned behavior across nations. All test data are validated by native speakers to ensure authenticity. To optimize cultural alignment, we experiment with post-training methods across multilingual and Arabic-centric language models, evaluating performance on both generation tasks and our cultural multiple-choice benchmark. By releasing an evaluation benchmark, we provide a foundation for systematically studying and improving culturally aligned behavior in language models.

---


### 272. [Mining the Self-Rewriting System: A Vision for Data Mining on AI-Native Infrastructure](https://arxiv.org/abs/2610.25374)

**<font color=#1a73e8>作者：</font>** Mayank Darbari, Chiman Salavati, Liang Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classical data mining treats data as generated outside the learner. Emerging AI-native infrastructure invalidates this assumption: as agents observe system state, act, update retrieval stores and models, and promote new artifacts into the serving path, their own decisions reshape the future logs, traces, corpora, and evaluation records used for later training and release. We call this new research object a self-rewriting system and the resulting system-induced distribution shift endogenous drift. Our central, falsifiable claim is that cross-surface causes are not identifiable in general from marginal per-surface monitoring: different coupled failures can produce the same individual signals while differing in their joint behavior, requiring joint analysis for reliable attribution. This agenda comprises four foundational research problems: fusing heterogeneous drift signals into calibrated gating and attribution (C1); mining agent traces whose activity alphabet evolves (C2); maintaining knowledge fabrics through online reindexing, faithfulness, and compression decisions (C3); and safely promoting concurrent learning streams through one shared evaluation gate (C4). These remain fragmented across concept drift, performative prediction, process mining, streaming retrieval-augmented generation, and MLOps, without a unified data-mining agenda. We outline public benchmarks and evaluation criteria, using AI-native telecom only as a motivating exemplar with analogues in finance, software CI/CD, and clinical decision support.

---


### 273. [Outcome-Anchored Credit Reallocation for Agentic Knowledge Graph Question Answering](https://arxiv.org/abs/2610.25384)

**<font color=#1a73e8>作者：</font>** Mingyuan Li, Yucheng Li, Xiaxia Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic knowledge graph question answering (KGQA) requires large language models (LLMs) to solve complex questions through multi-turn interactions with a knowledge graph (KG). Outcome-supervised reinforcement learning derives verifiable outcome rewards from final answers but uniformly assigns each rollout's outcome-level advantage to all policy-generated tokens, creating a trajectory-to-operation mismatch since KG operations within a rollout can have varying effects on the search process and final answer. To address this, we propose Outcome-Anchored Credit Reallocation (OACR), which employs a training-only KG-state outcome model to estimate outcome-reward changes between adjacent KG search states and converts them into operation credit, from which token-wise weights are derived. These multiplicative weights reallocate token-level update magnitudes while preserving the sign of the outcome-level advantage at every generated token. Across three benchmarks, OACR achieves stronger overall performance than existing KGQA methods while using fewer inference-time LLM calls and tokens.

---


### 274. [From Unverifiable Domain Text to Cross-Lingual RLVR via Code-Switched Task Synthesis](https://arxiv.org/abs/2610.25399)

**<font color=#1a73e8>作者：</font>** Cheonbok Park, Jihwan Kim, Shinyoung Joo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) can improve reasoning in large language models, but specialized non-English domains expose a data mismatch. Raw English domain text is often available, while target-language RLVR tasks with verifiable rewards are scarce. We introduce code-switched task synthesis for cross-lingual RLVR, a data-centric approach that derives target-language and code-switched RLVR task variants from otherwise unverifiable English domain text. Using fill-in-the-middle multiple-choice QA as a seed task format, we synthesize automatically verifiable tasks from domain passages and reshape them into cross-lingual variants. These variants preserve the same evidence-answer relation but change how English and target-language evidence are presented during RLVR. On Korean medical benchmarks and cybersecurity benchmarks across four target languages, code-switched training outperforms matched monolingual and bilingual-mixture baselines on average target-language performance while maintaining comparable English performance. Additional analyses provide evidence of better target-language input understanding and stronger cross-lingual alignment in both model outputs and internal representations. These results suggest that code-switched training helps target-language inputs access domain reasoning learned more strongly in English.

---


### 275. [When Form Changes but Logic Doesn't: Building Logic-invariant LLMs through Logical Structure](https://arxiv.org/abs/2610.25402)

**<font color=#1a73e8>作者：</font>** Xuyuan Liu, Xinshuai Dong, Elynn Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved strong performance across diverse reasoning tasks, yet it remains unclear whether this performance reflects an understanding of underlying logical structure or a reliance on shallow semantic cues. A key indicator of such understanding is whether models treat logically equivalent inputs consistently, producing the same predictions despite differences in expression. Through systematic evaluation on curated data, we show that even strong LLMs often fail this test: they do not consistently preserve predictions across logically equivalent inputs and generalize poorly to unseen logical forms. To address this limitation, we propose LoGIcal STructure-guided reasoning (LoGIST), a framework that guides LLM reasoning with explicit logical structure. LoGIST maps each input instance to a decision diagram, a directed acyclic graph that captures the underlying logical structure, and encodes this graph into a logical embedding that conditions the LLM's reasoning process. Across multiple training settings, LoGIST reduces inconsistency under logical equivalence and improves generalization to unseen logical forms, suggesting that logical invariance is a useful target for building more robust and generalizable logical reasoning in LLMs.

---


### 276. [Towards Figurative Language Understanding in Moroccan Darija: An Evaluation of Large Language Models](https://arxiv.org/abs/2610.25406)

**<font color=#1a73e8>作者：</font>** Jihad R'baiti, Youssef Hmamouche, Emmanuele Chersoni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Figurative language remains a major challenge for Machine Translation (MT) systems, as the intended meaning of such expressions often goes beyond literal translation. Although recent advances in Large Language Models (LLMs) improved the translation of Arabic dialects, benchmark resources for evaluating figurative language translation in Moroccan Darija remain scarce. To this end, we introduce the Moroccan Darija Figurative Language Corpus (MDFC), a benchmark dataset for MT and multiple-choice question (MCQ) selection covering idioms, metaphors, and proverbs. Using MDFC, we evaluate 19 open- and closed-weight language models and MT systems at both the expression and contextual levels under zero-shot and six-shot settings. We also conduct layer-wise similarity-based probing to determine how model representations distinguish figurative from literal meanings. Our findings reveal that closed-weight models achieve the strongest translation performance, while the benefits of contextual information vary across models and tasks. Differences between translation performance and MCQ accuracy highlight the distinction between generating an appropriate figurative translation and recognizing the intended meaning among candidate translations.

---


### 277. [From Label Priors to Task Evidence: Efficient Long-Video Frame Selection via Bayesian GRPO](https://arxiv.org/abs/2610.25418)

**<font color=#1a73e8>作者：</font>** Shuochen Chang, Bingjie Gao, Qingyang Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) face significant scalability challenges in long-video understanding due to quadratic attention complexity and context window constraints. Existing retrieval-based approaches typically rely on supervised learning from static keyframe annotations. However, these label priors often fail to align with the actual information required by downstream MLLMs for complex reasoning, creating a misalignment between the training target and inference needs. To bridge this gap, we propose a probabilistic framework that reformulates frame selection as latent-variable inference. We first initialize a lightweight policy using supervised learning to capture general visual saliency. Then, we treat a frozen MLLM as a task environment and use its answer likelihood as dense task evidence to refine the policy via Bayesian Group Relative Policy Optimization (GRPO). Within this formulation, the negative log-likelihood (NLL) over ground-truth answer tokens provides a principled dense reward, while a prior-matching KL term preserves semantic consistency with the elicited label prior. This process transitions the selection principle from static label priors to task evidence. Extensive experiments on Video-MME, MLVU, and LongVideoBench demonstrate that our selector achieves competitive accuracy with MLLM-based scorers while retaining the inference efficiency of lightweight methods. The selector is trained once with a frozen MLLM environment and transfers directly to multiple downstream MLLMs without retraining. Code is available at \url{this http URL}.

---


### 278. [Mixture-of-Memories: Low-Overhead Language Modeling with Modular Knowledge Injection](https://arxiv.org/abs/2610.25425)

**<font color=#1a73e8>作者：</font>** Yifan Lu, Rubin Wei, Ziyun Zou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models store substantial factual knowledge in their parameters, yet this knowledge is difficult to control, update, and reliably elicit at inference time. Existing memory-augmented approaches typically rely on a single auxiliary mechanism, such as retrieval, parameter updates, or neural memory, and therefore apply the same form of correction to tokens with very different knowledge demands. We propose Mixture-of-Memories (MoM), a memory-augmented language modeling framework that separates routed neural memory from writable factual memory. MoM combines a frozen base LM with two neural memory experts: a latent memory that provides low-latency hidden-state corrections and a lexical memory that provides a token-space knowledge pathway. A lightweight Budget Router sets per-token mixture weights from uncertainty and disagreement features, replacing the fixed interpolation of prior memory modules. For post-hoc updates, an external explicit memory stays outside the router, because a router trained before facts are written learns to down-weight it; new facts are appended without retraining any component and used only when an answer-level gate accepts the retrieved fact. Experiments across language modeling, factual QA, update analysis, and efficiency show that MoM improves both predictive accuracy and updateability while retaining low inference overhead.

---


### 279. [MOSAIC: Multi-Objective Search for Allocating Inference Cache Across LLM Decoder Layers](https://arxiv.org/abs/2610.25431)

**<font color=#1a73e8>作者：</font>** Sravanth Kodavanti, Manjunath Arveti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Key-Value (KV) cache is the main memory bottleneck of long-context LLM inference. Token eviction methods such as SnapKV, H2O, AdaKV and L2Norm shrink it, but they give every transformer layer the same budget, although layers differ in which tokens they need. We present MOSAIC, a multi-objective neural architecture search that learns per-layer KV-cache budgets for any eviction method. One search maps the trade-off between average budget and task score; its best allocation transfers to every target budget without further search, and an optional budget-constrained search refines it. Across four eviction methods on Llama-3-8B-Instruct and Mistral-7B-Instruct-v0.2, MOSAIC beats uniform allocation in 146 of 154 (task, method, budget) settings, by up to +48 points on RULER and +11.9 on LongBench (LCC). On both models, it reaches the score of uniform allocation with up to 4x less KV cache (75% smaller). Against EvolKV, MOSAIC explores a ~10^40 x larger search space with 4x fewer evaluations and 18% fewer GPU-hours per budget, and scores higher in 5 of 6 settings. The learned allocations consistently favour a small set of middle layers.

---


### 280. [Design Considerations in Low-Resource Archival OCR: A Case Study in Lakota](https://arxiv.org/abs/2610.25440)

**<font color=#1a73e8>作者：</font>** Téa Wright, Laura X. Ma, Claudia Iron Hawk 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building and expanding access to digital archives supports language reclamation and creates lasting resources for community revitalization. Designing effective tools to support these efforts requires taking into account the community-, language-, and document-specific context. We investigate how small ($\leq$3B) vision-language models (VLMs) can be adapted as optical character recognition (OCR) tools for Lakota, a North American Indigenous language. In addition to benchmarking modeling approaches, we inspect four practical facets of low-resource archival OCR that arise in previous work and conversations with community members: constrained training budgets, segmentation noise, scan degradation, and orthographic variance. We demonstrate that fine-tuning VLMs for OCR post-correction on 35 pages of transcribed data decreases character error rate (CER) from 17.1 to 3.9\% on a bilingual corpus, and find that training only with nine pages increases CER by only 1.1\% over this. However, evaluating under realistic automatic segmentation nearly doubles the CER of the best-performing models, stressing the importance of taking realistic use cases into account. We hope this work encourages future research on developing language technologies grounded in the workflows and constraints of ongoing revitalization efforts.

---


### 281. [Stepwise Reasoning Verification: Don't Generate, Classify!](https://arxiv.org/abs/2610.25441)

**<font color=#1a73e8>作者：</font>** Yifei Shi, Michalis Korakakis, Rami Aly 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifying the reasoning of large language models is increasingly important as they are applied to complex mathematical and scientific problems. Existing work focuses on large decoder models and reports mixed results for generative and discriminative verifiers, leaving unclear which paradigm is more effective and whether large models are necessary. In this work, we cast stepwise verification as a natural language inference task: the problem and partial solution prefix form the premise, while the next reasoning step serves as the hypothesis to be classified as entailed or non-entailed. This formulation enables error localisation at individual reasoning steps and direct comparison of encoder classification, decoder classification, and decoder verdict generation across model scales and annotation budgets. Across five reasoning datasets, a 0.15B encoder classifier outperforms most generative verifiers with up to 4B parameters. On identical decoder backbones, classification outperforms generation from 0.5B to 4B parameters and matches it on the strongest 7B backbone---reaching comparable performance with roughly one tenth as many annotated problems. Our findings establish classification as a parameter- and data-efficient approach to stepwise verification and show that strong verification does not require large generative decoders.

---


### 282. [Enhanced Masked Diffusion Unlearning](https://arxiv.org/abs/2610.25447)

**<font color=#1a73e8>作者：</font>** Tomer Garber, Tom Tirer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) generate text by iteratively unmasking tokens with bidirectional context. As these models reach real-world deployment, machine unlearning becomes essential. This process aims to remove the influence of a designated "forget set" without retraining from scratch, so that sensitive, copyrighted, or restricted content can no longer be elicited while preserving retained capabilities. Masked Diffusion Unlearning (MDU) is the first publicly available unlearning method customized for these models: it tunes the model $p_\theta$ to match a frozen prompt-masked anchor $p_{\mathrm{anchor}}$ on the forget set by minimizing the anchor-last divergence $\mathrm{KL}(p_\theta \Vert p_{\mathrm{anchor}})$. We identify two failure modes of MDU. First, random answer masking can leave key forget tokens visible to the anchor even when the question is fully masked. Second, at a memorized (near-one-hot) prediction, the anchor-last logit gradient vanishes while the anchor-first divergence $\mathrm{KL}(p_{\mathrm{anchor}} \Vert p_\theta)$ logit gradient does not. As a result, MDU training stalls on the tokens we most need to forget. Backed by theoretical and empirical analyses, we propose Enhanced Masked Diffusion Unlearning (EMDU): anchor-first KL divergence toward a frozen anchor whose entire answer span is masked. On TOFU and RWKU benchmarks using LLaDA-8B and Dream-7B, our EMDU matches or exceeds the forgetting of MDU and adapted AR baselines, while better preserving retain utility.

---


### 283. [System X: An LLM Decision Model That Replies from Its Own KV Cache](https://arxiv.org/abs/2610.25456)

**<font color=#1a73e8>作者：</font>** Syed Usama Khalid Bukhari, Syed Safwan Khalid, Muhammad Aamir  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models return probabilities over supplied options, but a deployed agent may also need to reply in words. The present study introduces System X, a large language model (LLM) decision model that adds a text-reply option to the LLM-as-Jev readout. When this option wins, or confidence is low, the same model continues from the decision's key-value (KV) cache, avoiding a repeated prompt prefill. Qwen3-0.6B has been fine-tuned with LoRA on Reason-9k and Bitext reply rows. JevBench accuracy shows no statistically significant change (55.4% to 54.5%, p=0.87), while expected calibration error falls from 0.292 to 0.169. Held-out Bitext routing accuracy reaches 98.3%. Cache reuse saves 15-37% of latency on an Apple M4 Pro, with token-identical replies in the FP32 demonstration cases. Scoring options on copies of the prompt cache matches full-sequence scoring to within 1.4e-6 in probability. Adding dialogue, industry and complaint data (System X+) improves support-task results but lowers IFEval accuracy from 55.5% to 45.0%. System X v4 uses Qwen3-1.7B, rebalanced data and teacher-rewritten reply targets. Against its base LLM, JevBench accuracy rises from 55.0% to 61.0% (p=0.04), with no statistically significant IFEval change (p=0.71). A matched latency test on unadapted Qwen3-1.7B saves 17-39%. One LLM judge prefers v4 replies to an unadapted 1.7B second call (31 to 11 pairs, p=0.003); the other's preference is not significant. These reply comparisons also differ in prompts and generation limits. State conflicts and unsupported reply details remain failure modes. Further studies with several seeds, human raters and real support data are recommended.

---


### 284. [Quality-Controlled Reply and Summary Data for Post-Training Small Language Models in AI Call-Screening Agents](https://arxiv.org/abs/2610.25458)

**<font color=#1a73e8>作者：</font>** Jiaqi Gan, Tsang Ng, Ankit Raj 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models have improved to the point where a phone can plausibly screen its own calls, answering on an absent owner's behalf without sending call content off the device, a privacy-respecting alternative to cloud call handling. Realizing that promise takes a model that can do two things well: reply within the owner's authority during the call, and afterward tell the owner what happened and what needs attention. Released small models do neither reliably - they raise unwarranted alarms about ordinary callers and write summaries that drop material conditions or report a caller's claims as fact - and real calls supply no reference replies or summaries to learn from. We construct supervision for both tasks from synthetic calls under an information-boundary constraint: a caller writer works from a private scenario brief, a reply writer sees only the conversation up to the current turn, and a summary writer sees the completed transcript. Separate model-based reviews of the full dialogue and the summary decide which calls enter training, yielding a corpus of 3,395 calls with 15,102 targets (11,707 reply, 3,395 summary). Training a single shared LoRA adapter on both tasks, we evaluate six models (0.6-4B parameters) before and after adaptation on 192 held-out calls. Reply qualification rises from 21-54% to 94-97% and summary qualification from 0-6% to 43-72%; all twelve paired gains (six models x two tasks) have bootstrap intervals above zero, and the summary gains hold in every source family. Because one model both screened the training data and scored the outputs, these rates measure agreement with that evaluator's standard rather than human acceptance, which a planned human study will test. After adaptation, coherence and naturalness failures nearly vanish, leaving grounding and usefulness - faithfully tracking who said what, under which conditions - as the remaining challenge.

---


### 285. [DiaLong: Benchmarking Reminiscence in Long-Context Dialogues](https://arxiv.org/abs/2610.25463)

**<font color=#1a73e8>作者：</font>** Owen Bianchi, Samer Aslan, Ryunosuke Saito  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How well can transformer-based Large Language Models (LLMs) retain and recall memories in long contexts of dialogue? LLMs are known to forget long-range factual information in their context, yet the field lacks a comprehensive benchmark to quantitatively assess these shortcomings. We present DiaLong, a long-context dialogue dataset and accompanying memory task that standardizes evaluation in this space. It consists of 100 unique conversations created by humans and then augmented with LLMs, extending beyond lengths found in existing datasets. Our selected memory task is fact recall: classify 40 candidate facts about a dialogue as true or false. This task directly probes the model's ability to actively retain and retrieve information, serving as a critical measure of memory within extended conversational contexts. In testing both the latest LLMs and proposed memory enhancements on DiaLong, we demonstrate that more work needs to be done to enable LLMs with better memory performance. By enhancing memory capabilities, LLMs can improve in maintaining coherence, relevance, and human-like interaction over extended conversation. Improving these capabilities will help LLMs fulfill diverse user needs and expectations in various conversational scenarios.

---


### 286. [A failure of Imagination: VLMs fail to use visual representations for text, but self-distillation can help](https://arxiv.org/abs/2610.25470)

**<font color=#1a73e8>作者：</font>** Shashwat Singh, He He, Tal Linzen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language (VL) models are typically built by fine-tuning a language model to attend to visual features in service of a Visual Question-Answering objective. We ask whether this alignment changes how language models represent text---especially on tasks where visualization would help, like geometry questions posed in words. We distinguish weak multimodality (the model can answer questions about an input image) from strong multimodality (the model's text representations themselves become vision-aligned, improving performance on text-only tasks with latent visual structure). To test for strong multimodality, we construct a task of shape-counting problems with paired equivalent text and image specifications. This task is trivial when the image is provided, but requires visualization when specified in text as line coordinates. We compare instruction-tuned Qwen-2.5 and Mistral models against their vision-aligned counterparts on the text variant of the task. We find that the multimodal models do no better in this setting, despite strong performance on the image version of the task. Probing experiments corroborate this: vision-aligned decoder embeddings carry no more visual structure than their text-only counterparts. Finally, we provide an optimization objective that distills in-context visual embeddings into text embeddings. This alignment induces gains on the text variant of the task without explicit task supervision, even on samples more complex than seen during alignment. This suggests that VQA-style alignment leaves available cross-modal transfer untapped.

---


### 287. [P(Yes): 15$\times$ Improvements via Test-Time Scaling of Decision Models](https://arxiv.org/abs/2610.25474)

**<font color=#1a73e8>作者：</font>** Lev Stambler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models answer typed questions, such as multiple-choice or yes/no questions, with a probability for each option. We add test-time search to frozen decision models, with no training: we show the model a complete proposed answer, read off its probability of saying "Yes" to the proposal's correctness, and search for answers that it rates higher. The search is done either by editing one answer at a time or by joint optimization, which changes several answers at once. Search raises accuracy for every model and test set we tried, and the gains are largest for exact correctness on logic puzzles, where every answer in a task must be right. On 128 such puzzles, it takes Qwen3.8-27B from 2 to 30 exactly correct puzzles ($15\times$) and its per-blank accuracy from 27.8% to 48.5%. On a shared set of 47 puzzles, searching over each model's own Yes/No score raises the per-blank accuracy of StartLux Instant, Perplexity Decider, Clef, and JEV, which we reach only through its public API, by 4.0 to 13.0 percentage points, and raises the number of puzzles they get exactly correct, out of 47 and averaged over three search seeds, from 10 to 35, 9 to 26, 2 to 11, and 9 to 31.7 respectively.

---


### 288. [Test-Time Scaling of Text-to-Image Flow Matching Models with Noise-Rejuvenated Sequential Monte Carlo](https://arxiv.org/abs/2610.25479)

**<font color=#1a73e8>作者：</font>** Wenyi Lian, Zheng Zhao, Thomas B. Sch{ö}n  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time scaling of diffusion models with sequential Monte Carlo (SMC) has become a promising strategy for sampling under user-specified rewards, such as human preference scores. However, the standard SMC framework typically relies on stochastic proposals and therefore does not directly transfer to flow matching models, in which inference is governed by deterministic ODEs. In this work, we introduce noise-rejuvenated SMC, an inference-time scaling method tailored for text-to-image flow matching models. Our key idea is to perturb each resampled particle by changing its source noise and constructing a new intermediate state using its current endpoint estimate. This moves the particle to another state that remains representable under the flow-matching interpolation form, enabling particle exploration without converting the sampler to an SDE. We further introduce a look-ahead mechanism to refine resampled particles before weighting. Experiments on Stable Diffusion 3, FLUX.1-dev, and Z-Image demonstrate consistent improvements in reward-guided generation, while ablation studies validate the contributions of noise rejuvenation and look-ahead refinement. Code is available at this https URL.

---


### 289. [Consistent LLM Call Handling Across Java Frameworks: A Reference Implementation and Benchmark](https://arxiv.org/abs/2610.25480)

**<font color=#1a73e8>作者：</font>** Oleksandr Klymenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Java applications reach large language models (LLMs) through an integration framework, and rely on it to handle a failing provider: to retry what can be retried and nothing else, to wait as long as the provider asks, never to present a truncated answer as complete, and to record each failure in the application's metrics. We state these expectations as a six-clause reliability contract and measure Spring AI 2.0.1 and LangChain4j 1.21.0 against it with a scripted OpenAI-compatible provider: fifteen failure scenarios, synchronous and streaming, three repetitions. LangChain4j meets it in 47 of 77 applicable cases with its defaults and in 51 of 83 when configured explicitly, Spring AI in 72 of 77 and 76 of 83; both deliver a stream that ended without its terminator as a complete answer. We then place one implementation of the contract beneath both frameworks, at the HTTP boundary - an OkHttp interceptor for Spring AI, an HttpClient for LangChain4j, and a this http URL transport for code without a framework - sharing a 725-line core that depends only on the JDK and the Micrometer Observation API. With it, all three clients behave identically and meet the contract in 90 of 91 cases; the remaining case is a policy trade-off between retrying a hung provider and waiting for a slow first token. Against a local model server the layer rejected none of 700 calls, and it adds a median of 32-217 microseconds to a call.

---


### 290. [PRIMA: Pose Refined Inductive Motion Adapter for Zero Shot Social Bodily Behavior Recognition](https://arxiv.org/abs/2610.25482)

**<font color=#1a73e8>作者：</font>** Mingcong Ding, Babette Bühler, Tim Fütterer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing fine-grained bodily behaviors, such as self-grooming, postural shifts, and backchanneling, is a useful intermediate step for computational social signal analysis. But the behaviors that matter vary across social contexts, and retraining a model for each new taxonomy is expensive. Vision-language models (VLMs) can adapt to new categories through text prompts, yet they lack sensitivity to body structure and often confuse subtle postural distinctions. We propose PRIMA (Pose Refined Inductive Motion Adapter), a lightweight module that injects a body-structure prior into frozen VLMs using human pose as a training-time supervisory signal, requiring no pose input at inference. PRIMA separates a model-specific projection head from a shared core that encodes transferable body-configuration knowledge; adapting to a new VLM requires retraining only the head. We train PRIMA on a micro-action dataset and evaluate entirely through zero-shot prompting. The adapter improves recognition on its training domain, transfers to additional VLM backbones at different scales with the core frozen, and generalizes to two unseen target datasets from social psychology and daily activity recognition. In a supporting downstream study, the improved behavior predictions also yield higher correlations with human ratings of rapport and dominance in a collaboration context. Within the scope of the tested models and indoor datasets, the results indicate that pose-guided training can produce body-structure priors that generalize across unseen behavior vocabularies and can be partially reused across VLM backbones while preserving RGB-only inference.

---


### 291. [GroundedVDR: Grounding Video-to-Web Evidence Dependencies in Video Deep Research](https://arxiv.org/abs/2610.25493)

**<font color=#1a73e8>作者：</font>** Xiyuan Liang, Yu Wang, Zuhao Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large multimodal models have improved at identifying cross-frame visual evidence and conducting open-web retrieval, as reflected in recent video deep research (VDR) benchmarks. However, existing VDR benchmarks primarily evaluate tool-use trajectories and final responses without verifying whether a model actually uses the temporal video information or the retrieved web evidence. To fill this gap, we introduce \method{}, an evidence-grounded benchmark with three features. First, it combines human review with restricted-access probing across multiple models to exclude questions answerable from parametric knowledge or a single information source. Second, each question carries structured video-to-web evidence annotations that link the relevant video segments to their supporting web evidence. Third, its evaluation protocol separately scores video grounding, web evidence grounding, and final-answer correctness. Across eight multimodal agent systems, the best reaches 76.0\% answer accuracy, yet none recovers the complete required web evidence for more than 8\% of questions. Our benchmark is publicly available at \url{this https URL}.

---


### 292. [Self-Distillation for Supervised Fine-Tuning](https://arxiv.org/abs/2610.25497)

**<font color=#1a73e8>作者：</font>** Wenxuan Zhu, Bang An, Shuming Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning treats the expert demonstration or gold response as a one-hot target, suppressing valid alternative continuations that the model would otherwise assign probability to. We propose Gold-Conditioned Distillation (GCD), a method that turns expert demonstrations into model-native supervision. GCD uses one model as both teacher and student: the teacher conditions on a prompt containing the gold response in context, the student conditions on the original prompt as at inference, and the student is trained to minimize the forward KL divergence to the teacher's next-token distribution at each gold response token. This lets the model use its prior knowledge to teach itself the new task: correctness is anchored by the gold response, while the soft target preserves plausible alternatives. Across various training tasks on Qwen and Llama models, GCD improves new-task accuracy over SFT and generally reduces degradation on general benchmarks.

---


### 293. [Formal Raising: Embedding Verifiable Ethical Properties into the Development of AI](https://arxiv.org/abs/2610.25501)

**<font color=#1a73e8>作者：</font>** Rolf Drechsler, Christina Plump  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Alan Turing proposed constructing a ``child machine'' and educating it rather than directly programming an adult-like intelligent machine. Recent work on model raising revives this developmental view for Large Language Models by arguing that moral values should accompany capability acquisition from the beginning rather than be added only through post-hoc alignment. This paper proposes Formal Raising (FR): selected moral values are represented as explicit, machine-checkable properties that participate in development, evaluation, and action selection. We present a C-based reasoning framework in which candidate actions are evaluated against prioritized ethical properties. Conflicts are resolved w.r.t. a given order, strict rules are non-defeasible, and underdetermination is reported explicitly. Exceptions are not encoded as special cases but emerge from the comparison of alternatives. We provide examples that cover conflicts involving life, truthfulness, harm, privacy, autonomy, and strict rules. We outline a property layer inspired by a Property Specification Language (PSL) for state and temporal requirements and discuss its integration into a raising process.

---


### 294. [From Seeing to Reporting: A Theory of Reliable Visual Set Generation in Vision-Language Models](https://arxiv.org/abs/2610.25503)

**<font color=#1a73e8>作者：</font>** Junzhe Shi, Yuan Gan, Shida Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are asked to report what they see: to count objects, box them, parse a screen or pick a click target (GUI grounding). We argue that reporting is part of the visual task, not merely its formatting. In a dense scene with 173 shapes, GPT-6.1 lists 173 records that match every shape, yet the counts it states in the same response sum to 188. From Seeing to Reporting (FSR) is a theory of visual reporting and a set of inference-time procedures that improve the reports of frozen VLMs. It models reporting as a chain from responses to decoded records, constructed sets and task answers, linked by task-compatible matching. The chain gives exact relations for deleting records, averaging their coordinates and switching readouts, and it splits the error of one answer chosen among several calls into missing candidates, lost representatives and wrong choices. These relations guide procedures for counting, detection, document layout, screen parsing and GUI grounding that use the task specification and a shipped configuration, without requiring labels from the target task. On 50 dense synthetic scenes, a one-call reporting-and-decoding protocol cuts per-type count error by 85.2% for GPT-6.1 and 98.8% for Claude Sonnet 5.5. On 600 ScreenSpot-Pro items, a GUI-grounding tier that combines three models lowers the miss rate from 13.67% for GPT-6.1's two-stage zoom to 9.33%, against 12.67% for three such zooms combined by a cluster vote at about the same cost. A plain vote over the same three models misses 12.33%: the other models supply the candidates, and selecting among them turns those candidates into fewer misses. We release the protocols, the stored responses and the analysis code.

---


### 295. [Where Are Language-Specific Features Represented in Multilingual LLMs? Everywhere](https://arxiv.org/abs/2610.25505)

**<font color=#1a73e8>作者：</font>** Mikaela Martins, Jonathan Dunn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Previous work has argued that multilingual LLMs encode language-specific features most strongly in their initial and final layers, implying that intermediate layers support language-agnostic representations. This paper reconsiders this finding by performing four different experiments: three that undertake a fine-grained analysis of representations of Portuguese and Spanish, two closely related languages, and one large-scale language identification experiment that covers over 200 languages. The results of these experiments challenge the strict separation between language-specific and language-agnostic layers in multilingual LLMs, using Llama 3.2 1B as a test case. By analyzing and manipulating contextual sentence embeddings, we demonstrate that language identity remains strongly recoverable throughout the model rather than being restricted to initial and final layers. Moreover, we find that the model tends to classify ambiguous strings as closer to Spanish than to Portuguese, revealing a skew in model behavior that differs from human judgments.

---


### 296. [Bud ContextCompact 2.0: Context Compaction for Agent Success and Accuracy with Small Language Models and Constrained Context Windows](https://arxiv.org/abs/2610.25516)

**<font color=#1a73e8>作者：</font>** Jithin VG, Ditto PS  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents that work for many turns outgrow the context window of the model that serves them, and on small language models (SLMs) and constrained inference systems that window is small. Context compaction replaces older turns with a summary so a session can continue, but it is lossy, costs a model call, and can help or hurt depending on when it runs. We describe Bud ContextCompact 2.0, the compaction built into the Bud agent runtime, and evaluate it in two settings. On recall questions over recorded agent sessions, compaction to a 16K budget raised a 1.2B-parameter model's accuracy to 0.335, from 0.247 with truncation and 0.176 with its full 32K history (p < 0.001), and raised a 9B model from 0.515 (truncation) to 0.577 (p = 0.04). On 100 SWE-bench Verified tasks run end to end by a 27B reasoning model on a 49K-token window (556 graded sessions), compaction raised the resolve rate on long sessions from 41% to 53% (+12.3 points, 95% CI +1.6 to +23.0, McNemar p = 0.043), left short sessions unchanged, and used 13% fewer tokens per solved task at equal total cost. The main failure without compaction was not the history overflowing but a reasoning turn exhausting the room the history left. The gain has limits: it vanished under a 45-minute session budget, because each summary took a median of 161 s, and in a threshold study it appeared only when compaction triggered early enough to leave room. An 8B model submitted after about ten turns at 5-8K tokens and never needed compaction. We argue that the accuracy results transfer across hardware, including CPU inference, for an equivalent model and window, while the time cost scales with the hardware and must be budgeted for.

---


### 297. [ATEST: Adaptive Resource-Aware Test-Time Scaling for LLM Inference](https://arxiv.org/abs/2610.25519)

**<font color=#1a73e8>作者：</font>** Mobina Kashaniyan, Ali Jannesari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling (TTS) improves large language model (LLM) reasoning by sampling multiple answers, but fixed sampling budgets ignore both query difficulty and the changing energy cost of inference under GPU contention. We measure up to a 4.1-fold increase in energy for the same four-sample query as GPU load rises. We present ATEST, a resource-aware TTS framework that jointly considers the expected value of additional samples and their current GPU cost. ATEST-Online, its default mode, requires no offline calibration: it incrementally generates samples, estimates the stability of the plurality answer, monitors live GPU conditions, and learns step energy cost online to decide when to stop. ATEST-Calibrated instead selects a per-query budget using offline accuracy and cost models, favoring deployments with stable loads. We evaluate both modes on four reasoning and question-answering datasets using Phi-3-mini on an NVIDIA A100 under controlled varying load, and test transfer to an NVIDIA L40S and Qwen2.5-3B. Across the four A100 datasets, ATEST-Online answers every query without exceeding the energy budget, while achieving the highest or statistically tied accuracy and reducing sampling as load increases. On GSM8K at high load, it achieves 60.0% accuracy with no deferrals, versus 44.0% accuracy and 42.4% deferrals for ATEST-Calibrated. Ablations show that online cost learning drives adaptation to load. Including offline profiling, ATEST-Online uses 42 times less GPU time and 48 times less energy than ATEST-Calibrated for the evaluated workload. Online control trades higher tail latency and lower throughput on short tasks for robustness under varying load; offline calibration remains competitive under stable conditions.

---


### 298. [When Empathy Misses the Goal: A Benchmark for Goal Displacement in LLM Advice](https://arxiv.org/abs/2610.25522)

**<font color=#1a73e8>作者：</font>** Dean Ariel, Guy Laban  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conversational large language models can respond with warmth and reassurance while failing to advance the user's stated goal. We conceptualize this failure as $\textbf{goal displacement}$, the substitution of persona-maintenance content for goal-relevant substance. To measure it, we introduce $\textbf{GDB}$ (Goal Displacement Benchmark), comprising 230 scenarios across nine domains and $4{,}134$ human-scored responses from 18 models. A $2 \times 2$ taxonomy crosses hard constraints with emotional distress, distinguishing failures to confront infeasible goals or combine empathy with practical guidance from reverse displacement, where unsolicited problem-solving replaces requested emotional support. A deletion-test rubric assesses whether substantive help remains after purely supportive sentences are removed. Independent raters achieve weighted $\kappa = 0.82$ against author scores for displacement severity. Trap displacement ranges from $0.0\%$ to $37.7\%$ and is strongly negatively correlated with Chatbot Arena Elo ($\rho = -0.706$, $n = 15$). Reverse displacement reaches $41.9\%$, including substantial rates in models with negligible trap displacement. A factorial probe supports a distinction from social sycophancy. Human-scored responses in the high-complexity, low-pressure condition exhibit $35.0\%$ sycophancy but $7.5\%$ displacement, with little association between the constructs. Matched OLMo-2 checkpoints show that mixed empathy-with-constraints displacement remains at $52.3\%$ after supervised fine-tuning and falls to $13.8\%$ after direct preference optimization. GDB provides a reproducible diagnostic of whether responses advance the operationalized user goal, supporting model comparison, post-training evaluation, and regression testing. We release the dataset, annotations, and rubric under CC-BY-4.0 and the evaluation code under MIT.

---


### 299. [StopLoss: Teaching Agents to Predict Failure and Stop Early](https://arxiv.org/abs/2610.25525)

**<font color=#1a73e8>作者：</font>** Jiarong Liang, Xueguang Ma, Dongfu Jiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents keep working on runs that will fail verification, and asking a frontier model to watch for this is expensive in its own right. We introduce StopLoss, a small external monitor that learns failure recognition from completed trajectories and their verifier outcomes. The name is inspired by the stop-loss order in finance: StopLoss ends a run early when the run is likely to fail, which saves resources. Final outcomes label earlier local windows, so a fine-tuned language model can score the most recent tool steps in a single forward pass, and a threshold calibrated on successful runs turns that score into an abort decision without changing the executor. Trained on GPT-family SWE-rebench trajectories and evaluated on SWE-bench Verified and a SWE-bench Pro subset with GPT and Claude executors, StopLoss is compared against six general-purpose judges reading identical windows. Outcome supervision lifts failure prediction from near chance to a useful signal at the first check, at one to two orders of magnitude lower cost per check than any tested judge. This translates into savings: relative to completing every task, StopLoss lowers cost per retained solve by 4.5\% on Verified while preserving 99\% of successful runs, and by up to 31\% on the costlier Pro subset, reaching 48\% with a Qwen3-8B backbone, and in all four settings its cost per retained solve is below that of every judge policy. Outcome-trained small monitors can make failure recognition cheap enough for early stopping to pay for itself.

---


### 300. [Auditing Tool Traces in Agentic LLMs: Source Localization and Counterfactual Dependence Testing](https://arxiv.org/abs/2610.25540)

**<font color=#1a73e8>作者：</font>** Junhao Liu, Tianxiao Li, Yongxian Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic LLMs increasingly support scientific prediction by grounding decisions in external evidence. In biology, they promise accurate, interpretable predictions for important problems by integrating complex experimental and computational evidence. However, serialized tool results can contain hidden label shortcuts, such as dataset identifiers or template artifacts, that create apparent success without biological reasoning. To address this risk, we introduce a two-stage audit. Stage 1, Per-Tool TF-IDF Decomposition (PT2D), localizes label-predictive patterns to individual tool results while avoiding signal dilution in the concatenated tool trace. Stage 2, Token-Class Redaction, counterfactually tests whether the frozen LLM depends on the localized shortcut. We apply this audit to TCR-pMHC binding, where tool augmentation substantially outperforms a no-evidence baseline. At face value, this suggests that the LLM has learned to use scientific evidence. The audit overturns this interpretation: PT2D localizes the strongest signal to identifiers in one tool result, and redacting them reduces performance to chance. These findings show how hidden label shortcuts can masquerade as scientific reasoning or discovery, motivating source-level audits before benchmark gains are trusted.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
