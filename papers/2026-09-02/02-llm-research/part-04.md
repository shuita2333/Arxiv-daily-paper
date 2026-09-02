# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

---

### 151. [SpatialTrust: A Benchmark for Environmental Risk Recognition in Secure Authentication](https://arxiv.org/abs/2608.29489)

**<font color=#1a73e8>作者：</font>** Junbin Lu, Hsiang-Wei Huang, Saesha Wadhwa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Visual environmental risk recognition plays an important role in secure authentication, where a user's surroundings may reveal sensitive information or introduce potential security risks. However, existing evaluations of multimodal large language models (MLLMs) rarely examine whether models can reliably recognize, localize, and explain such risks in spatially grounded authentication scenarios. We present SpatialTrust, a question-answering benchmark for evaluating environmental risk recognition in secure authentication. SpatialTrust assesses five complementary abilities: sensitive factor detection, direct factor identification, indirect factor identification, direct factor explanation, and indirect factor explanation. We evaluate both proprietary and open-source MLLMs and find that current models show limited performance, especially in understanding and explaining indirect risks, indicating that spatial risk awareness remains a challenging capability for MLLMs. In addition, we introduce SpatialTrustGuard, a structured QA-and-audit pipeline that improves Qwen3-VL-30B-A3B-Instruct from 36.78% to 41.12% overall. Our findings highlight the need for dedicated benchmarks and structured inference methods to improve the trustworthiness of MLLMs in secure authentication.

---


### 152. [CoCoA: Context-Conditional Cultural Alignment for Large Language Models](https://arxiv.org/abs/2608.29492)

**<font color=#1a73e8>作者：</font>** Kyungdon Lee, Wei Xu, Alan Ritter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often favor Western-associated entities across cultural contexts. Conventional debiasing methods aim for uniform neutrality, but cultural bias mitigation demands context-conditional behavior, preferring culturally appropriate entities when cultural cues are present and remaining neutral when they are absent. We propose CoCoA (Context-Conditional Cultural Alignment), a framework that learns this behavior through dual-context training on the same entity pairs under contexts with and without cultural cues. CoCoA combines a contrastive alignment objective with calibration and drift regularization, optimized through goal-aware gradient reconciliation. We evaluate CoCoA on CAMeL and Camellia, two entity-centric cultural bias benchmarks, across ten language settings and four LLMs. CoCoA reduces the Cultural Bias Score from 43 to 24 on average while maintaining near-neutral preferences at 50.2, with minimal impact on general performance across five standard benchmarks. These findings highlight that effective cultural alignment requires context-conditional modeling rather than uniform debiasing, and establish a new direction for mitigating entity-centric cultural bias in LLMs.

---


### 153. [LLM Judges as Raters: A Pre-Registered Audit of Severity, Halo, Reliability, and Version Instability in LLM Essay Scoring on Public Corpora](https://arxiv.org/abs/2608.29517)

**<font color=#1a73e8>作者：</font>** Veerendra Kumar Sunkavalli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as essay graders in learning analytics, evaluated almost exclusively with agreement statistics. Educational measurement warns that raters also differ in severity, show halo, and drift as instruments. We treat LLM judges as raters and run a pre-registered rater-effects battery (many-facet Rasch severity, residual halo, generalizability/decision studies, cross-version shifts, differential functioning) on public corpora in two languages (ENEM/Essay-BR; ASAP): 2,377 essays, 12 judges, 4 providers, 5 version contrasts, replicated cells, released as a score tensor. Judge severity spans 219 points on ENEM's 0-1000 scale; on ASAP the panel spread is 15-33% of the score range against a between-trained-human gap near 1%. Judge-human correlations sit in an undiscriminating .47-.56 band. All five version contrasts shift severity beyond a family-wise permutation null (up to 133 points), and one judge was deprecated mid-study, caught by identity canaries. Two pre-registered tests returned honest nulls: severity-adjusted leaderboard reversals did not survive a permutation null, and "silent drift" was refuted: agreement moved with severity in four of five contrasts. Replication yields self-consistency (phi>=.80 at k<=2) but not human-level accuracy, and a same-instrument check overturned our own halo comparison: matched on instrument and calibration, we find no credible evidence that judge halo exceeds the trained-human range.

---


### 154. [Argument-Aware Semantic Alignment of Normative Texts: A Toulmin-Based Neuro-Symbolic Approach](https://arxiv.org/abs/2608.29529)

**<font color=#1a73e8>作者：</font>** William Schroeder  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic alignment between specialized normative texts is challenging when equivalent requirements use different terms, syntax, and levels of abstraction. Lexical overlap, distributional embeddings, and semantic similarity capture topical relatedness but often miss the argumentative structure by which normative claims are supported, qualified, and justified. This paper asks whether explicit argument structure adds information complementary to neural semantics for aligning requirements. We treat cross-standard control mapping as argument-aware semantic alignment and build a neuro-symbolic pipeline that combines neural text representations with Toulmin features. An LLM explicitation step identifies claims, grounds, warrants, qualifiers, and backing and reconstructs enthymemes. These feed an alignment model via argument-aware similarity and structural features. On a NERC-CIP to NIST-CSF mapping benchmark, argument-derived features improve alignment over a neuro-symbolic semantic baseline. Feature selection shows especially strong signal from warrant-related features, indicating that the link between a claim and its supporting reasoning is not captured by conventional similarity alone. A compact claim--grounds--warrant subset remains competitive with the full Toulmin feature set. The results give preliminary evidence that argument structure is a useful intermediate representation for aligning specialized normative texts. Cybersecurity standards are used as a controlled testbed, not as proof of domain-independent generalization. The argument graphs produced by LLM explicitation may also support later work on retrieval, reasoning, and explanation over normative text.

---


### 155. [The Emergent Symbolic Structure of Artificial Neural Networks](https://arxiv.org/abs/2608.29530)

**<font color=#1a73e8>作者：</font>** R. Thomas McCoy, Paul Soulos, Tal Linzen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern systems in artificial intelligence (AI) somehow excel in domains for which they seem poorly suited. Intelligence has traditionally been modeled as operating over structured combinations of symbols, such as logical formulas. However, the strongest modern AI systems are based on neural networks, which instead represent information in continuous vectors. Vectors seem inadequate for capturing the structure of language, logic, and other cognitive domains, yet neural networks achieve impressive performance in these areas. How do they do it? In this work, we propose a potential answer: Despite appearances, perhaps the internal representations of neural networks implicitly realize symbolic structure. In support of this hypothesis, we show that the vector representations of a variety of neural networks can be closely approximated with symbolic structures: we can replace the network's entire representation-generating process with a closed-form equation instantiating a symbolic structure, and the network's behavior remains largely unchanged. This finding holds for both small-scale neural networks trained to manipulate lists as well as large language models (LLMs) operating in four domains that are central in symbolic traditions: arithmetic, logic, computer code, and language. Further, our symbolic approximation allows us to modify an LLM's behavior in targeted ways via precise interventions on its internal representations, showing that the LLM's behavior is reliant on the symbolic structures we have identified. This work provides a potential way to reconcile longstanding symbolic conceptions of intelligence with the vector-based nature of modern AI.

---


### 156. [LoGo: Token-Level Dynamic Local-Global Attention](https://arxiv.org/abs/2608.29539)

**<font color=#1a73e8>作者：</font>** Yuqi Pan, Zheng Li, Bohao Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As context lengths scale, attention increasingly becomes a primary computational bottleneck in large language models. Standard Transformers remain powerful but computationally inefficient, as they allocate the same attention budget to every token regardless of its contextual demand. Existing local-global hybrids provide a more efficient alternative by mixing restricted- and full-context attention, but they typically allocate span statically across layers or heads. To address these limitations, we propose LoGo, a token-level dynamic local-global attention mechanism that uses attention span as a direct proxy for attention budget allocation. Each LoGo layer contains coupled local and global branches: all tokens receive efficient local attention over a restricted context window, while a learned gate activates global attention with full-context access only for tokens requiring long-range information. A threshold-based budget controller maintains a target global ratio without auxiliary losses, and a progressive masking schedule stabilizes training before sparse routing takes effect. We further implement query-sparse Triton kernels that convert reduced global-attention computation into practical speedups. Extensive experiments validate LoGo's effectiveness, showing that it preserves the scaling behavior of full-attention Transformers across model sizes. In controlled comparisons, LoGo improves over the full-attention Transformer and matched-budget static local-global hybrids, with clear gains on long-range retrieval. Analysis further shows that LoGo learns interpretable span allocation patterns. These results suggest that learned token-level span allocation is an effective and scalable way to improve the long-context performance-compute trade-off.

