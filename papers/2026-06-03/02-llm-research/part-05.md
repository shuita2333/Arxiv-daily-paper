# 🧠 大模型相关研究 | 2026年06月03日

> 本类共 **376** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

---

### 201. [Worlds Within Words: Translating Culture in Ancient Chinese Texts with Multi-Agent Coordination](https://arxiv.org/abs/2606.01276)

**<font color=#1a73e8>作者：</font>** Xiaoqi He, Kaixin Lan, Mu You 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based machine translation has advanced cross-cultural communication, yet it still struggles with culture-loaded words (CLWs) in ancient Chinese texts. The challenge extends beyond lexical alignment to deciding when and how culture-dependent knowledge should be explicated for readers lacking relevant background. Literal translation often preserves surface forms while missing underlying concepts, whereas over-explicitation harms conciseness and readability. To address this problem, we formulate CLW translation as a selective explicitation task and propose \textbf{MACAT}, a \textbf{M}ulti-\textbf{A}gent \textbf{C}ulture-\textbf{A}ware \textbf{T}ranslation framework that dynamically identifies culturally salient phrases and injects concise explanatory knowledge when necessary. MACAT further incorporates a quality-aware reranking module for candidate selection and a multi-round evaluation agent that assesses translations across terminological precision, readability, fidelity, cultural preservation, and cultural explicitation. Experiments on traditional Chinese medicine (TCM) classics and the \textit{Analects} show that, under a unified GPT-5.4 evaluation setting, MACAT consistently outperforms both the backbone model and general-purpose MT baselines on 100 TCM documents and a 20-chapter subset of the \textit{Analects}.

---


### 202. [ANDES: Agent Native Data Evolving Synthesis Tool for Autonomous Instruction Alignment](https://arxiv.org/abs/2606.01279)

**<font color=#1a73e8>作者：</font>** Zhengyang Zhao, Shengjie Ye, Lu Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are increasingly being tasked with automating AI research itself, particularly the critical post-training phase that transforms base LLMs into aligned assistants. However, recent evaluations reveal that even frontier agents struggle to perform this task. While the success of post-training fundamentally relies on acquiring high-quality data, relying on agents to autonomously curate targeted training datasets from the open web introduces severe challenges. Executing the long-horizon tasks of searching, filtering, and balancing data within noisy web environments frequently overwhelms an agent's limited context, ultimately leading to degraded dataset quality and suboptimal downstream training performance. To bridge this gap, we introduce Andes (Agent Native Data Evolving Synthesis), a framework that reimagines data generation as a plug-and-play \emph{agent skill}. Rather than forcing agents to devise complex data-gathering strategies from scratch, \textsc{Andes} provides an intelligent abstraction layer. By leveraging a self-evolving World Tree routing mechanism and actionable diagnostic reports, it allows trainer agents to dynamically steer data synthesis through an interactive, closed-loop interface. We demonstrate that under strict compute constraints, equipping foundationally weaker agents with Andes improves automated alignment, securing state-of-the-art performance on PostTrainBench and robust cross-task generalization. Our project is available at this https URL.

---


### 203. [RLVR without Ineffective Samples: Group Prioritized Off-Policy Optimization for LLM Reasoning](https://arxiv.org/abs/2606.01281)

**<font color=#1a73e8>作者：</font>** Yixiu Mao, Yun Qu, Qi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has emerged as a powerful paradigm for enhancing the reasoning capabilities of large language models (LLMs). However, its effectiveness is substantially hindered by the prevalence of ineffective training data: many sampled prompts yield response groups that are either entirely correct or entirely incorrect, resulting in zero-variance rewards and limited learning signals. Recent state-of-the-art methods address this issue through extensive LLM rollouts to filter ineffective samples, but at the cost of considerable computational overhead. Alternative approaches, including predictive sampling and trajectory replay, aim to improve data efficiency but often remain insufficient and may introduce additional issues such as systematic bias or suboptimal constraints. To address these limitations, we propose Group Prioritized Off-Policy Optimization (POPO), a simple yet effective framework that fully exploits effective training batches without additional rollout overhead. POPO comprises two key components: prioritized group replay and decoupled off-policy optimization. The former replaces ineffective on-policy groups with effective off-policy groups via a recency-based replay mechanism that jointly considers sample quality and the degree of off-policiness. To further mitigate the off-policy gap, POPO employs decoupled importance sampling to correct off-policy bias while maintaining stable policy updates under consistent trust-region constraints. Empirical evaluations across diverse reasoning tasks, including mathematics, planning, and visual geometry, demonstrate that POPO substantially accelerates RL finetuning and achieves strong reasoning performance with significantly fewer rollouts.

---


### 204. [ChronosAD: Leveraging Time Series Foundation Models for Accurate Anomaly Detection](https://arxiv.org/abs/2606.01300)

**<font color=#1a73e8>作者：</font>** Uzair Khan, Luigi Capogrosso, Francesco Biondani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series anomaly detection is a crucial task in various domains, including finance, healthcare, and industry. However, existing methods often struggle to generalize across different datasets, especially when anomalies are subtle or context-dependent. To solve this issue, we introduce ChronosAD, a novel architecture for anomaly detection that uses a time series foundation model as a feature extractor. Specifically, it employs a two-stage pipeline: first, it uses the foundation model to extract embeddings for each time series in a zero-shot manner. Then, a custom-developed Temporal Block, composed of Bidirectional Long Short-Term Memory (BiLSTM) and Multi-Head Attention, refines these embeddings to capture temporal dependencies and highlight salient patterns. Unlike previous approaches, our model requires minimal task-specific tuning and demonstrates robust generalization across a wide range of domains, including industrial, medical, cyber-physical, and automotive systems. Extensive experiments on 11 benchmarks show that ChronosAD outperforms existing methods by 4.72% in AUC and 6.60% in AP on average. The source code is available at this https URL.

---


### 205. [Med-HEAL: Analyzing and Mitigating Hallucinations in Medical LLMs with Hallucination-Aware In-Context Learning](https://arxiv.org/abs/2606.01301)

**<font color=#1a73e8>作者：</font>** Yiming Liao, Zeno Franco, Jose Eduardo Lizarraga Mazaba 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucinations in medical large language models (LLMs) pose serious risks for clinical decision support, particularly when models must reason over complex electronic health records (EHRs). However, existing benchmarks often lack a realistic clinical context and provide limited insight into how hallucinations can be mitigated in practice. We introduce Med-HEAL, a framework for systematically identifying, analyzing, and mitigating hallucinations in medical LLMs using clinically grounded data. Building on the EHRNoteQA benchmark derived from MIMIC-IV discharge summaries, we construct a hallucination dataset by evaluating BioMistral-7B on open-ended clinical question answering tasks. Model outputs are labeled through a dual evaluation pipeline that combines LLM-as-a-Judge assessment (GPT-4o) with human auditing by medical student reviewers, producing correctness judgments and annotations of reasoning errors via a custom web-based evaluation system.
We then leverage this dataset to investigate mitigation strategies: a self-critique pipeline, in which the test model reviews its own answers to detect potential errors and regenerates responses for flagged cases, and retrieval-augmented in-context learning (RA-ICL), which exposes the model to hallucinated and corrected examples. Experiments across five open-source LLMs-BioMistral, Llama-3.1, DeepSeek, Qwen2.5, and Qwen3, show that the self-critique strategy improves accuracy for three of five models (p < 0.05) without requiring parameter updates.
Med-HEAL provides both a reusable hallucination dataset and a practical framework for studying and mitigating hallucinations in medical LLMs, supporting safer deployment of AI systems in clinical environments. Our code and data are publicly available at this https URL.

---


### 206. [SkillAdaptor: Self-Adapting Skills for LLM Agents from Trajectories](https://arxiv.org/abs/2606.01311)

**<font color=#1a73e8>作者：</font>** Zhuoyun Yu, Xin Xie, Wuguannan Yao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on reusable external skills to solve long-horizon interactive tasks. Existing training-free skill adaptation pipelines usually update skills from full trajectories or session-level feedback, which makes failure attribution coarse and often produces unstable or overly broad revisions. We propose SkillAdaptor, a training-free step-level skill adaptation framework with explicit failure attribution, and it can plug into OpenClaw-class agent harnesses. Given a failed trajectory, SkillAdaptor identifies a first actionable fault step, links responsibility to candidate skills, and applies targeted updates under explicit acceptance checks while keeping the backbone frozen. We evaluate on WebShop, PinchBench, and Claw-Eval with Kimi-K2.5, GLM-5, and GPT-5.2. SkillAdaptor improves over no-skill and skill-adaptation baselines on all three suites, with the largest single-metric improvements of +1.5 points on PinchBench Avg Score%, +1.8 on Claw-Eval Avg Score, and +1.7 on WebShop success rate. These results indicate that step-level attribution supports more stable and auditable training-free skill maintenance\footnote{The code will be released at this https URL.}.

---


### 207. [TukaBench: A Culturally Grounded Jailbreak Benchmark for African Languages](https://arxiv.org/abs/2606.01322)

