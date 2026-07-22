# 🧠 大模型相关研究 | 2026年07月23日

> 本类共 **104** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-104](./part-03.md)

---

### 1. [Calibrated Selective Fact-Checking via Evidence Chain Evaluation](https://arxiv.org/abs/2607.18240)

**<font color=#1a73e8>作者：</font>** Dekun Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can achieve strong fact-checking accuracy, yet forced binary decisions conceal a critical reliability problem: systems may issue confident verdicts even when supporting evidence is weak, sparse, or internally inconsistent. We address this issue through Evidence Chain Evaluation (ECE), a selective fact-checking framework that permits abstention via an uncertain verdict instead of requiring a true/false decision for every claim. The evaluated system is a tool-using verification agent that gathers evidence through web search, scholarly search, and executable checks, and then returns a structured verdict with confidence and source-level metadata. On ECE-Bench, ECE achieves 91.6% standard accuracy, 93.7% coverage, and 97.8% selective accuracy on answered claims. Although ECE does not outperform the strongest retrieval baseline on aggregate calibration metrics such as Expected Calibration Error, Brier score, or AURC, it delivers a clear selective-prediction trade-off: the system maintains very high accuracy on answered claims while deferring 6 of 95 cases. These deferred cases are concentrated in lower-reliability evidence settings (5/6 at source level L4), supporting the view that abstention functions as a safety-oriented mechanism for handling epistemically weak evidence. Code is available at this https URL cheshireyang/ECE.git

---


### 2. [BatchDAG: LLM-Planned Execution Graphs for Scalable Ad-Hoc Analysis Over Enterprise Data](https://arxiv.org/abs/2607.18241)

**<font color=#1a73e8>作者：</font>** Anupreet Walia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at analyzing individual documents but break down on exhaustive, cross-entity analytical questions over enterprise-scale datasets due to context overflow, loss of per-entity attribution, and linear latency from sequential tool calls. We present BatchDAG, a system in which an LLM generates a typed directed acyclic graph (DAG) of operations -- SQL queries, semantic searches, in-memory transforms, parallel fan-outs, and single-shot analyses -- which a deterministic engine evaluates with topological-wave parallelism and structured JSON data flow. A key optimization, entity-aware batching, groups rows by logical entity before fan-out, reducing LLM calls by up to 47x. BatchDAG is not primarily an accuracy improvement over hand-optimized pipelines; rather, it is a general-purpose orchestration layer that replaces multiple hand-engineered workflows with a single system that generates the appropriate execution strategy from natural language. In controlled experiments on 12 transcript-heavy queries, BatchDAG (3.74/5) achieves quality comparable to an expert-designed pipeline (3.25/5) and significantly outperforms a ReAct agent (3.09/5, p<0.01), with superior provenance (77% transcript evidence rate vs. 46-60% for baselines). A controlled ablation shows structured JSON intermediates reduce hallucinations by 27% versus prose summaries (paired t-test, p=0.107, n=12). The planner achieves 98.8% valid-DAG rate across 300 planning calls. In production at this http URL, BatchDAG processes queries over 50,000+ meetings in under 60 seconds, with measured per-query costs of $0.02-$0.24 at published GPT-5.1 pricing.

---


### 3. [From Agent Failure Paths to Quantified Residual Risk: A Compositional Framework for Resilient Agentic AI](https://arxiv.org/abs/2607.18243)

**<font color=#1a73e8>作者：</font>** Hassan Karim, Sai Sitharaman, Deepti Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI is crossing trust boundaries faster than current risk models can represent. Existing approaches provide one of two partial views. They either describe failure mechanisms without producing a transferable residual-risk estimate, or they produce a risk estimate while treating the internal failure path as a black box. We couple those two views by proposing CPSAINT, a seven-layer integrity decomposition over Physical state, Sensors, Data, Compute, Actuators, Environment, and Time, paired with FRIESA-K, a residual-risk functional that maps each failure path to a quantified risk instance. FRIESA-K grounds the resistance term K in a controlled absorbing Markov model so that control effectiveness is derived from state dynamics rather than assigned as an informal score. The result is a concise mechanism-to magnitude pipeline for resilient agentic and embodied AI. We report governance observability through a separate additive penalty instead of inserting governance as a new variable in the resistance functional. We formalize structural composability linking valid failure paths to well-defined risk instances and show the framework on two contrasting scenarios a hard real-time warehouse robot and a governance-instrumented financial-services agent. Across both cases, the same layer grammar, variable semantics, and dynamic-resistance construction remain intact. Thus, we obtain a compact kernel that supports cross-domain reasoning, explicit assumptions, and quantitatively grounded formalism of composable trust.

---


### 4. [Anthropomorphism in Children's Interactions with LLM Chatbots: A Systematic Review of Drivers and Outcomes](https://arxiv.org/abs/2607.18250)

**<font color=#1a73e8>作者：</font>** Hansinie Madushika Jayathilake, Renkai Ma  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Researchers across domains have investigated children's use of LLM-based chatbots through various perspectives and methodologies. However, prior research remains fragmented regarding anthropomorphism, the tendency for children to assign human characteristics to those large language Model (LLM) chatbots as non-human objects. By analyzing 35 empirical studies published between 2022 and 2025, this systematic literature review identifies the drivers of anthropomorphism in children's LLM chatbot interactions and the subsequent outcomes of these interactions. We found that human-like persona construction, adaptive scaffolding, supportive companionship, and non-human embodied design drive children's anthropomorphic interactions. Additionally, five anthropomorphic outcomes emerged, including children exhibiting paradoxical social and moral responses, dual consciousness about the chatbots, forming varying social ties, exploring social boundaries, and attributing human narratives to conversation breakdowns. The findings, including both benefits and risks, can inform the future design and development of LLM chatbots focused on children's well-being and promoting sustainable interactions that meet children's developmental needs.

---


### 5. [Beyond Accuracy and Cost: Latency-Aware LLM Query Routing for Dynamic Workloads](https://arxiv.org/abs/2607.18253)

**<font color=#1a73e8>作者：</font>** Shivam Patel, Akaash R. Parthasarathy, Ankur Mallick 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern language query routers improve inference efficiency by assigning each query to a model that balances response quality and monetary cost. However, current query routers are largely latency-agnostic and do not consider the generation latency experienced by queries at model instances. In practice, latency is often controlled by load-balancing policies such as round-robin or join-the-shortest-queue, which do not account for model accuracy or inference cost. Incorporating query latency into routing is challenging as it depends not only on the query's prompt length, but also on the current prefill and decode workload at the model instance and the scheduling and batching policy of the serving framework. We design a lightweight latency estimator that simulates autoregressive token batch processing in the serving framework and estimates the time-to-first-token (TTFT) of queries. We incorporate this latency estimator into a latency-aware router that jointly optimizes latency, accuracy, and cost when assigning queries to model instances. Our experimental results indicate that this joint optimization yields up to 40% improvement in accuracy--cost utility while maintaining the same latencies as standard load-balancing approaches.

---


### 6. [Semantic Cooperative Games for Contribution Attribution in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2607.18255)

**<font color=#1a73e8>作者：</font>** Pengyi Jiang, Xiaoguang Zhu, Quanyan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Contribution attribution has become a central problem in LLM-based multi-agent systems, where final outputs are produced through multiple agents, message exchanges, and ordered workflow dependencies. Existing attribution methods often rely on counterfactual valuation, such as removing agents or comparing score changes across altered agent subsets. In language-mediated workflows, these methods require repeated model calls, introduce high variance, and do not explicitly capture the intermediate semantic states through which agents produce, preserve, and transform task-relevant information. We propose Semantic Cooperative Games (SCG), a framework that represents a realized language flow as a semantic generation hypergraph and induces an agent-level semantic value function on this structure. We define the Semantic Shapley Value (SSV) to allocate contribution over semantic support logic, and introduce SLIC, a single-trajectory algorithm that constructs the semantic hypergraph, recovers minimal semantic supports, applies Boolean absorption, and computes SSV without rerunning agent subsets. We prove that SSV reduces to the classical Shapley value under standard set-based, fully observable, and no-order-dependence conditions. On a medical benchmark satisfying these conditions, SLIC reduces computation cost by 93.3% while remaining highly consistent with a Monte Carlo Shapley baseline. In more general multi-role workflows, SSV aligns with perturbation-induced score-drop profiles and exposes cases where semantic contribution and failure impact diverge. Overall, SLIC provides a fast, counterfactual-free, and interpretable attribution method for complex LLM-based multi-agent systems.

---


### 7. [PEARL: Solver-in-the-Loop Interactive Optimization Modeling from Natural Language](https://arxiv.org/abs/2607.18256)

