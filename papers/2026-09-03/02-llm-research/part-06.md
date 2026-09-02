# 🧠 大模型相关研究 | 2026年09月03日

> 本类共 **295** 篇论文：已确认 **283** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-295**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-295**

---

### 251. [Investigating Linear Probe Robustness to Linguistic Register, Medical Specialty, and Corpus Shifts in Medical QA](https://arxiv.org/abs/2609.01361)

**<font color=#1a73e8>作者：</font>** Nishant Mishra, Ameen Abu-Hanna, Iacer Calixto  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear classifiers trained on hidden states of a large language model (LLM), linear probes, can flag factual errors from a single forward pass. Geometrically, that implies that true and false statements separate along a stable direction in hidden state space, i.e., the truth direction. Prior work disagrees on whether this generalises across input shifts, but the disagreement is hard to interpret because cross-dataset probe transfer experiments confound several kinds of input change at once. We isolate three such variables in medical question-answering (QA): writing style (register), domain (medical specialty), and corpus (dataset). We build a benchmark using 500 MedQA entries, each rewritten into four styles (textbook, patient, clinical note, colloquial), annotated with clinical specialty, and grouped with two other exam corpora, MedMCQA and MMLU-medical, for cross-dataset evaluation. Probing four open-weight LLMs (2--8B), we find that the truth direction is largely robust to writing style (mean $\Delta_\text{register} \approx 0.10$ AUROC on held-out facts) and to medical specialty ($\Delta_\text{specialty} \approx 0.03$), but degrades unevenly across corpora: by $0.12$ AUROC on MMLU-medical and by $0.21$ on MedMCQA, roughly twice the register gap. The register result replicates with a second generator and carries over to human-written patient questions. The truth direction is therefore largely stable within the medical domain but breaks under some corpus shifts, and question format does not explain the break, which suggests that the signal a linear probe recovers is partly bound to dataset structure rather than to medical knowledge alone.

---


### 252. [How Correct Is Your Answer? A Semantic Correctness Framework for Open QA Evaluation](https://arxiv.org/abs/2609.01369)

**<font color=#1a73e8>作者：</font>** Elitsa Yotkova, Violeta Kastreva, Petar Velkov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of open-ended question answering remains a bottleneck for measuring answer correctness of modern LLMs. Unlike multiple-choice tasks, free-form answers may be correct in many surface forms and may fail in qualitatively different ways, including incompleteness, contradiction, overgeneration, and endorsement of false premises. Existing judgment-based and similarity-based metrics often collapse these distinctions. We address this gap with three reusable contributions. First, we introduce a semantic correctness taxonomy that assigns open-ended answers to eight ordered classes, separating verbose-but-correct answers from those contaminated by hallucinated content. Second, we release CAP-Correctness, an 8.8k-example benchmark spanning widely used QA datasets, and CAP-Statements, an 11k-example dataset for converting question-answer pairs into declarative statements for natural language inference (NLI) training and statement-based evaluation. Third, we introduce CAP (Context-Aware Precision), a reference-based metric that scores question-conditioned statements using bidirectional NLI. Under a monotonicity protocol testing whether metrics respect the taxonomy's intended ordering, CAP outperforms established baselines.

---


### 253. [Behaviorally Effective LoRA Writes Are Sparse and Structured](https://arxiv.org/abs/2609.01374)

**<font color=#1a73e8>作者：</font>** Haruto Sato, Yuki Tanaka, Ren Nakamura 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation fixes the rank of the update, but it does not identify which parts of a trained
write actually carry behavior. We study that question directly and show that behaviorally effective
LoRA writes are sparse, structured, and far more concentrated than the raw low-rank parameterization
suggests.
We use Learned-Basis LoRA, a learned-basis continuation recipe, to expose that structure. The recipe
warms up an unconstrained adapter, converts its learned write columns into a module-wise orthonormal
basis, freezes that basis, and continues training inside the constrained parameterization. Across 14
exact switches from unconstrained to constrained form, held-out accuracy is unchanged at the
conversion step and reconstructed write matrices differ by at most 0.25% relative Frobenius error.
Same-state continuation then shows that the same trained checkpoint develops differently under
different write subspaces, establishing write geometry as a causal state variable. A no-retraining
projection test shows that useful write signal stays inside the learned write space and largely
disappears from random or frozen-activation PCA controls.
The concentration pattern is strong at both local and global scales. Across GSM8K, MathQA, and AQuA,
per-module top-k continuation reaches its optimum at k in {2, 4} in all twelve seed-level cases we
test. A stricter global ranking test shows that learned top-16 and top-32 subsets outperform matched
random subsets, especially on GSM8K/Qwen and MathQA/Qwen. Single-direction ablations further reveal a
sparse set of late q_proj, o_proj, and down_proj components with outsized behavioral impact.

---


### 254. [IntroConformal: Conformal Factuality Guarantees for Large Vision-Language Models via Introspective Signals](https://arxiv.org/abs/2609.01375)

**<font color=#1a73e8>作者：</font>** Md. Atabuzzaman, Christian Alexander, Chris Thomas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have achieved strong multimodal performance, yet ensuring the factual correctness of generated content remains challenging. Existing methods that provide statistical guarantees on factuality typically rely on external verifiers or generation-time confidence signals, which introduce auxiliary dependencies or often fail for confident but incorrect outputs. We argue that reliable factuality control can instead be achieved through introspective signals derived from the model itself. We introduce IntroConformal, a training-free Conformal Risk Control (CRC) framework that provides finite-sample, distribution-free factuality guarantees. We first instantiate it with layer-wise semantic stability, a conformity score derived from hidden-state representations, and then propose verification probability, a stronger score capturing the model's self-administered judgment on claim factuality. Across multiple LVLM architectures, IntroConformal satisfies the conformal risk guarantee while substantially reducing abstention and achieving competitive or superior claim-level discrimination relative to external verifier-based baselines.

---


### 255. [InSight: A Benchmark for Agentic Claim Verification in Interactive Visualizations](https://arxiv.org/abs/2609.01383)

**<font color=#1a73e8>作者：</font>** Maeve Hutchinson, Syed Mahbubul Huq, Mohammad Albinhassan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision Language Models have demonstrated remarkable proficiency in interpreting static visual artifacts, but modern data analysis is inherently dynamic, requiring the active interrogation of interactive environments. Existing benchmarks are predominantly constrained to static imagery and one-shot question answering and fail to capture the epistemic demands of this domain, where evidence is frequently occluded, distributed across linked views, or conditionally revealed through user agency. In this paper, we introduce InSight, a benchmark for agentic claim verification over interactive visualizations. The dataset consists of 21,349 claims derived from human-authored analytical narratives and grounded in fully interactive web-based environments. Agents must navigate these environments to determine whether a natural language claim is supported, refuted or not verifiable given the available evidence. Unlike traditional evaluations, InSight treats interaction traces as intrinsic proxies for reasoning, enabling a rigorous audit of how models seek and synthesize visual evidence. We evaluate state-of-the-art models, revealing that interactive verification remains a non-trivial challenge. We release InSight at this https URL.

---


### 256. [When Tokenization is Secretly Output Supervision](https://arxiv.org/abs/2609.01386)

**<font color=#1a73e8>作者：</font>** Tanja Baeumel, Josef van Genabith, Simon Ostermann  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenization in language models is treated by default as an input preprocessing decision. We argue that this framing is incomplete: in autoregressive models, tokenizer granularity determines what the model must resolve in a single forward pass, and therefore the supervision signal it receives. This affects both the difficulty of the learning problem and the representations that emerge inside the model. We test this in a controlled experiment on numeric reasoning with a novel decoupling of input and output tokenization. As the output supervision view predicts, differences in task performance, training dynamics, and model internals are induced by output tokenization and largely invariant to input tokenization. This may matter in practice, because models with different tokenization strategies differ not only in input representation but in the task they were trained on. Comparisons between models may thus partly reflect task definition rather than ability. A survey of 120 recent *CL papers on numeric reasoning confirms that this is rarely acknowledged: only about 10% report the numeric tokenization of the models they evaluate, while 69% compare across tokenization, and thus supervision, regimes without reporting it. While prior work documents that tokenization consistently affects model performance, there is no principled account of why. We argue that framing tokenization as output supervision provides that account.