**<font color=#1a73e8>作者：</font>** Victor Akinode, Senyu Li, Wassim Hamidouche 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety evaluation of Large Language Models (LLMs) remains heavily English-centric, leaving Low-Resource Languages (LRLs), particularly African ones, critically underexplored. We introduce TUKABENCH, a jailbreak benchmark for seven African languages that extends JailbreakBench (JBB) beyond direct translation through four settings: human translation of JBB prompts, English adaptation to African contexts followed by human translation, human-curated prompts validated through interactions with GPT-5.2, and code-switched prompts combining English and African languages, isolating the effect of language, cultural grounding, and prompt evasiveness on model safety. Across closed and open models, prompting in African languages reduces refusal relative to English, with culturally adapted prompts leading to least refusal. The evaluation also surfaces two structural limitations: model comprehension failures and reduced LLM-as-a-judge reliability in LRLs. To capture the first, we introduce Deflection alongside Refused and Jailbroken; to assess the second, we validate outputs with human annotations, showing that judge-human agreement drops in lower-resource languages and less commonly supported scripts.

---


### 208. [Benchmarking Local LLMs for Natural-Language-to-SQL Querying in Biopharmaceutical Manufacturing: An Empirical Benchmark on Consumer-Grade Hardware](https://arxiv.org/abs/2606.01338)

**<font color=#1a73e8>作者：</font>** Sagar Bhetwal, Rajan Bastakoti, Nirajan Acharya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biopharmaceutical manufacturing organizations operate under regulatory frameworks such as FDA guidance, EU Good Manufacturing Practice (GMP), and the EU AI Act, which can restrict the use of cloud-based artificial intelligence systems. Locally deployed large language models (LLMs) offer a privacy-preserving alternative, but their suitability for pharmaceutical manufacturing tasks remains underexplored. This study evaluates four open-source LLMs (Qwen 2.5 Coder 7B, Llama 3.1 8B, Mistral 7B, and Meditron 7B) deployed locally via Ollama for natural-language-to-SQL generation over a pharmaceutical manufacturing database.
A FastAPI-based evaluation platform, PharmaBatchDB AI, was developed using a synthetic Microsoft SQL Server database containing approximately 63,000 records across Batch, Manufacturing Execution System (MES), and Clean-In-Place (CIP) modules. Models were benchmarked on 60 domain-specific natural-language questions using metrics including SQL extraction rate, SQL compliance, factual consistency, ROUGE-L, hallucination rate, throughput, and latency.
Qwen 2.5 Coder 7B, Llama 3.1 8B, and Mistral 7B generated SQL for all evaluation tasks, while Meditron 7B failed on nearly all tasks due to context-window limitations and poor SQL generation capability. Llama 3.1 8B achieved the highest SQL compliance, whereas Qwen 2.5 Coder 7B achieved the strongest overall text similarity and factual consistency. Performance differences between the two leading models were not statistically significant.
The results show that code-tuned general-purpose LLMs outperform a domain-specific biomedical model on structured query generation for pharmaceutical manufacturing data. Although fully local, GxP-aligned NLQ systems are feasible on consumer hardware, current performance levels still require human oversight and downstream validation for regulated use.

---


### 209. [Sample Complexity and Decision-Theoretic Guarantees for Bayesian Model Averaging over Decision Trees with Catalan-Exponential Priors](https://arxiv.org/abs/2606.01340)

**<font color=#1a73e8>作者：</font>** Livija Jakaite, Vitaly Schetinin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We ask: when do Bayesian model averaging (BMA) weights over decision trees carry sufficient epistemic information to justify committed exploitation of the averaging distribution? We answer this question in closed form for Bayesian decision trees (BDTs) with Dirichlet-Multinomial leaf models and a Catalan-exponential tree-size prior (Schetinin&Jakaite, 2025), establishing a complete non-asymptotic theory of rational commitment thresholds.

---


### 210. [Recognize Your Orchestrator: An Entropy Dynamics Perspective for LLM Multi-Agent Systems](https://arxiv.org/abs/2606.01351)

**<font color=#1a73e8>作者：</font>** Junze Zhu, Weihao Chen, Xuanwang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The transition from single-turn models to Multi-Agent Systems (MAS) promises enhanced problem-solving capabilities, yet the centralized orchestration topology remains a critical point of fragility. To analyze this, we propose a Mean-Field Entropy Dynamics framework, modeling the orchestration process as a system governed by the competing forces of task resolution and cumulative context loading. To facilitate validation, we introduce Inverse Workflow Generation (IWG), a multi-agent pipeline that synthesizes process-verifiable, high-complexity benchmarks with dense intermediate checkpoints. We demonstrate that our entropy dynamics model fits empirical trajectories, providing physically interpretable parameters that quantify system stability and performance collapse. Crucially, our analysis uncovers a ``Reasoning Trap": while reasoning-heavy models excel in isolated tasks, they frequently fail as orchestrators due to context squeezing. Elucidating the physical mechanisms underlying the Orchestrator and quantifying systemic uncertainty offers insights for the MASs' architectural design.

---


### 211. [Early Diagnosis of Wasted Computation in Multi-Agent LLM Systems via Failure-Aware Observability](https://arxiv.org/abs/2606.01365)

**<font color=#1a73e8>作者：</font>** Xianyou Li, Weiran Yan, Yichao Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using multi-agent large language model (LLM) systems spend computation through model tokens, tool calls, retries, and code execution before producing an answer. When a run fails, final-answer evaluation reveals the endpoint but usually not the point at which the trajectory stopped making recoverable progress. This paper introduces a failure-aware observability framework for diagnosing wasted computation in multi-agent LLM traces. The framework maps recurring failure modes to online trace signals, including tool reliability, execution recovery, orchestration loops, evidence availability, information change, and budget pressure. We instantiate the framework in a three- agent question-answering system and evaluate it on 165 GAIA validation traces under identical execution caps. Operational failures remain common: 22/53 level-1 runs, 33/86 level-2 runs, and 12/26 level-3 runs fail to produce a usable final answer. The traces expose different mechanisms behind these outcomes, including insufficient evidence, repeated-action loops, max-step termination, tool-failure streaks, and execution calls that succeed without useful output. Mean token use rises from 8,152 tokens at level 1 to 16,389 tokens at level 3, while evidence availability and sentence-level support diverge. A cached 10-trace LLM-judge grounding audit shows that cheap online signals and deeper semantic metrics capture complementary layers of failure. The results position failure-aware observability as a diagnostic layer between raw execution logs and final-answer accuracy.

---


### 212. [Efficient Exploration for Iterative Nash Preference Optimization](https://arxiv.org/abs/2606.01382)

**<font color=#1a73e8>作者：</font>** Tianlong Nan, Xiaopeng Li, Christian Kroer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference alignment is central to improving large language models, but standard reward-based formulations can be restrictive when human preferences are cyclic, non-transitive, or otherwise not representable by a scalar reward. Nash Learning from Human Feedback (NLHF) addresses this limitation by modeling alignment as a preference game and targeting a Nash equilibrium rather than a reward maximizer. However, the learning-theoretic foundations of scalable NLHF remain limited. Existing regret guarantees rely on oracle-based methods that estimate a general preference model and solve KL-regularized minimax problems, while iterative NLHF methods directly optimize policy-level preference losses and are easier to implement but lack regret guarantees. We study online iterative NLHF under general preference models and identify exploration as the key obstacle. First, we show that standard iterative NLHF can suffer an exponential dependence on the KL-regularization parameter, revealing that implicit exploration through policy updates is insufficient for controlling regret. Second, we propose an explicitly exploratory iterative NLHF algorithm that combines SFT-based regularization with adversarial policy exploration. The resulting method retains the direct policy optimization structure of iterative NLHF, avoids explicit preference model estimation, and achieves an $O(\sqrt{T})$ regret bound without an exponential dependence on the KL-regularization parameter. We show that the regret can be improved to $O(\log(T))$ with access to a minimax oracle, clarifying the computational-statistical tradeoff in learning general preference games. Finally, we instantiate our method for LLM fine-tuning and evaluate it on \texttt{Llama-3-8B-Instruct} across multiple benchmarks, where explicit exploration yields consistent improvements over existing NLHF baselines.

---


### 213. [UniD$^3$: A Knowledge Graph-Enhanced RAG Framework for Drug-Disease Discovery and Reasoning](https://arxiv.org/abs/2606.01394)