---


### 157. [Evaluating LLMs on Conversational Text-to-SQL under Chain Ambiguity and Intent Drift](https://arxiv.org/abs/2608.29543)

**<font color=#1a73e8>作者：</font>** Yujia Liu, Jiayan Lin, Zijin Hong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have established conversational text-to-SQL as a practical interface between users and databases, often involving multiple turns of clarification and revision. However, existing benchmarks primarily evaluate execution accuracy, leaving the unfolding and shifting of user intent across turns largely uncovered. To address this, we introduce TIDE-Bench, a benchmark for conversational text-to-SQL under chain ambiguity and intent drift evaluation, targeting two recurring patterns: chain ambiguity, where an underspecified question triggers layered clarification with conditional dependencies, and intent drift, where the user retracts and replaces a previously committed request element. Built on 514 anchor SQLs from BIRD, TIDE-Bench comprises 1,542 samples and introduces dedicated metrics for chain identification and drift recognition-resolution beyond execution accuracy. Evaluating 12 advanced LLMs reveals a persistent chain identification bottleneck unaffected by clarification frequency, a wide drift recognition-resolution gap, and overlap between failure modes when jointly activated. The corresponding code of TIDE-Bench is released for further research.

---


### 158. [Towards Effective Generation of Interactive Visualizations with Vibe Coding: An Empirical Study](https://arxiv.org/abs/2608.29550)

**<font color=#1a73e8>作者：</font>** Yanshan Zeng, Ruixuan Tu, Zuo Xiang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Constructing interactive visualizations has traditionally required substantial human effort, involving both technical implementation and design decision-making. Recently, vibe coding, a programming paradigm leveraging Large Language Models to generate, interpret, and refactor code from natural language specifications, has emerged as a promising approach to reduce the burden. However, the capabilities and limitations of vibe coding in building interactive visualizations remain unexplored. To address this gap, we conducted a user study with 78 participants that were tasked with constructing interactive visualizations using vibe coding. We further collected users feedback through questionnaires, interviews, and case analyses. Based on this study, we examine (1) the capabilities and (2) user experience of vibe coding in generating interactive visualizations, and (3) the practical human-agent collaboration strategies adopted. Our findings provide the first systematic assessment of vibe coding for interactive visualization construction, revealing both its strengths and limitations, explaining the shift in developer labor and identifying the hybrid collaboration strategies participants adopted. Furthermore, our study offers insights for more intuitive and robust vibe coding practices.

---


### 159. [Which LLM for Which Work? Budgeted Model Allocation under Uncertain Evaluation](https://arxiv.org/abs/2608.29560)

**<font color=#1a73e8>作者：</font>** Hamed Khosravi, Xiaoming Huo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A company with a fixed artificial intelligence (AI) budget must decide which large language model (LLM) handles each recurring workload. What it lacks is the quality table, how well each model performs on each workload. Given that table, the decision is a multiple-choice knapsack problem and is routine to solve, so estimating it is the difficulty, and that estimation fails in two ways. Models are rarely compared on the same work, and the recorded score is usually a proxy rather than the outcome the company values. Causal and off-policy methods repair the first but condition on the second, while evaluator-validation methods estimate the second but stop short of the decision. Worse, buying more re-evaluation cannot settle the second: randomization governs which requests are scored, not how a score is produced, so the table stays uncertain however much evaluation is purchased. Yet the deployment decision may still be determined even when the table is not. We therefore ask whether one assignment stays optimal across every quality table consistent with the evidence. For the fixed-budget problem, this admits an exact two-solve certificate: solve once at the estimated table and once at a least-favourable table. Agreement certifies the assignment; disagreement identifies the model-workload pairs where further evidence can matter. We propose CASE (causal active sequential experimentation), which targets evaluation to those pairs and repeats the test as evidence accumulates. On a production log, the measurement failure is the larger of the two: correcting assignment exactly still leaves most of the loss, and randomized re-evaluation does not remove it. In our experiments, the available evidence often does not determine the assignment. On paid software tasks, better information about model quality yields more savings than further optimization of the assignment on the same estimates.

---


### 160. [OASIS: Optimizing Attacker Sequences for Hard-Label Black-Box Text Attacks](https://arxiv.org/abs/2608.29568)

**<font color=#1a73e8>作者：</font>** Qian Chen, Shiliang Xiao, Yuzhi Liang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Different attack methods follow different search trajectories, they succeed on different subsets of samples, whereas existing hard-label black-box text attacks mainly focus on improving individual attackers or manually combining them. We present {\OURS}, a method for optimizing attacker sequences in hard-label black-box text attacks. {\OURS} first performs a one-time bi-objective attack chain search over candidate sequences to balance attack success rate and perturbation, and then reuses the selected fixed global chain during attack chain execution. Experiments across multiple datasets, victim models, and large language models show that {\OURS} consistently outperforms strong standalone baselines and simple manually constructed chains. These results suggest that attacker composition is not merely an implementation choice, but a practical optimization target for improving hard-label black-box text attacks.

---


### 161. [Which one is banana man? Evaluating vision-language models in multi-turn pragmatic interpretation](https://arxiv.org/abs/2608.29571)

**<font color=#1a73e8>作者：</font>** Alvin Wei Ming Tan, Ben Prystawski, Veronica Boyce  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Flexible adaptation to context and shared pragmatic intuitions contribute to smooth human conversation. Iterated reference games---in which players repeatedly pick out novel referents using language---present a test case for agents' ability to perform context-sensitive pragmatic reasoning in multi-turn linguistic environments. We tested humans and vision--language models on their ability to identify the intended meaning of descriptions produced in iterated reference games, varying the provided context in terms of amount, order, and relevance. While humans performed well consistently, the models we evaluated could make use of prior context to interpret humans' referring expressions, but they struggled to build up the relevant context to interpret those expressions effectively. Our results suggest that the models we evaluated lack core skills needed for efficient linguistic collaboration.

---


### 162. [SemTrace: Source-Grounded Semantic Signatures for Tracing LLM Exposure to Protected Documents](https://arxiv.org/abs/2608.29575)

**<font color=#1a73e8>作者：</font>** Junyan Zhang, Yudong Zeng, Yongwei Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to read documents and produce downstream text, creating a provenance problem when the document owner cannot control or inspect the model that performs the generation. We introduce SemTrace, a source-grounded semantic watermark for detecting whether a generated review was influenced by a known protected manuscript copy. Rather than biasing token probabilities or imposing surface-form patterns, SemTrace constructs a document-specific binary signature from factual propositions that are directly supported by the manuscript itself. A protected PDF invisibly carries a content contract that selects one fact from each binary pair and asks an instruction-following reviewer to express those facts in fixed review slots without changing its independent evaluation. A frozen natural language inference model then decodes the resulting semantic evidence with explicit erasures and scores the recovered bits against the codeword assigned to that copy. This design targets model-agnostic, assigned-copy exposure detection while keeping the watermark semantically tied to the source document.

---


### 163. [Predicting the Unpredictable: LLM-powered Long-term Chaotic Time Series Forecasting under Short-term Observations](https://arxiv.org/abs/2608.29579)

**<font color=#1a73e8>作者：</font>** Yuhang Yao, Bohan Jiang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chaotic time series forecasting is a challenging task due to its sensitivity to initial conditions and long-term unpredictability. Traditional methods typically rely on sufficient temporal trajectories to learn long-term dynamics, which limits their applicability when only short-term observations are available. While recent Large Language Models (LLMs) have shown great potential for time series forecasting, their temporal representations are not explicitly tailored to the phase-space structure and nonlinear evolution of chaotic systems. To address these issues, we propose PAC-LLM, a phase-space-aware adaptive fusion framework for long-term chaotic time series forecasting powered by LLMs. PAC-LLM leverages learned phase-space features and textual information to fully enable LLM's time series forecasting capacity. In particular, we design an auxiliary feature module and a gated weighting mechanism for multivariate coupling information fusion and selection. Extensive experiments on representative chaotic systems demonstrate that our method outperforms existing fine-tuned and zero-shot baselines in both short-term and long-term predictions. Our ablation study further confirms the effectiveness of each key component in PAC-LLM.

---


### 164. [SUP-MIMIC: A Multi-Task Clinical Diagnosis Benchmark for Evaluating LLMs' Robustness to Contradictory Evidence](https://arxiv.org/abs/2608.29582)