---


### 257. [EdiTikZ: Scientific Figure Editing from Revision Trajectories](https://arxiv.org/abs/2609.01409)

**<font color=#1a73e8>作者：</font>** Christian Greisinger, Zhixue Zhao, Steffen Eger  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown strong performance in generating scientific figures from text or images. However, producing publication-ready figures requires iterative refinement, making scientific figure editing an important yet largely unexplored task. Existing approaches rely on costly proprietary agentic systems, focus primarily on evaluation, or construct training supervision from synthetically generated edits. Instead, we leverage naturally occurring scientific revision and development trajectories as a scalable source of supervision. To this end, we introduce DaEdiTikZ, the first large-scale dataset of revision-derived scientific figure edits, constructed by mining 391K plausible TikZ edit pairs from arXiv, GitHub, and TeX SE and inferring 781K directed edit instructions with a VLM conditioned on rendered figures and TikZ code. We further introduce DaEdiTikZ-Bench, a human-refined benchmark with 790 instances, and train two compact Qwen3.5-based EdiTikZ models (4B and 9B) by jointly learning reconstruction and editing, followed by reinforcement learning (RL) with complementary rewards for rendered fidelity and edit application. Automatic evaluation places our 9B model above all tested baselines, while human evaluation with 9 annotators and 4,320 ratings places it above GPT-5.6-Sol and on par with Gemini-3.1-Pro. Under severe out-of-distribution shifts, it remains competitive with GPT-5.6-Sol near its 2K training sequence-length regime. Models and datasets will be released.

---


### 258. [From Rollouts to Recipes: Self-Contained Post-Training for LLMs](https://arxiv.org/abs/2609.01422)

**<font color=#1a73e8>作者：</font>** Yifei Li, Lingling Zhang, Muye Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training large language models usually applies a single training recipe to all samples, even though the model's own rollouts reveal different sample-level learning states. We propose Self-Routing, a behavior-conditioned post-training framework that uses rollout correctness and confidence to decide how each sample should be optimized. Depending on its behavior state, a sample is routed to GRPO, on-policy self-distillation, regularization, or skipping, allowing training to adapt without external teachers, extra annotations, or additional sampling. Experiments on mathematical reasoning across Qwen3 and Qwen3.5 backbones show that Self-Routing consistently improves over uniform GRPO, uniform OPSD, fixed mixtures, and simpler routing baselines. Further analyses show that the routing distribution changes over training and reduces unnecessary updates on low-signal or already stable samples.

---


### 259. [TRIAGE: Three-level Routing and Intelligent Agent Guidance for Efficient Execution](https://arxiv.org/abs/2609.01428)

**<font color=#1a73e8>作者：</font>** Ruocan Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents based on the ReAct paradigm have demonstrated remarkable capabilities in tool use and task execution. However, ReAct suffers from a fundamental efficiency problem: every query triggers a complete reasoning loop from scratch, and similar queries repeat identical steps without leveraging historical experience. We propose TRIAGE,a three-level routing framework that reduces token consumption by reusing historical execution trajectories. Its core innovation is TaaS (Trajectory-as-a-Skill), which abstracts historical execution trajectories into reusable skills, realizing 'experience as a service'. TRIAGE classifies queries into three levels: (1) Direct Reuse-identical queries, 0 tokens; (2) Skill Substitution-similar queries, 0 tokens via deterministic parameter substitution; (3) Full ReAct-novel queries, automatically stored for future reuse. In large-scale experiments on 1,007 security monitoring queries, TRIAGE achieves 62.3% token savings, with 56.0% of queries at Level 2 and 5.5% at Level 1, both executing at zero cost. Cross-domain validation on ToolBench (15 domains, 345 queries) achieves 76.3% token reduction, confirming the generalizability of semantic routing. An online learning experiment demonstrates cold-start-to-mature evolution: the L2 hit rate rises from 0% to 57% within the first 100 queries, and the average token cost drops from 198 to 74.7. We also propose an automatic Skill extraction mechanism that distills high-frequency trajectory patterns into deterministic Skills, creating a positive feedback loop of 'the more you use it, the more efficient it becomes'.

---


### 260. [Efficiently Estimating Optimal Hyperparameter Scaling Laws through Power-Law Entropy Search](https://arxiv.org/abs/2609.01431)

**<font color=#1a73e8>作者：</font>** Zhiliang Chen, Sebastian Ament, David Eriksson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimal hyperparameter scaling laws describe how the best hyperparameters for large language model (LLM) training change with model and data scale, enabling practitioners to predict optimal configurations at production scales without expensive large-scale tuning. However, estimating these scaling laws conventionally requires exhaustive grid searches over thousands of training runs, consuming enormous computational resources. We introduce Power-Law Entropy Search (PLES), a computational cost-aware acquisition function built on multi-fidelity Bayesian optimization that efficiently estimates optimal hyperparameter scaling laws through adaptive experimentation. A key innovation in PLES is that it searches for candidates that reduce the overall uncertainty of a scaling law estimate, instead of optimizing a single objective function. At each iteration, PLES selects the candidate configuration that maximally reduces the uncertainty of the scaling law estimates per unit computational cost, naturally favoring informative small-scale experiments. We evaluate PLES on synthetic benchmarks, surrogate models fitted to real LLM training data, and actual LLM pre-training runs. Across all settings, PLES converges to accurate optimal hyperparameter scaling laws using less than one-tenth of the computational budget required by conventional grid search and other baselines.

---


### 261. [When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning](https://arxiv.org/abs/2609.01455)

**<font color=#1a73e8>作者：</font>** Yitong Guo, Xiaoyi Chen, Siyuan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Benign fine-tuning severely weakens the safety alignment of large language models (LLMs), so we study why refusal behavior is so fragile. While prior work often attributes this failure to gradient conflict, we propose a fundamentally different Fisher-geometric explanation: safety Fisher is low-rank, and alignment makes the safety geometry flatter while preserving an output-routing pathway. After 100 benign fine-tuning examples, this pathway is selectively re-sharpened in output-side MLP modules, explaining the asymmetric fragility: safety can collapse to high attack success rates, while general utility degrades mildly. The routing view also explains why few safety examples can restore refusal behavior, indicating that internal safety-relevant representations are preserved. Finally, we show that LoRA and ASAM mitigate early collapse by suppressing output-side sharpness, but their protection weakens at larger fine-tuning scales. Overall, safety failure is best understood as a disruption of a low-rank output-routing mechanism

---


### 262. [Parsing the Stream: A Live Trace Model for Long-Horizon Agents and Their Observers](https://arxiv.org/abs/2609.01466)

**<font color=#1a73e8>作者：</font>** Egor Pakhomov, Erik Nijkamp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A long-horizon agent's trace outgrows both of its consumers: the human observer monitoring the run, and the agent itself, whose bounded context the trace must be folded back into. We present a live trace model, an append-only event ledger folded incrementally into typed run state and compiled into per-consumer views, and evaluate it for both consumers against deterministic ground truth. For the observer side, evaluated with an LLM reader as proxy, the compiled view answers monitoring questions using approximately 14x and 15x fewer input tokens (by reader) and at 5-7x lower cost than a budget-capped single-call reading of the raw trace, with higher accuracy (0.85-0.87 versus 0.48). Because the questions were co-designed with the view schema, we treat the token and cost reduction, conditional on schema coverage, as the transferable result. For the agent, on 120-link sequential-dependency tasks, mechanisms that maintain the task's running statistic in per-step state succeed where full-context prompting fails (30/30 versus 8/30 under a clean protocol, n=30, labeled descriptive owing to benchmark-system co-development); a prompt-level scratchpad matches the fold's accuracy at lower cost, and a two-arm decomposition attributes the fold's accuracy to its deterministic aggregate and its cost advantage to its compactness. The fold's remaining value over cheaper alternatives is deterministic auditability and serving the observer from the same state. We derive eleven candidate requirements for trace folding from observed failures and delimit them with an order-sensitive task family on which the fold ceases to help. Code, benchmarks, a regenerable synthetic corpus, and all workbench traces are released.