**<font color=#1a73e8>作者：</font>** Hongliang Lu, Zhong Li, Yuxuan Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Optimization modeling is the process of translating real-world decision problems, often described in natural language, into formal mathematical formulations and executable solver code. While recent advances in large language models have shown promise in automating this process, most existing approaches remain one-shot: a model produces a formulation once, without executing it, conditioning on solver feedback, or iteratively revising errors. This stands in sharp contrast to real-world optimization modeling, which is inherently interactive and proceeds through repeated solve-debug-revise cycles. We introduce PEARL, a system for interactive optimization modeling that uses Python execution and mathematical programming solvers inside this loop. Rather than relying on a fixed repair workflow, PEARL learns when to test partial models, how to revise from solver diagnostics, and when to stop. It operates in a multi-turn tool-integrated setting where intermediate execution results, feasibility signals, and solution checks are used to improve both formulations and solver code before finalization. Across diverse optimization benchmarks, PEARL substantially improves verified solve rates over strong one-shot and tool-augmented baselines; notably, our PEARL-Qwen3-\textbf{4B} model outperforms the much larger DeepSeek-V3.2-\textbf{685B} in both macro- and micro-averaged accuracy on optimization modeling tasks.

---


### 8. [S2T-RLHF: Hierarchical Credit Assignment for Stable Preference-Based RLHF](https://arxiv.org/abs/2607.18258)

**<font color=#1a73e8>作者：</font>** Wei Chen, Guanghui Zhu, Yafei Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) with preference-based reward models often exhibits unstable training dynamics. A key contributing factor is that standard RLHF relies on a single sequence-level scalar reward, which is propagated to token-level policy updates and leaves credit assignment within a response inherently ambiguous. Recent work has attempted to address this issue by refining rewards into denser token-level supervision, often relying on the implicit assumption that finer-grained credit assignment improves optimization. We argue that this assumption is incomplete: when preference signals are noisy and only defined at the response level, overly fine-grained reward refinement can amplify reward uncertainty and destabilize learning. To address this problem, we propose a granularity-aware principle for hierarchical credit assignment, emphasizing stability-oriented reward design rather than maximal allocation precision. Under this principle, sentences serve as a natural intermediate granularity, balancing semantic coherence with robustness to token-level noise. Guided by this view, we introduce S2T-RLHF. This sentence-to-token reward decomposition framework first allocates sequence-level preference rewards across sentences and then applies bounded token-level refinement within each sentence, without reward-model retraining or token-level supervision. Experiments across multiple datasets and optimization settings show that S2T-RLHF improves training stability and robustness while maintaining competitive preference alignment.

---


### 9. [Probabilistic Concept-Aware Steering for Trustworthy LLM Inference](https://arxiv.org/abs/2607.18259)

**<font color=#1a73e8>作者：</font>** Brian Becker, Rui Chu, Yingjie Lao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Steering vectors (SVs), an inference-time intervention technique for large language models (LLMs), guide the generation process by adding a concept-specific direction vector to intermediate activations during inference. However, existing SV methods frequently yield representation-incoherent behaviors that undermine interpretability and fine-grained control, largely because prior work has focused on binary positive-negative steering evaluation while employing discrete clustering metrics that fail to capture the continuous spectrum of semantic alignment. In this work, we present the Probabilistic Concept-Aware Steering (PCS) framework for LLM inference. PCS preserves original task competence while providing controllable, safety-oriented semantic bias through concept-driven steering-vector retrieval and probabilistic strength calibration.

---


### 10. [FindStatBench: Evaluating Large Language Models on Combinatorial Code Synthesis](https://arxiv.org/abs/2607.18260)

**<font color=#1a73e8>作者：</font>** Soham Dan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce FindStatBench, an execution benchmark for evaluating large language models on combinatorial code synthesis. Built from FindStat, it contains 2,329 tasks across 24 collections and 5.52M hidden instances, covering statistic synthesis, which maps objects to integers, and map synthesis, which maps objects to objects. Each task gives a mathematical description and at most five public input-output examples; a model must emit one Python solve function with no retrieval, tool use, execution feedback, voting, or reranking. Submissions are scored by exact sandboxed execution on held-out combinatorial objects. We evaluate eleven systems: four closed-source production models and seven open-weight models served through one inference provider. FindStatBench reveals three main patterns. First, the strongest open- and closed-source systems converge within 1 pp instance accuracy, and both an oracle over all systems and five-way sampling from one mid-tier model yield only limited task-accuracy gains. Second, examples can hurt: several classical bijections are solved perfectly with zero examples but fail under five-example prompts. Third, some failures reflect output-budget mechanics, as reasoning can exhaust the visible response before code is emitted. Overall, statistic synthesis is much easier than map synthesis, some collections remain near-zero, long prompts cause a sharp accuracy cliff, and exact symbolic rule induction remains brittle.

---


### 11. [When JSON Is Not Enough: Semantic Reliability of Schema-Constrained LLM Ordering Agents](https://arxiv.org/abs/2607.18261)

**<font color=#1a73e8>作者：</font>** Yin Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly used as transaction compilers: a user states an intent in natural language, and the model emits a structured object that an API can execute. JSON Schema and provider-level structured-output modes are useful because they remove a large class of parse failures, but they do not by themselves decide whether the object is a safe, faithful transaction. We introduce OrderBench, a deterministic benchmark for restaurant ordering agents that separates syntactic validity, schema validity, status decisions, exact item semantics, constraint preservation, and unsafe acceptances. Across 2,400 Nebius Token Factory calls to four open models in prompt-only and JSON-schema modes, we find that schema-valid output can still have large semantic error rates. In the strongest model, both modes achieve 100% schema validity, yet semantic success remains near 80%; in weaker models, schema-valid unsafe acceptances occur in double digits. The result is a concrete engineering warning: structured output is a necessary interface layer, not a substitute for domain verification and fail-closed execution.

---


### 12. [State Compression in Two-Agent LLM Relays: A Closed-World Study of Constraint Preservation](https://arxiv.org/abs/2607.18265)

**<font color=#1a73e8>作者：</font>** Anantha Sharma, Sheeba Elizabeth John, Kaarthik Senthil Kumar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running Large Language Model (LLM)-based agents often accumulate large intermediate traces containing audits, eliminations, and numeric calculations. In practice, this state is compressed before handing it to a downstream decision step, creating an information bottleneck in which small omissions can break strict numeric or categorical constraints. This paper evaluates hand-off compression in a closed-world travel-planning relay with two LLM agents. A Researcher audits a fixed inventory of hotels and flights for 50 goal instances, and a Booker selects a hotel--flight pair using only the goal and the hand-off payload, with the inventory withheld. We compare four hand-off conditions: no compression, narrative summarization, schema-constrained JSON extraction, and embedding-based pruning. Exhaustive enumeration over the fixed inventory provides exact feasible and optimal labels. Results show that hand-off representation strongly affects downstream feasibility under a small decision model. JSON extraction achieves the highest feasibility accuracy at 0.96, while narrative summarization, despite producing the smallest compressed hand-off payload, degrades feasibility to 0.48. Embedding-based pruning matches the uncompressed control on feasibility at 0.88 without an additional generative compression call. These findings indicate that constraint checking benefits from structured and auditable hand-off representations rather than relying on brevity alone.

---


### 13. [Structured Synthetic Reasoning Data for Arithmetic Fine-Tuning of Small Language Models](https://arxiv.org/abs/2607.18266)

**<font color=#1a73e8>作者：</font>** Jake O'Grady, Effirul Ramlan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small language models are attractive for local deployment, but they often struggle with multi-step arithmetic reasoning. We study whether structured synthetic reasoning data can improve this behaviour under consumer-hardware constraints. Starting from GSM8K, we generated a 21,250-example corpus of grade-school arithmetic word-problem variants using GPT-5-mini, combining natural-language solution traces, light Socratic-style cues, structural variation, and irrelevant distractor context. We then fine-tuned Qwen3-0.6B and Qwen3-1.7B with LoRA on consumer hardware (Apple M4, 16 GB RAM). Exact-match accuracy on GSM8K improved from 36.5% to 49.1% for Qwen3-0.6B and from 53.5% to 66.5% for Qwen3-1.7B. For Qwen3-1.7B, transfer to related arithmetic benchmarks was stronger, reaching 98.9% on MultiArith and 73.0% on SVAMP, compared with 54.4% and 45.3% for the base model. Qualitative analysis suggests that fine-tuned models produce shorter reasoning traces, make fewer arithmetic and distractor-use errors, and benefit more consistently from self-consistency sampling. These results show that low-cost synthetic data design can materially improve arithmetic adaptation in small language models. Because the intervention combines Socratic-style cues with other data-design choices, we interpret the gains as evidence for structured synthetic reasoning data rather than as a causal test of Socratic guidance alone.

---


### 14. [Fence: Specialized SLM Guardrails for LLM Applications](https://arxiv.org/abs/2607.18268)