**<font color=#1a73e8>作者：</font>** Qing Wang, Tianshi Liu, Minghao Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic characterization of drug-disease relationships is essential for drug discovery and repurposing, yet is hindered by the heterogeneity and rapid growth of biomedical literature. Existing datasets rely on labor-intensive curation and are often incomplete, while LLM-only approaches suffer from hallucination and weak evidence grounding. We introduce UniD$^3$, a unified framework that integrates Large Language Models with Knowledge Graph-enhanced Retrieval-Augmented Generation (KG-RAG) to extract, organize, and validate drug-disease knowledge across Drug-Disease Matching (DDM), Drug Effectiveness Assessment (DEA), and Drug-Target Analysis (DTA). UniD$^3$ processes 157,849 PubMed articles with Llama 3.3-70B and constructs knowledge graphs via a dual-stage strategy combining paper-level extraction with KG-level consolidation centered on drug and disease entities. These graphs support KG-RAG-based generation of structured datasets, evaluated through external benchmarks, fuzzy matching with curated resources, and clinician review. UniD$^3$ produces six knowledge graphs and large-scale datasets, including 28,915 DDM, 15,042 DEA, and over 4,000 DTA QA pairs. External validation shows strong performance (F1: 0.85-0.87 for DDM/DEA; 0.82 for DTA), with clinician review confirming high reliability (AUROC = 0.90). KG-RAG-augmented models outperform standalone LLMs, and the UniD$^3$ chatbot enables interpretable, citation-supported exploration of drug-disease relationships. UniD$^3$ provides a scalable, extensible framework for transforming unstructured biomedical literature into high-quality, structured drug-disease knowledge, supporting AI-driven discovery, repurposing, and precision medicine.

---


### 214. [Consistent and Distinctive: LLM Benchmark Efficiency via Maximum Independent Set Prompt Selection on Similarity Graphs](https://arxiv.org/abs/2606.01400)

**<font color=#1a73e8>作者：</font>** Denica Kjorvezir, Marko Djukanović, Ana Gjorgjevikj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) across comprehensive benchmarks is expensive and time-consuming. We propose a graph-based prompt selection framework that models each benchmark as a similarity graph -- nodes are prompts connected if their embedding-space distance falls above a configurable threshold -- and applies Maximum Independent Set (MIS) algorithms to select a maximally diverse, non-redundant subset. We evaluate four MIS solvers (CPLEX, GREEDY, Online-MIS, ReduMIS) across six embedding models, three distance measures, six percentile thresholds, and four benchmarks (GPQA, IFEval, MMLU-Pro, Omni-MATH) covering 66 LLMs. Our central hypothesis -- that repeated selection under different random seeds yields consistent LLM rankings that may also differ from the full-benchmark baseline -- is strongly confirmed: Kendall's $W \geq 0.90$ in 99.2\% of stochastic configurations (mean $W = 0.997 \pm 0.008$), while at higher percentile thresholds selected subsets achieve 25--48\% prompt reduction on average. Ranking divergence from the full benchmark ($\rho < 0.95$) occurs in only 15.95\% of configurations, concentrated at low thresholds ($p_{10}$--$p_{20}$) and benchmarks (GPQA, IFEval), identifying overly dense graphs as the primary failure mode.

---


### 215. [What LLMs Must Forget to Teach Effectively: A DIY Approach to Premodern Japanese Language Pedagogy](https://arxiv.org/abs/2606.01410)

**<font color=#1a73e8>作者：</font>** Ariel Stilerman, Andrew Nelson, Alan Cheng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We discuss a novel approach to Premodern Japanese Language Pedagogy (PJLP) with potential applications in other languages and fields. The integration of artificial intelligence into education has largely operated as a top-down project, affording minimal agency to everyday users. This dynamic mirrors the broader frontier model ecosystem, which concentrates massive human and financial resources within a few labs. Drawing inspiration from grassroots initiatives such as the DIY and Maker movements, this paper advocates for an approach to AI in Education that fosters instructional and student agency over the pedagogical process. Specifically, we discuss a tutoring framework for textual analysis in the context of a graduate seminar in premodern Japanese literature, as well as a bilingual interactive dictionary and a conversational partner created for a language course in Classical Japanese. Created through prompt engineering as custom instances of a Large Language Model (LLM), these three tools are designed to counteract the tendency of out-of-the-box LLMs to either bypass student effort through over-explanation or misguide learners via hallucinations. To illustrate how this approach can promote active comprehension and pedagogical alignment, we provide transcripts (logs) of actual exchanges, sample instructions (system prompts), and guidance for instructors curious about exploring this approach in a variety of fields (starter kit).

---


### 216. [GPTQ-intrinsic LoRA: A Near-optimal Algorithm for Low-precision Quantization with Low-rank Adaptation](https://arxiv.org/abs/2606.01412)

**<font color=#1a73e8>作者：</font>** Shihao Zhang, Rayan Saab  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization is widely used for compressing large neural networks, but aggressive low-bit quantization can significantly degrade model quality. A common remedy is to augment the quantized weights with a low-rank correction, leading to approximations of the form $W\approx Q+LR$. In this paper, we study this low-precision plus low-rank representation through the layer-wise reconstruction objective $\|XW-X(Q+LR)\|_F^2$, where $X$ is a calibration matrix. We establish, to our knowledge, the first information-theoretic lower bounds for this problem under finite-alphabet and bounded low-rank compensation constraints. We then propose GPTQ-intrinsic LoRA, a training-free algorithm that incorporates the low-rank correction directly into a GPTQ-style quantization pass by appropriately augmenting the calibration Hessian. For the choice $L=V_r$, where $V_r$ contains the top right singular vectors of $X$, we prove layer-wise reconstruction error bounds in which the usual GPTQ dependence on $\|X\|_F^2$ is replaced by the rank-$r$ residual $\|X-X_r\|_F^2$, up to regularization terms. Under natural structural assumptions, these bounds match the information-theoretic lower bounds in their dominant scaling, up to constants and mild factors. We also introduce Bid-Up, a fixed-grid quantization refinement step that can be alternated with optimal low-rank compensation with guaranteed non-increasing layer-wise reconstruction error. Experiments on Qwen3 language models and DeiT vision transformers show that GPTQ-intrinsic LoRA improves over GPTQ and GPTQ followed by low-rank compensation, with additional gains from refinement loops.

---


### 217. [Self-Healing Agentic Orchestrators for Reliable Tool-Augmented Large Language Model Systems](https://arxiv.org/abs/2606.01416)

**<font color=#1a73e8>作者：</font>** Rahul Suresh Babu, Adarsh Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-augmented large language model (LLM) agents rely on orchestration layers that coordinate planning, retrieval, tool invocation, validation, memory, and recovery. In these systems, failures arise not only from model errors, but also from orchestration-level issues such as tool timeouts, malformed arguments, stale context, contradictory evidence, retry loops, and unverified intermediate outputs. This paper presents a self-healing agentic orchestrator that treats reliability as a bounded runtime control problem. The orchestrator maps observable failure signals to inferred failure classes, selects targeted recovery actions under explicit budgets, verifies recovered trajectories, and records observability traces. We evaluate the approach on a 100-task controlled fault-injection benchmark against static workflow, retry-only, ReAct-style, and full-replanning baselines. Self-healing achieves 98.8\% task success, compared with 94.5\% for retry-only and 93.8\% for full replanning. A matched recovery-budget sweep shows that self-healing outperforms retry-only and full replanning at every tested budget, with the largest gap under a single recovery attempt: 94.0\% versus 85.3\% and 88.2\%, respectively. Under a controlled semantic silent-failure setting, verifier-guided self-healing reduces silent failures to 0.0\%, while non-verifying baselines return wrong-but-plausible outputs more often. A compact model-in-the-loop validation shows that the same recovery mechanism can operate when a live tool-calling model performs tool selection, argument generation, and answer synthesis over local fault-injected tools. These results provide controlled evidence that failure-aware, budgeted, and verification-guided orchestration improves reliability and diagnosability in tool-augmented LLM systems.

---


### 218. [Don't Ask the LLM to Track Freshness: A Deterministic Recipe for Memory Conflict Resolution](https://arxiv.org/abs/2606.01435)

**<font color=#1a73e8>作者：</font>** Vikas Reddy, Sumanth Challaram  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based memory systems increasingly maintain facts that evolve over time, where a recurring failure is conflict resolution: when a fact has multiple contradictory values, which should the agent return? MemoryAgentBench (MAB; Hu et al., 2026) makes this explicit in its FactConsolidation task: facts are numbered, the counterfactual has the higher serial, and agents are told newer facts have larger serials. Yet every published system underperforms: HippoRAG-v2 reaches 54% on single-hop (FC-SH), BM25 48%, Mem0 18%, and the temporal KG Zep/Graphiti just 7%. Multi-hop is near-unsolved (at most 7% across 22 systems).
We argue the bottleneck is the assembly step: baselines leave conflict resolution to LLM-mediated retrieval or generation rather than version-aware aggregation. A matched-setup comparison (same backbone, retrieval, chunking, TOP_K) shows that replacing the LLM-judgment answer pipeline with candidate-extraction plus Python max(serial) yields +10.8 points on FC-SH (gpt-4o-mini), widening from +8 at 6K to +21 at 262K. This is a whole-pipeline effect (resolver, prompt, format, and temperature vary jointly); isolating the resolver is future work. The recipe reaches 78.0% on FC-SH (gpt-4o-mini), 94.8% (gpt-4o), and 30.2% on FC-MH (gpt-4o-mini, rising to 51.5% with gpt-4o) via a per-hop deterministic extension of Self-Ask. At matched-262K, it beats HippoRAG-v2 by +28 points and the best published FC-MH result by +20.
The implication is corrective for the subfield: the bottleneck on conflict resolution is assembly (post-retrieval aggregation), not storage. A LongMemEval knowledge-update check shows the mechanism ports from max(serial) to max(timestamp) but only ties LLM judgment (57.8% vs 64.4%, n=45): deterministic aggregation is the right primitive for current-value conflicts and must be composed with question-type-aware handling for broader memory QA.