---


### 263. [RadMatch: Auditable Radiology Report Evaluation via Finding-Level Matching](https://arxiv.org/abs/2609.01470)

**<font color=#1a73e8>作者：</font>** Charles Corbière, Léo Machado, Aubin Charley 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As AI systems are increasingly used to draft radiology reports, reliably evaluating their clinical quality remains a critical challenge. Large language model (LLM)-based metrics are now the best-correlated with radiologist judgment, yet they output a single opaque score that neither a clinician nor a model builder can easily interpret or audit. We introduce RadMatch, a multi-stage, LLM-based metric that decomposes report comparison into a structured finding-level matching with significance-aware scoring and error characterization across seven clinical attribute dimensions (status, location, severity, morphology, certainty, longitudinal comparison, and measurement). The main score is the actionable-error count, both interpretable and auditable. Candidate findings are graded correct, partial, or incorrect, and unmatched findings are counted as missed or hallucinated. Triage and actionable safety recall/precision and per-subset views add complementary, deployment-oriented lenses. Across two expert benchmarks, RadMatch is the most clinically aligned metric, matching inter-radiologist agreement on ReXVal and more than doubling the best prior metric on the harder RadEvalExpert. Relying only on few-shot prompting, it is designed to extend to other modalities and anatomies. We will release RadMatch as open-source code with an interactive dashboard for inspecting results.

---


### 264. [Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Improvement](https://arxiv.org/abs/2609.01481)

**<font color=#1a73e8>作者：</font>** Haoyang Yan, Min-le Su, Hangfan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper studies autonomous software development, in which LLM-based coding agents transform high-level requirements into complete, functional, and usable software systems without human intervention. We introduce Harness-of-Harness (HoH), a framework that enables coding agents to continually improve software during autonomous development. HoH operates on existing coding-agent harnesses, and organizes their executions into iterative planning-coding-testing loops. To sustain improvement across loops, HoH balances repair with capability growth, scopes development into small and verifiable increments, separates implementation-time testing from independent evaluation, and constrains verifiable outputs rather than prescribing agent workflows. It progressively exposes deliverables, role-specific tools, and skills, encourages reuse rather than recreation, and maintains versioned project histories. On GameCraft-Bench, FrontierSWE, and ProgramBench, three harness-model pairs (Codex with GPT-5.5, OpenCode with DeepSeek-V4-Pro, and Pi with MiniMax-M3), HoH consistently outperforms the corresponding standalone harnesses, achieving an average relative gain of 52.25 percent and a maximum gain of 82.86 percent after three iterations. In a multi-day deployment with more than 70 iterations, HoH autonomously develops a first-person-shooter game, featuring a coherent storyline, fully implemented core mechanics, human-playable experience, polished visuals and integrated audio. Github: this https URL Project Page: this https URL

---


### 265. [Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents](https://arxiv.org/abs/2609.01487)

**<font color=#1a73e8>作者：</font>** Xiaofang Yang, Ziqi Miao, Dianbo Sui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Skill-augmented agents load reusable skills as persistent runtime context, improving task performance but also giving malicious skills a durable channel for steering future actions. Such skills may leak secrets, corrupt code, bypass approvals, or stage data for exfiltration only after a concrete user task and workspace state make the unsafe action appear useful. This makes pre-install vetting insufficient and calls for runtime, task-conditioned protection. We propose Defense-as-Skill, a defense paradigm that implements the runtime guard itself as an installable, inspectable, and editable skill. Our guard, SkillSonar, runs alongside untrusted task skills and checks sensitive actions against the user's task boundary, routing each action to an allow, replan, or confirmation decision without modifying the underlying agent runtime. To study this setting, we construct SCOPE-R, a task-conditioned dataset covering 6 risk families and 21 sub-categories, with 206 attack-confirmed malicious instances and 43 benign tasks. We then improve SkillSonar on the SCOPE-R training subset using runtime guard-skill evolution, a Monte-Carlo Tree Search procedure that evolves the on-disk guard skill from feedback on the rollouts. Across Claude Code and OpenClaw, the evolved guard substantially reduces attack success while maintaining a favorable safety-utility trade-off. On repeated GLM-5 runs, SkillSonar reduces ID ASR from 0.482 to 0.104 and OOD ASR from 0.606 to 0.115. Further analyses demonstrate transfer across victim models, held-out risk families, and external benchmarks, as well as retained protection against adaptive attackers. Ablations further show that explicit safety responsibility assignment and the skill-native representation are both important to the observed gains.

---


### 266. [GlossoGen: Emergent Language in Complex Multi-Agent LLM Interactions](https://arxiv.org/abs/2609.01491)

**<font color=#1a73e8>作者：</font>** Elias Stengel-Eskin, Newton Sander, Carlos Bonetti 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growing rate at which LLM agents interact with one another raises key questions about language evolution in multi-LLM-agent settings, with implications for safety and monitorability as well as for linguistic accounts of LLMs. To address these questions, we introduce GlossoGen, a novel platform for studying multi-agent language evolution in complex scenarios. Within GlossoGen, we build the SaveVeyru scenario, which requires agents with partial information to communicate under pressure. We find that language evolution does occur between LLM agents, that the resulting languages are compositional and morphologically productive, and that they deviate from the LLMs' English prior in ways that render them incomprehensible to humans. Moreover, we identify several qualities essential to this evolution: pressure towards efficiency; the strength of the models backing the agents; and access to a "postmortem" stage in which agents can agree on linguistic conventions. Importantly, we observe that different conditions govern the transmission of language to new agents. Specifically, we find that agents learn new languages from usage alone, take an active role in this learning, and that while stronger models are required for novel language emergence, weaker models can learn an existing language once it has emerged. Taken together, our results indicate that current LLMs have the potential for cumulative cultural evolution -- previously attested only in humans -- with mixed populations of agents developing capacities that go beyond their lowest common denominator.

---


### 267. [LatentPress: Context Compression Beyond Text and Vision](https://arxiv.org/abs/2609.01507)

**<font color=#1a73e8>作者：</font>** Zhengze Zhou, Hejian Sang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compressed context is usually carried as human-readable text or as rendered images that must be decoded, even when its consumer is a language model. We introduce LatentPress, which writes conversational histories and long documents into a third representation: continuous memory tokens that a frozen decoder reads directly through its input-embedding interface, with no text reconstruction at inference. A small reader-matched writer compresses $4$-$16\times$ while training only an adapter (4.2M-26.2M parameters, $\sim\!0.1\%$ of the decoder). On LongMemEval, LatentPress reaches $0.504$ accuracy at $7.70\times$ compression versus $0.490$ for uncompressed evidence, outperforming text summaries (0.184) and OCR-based compression (0.426 to 0.312). On LongBench-QA, in-domain writers match or exceed raw-context reading at $4$-$8\times$ compression, while $16\times$ trails raw. Writing takes 43ms per conversation, roughly an order of magnitude faster than text summarization or OCR reconstruction, and reading is $5$-$9\times$ faster than raw context or cached OCR. We validate the interface under two transfer settings, zero-shot from UltraChat to LongMemEval memory QA and from LongMemEval-derived QA to unseen LongBench document domains, establishing direct soft tokens as a practical machine-facing context interface beyond text and vision. The implementation of the experiments could be found at: this https URL .