**<font color=#1a73e8>作者：</font>** Kumud Lakara, Ruibo Shi, Fran Silavong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world applications that use closed-source large language models (LLMs) need advanced safety measures that go beyond the basic content filters. Content moderation filters such as toxicity and bias have relatively standard definitions where as application specific guardrails like hallucination, topic drift and behaviour deviation are more difficult to model and can vary by use case. Additionally, data scarcity and annotation costs, make the process of creating and testing specialized guardrails challenging. In this work, we propose using Small Language Models (SLMs) trained on synthetic data as specialized guardrails for LLM applications. We introduce a novel synthetic data generation method inspired by the design of Generative Adversarial Networks (GANs) to generate high quality synthetic data samples which can be used to train SLMs to encode use case specific guardrail information and hence function as specialized guardrails. Our experiments demonstrate that SLM guardrails trained on high quality synthetic data show performance gains over prompt based LLM guardrails.

---


### 15. [Wisdom of LLM Crowds: Aggregation and Contamination in Language Model Ensembles](https://arxiv.org/abs/2607.18269)

**<font color=#1a73e8>作者：</font>** Igor Douven  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The wisdom of crowds -- the finding that aggregating judgments across individuals often outperforms the best individual -- has been extensively studied with human forecasters. Whether the same phenomenon emerges when the ``crowd'' consists of large language models (LLMs) is an open question with both theoretical and practical implications. We elicited probability estimates from 15 LLMs on 254 binary prediction market questions and evaluated classical and learned aggregation methods. Learned aggregators -- a multilayer perceptron and a logistic regression -- outperformed all individual models and classical methods. The logistic regression was found to match the neural network, suggesting that the benefit of learned aggregation derives from learning a linear combination of diverse model outputs rather than from nonlinear interactions. Symbolic regression applied to the neural network's learned mapping recovered a pure model-disagreement signal as the lowest-complexity useful formula on the Pareto frontier, further supporting this interpretation. Training cutoff contamination proved a pervasive confound: the apparent capability gap between frontier cloud models and smaller local models collapsed from 35.8% to 8.9% on a clean subset of questions resolving after all models' training cutoffs, and individual model rankings showed only moderate stability. Even when the prediction market is evaluated at each model's training cutoff, LLMs remained substantially less accurate, indicating a genuine gap in collective information aggregation. These findings suggest that LLM crowds can exhibit wisdom-of-crowds effects, but that contamination-free evaluation is essential for reliable assessment.

---


### 16. [Using LLMs for Explainable, Data-Driven Insight Generation from Time Series](https://arxiv.org/abs/2607.18271)

**<font color=#1a73e8>作者：</font>** Ria Mundhra, Gustavo Sato dos Santos, Michael Benedikt  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time series forecasts are widely used in decision-critical domains, where they are rarely consumed without accompanying explanations. Producing such explanations is usually a manual and costly process, and attempts to automate it using large language models often suffer from hallucination when applied to temporal data. We propose a domain-agnostic framework for grounded natural language explanation generation for time series forecasts, illustrated in Figure 1. The framework consists of three components: (i) extraction of structured explanatory factors from historical analyst-written explanations, (ii) evidence-conditioned explanation generation, and (iii) scalable evaluation for readability, logical consistency, and persuasiveness. The design explicitly constrains generation to verifiable evidence, reducing unsupported claims.
We evaluate the framework on a financial forecasting case study involving the NASDAQ-100 index and a freight pricing case study using data from Vortexa. Results show that generated explanations approached analyst-written explanations in terms of readability, consistency and persuasiveness. These findings demonstrate that grounded explanation generation for time series forecasting can be achieved at scale without domain-specific fine-tuning.

---


### 17. [Beyond Single-Dimensional Compression: The Compound Sparsity Frontier of Large Language Models](https://arxiv.org/abs/2607.18280)

**<font color=#1a73e8>作者：</font>** Chao Han, Haozhe Hu, Xiaoyu Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are often compressed through static parameter pruning or dynamic token-level computation, yet aggressive sparsification can trigger rapid performance degradation beyond an essential sparsity boundary. This work asks \emph{whether combining these two mechanisms can delay such degradation by distributing the compression burden}. We study a minimalist compound sparsity framework that first applies low-rank approximation and channel pruning to obtain a statically compressed backbone, and then introduces lightweight routers for per-token dynamic layer skipping. This design enables independent control of parameter sparsity and token-level computation sparsity. Experiments across language understanding and modeling benchmarks show that compound sparsity consistently outperforms single-mechanism compression under the same total sparsity, delaying the decay point on understanding tasks and preserving stronger modeling performance. Further analysis reveals cross-dimensional interference between parameter pruning and token skipping, and shows that near-balanced allocation is most effective under a fixed sparsity budget. These results demonstrate that compound compression provides a practical way to improve LLM compression, while revealing a broader cross-dimensional sparsity boundary that ultimately limits further compression. Code will be available at this https URL.

---


### 18. [FedCC: A Low-Resource Federated Adaptation of Foundation Models for Robust Corpus Callosum localization in Fetal Ultrasound Images](https://arxiv.org/abs/2607.18283)

**<font color=#1a73e8>作者：</font>** Alessandro Di Matteo, Sara Moccia, Giuseppe Rizzo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate localization of the corpus callosum (CC) in fetal ultrasound (US) images is crucial for the early identification of neurodevelopmental abnormalities. However, this task remains highly challenging due to the intrinsic limitations of US imaging, including low contrast, speckle noise, and the considerable anatomical variability of the CC. We propose FedCC, a federated learning (FL)-based framework for CC localization in fetal US images, specifically designed for realistic multi-center and resource-constrained clinical settings without requiring data sharing. The framework integrates a frozen DINOv2 backbone with a lightweight YOLO-based detection head. To enable parameter-efficient adaptation, Low-Rank Adaptation (LoRA) modules are incorporated, allowing only a small subset of parameters to be optimized and exchanged among clients. This strategy substantially reduces both computational and communication overhead, making the framework suitable for low-resource environments. The proposed approach was evaluated on a multi-center dataset comprising 10,970 ultrasound frames acquired from 58 pregnant women during routine neurosonographic examinations across three clinical sites using heterogeneous imaging devices. The proposed framework achieved strong performance in the federated setting. In particular, the combination of DINOv2 and LoRA under the FedAvg strategy achieved an average mAP@50 of 0.857 and an F1-score of 0.803, outperforming both full fine-tuning and encoder-freezing baselines. Notably, the proposed approach reduced the number of trainable parameters to 2.9M compared with 24.4M in full fine-tuning, corresponding to an approximately 8.5$\times$ reduction in communication cost. These findings represent a promising step toward scalable, privacy-preserving, and clinically deployable AI systems for fetal neurosonography.

---


### 19. [Compressing What Matters: Neuron Importance Meets Data-Aware Low Rank Approximation for Language Model Compression](https://arxiv.org/abs/2607.18284)

**<font color=#1a73e8>作者：</font>** Athanasios Ntovas, Alexandros Doumanoglou, Petros Drakoulis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To excel at their domain large language models are comprised of billions of parameters. Yet this comes at the cost of huge memory requirements restricting their applicability in resource-constrained environments. To address the problem of neural network (NN) compression Singular Value Decomposition (SVD) has played a key role as a fundamental component for matrix compression through decomposition. To minimize compression error and to maximize the efficacy of the compressed model on the downstream tasks previous works focused on low-rank approximation of the NN's weight matrices either from the perspective of parameter importance or per-layer functional equivalence. While previous works studied the aforementioned perspectives in isolation in this work we are investigating the effectiveness of an approach that combines ideas from these two perspectives in a single objective. In parallel to this an important aspect that affects the compression quality is the distribution of the compression rate across layers and NN parameters. Earlier works mostly considered distributing the compression rate uniformly across layers and network weights or relied on computationally expensive heuristic search. Contrary to them in this work we propose an enhanced and computationally efficient algorithm for dynamic compression rate allocation. Experimental results support the efficacy of the proposed approach which performs on par or substantially better than the previous state-of-the-art especially under high compression ratios.

---


### 20. [One Student, Many Teachers: Multi-Task On-Policy Distillation via Soft-Prompt Privileged Context](https://arxiv.org/abs/2607.18293)

**<font color=#1a73e8>作者：</font>** Yingzi Ma, Zichen Zhu, Ming Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) teaches large language models new skills through a teacher that shares the student's backbone and supervises its own rollouts. Existing teachers either inject privileged context at the input -- inducing post-hoc rationalization -- or fine-tune weights, accumulating drift and forgetting across tasks. We propose \method, whose teacher differs from the student only by a learnable soft prompt: trained on $(x, y_\text{gold})$ pairs with the backbone frozen, the prompt yields a task-specific teacher that preserves the student's exact representational geometry. \method\ extends naturally to multi-task settings by routing each example in a merged corpus to its corresponding soft-prompt teacher, allowing a single student to absorb knowledge from $K$ teachers in parallel; at inference, all prompts are discarded. On Qwen3-1.7B-Base and Phi-4-mini-instruct across four tasks (Science, Tool Use, Biology, Math), the single-task variant (OPD with a PT teacher) matches or exceeds full fine-tuning while training orders of magnitude fewer parameters, and the multi-task variant achieves the best overall average ($56.2$ on Qwen3-1.7B-Base) while preserving general-capability benchmarks -- in contrast to sequential SFT, which degrades both.