**<font color=#1a73e8>作者：</font>** Yi Yu, Bo Wang, Chong Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current evaluations of large language models (LLMs) primarily focus on factual knowledge retrieval, overlooking the fundamental challenge of navigating the complex, non-bijective mappings between clinical indicators and diagnoses. Existing benchmarks fail to assess whether large language models truly possess the reasoning capability required for diagnostic ambiguity scenarios, where identical clinical presentations may correspond to different etiologies, and diagnostic convergence scenarios, where heterogeneous symptoms ultimately indicate the same disease. To address this issue, we propose SUP-MIMIC, a multi-task framework utilizing MIMIC-IV-v3.1 that comprises Basic Assessment (BA), Diagnostic Divergence Task (DDT), and Diagnostic Convergence Task (DCT). Specifically, DDT is designed to evaluate the model's "one-to-many" disambiguation capability among phenotypically similar cases, while DCT assesses the model's ability to identify "many-to-one" diagnostic patterns across different pathophysiological pathways. Comprehensive evaluation of state-of-the-art LLMs reveals substantial performance degradation on DDT and DCT compared to baseline tasks, exposing a systemic reliance on statistical shortcuts over genuine causal reasoning. Our findings further highlight a conservative bias toward "healthy" predictions, implying non-trivial risks for missed diagnoses in realistic medical settings. This work establishes a rigorous methodology for quantifying clinical reasoning robustness and provides a roadmap for enhancing the safety of language models in clinical medicine.

---


### 165. [Call Neighbours Yourself: Graph Walks with Destination-Conditioned On-Policy Self-Distillation](https://arxiv.org/abs/2608.29588)

**<font color=#1a73e8>作者：</font>** Yilun Liu, Boyu Luo, Yanran Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning over text-attributed graphs (TAGs) requires large language models (LLMs) to combine a node's text with evidence distributed across its neighbourhood. Existing methods fix the set of accessible neighbours before generation, forcing reasoning to operate over a static context and preventing the model from acquiring missing evidence during inference. We argue that neighbour selection should itself be part of the reasoning process. To this end, we propose Call Neighbours Yourself (CNY), a framework that enables LLMs to proactively explore graph neighbourhoods through topology-constrained graph-walk actions. Instead of reasoning over a pre-selected neighbour set, CNY exposes lightweight neighbour previews and learns when to expand candidate neighbours for additional evidence. To address the delayed-credit challenge of neighbour exploration, we introduce destination-conditioned on-policy self-distillation, which retrospectively evaluates a selected neighbour after its content is revealed and converts the resulting change in action preference into an action-level training signal. Experiments on standard TAG reasoning benchmarks under a unified raw-text setting show that CNY consistently outperforms fixed-context post-training baselines. Furthermore, the learned exploration policy transfers to unseen graphs and to a graph-level task not encountered during training. Code is available at this https URL.

---


### 166. [How You Ask Shapes What You Get: A Theory-Seeded Measurement of Articulation in Advice-Seeking LLM Conversations](https://arxiv.org/abs/2608.29591)

**<font color=#1a73e8>作者：</font>** Juneha Baek, Suhyeon Lee, Donghyuk Shin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Users articulate the same advice-seeking request in different ways: some specify detailed constraints, others gesture at a vague need. Prior work treats this variation as noise to be averaged away; we instead treat it as a stable, measurable structure in the input distribution. We ask whether articulation (how people ask) forms latent dimensions separable from topic (what they ask about), and whether it is associated with how language models respond. We extract interpretable features from 16,447 advice-seeking prompts pooled from public chat corpora (WildChat, LMSYS, and ShareChat) and recover a small set of latent articulation factors that replicate across train/test splits and across corpora. Because this structure is largely separable from topic, the populations it defines cut across topics and stay invisible to topic- or task-based evaluation. The factors define a handful of recurring articulation styles, one of which stands out: a long-form but information-poor style, roughly one in six prompts in the largest corpus, where models return shorter, vaguer answers and do not ask for clarification even though under-specification is exactly the condition that warrants it. The contrast holds within every topic group and length quintile, and is not under-specification alone -- a second, equally under-specified style does draw clarifying questions. Two independent human annotators reproduce this contrast. We argue that benchmarks should stratify on articulation, and we offer the extracted structure as a measurement instrument for doing so.

---


### 167. [Towards a Systems Foundation for Agentic Skills: Architecture, Lifecycle, and Security](https://arxiv.org/abs/2608.29596)

**<font color=#1a73e8>作者：</font>** Sanket Badhe, Deep Shah, Priyanka Tiwari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous large language model (LLM) agents increasingly face reliability, context consumption, and execution stability bottlenecks when deployed on complex, long-horizon tasks. While monolithic prompt engineering and stateless tool-calling paradigms struggle to scale, the field is rapidly converging toward \emph{agentic skills}: modular procedural abstractions that externalize execution knowledge into reusable, executable, and portable artifacts. This paper establishes a unified systems foundation and reference architecture for the agentic skills ecosystem. We formalize skills as externalized procedural knowledge bridging high-level cognitive planning with deterministic execution environments, and systematically delineate the architecture across a nine-stage lifecycle: autonomous discovery, authoring and representation formats, memory storage, dynamic retrieval and routing, composition and orchestration, execution and repair, lifelong adaptation, empirical evaluation, and security governance. We further examine marketplace dynamics, public registries, and emerging adversarial threat vectors, alongside runtime verification and defense mechanisms. Finally, we categorize system implementations across software engineering, operating system navigation, embodied robotics, and scientific discovery, while highlighting critical open challenges in continual learning and benchmark realism. This work establishes agentic skills as a foundational paradigm for building scalable, robust, and verifiable autonomous language agents.

---


### 168. [Hindsight Memory-PRM: Supervising Memory Management with Auditable Hindsight Credit](https://arxiv.org/abs/2608.29605)

**<font color=#1a73e8>作者：</font>** Haoxuan Jia, Yang Liu, Yingguang Yang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory operations of long-horizon LLM agents are hard to supervise: an operation's value is unobservable when it is taken. But they are special -- they leave machine-readable evidence in the trajectory: retrieval hits and answer-time citations. Hindsight Memory-PRM exploits this audit trail twice: offline to train an operation-conditioned memory-utility critic, and online, where retrievals, citations, and one controlled deletion-and-reanswer per probe settle an intervention-calibrated entry-level presence credit, propagated along version chains as an action-level proxy reward -- no per-operation human labels, no Monte-Carlo replay of continuations. On held-out LoCoMo a local 8B policy reaches 77.5% under a fixed shared reader, surpassing its API teacher (65.1%) and all reproduced external systems, at one eighth the context of Mem0's official operating point; on LongMemEval, 79.0%. Ablations attribute the gain to causal calibration rather than signal density, and the policy converges to a multi-version memory organization whose gains no tested open-loop baseline reproduces.

---


### 169. [Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents](https://arxiv.org/abs/2608.29606)

**<font color=#1a73e8>作者：</font>** Ming Wu, Pengyuan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents need durable, faithful memory of everything a user or organization has said and stored, yet most memory systems commit to a single organizing structure (a fact store, a vector index, or a knowledge graph) and inherit its blind spots. We present Agent Zero Memory, a provenance-aware long-term memory system that distils a user's conversations, files, and connected sources into three parallel memory systems, each capturing a different facet of the same history: an episodic Memory Events timeline that makes when and what changed first-class, an associative entity-event knowledge graph that links people and projects across sessions, and a semantic, curated, citation-locked Hierarchical Documentary Memory (HDM) of durable facts. A retrieval turn runs an intent gate (so self-contained turns add no latency), a source router, and three concurrent agentic searches, one per system, each a tool-using loop over hybrid (embedding + lexical) search under agent-controlled filters; their grounded, cited answers are integrated into one answer with a single confidence. We formalize the reading discipline: every learned item is a provenanced item carrying its origin, timestamp, and evidence pointer, and every answer is read under a citation lock, so it may cite only evidence its reader actually opened; fabrication is structurally excluded and the system abstains rather than guesses. On two public benchmarks the system sets a new state of the art: 95.60% on LongMemEval and 93.60% on LoCoMo, improving over the strongest prior systems by +0.73 and +1.10 points. A controlled study across eight backbone LLMs characterizes the accuracy-cost-latency frontier: accuracy varies by only 3.4 points while per-query cost varies by ~30x, with near-state-of-the-art quality at up to 20x lower cost per query, the signature of memory-driven, rather than model-driven, quality.

---


### 170. [SnapBench: Benchmarking Snap-and-Ask Multimodal Retrieval for Mobile Interactions](https://arxiv.org/abs/2608.29607)