---


### 268. [TempCloze: Can Video-LLMs Identify the Missing Middle?](https://arxiv.org/abs/2609.01515)

**<font color=#1a73e8>作者：</font>** Wenqi Pei, Henry Hengyuan Zhao, Yilai Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal reasoning benchmarks for Video-LLMs are often mediated by language, leaving room for linguistic shortcuts from option wording, answer correlations, or language priors. To reduce such shortcuts, we introduce TempCloze, a video cloze benchmark for evaluating visual temporal reasoning in Video-LLMs. Given the beginning and ending clips of a video, models must identify the true missing middle from four candidates. TempCloze contains 1,521 carefully filtered videos from seven sources, mainly long-take and egocentric videos. We construct same-source distractors along three dimensions: Semantic asks what event should happen, Alignment probes when it should occur, and Progression tests how it should unfold, while shared scenes and objects reduce appearance cues. Our evaluation of 10 proprietary and 21 open-source Video-LLMs reveals Alignment as the primary bottleneck: models often recognize plausible semantic content and local event progression but struggle with temporal alignment. We further conduct error pattern and behavioral sensitivity analyses on TempCloze-Mixed and TempCloze-Hard with four representative models to examine where errors arise and how candidate order, context direction, visible span, frame density, and test-time scaling influence model choices.

---


### 269. [EvoSCM: Scientific Belief Revision Through Causal Model Evolution and Experimentation](https://arxiv.org/abs/2609.01526)

**<font color=#1a73e8>作者：</font>** Qing Zhao, Haowei Li, Weijian Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific agents must learn not only how to reason, but also what to believe. However, existing LLM agents typically express scientific hypotheses in free-form text, leaving their beliefs implicit and difficult to test or revise. We introduce EvoSCM, which equips scientific agents with explicit structural causal models that evolve as new experimental evidence is collected. EvoSCM maintains a population of competing SCM hypotheses, each encoding a candidate causal explanation of the environment, and evolves them through a closed discovery loop. In each round, the agent abduces latent mechanisms from accumulated evidence, designs discriminative interventions, and commits to falsifiable predictions that it tests through experimentation. Discrepancies between prediction and observation are inductively distilled into correction rules that revise the causal structures and mechanisms of each hypothesis, and the agent then deductively validates the revised population against accumulated evidence and structural consistency to guide the next round. We evaluate EvoSCM on DiscoverPhysics, a benchmark requiring agents to uncover the hidden dynamics of noncanonical physical worlds through experimentation. EvoSCM consistently improves scientific discovery over baselines, yielding more accurate explanations and predictions while making more effective use of experimental interactions.

---


### 270. [Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall](https://arxiv.org/abs/2609.01532)

**<font color=#1a73e8>作者：</font>** Jacqueline He, Howard Yen, Shuyue Stella Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Logit-based knowledge distillation (KD) is used to train smaller language models (LMs) via supervision from stronger teachers, but whether its benefits are consistent across training stages remains unclear. Through controlled experiments, we find that forward Kullback-Leibler (KL) distillation--the standard KD formulation--with post-trained teachers behaves fundamentally differently during mid-training, an intermediate phase of self-supervised learning on curated corpora. Surprisingly, while forward KD simultaneously improves reasoning and factual recall during pre-training relative to standard next-token prediction (NTP), it instead slows factual recall acquisition during mid-training despite continued reasoning gains. We trace this stage dependence to an asymmetry in teacher confidence across data domains and the student's evolving knowledge state: teachers are more confident on procedural than knowledge-intensive data, while students acquire low-entropy factual knowledge earlier in training. To mitigate this imbalance, we propose Switch Distillation, a simple mid-training objective that distills on tokens where the teacher is confident, using teacher predictive entropy as a lightweight routing signal, and otherwise falls back to cross-entropy. Switch Distillation consistently outperforms existing distillation objectives across teacher sizes. Relative to standard NTP, it achieves 1.61-1.71x the reasoning performance and 1.13-1.19x the knowledge and commonsense performance while preserving 96.7-96.8% of factual recall. Crucially, these benefits persist after post-training: Switch Distillation closes the factual recall gap while maintaining 1.25-1.32x and 1.13-1.20x gains in reasoning and knowledge and commonsense, respectively.

---


### 271. [SDARE-Bench: Evaluating Large Language Models on Conversational Stigma Detection and Response in Dyadic and Group Dialogue](https://arxiv.org/abs/2609.01548)

**<font color=#1a73e8>作者：</font>** Stephanie Fong, Yiwen Jiang, Zimu Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used in advice seeking and decision making that may affect social judgements. Despite stigma's profound effects on people and communities, benchmarks remain scarce. Existing general-domain evaluations typically rely on static prompts and fixed-format tasks, overlooking conversational contexts and audience effects in everyday communication. To address these gaps, we introduce SDARE-Bench, the first scenario-based benchmark evaluating both stigma detection and open-ended response generation in LLMs, comprising 1,138 dyadic queries and 1,388 group dialogue. Empirical results across 8 LLMs consistently demonstrate poor identification of stigma components, especially in group dialogues. In open-ended response generation, stigma expression was substantially higher in group settings than in dyadic, with weaker resistance to stigma and more unrealistic advice. Responses were evaluated using a classifier trained on 1,392 human annotated responses. In constructed group pressure settings, stigma expression rates further increased to a striking average of 97.5%. Our findings identify stigma response as a recurring LLM safety vulnerability, especially in socially complex conversational contexts.

---


### 272. [Can LLMs Discover Scientific Laws in Real and Parallel Worlds?](https://arxiv.org/abs/2609.01552)

**<font color=#1a73e8>作者：</font>** Yiming Huang, Ziche Liu, Zhuohang Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific equation discovery has long been central to scientific progress, proceeding through iterative cycles of hypothesis generation, observational testing, and refinement under scientific constraints. As LLM capabilities advance and their role in AI for Science expands, it remains an open problem whether they can genuinely discover scientific laws and how this ability should be evaluated. Existing evaluations, however, often either simplify discovery through synthetic settings or reuse published targets that may already be familiar to LLMs. We therefore introduce SCILAWS-BENCH, a benchmark for scientific law discovery built from published research and real scientific data. It comprises 118 problems drawn from 381 scientific papers, covering 291 candidate laws and roughly 8M real data points across six scientific disciplines. Each problem is instantiated in two complementary settings: (1) SCILAWS-REAL asks models to propose laws from fixed real observations and evaluates held-out predictive fit and scientific validity derived from the source literature, and (2) SCILAWS-PARALLEL asks models to actively query residual-calibrated worlds and recover synthesized hidden laws derived from published forms. This two-setting task design preserves each problem's scientific context while separately evaluating fixed-record law discovery and active recovery of a newly synthesized hidden law. We find that predictive fit can diverge from scientific validity, memorization shapes whether models reproduce or move beyond published formulas, and our best-of-N study reveals a selection bottleneck. Our work provides a paper-grounded benchmark and new empirical perspectives for evaluating AI for scientific discovery. Project page: this https URL

---


### 273. [Retrieved but not ranked: surface-form bias in structural retrieval, from mathematics to agent trajectories](https://arxiv.org/abs/2609.01556)