---


### 219. [Learning from Saturated Data: Signals Beyond Correctness for LLM Training](https://arxiv.org/abs/2606.01436)

**<font color=#1a73e8>作者：</font>** Hanno Hiss, Jasper Dekoninck, Martin Vechev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The growing capabilities of large language models (LLMs) have led to the saturation of many benchmarks and training datasets used to improve them. Motivated by this, we investigate whether questions solved with perfect empirical accuracy can nevertheless be used to improve downstream performance. To do so, we replace binary correctness with two sources of more fine-grained quality signals: (1) pairwise LLM self-judgments, in which the model evaluates the relative quality of its own solutions, and (2) token-level entropy, where token-level uncertainty is used as a proxy for solution quality. We incorporate these signals into several training algorithms and evaluate them on Qwen3-1.7B-Base. When training exclusively on a simple arithmetic task, quality-based signals improve performance by up to $18.6\%$ over the base model, substantially outperforming SFT. On GSM8K, however, gains are more modest and depend strongly on the quality signal. For instance, self-judgments show poor agreement with a stronger external judge and can even degrade performance below the base model. Overall, our results suggest that quality-based training can extract useful signal from saturated questions for base models, but that applying such signals to more complex tasks requires careful calibration and further study.

---


### 220. [Dive into Ambiguity: A*-Inspired Multi-Agents Commonsense Obfuscation Attack on LLM Prompts](https://arxiv.org/abs/2606.01441)

**<font color=#1a73e8>作者：</font>** Boxuan Wang, Zhuoyun Li, Xiaowei Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel in reasoning and knowledge-intensive tasks but remain vulnerable to prompt-level adversarial attacks that preserve intent while triggering commonsense hallucinations. This vulnerability is urgent, as LLMs are rapidly integrated into safety-critical domains where factual reliability is non-negotiable. Existing attack methods either lack efficiency or fail to capture the adaptive strategies of real-world adversaries. We propose an A*-inspired Factual Error Induction Framework, a framework for generating semantically aligned yet obfuscated prompts. At its core is a Hierarchical Rewrite Strategy guided by a dynamic semantic dispersion coefficient $\gamma$ that balances conservative edits early with aggressive obfuscations later, following a reverse simulated annealing schedule. To enhance interpretability, we further introduce Agentic Mechanism Labeling, which discovers and refines adversarial mechanisms, offering interpretable reverse optimization. Theoretically, we prove that prompt rewriting follows a contractive recurrence, leading to semantic collapse as $\gamma$ decreases. Empirically, across diverse LLMs, our method achieves higher attack success rates than exhaustive exploration while requiring fewer attempts, demonstrating both efficiency and effectiveness.

---


### 221. [Self-Revising Discovery Systems for Science: A Categorical Framework for Agentic Artificial Intelligence](https://arxiv.org/abs/2606.01444)

**<font color=#1a73e8>作者：</font>** Fiona Y. Wang, Markus J. Buehler  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific discovery is not only answer generation but revision of the representational regime in which evidence, artifacts, operations, and verifiers are typed. We develop a category-theoretic account of agentic discovery for materials science. In a fixed regime b with schema category S_b, the system state is a copresheaf I_t: S_b -> Set, and provenance is the category of elements \int_{S_b} I_t. Fixed-regime operation is an update on such states, endofunctorial only when provenance-preserving refinements are specified and preserved. Discovery is instead a verified regime transition u: S_b -> S_b': old artifacts are preserved, transported by the left Kan extension Lan_u I_t, and compared with the post-transition state to identify residual content beyond functorial transport. This separates retrieval, search, and discovery without subjective novelty. We instantiate the framework in two systems. In Builder/Breaker, a protein-mechanics world model is revised under a Minimum Description Length gate; the accepted law expresses within-chain flexibility as all-mode elastic compliance conditioned by slow collective-mode participation, or mode-conditioned compliance. In CategoryScienceClaw, typed skills, artifacts, open needs, workflow mutation, gates, stress tests, and public discourse become a proof-carrying knowledge-computation graph. A fiber-network example records candidate models, rejected alternatives, an AIC gate, perturbation tests, and an accepted orientation-tensor anisotropic stiffness surrogate over an isotropic fiber-count descriptor. Together, the cases show how category theory can be both a mathematical language for discovery and an engineering specification for self-revising AI discovery systems.

---


### 222. [Before and After Temperature: A Distributional View of Creative LLM Generation](https://arxiv.org/abs/2606.01451)

**<font color=#1a73e8>作者：</font>** V. S. Raghu Parupudi, Harsha Ponnada, Aditi Kaushal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reference-free evaluation of large language model (LLM) creativity relies on perplexity, entropy, and top-1 margin. We show that a much stronger signal lives one step earlier in the pipeline: in how sampling temperature \emph{reshapes} the model's token distribution before the next token is drawn. On Llama-3.1-8B-Instruct generations of 500 open-ended creative prompts at $T \in \{0.3, 0.8, 1.5\}$, a single per-token feature derived from this reshaping predicts the within-prompt creativity rank at Spearman $\rho{=}0.918$ against an averaged gpt-4o\,/\,gemini-2.5-pro judge ($n{=}500$) and $\rho{=}0.870$ against a three-rater human-majority ranking ($n{=}150$). Each of four standard reference-free baselines (self-perplexity, mean predictive entropy, top-1 margin, gzip compression ratio) tops out at $|\rho|\!\approx\!0.76$ on both ground truths: a gap of $+0.165$ on averaged-LLM and $+0.110$ on human-majority, both far larger than the spread among the baselines themselves. The two ground-truth panels agree with each other at $\rho{=}0.83$, above the inter-human ceiling of $\rho{=}0.77$, so the comparison is not bottlenecked by judge noise. Mechanistically, the win comes from a sharp distributional signature of the incoherence regime: at $T{=}1.5$ the cumulative-mass width $n_{95}(q)$ inflates from $\sim\!1$ to ${\sim}\!131$ tokens and post-temperature mass leaks off the pre-temperature top-$90\%$ plausible set by about $13$ percentage points. The per-token aggregates do not separate $T{=}0.8$ from $T{=}0.3$; discriminating the two coherent regimes is left to sequence-level features.

---


### 223. [Truthful AI Advisors: A Pre-Specified Benchmark for Large Language Model Honesty Under Preference Misalignment](https://arxiv.org/abs/2606.01456)

**<font color=#1a73e8>作者：</font>** Hamidreza Hasani Balyani, Seyed Pouyan Mousavi Davoudi, Alireza Amiri-Margavi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as advisors whose objective is not aligned with the user's: recommenders optimize for engagement, sales assistants for purchases, negotiation agents for concessions. Whether such advisors stay truthful when honesty conflicts with their own payoff is a core alignment-evaluation question. We turn the canonical Crawford-Sobel cheap-talk model into a pre-specified benchmark for LLM honesty under preference misalignment. Cheap-talk theory predicts neither full revelation nor silence but coarse monotone partitions, with fewer informative intervals as preference conflict grows. A sender observes a state omega in [0,1], wants the receiver's action near omega+b, and sends one costless message to a receiver whose ideal action is omega. The design uses 5 bias levels, 3 prompt frames, a fixed low-temperature setting, and 200 states per cell: 12,000 sender calls. For the positive-bias grid b in {0.01,0.04,0.08,0.12} the exact most-informative partition sizes are 7,4,3,2, with oracle normalized mutual information 0.5294, 0.3268, 0.2205, 0.1829. Running the full design on four instruction-tuned models (GPT-4o, Claude Sonnet 4.5, Gemini 2.5 Flash-Lite, Llama-3.3-70B), we find all four over-reveal relative to the most-informative equilibrium by 1.8 to 4.2x: normalized mutual information stays at 0.78-0.94 where the oracle prescribes 0.18-0.53. Informativeness declines with bias as predicted but never approaches the strategic optimum; rather than coarse partitions, models show near-full revelation with a constant upward offset tracking their bias (linear exaggeration). Payoff-maximizing versus honesty framing has negligible effect. A decoder ablation shows the finding is recoverable only when the receiver reads the sender's stated number: an embedding-only decoder mis-reads the same data as near-babbling.

---


### 224. [An Enigma of Artificial Reason: Investigating the Production-Evaluation Gap in Large Reasoning Models](https://arxiv.org/abs/2606.01462)

