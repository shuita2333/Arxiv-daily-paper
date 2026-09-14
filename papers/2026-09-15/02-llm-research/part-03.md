# 🧠 大模型相关研究 | 2026年09月15日

> 本类共 **134** 篇论文：已确认 **130** 篇，待复核 **4** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-134**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-134**

---

### 101. [K-Bench: A Benchmark for LLM Unlearning in Agentic Deployments](https://arxiv.org/abs/2609.12808)

**<font color=#1a73e8>作者：</font>** Guangsheng Yu, Yanna Jiang, Qin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unlearning benchmarks such as TOFU and MUSE certify forgetting by reading the model's final answer, where a model that refuses to answer already counts as having forgotten. We show that this model-level certificate does not transfer once the model is deployed as an agent. We introduce K-Bench, a benchmark that scores LLM unlearning under agentic deployment. K-Bench inspects all six channels a ReAct agent exposes, including its chain-of-thought (CoT), tool calls and tool observations, and elicited summary. A query counts as leaked if the secret appears in any of them. Each experiment places the secret in exactly one of the agent's three sources (the weights, the prompt, or the retrieval store). The K-Score is computed separately for each source and credits forgetting only when the agent remains usable. Clearing the answer channel does not make the secret unrecoverable. On structured retrieval, the secret stays verbatim in the tool-observation channel and the aggregate leak rate is unchanged. When the secret lives in the prompt or the retrieval store, TOFU and MUSE report no leakage, while the deployed agent still leaks it on 22--86\% of queries. When the secret is in the weights, none of the twenty evaluated published methods demonstrably removes it, and only an input-corruption intervention reaches selective forgetting under the evaluated observer. The top-ranked method changes across base models. A refusal-tuning method resists the evaluated extraction without verified knowledge removal.

---


### 102. [Online Video Agent Harness for Long Video Understanding](https://arxiv.org/abs/2609.12818)

**<font color=#1a73e8>作者：</font>** Sen Yang, Boqiang Duan, Jing Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding often behaves like a visual needle-in-a-haystack problem: query-relevant evidence is sparsely distributed across long temporal spans, while packing dense frames into a single VLM context incurs \textit{context rot} and high cost. Existing video agents often rely on query-agnostic offline preprocessing or ad hoc tool sets, which can miss query-specific details and waste computation. In this work, we present VideoXAgent, a purely online video-agent harness for long video understanding that starts from the given video file and user query, plans and decomposes the task, invokes specialized expert tools on demand, and aggregates multimodal evidence to produce a final answer while resolving conflicts among observations. To support this on-demand invocation, we design a suite of heterogeneous expert tools guided by a data-driven taxonomy of atomic capabilities, spanning scripts, VLMs, and domain models (e.g., detection, OCR, ASR, face recognition). The harness further enforces objective evidence prompting and budget-aware control to curb hallucination and non-termination. Across Video-MME-Long, LongVideoBench-Long, LVBench, and MINERVA, VideoXAgent is competitive with frontier LMMs and video agents under a smaller context footprint---about 50k tokens of agent context per sample, even on hour-long videos. In particular, on complex video-reasoning benchmarks such as MINERVA, it matches this level while using only about 15\% of the context of a 1,024-frame dense-packing baseline. Notably, the harness remains effective with a visually weak or even text-only orchestrator, suggesting that strong long-video understanding can emerge from progressive agentic evidence seeking rather than from packing the full video into a single context. Project page: this https URL

---


### 103. [Scaling Clinical Judgment to Evaluate Medical AI](https://arxiv.org/abs/2609.12822)

**<font color=#1a73e8>作者：</font>** Thomas A. Buckley, Zahir Kanjee, Peter G. Brodeur 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Blinded physician evaluation has been considered by many to be the gold standard for assessing clinical reasoning in large language models (LLMs). This is difficult to scale; thus, prior studies typically rely on small physician panels, often from a single institution or specialty, which both limits the scientific questions investigated and makes it unclear whether findings would be reproduced with a different set of evaluators. To more rigorously and scalably study clinical reasoning in AI models, here we introduce PrecepTron, an LLM fine-tuned for physician-level evaluation of open-ended responses. PrecepTron was trained using low-rank adaptation (LoRA) of a 32-billion-parameter model on a small number of physician examples. We also release GRAND-ROUNDS, a new large-scale physician-annotated benchmark of 9,217 scores by 11 physicians across seven studies. We show that frontier LLMs in typical "LLM-as-a-judge" approaches often disagree with physicians and with each other, but fine-tuning PrecepTron on a small number of cases enables physician-level consistent scoring across tasks. We use PrecepTron to reproduce headline findings from five influential studies assessing LLMs for clinical care in JAMA, Science, and Nature Medicine without new human grading. Using PrecepTron, we then pose new questions about how LLMs reason in medicine that would have been infeasible with human grading alone, including measuring the diagnostic accuracy of frontier LLMs when clinical cases are provided piecemeal, even token by token. Together, PrecepTron and GRAND-ROUNDS provide a foundation for reproducible, large-scale study of how LLMs reason in medicine. All code, data, and labels are made freely available for researchers.

---


### 104. [Evaluating Context Segmentation in Locally Deployable SLMs for Cybersecurity CTF Tasks](https://arxiv.org/abs/2609.12839)

**<font color=#1a73e8>作者：</font>** Sebastiano Nordio, Michele Lotto  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The proliferation of highly capable open-weight Small Language Models (SLMs) democratizes access to advanced cybersecurity capabilities, posing a escalating risk as these models can bypass proprietary API guardrails when deployed locally. However, SLMs deployed as autonomous agents often struggle with long-horizon, exploratory tasks like cybersecurity Capture The Flag (CTF) challenges due to context bloat and cognitive degradation from accumulated tool-call outputs. To understand and mitigate this cybersecurity threat, we introduce \textit{context segmentation}, a two-level agentic framework that divides complex exploitation tasks into manageable, contextually isolated sub-problems. Evaluating on the \texttt{picoCTF} dataset using memory-constrained \texttt{gemma-4} models, we demonstrate that for the E4B model, our strategy acts as an intelligent search, achieving competitive rewards with superior token efficiency compared to brute-force retries, and successfully solving 18.52\% of tasks that standard agentic execution fails to complete. Code is available at this https URL.