**<font color=#1a73e8>作者：</font>** Nabira Rashid, Manolis Kellis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We evaluate embedding retrieval where surface form and meaning are pulled apart on purpose: retrieving items that share underlying structure but not wording, in two unrelated domains under one protocol, competition mathematics (MathNet-Retrieve; 500 queries, 117,088-item corpus) and embodied-agent trajectories (ALFWorld-derived; 118 queries, 336 trajectories). In mathematics the failure is complete: strict Hit@1 at the heaviest disguise tier is 0.0% for both production embedders (bootstrap 95% CI [0.0, 0.0]) while the correct item sits in the top 10 nearly always, and in 95.2 to 99.8% of misses the winner is more lexically similar to the query than the correct answer. In trajectories, where surface variation is incidental, the same models land at or near hypergeometric chance when gold must involve a different object, and below chance for all three embedders once gold must differ in object and receptacle: retrieval anchors on literal tokens, not task structure. A lexical reranker control hurts in mathematics and helps in trajectories (closing 26 to 36% of the gap, CIs excluding zero); its sign reveals whether a benchmark's surface variation is adversarial or incidental. An LLM reranker recovers 5 to 63% of the gap in mathematics and 43 to 76% in trajectories; direction replicates across three judges (all 21 cells positive), but effect sizes, tier profiles, and the outlier judge change with domain (paired differences excluding zero everywhere). Mathematics gains concentrate on well-known competitions (+19.8 points, CI [+6.7, +33.2], one of six cells), so part of the recovery is memorization. In a paired downstream experiment (210 queries, graders at 96 to 99% agreement), oracle retrieval was indistinguishable from adversarially bad retrieval (McNemar p = 0.678); the solver's 69.5% zero-shot accuracy is largely a truncation proxy (97 to 100% on finished answers), leaving no headroom.

---


### 274. [A systematic Approach to constructing a Chance-and-Risk Matrix for Semiconductor Supply Chains](https://arxiv.org/abs/2609.01563)

**<font color=#1a73e8>作者：</font>** Ema Salkić, Alexander Fichtl, Philipp Ulrich 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semiconductor supply chains face escalating risks from geopolitical tensions, geographic concentration, and rapid technological shifts, yet no scalable system continuously extracts, structures, and prioritizes risk intelligence from public corporate disclosures. We present an end-to-end pipeline that retrieves corporate documents for semiconductor companies and uses large language models (LLMs) to extract the risks and opportunities they describe. It organizes these into a knowledge graph linking each item to its category, sources, and related events, then merges duplicates and ranks them with a three-layer mechanism combining an algorithmic formula, an LLM relevance adjustment, and expert validation. Applied to five companies across the value chain, the pipeline produces 76,207 scored items, of which an independent check finds 92.6% valid. The automated rankings match expert judgment at an average Spearman correlation of 0.55 for risks and 0.72 for opportunities, and the resulting matrices identify trade restrictions as the dominant cross-company risk.

---


### 275. [From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection for Text Classification](https://arxiv.org/abs/2609.01564)

**<font color=#1a73e8>作者：</font>** Manish Gupta, Chaitanya Giri, Jayasimha Talur  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) struggle to classify text into taxonomies with many semantically similar labels, as the distinctions are domain-specific and not captured by pre-training. To handle large label spaces, a common approach retrieves top-$K$ candidate labels by embedding similarity and prompt the LLM to choose among them. However, top-$K$ retrieval reduces the number of candidates but does not help the model tell similar ones apart. When two similar labels both appear as candidates, the model lacks the signal to choose correctly between them. We propose a framework that (1) identifies which label pairs the model struggles to distinguish, (2) expands the candidate set to include confusable labels, and (3) generates targeted rules to differentiate between similar candidates. The framework requires no fine-tuning, and the generated rules transfer to smaller, cheaper models. On three benchmarks (WOS, Flipkart, LEDGAR), our approach improves Macro F1 by up to 10.0pp over retrieval baselines, with smaller models (2B--20B) gaining up to 11.5pp via cross-model transfer.

---


### 276. [Selective Agent Guidance via Entropy: Learning Autonomous Policies from Imperfect VLM Teachers](https://arxiv.org/abs/2609.01567)

**<font color=#1a73e8>作者：</font>** Matteo Merler, Giovanni Bonetta, Davide Zago 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) provide useful priors for interactive decision-making, but using them directly as policies is expensive and brittle: they must be queried at every step, do not improve from environment interaction, and can repeat systematic errors. We study how to learn a cheap autonomous policy from an online, expensive, and imperfect but informative VLM teacher. We propose SAGE (Selective Agent Guidance via Entropy), a framework that queries a VLM only when the learner is uncertain, executes the suggested action during training, and distills guidance into a lightweight Reinforcement Learning (RL) policy. Because VLM advice is not always reliable, SAGE can weight teacher-action distillation using environment-derived advantages rather than treating all suggestions as equally useful. Across sparse-reward visual reasoning and navigation tasks, SAGE learns policies that act without VLM guidance at evaluation time and improves over unguided RL in several environments, including settings where the learned policy exceeds its VLM teacher. The results show that selective guidance is most beneficial when the VLM can help the agent discover high-reward trajectories, and less useful when unguided exploration already succeeds or teacher actions do not lead to informative experience. SAGE also reduces VLM usage by prompting the teacher only on a fraction of training steps and requiring no VLM calls at deployment. Overall, our results suggest that VLMs don't need to be used as fixed policies to be useful; they can instead act as temporary, imperfect sources of guidance whose value is tested and internalized through interaction.

---


### 277. [From Production Traffic to Post-Training: Building a Self-Hosted LLM That Covers the Corporate Request Mix](https://arxiv.org/abs/2609.01572)

**<font color=#1a73e8>作者：</font>** Olga Tsymboi, Dmitrii Stoianov, Ramil Latypov 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data-residency constraints force enterprises to self-host LLMs, but continuous adoption of newer models without decommissioning their predecessors expands the serving fleet, fragmenting a finite GPU pool. We consolidate traffic from over 200 internal applications onto a single model by closing quality gaps identified through production error analysis along three axes: instruction following, function-calling, and internal task distribution. Quality is tracked by offline benchmarks stratified to production traffic and scored by deterministic verifiers or calibrated LLM judges. Rather than optimising all objectives jointly, which introduces cross-domain reward interference, we train a separate GRPO expert per axis and merge them via two-stage SLERP. Each expert's reward exposes a distinct failure mode, namely semantic collapse, over-calling, and verbosity hacking, each requiring a domain-specific fix. In non-reasoning mode the recipe surpasses a ${\sim}7\times$ larger by total parameters baseline on the in-house Arena with 69.6 to 65.8, instruction following with 0.85 to 0.83, and function-calling with 0.79 to 0.77, while lifting general dialogue benchmarks. The model absorbs 50% of platform traffic, 116M requests per month, at a fraction of the serving cost.

---


### 278. [Scaling Near-Optimal SFT-RL Annotation Budget Allocation from Small to Large LLMs](https://arxiv.org/abs/2609.01573)

**<font color=#1a73e8>作者：</font>** Jingtan Wang, Arun Verma, Xiaoqiang Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How to divide a fixed annotation budget between supervised fine-tuning (SFT) and reinforcement learning (RL) during LLM post-training remains an open problem. Existing work characterizes only broad trends (e.g., SFT dominates in low-data regimes), lacks a principled allocation framework, and does not examine whether the optimal ratio transfers across model sizes. We frame this problem in terms of near-optimality: rather than seeking a single optimal SFT-RL ratio, we characterize the near-optimal region, the set of allocations within a specified tolerance of peak performance. Empirically, this region is wide even for small tolerances (2-10%), widens with model scale, and transfers reliably from small proxy models to large target models. This yields a practical strategy: small proxy-model experiments suffice to identify a transferable near-optimal region, eliminating the need for exhaustive large-scale search. Our results hold consistently across tasks, model families, and both preference-based off-policy and reward-supervision on-policy RL methods. We further analyze how the asymmetry in annotation costs between SFT and RL data shifts the near-optimal region.

---


### 279. [Closing Cost-Quality Gap in Document VLMs: Difficulty-Aware Data Curation and Quality-Adjusted Deployment Economics](https://arxiv.org/abs/2609.01575)