---


### 21. [On the Limits of Support-Preserving Alignment and Bounded Filtering](https://arxiv.org/abs/2607.18295)

**<font color=#1a73e8>作者：</font>** Aryan Dutt, Rui Mao, Anupam Chattopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study whether alignment schemes that reshape a base model's output distribution, combined with bounded safety filters, can drive the probability of harmful behavior to zero in modern large language models. Recent research suggests that harmful behaviors can persist under preference-based alignment and that external filtering can be computationally hard in the worst case, but it remains unclear whether practical alignment pipelines that largely preserve internal representations can eliminate harmful behavior entirely rather than merely suppressing its most visible forms. We formalize this setting using support-preserving alignment operators together with bounded filtering algorithms under black-box, white-box, and statistical-query access, and analyze their ability to approximate an ideal eliminator that removes all harmful mass. Building on this framework, we provide computational and information-theoretic arguments indicating that, under these constraints, bounded filtering may fail to eliminate all harmful outputs supported by the base model's distribution. To evaluate these limits empirically, we analyze a range of state-of-the-art open-weight and hosted LLMs accessed via OpenRouter under bounded black-box, white-box, and statistical-query filters on adversarial prompts drawn from curated cybersecurity scenarios and PKU-SafeRLHF. Across models, filter classes, and query budgets, the estimated harmful-output rate decreases with additional filtering compute but consistently plateaus above zero, suggesting a persistent empirical harm floor.

---


### 22. [A Better Start for Language Models: Domain-Conditional Position Offsets](https://arxiv.org/abs/2607.18302)

**<font color=#1a73e8>作者：</font>** Ye Qiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive language models are least accurate at the beginning of a sequence, where little context forces reliance on a generic pretraining prior. We show that this cold-start penalty is domain dependent and reduce it with a domain-conditional position offset: a single learned vector added to the embedding activation at the first sequence positions while all model weights remain frozen. The offset trains in minutes on roughly one hundred documents, switches between domains without added sequence state, and has no measurable latency overhead. Across eight Mamba, GPT-NeoX, and Llama models spanning 410M to 8B parameters, it reduces held-out in-domain perplexity by up to 27%; the effect persists at 70B, and one position captures most of the benefit. A matched, converged direct logit-bias correction reaches at most only 7.9% and leaves later-token loss unchanged, showing that the offset propagates through model state rather than merely recalibrating the output prior. A tuned LoRA reaches lower perplexity but uses two to three orders of magnitude more parameters and an active low-rank weight path, while soft prompts add sequence positions. With wrong-domain controls, offsets improve retrieval reranking and domain classification when decisions depend on early in-domain tokens, For the few-shot reasoning whose signal occurs later, the results maintains unchanged. Position-aware prefill application also help generation tasks, whereas naive application at every cached decoding step causes repetition. The offset is therefore not the strongest adapter, but a lightweight, hot switchable tool for short in-domain scoring and calibration.

---


### 23. [TD-DPO: Difference-Aware Preference Optimization for Mitigating Sycophancy in Clinical Autism Intervention Dialogue](https://arxiv.org/abs/2607.18304)

**<font color=#1a73e8>作者：</font>** Shuzhong Lai, Junhong Lai, Chenxi Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The sycophancy of large language models can increase the safety risk in intervention dialogue for autistic children. Supervised fine-tuning can somewhat reduce sycophancy, but relying solely on positive examples is often insufficient to identify and correct failure patterns. We observe that sycophancy behaviors can often be localized to a limited span within the model response. In this regime, sequence-level preference optimization can over-update preference-irrelevant tokens and degrade intervention ability. To address this, we propose the \textbf{M}inimal \textbf{E}dit \textbf{D}ata \textbf{A}ugmentation (MEDA) strategy to construct controlled, stable, minimal edit preference pairs and \textbf{T}oken-level \textbf{D}ifference \textbf{D}irect \textbf{P}reference \textbf{O}ptimization (TD-DPO), which upweights difference tokens between chosen and rejected responses while downweighting shared tokens to suppress background drift. Extensive experiments across multiple backbones and evaluators show that TD-DPO achieves a better trade-off between sycophancy mitigation and intervention ability retention in our offline settings, highlighting its potential as a practical alignment approach for autism intervention.

---


### 24. [The Information Shadow: Measuring Structural Limits on What Language Models Can Learn](https://arxiv.org/abs/2607.18305)

**<font color=#1a73e8>作者：</font>** Priyansh Srivastava, Romit Chatterjee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Some limits on what language models know are not gaps in data coverage but structural properties of learning from text. We introduce the information shadow: the region of phenomena that a text-trained learner cannot acquire regardless of scale, comprising (I) structures language cannot express, (II) functions that are statistically non-identifiable from the training distribution, and (III) functions that are representable but unreachable by gradient-based training. We give each type a probe that is decisive because the premise of the shadow is, in that setting, provable. For Type I, Language Compression Residuals compare a text learner, which sees only a lossy text-like encoding of the signal, against a full-signal learner, which sees the underlying signal directly. The text learner sits at a computable expressibility ceiling while the full-signal learner pulls away by a gap that stays flat across 300x more data, so the deficit is a property of the channel, not of training. For Type II, the Counterfactual Distinction Test trains models on data exactly consistent with two incompatible rules. Across a provable string task and a language-like agreement task, behavior on counterfactuals is set by the model's inductive bias, while 5% disambiguating data steers the learned rule bidirectionally to either target (r = +/-1.0, p < 1e-10). For Type III, Basin Escape Mapping exhibits a function that is representable at 100% (by hand construction) yet reached 0% of the time by standard training and instantly from a nearby initialization, with width scaling providing no help (p = 1.6 x 10^-14). Each effect is isolated by a control that rules out a capacity or modality artifact. We release the probe suite and discuss implications for benchmark design, capability auditing, and shadow-aware uncertainty.

---


### 25. [Agentic Calibration of Grey-Box Simulation Models: An LLM-Driven Alternative](https://arxiv.org/abs/2607.18308)

**<font color=#1a73e8>作者：</font>** David Gómez-Guillén, Mireia Diaz, Josep Lluis Arcos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Calibration of grey-box simulation models is a constrained optimization problem in which model evaluations are expensive, the parameter space can be high-dimensional, and the search must respect plausibility constraints. Although the simulation code is fully available to the analyst, the joint effect of multiple parameters remains difficult to predict analytically. Classical optimizers such as Nelder--Mead (NM) are simple to deploy but sample-inefficient, particularly under constraints. Modern Bayesian Optimization methods achieve competitive solutions with far fewer evaluations but require non-trivial modeling machinery for constraint handling. We introduce an agentic calibration method in which a large language model acts as the optimizer, with constraints incorporated as a plain-language section of the system prompt. We evaluate the agentic method, NM, and Bayesian Optimization (BO) on an anal cancer simulation model under both unconstrained and clinically constrained calibration. Under unconstrained calibration, the agentic method achieves substantially lower best error than BO and NM, while requiring fewer model evaluations. Under constrained calibration, the agentic method reaches comparable error levels and both outperform NM. These results are obtained at the cost of increased inference time per iteration. Agentic calibration achieves competitive performance with substantially fewer model evaluations, and constraint handling is essentially free at the modeller-facing interface through simple textual specifications rather than additional modelling machinery. The main trade-off lies in increased per-iteration inference cost, making the approach particularly suitable when simulation time dominates. Beyond performance, the per-iteration rationale makes the search auditable and explainable, so its decisions can be scrutinised and justified to third parties.

---


### 26. [Physics-Guided Masked Multi-Task Network for Edge-Friendly Battery Health Diagnostics from Sto-chastically Fragmented Charging Profiles](https://arxiv.org/abs/2607.18330)

**<font color=#1a73e8>作者：</font>** Shuhao Chen, Tianyu Shi, Chengyi Tu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The deployment of reliable lithium-ion battery management systems is crucial for accelerating electrification, yet the joint prognosis of State of Health (SOH) and Remaining Useful Life (RUL) remains severely hindered by task heteroscedasticity. Conventional multi-task learning frameworks fail to balance the bounded, low-variance noise of SOH estimation with the unbounded, nonlinearly expanding uncertainty of long-term RUL predictions. Here, we present the Rotary SOH-Injected Prior Battery Transformer (RoSIP-Batt), a unified co-estimation framework that resolves these optimization conflicts. By formulating joint prediction as a Bayesian multi-task objective, RoSIP-Batt introduces a homoscedastic uncertainty weighting mechanism to dynamically scale task-specific gradients based on learned residual noise levels. The architecture leverages decoupled dual classification tokens and a per-dimension gated fusion mechanism, secured by a gradient-detachment operator to prevent high-variance RUL updates from corrupting the stable SOH representation space. To capture electrochemical degradation patterns without relying on absolute cycle steps, Rotary Position Embedding (RoPE) is incorporated into a shared Transformer backbone to model translation-invariant relative temporal profiles. Crucially, the intermediate SOH estimate is directly injected into the RUL regression head as a physical degradation prior. Evaluations across the NASA, MIT-Stanford, and HUST datasets show that RoSIP-Batt significantly outperforms state-of-the-art baselines, reducing SOH estimation error to 1.994% MAE on NASA and restricting RUL prediction error to 62.85 cycles on Stanford. These findings establish RoSIP-Batt as a highly generalizable, computationally efficient solution suitable for real-time embedded BMS deployment.