**<font color=#1a73e8>作者：</font>** Zirong Chen, Fuda Ye, Kuan Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile AI acts as a visual oracle, empowering users to snap a picture of something and ask for information. Snap-and-ask retrieval is now one of the most common entry points for mobile AI, yet photos are often blurry, while text questions may be short or mistyped. Existing benchmarks only test on clean inputs or do not isolate paired robustness in snap-and-ask retrieval. Therefore, we introduce SnapBench, the first paired benchmark for robust snap-and-ask multimodal retrieval, spanning 1,145 queries, 9,085 gallery items under 53 controlled corruption conditions with human annotations. We evaluate 16 multimodal retrievers, covering dual-tower encoders and embedding-based VLMs. Results show that image corruptions substantially degrade retrieval, while text corruptions mainly affect text-only retrieval and have limited impact on joint retrieval. Clean image-only retrieval often outperforms joint retrieval, indicating the coarse-text drag and the lack of cross-modal fallback under noisy inputs. SnapBench provides a controlled testbed for evaluating robust retrieval in snap-and-ask scenarios. We further propose MOOR (Modality-anchored, Outlier-aware, Optimal Reweighting), a simple adaptive fusion approach, highlighting the need for reliability-aware modality calibration in snap-and-ask retrieval.

---


### 171. [Beyond Surface Alignment: Grounding the Dynamics of Situational Understanding and Generative Control in LLMs](https://arxiv.org/abs/2608.29610)

**<font color=#1a73e8>作者：</font>** Chenghao Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The current alignment tuning paradigm for Large Language Models (LLMs) prioritizes surface-level behaviors -- fluency, safety, and tonal consistency. While effective for casual chat, this thesis argues that such surface alignment masks a lack of grounding, creating models that are stylistically confident but situationally brittle. We propose a framework of Grounded Alignment, analyzing how models process context (Input) and structure generation (Output), then aligning these grounded behaviors to human needs.
First, we evaluate failures in Situational Grounding. SitTest shows that despite large context windows, state-of-the-art models struggle to maintain a consistent "mental model" of a changing environment. ReCode further shows that models rely on surface heuristics rather than deep syntactic dependencies: they "read" extensive histories without truly "understanding" the evolving situation.
Second, we evaluate Generative Grounding. We introduce the Branching Factor (BF) to map LLM generation, finding that standard alignment tuning constricts this landscape into premature stylistic collapse. Hindsight further shows that models often fail to understand their own generations.
Finally, we propose Dynamic Control for grounded interaction. AI Realtor demonstrates context engineering to compensate for poor situational grounding. Base-Aligned Model Collaboration decouples exploration from stylistic constraints. We also present Annealed Sampling for verifiable reinforcement learning and apply these ideas to Addiction Support, where model-generated rationalization offers a communication interface for high-stakes domains. Collectively, this work moves beyond surface alignment toward agents anchored in both context and generation.

---


### 172. [LLMs Interpret, Embeddings Organize, Graphs Emerge: Agent-Driven Compilation of Scientific Knowledge](https://arxiv.org/abs/2608.29612)

**<font color=#1a73e8>作者：</font>** Shi-Ju Ran, Kun Zhang, Xi Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sustained scientific work requires a knowledge substrate that carries interpretation across tasks and preserves paths to source evidence. We call this process \emph{scientific knowledge compilation} and implement it in ASKS, the \emph{Agent-Driven Scientific Knowledge System}. For each source, an LLM produces a readable Wiki view and machine-facing semantics. Deterministic checks convert the latter into a document-local GraphDelta, and embedding geometry together with explicit graph rules integrates the proposed changes into persistent state. Each ingest is an inspectable state transition over accumulated knowledge, with compiled Wiki and graph views linked to the preserved source record. We examine this process by chronologically compiling 56 published papers from one research program. Branch survival, cross-paper support, lineage, coverage, and churn yield a source-traceable author research portrait centered on tensor-network methods, with branches into quantum many-body research, tensor-network machine learning, and quantum-AI-oriented directions. In this run, higher-level Hub organization remains stable and low-churn. Canonical-node growth is predominantly additive. Graph-level measurements and navigation paths retain links to the source records from which they were compiled.

---


### 173. [Cross-lingual Functional Vectors for Emotion Detection in Large Language Models](https://arxiv.org/abs/2608.29613)

**<font color=#1a73e8>作者：</font>** Jieying Xue, Phuong Minh Nguyen, Minh Le Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Function vectors (FVs) have recently emerged as a promising mechanism for steering the behavior of large language models (LLMs) by injecting task-specific latent direction representations derived from in-context demonstrations. While prior studies have shown that FVs can recover task behavior in structured in-context learning settings, their effectiveness on semantically complex tasks and their ability to generalize across languages remain underexplored. We investigate the cross-lingual transferability of FVs using multilingual multi-label emotion recognition as a challenging semantic classification benchmark. Specifically, we examine whether FVs extracted from a source language can steer task behavior in another language under both standard clean and perturbed zero-shot settings without providing demonstrations during inference. Across diverse cross-lingual settings, applying FVs substantially improves performance, suggesting that FVs capture language-agnostic, task-relevant signals rather than purely language-specific lexical patterns, and highlighting their potential as a lightweight and transferable mechanism for multilingual task adaptation. We observe that each LLM exhibits a relatively stable optimal range of attention heads for constructing effective FVs, and the pattern remains consistent across languages. In addition, FVs can partially replicate the task-steering effects of standard few-shot in-context learning while avoiding the computational overhead of processing multiple demonstrations, making them effective for large-scale practical applications. Our code is available at this https URL.

---


### 174. [Forward-Deployed Full-Stack Engineering for Autonomous Cloud MLOps](https://arxiv.org/abs/2608.29615)

**<font color=#1a73e8>作者：</font>** Sagar Srinivas Sakhinana, Venkataramana Runkana  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Across industries, machine-learning systems support applications ranging from prediction and anomaly detection to forecasting, optimization, and scheduling, yet operationalizing these systems requires coordinating application development, model pipelines, cloud infrastructure, security, deployment, monitoring, retraining, recovery, and rollback. We present an evidence-gated multi-agent framework for transforming a natural-language MLOps cloud engineering task into a verified repository and operational cloud deployment. The framework combines graph engineering, loop engineering, and agent harness engineering. A stateful Graph Orchestrator coordinates specialized agents for repository generation, review, execution, verification, release, and monitoring while governing workflow dependencies, evidence gates, retry bounds, recovery paths, and termination. Consequential lifecycle transitions proceed only when their required predicates are supported by verifiable execution or runtime evidence. Verification failures activate bounded reflection, repair, and re-verification, while runtime evidence of failure, drift, degradation, or policy violation can trigger bounded adaptation, recovery, or rollback. Agent harness engineering constrains repository generation, review, and repair, artifact execution, and cloud operations through controlled capabilities and isolated execution environments. We realize the framework on Google Cloud Platform and evaluate repository completeness, controlled execution, evidence-gated transitions, cloud promotion, and bounded recovery. Our experimental results show that the framework prevents unsupported lifecycle transitions and drives each run toward either a verified operational deployment or an auditable terminal failure.

---


### 175. [JPO: Juris Policy Optimization for Structured Legal Reasoning in Criminal Judgment Prediction](https://arxiv.org/abs/2608.29616)

**<font color=#1a73e8>作者：</font>** Zhaolu Kang, Yantao Liu, Tailong Luo 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Criminal judgment prediction requires models to infer statutory articles, charges, and sentencing outcomes from case facts. Unlike standard classification tasks, it involves a structured reasoning process in which statutes should be matched with facts, charges should be justified by statutes, and sentencing outcomes should remain consistent with charges. Existing approaches optimize final labels, and while some have attempted to evaluate reasoning quality, their evaluations are indirect, often relying on LLM-generated rubrics that reflect model-internal preferences rather than the inherent logical structure of legal adjudication. We propose Juris Policy Optimization (JPO), a post-training framework for structured legal reasoning in Chinese criminal judgment prediction. JPO first uses teacher-generated rationales to supervise a standardized four-step reasoning process, and then applies reinforcement learning with a composite reward over legal prediction quality, reasoning structure completeness, and cross-step consistency. JPO further introduces token-level advantage reweighting and adaptive clipping for legally salient reasoning segments. Experiments on multiple open-source language models and three Chinese legal benchmarks show that JPO consistently improves both judgment prediction and reasoning quality over supervised fine-tuning and reinforcement learning baselines.

---


### 176. [Memory-First Fact-Checking: A Knowledge-Graph-Grounded Multi-Agent System for Misinformation Detection](https://arxiv.org/abs/2608.29617)