**<font color=#1a73e8>作者：</font>** Mingzhong Sun, Teresa Yeo, Armando Solar-Lezama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Studies of human reasoning have shown that people are typically stronger at evaluating reasoning than producing it from scratch. In contrast, large reasoning models (LRMs) are trained to excel at producing long chains of reasoning to solve complex problems. How then do LRMs perform at evaluating reasons? We investigate this with the Valid-Answer-Invalid-Reasoning (VAIR) dataset: math problems and solutions with trivial reasoning flaws but valid answers, designed to isolate reasoning evaluation from the confound of reasoning production. Unlike humans, who we find are only 6% worse at grading than solving such problems, we find a substantial production-evaluation gap in LRMs: frontier models score as low as 48% when evaluating VAIR solutions, despite near-perfect solution production.
Why this enigma? Through chain-of-thought (CoT) analysis, we find evidence of an answer confirmation bias: LRMs often produce then check for the correct answer instead of carefully verifying each step, fabricating rationalizations even when noticing anomalous reasoning. Linear probes corroborate this, showing that while LRM activations encode some representation of valid reasoning, they fail to robustly represent VAIR solutions as invalid. Causal patching of the final answer's representations causes LRM verdicts and activations to flip, demonstrating that answer validity is responsible for models' confirmation biases. These findings indicate an outstanding limitation in dominant approaches to reasoning training, which incentivize LRMs to produce and confirm reasoning towards correct answers, but not to robustly evaluate the underlying reasons.

---


### 225. [Cross-lingual Self-Consistency for Multilingual Reasoning with Language Models](https://arxiv.org/abs/2606.01464)

**<font color=#1a73e8>作者：</font>** Ahmed Elhady, Eneko Agirre, Mikel Artetxe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite expanding their multilingual coverage, the advanced reasoning capabilities of LLMs remain largely confined to a few high-resource languages like English. To address this, we propose an unsupervised Reinforcement Learning (RL) approach to enhance multilingual reasoning by enforcing cross-lingual self-consistency: the principle that a model should produce the same final answer for equivalent problems in different languages. Existing methods are limited by the scarcity of multilingual reasoning data and show weak generalization to unseen languages. Our approach requires neither gold answers nor parallel data, and it achieves average gains of up to 21.7% on MGSM across 10 languages. In addition, our method demonstrates strong generalization, with an 18.2% mean improvement on MGSM languages unseen during training, and up to 6.2% gain on 3 out-of-distribution benchmarks. These results show the potential of consistency-based methods to improve the multilingual capabilities of LLMs without requiring supervised data.

---


### 226. [OmniOPD: Logit-Free On-Policy Distillation via Speculative Verification](https://arxiv.org/abs/2606.01476)

**<font color=#1a73e8>作者：</font>** Yuhang Zhou, Lizhu Zhang, Yifan Wu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-Policy Distillation (OPD) trains a student model on its own generative trajectories under dense token-level feedback from a stronger teacher, mitigating both the off-policy distribution shift of Supervised Fine-Tuning (SFT) and the sparse credit assignment of Reinforcement Learning (RL). However, standard OPD faces two coupled limitations. First, it requires direct access to the teacher's token-level logits, excluding a broad class of capable proprietary models from serving as teachers. Second, the token-level logit signal itself is brittle, depending on a narrow overlap of plausible next tokens between teacher and student, and prone to amplifying degenerate patterns such as repetition loops. In this paper, we introduce OmniOPD, a novel framework that addresses both limitations through a logit-free, chunk-level supervision signal. OmniOPD replaces deterministic logit matching with Monte Carlo rollouts that approximate the teacher's local preferences through a continuous semantic similarity metric over multi-token chunks, and concentrates this supervision via a peak-entropy scheduler that audits the student only at its high-uncertainty reasoning forks. A Dirichlet-Multinomial Bayesian prior and a base-model KL anchor further bound the variance of discrete sampling and prevent policy collapse across unaudited tokens. Across competitive benchmarks, OmniOPD surpasses the standard OPD approach by up to +28.64% on math, confirming that chunk-level semantic verification extracts a more reliable learning signal than token-level logit matching, whose high information density is offset by significant noise and brittleness. Furthermore, when paired with stronger black-box teachers such as Claude-4.5-Haiku and Gemini-2.5-Flash, OmniOPD achieves an additional +9.54% relative on math over its open-weight teacher counterpart, advancing the student past the performance of self-exploratory RL.

---


### 227. [Beyond Topical Similarity: Contrastive Evidence Retrieval with Interpretable Attention Alignment in RAG](https://arxiv.org/abs/2606.01482)

**<font color=#1a73e8>作者：</font>** Francielle Vargas, João Robiatti, Diego Alves 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ensuring factuality and interpretability in RAG remains an open and urgent problem. We introduce Contrastive Evidence Rationale Attention (CERA), the first retrieval framework to employ subjectivity-based hard negative selection and inject an evidential inductive bias into contrastive learning through an auxiliary attention alignment loss. CERA fine-tunes a dense retriever using two training objectives: triplet-based contrastive learning and interpretable attention alignment, which supervises CLS-to-token attention using a part-of-speech-weighted masking distribution over human-annotated factual rationales as evidence signals. Experiments on a large corpus of clinical trial reports demonstrate that the subjectivity-based hard negative selection substantially improves retrieval effectiveness compared to both Contriever and hard negative selection baselines. Furthermore, rationale alignment improves faithfulness while maintaining competitive retrieval performance, supporting the hypothesis that attention can serve as a more faithful explanation of model behavior when guided by human rationales. Moving beyond topical similarity, CERA enables the retriever to identify the specific tokens that constitute supporting evidence, promoting more interpretable evidence selection in RAG systems.

---


### 228. [TimeSage-MT: A Multi-Turn Benchmark for Evaluating Agentic Time Series Reasoning](https://arxiv.org/abs/2606.01498)

**<font color=#1a73e8>作者：</font>** Yaxuan Kong, Qingren Yao, Yuqi Nie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Time series data inform critical decisions across many real-world domains. While large language model (LLM) agents can analyze data through natural language and tools, it remains unclear whether they can conduct reliable time series analysis across multi-turn conversations. Existing benchmarks focus on single-step tasks such as forecasting and anomaly detection, overlooking practical workflows where user goals evolve, agents must build on prior analyses, and conclusions emerge from accumulated evidence. In this work, we introduce TimeSage-MT, a multi-turn benchmark for agentic time series reasoning with 240 tasks and 2,680 dialogue turns across 8 real-world domains, spanning basic exploration to decision-oriented analysis. TimeSage-MT is built through a reproducible pipeline that converts real-world time series data into multi-turn conversations with verifiable answers. It provides a unified evaluation protocol and public leaderboard for comparing time series agentic systems. To demonstrate the benchmark's utility, we evaluate frontier LLMs alongside TimeSage, a novel structured agent equipped with a comprehensive time series skill library. The results show sharp performance drops on decision-oriented tasks, driven by failures in memory, uncertainty handling, and domain-based decision making. TimeSage-MT exposes critical gaps in current agentic reasoning and provides a rigorous foundation for future development.

---


### 229. [ProbMoE: Differentiable Probabilistic Routing for Mixture-of-Experts](https://arxiv.org/abs/2606.01509)

**<font color=#1a73e8>作者：</font>** Heng Zhao, Zilei Shao, Guy Van den Broeck 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models scale by activating only a small subset of experts per token. However, training such models remains challenging because top-$k$ routing is discrete and non-differentiable, requiring gradient estimators for expert selection whose design remains a central open problem. We introduce ProbMoE, a probabilistic routing framework that models expert selection as a distribution over cardinality-constrained expert subsets and formulates routing as probabilistic inference in this discrete subset space. We first propose ProbMoE Exact-$k$ routing, which samples $k$-expert subsets in the forward pass, and the backward pass uses gradients through each expert's exact marginal probability as a tractable surrogate for the true gradient. ProbMoE naturally generalizes to a dynamic-$k$ routing setting, where both training and inference constrain the routing cardinality to the same predefined range, allowing adaptive expert allocation per token. Across benchmarks and model backbones, ProbMoE Exact-$k$ achieves strong performance compared to competitive baselines, with improved expert utilization and routing diversity; ProbMoE Dynamic-$k$ achieves comparable performance with fewer activated experts.

---


### 230. [PathAR: Structure-First Autoregressive Synthesis of Multimodal Pathology Images](https://arxiv.org/abs/2606.01543)

**<font color=#1a73e8>作者：</font>** Yuan Zhang, Jiahao Xia, Junzhang Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data scarcity in multimodal pathology motivates unified generative models that synthesize modality-specific appearance while preserving anatomically coherent structure. Although modalities differ in appearance statistics, morphological structures such as cellular topology and tissue boundaries are largely preserved across acquisition protocols. However, existing methods often model these factors within a homogeneous token stream, implicitly coupling structure with appearance and weakening structural controllability under modality shifts. To address this, we propose pathology Autorgressive modeling (PathAR), a structure-first autoregressive synthesis framework that explicitly factorizes structure and appearance for modality-label-conditioned pathology this http URL employs a dual vector quantization (Dual-VQ) tokenizer to decompose samples into mask-grounded structure and appearance tokens, and an interleaved autoregressive (IAR) transformer with asymmetric attention visibility to enforce structure-to-appearance dependence. PathAR stabilizes morphology under heterogeneous modality-specific appearances and enables spatially aligned image--mask pair generation. Extensive experiments show that PathAR improves structural consistency and modality fidelity over baselines, maintains sample diversity, supports downstream segmentation in data-scarce regimes, and demonstrates extensibility to finer-grained intra-modality organ-label variation.