---


### 27. [Federated Lightweight Fine-Tuning](https://arxiv.org/abs/2607.18343)

**<font color=#1a73e8>作者：</font>** Radhakrishna Achanta, Will Reed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated fine-tuning is bottlenecked by communication: FedAvg and pseudo-gradient schemes transmit a payload that scales with the model, and gradient compression shrinks it by only a constant factor. We take a different lever. Mapping networks generate a network's weights from a small trainable latent through a frozen affine projection; because the map is shared and affine, averaging latents is exactly averaging the generated weights. We turn this into a practical low-bandwidth federated channel with two changes: a low-rank, seed-regenerable factorisation of the projection (cutting generator memory from ~80 GB to ~10 MB), and a delta formulation $\theta = \theta^{\mathrm{pre}} + U V^{\top} z$ that learns an additive correction around a shared centrally-pretrained base -- federated fine-tuning, which is what makes the method work at scale. A frozen orthogonal classifier head further removes the head from the payload while improving accuracy. On CIFAR-100 with ResNet-18+GroupNorm, our method (FLITE, Federated Low-rank Iterative Training Engine) communicates 1,280 floats (~5 KB) per client per round -- an 8718x reduction -- and reaches 74.67%, within ~0.5 pp of full-weight FedAvg. The averaging identity holds to floating-point precision ($6 \times 10^{-8}$); the method sits one to two orders of magnitude below PowerSGD and top-k on the bandwidth-accuracy Pareto; it matches or exceeds full-weight FedAvg under strong non-IID skew. int4 latents reach 648 bytes per round at unchanged accuracy, whereas int4 full-weight FedAvg collapses to chance.

---


### 28. [Operational Hallucination and Safety Drift in AI Agents](https://arxiv.org/abs/2607.18366)

**<font color=#1a73e8>作者：</font>** Shasha Yu, Fiona Carroll, Barry L. Bentley  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) serving as planners in tool-using autonomous agents introduce dynamic reliability risks in multi-turn execution. While single-turn safety mechanisms are relatively mature, extended interactions reveal structural vulnerabilities where initial alignment degrades over time. This paper empirically characterizes two observed failure modes across multiple state-of-the-art LLMs: Safety Drift, the gradual erosion of declared safety intent leading to constraint-violating actions (e.g., textual refusal followed by reconnaissance and unsafe execution), and Operational Hallucination, persistent repetitive tool calls indicative of flawed state perception (e.g., livelocks even in legitimate tasks). Through controlled multi-turn evaluation on high-stakes ethical dilemmas, malicious requests, and benign controls, we quantify these phenomena using declaration-action gap and livelock metrics, demonstrating their cross-model prevalence under direct execution protocols. Root-cause analysis attributes the instabilities to the decoupling of reasoning context from execution state in current agent loops. We propose an Action-Aware Supervision Layer - a lightweight, plug-and-play architectural blueprint incorporating intent-action consistency checks, runtime state tracking, and forced termination primitives. Post-hoc simulation on captured failure trajectories shows the layer can intercept observed violations without false positives on benign cases. This work advances agent reliability by shifting focus from linguistic safeguards to enforceable architectural mechanisms for responsible agentic AI.

---


### 29. [AlayaWorld: Interactive Long-Horizon World Modeling -- Full Technical Report](https://arxiv.org/abs/2607.18367)

**<font color=#1a73e8>作者：</font>** AlayaWorld Team, Kaipeng Zhang, Chuanhao Li 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Unlike conventional video game development, which relies on labor-intensive pipelines for asset production, animation, physics, and programming, video world models generate interactive environments from user inputs instantly. It enable us to create customized, explorable, and continuously evolving virtual world from text, an image, or video. Realizing this vision requires four tightly coupled capabilities: interaction, persistent spatiotemporal consistency, stable long-horizon generation, and efficient response. We present AlayaWorld, an interactive long-horizon video world model that generates 24-fps video at 540p and 720p. Built on a 15B video diffusion transformer, AlayaWorld generates short latent chunks autoregressively under camera trajectories and switchable text prompts. Its bounded visual context combines a persistent sink frame, compressed temporal history, geometry-aligned spatial memory, and recent-frame conditioning. To reduce long-term drift, the model is trained with corrupted histories and prediction residuals collected from its own roll-outs. We further introduce a discrete autoregressive distillation formulation that combines distribution-matching distillation, self-forcing++, and consistency distillation, reducing inference from approximately 30 sampling steps to four steps per chunk. On iWorld-Bench, AlayaWorld achieves the best performance over long-horizon generation. Conceived as a full-stack, open-source, and long-term project, AlayaWorld is intended to provide an extensible foundation for future research on interactive video world models.

---


### 30. [Convolution for Large Language Models](https://arxiv.org/abs/2607.18413)

**<font color=#1a73e8>作者：</font>** Yuchuan Tian, Yingte Shu, Wei He 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) largely rely on Transformers, where self-attention provides global token interaction but does not explicitly encode the locality of natural language. We study whether lightweight depthwise convolutions can supply this local inductive bias without materially increasing model size. Our macro-level ablation compares convolution at 17 locations in a Qwen3 Transformer block and finds the best results when convolution is applied to the projected queries, keys, and values before attention. A subsequent micro-level study favors a residual depthwise convolution with kernel size $k=3$, without additional normalization or activation. Across Qwen3 models and several pre-training data budgets, this design improves the average accuracy on seven downstream benchmarks while adding less than $0.01\%$ parameters. A representation-level case study further suggests that the convolution makes repeated token IDs more sensitive to their immediate context. These results support depthwise convolution as a lightweight complement to self-attention for modeling short-range token interactions.

---


### 31. [Relay-Bench: Evaluating LLMs on Multi-Domain Reasoning Chains](https://arxiv.org/abs/2607.18438)

**<font color=#1a73e8>作者：</font>** Liam Swayne  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Introducing Relay-Bench, an unsaturated, holistic, text-only benchmark that measures LLMs' ability to complete an assortment of tasks from distinct domains in a single prompt. The leading model, GPT-5.5 (xHigh), scores 43.3%. The test set entirely consists of composite problems: groups of single-domain subproblems that are strung together into challenges that require reasoning across multiple domains in combination. Many of these problems then have layers of complexity added through prompt encoding and deliberate context bloat. Domains tested include visual reasoning, coding, math, information extraction (with a focus on web search), problem-solving, general knowledge, and data analysis. No restrictions are imposed outside of the model harness, and models are explicitly encouraged to leverage code-execution, web searches, and all available tools. All problems are composed of two to thirteen subproblems and do not require multi-modal input or output.

---


### 32. [Computational models of pragmatic reasoning with flexible generation of meaning and expression alternatives](https://arxiv.org/abs/2607.18443)

**<font color=#1a73e8>作者：</font>** Polina Tsvilodub, Fausto Carcassi, Michael Franke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pragmatic language use requires reasoning about alternatives: the alternative expressions a speaker might have chosen, or the alternative interpretations a listener might entertain. Formal and computational models of pragmatics must therefore specify the sets of alternatives that interlocutors reason over, which is often done through manual specification. Here we propose a framework, ScAffolded Generative models for Explanation (SAGE), that combines the explanatory transparency of cognitive models with the generative flexibility of language models (LMs). SAGE decomposes a pragmatic process into three kinds of modules: proposers, which use LMs to generate an open-ended space of candidate alternatives; evaluators, which assess those alternatives (e.g., their semantics, complexity, or typicality); and selectors, which implement the rule-based computational steps of a cognitively motivated task analysis. We assess SAGE in three case studies spanning pragmatic generation and interpretation-referential expression generation, manner (M-)implicatures, and Gricean conversational implicatures. SAGE models are evaluated critically using established methods from computational cognitive modeling, including ablations, baseline comparisons, and quantitative fit to human data. Across studies, SAGE models achieved high accuracy and often outperformed baselines, but component-level analyses reveal an asymmetry: LM proposers reliably generated alternatives well-suited to pragmatic modeling, whereas LM evaluators are better at providing intuitive judgements rather than judgements of theoretical or formal measures. We discuss the promise and the limitations of neuro-symbolic models as candidate explanatory accounts of human pragmatic language use.