---


### 105. [A Graph-Based Approach for Mapping Kernel-Level Telemetry to MITRE ATT&CK](https://arxiv.org/abs/2609.12841)

**<font color=#1a73e8>作者：</font>** Matteo Lupinacci, Luigi Arena, Francesco Blefari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mapping observed system behavior to standardized frameworks like MITRE ATT&CK is essential for threat-informed defense, but remains largely manual. Existing automated methods depend on Cyber Threat Intelligence reports, which offer only retrospective accounts of attacks. Low-level telemetry, i.e. kernel-level system calls, instead provides evidence of adversary behavior, yet its volume and complexity have limited its use for automated mapping. We present a methodology that collects kernel-level events via eBPF, correlates attacker commands into a provenance graph, and derives compact graph representations suitable for LLM-based reasoning. These representations are mapped to the MITRE ATT&CK framework using both pure LLM prompting and retrieval-augmented generation (RAG) grounded in the ATT&CK knowledge base, producing ranked technique candidates along with supporting rationales. We implement this methodology as an end-to-end pipeline, named Trace2ATT&CK and evaluate it on 347 Linux Atomic Red Team tests using locally deployed open-weights LLMs. RAG consistently improves ATT&CK mapping performance over pure prompting, while provenance graph substantially outperforms raw telemetry. These results show that local inference over graph-based behavioral descriptions can make automated ATT&CK mapping from kernel-level telemetry operationally viable, without compromising data confidentiality.

---


### 106. [MedRoundsQA: A Persona and Difficulty Aware Evaluation for Multi-Turn Medical Consultations](https://arxiv.org/abs/2609.12851)

**<font color=#1a73e8>作者：</font>** Youssef Mohamed, Ahmed Heakl, Qinrong Cui 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical benchmarks are dominated by single-turn, multiple-choice clinical cases that poorly reflect real consultations. Practically, clinicians elicit evidence interactively and patient communication varies widely. We introduce MedRoundsQA, a multi-turn diagnostic benchmark derived from 1,387 board-exam cases across 17 specialties. Each case is converted into a structured 24-slot clinical record, and then instantiated as controlled doctor-patient dual-agent dialogues under varying patient personas, with the underlying clinical content held fixed. We further classify cases by difficulty using model-based uncertainty to enable easy-to-hard analysis. Evaluations of fifteen LLM doctor agents show that (i) moving from a single-turn diagnosis on the standardized records to multi-turn consultations causes large degradations of roughly 13-39 points; (ii) more turns reliably improves question relevance, but diagnostic accuracy exhibits diminishing returns and typically plateaus after 6-12 turns; and (iii) patient persona differences can shift diagnosis accuracy by about 7-8 points (lowest to highest education), highlighting equity risks that single-turn benchmarks miss.

---


### 107. [GenOR-Twin: A Semantic Middleware for Integrating Operational Discourse with Mathematical Optimization](https://arxiv.org/abs/2609.12863)

**<font color=#1a73e8>作者：</font>** Rahimeh Neamatian Monemi, Shahin Gelareh, Lubin Cui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce GenOR-Twin, a neuro-symbolic framework that bridges the translation gap between unstructured operational logs and rigorous mathematical optimization. Our architecture uniquely positions Large Language Models as semantic translators rather than direct solvers, ensuring that the system retains the feasibility guarantees of exact combinatorial methods. { \color{red}We design a dynamic constraint injection mechanism (the runtime translation of qualitative disruption events into formal mathematical constraints) that allows the system to structurally modify the optimization problem's feasibility region in real-time based on qualitative human inputs. The resulting bidirectional coupling---where operational observations update the virtual model state and optimized decisions are reflected back into the Knowledge Graph---satisfies the synchronization requirement of a proper Digital Twin. The framework features an adaptive decision policy} that automatically selects between low-complexity schedule repair and full re-optimization by analyzing the available system slack. Finally, we demonstrate the generalization of this approach across six distinct optimization domains, {\color{red}turning static models into resilient systems that adapt to the operational uncertainty and variability of real-world environments.}

---


### 108. [DuplexDrama: A Synthesized Dialogue Dataset with Scenarios, Full-Duplex Behaviors, Expressive Speech, and Sound Events](https://arxiv.org/abs/2609.12872)

**<font color=#1a73e8>作者：</font>** Qingxiang Guo, Wenke Fan, Shuofeng Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present DuplexDrama, the first synthesized spoken dialogue dataset that simultaneously covers four dimensions: (i) complete persona and scenario settings; (ii) three full-duplex behaviors (interruption, backchannel, incomplete); (iii) expressive speech with persona-aligned emotion labels; and (iv) script-aware sound events. DuplexDrama is built via a 4-stage pipeline; quality validation on both scripts and synthesized audio confirms its quality. We have produced more than 2,000 hours audio data with a 64-voice timbre pool spanning 13 personas and 5 age buckets; 3.8% of all turns carry at least one full-duplex behavior. This data has been validated through internal full-duplex model training. We will release a curated subset of 6,400 bilingual dialogues (800 h, Chinese ~500 h + English ~300 h) to advance full-duplex spoken dialogue model research. Data samples are available at our demo page and LLM-judge evaluation prompts will be released with the dataset.

---


### 109. [Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents](https://arxiv.org/abs/2609.12896)

**<font color=#1a73e8>作者：</font>** Pengyang Zhou, Xiaobin Tu, Zhengxi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-based agents rely on heterogeneous interaction capabilities to accomplish complex tasks. Existing approaches often distribute these capabilities across multiple LoRA adapters, which increases adapter storage requirements and introduces routing overhead during inference. A single LoRA avoids this overhead, but learning from diverse agent trajectories under a fixed rank budget presents two challenges. First, trajectories with different interaction traces and parameter gradients can induce equivalent changes in decision distributions, causing repeated updates to overemphasize redundant behavioral changes. Second, an aggregated update may exceed the rank budget of the adapter, and approximating it in weight space can distort the decision changes that it is intended to produce. We propose BQ-LoRA, a low-rank adaptation framework that organizes trajectory updates through a local behavior quotient manifold. It contains two modules, i.e., behavior quotient balancing (BQB) and decision preserving compression (DPC). BQB constructs the quotient manifold from decision distributions and reweights trajectory update directions according to their local density in the quotient tangent space. DPC projects the balanced gradient onto the intrinsic fixed rank tangent space and refactorizes the resulting target by jointly controlling effective weight error and distortion of decision distributions. Experiments on AppWorld and BrowseComp-Plus compare BQ-LoRA with standard LoRA and recent low-rank adaptation methods, while separate ablations evaluate the complementary contributions of both components.