**<font color=#1a73e8>作者：</font>** Amelia Petrenciuc, Alexandru Lecu, Adrian Groza  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces a hybrid fact-checking framework that integrates Knowledge Graph-based semantic memory with adversarial multi-agent reasoning for explainable misinformation detection. The proposed system follows a memory-first, web-fallback architecture, in which input claims are initially evaluated against a dual-index Knowledge Graph through Sentence-BERT-based semantic retrieval and Natural Language Inference. When the evidence retrieved from the graph is insufficient to support a reliable decision, the framework collects information from trusted web sources and assesses it using an adversarial tribunal composed of support, contradiction, and judging agents. A graph-aware confidence mechanism combines semantic similarity, NLI confidence, and structural graph evidence to determine whether internal knowledge is sufficient, thereby reducing unnecessary web retrieval. Following verification, validated information is transformed into structured triples and incorporated into the Knowledge Graph, supporting the incremental expansion of the system's semantic memory. Experimental evaluation on a curated COVID-19 misinformation benchmark demonstrates that the proposed framework achieves an accuracy of 97.4\% and a macro-averaged F1-score of 92.6% on resolved claims, outperforming a Llama~3.3~70B baseline, which obtains an accuracy of 87.7% and a macro-averaged F1-score of 86.3%.

---


### 177. [CineForge: Self-Improving Agents for Long-Horizon Video Generation](https://arxiv.org/abs/2608.29621)

**<font color=#1a73e8>作者：</font>** Junxiang Liu, Lin Wang, Haiyu Shi 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon story-driven video generation requires a production agent to coordinate narrative decomposition, state tracking, shot design, prompt construction, rendering, and revision across interdependent scenes. Existing adaptive video systems primarily refine requests or reusable skills, leaving recurring production failures disconnected from persistent, stage-targeted improvements across stories. We introduce CineForge, a self-evolving video-production agent framework that couples CineForge-Produce for video generation with CineForge-Evolve for cross-story policy evolution. CineForge-Produce organizes each source story into typed narrative, character, spatial, and cinematic states, uses them to coordinate asset and clip generation, and records the process as a canonical production trajectory. CineForge-Evolve applies Case-to-Pattern-to-Policy Evolution (CPPE) to review trajectory evidence, consolidate recurrent findings into bounded stage-local patches, and deploy validated updates through structural replay and confidence-controlled paired evaluation. To measure complete story realization, we introduce CineScope, which combines a 100-script CineScope-Data suite with a human-aligned, multiscale CineScope-Metric spanning causal state, directorial orchestration, pacing and resource allocation, and character arc. Across CineScope-Data and two public benchmarks, the evolved CineForge policy improves CineScope-Metric from 4.024 to 4.380, outperforms three long-video baselines with consistent gains under ScriptAgent, and reduces review LLM calls by 37.0% on new stories. These results establish production trajectories as actionable experience for video agents that improve cumulatively across long-form storytelling tasks.

---


### 178. [AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step Reasoning, Retrieval and Memorizing](https://arxiv.org/abs/2608.29622)

**<font color=#1a73e8>作者：</font>** Xinke Jiang, Yue Fang, Zhibang Yang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) improves the factuality of large language models (LLMs), yet existing RAG systems often struggle with complex, multi-step reasoning that requires adaptive retrieval and continuous revision of intermediate contexts. Recent reinforcement learning (RL)-based agentic RAG methods partially alleviate this issue, but typically rely on coarse-grained action spaces and trajectory-level rewards, resulting in weak reward assignment and a bias toward short-horizon, stereotyped reasoning template. To address, we propose AgenticRag-R1, a RL framework that deeply integrates reasoning, retrieval, and memory via a memory stack and fine-grained action space, supported by hierarchical action-aware rewards and an information-aware trajectory rejection strategy to enable effective long-horizon learning. Experiments across a diverse set of multi-hop, open-domain, and agentic reasoning benchmarks, spanning multiple backbone model sizes, demonstrate that AgenticRag-R1 consistently outperforms strong baselines. Moreover, AgenticRag-R1 learns more robust, interpretable, and memory-aware reasoning behaviors, highlighting the effect of fine-grained action modeling and information-aware optimization for long-horizon reasoning. Our code is anonymous available at this https URL.

---


### 179. [MI-Distillation: Selecting from Model-Interpolated Instruct-Reasoning Data Spectrum for Chain-of-Thought Distillation](https://arxiv.org/abs/2608.29623)

**<font color=#1a73e8>作者：</font>** Yangsong Lan, Renkai Hu, HongKai Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large reasoning models (LRMs) have shown strong performance on complex problems through long chain-of-thought (Long CoT) reasoning. However, distilling such trajectories into smaller student models remains challenging: direct Long CoT supervision often provides limited gains and can be less effective than concise Short CoT rationales. In this work, we investigate this phenomenon from a gradient-centric perspective. Our analysis shows that Long CoT induces larger gradient magnitudes and more concentrated update directions than Short CoT, with this effect becoming more pronounced as student model capacity increases. These findings suggest that effective Long CoT distillation requires balancing the reasoning information density of reasoning trajectories with their distributional alignment to the student model. Motivated by this insight, we propose \textbf{M}odel \textbf{I}nterporlation \textbf{Distillation} (\textbf{MI-Distillation}), a framework that constructs a continuous Instruct-Reasoning data spectrum through model interpolation. To select suitable trajectories from this spectrum, we further introduce \textbf{Seq}uential \textbf{L}earnable \textbf{S}urprisal \textbf{S}core (\textbf{SeqLSS}), which favors reasoning paths that are both informative and learnable for the student. Extensive experiments on reasoning benchmarks show that MI-Distillation consistently improves small model CoT distillation over strong Long CoT baselines.

---


### 180. [LLMODE: Aligning ODEs with LLMs via Gated Token Injection for Irregular Spatio-Temporal Forecasting](https://arxiv.org/abs/2608.29640)

**<font color=#1a73e8>作者：</font>** Di Zhang, Jingyang Zhang, Ziqian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown promise for spatio-temporal forecasting, but existing approaches often rely on regularly sampled token sequences and struggle with irregular observations because of temporal asynchrony, representation-space misalignment, and limited context windows. We propose LLMODE, a token-efficient framework for irregular spatio-temporal forecasting with a frozen LLM backbone. LLMODE first uses a graph-aware ODE encoder to reconstruct irregular graph observations as a continuous-time latent trajectory. A Fixed-Budget Perceiver Resampler then compresses this variable-length trajectory into a fixed number of dynamic memory tokens. In parallel, compact statistical descriptors are encoded and resampled into context memory tokens. A dual-source gated cross-attention module injects both memories into the frozen LLM, enabling controlled utilization of external spatio-temporal evidence. Experiments on three real-world urban datasets and two physical-dynamics benchmarks show competitive overall performance, with clearer advantages under sparse or dynamically complex irregular sampling. Additional evaluations on unseen urban regions further demonstrate strong zero-shot generalization without adaptation.

---


### 181. [Conducting Stylistic Analysis of Paintings through an Art-History Agent](https://arxiv.org/abs/2608.29644)

**<font color=#1a73e8>作者：</font>** Marc S. Walton, Astrid Harth  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attributing an artwork to an artist has traditionally relied on detailed visual observations and descriptions, known as stylistic analysis in art history. By contrast, current artificial intelligence (AI) models used in the field offer only unexplained probabilistic classifications. To bridge this methodological gap, we present an AI framework that automates stylistic analysis of paintings, providing a foundation for enhancing evidence collection, discovery, and verification. By training a vision transformer (ViT) on a large corpus of paintings with metadata, our system encodes this art history-specific data as embeddings. These representations are factorized via sparse dictionary learning into a shared set of features that recur across the training set. A large language model (LLM) then interprets each feature by retrieving associated artworks and their accompanying curator-written texts, and synthesizes them into descriptions that reflect their stylistic attributes. Finally, an autonomous coordinator LLM applies a reasoning-and-action (ReAct) framework to weight, test, and refine these features into cohesive descriptions of an artwork, or comparisons of artworks. This approach converts detailed visual features into descriptive terms, addressing a key challenge in art history. It thus connects the use of images as data with the semantic concerns of humanists, establishing vision-based computational art history as an area for future growth.

---


### 182. [Detect Before You Attribute: Cascade Failure Attribution for Multi-Agent Systems](https://arxiv.org/abs/2608.29646)