---


### 33. [Using Fine-Tuned LLMs to Identify Indicators of Vulnerability in UK Police Incident Logs](https://arxiv.org/abs/2607.18446)

**<font color=#1a73e8>作者：</font>** Sam Relins, Daniel Birks  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Purpose: Understanding how much of routine policing involves vulnerable people could inform resourcing, training, and multi-agency response, yet administrative data provide limited insight. We explore whether an LLM-based classification pipeline, developed on open-source US police data, can be adapted to estimate the prevalence of four vulnerability indicators - mental ill health, substance misuse, alcohol dependence, and homelessness - in UK police incident narratives, and when outputs can be treated as defensible measurements.
Methods: We analyse nearly 3,000 de-identified incident logs from a UK police force, using a multi-stage pipeline combining repeated model inference, label aggregation, structured human review, and statistical correction. The pipeline runs on a locally hosted open-weight LLM, reflecting the secure environments police must work in.
Results: LLMs can produce meaningful, if imperfect, prevalence estimates at scale. Mental ill health indicators are present in approximately one in five incidents, with lower prevalence for other indicators. However, naive LLM deployment is unreliable: single-pass classifications are unstable, and aggregated outputs systematically over-assign indicators relative to human judgement. Correcting these biases required substantial human input and statistical adjustment, leaving considerable uncertainty.
Conclusions: While LLMs can extract information from unstructured police data, their outputs cannot be treated as valid measurements without careful methodological support. At the population level, defensible estimates are achievable but resource-intensive; at the individual level, errors remain frequent and unpredictable, limiting suitability for operational decisions. This study highlights both the potential and the constraints of LLM-based measurement in applied settings.

---


### 34. [Estimating Rare Events in Language Models with Proper Evaluation](https://arxiv.org/abs/2607.18454)

**<font color=#1a73e8>作者：</font>** Nikita Y. Parulekar, Anqi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantifying the risk of rare failures in language models, such as those triggered by adversarial distribution shifts or very large-scale deployments, requires estimating probabilities far too small for random sampling. While recent work has formalized Low Probability Estimation, existing pipelines remain fragile in the rarest regimes: estimators can suffer zero-estimate collapse or systematic bias, and standard evaluation losses can become unstable or poorly matched to asymmetric safety costs. In this work, we introduce Gradient Activation Adaptive Multi-Level Splitting (GA-AMLS), which adapts rare-event Monte Carlo methods to the continuous activation space of language models. Specifically, GA-AMLS uses a gradient-based MCMC kernel to navigate activation space, eliminating the zero-estimate collapse of input-space search and replacing the independence assumptions of prior activation-space estimators with conditional sampling under an explicit, heavier-tailed activation prior. We also propose the Shifted-Power Bregman (SPB) Loss, a proper scoring rule that remains finite for zero-estimates and offers tunable asymmetry between underestimation and overestimation penalties. Experiments on small transformer models reveal a bias-variance tradeoff: GA-AMLS achieves the lowest loss under symmetric evaluation, reducing average log-space squared error relative to the strongest baseline across model sizes, while methods with overestimation bias prevail under asymmetric penalties. Our findings highlight that estimator choice should be matched to deployment context. More broadly, our work establishes activation space as a tractable domain for rare-event estimation in language models, circumventing the brittleness of discrete input-space search.

---


### 35. [Structured Output Collapses Answer Diversity Across 44 Language Models](https://arxiv.org/abs/2607.18476)

**<font color=#1a73e8>作者：</font>** Tapan Parikh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model must choose one answer from a large space of equally valid options, a format clause -- "Reply with JSON only" -- changes which answer it chooses. We re-run the One-Word Census (arXiv:2607.12796): 31 wide-answer-space category prompts asked of 44 models, now with the reply requested in JSON -- no schema enforcement, no constrained decoding, only the request. Convergence deepens sharply: on the unconstrained "Pick a word" prompt the modal answer rises from 41% to 64% of the pool and distinct answers fall from 52 to 36; mean answer-choice surprisal drops from 1.80 to 1.58 bits. The tax is progressive: six of 44 models move individually (BH-FDR q=.10), all toward the mode, led by the most distinctive models, while the conformist floor is immobile. It is a sharpener, not a re-indexer -- the plain-chat modal answer survives in 28 of 31 categories. Defaults are register-indexed: a within-run re-sample (n=20) finds JSON shifts 53% of a model's stable chat defaults, mostly back to the crowd, and installs defaults absent from chat (Claude Fable 5 answers "cerulean" for colour 0% of the time in chat, 100% in JSON). Full-battery controls reveal a register gradient: compression is significant and specific to the answer-delivery formats models are trained to speak (JSON -0.22 bits, p=.0002; XML -0.19, p=.002), absent for YAML and CSV, and reversed for an arbitrary bracket wrapper (+0.13, p=.009) -- weighing the mechanism toward tool-use post-training. Enforcing the schema at the decoder (response_format) compresses no further than the request (-0.03 bits): the collapse lives in the model's response to the register, not the decoder. Structured output is how software consumes language models, and that surface is served by a measurably more homogeneous model than the chat surface on which models are evaluated, compared, and chosen.

---


### 36. [Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning](https://arxiv.org/abs/2607.18481)

**<font color=#1a73e8>作者：</font>** Jia Ao Sun, Hao Yu, Fengran Mo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question answering (KGQA) requires navigating from topic entities to an answer several relations away. Recent methods prompt a frontier LLM to explore the graph through a retrieval tool, but their reliance on frontier-scale inference makes them costly to deploy. We present Search-on-Graph-R1 (\sogrone{}), which internalizes this navigation into a compact 8B model through supervised fine-tuning (SFT) followed by reinforcement learning (RL). Our central idea is to scaffold a frontier teacher with each question's gold SPARQL query, so the teacher traverses a known answer-bearing path with a live \texttt{Search} tool rather than having to discover the path itself. Since every call executes against a live Freebase server, the resulting trajectories are grounded in the knowledge graph by construction. On WebQSP, CWQ, and GrailQA, \sogrone{} at 8B surpasses every frozen frontier-LLM system in our comparison and posts the strongest results on CWQ of any system we compare against. It does so using no auxiliary module at inference and no LLM judge during training. Isolating each training stage shows that SFT and RL contribute complementary gains, our approach transfers across model families, and RL learns to reach answers in fewer \texttt{Search} calls than its SFT initialization.

---


### 37. [Querying Multimodal Scientific Papers with AI: Practices and Preferences Across Blind, Low-Vision, and Sighted Scientists](https://arxiv.org/abs/2607.18514)

**<font color=#1a73e8>作者：</font>** Arnavi Chheda-Kothary, Lucy Lu Wang, Joseph Chee Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visual diagrams, figures, and tables are central to scientific papers, and convey information beyond what is captured in text. While blind or low-vision (BLV) scientists have traditionally relied on static alternative text to access figures in papers, the rise of artificial intelligence (AI) has made interactive question-answering (QA) a feasible paradigm for visual exploration; yet little is known about how scientists use visual QA in practice or how to improve its accessibility. In this work, we interview five BLV and five sighted scientists across different STEM fields to understand how they use two AI tools, ChatGPT and Gemini, to query multimodal scientific documents. Our findings characterize how scientists review multimodal content, including existing practices (along with accessibility workarounds) for engaging with visuals, and feedback on the suitability of AI-generated responses to multimodal queries. We further find that vague or incomplete image descriptions, as well as incorrect AI outputs more broadly, can cause both BLV and sighted scientists to abandon AI workflows. To support future research, we additionally contribute a dataset of 115 queries and responses from our participants' interactions with the AI tools for papers in their field. We close by discussing implications for AI-powered scientific QA systems, emphasizing considerations for access across abilities and domains.

---


### 38. [EduPanel: A Three-Agent LLM Judge for Teaching Videos -- Reliability, Complementarity, and Human Trust Calibration](https://arxiv.org/abs/2607.18529)

**<font color=#1a73e8>作者：</font>** Jia-Kai Dong, Yi-Cheng Lin, Hung-yi Lee  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Teaching videos are becoming a major medium for education, creating a growing need for scalable evaluation of their pedagogical quality. Existing automatic judges do not fully address this setting because teaching quality depends on multimodal evidence and should be evaluated with respect to the intended learner rather than as a universal property. We present EduPanel, a rubric-grounded, learner-conditioned LLM judge that decomposes evaluation across specialized agents to produce interpretable assessments for different aspects of teaching quality. Across expert studies, architecture ablations, and learner-persona analyses, EduPanel achieves reliability comparable to a median human expert. In expert evaluation, its feedback improves scoring accuracy (MAE 0.87 to 0.73), while experts remain able to detect unreliable outputs (AUC = 0.77) instead of accepting them blindly. These results suggest that EduPanel can serve as effective assistants for educational evaluation rather than replacements for human experts.