---


### 110. [Parameter-Efficient Retrievers for Polish and European Languages](https://arxiv.org/abs/2609.12913)

**<font color=#1a73e8>作者：</font>** Sławomir Dadas, Rafał Poświata, Małgorzata Grębowiec 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dense retrieval systems increasingly rely on multi-billion-parameter language models, whose memory and computational requirements make large-scale indexing, frequent corpus updates, and low-latency serving costly. We present a three-stage training pipeline for developing compact and efficient retrievers that remain competitive with substantially larger models. The pipeline combines cross-lingual alignment, relational knowledge distillation, and contrastive fine-tuning. It requires no original ground-truth relevance labels, relying exclusively on supervision generated by strong embedding models and rerankers utilised as teachers. Using this pipeline, we develop PolDense and EuroDense, both supporting contexts of up to 8,192 tokens. PolDense is a family of six Polish retrievers ranging from 17M to 1B parameters. EuroDense is a 435M-parameter retriever supporting nine European languages. We conduct an extensive evaluation covering 41 Polish and 150 multilingual retrieval tasks. The results demonstrate strong quality-efficiency trade-offs. PolDense-1B outperforms the evaluated retrievers with up to 9B parameters, while the PolDense family forms the Pareto frontier across model sizes. Among the evaluated models below 1B parameters, EuroDense ranks first in both task-averaged and language-averaged performance and leads in seven of nine languages. We release all models publicly.

---


### 111. [LLM-Enhanced Dual-Branch Learning for Large-Scale Multi-Label Text Classification](https://arxiv.org/abs/2609.12915)

**<font color=#1a73e8>作者：</font>** Hui Ye, Jing Zhang, Xiulong Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale multi-label text classification assigns a small subset of relevant labels to each document from a vocabulary containing thousands or tens of thousands of candidate labels. Although pretrained language models have improved semantic text representations, most representation-based approaches center their prediction pipelines on a primary encoder or combine auxiliary features within a single ranker. The complementarity between heterogeneous language models therefore remains insufficiently explored. We propose DualMLC, a dual-branch framework that processes the same document through an autoregressive decoder-only language model and a bidirectional encoder. Each branch maintains its own representation pathway and independently estimates relevance scores over the shared label space. DualMLC combines the two score vectors through late logit fusion, allowing shared evidence to reinforce relevant labels and branch-specific evidence to compensate for limitations in the other branch's representation. DualMLC achieves state-of-the-art results on three widely used large-scale multi-label text classification benchmarks. Ablation results further confirm that integrating the heterogeneous predictors produces stronger rankings than either branch alone. The source code is publicly available at this https URL.

---


### 112. [PA-CDM: Position-Aware Character Detection Matching for Evaluating Handwritten Mathematical Expression Recognition](https://arxiv.org/abs/2609.12917)

**<font color=#1a73e8>作者：</font>** Shiliang Luo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten mathematical expression recognition (HMER) is conventionally scored by exact-match rates and string-similarity metrics that are blind to where an error occurs: two predictions with identical token-error counts receive identical scores whether they misplace a subscript or swap the operands of a fraction. Render-based character detection matching (CDM) aligns glyphs robustly but remains position-blind---on controlled fraction-operand swaps it scores 0.8595 where position-aware scoring yields 0.6253. Tree-edit metrics exhibit a complementary blind spot: rewrites outside the parser's normalization coverage are penalized as structural errors (0.8552 where render-based metrics score 1.0). We propose PA-CDM, a position-aware metric that couples character detection matching with position-forest encoding and divergence-level weighting; StructPerturb v2.0, a frozen benchmark of 1,340 controlled perturbation pairs across 15 type--intensity cells; and a cross-metric consistency protocol combining a sensitivity matrix, a human study, and LLM-judge calibration. In a six-annotator study, PA-CDM attains the highest correlation with human judgments among seven automatic metrics (Spearman rho=0.9535, n=990). A frontier LLM judge correlates slightly higher (rho=0.9613) but is costly, nondeterministic, and API-dependent; PA-CDM approaches it at zero marginal cost with deterministic, diagnosable behavior.

---


### 113. [DementiaCare-Bench: A Modality-Validated Video Benchmark](https://arxiv.org/abs/2609.12929)

**<font color=#1a73e8>作者：</font>** Afrouz Sheikholeslami, Yuankai Qi, Xuyun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dementia affects an estimated 57 million people worldwide, and for most families the hardest part of care is not memory loss but the behavioral and psychological symptoms of dementia (BPSD): agitation, wandering, resistance to care, sundowning. Understanding these symptoms requires more than recognizing the behavior itself; it also requires knowing what happened beforehand. The same behavior may call for a different response depending on its trigger. Video-language models (VLMs) could potentially support caregivers, yet no existing benchmark evaluates this capability. To fill this gap, we present DementiaCare-Bench: 56 professionally produced caregiver training videos segmented into 94 clips across nine BPSD categories, with 2023 questions generated by a multi-agent pipeline that grounds every clinical claim in a verbatim transcript span. Each question is then probed under four visual conditions and labelled by the least it requires, so its visual demand is measured rather than assumed. Measurement contradicts intent: we wrote 77.7% of the questions to require ordered frames, and 34.8% do. Across 12 current VLMs the pattern is uniform. The best reach 85% overall, but that average is carried by questions a language model can answer from clinical knowledge alone; accuracy falls by 17 points on average on questions that require the ordered clip, and a leading open model scores at chance on judging whether a caregiver's response was appropriate. A lightweight LoRA fine-tune, DemCare-VLM, moves video dependence from -3.3 to +4.5 points, so what the benchmark exposes can be repaired and not only measured.

---


### 114. [EduFair-Bench: Evaluating Pedagogical Fairness of LLM Tutors Across Student Demographics](https://arxiv.org/abs/2609.12949)