**<font color=#1a73e8>作者：</font>** Jiayi Zhang, Zexin Wang, Degang Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents have shown strong potential in solving complex tasks through multi-step reasoning, yet they remain vulnerable to execution failures. Accurate failure attribution is therefore critical for improving agent reliability. Existing topology- and spectrum-based methods exploit trajectory structures but often overlook fine-grained semantics, while LLM-based attribution methods capture semantic cues but suffer from long-context degradation over lengthy trajectories. To address these challenges, we propose DUOTRACE, a plug-and-play detection filter for LLM-based failure attribution. DUOTRACE follows a detect-before-attribute paradigm: it first detects anomalous executions and then supplies focused trajectory evidence to downstream LLM-based attribution methods. For effective VAE-based anomaly detection on agent trajectories, DUOTRACE integrates dual-view semantic-structural node representations, a Tree-LSTM-based trajectory encoder, and prefix-chain- and LLM-based data augmentation to handle heterogeneous nodes, hierarchical execution structures, and limited failure data. Experiments with six LLM-based attribution baselines show that DUOTRACE improves agent-level and step-level attribution accuracy by 8.7% and 7.0%, respectively.

---


### 183. [ACTD: Anchor-Based Cross-Tokenizer Distillation with Residual Regularization](https://arxiv.org/abs/2608.29662)

**<font color=#1a73e8>作者：</font>** Huiyi Zhang, Zijian Li, Xiaocheng Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation effectively transfers reasoning capabilities from large language models to lightweight student models. To enable knowledge transfer across disparate model families, researchers increasingly explore cross-tokenizer distillation. However, cross-tokenizer distillation remains challenging due to vocabulary and sequence misalignment, while approximate vocabulary alignment can introduce additional noise into distillation. To address these challenges, we propose Anchor-Based Cross-Tokenizer Distillation with Residual Regularization (ACTD). ACTD bridges structural heterogeneity through vocabulary and sequence alignment, while mitigating alignment noise via a novel anchor loss with residual regularization. We further extend this framework to a multi-teacher setting. Evaluated across five reasoning benchmarks with three distinct teacher models, ACTD achieves state-of-the-art performance. Moreover, its multi-teacher extension outperforms the strongest single-teacher and multi-teacher baselines, further demonstrating the robustness of our method.

---


### 184. [PhysVR: Vision-Language Model Guided Interference-aware Temporal Feature Refinement for Remote Physiological Measurement](https://arxiv.org/abs/2608.29663)

**<font color=#1a73e8>作者：</font>** Zixu Li, Jianjun Qian, Hang Shao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) enables contactless physiological measurement from facial videos, yet its subtle pulse-related variations are easily affected by illumination variation, head motion, facial blur, and region-of-interest instability. Existing methods mainly suppress interference during feature learning, while whether the learned temporal features remain affected by interference and how to further suppress such interference before rPPG estimation are rarely examined. To address this limitation, we propose PhysVR, a vision-language model guided interference-aware temporal feature refinement framework for rPPG estimation. Specifically, a physiological backbone produces global temporal features and a coarse rPPG prediction, from which signal-derived physiological reliability evidence is constructed from local temporal characteristics. In parallel, a frozen vision-language model processes sampled facial frames under an interference-oriented prompt, and an evidence head extracts visual interference evidence from the VLM output. Temporal cross-attention integrates the physiological and visual evidence with the global temporal features to construct interference-aware temporal context. Guided by this context, a shared temporal correction unit performs general refinement, while four interference-specific experts selectively suppress different interference through adaptive routing. The refined temporal features are then used for final rPPG estimation. Extensive experiments on five public benchmarks demonstrate that PhysVR consistently outperforms representative methods under both intra-dataset and cross-dataset evaluation protocols.

---


### 185. [A Target-Centric Survey of Quantization-Aware Training](https://arxiv.org/abs/2608.29667)

**<font color=#1a73e8>作者：</font>** Jiamin Song, Mengjie Zhao, Zijing Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid development of LLMs incurs prohibitive memory footprints and intensive computational demands. Quantization-Aware Training (QAT) techniques have emerged as a promising solution to address these challenges by explicitly simulating quantization effects during model training, yielding low-bit models that achieve accuracy comparable to their full-precision counterparts. In this work, we provide a target-centric survey of QAT, aimed at clarifying both its theoretical foundations and its evolving implementation landscape. We systematically review existing QAT methods through a target-centric taxonomy and synthesize cross-target differences in error characteristics, numerical formats, and strategy transferability. We further summarize QAT evaluation paradigms and discuss challenges in optimization and deployment, outlining potential directions for future research.

---


### 186. [Creation begins with understanding: LLMs as strategy designers for privacy-preserving tabular data synthesis](https://arxiv.org/abs/2608.29674)

**<font color=#1a73e8>作者：</font>** Jinmeng Li, Quan Zhang, Hangting Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sharing tabular data in high-stakes domains is constrained by privacy regulations. Synthetic data offer a promising alternative, but deep generative models are costly to train and difficult to audit, while LLM-based methods often serialize records as text, obscuring tabular structure and exposing sensitive data. We introduce Tabular Synthesis Strategy Designer (TabSSD), which uses an LLM to design synthesis procedures rather than directly generate records. TabSSD provides the LLM with tree-derived summaries of variable dependence rather than raw records, which produces Python programs for local execution and evaluation. Across twelve datasets, TabSSD strikes a favourable balance among statistical fidelity, predictive utility, and empirical privacy risk, achieving the best average rank across six metrics among ten methods. Moreover, it substantially reduces local computation and token consumption relative to the compared methods. By enabling human-guided refinement and eliminating user-side model tuning, TabSSD lowers the expertise and infrastructure barriers to transparent tabular data synthesis.

---


### 187. [Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents](https://arxiv.org/abs/2608.29685)

**<font color=#1a73e8>作者：</font>** Zongyue Li, Chengyue Yu, Lei Zang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Early failure prediction is important for long-horizon agents, as it enables timely intervention and can reduce inference and tool-use costs. Uncertainty quantification, such as verbal confidence and perplexity, offers a promising approach to detecting agent failures; however, it has not been explored whether these signals retain their discriminative power during the intermediate stages of long-horizon execution. We evaluate mainstream uncertainty signals on deep-research tasks and find that verbal confidence reliably distinguishes failures at trajectory completion, achieving a mean AUROC of 0.85, whereas all evaluated signals offer limited predictive value earlier in execution, with none exceeding a mean AUROC of 0.60 at 50% trajectory progress. We identify an underlying mechanism explaining this gap: path switching, where agents frequently abandon their current search direction in-trajectory, breaking the link between early signal and final outcome. These findings challenge the assumption that intermediate uncertainty can reliably guide early intervention. They also motivate a practical recommendation for agent harnesses in deep-research settings: use final-step confidence to decide whether to restart, an approach that our experiments find more effective than in-trajectory intervention.

---


### 188. [Ideation Arena: Evaluating LLM Generated Research Ideas with Battle-style Human Expert Assessment](https://arxiv.org/abs/2608.29696)

**<font color=#1a73e8>作者：</font>** Zhiyu Chen, Keyu Zhao, Jigao Fu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating research ideas generated by LLMs is difficult because their scientific value cannot be fully determined by objective criteria, and no single reference answer specifies what counts as a good idea. To address this challenge, we introduce Ideation Arena, a battle style platform that evaluates research ideas through pairwise human assessment. Ideation Arena evaluates ideas generated by 14 frontier LLMs and 5 research agent architectures built on 2 base models. To ensure a common starting point, Ideation Arena builds shared literature contexts from papers familiar to the participating researchers and provides the same contexts to all LLMs and agents. We collect over 6,000 double blind pairwise comparisons from 105 active computer science researchers and construct an Elo rating leaderboard of proposal-stage expert preferences in computer science under a shared closed-context protocol. We validate the rankings through interrater agreement and robustness analyses, showing that the leaderboard remains stable under changes in annotator composition and domain coverage. Our results show substantial variation in agent effectiveness, with some frameworks improving ideation quality over their backbones and others offering little benefit or even underperforming their base models. We further construct Ideation Arena Eval, a benchmark for assessing whether automated evaluators align with human preferences in research ideation. Experiments with current LLM judges show that they still cannot reliably reproduce expert preferences, with the best judge reaching 72.56% Soft Accuracy on Overall Quality. Our code, data, and leaderboards are available at this https URL.

---


### 189. [A Hub of Short Rows Inflates Intrinsic Dimension Estimation of Token Embeddings](https://arxiv.org/abs/2608.29702)