---


### 39. [Censoring-Aware In-Context Learning for Generalized Supplier Lead Time Estimation in Supply Chain Planning](https://arxiv.org/abs/2607.18530)

**<font color=#1a73e8>作者：</font>** Christopher Wang, Sebastien Ouellet, Behrouz Haji Soleimani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Supplier lead time forecasting is a central input to material requirements planning, inventory optimization, and supply chain risk management. However, many industrial lead time datasets are naturally right-censored: at the time forecasts are required, some orders have not yet arrived. Standard regression and classification approaches discard this information, while conventional survival models require task-specific modeling. We propose LeadTime-ICL (LT-ICL), a censoring-aware in-context learning model for probabilistic lead time forecasting. LT-ICL combines a transformer backbone with a conditional normalizing-flow head, producing a full predictive distribution over lead times. The model is pretrained on synthetic right-censored lead time tasks, enabling in-context adaptation to new industrial datasets without task-specific parameter updates. We provide theoretical support for this formulation by showing that excess CRPS is bounded by prior misspecification and amortized approximation errors, providing clear direction for improving forecasting performance. We evaluate LT-ICL on 24 proprietary supply-chain datasets spanning seven industries. LT-ICL achieves the lowest point-forecasting error on 15 of the 24 datasets, and the lowest probabilistic forecasting error on 14 datasets, yielding the best average rank across both. These results support right-censored probabilistic forecasting as a practical formulation for supplier lead time prediction and demonstrate that pretrained in-context models can provide accurate, low-adaptation-cost forecasting for industrial planning systems.

---


### 40. [Reasoning Fine-Tuning Induces Persistent Latent Policy States](https://arxiv.org/abs/2607.18532)

**<font color=#1a73e8>作者：</font>** Abir Harrasse, Michael Lan, Hunar Batra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning-specialized language models show large performance gains over base models, yet the internal changes responsible for improved multi-step reasoning remain poorly understood. It is unclear whether reasoning fine-tuning improves local token-level competence or globally reorganizes how models structure inference over time. We address this question by modeling Chain-of-Thought reasoning as a switching dynamical system (SDS), in which internal representations evolve under discrete latent policy states. Our framework combines time-aware contrastive representation learning with discrete regime discovery to recover latent policies from activation trajectories. Across four benchmarks and model scales from 1.5B to 32B parameters, reasoning-fine-tuned models exhibit richer latent-policy organization than their base counterparts, characterized by more differentiated transition structure and model-dependent changes in state utilization, persistence, and mixing. The recovered regimes exhibit functional specialization aligned with distinct reasoning stages, and extensive controls confirm that their structure is not explained by correctness, representation learning, or modeling priors, but depends on the coherent temporal organization of reasoning trajectories. Causal interventions further show that the regimes are functionally meaningful: state-swap ablations reduce one-step predictive fit, while transplanting reasoning dynamics into base models improves performance on challenging reasoning problems. Finally, SDS-guided pruning of failure-prone reasoning prefixes outperforms self-consistency in 11 of 12 model-dataset settings, with gains of up to 12.5 percentage points. Together, our results suggest that reasoning fine-tuning globally reorganizes latent dynamics, offering a new lens for mechanistic analysis and process-level control of reasoning models.

---


### 41. [MAGE: Human-Like Macro Placement via Agentic Multimodal Reasoning](https://arxiv.org/abs/2607.18536)

**<font color=#1a73e8>作者：</font>** Andrew B. Kahng, Sayak Kundu, Bodhisatta Pramanik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Macro placement still requires substantial manual refinement in industrial physical design flows. We present MAGE (Macro Placement Agentic Engine), a multimodal multi-agent framework for macro placement refinement. MAGE decomposes the macro placement task into a six-phase workflow that combines structured floorplanning rules, visual checks, and iterative refinement. Expert floorplanning knowledge is encoded through natural-language directives and validation criteria, rather than learned from labeled placement data. A tournament-style refinement mode evaluates multiple candidate placements and propagates feedback from higher-quality solutions. We also introduce four metrics for quantifying human-likeness in macro placement: notch score, whitespace score, pocket score, and alignment score. These metrics capture structural properties used by expert designers but not directly measured by conventional PPA metrics. Across nine designs in NanGate45 and GlobalFoundries 12nm enablements, MAGE achieves geometric-mean improvements of 11.1%-19.3% in WNS and 70.0%-74.0% in TNS over commercial macro placers. On the three NanGate45 designs, for which human-expert and Hier-RTLMP baselines are available, MAGE improves WNS and TNS by 18.3% and 72.5% over the human expert, and by 47.0% and 80.4% over Hier-RTLMP, with comparable wirelength and power. On human-likeness metrics, MAGE improves the overall score by 6%-48% over all baselines. Additional case studies on anonymized netlists, unseen designs, dense rectilinear floorplans, and high-utilization settings show that the framework transfers to new placement settings without design-specific retraining.

---


### 42. [Engineering Trustworthy Agentic AI for Critical Systems](https://arxiv.org/abs/2607.18548)

**<font color=#1a73e8>作者：</font>** Omar Al-Refai, Ibrahim Shahbaz, Adam Ali Husseinat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic artificial intelligence systems, capable of autonomous perception, planning, tool use, and multi-step action, are increasingly proposed for critical engineering domains where decisions carry physical, operational, or economic consequences. This survey addresses a gap in current literature by treating trustworthiness, whether agentic behavior can be verified, audited, and trusted under the constraints that engineering practice actually requires, as a first-class engineering property, rather than evaluating agentic AI by task capability alone. The study adopts a trustworthiness model organized around five cross-cutting dimensions: safety and constraint satisfaction; robustness and reliability; transparency and interpretability; accountability and auditability; and privacy and security. This is mapped onto an agentic assurance workflow spanning perception through audit. Building on this foundation, agentic systems architectures, threats, concrete trust mechanisms, and quantitative metrics are surveyed for direct application in agentic systems development and evaluation. These principles are then examined across four constraint-bound engineering domains: power systems, autonomous vehicles/robotics/UAVs, high-performance computing, and communication networks, identifying recurring design patterns, shared failure modes, and domain-specific gaps. Synthesizing across those domains, agentic AI trustworthiness is shown to be a single problem, with a path outlined toward a reusable, cross-domain assurance framework analogous to the graded certification regimes used by mature safety-critical engineering fields.

---


### 43. [Operational Proto-Introspection in Looped Language Models: Process-Quality Taps, Executable Branching, and the Readout-Control Boundary](https://arxiv.org/abs/2607.18553)

**<font color=#1a73e8>作者：</font>** Jan Kirin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can a language model read the quality of ongoing computation, and can an external intervention turn that readout into better outcomes? We test both questions in a frozen 2.6B looped transformer, Ouro-RLTT. On GSM8K, a strict pre-answer probe excludes the answer region and gold value yet predicts eventual success: hidden states plus length and log-probability shortcuts reach AUROC 0.797, versus 0.731 for the shortcuts alone (incremental +0.066; task-clustered 95% CI [+0.021, +0.112]; 170 tasks, 680 candidates). Low-capacity taps also read role-specialized properties: task-disjoint branch survival reaches 0.9697 oracle retention, content ranking reaches 0.6310 macro top-1, and generated-branch correctness reaches AUROC 0.7755. A non-looped control replicates a candidate-quality readout, so recurrence is not required for every signal.
We build branch/carry/prune machinery over Ouro's 192-slot recurrent cache, including branch-specific cache lineage and a bit-exact residual-capture splice that recomputes only the affected suffix and saves up to 88% of per-branch layer passes. No frozen intervention produces a validated capability gain. Directional steering is an established negative; a four-task matched-sampling comparison removes evidence for a frozen-fork gain but cannot estimate a general deficit; terminal selection remains unresolved and underpowered; and bounded LoRA changes surface behavior without improving net reachability. A two-null audit does not support the simplest span-misalignment explanation.
We call this readable-but-not-yet-usable property operational proto-introspection. The model is not consulting our probes: we read its hidden trajectories, and our interventions fail to convert those readouts into validated capability. The pre-answer result is limited to one domain. Load-bearing values use source-item-disjoint splits and antisymmetrized evaluation where applicable.

---


### 44. [The Story Shapes the Agent: Narrative Priors in LLM Behavior](https://arxiv.org/abs/2607.18566)