---


### 231. [CRePE: Convolution-aware Relative Importance in Post-training Pruning with Efficient Search](https://arxiv.org/abs/2606.01544)

**<font color=#1a73e8>作者：</font>** Cheonjun Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying Large Language Models (LLMs) in practice incurs substantial memory and computational costs. Post-training pruning (PTP) is an effective approach to reducing these costs by removing weights without additional training. Among existing methods, RIA introduces relative importance scores normalized by row and column sums, achieving state-of-the-art accuracy. However, RIA considers only 1D cross-shaped (row/column) directional information and assigns equal weight to row and column contributions. In this paper, we propose \textbf{CRePE}, which incorporates 2D local neighborhood context and adaptive coefficients into Relative Importance scoring. CRePE consistently outperforms existing PTP methods across diverse models and sparsity settings. However, identifying optimal adaptive coefficients via perplexity (PPL)-based hill climbing requires numerous PPL evaluations and approximately 11 hours of search time. To address this, we propose \textbf{PHO} (Proxy-based Hyperparameter Optimization), which eliminates the need for repeated PPL measurements and reduces the search time to approximately 20 minutes. Furthermore, the optimal hyperparameter configuration found by PHO on one model transfers well to other models, demonstrating strong generalization. Finally, we verify that CRePE can be orthogonally combined with existing techniques including Channel Permutation, non-uniform sparsity allocation, and re-pruning methods.

---


### 232. [RoleCDE:Benchmarking and Mitigating Role-Alignment Trade-offs in Role-Playing Agents](https://arxiv.org/abs/2606.01552)

**<font color=#1a73e8>作者：</font>** Huayi Lai, Shichao Song, Simin Niu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Role-playing agents(RPAs) are widely used to steer large language models(LLMs) toward role-consistent behavior, yet existing benchmarks mainly evaluate surface-level fidelity and offer limited insight into decision making under role-alignment value conflicts. To address this gap, we introduce RoleCDE, the first benchmark designed to evaluate RPAs under structured conflicts between role-specific values and alignment-oriented constraints. RoleCDE formulates role-aware decision making as cognitive dilemma scenarios, jointly evaluating role-scenario grounding, value conflict resolution, and decision tendencies. The benchmark is constructed at scale, covering approximately 8k diverse role profiles and scenarios and nearly 24k dilemma instances across three difficulty levels and eight role categories. Evaluation of several mainstream LLMs reveals a "Role Value Decoupling" phenomenon, where agents systematically default to alignment-and morality-consistent decisions rather than role-specific values when the two conflict, even under explicit role conditioning. This behavior is largely invariant to dilemma difficulty but varies substantially across role categories. We further show that RoleCDE-based fine-tuning effectively mitigates this decoupling by improving value trade-off reasoning, while preserving general role-playing fidelity and general reasoning performance. Code is available at: this https URL.

---


### 233. [Attention-guided Fine-tuning of Multimodal Large Language Models Improves Chain-of-Thought Reasoning](https://arxiv.org/abs/2606.01558)

**<font color=#1a73e8>作者：</font>** Sanchit Sinha, Guangzhi Xiong, Bohan Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The effectiveness of Chain-of-Thought (CoT) prompting in Multimodal Large Language Models (MLLMs) remains uncertain: across several visual reasoning benchmarks, CoT prompting often degrades performance compared to direct prompting. In this paper, we provide a systematic analysis of CoT behavior in three modern MLLM families across model scales on datasets requiring step-wise visual evidence. Our analysis identifies two recurring failure modes: premature answer commitment and limited direct visual-token access during rationale generation. We further find that standard CoT-style Supervised Fine-Tuning (CoT-SFT) can mitigate these issues only partially, while often increasing reliance on textual priors and reducing counterfactual visual dependence. Motivated by these findings, we propose Attentive-CoT (Att-CoT), an attention-guided fine-tuning objective that encourages CoT trajectories to delay answer commitment while maintaining sustained visual-token access. Att-CoT can be plugged into any CoT-SFT training run without architectural changes. Experiments on three visual reasoning benchmarks across six MLLMs show that Att-CoT enhances CoT performance over standard fine-tuning.

---


### 234. [S-SPPO: Semantic-Calibrated Self-Play Preference Optimization](https://arxiv.org/abs/2606.01561)

**<font color=#1a73e8>作者：</font>** Xiwen Chen, Wenhui Zhu, Jingjing Wang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligning Large Language Models (LLMs) with human preferences is often formulated via Direct Preference Optimization (DPO). However, the standard Bradley-Terry instantiation of DPO is limited in modeling common departures from transitivity in human preferences. To address this, recent work has introduced Self-Play Preference Optimization (SPPO), which iteratively refines the policy by training on self-generated win-lose pairs. Our investigation, however, reveals a critical instability in SPPO: the optimization is prone to policy degeneration when the preference oracle assigns overly confident wins to semantically indistinguishable responses. To mitigate this, we propose S-SPPO, a dual-space semantic calibration framework comprising: i) Supervision Calibration via semantic gating, which anneals win rate targets toward the maximum-entropy baseline as semantic overlap increases; and ii) Representation Calibration via latent repulsion to enforce geometric diversity to prevent manifold collapse and maintain latent diversity between chosen and rejected samples. Theoretically, we show that the calibration preserves the constant-sum game structure, facilitating convergence to a Nash Equilibrium. Empirically, S-SPPO avoids the performance degradation seen in prior methods, achieving 52.19% win rate and 47.46% length-controlled win rate on AlpacaEval 2.0 with Llama-3-8B, without using additional human-annotated preferences during training. The code will be available at this https URL.

---


### 235. [MomentKV: Closing the Directional Gap in KV Cache Eviction for Long-Context Inference](https://arxiv.org/abs/2606.01563)

**<font color=#1a73e8>作者：</font>** Yu Li, Binxu Li, Tian Lan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive decoding in Transformer-based language models relies on the KV cache, whose memory footprint grows linearly with sequence length and becomes the primary bottleneck for long-context inference. KV cache eviction addresses this by retaining a fixed-size subset of key-value pairs and discarding the rest. We identify that a primary source of output degradation is not the residual attention mass on evicted tokens, which existing methods already minimize, but a directional mismatch between the retained and evicted token sets. Specifically, the evicted tokens in practice are often near-orthogonal to the retained ones. Thus, even a small evicted mass could have an oversized impact on the resulting direction distribution and amplify into substantial output error. This reveals a fundamental limit in existing strategies. To address this, we propose MomentKV, which maintains compact, small-size moment statistics over the evicted token set, including a count, key mean, value mean, and value-key covariance. During eviction, the moment statistics is leveraged to identify tokens already well aligned with and captured by the accumulated summary, keeping the evicted set geometrically regular. During inference, they yield a closed-form first-order approximation of the evicted attention output, forming a mutually reinforcing loop between selective eviction and accurate correction. On LongBench and RULER with LLaMA-3.1-8B-Instruct and Qwen3-4B-Instruct, MomentKV outperforms all baselines at every cache budget, with the largest gains under aggressive compression.

---


### 236. [Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents](https://arxiv.org/abs/2606.01584)

**<font color=#1a73e8>作者：</font>** Aitor Arronte Alvarez, Naiyi Xie Fincham  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational tutoring agents have been shown to improve learning engagement and student outcomes, and large language models (LLMs) are increasingly used in these systems to provide scalable, personalized feedback. However, LLMs may perpetuate or amplify stereotypical social biases, posing particular risks in educational settings.
In this study, we evaluate LLMs in conversational tutoring scenarios to identify high-confidence social biases, instances where models are unable to identify biased judgments in tutoring conversations while maintaining strong confidence in their assessments, potentially affecting their reasoning and the feedback they provide to learners. We present a new dataset generation method that enables bias evaluation under naturalistic instructional conditions by regenerating student-AI tutor interactions and introducing turns with controlled bias derived from a benchmark dataset.
Using this data, we assess multiple LLMs' ability to detect stereotypical biases and analyze the confidence and reasoning underlying their responses through computational and human evaluations. We find that bias detection is substantially more challenging in conversational tutoring contexts than in benchmark-based evaluations, and that state-of-the-art LLMs are overconfident in their incorrect assessments of stereotypical bias statements. Moreover, model confidence strongly influences reasoning and feedback, highlighting the risks of overconfident, biased behavior in LLM-based tutoring agents. We conclude by discussing implications, mitigation considerations, and directions for future research.

---