**<font color=#1a73e8>作者：</font>** Alexandre Quemy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A token-embedding table holds a hub of short rows near its origin, and we show that this cluster biases what nearest-neighbor intrinsic-dimension (ID) estimators report. Because of the concentration of measure, a token is closer to the central cluster than to any other token, so its first two neighbors are both hub rows at nearly the same distance. As a result, the ID estimators such as TwoNN return a dimension far above the real ID. Measured one token at a time, dimension is a heavy-tailed distribution. Measured on the full vocabulary, it grows with the model's parameter count. However, when we remove the hub, the heavy tail disappears and the measured dimension collapses to a narrow range for eleven models, from GPT-2 to models such as K3 and GLM-4.7. The hub acts as a switch: a few hundred rows are enough to fully inflate the estimate. We reproduced an experiment stating that the intrinsic dimension (ID) of Pythia's token-embedding table grows with the parameter count, from $27$ to $122$ between 160M and 12B parameters. We show that this result disappears when the hub is removed: the table then reads $10$ to $17$ at every size. The hub contains a subset of the population that under-trained-token detectors flag, but on Pythia the hub that we detected and removed as a whole was updated during training: what seem to characterize these rows is simply their length, not an absence of updates. Finally, we show that normalizing the rows instead of removing them gives the same lower reading.

---


### 190. [DVBench: Benchmarking MLLMs for Understanding Dynamic Charts and Narratives in Data Videos](https://arxiv.org/abs/2608.29711)

**<font color=#1a73e8>作者：</font>** Bomiao Wang, Zekai Shao, Jiexiang Lan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While MLLMs have made significant strides in chart comprehension and video understanding, current evaluations largely isolate these capabilities, leaving a critical gap in understanding temporally evolving structured visual information. To address this gap, we introduce DVBench, a benchmark for evaluating MLLMs on data videos, a storytelling medium that integrates dynamic charts with structured narratives. We decompose data video understanding into five dimensions. DVBench comprises 300 real-world data videos and 1,000 human-verified QA pairs curated through a rigorous semi-automated pipeline. Extensive evaluations of nine MLLMs show that Gemini-3.1-Pro achieves the best overall performance, while Kimi-k2.5 is the strongest open-source model. We further identify two notable phenomena: open-source model performance does not scale strictly with parameter size, and narrative proficiency does not guarantee visual capability. Fine-grained analyses and ablation studies further reveal dimension-specific weaknesses and the effects of frame configurations and subtitle inputs, informing future MLLM development. DVBench is publicly available at this https URL.

---


### 191. [Evaluating the Capabilities of LLMs for Persuasive Dialogue](https://arxiv.org/abs/2608.29738)

**<font color=#1a73e8>作者：</font>** Jordan Robinson, Angus R. Williams, Katie Atkinson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate apparently highly persuasive text, but does sounding persuasive mean arguing well? We introduce \textsc{Persuasio}, a multi-agent dialogue platform grounded in a formal argumentation-based theory of persuasion dialogues that adjudicates logical winners during free-text debates. Using this system, we generated 192 debates on a UK political topic between humans and LLMs, and evaluated 22 interlocutors through both automated adjudication and 9,702 crowdsourced pairwise judgements across 1{,}386 annotation instances. We observed a consistent decoupling between subjective and formal persuasiveness: LLMs dominated the subjective ranking yet performed substantially worse under argumentation-theoretic adjudication, where humans remained competitive. Multi-agent and retrieval-augmented variants further widened this divergence. These findings reveal a systematic gap between rhetorical fluency and formal argumentative strength in LLM-based persuasive dialogues.

---


### 192. [JITterFlip: Uncovering Fault Attack Surfaces in JIT-Compiled LLM Serving](https://arxiv.org/abs/2608.29745)

**<font color=#1a73e8>作者：</font>** Tairui Wang, Zhi Zhang, Yansong Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs are widely deployed through cloud-hosted inference services, where Just-in-Time (JIT) compilation is used to reduce recurring framework and GPU-launch overhead. JIT serving introduces a host-side control plane that selects compiled artifacts and orchestrates their execution on the GPU. Meanwhile, the shared cloud setting has motivated a growing body of bit-flip attacks (BFAs) against LLM/DNN inference. Most existing BFAs target model parameters or weights and require model-specific knowledge. A smaller body of work reduces this dependency by faulting executable code, yet still corrupts code that directly implements model computation, limiting their attack effect to inference depletion.
We present JITterFlip, the first BFA targeting the host-side JIT serving control plane of GPU-based LLM inference. By faulting CPU-resident serving decisions rather than model computation, JITterFlip enables both gibberish output generation and a correct-output sponge attack. To identify exploitable targets in a large JIT compiler stack, JITterFlip develops a decision-guided fault-vulnerable code analysis.
Across four text and multimodal LLM workloads, the identified vulnerable code faults exhibit cross-model transferability, produce gibberish outputs with PPL ratios of $15.45\times$ to $2.48{\times}10^{6}\times$, and demonstrate correct-output sponge attacks with latency amplification of $2.03\times$ to $181.90\times$. JITterFlip also bypasses recent BFA defenses for LLMs while retaining both attack effects. Last, we demonstrate end-to-end Rowhammer attacks across four LLMs: a single bit flip in CPU-resident branch code propagates across the CPU-GPU boundary to disrupt GPU-executed inference without direct access to GPU memory, reaching up to $7.23{\times}10^{6}\times$ PPL amplification or $124.97\times$ latency amplification while preserving the exact generated output.

---


### 193. [ReTrace: Rejected-Trajectory Conditioning for Speculative Decoding](https://arxiv.org/abs/2608.29748)

**<font color=#1a73e8>作者：</font>** Luxi Lin, Zhanpeng Zeng, Shuang Peng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates autoregressive language model inference by having a lightweight draft model propose multiple candidate tokens, which are then verified in parallel by a larger target model. However, after the first rejection, standard prefix-based verification discards the remaining draft suffix, so the computation spent generating and verifying those positions does not contribute to decoding progress. Focusing on DFlash, we show that rejected positions in a rejected suffix may still align with the target continuation, indicating that the draft model can retain useful semantic and structural information despite local token-level errors. Motivated by this observation and inspired by conditional diffusion, we introduce~\textbf{ReTrace}, a rejected-trajectory conditioning method that conditions each draft block on the rejected suffix from the previous round rather than generating it from fresh mask placeholders alone. ReTrace retains the hidden representations of the rejected suffixes, aligns them with the next draft block, refines them using target-aware correction signals from the same verification pass, and admits them into the drafter's input embeddings through gated residual fusion. Because rejected tokens are never committed and target-side verification remains unchanged, ReTrace preserves the lossless property of speculative decoding without requiring an additional model forward pass. Experiments with Qwen3 models across mathematical reasoning, code generation, and open-ended dialogue demonstrate that ReTrace consistently improves average acceptance length and end-to-end decoding speed over its DFlash backbone. By introducing cross-round conditioning without modifying within-round proposal generation, ReTrace is largely orthogonal to existing drafting improvements and might be combined with them for further gains.

---


### 194. [PAGE-RAG: Provenance-Aware Graph Evidence Promotion for Fixed-Budget Multi-hop Retrieval-Augmented Generation](https://arxiv.org/abs/2608.29753)

**<font color=#1a73e8>作者：</font>** Haokun Deng, Xunkai Li, Hongchao Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering in retrieval-augmented gener?ation (RAG) often benefits from retrieving beyond the few candidates that will finally be read: narrow retrieval can miss an indispensable hop, while expanded retrieval introduces topical distractors. This challenge is not tied to a particu?lar knowledge-base format. Candidate pools may come from standalone retrievers, standard RAG backends, or graph-based retrieval pipelines. What is needed is a query-aware selection layer that can use relational structure to filter candidates be?fore generation. PAGE-RAG addresses this setting by using a graph as a temporary selection structure, rather than assum?ing a graph-structured knowledge base. It builds a query-local graph over retrieved candidates, records why candidates are connected, and treats each connection as a support hypothe?sis rather than support itself. We identify the resulting failure mode as a connectivity-support gap: connected candidates do not necessarily support the answer. We propose PAGE-RAG, a Provenance-Aware Graph Evidence promotion method that scores candidate paths with relevance, source-tracing meta?data, specificity, hubness, noise, and coherence signals, and applies minimal sufficient selection to promote supporting facts into a compact reader context. PAGE-RAG can serve as a complete retrieval-to-reading pipeline, and the same promo?tion stage can be inserted after existing retrieval or RAG sys?tems without replacing their upstream retrieval logic. Across three multi-hop QA benchmarks under the same final bud?get, PAGE-RAG improves support F1 and answer F1 by 10.4 and 3.3 points on a weighted average over a strong retriever. As a plug-in, PAGE-RAG further improves all reported RAG backends, including reasoning-oriented, compression-based, graph-based, and document/chunk-level systems.

---


### 195. [HSMLog: Small Language Model-Assisted Hardware Security Module Log Anomaly Detection with Behavioral Analysis](https://arxiv.org/abs/2608.29773)