**<font color=#1a73e8>作者：</font>** Jiaxu Zhao, Bahar Radmehr, Fares Fawzi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as tutors, but it is unclear whether they support all students equally well. We introduce \textbf{EduFair-Bench}, a benchmark for auditing the pedagogical fairness of LLM tutors---whether tutoring quality varies systematically with student demographics. EduFair-Bench pairs a multi-domain question bank (mathematics, physics, chemistry) with a controlled simulation in which a fixed LLM student interacts with each tutor across nine demographic levels spanning four dimensions: gender, immigration background, first language, and socioeconomic status (SES). Tutoring quality is scored on five turn-level pedagogical metrics and four conversation-level dimensions, using an LLM judge validated against three-annotator consensus on 180 tutor turns. Bias is measured via paired Wilcoxon signed-rank tests and bootstrap effect-size confidence intervals. Two ablations (demographic cues conveyed through names; conflicting demographic information between tutor and student) disentangle tutor-driven from student-driven bias. Across five tutors, we find that model capability and demographic fairness are largely orthogonal: the smallest model is the most consistent while the four more capable tutors all exhibit wide demographic gaps with no clear capability-to-fairness ordering, pedagogy-specific RL training redistributes rather than removes bias, and language- and immigration-related cues produce larger gaps than gender- and SES-related cues.

---


### 115. [Dimension-Corrected Hitting Times for Heavy-Tailed Spectral Emergence in Neural Optimizer Dynamics](https://arxiv.org/abs/2609.12994)

**<font color=#1a73e8>作者：</font>** Zongmin Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heavy-tailed empirical spectral densities of neural-network weight matrices are widely used as diagnostics of implicit self-regularization, but the step complexity of heavy-tail emergence remains poorly understood. We formulate spectral heavy-tail formation as a right-censored hitting-time problem: a run that does not reach a heavy-tail diagnostic within the observation horizon is treated as censored rather than discarded. In controlled full-batch teacher--student dynamics, we find that the first-step spike--bulk gap alone does not explain onset time. Instead, finite-onset regression supports a dimension-corrected spectral-gap law, (\tau_{\mathrm{HT}}\approx C\Delta_1^{-\gamma}d^\rho), with (R^2=0.683), (\gamma=0.626), and (\rho=0.772) across 330 completed runs. Right-censored lognormal accelerated-failure-time models further favor the dimension-corrected model over a gap-only model, improving AIC from 706.62 to 628.70. Theoretically, we prove that exact early loss dynamics in linear networks do not determine factor spectral tails, that Adam recurrences alone do not imply spectral redistribution, and that projected singular-basis spreading implies contraction of a spectral-tail potential and hence a dimension-corrected hitting-time bound. Empirically, projected-kernel profiles support the sufficient spreading mechanism, Adam and AdamW agree under tested grids, GD and signGD do not reach onset in the same regimes, and real pretrained Qwen2.5-0.5B and Pythia-70M transformer weights show non-Gaussian spectral-tail structure relative to matched Gaussian nulls. The result is a reproducible spectral hitting-time law with rigorous conditional theory, not a claim that Adam necessarily generates heavy tails from first principles.

---


### 116. [Judging by the Cover: Cleaning LLM Truthfulness Benchmarks to Avoid Surface-Level Feature Leakage](https://arxiv.org/abs/2609.13003)

**<font color=#1a73e8>作者：</font>** Foad Namjoo, Remy Ogasawara, Amirali Abdullah 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Binary-choice truth benchmarks ask models to choose between a correct and an incorrect answer, but if the two answers differ systematically in surface-level features, models can exceed chance without performing the intended reasoning. We show that this failure mode is detectable and can be exploited by downstream classifiers. In TruthfulQA, a simple six-feature logistic classifier achieves substantial accuracy in separating correct from incorrect answers. We further show that similar surface-level artifacts are present in additional benchmarks. To counteract this, we developed a general mechanism to clean them by removing the most leakage-reinforcing pairs. We release a version of TruthfulQA with surface-feature leakage reduced close to chance and provide a mechanism, Audit-Prune, so that the datasets can be cleaned before release.

---


### 117. [IntentFuzz: A Protocol-Aware Fuzzer for Automated Invariant Violation Detection in Intent-Based Cross-Chain Bridges](https://arxiv.org/abs/2609.13004)

**<font color=#1a73e8>作者：</font>** André Augusto, Christof Ferreira Torres, André Vasconcelos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cross-chain bridges move value between blockchains. Intent-based bridges are a variant where a solver fulfills a user's declared outcome and an off-chain settlement layer later reconciles the fill against the deposit. Existing smart-contract fuzzers and static analyzers only flag known-bad code patterns or require protocol-specific hand-written assertions. This work formalizes a taxonomy separating invariant violations, safety properties a contract must enforce locally, from settlement exposures legitimately delegated to the off-chain settlement layer, and proposes IntentFuzz: a protocol-aware fuzzer that recovers a bridge's intent structure and deposit/fill function roles directly from unannotated Solidity source, then synthesizes multi-step fuzz sequences using an LLM-based fallback to help build call arguments. IntentFuzz recovers the correct intent structure in 9/9 benchmark protocols and classifies deposit and fill functions with 100% recall and 82% combined precision; across a corpus of 77 manually labeled contracts, it reaches 79.5% bridge-classification precision and 97.2% recall, and among confirmed bridges, struct selection reaches 88.6% precision and recall while deposit and fill classification each reach 100% recall. On 23 planted-bug mutants, IntentFuzz attains 100% recall and 100% precision, executing 273 templates (507 transactions in a median of 14ms per template). Across 24 real-world deployments, it confirms 17 genuine invariant violations under heuristic-only input generation, rising to 22 with its LLM-assisted tier enabled, spanning eight vulnerable GitHub repositories, each finding reproducible against public, deployed bytecode.

---


### 118. [Tasks over Application Manuals: Revealing Gaps in Long-Horizon Procedural Reasoning for Language Models](https://arxiv.org/abs/2609.13005)