**<font color=#1a73e8>作者：</font>** Maksim Evdokimov, Matvey Ivanov, Dmitrii Tsiupin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extracting structured fields from hundreds of millions of documents annually remains costly in regulated industries: bespoke OCR cascades cover only a fraction of workflows, privacy rules preclude external models, and existing open-source VLMs that clear quality thresholds cost more to serve than human annotation. We present a deployed document-understanding system built on a Mixture-of-Experts VLM (35B total, 3B active), fine-tuned on in-house production data mixed with open-domain documents curated by a Difficulty-Aware pipeline for layout diversity, fact-extractability, and cross-model consistency. Fitting on a single H100 and serving heterogeneous workflows via prompting, the model leads all deployable (non-reasoning) baselines up to an order of magnitude larger. A quality-adjusted cost analysis, with confirmation and correction costs calibrated from production telemetry, shows it reduces expected costs by over 80% against the human baseline and by more than 50% against the best competing open-source model, while larger baselines remain economically unviable.

---


### 280. [The Structure of Quantization Damage in LLMs: Why the Next Bit Should Be Spent Globally](https://arxiv.org/abs/2609.01587)

**<font color=#1a73e8>作者：</font>** Jundong Hu, Shekar Ramachandran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) is widely used to reduce the cost of serving large language models (LLMs), but its accuracy cost is uneven and is often tuned per model. We study where quantization damage occurs and how to allocate a small additional precision budget. Using causal mixed-precision intervention as ground truth (raise each layer to 8-bit in turn and measure the accuracy it recovers) across 9 open-weight models in 4 architecture families, we test 3 intuitive hypotheses: that quantization damage lives in task circuits, where the model computes, or in weight statistics. None of them predicts which layers benefit from restored precision. Recovery is instead diffuse: for 8 of 9 models, recovering 75% of the gap takes roughly half the layers; the lone exception, Qwen3-8B, is sharply concentrated. At a matched precision budget, spending it globally on finer quantization granularity beats locally repairing the most recoverable layers for all 8 group-128-compatible models (all but OpenLLaMA, whose width rules out group-128), by 21-52 points, including the concentrated Qwen3-8B. We report 2 secondary findings: the residual is budget-limited (8-bit is near-lossless in our evaluation across RTN, GPTQ, and AWQ), and the location of peak recovery correlates with architecture within a family, though not across families. Within this budget setting, global granularity is a better default than selectively protecting critical layers. More broadly, cheap signals that correlate with quantization damage do not necessarily identify where restoring precision improves accuracy; this must be tested with causal intervention.

---


### 281. [StudentSim: Training LLM-based Student Simulators](https://arxiv.org/abs/2609.01591)

**<font color=#1a73e8>作者：</font>** Ke Yang, Chenglong Wang, Michel Galley 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI tutors are most useful when they adapt to each student's strengths, weaknesses, and preferred guidance, but evidence about which guidance works for which student is sparse, slow, and costly to collect from real learners. Student simulators can provide this signal as a proxy, yet existing approaches are limited: state-tracking models fit student behavior but struggle to process explanations or corrections, while LLM role-play follows guidance fluently but does not reliably match the competence of the student being imitated. We present StudentSim, a training framework that turns sparse per-student data into individualized simulators through pooled training followed by per-student specialization. The resulting simulators both mirror a student's own responses and update them under tutor guidance. We also introduce StudentSimEval, a standardized protocol covering 60 students across chess, second-language English writing, and mathematics, using public learner datasets with de-identified records shared for research. StudentSimEval measures behavioral fidelity (F), or how well a simulator matches a student's responses, and guidance responsiveness (R), or how readily it updates under tutor guidance, with all methods fit and evaluated on the same records. Across all three domains, StudentSim outperforms GPT-5.4 on both metrics. In chess, StudentSim reaches F=0.51 and R=0.91, compared with 0.23 and 0.72 for GPT-5.4 and 0.45 and 0.27 for Maia2. As a proof of concept, using StudentSim as a reward model for tutor reinforcement learning produces a chess tutor that expert humans rate as more accurate, better-guided, and more personalized than a no-RL baseline and a tutor trained against a GPT-5.4 simulator reward. Code is available at this https URL.

---


### 282. [The Rise of Verbal Reinforcement Learning](https://arxiv.org/abs/2609.01597)

**<font color=#1a73e8>作者：</font>** Kshitij Tayal, Arun Sharma, Genta Indra Winata 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Natural language is emerging as a primary feedback channel for improving language agents, capable of conveying intent, preferences, and causal structure in forms interpretable by both humans and modern language models. We call this paradigm Verbal Reinforcement Learning (VRL) and offer the first unified account of it. We organize the field around a single axis, \textit{when} verbal feedback takes effect in an agent's lifecycle and \textit{what} it modifies, yielding three pillars: (1) \textbf{Language as Grounding Signal}, where language defines the task itself by specifying goals, states, and reward structures; (2) \textbf{Language as Deliberative Feedback}, where natural language guides reasoning at test time without the need to update model parameters; (3) \textbf{Language as Learning Signal}, where language-based feedback shapes model parameters through training. Within each pillar, we synthesize representative work, distinguish key subcategories of approaches, and outline the distinct role language plays in shaping agent behavior. Together, this taxonomy shows how verbal reinforcement is reshaping agent development, while also defining the challenges and opportunities for building more capable and aligned agents.

---


### 283. [Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation](https://arxiv.org/abs/2609.01604)