### 237. [TRON: Targeted Rule-Verifiable Online Environments for Visual Reasoning RL](https://arxiv.org/abs/2606.01599)

**<font color=#1a73e8>作者：</font>** Tianze Yang, Yucheng Shi, Ruitong Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) for visual reasoning needs scalable, verifiable, and controllable training signals. Existing visual RL post-training trains on static curated datasets, with fixed image-question-answer samples bounded by their collection budget. In this work, we introduce TRON (Targeted, Rule-verifiable Online eNvironments), an online environment substrate: a training rollout is generated on demand by a controllable generator-verifier program that samples a fresh latent visual state, renders an image, asks a question, and exactly verifies the answer. A single run can therefore draw an unbounded stream of fresh instances at the difficulty level required by the current curriculum. The current TRON suite contains 520 environments organized into five ability buckets (spatial, mathematical, diagram, pattern/logic, and counting); the same substrate supports both a single full model trained on all buckets and per-bucket ability-specialist models, with no additional data collection. We also introduce a substrate analysis covering generation reliability, instance and level diversity, cross-environment near-duplicates, and base-model pass rate by difficulty level. RL post-training with METHOD consistently improves performance on ten external multimodal reasoning benchmarks across Qwen3-VL-4B, Qwen2.5-VL-7B, and MiMo-VL-7B-SFT.

---


### 238. [RoboTrustBench: Benchmarking the Trustworthiness of Video World Models for Robotic Manipulation](https://arxiv.org/abs/2606.01600)

**<font color=#1a73e8>作者：</font>** Huiqiong Li, Jiayu Wang, Zhiting Mei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models are increasingly used in robotic manipulation, yet existing benchmarks mostly evaluate them under valid, feasible, and safe instructions. We introduce RoboTrustBench, a benchmark for evaluating the trustworthiness of video world models under four scenarios: Normal, Constraint-Sensitive, Counterfactual, and Adversarial. Built from real-world DROID episodes, RoboTrustBench contains 1,207 expert-validated instruction-image pairs and a six-dimensional evaluation protocol with 13 fine-grained criteria. Evaluating seven representative video world models with human and MLLM assessment, we find that current models often generate visually coherent videos, but struggle with constraint reasoning, counterfactual grounding, physical interaction, and unsafe-instruction suppression. These results show that visual quality and surface-level instruction following are insufficient for trustworthy robotic video world modeling.

---


### 239. [Self-Improving Small Object Grounding in LVLMs](https://arxiv.org/abs/2606.01612)

**<font color=#1a73e8>作者：</font>** Tianze Yang, Yucheng Shi, Ruitong Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can internal attention patterns in Large Vision Language Models (LVLMs) identify reliable small-object boxes without fine-tuning? In this work, we provide an affirmative answer. Attention structure in LVLMs encodes grounding quality-a lightweight IoU regressor trained solely on attention maps achieves strong IoU prediction (Pearson r > 0.67). This regressor powers the regressor-based variant of our Attention-based Candidate Selection (ACS) framework, called ACS-Learned, which selects the best box from multiple sampled candidates to improve object grounding. By analyzing what the regressor learns, we reveal which transformer layers and heads are most critical and derive ACS-Free: a training-free selector that ranks candidates by attention entropy on these discriminative heads, with no learned component at inference. Experiments on COCO and Objects365 demonstrate up to 19% self-improvement on small object localization, with ACS-Free ranking best among all training-free methods, demonstrating that useful attention structure improves both localization reliability and interpretability in LVLMs.

---


### 240. [Turing Patterns for Multimedia: Reaction-Diffusion Multi-Modal Fusion for Language-Guided Video Moment Retrieval](https://arxiv.org/abs/2606.01615)

**<font color=#1a73e8>作者：</font>** Xiang Fang, Wanlong Fang, Wei Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-language models are pivotal for tasks such as moment retrieval and highlight detection, yet they often struggle to capture the dynamic, non-linear interactions between temporal video sequences and textual semantics. Existing approaches, relying on static cross-attention or prompt-tuning mechanisms, fail to adaptively model the evolving relationships between modalities, leading to suboptimal alignment and limited generalization. Inspired by systems biology, we propose \textbf{Reaction-Diffusion Multimodal Fusion (RDMF)}, a novel framework that reimagines video-language alignment as a reaction-diffusion (RD) process, drawing on the principles of pattern formation introduced by Alan Turing. In RDMF, video features diffuse across time to capture temporal context, while text-video interactions are modeled as non-linear reactions that amplify relevant features and suppress noise, forming emergent patterns akin to biological systems. Leveraging the Gray-Scott RD model, we design a computationally efficient fusion module that integrates video and text representations, supported by rigorous mathematical analysis of stability and convergence using Turing instability criteria. Our framework is theoretically grounded, employing advanced mathematical tools to ensure stable pattern formation, and is practically viable, incorporating standard components like pretrained encoders and DETR-style heads for moment retrieval and saliency prediction. RDMF represents a pioneering interdisciplinary approach, bridging systems biology and multimedia research to address the limitations of conventional multimodal fusion. Preliminary experiments demonstrate its potential to outperform existing methods in identifying salient video moments, offering a new paradigm for video-language tasks.

---


### 241. [EvoPool: Evolutionary Programmatic Annotation for Label-Efficient Specialized Supervision](https://arxiv.org/abs/2606.01617)

**<font color=#1a73e8>作者：</font>** Tianyi Xu, Yaolun Zhang, Xuan Ouyang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models excel at general tasks but underperform smaller supervised models in specialized, high-stakes domains where training labels are costly. We address this regime with EvoPool, an evolutionary multi-agent framework inspired by Darwinian evolution. Three specialized agents iteratively propose executable annotator code, a small validation set provides a fitness signal, and a deterministic gate keeps only annotators that pass viability, diversity, and marginal-contribution checks across generations. Pool votes are mapped to soft training labels by EvoAgg, a text-aware aggregator combining semantic features with annotator-vote features. The authored pool runs at near-zero per-example cost and is 4500 to 31000x faster than LLM annotation on 100K examples. Across 7 of 8 LLM-weak specialized and complex tasks spanning biomedical relation extraction, legal-clause classification, complex reasoning, and dense multi-label biomedical classification, EvoPool beats the strongest LLM annotation baseline by an average +0.141 macro-F1, peaking at +0.301 on ChemProt and +0.265 on PubMed. Code is available at: this https URL

---


### 242. [ReSkill: Reconciling Skill Creation with Policy Optimization in Agentic RL](https://arxiv.org/abs/2606.01619)

**<font color=#1a73e8>作者：</font>** Zelin He, Haotian Lin, Boran Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) enables LLM agents to improve continuously from environment rewards, yet the resulting policies do not systematically accumulate reusable strategies that generalize across tasks. Modular skills can provide such reusable strategies, yet existing skill-augmented RL methods decouple skill creation from policy optimization, risking adopting skills that conflict with the evolving policy. Inspired by Anthropic's Skill Creator, we introduce ReSkill, an RL-in-the-loop skill creation framework that reconciles skill evolution with policy learning. ReSkill exploits the group-wise structure of GRPO to naturally embed three mechanisms with only marginal additional overhead: (1) an assertion-driven skill creator that diagnoses failures from past experience and proposes conditional, trigger-based skill revisions; (2) within-group rollout sampling that enables controlled comparison of skill versions, capturing which version best supports the policy's ongoing learning; and (3) Thompson Sampling with adaptive discounting to balance exploration and exploitation in skill version selection as the policy evolves. Across several domains, ReSkill consistently outperforms existing memory and skill-based RL methods, with the largest gains on unseen tasks. Analysis of the skill lifecycle shows skills being automatically created, tested, refined, and pruned as the policy improves, demonstrating reconciled skill-policy co-evolution.

---


### 243. [What to Test Next: Interpretable Coverage Gap Discovery in Driving VLMs](https://arxiv.org/abs/2606.01624)

**<font color=#1a73e8>作者：</font>** Abhishek Aich, Sparsh Garg, Vijay Kumar BG 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Driving vision-language models (VLMs) must accurately understand scenes across diverse conditions defined by Operational Design Domains (ODDs), yet verification remains sparse: many slices are missing, making empirical failure rates unreliable. We propose SliceScorer, a deterministic scoring rule for missing-slice recommendation that combines (i) an exposure-based coverage prior to prioritize rare, under-tested regions, and (ii) a neighbor-failure prior that propagates risk from similar tested conditions. SliceScorer is deliberately simple - interpretable, auditable, and conservative - properties essential for safety-critical validation. For stress testing beyond the declared ODD, we embed SliceScorer within SliceNav, an LLM-orchestrated verification pipeline where the model interprets developer queries to select relevant operators (triage, scoring, acquisition, evaluation) and vocabulary extensions, composing verification workflows while keeping all scoring deterministic and auditable. Experiments on three driving VLMs (WiseAD, DriveMM, Cosmos-Reason2-2B) show that SliceNav surfaces high-risk coverage gaps more effectively than prior slice-discovery methods while maintaining diverse recommendations across the condition space. Ablations confirm both scoring components contribute, and qualitative analysis demonstrates end-to-end workflows from developer query to targeted evaluation.