**<font color=#1a73e8>作者：</font>** Utkarsh Soni, Syed Shariyar Murtaza, Yifan Nie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved strong performance on a wide range of natural language tasks, and recent benchmarks suggest that they are increasingly adept at multi-hop reasoning. However, these benchmarks are typically short-horizon, requiring only a small number of retrieval or inference steps, and provide limited evidence of reliability on real-world tasks that involve following manuals spanning hundreds of pages with complex, interdependent guidelines. In this paper, we introduce Tasks over Application Manuals (TAM), a benchmark for evaluating long-horizon procedural reasoning. We construct TAM by curating real-world tasks from two domains: ICD-10-CM clinical coding (mapping medical conditions to diagnostic codes) and U.S. federal sentencing (computing crime sentencing guideline outcomes, specifically offense levels), with human-validated labels. Each task requires following an authoritative manual with tens of thousands of rules and executing a sequence of interdependent steps across different sections to produce an exact answer. We evaluate general-purpose prompting approaches, including retrieval-augmented generation, ReAct-style prompting, and an agent-harness baseline on GPT-5, and find that the best exact-match performance remains extremely low: 1% on ICD-10-CM coding and 15.5% on sentencing tasks. These results show that current benchmarks may overestimate LLM reasoning ability and miss a key challenge: reliably following long, rule-based procedures. The complete TAM data and code are publicly available.

---


### 119. [Physics-Aware Video Generation via Agentic Planning and Graph-Guided Optimization](https://arxiv.org/abs/2609.13006)

**<font color=#1a73e8>作者：</font>** Minh-Loi Nguyen, Xuan-Vu Le, Thanh-Toan Do 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion models (VDMs) have demonstrated remarkable capabilities in synthesizing high-fidelity, photorealistic video content. However, they fundamentally lack an intrinsic understanding of physical laws and frequently produce visually appealing but causally illogical sequences characterized by structural hallucinations and physically implausible dynamics. Injecting physical awareness via training-free test-time optimization is a promising alternative, yet existing methods rely on global gradient updates and rigid scheduling heuristics that inadvertently corrupt passive backgrounds and fail to model complex dynamic state changes. To address this, we propose PhysPlan, a novel training-free guidance framework that shifts the paradigm from stochastic visual interpolation to agentic physics simulation. First, a VLM operates as an iterative cognitive simulator, decomposing multimodal inputs into a Chain-of-Visual-Thought to create a multimodal representation of kinematic trajectories and 3D depth geometries. Second, these signals drives an object-centric test-time optimization. Unlike prior training-free methods that rely on global gradients and rigid scheduling heuristics, PhysPlan introduces Object-Centric Gradient Routing to isolate kinematic modifications and completely lock the passive environment. Furthermore, our Kinetic Intensity Profiling dynamically parameterizes framework hyperparameters to accommodate the varying severity of physical deformations. Extensive evaluations on the PhyGenBench and Physics-IQ benchmarks demonstrate that PhysPlan significantly outperforms both foundational and controllable VDM baselines, offering a promising approach for improving the physical understanding of video generation.

---


### 120. [How Good Are Frontier Models at Physics? Expert Re-Grading Reveals Broken Evaluations and Near-Saturation of Leading Benchmarks](https://arxiv.org/abs/2609.13009)

**<font color=#1a73e8>作者：</font>** Ali Ansari, Haoran Sun, Andy Zeyi Liu 等 51 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Low reported scores on leading physics benchmarks, including those featured in the Artificial Analysis Intelligence Index (2026), suggest that frontier language models still struggle with advanced physics, a demanding test of their scientific reasoning and quantitative problem-solving abilities. Yet this impression does not always align with domain experts' experiences using these models in their work. We revisit these reported findings by evaluating frontier models on six widely used physics benchmarks and auditing them with experts, focusing on text-only problems with verifiable final answers. For each subfield of physics, faculty and graduate researchers with relevant expertise carefully review problem statements, reference solutions, and model responses to distinguish genuine model errors from grader errors, incorrect reference solutions, and ambiguous or underspecified questions. Most audited cases initially evaluated as incorrect reflect these benchmarking issues rather than errors in the models' physics reasoning. We then ask experts to address these benchmarking issues by correcting erroneous reference solutions and repairing or excluding flawed questions. We find that GPT-5.6-Sol's measured mean@4 rises from 47.3% to 78.7% on HLE-Physics and from 61.0% to 87.2% on CMT-Benchmark, while its corrected pass@4 reaches 94.4% on the 54 retained CritPt challenges. Corrected scores are computed on the retained evaluation subsets following expert review. Scores on the audited subsets of UGPhysics, PRISM-Physics, and PHYBench also rise substantially after correction. These findings suggest that current benchmarks substantially understate frontier models' ability to solve well-posed physics problems. Near-saturation on these closed-ended tasks highlights the need for more demanding, expert-validated evaluations.

---


### 121. [Pixel Decodability Is Not a Compression Signal: Causally Evaluating Importance Proxies for Visual KV-Cache Eviction](https://arxiv.org/abs/2609.13012)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Qiliang Jiang, Shuning Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models retain a substantial amount of pixel-decodable visual content in their visual key-value cache. We show, in our setting, that this retention is task-inert: across our preregistered tests, how much a unit retains never positively tracks whether the computation that answers the question causally relies on it. We measure retention with a learned pixel-inversion decoder and causal use with single-super-patch KV ablation, the teacher-forced drop in gold-answer log-probability, and relate the two within images under a preregistered, sign-calibrated, held-out design. Retention is decoupled from attention and, in a well-powered null, from causal utilization. Utilization is not inert to every proxy: attention weakly but significantly tracks it, the only signal we find that does and the design's positive control. We characterize pixel-decodable retention as an informational axis of the visual KV cache, orthogonal to the functional one. How much task-inert content a cache holds differs by architecture in our model pair: the encoder-free model retains 2.7 times more than the encoder-based one. The engineering consequence is a controlled negative result. At super-patch granularity, deconfounded pixel-decodable retention ranks KV eviction no better than random; at token granularity it acquires only a weak inverse-importance signal at larger budgets, dominated at every budget by attention magnitude. In our setting, pixel-decodable reconstructability is not a competitive KV-compression signal at any granularity we test.

---


### 122. [Attention Quantization for Tabular Foundation Models](https://arxiv.org/abs/2609.13031)