**<font color=#1a73e8>作者：</font>** Himil Vasava, Ming Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based evaluators of natural language generation (NLG) quality are widely deployed as scoring tools and as automated training signals, yet the internal procedure by which they assign a rating remains poorly understood. We investigate this procedure mechanistically through an eight-attack perturbation taxonomy across the Readability and Adequacy dimensions of NLG quality, a generation pipeline that produces paired clean and corrupt summaries with controlled error intensity and explicit token-level modification maps, and a four-experiment battery of causal tracing, logit-lens vocabulary projection, and attention-head knockout applied to Themis (Llama-3-8B) and Prometheus (Mistral-7B). Both evaluators implement a structured, coherent evaluation pipeline operating in two stages: below layer 15, attention performs local error comparison and routes the result to the final input position; above it, the MLP cascade integrates the signal and writes the rating, with the decision crystallizing in the residual stream at a sharp late layer (L = 26 on Themis, L = 25 on Prometheus). Furthermore, a base-model control at the same scale (Llama-3-8B) reproduces the routing architecture and crystallization but not the stage separation, isolating the two mechanisms that fine-tuning specifically installs, suppression of below-L15 MLP contribution at the last position and a two-layer advance of the crystallization depth, indicating that fine-tuning sculpts an existing substrate rather than building the pipeline from scratch. We release the source code and data at this https URL

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 284. [Foundation models for electricity price forecasting and battery arbitrage: Can they replace market-specific forecasting models?](https://arxiv.org/abs/2609.00089)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Arkadiusz Lipiecki, Rafał Weron  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models promise accurate forecasts with little or no task-specific training, but whether they can replace models designed specifically for electricity price forecasting remains unclear. We compare nine variants from five foundation model families, evaluated in zero-shot mode, with two state-of-the-art electricity price forecasting benchmarks in Germany, Poland, and Spain over 2021-2025. Their performance is assessed in terms of point and probabilistic forecasting accuracy, as well as economic value in battery energy storage arbitrage. Only the TabPFN models consistently and significantly outperform the benchmarks across all three markets and all statistical measures. However, this statistical dominance does not translate directly into economic dominance: TabPFN performs best under unlimited bids and riskier quantile-based strategies, whereas the Distributional Deep Neural Network benchmark is more profitable when risk tolerance is lower. Thus, foundation models cannot universally replace market-specific models, and their value depends on both model architecture and the decision problem.

---


### 285. [Unmasking Face Embeddings: Reading, Rendering and Naming with Foundation Models](https://arxiv.org/abs/2609.00411)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Fizza Rubab, Yiying Tong, Arun Ross  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern face recognition (FR) owes much of its success to deep neural networks that learn to extract compact identity embeddings from face images. These models are typically trained for identity discrimination, producing embeddings that are highly effective for biometric matching but largely opaque to semantic interpretation. In contrast, foundation models, pretrained on broad visual or vision--language tasks, provide rich interfaces for describing, retrieving, generating, and organizing visual content. This contrast raises a natural question: what capabilities become available when face embeddings from domain-specific FR models are made interoperable with foundation models? Building on recent work on embedding compatibility across models, we use simple pre-computed linear transformations, estimated from paired embeddings alone, to connect existing FR models with off-the-shelf foundation models. Once aligned with a foundation model, a face embedding can be 'unmasked' in multiple ways, without training or modifying either model: it can be read in natural language, enabling free-form text queries over a gallery of FR embeddings; rendered into a face image that recovers a person's appearance, using an unmodified diffusion decoder; and converted to a name, enabling identification even in the absence of an enrolled face gallery. In effect, one linear transformation turns an identity embedding into a rich embedding for web-scale foundation models. This interoperability exposes face embeddings as semantically and visually rich biometric representations, with direct implications for interpretability, retrieval, reconstruction, and template security.

---


### 286. [Context Window Failures in Relational Foundation Models](https://arxiv.org/abs/2609.00460)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Denis Oliveira Correa, Francisco Galuppo Azevedo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent Relational Deep Learning architectures have been proposed as foundation models for multi-table relational data, yet they impose constrained neighborhood budgets that force row truncation when an entity has many related records. We introduce Animus, a synthetic financial dataset in which predicting customer income requires aggregating up to tens of thousands of transactions. On the raw representation, three recently proposed models (RT, Griffin, RelGT) achieve $R^2 \le 0.18$; a single, routine, temporal pre-aggregation step recovers $R^2$ up to $0.65$. This questions whether current relational foundation models are ready for high-cardinality real-world data.

---


### 287. [SAM3-LoRA: Parameter-Efficient Adaptation of a Concept-Promptable Foundation Model for Multi-Class Structural Defect Segmentation](https://arxiv.org/abs/2609.00469)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** P. Malaisree, S. Youwai, S. Janrungautai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Promptable segmentation foundation models such as SAM3 accept an open-vocabulary text concept and return every instance matching it, but adapting them to a specialized domain by full fine-tuning is computationally prohibitive for the organizations that would benefit most. This study applies Low-Rank Adaptation (LoRA) to SAM3 for multi-class structural defect segmentation and examines both how such a model can be supervised from conventional annotation and whether the resulting efficiency gain transfers across datasets. Two contributions are methodological. First, we describe a supervision procedure that trains a concept-promptable model directly from COCO-style class-labeled instance segmentation by using the category name itself as the prompt, requiring no prompt templates, no synonym expansion, and no learned class embeddings. Second, we identify and mitigate a failure mode specific to this setting: because a conventional annotation file yields positive prompts exclusively, the model's presence prediction decouples from the text condition and degenerates into responding to any prompt, a collapse that is invisible to every metric computed on positive prompts alone. Exhaustive hard-negative prompting, in which every dataset category absent from an image is issued as a zero-detection query, addresses this at no annotation cost. Two adapter placements were compared under an identical protocol, updating 0.121% and 1.341% of model parameters. On a purpose-built tunnel lining dataset, pixel intersection-over-union improved from 0.017 to 0.338 and instance-level recall from 0.375 to 0.672; on the independent public Structural Defects Dataset, from 0.017 to 0.855 and from 0.574 to 1.000. Improvements were directionally consistent across ten metrics on both datasets, and the largest per-category gains occurred precisely where zero-shot competence was absent.

---


### 288. [EEG-AS: Instance-Level Foundation Model Selection for EEG Foundation Models via Behavior Reconstruction](https://arxiv.org/abs/2609.00653)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yunzhen Zhang, Ruoxi Piao, Hasan Onur Keles 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) is a non-invasive technique for measuring neural activity and has been widely used in neuroscience applications. Recent advances in EEG foundation models have enabled strong performance across diverse neural decoding tasks. However, no single foundation model consistently performs best across datasets or individual EEG instances, while instance-level model selection remains largely unexplored. To address this limitation, we formulate EEG foundation model selection as an instance-level Algorithm Selection (AS) problem. We propose \textbf{EEG-AS}, an instance-level algorithm selection framework that characterizes each EEG instance using inference-available latent EEG embeddings, handcrafted neurophysiological features, and an anchor foundation model. During training, EEG-AS learns to reconstruct unavailable foundation-model behaviors from privileged prediction tokens conditioned on an anchor foundation model, while during inference it estimates these behaviors without executing the entire model portfolio, enabling efficient selection from seven EEG foundation models. Experiments on seven public EEG benchmarks demonstrate that EEG-AS substantially narrows the gap between the Single Best Solver (SBS) and the oracle upper bound for each instance. These results highlight the effectiveness of instance-level AS for adaptive deployment of EEG foundation models.

---


### 289. [Physically Plausible Video Generation via Visual-Semantic Chain-of-Events Conditioning](https://arxiv.org/abs/2609.00656)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zixuan Wang, Yixin Hu, Wen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physically Plausible Video Generation (PPVG) seeks to synthesize videos consistent with physical principles, yet remains challenging due to underspecified natural language conditioning. Advanced chain-of-thought (CoT) frameworks augment prompts with physical knowledge. However, such prompts describe physical phenomena holistically, overlooking intermediate states and transition dynamics. In this paper, we reformulate PPVG as event-centric generation by representing physical evolution as a chain of causally connected and physically constrained events. Our framework comprises three key modules: (1) Physics-driven Event Chain Reasoning. This module decomposes physical phenomena into causally connected events represented by evolving scene graphs. Formula-derived physical quantities are bound to relevant objects and interactions, characterizing the direction and magnitude of each event transition. (2) Transition-aware Routed Keyframe Conditioning. This module routes each event to a specialized keyframe synthesis operator for appearance variation or object transformation. Consecutive keyframes are injected as residual guidance during denoising, enabling smooth visual transitions between event-boundary states. (3) Physics-injected Contrastive Semantic Guidance. This module constructs physics-informed positive and counterfactual negative prompts for classifier-free guidance, steering generation toward plausible dynamics and away from physics-violating counterparts. Experiments on PhyGenBench, VideoPhy, PhyWorldBench, and Physics-IQ demonstrate that our framework generates videos with superior physical plausibility across diverse domains.

---


### 290. [Do Satellites See Commuters? A Critical Benchmark of Vision Foundation Models](https://arxiv.org/abs/2609.00661)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ashiq Shukoor Iqbal, Wilson Wongso, Flora D. Salim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite foundation models offer a globally available alternative to census data for commuting origin-destination (OD) generation, yet no study has systematically compared encoder paradigms within a single downstream pipeline. We ablate four satellite vision encoders: language-supervised (RemoteCLIP), self-supervised (DINOv3), and geographically grounded (SatCLIP, AlphaEarth) within an identical WeDAN graph diffusion framework across 1,925 US counties, 325 UK districts, and 14 global cities under five random seeds. Three main findings emerge. First, language-supervised features achieve the strongest in-distribution performance (RemoteCLIP CPC 0.602), while geographically grounded encoders transfer more reliably zero-shot: AlphaEarth improves CPC by 33% over RemoteCLIP on UK districts. Second, pretraining corpus scale alone is insufficient: DINOv3, trained on a substantially larger satellite corpus, underperforms RemoteCLIP by 0.091 CPC in-distribution and collapses to CPC 0.022 globally. Third, no encoder transfers usefully to global cities (best CPC 0.122 for RemoteCLIP, 0.022 for DINOv3), confirming cross-continental OD generation remains an open problem. We additionally clarify the semantics of the census noise parameter $\eta$, whose ordering reverses under cross-continental evaluation, a distinction critical to correctly interpreting prior results. Training scripts and evaluation logs will be released.

---


### 291. [FTU-Seek: Foundation Model-Guided Hard-Negative Learning for Sparse Functional Tissue Unit Segmentation](https://arxiv.org/abs/2609.00704)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zonghao Liu, Lei Su, Jiguang Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Functional tissue units (FTUs), including tertiary lymphoid structures (TLSs), blood vessels, and glands, encode localized immune, vascular, and epithelial organization in histopathology. Accurate quantification of these structures is important for studying tissue architecture and disease-associated tissue organization. However, FTUs are frequently sparse, heterogeneous, and surrounded by large amounts of morphologically similar background tissue, making automated segmentation in whole-slide images (WSIs) challenging. We therefore developed FTU-Seek, a pathology foundation model-guided framework that treats morphology-aware negative-patch selection as a key component of sparse FTU segmentation. FTU-Seek uses frozen multi-depth features from the UNI pathology foundation model to train a patch-level classifier that distinguishes FTU-containing from FTU-absent tissue. Target-absent patches are subsequently ranked according to their predicted target-containing probabilities, and the highest-scoring hard negatives are selected through a static Top$K$ strategy to construct compact segmentation training sets. The framework was evaluated using five-fold cross-validation and internal test cohorts across TLS, blood-vessel, and gland segmentation tasks, with an additional independent 30-WSI held-out cohort for TLS. Positive-only, all-tissue, random-negative, and matched random Top$K$ sampling strategies served as comparators. Segmentation-derived phenotypes were further explored in external TCGA cohorts.

---


### 292. [Jailbreaking Text-to-Image Models Through Cracks: Navigating Heterogeneous Safety Filters via Multi-Agent Debate](https://arxiv.org/abs/2609.01168)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kaiyan Wen, Shijie Zhang, Lu Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text-to-image (T2I) models remain vulnerable to jailbreak attacks that elicit Not-Safe-For-Work (NSFW) content, despite increasingly being guarded by heterogeneous, multi-layer safety stacks combining text filters, image classifiers, and cross-modal detectors. Existing jailbreak studies either optimize against individual filters or query the complete pipeline with aggregate feedback, making it difficult to identify the active constraint and adapt to conflicts across safety this http URL this paper, we introduce the \emph{Detection Surface}, a unified geometric framework that characterizes the decision boundaries induced by heterogeneous T2I safety filters and their joint effect on the jailbreak search space. This formulation reveals that successful evasion is governed by a sparse and non-convex region shaped by cross-layer conflicts, where mutations that bypass one filter may increase exposure to another. Motivated by this analysis, we propose \emph{CRACK}, a multi-agent debate framework for adaptive jailbreak search that decomposes jailbreak search into exploration, diagnosis, and arbitration. CRACK coordinates an Attack Agent, a Defense Agent, and a Judge Agent to iteratively generate prompt mutations, obtain layer-specific diagnostic feedback, and optimize mutation strategies through reward-guided refinement. Through repeated rounds of debate, CRACK adapts its search direction to the evolving cross-layer constraints while preserving the original harmful intent. Extensive experiments across multiple T2I models, datasets, and safety configurations show that CRACK achieves Attack Success Rates (ASR) of up to 99.63\% under composite defenses, while requiring fewer queries than existing methods and maintaining semantic fidelity.

---


### 293. [CMRVision: A Foundation Model for Cardiac MR Image Analysis](https://arxiv.org/abs/2609.01308)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Athira J. Jacob, Puneet Sharma, Daniel Rueckert  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cardiac magnetic resonance (CMR) imaging provides complementary information on cardiac anatomy, function, and tissue characterization across multiple sequences and views. In this work, we investigate foundation model pretraining for 2D CMR and introduce CMRVision, a CMR-specific foundation model trained using DINOv3-style self-supervised learning on a multi-center, multi-sequence cohort of 36 million CMR images. We systematically evaluate architectural and training design choices for domain-specific pretraining. CMRVision is evaluated on two downstream tasks: multi-task segmentation across cine, late gadolinium enhancement (LGE), and mapping sequences, and cine view classification. Our experiments show that CMR-specific pretraining, smaller patch sizes, and patch-level objectives consistently improve downstream performance. Across a multi-task segmentation benchmark, CMRVision achieved the strongest overall performance, outperforming prior natural-image (NI), medical-image, supervised, and CMR foundation model baselines. Improvements were modest but consistent across structures and sequences, with Dice scores ranging from 0.940-0.967 for LV and 0.855-0.905 for myocardium, and reaching 0.929 for RV, 0.920 for LA, and 0.931 for RA. The largest gains were observed for myocardium segmentation in LGE and mapping images. In a zero-shot segmentation task on unseen LGE long-axis views, the model achieved an average Dice score of 0.692, demonstrating cross-view generalization. For cine view classification, CMRVision achieved the highest average accuracy (0.906), compared to prior methods reported in the literature. These results highlight the potential of CMRVision to support robust and generalizable cardiac MRI analysis across multiple sequences and views.

---


### 294. [Diffusion as a Training Curriculum for Timestep-Free Iterative Reasoning](https://arxiv.org/abs/2609.01449)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Mariia Drozdova, Aidan Sirbu, Pietro Miotti 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models and recursive reasoners are both iterative, but they carry information across iterations differently. We add a persistent hidden state to a diffusion denoiser and remove its timestep conditioning, leaving a single shared update that can be run to arbitrary depth. The result is an anytime solver: accuracy keeps improving with inference depth far beyond the rollout lengths and backpropagation window used in training, reaching 99.90% exact solve on Sudoku-Extreme. We also obtain 98.93% solve rate on Maze-Unique. Surprisingly, progressive denoising is unnecessary at inference: holding corruption at its maximum by replacing every non-clue variable with fresh Gaussian noise at each step retains near-perfect solving and converges to stable solutions. This simple noise-injection mechanism enables a single trajectory to efficiently explore the solution space and settle on the correct answer without parallel rollouts, candidate selection, or external verifiers required by prior reasoning models. Nonetheless, ordered annealed corruption remains critical during training, which suggests that diffusion's primary contribution to our anytime solver is not a sampling procedure at inference, but a denoising training curriculum.

---


### 295. [What, Where, and How: Probing Spatiotemporal Representations in Video Foundation Models](https://arxiv.org/abs/2609.01551)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Sharon S. Musa, Fereshteh Forghani, Harrish Thasarathan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised video foundation models learn rich spatiotemporal representations, yet it remains unclear what visual concepts these representations encode, where they emerge across transformer layers, and how they are geometrically organized. In this work, we tackle these three questions through a systematic layer-wise analysis of V-JEPA 2 and VideoMAE-v2. We leverage lightweight probes trained to discover three temporally grounded properties: (i) camera motion understanding, (ii) intuitive physics, and (iii) anomaly detection. Both models encode camera motion, with best results ($>90$ ROC AUC) emerging at 60-70% of network depth, and achieve moderate anomaly detection performance ($>60$ ROC AUC), but remain near chance on intuitive-physics tasks, suggesting a limited encoding of deeper physical reasoning. Beyond classification, we find that temporal features from individual videos form smooth low-dimensional trajectories in representation space, suggesting that camera motion is not only linearly decodable but also geometrically organized. Based on these results, we apply geometry-aware spline-based steering in the model's latent representations to interpolate camera motion, yielding steered videos with smoother trajectories and more coherent temporal progression than linear interpolation.

---


> [!TIP]
> 当前位于：**251-295**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-295**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