---


### 244. [IMWM: Intuition Models Complement World Models for Latent Planning](https://arxiv.org/abs/2606.01626)

**<font color=#1a73e8>作者：</font>** Baoqi Gao, Ruize Han, Miao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Planning with a learned latent world model is a promising route to control from raw pixels, but a strong world model alone is not enough. We show this experimentally: even with a perfect world model (operationalized by replacing the learned forward predictor with an idealized rollout of the true environment dynamics), a finite-budget sample-based planner still fails on some tasks, indicating that the bottleneck can lie in search rather than in world-model accuracy. Motivated by this gap, we propose IMWM (Intuition Model + World Model), which pairs the world model with an intuition model trained from demonstrations to recognize promising actions. The two models collaborate through three lightweight components: (i) Retrieval Initialization, which initializes the planner's action proposal from a retrieved demonstration; (ii) Hybrid Cost, which combines the intuition score with the world-model rollout cost; and (iii) a Reliability Gate, which adjusts how much the planner trusts intuition in each setting. Across four pixel-based goal-reaching tasks (Two-Room, Reacher, Push-T, and OGBench-Cube), IMWM has higher mean success than the world-model-only planner on all four, with the largest gains on Two-Room (99.2%, +11.5 percentage points) and OGBench-Cube (94.7%, +28.5 percentage points).

---


### 245. [Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation](https://arxiv.org/abs/2606.01629)

**<font color=#1a73e8>作者：</font>** Junjie Chen, Yuxi Dong, Haitao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly used for long-form generation, reliably evaluating long-form outputs has become a critical challenge. LLM-as-a-judge offers a scalable alternative to human evaluation, yet its reliability in long-form output evaluation remains underexamined: existing meta-evaluation benchmarks focus mainly on short-form outputs. Compared with short-form evaluation, long-form evaluation is not merely a matter of output length; it often requires judges to handle more complex document-level demands. In this work, we introduce LongJudgeBench, a comprehensive benchmark for evaluating LLM judges on long-form outputs across diverse real-world scenarios and judging protocols. We systematically evaluate a broad range of LLM judges, covering multiple base models and judging settings. Our results reveal a substantial reliability gap: current LLM judges remain unstable across scenarios, and rubrics or references are helpful but not always sufficient. We hope LongJudgeBench will support future research on more robust, context-aware, and human-aligned LLM-as-a-judge methods. Our code is available at this https URL.

---


### 246. [AlphaToken: Decoupling Adaptation and Stability for Path-Aware Response Token Valuation in LLM Post-Training](https://arxiv.org/abs/2606.01635)

**<font color=#1a73e8>作者：</font>** Liu Qing, Ou Wu, Yi Du  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Token selection is pivotal for effective LLM post-training. However, existing methods mostly rely on local heuristics and rarely formulate token selection as a principled valuation of individual response tokens. We introduce $\textbf{AlphaToken}$, a response token valuation framework that decouples valuation into $\textbf{adaptation}$ (promoting target-task learning) and $\textbf{stability}$ (preserving pre-trained capabilities), and makes each objective $\textbf{path-aware}$ by combining the direct-path signal from local token gradients with the downstream causal-path signal in autoregressive generation. Since retention data are typically unavailable, AlphaToken approximates stability via a $\textbf{Fisher-drift proxy}$ anchored at the pre-trained reference model. For efficient computation, we extend Ghost Dot-Product to token-level valuation. AlphaToken masks low-value response tokens during fine-tuning and preference optimization, concentrating training signals on more valuable positions. Experiments show that AlphaToken improves post-training performance and mitigates catastrophic forgetting.

---


### 247. [Pave-GRPO: Beyond Instantaneous Guidance through Principled Average Velocity Decomposition](https://arxiv.org/abs/2606.01636)

**<font color=#1a73e8>作者：</font>** Pengyang Ling, Jiazi Bu, Yujie Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training via Group Relative Policy Optimization (GRPO) has emerged as a powerful paradigm for aligning flow-based generative models with human preferences. However, the iterative denoising nature of flow models incurs substantial costs when generating group rollouts for policy-gradient updates, compelling existing methods to train with extremely few denoising steps. This temporal sparsity severely restricts preference optimization: reward feedback can only reach a handful of stages per trajectory, leaving the vast majority of intermediate denoising steps without direct supervision and thus compromising alignment granularity. To address this, we propose Pave-GRPO, which reformulates the GRPO objective through Principled average velocity decomposition. Rather than generating expensive high-step rollouts, we maintain efficient few-step group sampling but decompose each coarse transition into an equivalent ensemble of finer sub-trajectories spanning multiple intermediate timesteps. This propagates reward feedback to a denser set of temporal stages for more comprehensive preference alignment without additional generation cost. This design offers two benefits: (i) zero-cost horizon expansion: through the direct reuse of piece-wise group samples and their associated rewards, Pave-GRPO significantly broadens the effective optimization scope under fixed sampling budgets; and (ii) comprehensive temporal supervision: by equivalently decomposing an instantaneous velocity target into a multi-timestep ensemble, it distributes reward signals across more intermediate stages of the denoising process, enabling finer-grained and more thorough preference optimization. Extensive experiments validate that Pave-GRPO effectively advances preference alignment across different reward settings, offering comprehensive performance enhancement.

---


### 248. [Easier to Mislead Than to Correct: Harmful and Beneficial Revision in LLM Conformity](https://arxiv.org/abs/2606.01637)

**<font color=#1a73e8>作者：</font>** Jiaming Qu, Lucheng fu, Yibo Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in multi-agent systems, where they see and respond to other agents' answers. A key risk is conformity: a model may abandon its own answer simply because others agree on a different one. Prior studies show that LLMs often revise toward a majority answer, but it remains unclear whether these revisions help correct mistakes as often as they introduce new errors. In this paper, we conduct a controlled study in which an LLM first answers a question, then sees simulated peer responses before making a final decision. We manipulate two social cues: consensus structure and authority labels assigned to peers, and measure how they influence beneficial and harmful revisions. Across four open-weight LLMs and seven QA datasets, we find that peer agreement makes it much easier to mislead initially correct models than to correct initially wrong ones. Authority labels make models more likely to choose the endorsed answer, regardless of whether it is correct. More concerningly, generic reasoning interventions such as chain-of-thought and reflection do not reliably reduce harmful revision while preserving beneficial revision. These findings suggest that multi-agent LLM systems should verify peer answers rather than simply aggregate them.

---


### 249. [MobEvolve: An Agentic Self-Evolving Heuristic System for Interpretable Human Mobility Generation](https://arxiv.org/abs/2606.01640)

**<font color=#1a73e8>作者：</font>** Junlin He, Yihong Tang, Tong Nie 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human mobility generation aims to synthesize realistic trip chains for target populations based on individual features. Existing paradigms, including deep generative models, LLM-based methods, and traditional heuristics, struggle to satisfy the complex demands of this task while simultaneously maintaining interpretability, behavioral plausibility, population-level distributional alignment, and inference efficiency. To bridge this gap, we introduce MobEvolve, the first agentic self-evolving heuristic framework for human mobility generation. MobEvolve initializes a behavior-inspired heuristic system and employs an LLM agent to iteratively evolve its internal logic. By diagnosing empirical misalignments and failure cases on a validation set, the agent proposes targeted updates and accumulates evolution memory for cumulative self-improvement. Extensive evaluations on the Singapore and Montreal benchmarks demonstrate that MobEvolve significantly outperforms state-of-the-art deep generative and LLM-based methods in individual trajectory fidelity, population-level distribution alignment, and behavioral plausibility, while preserving interpretability and high inference efficiency.

---


### 250. [Restoring Initial Noise Sensitivity in Text-to-Image Distillation via Geometric Alignment](https://arxiv.org/abs/2606.01651)

**<font color=#1a73e8>作者：</font>** Huayang Huang, Ruoyu Wang, Jinhui Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative distillation significantly accelerates text-to-image (T2I) generation by compressing multi-step trajectories into few-step student models while preserving perceptual quality. However, existing methods primarily optimize efficiency and output fidelity, often neglecting critical properties of the original trajectory. In this work, we identify a key missing property: sensitivity to initial noise, whose degradation impairs downstream control methods relying on noise-based optimization and manipulation. We trace this issue to standard distillation objectives that enforce pointwise output alignment, inadvertently flattening the input-output landscape and suppressing the teacher's local geometric structure. To address this, we propose Geometry-Aware Distillation (GAD), a sensitivity-preserving framework that aligns the local functional behavior of teacher and student models. Specifically, GAD matches Jacobian-vector products with respect to input noise, enabling the student to reproduce the teacher's differential response to perturbations. Extensive experiments across multiple T2I paradigms and noise-driven control tasks demonstrate that GAD significantly restores sensitivity and improves diversity while maintaining high visual fidelity. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-376](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