**<font color=#1a73e8>作者：</font>** Jonas M. Kübler, Benjamin Jäger, Klemens Flöge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the recent rise and adoption of tabular foundation models, optimizing their inference performance becomes an emerging field for efficiency research. While the models are architecturally similar to transformer-based large language models (LLMs), the size and serving patterns differ significantly. We show that the focus should be on the attention calculation and less on weight or KV cache quantization, which are more popular in LLMs. We develop a quantization strategy for queries, keys, and values to FP8 and use explicit FP8 matrix multiplication instructions to speed up the attention calculation. We find that it is crucial to align the quantization error in the test rows with the quantization error in the training rows, as otherwise the accuracy drops drastically. Our Triton kernel achieves a speedup up to 1.7x over regular 16-bit kernels, and we show that on TabPFN-v3 and TabICLv2 there is no relevant accuracy loss across TabArena and BeyondArena.

---


### 123. [Kraken: LLM-based Speech-to-Speech Translation via Low-bitrate VQ and Dual-path Source Conditioning](https://arxiv.org/abs/2609.13045)

**<font color=#1a73e8>作者：</font>** Hayato Futami, Hassan Shahmohammadi, Tushar Dhyani 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech translation (S2ST) has advanced significantly with speech LLMs, offering the potential for joint optimization and preserving non-linguistic information. However, these models struggle with predicting high-bitrate speech tokens in LLMs, and face the challenge of relying on S2ST training data with ideally aligned speaker identity and prosody. We propose using low-bitrate tokens based on single-layer vector quantization, trained to reconstruct self-supervised learning (SSL) features. We also employ a separate token-to-waveform decoder named Autowave-X, which is also conditioned on the source speech to improve non-linguistic transfer, thereby relaxing the training data constraints. With the integration of these techniques, we propose an S2ST model named Kraken, which augments a pre-trained LLM with speech feature inputs and the low-bitrate token outputs, followed by Autowave-X vocoder. We built the model upon Qwen3-8B and trained it using 150k hours of multilingual and multitask speech data. We demonstrated that our model exhibited better translation quality than SeamlessM4T-Large v2 and Qwen2.5-Omni, along with improved speaker and prosody transfer capabilities.

---


### 124. [Expert-Space Exploration in MoE Reinforcement Learning](https://arxiv.org/abs/2609.13058)

**<font color=#1a73e8>作者：</font>** Hongyi He, Zhenghao Lin, Xiao Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has become central to post-training of large language models. Recent advances in RL for Mixture-of-Experts (MoE) models have primarily focused on improving optimization stability and training efficiency, while treating the expert selection as a fixed component. Since routing determines the sparse computation paths that induce output distributions, expert selection offers an additional source of rollout diversity. Through empirical analysis, we find that perturbing expert routing effectively alters model output and increases rollout diversity, which is similar to increasing the decoding temperature. However, direct perturbation can activate unsuitable experts and substantially degrade rollout quality. Motivated by these observations, we introduce Expert-Space Exploration Reinforcement Learning (ESRL), an architecture-aware framework that explicitly explores the expert-routing space of MoE models. ESRL preserves high-confidence experts as anchors, and restricts stochastic routing to a plausible candidate pool, thereby retaining reliable computation paths. The perturbation strength is further adapted according to router entropy to avoid over-perturbation. To mitigate the routing mismatch introduced by perturbation, ESRL records the expert paths used during rollout and replays them during policy optimization. Experiments demonstrate that ESRL achieves the best performance across MoE backbones with top-K, top-1, and shared-expert routing, as well as across mathematics, science, and code tasks without additional sampling or computational cost. Specifically, ESRL on Qwen3-30B-A3B achieves the best among all compared methods, improving average Pass@1 and Pass@8 over GRPO by 3.2 and 4.5 percentage points, respectively. Further analyses of expert utilization and training dynamics provide insights into how exploiting MoE-specific routing structure benefits RL training.

---


### 125. [CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models](https://arxiv.org/abs/2609.13060)

**<font color=#1a73e8>作者：</font>** Blake Olson, Yuhang Song, Emmett McQuinn 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion Language Models (DLMs) offer promising parallel generation capabilities but lag behind autoregressive models in complex reasoning and tool-use tasks. While Reinforcement Learning (RL) has recently been applied to enhance DLMs, standard RL approaches suffer from an exploration bottleneck. To address this, we inject reasoning priors from a stronger teacher model to guide RL exploration. In this paper, we introduce CanvasAnneal, a curriculum-guided diffusion RL framework. During the initial RL phase, we warm-start exploration by injecting teacher-generated reasoning traces into the initial diffusion canvas. As training progresses, we gradually remove this guidance and require the model to generate more of the reasoning trajectory independently. Across mathematical reasoning and tool-use benchmarks, CanvasAnneal improves over standard diffu-GRPO on MATH500, Countdown, and Tau2 and substantially accelerates reward improvement on several tasks, while gains are task-dependent. Our results suggest that structured training-time guidance can alleviate exploration bottlenecks in diffusion RL and speed up convergence on harder tasks.

---


### 126. [Anchoring Clinical Events in Time: UID-Preserving Multimodal Reconstruction and Source-Grounded Adjudication](https://arxiv.org/abs/2609.13062)

**<font color=#1a73e8>作者：</font>** Sayantan Kumar, Nicolas Grimaldi, Jack Cummins 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical timelines support treatment-window analysis and leakage-free modeling, but discharge summaries often obscure chronology and structured EHR tables describe only part of the patient course. We present a UID-preserving framework that links each narrative event occurrence to its source span and retains that identity through text-only estimation, structured-evidence retrieval, timestamped source-row grounding, and joint revision. We also present GAVEL, an LLM judge that compares two UID-aligned timelines against the narrative and structured record, to augment prior matching and temporal assessments. Across six open-weight models and 40 mixed-critical-care summaries, the GLM 5.2 multimodal revision, as compared to its text-only variant, improved temporal agreement without reducing event recovery and performed competitively with clinician annotations, while other model revisions showed smaller gains and lower overall performance. Ablations showed that UIDs primarily preserve event retention, whereas source-row linkage supports temporal placement. Blinded human review upheld most GAVEL findings, and controlled adjudication favored multimodal over text-only GLM 5.2 but did not for DeepSeek V3.2. In developing the UID and judge pipeline, we are able to demonstrate 43\% increased event recovery, a framework competitive with clinician annotations, and a system with occurrence-level provenance for both reconstruction and evaluation.