**<font color=#1a73e8>作者：</font>** Yixuan Wang, James Lester, Shashank Srivastava  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Persona prompting is widely used to steer LLM agent behavior, yet the narrative framing of a task can matter more than the assigned persona. We isolate this effect through structural isomorphism, constructing three text-based investigation games that share the same action space, stage progression, and resource constraints while varying only task narrative: disease investigation, IT troubleshooting, and murder mystery. Across 1,890 sessions spanning 3 models and 10 personas, we identify narrative priors: systematic action tendencies activated by a task's story framing, independent of its decision structure. Narrative priors explain 5-31x more behavioral variance than persona, are consistent across model architectures, and in two of three domains are negatively associated with task success. Persona effects that do transfer across narratives arise from behavioral anchors, persona descriptions whose language maps directly onto shared actions. Causal interventions confirm this: removing anchor words from a high-transfer persona reduces cross-narrative consistency by 95%. Our framework also generalizes to a held-out fourth narrative and yields a persona-selection method that improves cross-narrative transfer. These results suggest that LLM behavior that survives narrative changes should be grounded in concrete actions rather than abstract descriptions.

---


### 45. [Attacking Graph Foundation Models Through Their Shared Representation](https://arxiv.org/abs/2607.18567)

**<font color=#1a73e8>作者：</font>** Pankaj Kumar, Subhankar Mishra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A graph foundation model generalizes across graph domains by mapping every input into one shared representation before any task reasoning. We call this map the alignment layer, the component that separates a graph foundation model from a graph neural network, and we show it is a distinct attack surface that prior work has not studied. We attack it at inference time, with no access to training, on six public models spanning spectral tokenizers, text embedding spaces, and a discrete codebook. A directed representation-space perturbation collapses every model, but at a budget comparable to the representation norm a plain graph network also needs, with one exception: OpenGraph, whose spectral tokenizer collapses at a fifth of that budget, an alignment-specific fragility a plain network does not share and which a same-representation control traces to the tokenizer rather than the decoder. A realizable input-space attack that edits edges, features, or text removes at least half the correct predictions on three of the six models at peak. How much of this fragility an input-access attacker realizes tracks how directly the decoder reads the representation, and not the clean accuracy a task leaves; we measure this carrier gain structurally from the decoder's local Lipschitz sensitivity, and report clean-accuracy headroom as a within-model ordering heuristic that does not survive on realizable attacks.

---


### 46. [Stochastic Meta-Unlearning: Bridging Language Backbone and Multimodal Unlearning](https://arxiv.org/abs/2607.18615)

**<font color=#1a73e8>作者：</font>** Zijie Liu, Jinhao Duan, Gaowen Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine unlearning for vision-language models (VLMs) remains underexplored. Unlike language models, VLMs combine a language backbone with visual components, which makes unlearning more complex. There is a surprising phenomenon when moving from single-modality unlearning to VLM unlearning: a target forgotten by the standalone language backbone can still be recovered when image information is given to the full VLM. This shows that text-only feedback is not enough for reliable VLM unlearning. Motivated by this observation, we propose Stochastic Meta-Unlearning (SMU), a bilevel framework that uses VLM-level feedback to learn an unlearning-ready initialization. In the inner loop, SMU applies a few unlearning steps to the language backbone using text data. In the outer loop, SMU recomposes the updated backbone with the frozen VLM and evaluates forgetting and utility at the VLM level. This design makes the unlearning update aware of the final multimodal behavior, while still keeping the update local to the language backbone. Experiments on two VLMs, two multimodal meme datasets, and three baselines show that SMU achieves the best overall forget-retain trade-off. Compared with the strongest baseline for each metric, SMU reduces average Forget accuracy by 10.52 points and improves average Retain and Test accuracy by 20.10 and 17.01 points, respectively. More importantly, SMU also transfers to new forgetting targets and to different meta-test unlearning methods. These results suggest that VLM-level feedback can make language-backbone unlearning more reliable and more transferable for VLMs.

---


### 47. [Mark, Don't Erase: Token Inoculation for Dual-Use Knowledge in LLMs](https://arxiv.org/abs/2607.18639)

**<font color=#1a73e8>作者：</font>** Seunghyun Lee, Dongyoon Han, Sangdoo Yun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety interventions on dual-use knowledge typically choose between destroying hazardous content (e.g., unlearning, filtering) and suppressing it at the output layer (e.g., refusal training); both pay a tax in adjacent-domain competence or over-refusal. We argue that the right operation is conditioning, not reduction: we show that hazardous knowledge can be retained in the model and behaviorally gated by a privileged control token. Our method, Token Inoculation, introduces a binding-and-branching approach. First, during continued pre-training, we mark hazardous content by inserting a special token alongside dual-use documents, so the model binds the marker to the underlying semantics of the hazardous domain. Second, during supervised fine-tuning, we teach the model to answer hazardous queries correctly when the special token is present and to refuse them when it is absent, thereby enabling selective refusal without removing dual-use knowledge. On hazardous domain (e.g., WMDP-Bio), Token Inoculation reduces accuracy from 79% to 18% while retaining 93% of the base-model's benign-domain performance (e.g., MMLU), achieving the best safety-utility trade-off against unlearning and refusal-tuning baselines across 1B-14B model scales. We further show that refusal selectivity is controllable through the quality of the conditioning signal and that domain-specific semantic binding during pre-training is critical for the conditional behavior to generalize beyond memorized triggers. Our results suggest that safety alignment is better cast as a conditioning problem than a forgetting one: behavioral control is more precise when sensitive knowledge is retained under controlled access than when it is destroyed.

---


### 48. [MissingBench-Verified: Probing Vision-Language Models' Inability to Detect Missing Object Parts](https://arxiv.org/abs/2607.18673)

**<font color=#1a73e8>作者：</font>** Wenqi Marshall Guo, Qingyun Qian, Shiyu Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) are well known for hallucinating non-existent objects in images. Objects with missing parts present a unique challenge for VLMs, stemming from both real-world knowledge bias and the scarcity of such images in training data. We present MissingBench-Verified, a benchmark designed to evaluate a specific and practically relevant scenario: when vision-language models fail to recognize that an essential component of an object has been removed. Across ten leading models, we observe consistent and significant failure rates that persist even when external tool evidence explicitly contradicts the model's visual perception. We further ask whether granting models access to image processing tools (e.g., cropping, contrast adjustment) enables autonomous inspection to resolve these failures. We find that existing mitigation strategies, including tool-assisted verification, autonomous visual reasoning, longer reasoning durations, and fine-tuning on an easier dataset, provide negligible improvement, indicating that this failure mode cannot be addressed through current prompting or post-hoc correction techniques. Our findings highlight a fundamental limitation of current VLM for inspection and monitoring tasks and underscore the need for architectural or training-level interventions that enable models to override internal expectations when confronted with contradictory evidence.

---


### 49. [Semantic Primes as Explanans for Emotion in Large Language Models](https://arxiv.org/abs/2607.18691)

**<font color=#1a73e8>作者：</font>** Frank Xing  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Progresses have been made on understanding emotion mechanisms of large language models (LLMs). However, how to explain emotion in LLMs, or even what constitutes good explanations, are less clear. Emotion representations, components, circuits are widely recoverable, but as explanations of a model's own computation they are circular; the emotion space dimensions tend to be arbitrary and non-terminating. A pressing question to ask is whether a more primitive set of internal variables does the work: the semantic primes of the Natural Semantic Metalanguage (NSM). Across four instruction-tuned LLMs (Llama-1B, Gemma-2B, Gemma-9B, OLMo-7B), experiments show that the NSM primes are (1) recoverable internal elements; and (2) on the reference model, intervening with a prime based direction controls emotion about three times as strongly, and twice as selectively, as the best appraisal based direction; and (3) the model treats a prime based explication as interchangeable with the corresponding emotion. These evidences suggest that NSM primes seem to be better explanans for emotion in LLMs than many alternative options according to scientific explanations criteria.

---


### 50. [Attributes Should Come from Images, Not Class Names: Distribution-Conditioned Attribute Selection for Vision-Language Models](https://arxiv.org/abs/2607.18695)

**<font color=#1a73e8>作者：</font>** Gautam Rajendrakumar Gare, Jia Shi, Zhiqiu Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A popular route to interpretable zero-shot classification asks a large language model (LLM) to describe each class name and prompts CLIP with the resulting descriptors. We show that these descriptors carry little visual evidence of their own: removing the class name from the prompt collapses ImageNet accuracy from 59.5% to 15.5%. The diagnosis is that the descriptors are conditioned on the label rather than on the images, so they describe the concept in general and mislead exactly when the data shifts; an LLM insists that strawberries are red, but every strawberry in ImageNet-Sketch is a colorless line drawing. We therefore select attributes from the target image collection instead: we score a large attribute pool against the images in CLIP's joint embedding space and keep the top-scoring attributes per class. Selected this way, class-name-free attribute prompts reach 23.8% on ImageNet (against 15.5% for LLM descriptors), the gain holds on four shifted ImageNet variants, and reselecting from the LLM's own pool isolates the selection mechanism as the cause. With one image per class, the selected attributes outperform the prompt-tuning method CoOp by 3 points while fitting in under a minute instead of 14 hours, with no learned soft prompt to obscure the decision. Because the attribute set is chosen by the data, it doubles as a readable summary of a dataset, which we use to describe distribution shift in words.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-104](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