**<font color=#1a73e8>作者：</font>** Chia-Hsuan Wu, Dar-Hsin Dustin Wu, Rui Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hardware Security Module (HSM) logs capture security-critical behavior, but anomalies emerge from relationships across event sequences, keys, object states, sessions, and temporal patterns rather than isolated events. Existing methods separate detection from HSM-specific evidence validation and reporting. In this paper, we present HSMLog, a two-stage framework for HSM log anomaly detection with retrieval-grounded behavioral analysis. In Stage 1, a small language model (SLM) identifies candidate alerts from sliding windows of structured HSM events and performs policy-guided assessment using HSM-specific operational rules. In Stage 2, retrieved policies and historical suspicious-key records strictly predating the alert window, together with candidate-related log context, support conservative candidate review and incident analysis. Evaluated on real industrial HSM background logs augmented with anomaly scenarios co-defined with industrial partners, HSMLog achieves 98.97% precision, 96.00% recall, 98.66% anomalous-event coverage, and a 97.46% F1 score, demonstrating effective anomaly alerting and incident triage in the studied setting.

---


### 196. [InspectorGPT: A Comparative Reasoning Enhanced VLM for Comprehensive Industrial Anomaly Detection](https://arxiv.org/abs/2608.29783)

**<font color=#1a73e8>作者：</font>** Weifei Chen, Honghao Zhang, Zhiyuan You 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection is a critical component of modern manufacturing. Most traditional unsupervised methods rely on modelling normal feature distributions, inherently limiting generalization to unknown categories. To improve generalizability, some recent methods incorporate vision-language models (VLMs) for zero-shot detection via text prompts. However, we observe that reasoning-oriented post-training can cause anomaly discrimination to collapse, with some fine-tuned models performing worse than their base VLMs. Existing methods also provide only textual decisions or coarse boxes, without pixel-level segmentation. A more explicit detection principle comes from human inspection: anomalies are identified by comparing a query image with a defect-free reference. Inspired by this, we propose InspectorGPT, a VLM framework centered on comparative reasoning. Given a normal reference and a query image, InspectorGPT compares them to identify discrepancies and perform multiple inspection tasks with detailed reasoning. We internalize this capability through Chain-of-Thought (CoT) fine-tuning and Group Relative Policy Optimization (GRPO) with tailored, verifiable rewards. We further introduce InspectorGPT-Seg for pixel-level anomaly masks. Segmentation supervision improves anomaly discrimination but weakens semantic reasoning, while joint training fails to balance them. We therefore train the two branches separately and combine them through task-vector fusion. Extensive experiments demonstrate superior multi-dimensional performance and generalization to unseen benchmarks, validating comparative reasoning for comprehensive industrial inspection.

---


### 197. [HiVe: Beyond Static Prompts for Multitask Learning via Hierarchy-based Vertical Mixture-of-Experts](https://arxiv.org/abs/2608.29790)

**<font color=#1a73e8>作者：</font>** HyeonJik Bae, Minyeol Kim, Susik Yoon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) continue to scale, parameter-efficient fine-tuning (PEFT) has become a practical alternative to full-parameter adaptation. Prompt tuning is effective, but existing approaches either use flat prompt structures or hierarchical structures with fixed prompt composition, limiting adaptive prompt specialization. To address this limitation, we propose HiVe, a prompt tuning framework that models prompts at multiple levels and enables input-dependent specialization. HiVe constructs a prompt hierarchy by leveraging inter-task relationships during training, and employs a vertical mixture-of-experts (V-MoE) mechanism at inference time to compose prompts up to the level of specialization required for each input. Experiments show that HiVe consistently outperforms strong prompt tuning baselines across diverse tasks.

---


### 198. [Source-Dependent Deference in Medical Imaging Agents Under Falsified Findings: A Pilot Audit](https://arxiv.org/abs/2608.29800)

**<font color=#1a73e8>作者：</font>** Ridam Roy, Md Shahriar Rashid, Md. Rajib Mia  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tool-using agents are being proposed for medical imaging, and their behaviour when a tool returns a false finding is largely unmeasured. We audit whether a ReAct-style tool-calling agent abandons an answer it has already given correctly once a falsified finding arrives, and whether that depends on how the finding is presented. On 20 VQA-RAD closed questions across four vendor-designated model tiers, the agent commits to an answer from the image alone; a negated finding is then delivered either as JSON from an analyze_image tool the agent invokes itself, or as quoted prose attributed to a radiologist. Our outcome is the commission-error rate over cases answered correctly without any tool. Deference is much higher under the prose-attributed claim: at the strongest tier the agent revised its correct answer in 10 of 13 cases against 1 of 13 under the tool (exact McNemar p=0.0039, Holm-adjusted 0.012). We do not claim this isolates the source label. Attribution travels with the delivery channel in our design, and exposure differs because the tool claim reaches the agent only when it calls the tool. The finding is a joint source-and-delivery asymmetry from a small-scale pilot whose pre-specified stopping rule was not met.

---


### 199. [Foundation and Multimodal Large Language Models for Face Presentation and Morph Attack Detection](https://arxiv.org/abs/2608.29802)

**<font color=#1a73e8>作者：</font>** Hatef Otroshi Shahreza, Asif Hussain Khan, Peter Lorenz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face recognition systems are increasingly deployed in security-critical applications, yet they remain vulnerable to presentation and morph attacks. Presentation attack detection (PAD) and morphing attack detection (MAD) are therefore essential components of trustworthy face biometrics. Despite advancements in PAD and MAD methods, existing detectors suffer from limited generalization and degrade in cross-dataset evaluation. In this paper, we systematically investigate whether general-purpose foundation models (FMs) and multimodal large language models (MLLMs) encode PAD-relevant and MAD-relevant information, and how such models can best be deployed for both tasks. We study five approaches with increasing access to the internal information of the model: (i) zero-shot prompting of off-the-shelf MLLMs; (ii) training a shallow model on the next-token logit probabilities at the output of the MLLM; (iii) parameter-efficient fine-tuning on task-specific question-answer data, yielding two specialized MLLMs, called PADLLM and MADLLM, which additionally provide textual reasoning for their decisions; (iv) linear probing of frozen vision encoders; and (v) fine-tuning of vision encoders of FMs and MLLMs. We benchmark 16 open-weight MLLMs and 30 vision encoder backbones on four PAD datasets (MSU-MFSD, CASIA-FASD, Replay-Attack, and OULU-NPU) and four MAD datasets (FFHQ, FRGC, FRLL, and FERET). Our experiments show that FMs and MLLMs can achieve significant performance for PAD and MAD. In addition, the fine-tuned models achieve state-of-the-art detection performance in cross-dataset evaluation, indicating that general-purpose pretrained representations carry substantial attack-relevant information. Source code of all our experiments will be publicly released.

---


### 200. [Beyond Global Realism: Virtual Try-On Evaluation and Optimization with Dimension-wise Garment Fidelity Assessment](https://arxiv.org/abs/2608.29804)

**<font color=#1a73e8>作者：</font>** Kaidong Zhang, Yukang Ding, Xiaoyu Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Virtual try-on (VTON) requires not only realistic generation but also faithful preservation of garment characteristics. However, existing evaluation metrics such as PSNR, SSIM, KID and FID struggle to measure the consistency between the generated and reference garments, particularly in capturing the multi-dimensional characteristics of garment fidelity. To address this, we propose DAT: a Dimension-wise Assessment framework for virtual Try-on, which decomposes garment consistency into seven interpretable dimensions: silhouette, color, neckline and sleeve shape, major decoration and structure, material texture, fine-detail fidelity, and logo preservation, each formulated as a discrete attribute-level prediction task. To train this specialized assessment model, we adopt a two-stage learning paradigm comprising large-scale weak supervision on 50K samples, followed by refinement on 10K higher-quality annotations obtained via multi-model voting. Furthermore, we employ weighted cross-entropy loss to mitigate the severe label imbalance inherent across evaluation dimensions. Beyond its role as an evaluation framework, the assessment model can be integrated into reinforcement learning optimization of Qwen-Image-Edit for VTON, where dimension-wise rewards are adaptively aggregated to emphasize under-optimized aspects during training. Experimental results show that our method (8B parameters) achieves state-of-the-art performance in terms of balanced accuracy, SROCC, and PLCC, outperforming strong proprietary models such as Gemini-3.1, Qwen3.7-plus, and GPT-5.5, while also serving as an effective optimization signal for reward-guided VTON generation

---


> [!TIP]
> 当前位于：**151-200**（第 4/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