---


### 127. [MAxBench: A Multinomial Concept Recovery Benchmark](https://arxiv.org/abs/2609.13072)

**<font color=#1a73e8>作者：</font>** Divya Appapogu, Freya Behrens, Yonatan Belinkov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-grained control of language model behaviors (e.g., steering) is among the more actionable outcomes of interpretability research. For binary concepts such as refusal, a single direction in activation space often suffices for steering. However, many concepts are not binary: Animals and Countries contain many subcategories, each with multiple instances. For these concepts, the search space over possible representation geometries is far larger than for binary concepts; it is thus not clear what geometries are most appropriate, nor what methods are most effective at recovering them. In this work, we introduce MAxBench, a geometry-agnostic evaluation framework for multinomial concept representations based on sampling from the recovered concept representation. We use MAxBench to compare 10 localization methods (covering 5 geometry types) across 6 concepts and 4 models. Using this framework, we find that (i) affine subspaces steer more reliably and have greater recall than rank-one or linear subspaces; (ii) much of this advantage is due to better non-zero offsets rather than the choice of bases; (iii) manifold steering is competitive with the best methods when applicable; and (iv) no method consistently outperforms prompting, in alignment with prior findings on binary concepts. These findings underscore the importance of expanding the scope of interpretability research and meta-evaluation to concepts with more varied structure.

---


### 128. [Autonomous Research for Open-Ended Problems: A Case Study on Telecom Ticket Retrieval](https://arxiv.org/abs/2609.13073)

**<font color=#1a73e8>作者：</font>** Junghyun Min, Huseyin Uzunalioglu, Mohamed Trabelsi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs in LLM-based systems and their abilities in problem solving and coding have allowed progress in the AI for Science paradigm, potentially replacing human roles in machine learning (ML) research. However, while several frameworks of fully autonomous end-to-end ML research have been proposed, successful implementations of them are often limited to problems with narrow search spaces, like language modeling or biomedical ML benchmarks. In this paper, we explore how autonomous research can be adapted to solve open-ended, industry-grade ML problems, by considering a case study: telecom ticket retrieval, an open-ended task with degrees of freedom in representation, architecture, and training data generation. We discover that autonomous research for open-ended problems with commercial and open-source agents shows both promise and limitations: while autonomous research can excel in narrow hyperparameter optimization, it lacks human-like intuition and creativity and requires operational overhead. Even with minimal human supervision, autonomous research can reach $90\%$ of state-of-the-art performance (0.34 vs. 0.38 Recall@1) in a much shorter time period (10 weeks vs. 10 months of human work) at a modest cost (up to \$200 per Cursor campaign). Our empirical evidence recommends that human researchers and autonomous research frameworks work together for best results in ML research.

---


### 129. [Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction](https://arxiv.org/abs/2609.13082)

**<font color=#1a73e8>作者：</font>** Baoyang Jiang, Fengchun Zhang, Leyuan Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic systems offer a promising way to automate embodied benchmark construction, but existing approaches typically cover isolated stages or remain specialized to predefined environments and task families. More importantly, multi-step construction produces dependent intermediate artifacts that are often passed downstream without artifact-specific verification, allowing local defects to propagate into the final benchmark. We present Embodied-BenchForge, an agentic framework that transforms user-specified evaluation intents into complete embodied benchmark artifacts. It formulates construction as Closed-Loop Benchmark Synthesis, integrating forward artifact synthesis with backward verification and repair. Skill-Orchestrated Artifact Synthesis composes typed and reusable skills into executable workflows, while an artifact dependency graph records intermediate outputs and their dependencies. Requirement-Guided Verification and Repair applies artifact-specific contracts throughout construction and uses provenance to trigger local re-execution or upstream rollback when verification fails. Embodied-BenchForge constructs six benchmarks covering diverse embodied scenarios in the Offline EQA Track, together with one interactive benchmark containing 220 executable tasks in the Interactive Embodied Track. Evaluations of representative MLLMs and embodied agents show that the benchmarks distinguish model capabilities in both observation-based understanding and closed-loop execution. Quality assessment and ablations validate benchmark quality and the effectiveness of verification and repair, while repair and skill-reuse analyses demonstrate efficient localized recovery and cross-benchmark reusability.

---


### 130. [Rethinking Heterogeneous System Disaggregation for Subquadratic Attention](https://arxiv.org/abs/2609.13134)

**<font color=#1a73e8>作者：</font>** Arya Tschand, Yaosheng Fu, Vikram Sharma Mailthody 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier language models are more aggressively using subquadratic attention to reduce the memory footprint and compute requirements during inference while still delivering frontier accuracy. While existing systems make dense attention-centric disaggregated serving decisions, we show that disaggregating inference around the unique arithmetic intensity and memory footprint of subquadratic attention LLMs can achieve significant throughput and energy efficiency gains on emerging DRAM-based and SRAM-only heterogeneous systems.
We introduce SQD (SubQuadratic Disaggregation), a fine-grained heterogeneous disaggregation scheme that splits decode by quadratic and subquadratic attention rather than by operator type, and that applies across subquadratic attention variants. For sparse attention LLMs, we disaggregate decode into top-k selection, which must index through the full KV, and top-k attention plus FFN, which have static memory footprints. For linear and sliding-window attention LLMs, we disaggregate decode into dense attention layers and subquadratic attention layers plus FFN. In an adjusted 8xB200 heterogeneous system proxy, we observe average tokens/J improvements of 53% on GLM 5.2, 31% on Nemotron 3 Ultra, and 56% on Gemma 4 31B over the strongest GPU-only baselines. In an analytical model of a Rubin plus LPX system with fixed power budgets, we observe 1.2x to 1.5x tighter achievable latencies and up to 3.6x higher throughput over the best baseline of attention-FFN disaggregation. Our experiments also reveal architectural insights on chip and interconnect provisioning for next-generation heterogeneous systems serving subquadratic attention.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 131. [Scan the Skill, Govern the Action: Composing Registry Verdicts with Runtime Consequence Control](https://arxiv.org/abs/2609.12001)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Rohit Taneja, Travis Weber  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skill registries screen what they publish. OpenClaw's security team reported that its scanners overlap on at most 10.4% of combined positives, and 81.9% of flagged skills are caught by one scanner alone. We take that as given, and suggest the open question is not which scanner is right but which is being asked. Each answers a form of "is this skill malicious?", which is what it was built for. "Is this action permitted here, by this operator, right now?" is not one it is designed to express.
We report three measurements over 66,192 public ClawHub skill versions. First, 705 skills across 135 distinct publishers that every scanner and the registry's judge rate clean nonetheless instruct an action prohibited by CIS Control 2.7 and NIST SP 800-53 CM-11. A hand audit of 100 puts our detector at 92% precision and found no marker of malicious intent. One publisher contributes 506 of the 705, so we report the distribution with the count. This is reproducible from public artifacts.
Second, of 144 commands a live agent executed in a sandbox while following real skill documentation, 34.7% carried a consequence class absent from that document. Third, over 53 cleared skills documenting an action no clean record earns, the agent reached for one in 23 and the gate stopped all 23. The harness and every recorded command are released.
We offer one design for that gap: a deterministic resolver with no model in the decision path, feeding a per-(resource, class) trust ledger whose promotion thresholds derive from the operator's stated risk tolerance. Ten clean approvals cannot exclude a true failure rate of 25.9% at 95% confidence. We price the gate's interruptions across a spectrum of operator policies rather than quote one false-positive rate, since friction is a property of the policy, not the gate. We release a 64-case obfuscation benchmark; ours resolves 52%.

---


### 132. [Beyond Argmax: A Mechanistic Study of Semantic Retention in Frozen Foundation-Model Composition for Generalized Few-Shot 3D Segmentation](https://arxiv.org/abs/2609.12099)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Silas Kwabla Gah, Ebenezer Owusu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classical classifier-combination work distinguishes score-level fusion from hard decision-level voting. We revisit this distinction where independently pretrained, frozen foundation models are composed at inference time for generalized few-shot 3D segmentation. We ask: how much useful semantic information is lost when heterogeneous sources are collapsed to a single class before they can interact?
We answer with a same-input semantic-retention intervention. Dense RegionPLC and sparse cross-view SAM3 evidence, model weights, masks, geometry, vocabularies, and fusion rules are frozen; only the number of semantic alternatives retained before interaction is varied via a matched top-k ladder. On 156 held-out ScanNet200 scenes, top-1 reaches 28.47 harmonic-mean (HM) IoU while full distribution fusion reaches 34.87 HM (+6.40, 95% CI [+5.24,+7.64]). The pattern replicates on 50 ScanNet++ scenes: 23.02 vs. 26.50 HM (+3.48, 95% CI [+1.64,+5.93]).
The conclusion is robust: full-distribution HM is stable across sparse-source weights 0.3--0.7; alternative operators (max, geometric pooling) also outperform top-1; and a GroundingDINO--SAM2.1 source-replacement diagnostic shows monotonic HM increase from 14.77 to 18.75 with full retention. Calibration diagnostics reveal opposite miscalibration of the two sources, yet correcting calibration does not eliminate the retention advantage.
Across datasets and source stacks, most information is recovered by retaining a compact set of plausible alternatives. The contribution is a controlled diagnosis of premature semantic collapse as a repeatable information bottleneck in heterogeneous frozen-model composition.

---


### 133. [Amortized Low-Rank Adaptation for Model-Based Reinforcement Learning](https://arxiv.org/abs/2609.12278)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fernando Palafox, David Fridovich-Keil  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World models let agents plan by predicting the consequences of their actions, but changes in the environment can make them inaccurate. We study the problem of adapting a world model to an unknown test-time environment, drawn from a known environment family, using only a few episodes of interaction. Existing approaches trade off computational cost against expressivity, i.e., the range of models a method can produce. For example, in-context learning is computationally cheap but limited in expressivity, and gradient-based adaptation is expressive but computationally expensive. We present CLAW (Context-conditioned Low-rank Adaptation of World models), which addresses this tradeoff by using a hypernetwork to generate low-rank (LoRA) adapters at test time. During pretraining, we simulate adaptation to a variety of environments and jointly train the hypernetwork and base world model. At test time, we freeze the base model and use a forward pass of the hypernetwork to generate adapters from a small batch of test-time transitions. We evaluate CLAW in locomotion and manipulation environment families that vary in dynamics, embodiment, and reward. We show that, using only seconds of test-time data, CLAW outperforms gradient-based adaptation and in-context learning during online adaptation. We also show that CLAW avoids overfitting in data-scarce regimes, that its advantage comes from the expressive adapters rather than context conditioning, and that pretraining the hypernetwork jointly with the base model outperforms training it post hoc.

---


### 134. [Balancing Emotional Alignment and Semantic Consistency in Image Generation via Reinforcement Learning with Valence-Arousal Anchoring](https://arxiv.org/abs/2609.12830)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jisheng Dang, Zhenxuan Wang, Bin Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continuous emotion control in text-to-image generation requires a model to improve affective alignment without changing the objects, layout, or scene described by the prompt. Existing supervised emotion-injection methods often optimize feature-space proxies and may therefore exhibit emotion-semantic drift, in which stronger emotional conditioning is accompanied by unintended content changes. We address this problem with a flow-matching image-generation framework that combines continuous valence-arousal (VA) conditioning, Group Relative Policy Optimization (GRPO), and a neutral semantic anchor. The deterministic probability-flow ODE is converted into a marginal-preserving SDE, yielding non-degenerate transition densities for trajectory sampling and policy-ratio estimation. A frozen CLIP-based VA regressor supplies a terminal reward measuring the distance between the predicted and target VA coordinates, while an image generated from the same prompt under zero VA conditioning provides a feature-space reference for semantic preservation. A reduced denoising schedule is used for online RL sampling, whereas the original schedule is retained at inference. Experiments on 3,300 prompt-emotion combinations show substantially lower valence and arousal errors than the VA-conditioned baseline and an improved CLIPScore relative to EmotiCrafter, with a measurable trade-off in reference-free image quality. The results support anchor-regularized Flow-GRPO as a practical approach to balancing emotional alignment and semantic consistency in continuous-affect image synthesis.

---


> [!TIP]
> 当前位于：**101-134**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-134**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
