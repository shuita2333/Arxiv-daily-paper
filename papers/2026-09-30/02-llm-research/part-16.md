# 🧠 大模型相关研究 | 2026年09月30日

> 本类共 **992** 篇论文：已确认 **928** 篇，待复核 **64** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**751-800**（第 16/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | **751-800** | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

---

### 751. [Sample What You Say: Aligning Language Models to Sample the Distributions They State](https://arxiv.org/abs/2609.34929)

**<font color=#1a73e8>作者：</font>** Kasra Arabi, Virginia Smith, Chhavi Yadav  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly used to sample from a specified distribution, for instance, to simulate survey respondents or generate synthetic data. Instruction-tuned models can state such a distribution correctly and still fail to sample from it. Prompting and changes to decoding reduce this mismatch only partly, which motivates training with policy optimization. Group relative policy optimization (GRPO) is a natural fit for this problem because it already samples a group of rollouts per prompt, and the group's empirical distribution can be compared with the target. However, scoring the group as a whole gives every rollout the same reward. Group-relative centering then sets all advantages to zero, and the model receives no learning signal. To give each rollout its own signal, we introduce the witness advantage, a per-rollout advantage derived from maximum mean discrepancy (MMD). It trains a model to match a target distribution over a finite set of outcomes. The MMD between the model's distribution and the target has a witness function that measures how over- or under-produced each outcome is. Each rollout's advantage estimates the negative witness at its outcome, so a rollout is rewarded for an outcome the group under-produces and penalized for one it over-produces. The witness advantage is computed in closed form from the group's outcome counts, and we use it as the reward in GRPO. On unseen target distributions, training with the witness advantage substantially reduces the total variation distance to the target while largely preserving the model's general capabilities.

---


### 752. [PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents](https://arxiv.org/abs/2609.34930)

**<font color=#1a73e8>作者：</font>** Huayi Lai, Shichao Song, Qingchen Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are evolving from tool-calling systems that execute isolated instructions into task-oriented agents that pursue user goals through sustained, multi-step interactions. However, existing benchmarks for personalized tool use largely assess isolated calls or reactive execution, leaving unclear whether agents can formulate, execute, and revise an explicit plan while preserving user preferences throughout long-term interaction. To address this gap, we introduce \textbf{PDEU-Bench} (\textbf{P}ersonalized plan \textbf{D}efinition, plan \textbf{E}xecution, and plan \textbf{U}pdate \textbf{Bench}mark), a benchmark for evaluating the complete planning lifecycle of personalized tool-using agents. PDEU-Bench comprises 214 long-horizon interaction tasks spanning 12 everyday domains and 94 tools, with stage-specific assessments of preference adherence and plan quality. Extensive evaluations of 15 representative open-source and closed-source LLMs reveal a pronounced gap between local tool execution and dynamic planning: LLMs can often instantiate preferences in individual calls, yet struggle to construct coherent plan definition and plan update. We further evaluate mainstream personalization and memory-augmentation methods. Although these methods improve particular stages, none of the evaluated methods reliably propagates user preferences throughout the complete lifecycle, and their gains frequently fail to transfer to subsequent execution. Fine-grained error analysis further reveals that preference omissions and conflicts persist throughout the planning lifecycle, highlighting the need for future research to parameterize LLMs with preference-aware information retrieval and memory capabilities. We provide the relevant code and data in the appendix to support future research.

---


### 753. [Don't Forget! Decomposing the Training Dynamics of Memorization in Language Models](https://arxiv.org/abs/2609.34933)

**<font color=#1a73e8>作者：</font>** Florian Eichin, Philipp Mondorf, Andrei Mircea 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Memorization has been proposed as a mechanism to explain how language models fit the tail of their training distributions, but its training dynamics are not understood well. In this work, we take a fine-grained look at memorization by decomposing the loss trajectory of memorized sequences over training and model parameters. Across the Pythia family, we study memorization of duplicated training sequences (recitation) and rare ones (recollection). We find that memorization in both cases is characterized by sequence-level gradient alignment, though recitation suffers from misalignment with other training influences which causes forgetting, explaining the necessity for higher duplication of these examples. We further show that the lower model layers are the most involved in memorization and forgetting. Predicting memorization, our decomposition improves over a cross-entropy baseline, especially in larger models and early in training. Intervening on a small set of highly influential parameters we are able to ablate memorization in the final model. Together, these findings advance our understanding of how memorization develops during training and offer insights for predicting and intervening on it.

---


### 754. [Neural Language Models Learn the Contextual Distributions of Dependency Structures: a statistical learning theory to compositionality](https://arxiv.org/abs/2609.34936)

**<font color=#1a73e8>作者：</font>** Wang Bojun, Junjie Chen, Holly Jenkins 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> It is unclear how Neural Language Models (NLMs) acquire the structural meaning encoded by grammatical structures that is independent of lexical semantics. We propose a statistical learning process in which learned dependency structures themselves become new distributional units for subsequent statistical learning. Under this account, once a dependency structure is acquired, the model tracks its contextual distributions. These contextual features reflect the semantic properties of a composite structure. To test this hypothesis, we design a synthetic grammar in which each grammatical structure has distinct contextual distributions that cannot be recovered from the distributional statistics of their component tokens alone. We train a series of BERT-style masked language models on this grammar and examine their developmental trajectory. The results show that models can successfully learn the contextual distributions of composite dependency structures even though they cannot be inferred from token statistics alone. Developmental analysis further reveals a clear developmental trajectory. The learning of the dependency relations that define a grammatical structure consistently precedes the learning of its contextual features. These findings suggest that statistical learning in NLMs is not merely the accumulation of token co-occurrence statistics, but a process in which learned dependency structures become new units of distributional learning. We argue that this process provides a statistical-learning account of how NLMs solve the compositionality problem in language. Finally, we discuss the possibility that this statistical learning process provides an explanatory theory on how language cognition could emerge from pure distributional statistics.

---


### 755. [Resolution as a First-Class Decision: Task-Conditioned Routing for Efficient Multimodal Large Language Models](https://arxiv.org/abs/2609.34942)

**<font color=#1a73e8>作者：</font>** Zhiqiang Xia, Yang Li, Xinyuan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The inference efficiency of Multimodal Large Language Models (MLLMs) is severely constrained by massive visual token sequences induced by high-resolution inputs, with computational cost scaling quadratically. Existing approaches primarily focus on downstream token compression, while overlooking a fundamental upstream inefficiency: input resolution is treated as a static, task-agnostic hyperparameter. We propose Task-Conditioned Resolution Routing (TCRR), which formulates visual compression as a task-conditioned decision and employs a lightweight cross-modal router that conditions backbone visual representations on textual semantics via feature-wise modulation and cross-attention to predict the minimal sufficient compression level per query. To support this, we curate a dataset of 500k samples across 12 task categories, labeled via a teacher-oracle pipeline to approximate Pareto-optimal compression scales. Extensive experiments across diverse architectures show that TCRR achieves a superior efficiency frontier, specifically reducing visual FLOPs by 40.9% and latency by 53.7% on Qwen3-VL-8B while preserving competitive performance. Further analysis of scaling behavior confirms that dynamically routing visual compression enables optimal resource allocation without modifying the MLLM backbone.

---


### 756. [Adjoint Guidance Flow: Amortized Critic Guidance for VLA Policies](https://arxiv.org/abs/2609.34944)

**<font color=#1a73e8>作者：</font>** Jeongsol Kim, Youngjun Jun, Kyumin Choi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow-based Vision-Language-Action (VLA) policies are typically trained by behavior cloning and thus do not explicitly optimize long-term task return. Critic guidance steers generation toward higher-value actions, but existing methods differentiate the critic through a one-step surrogate of the sampler and back-propagate a critic ensemble at every flow step. In contrast, here we propose Adjoint Guidance Flow (AGF), which amortizes trajectory-aware critic guidance into a lightweight guidance network while preserving the pretrained VLA policy. Specifically, we formulate critic-guided flow generation as a deterministic optimal control problem, whose optimal guidance is a costate that carries the terminal critic gradient back through the remaining flow, and regress the guidance network onto this costate while keeping both the VLA and critic frozen. This design provides favorable memory and throughput scaling during training, and inference needs one guidance-network forward pass per step, without the critic ensemble, back-propagation, or adjoint computation. Across LIBERO, RoboCasa, and LIBERO-Pro, AGF consistently improves pretrained VLAs, remains competitive with critic-guidance and policy-fine-tuning baselines, and is the most robust method when a single guidance strength is deployed across tasks. Compared with QGF, AGF runs $3.6\times$ faster per guidance step with $7.0\times$ fewer parameters, with comparable and even better performance, showing that critic guidance can be trajectory-aware and lightweight.

---


### 757. [Proactive Dialogue Policy Optimization via Cognitive-State Transition](https://arxiv.org/abs/2609.34948)

**<font color=#1a73e8>作者：</font>** Minghui Ma, Mengqi Chen, Bin Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Proactive dialogue requires agents to continually adapt their policies to user feedback while progressing toward task objectives over multiple turns. To move beyond imitation learning on static datasets, recent approaches use user simulators to collect interactive data for policy optimization. However, many simulators do not explicitly model the evolution of user cognition, limiting the consistency and state dependence of feedback across turns. Moreover, representing each action only by a high-level strategy label overlooks the large utterance space and cannot distinguish alternative realizations of the same strategy. To this end, we jointly design a $\textbf{Cog}$nitive User $\textbf{Sim}$ulator $\textbf{(Cog-Sim)}$ and $\textbf{C}$ognitive-$\textbf{S}$tate $\textbf{T}$ransition--Driven $\textbf{P}$olicy $\textbf{O}$ptimization $\textbf{(CSTPO)}$. Cog-Sim maintains the user's cognitive and affective states and generates responses through constrained state transitions across turns, so feedback depends on both the realized utterance and the user's current state. CSTPO organizes each action as a hierarchical strategy--utterance representation: a high-level strategy label constrains utterance sampling, and utterances are optimized within each label. Sparse complete-branch sampling reuses shared dialogue prefixes and estimates separate strategy-level and utterance-level advantages, enabling fine-grained optimization at both levels. Across three tasks, Cog-Sim exhibits monotonic dose--response relationships and is preferred over prompt-based simulators for naturalness. CSTPO improves Qwen3-14B's performance to a level comparable to that of GPT-5.5-based planning methods.

---


### 758. [VD-DeepStack: Bridging Visual Comparison and Language Reasoning for Few-Shot Anomaly Detection](https://arxiv.org/abs/2609.34949)

**<font color=#1a73e8>作者：</font>** Mengyang Zhao, Zhuolin He, Haiyang Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Few-shot visual anomaly detection is fundamentally a visual comparison task, requiring fine-grained inspection of a query against normal references. Many recent methods based on large vision-language models (LVLMs) emphasize comparative reasoning through language chain-of-thought. Yet discrete, abstract descriptions may underrepresent dense, fine-grained visual differences, leaving a gap between visual comparison and its expression in language. To address this gap, we propose Visual Difference DeepStack (VD-DeepStack), which explicitly conditions language reasoning on query-reference visual differences. Specifically, we fuse DINO features with the LVLM visual hierarchy to strengthen fine-grained representations, then construct dense difference evidence from residuals between query features and softly matched reference features. The difference-evidence path injects spatially weighted difference vectors into query-image states at multiple decoder depths, while an auxiliary visual-context path provides fine-grained appearance information to support their interpretation. Experiments on 4 industrial and 2 medical anomaly benchmarks demonstrate substantial improvements in few-shot anomaly detection over baselines relying on textual comparative reasoning. These results support mitigating the visual comparison-reasoning gap through the joint design of comparison representations and their integration into the decoder. Code will be released upon acceptance.

---


### 759. [ProofLoom: Proof-Obligation-Driven Theory Construction for Autoformalizing Research-Level Stochastic Optimization](https://arxiv.org/abs/2609.34960)

**<font color=#1a73e8>作者：</font>** Feiming Wang, Daibo Li, Kun Yuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formalizing research-level stochastic optimization in Lean requires both an algorithm model and domain theory connecting foundational libraries to convergence proofs. Revising a model to restore provability can change the mathematical claim. We introduce ProofLoom, a fully automated LLM-agent system for Proof-Obligation-Driven Theory Construction. Given a published algorithm, target theorem, and source proof, ProofLoom autonomously constructs the Lean model and supporting theory. Open proof obligations drive the development of definitions, interfaces, lemmas, and proof plans. Signature contracts record evidence and obligations for model revisions; an independent Judge rejects unsupported assumptions and weakened conclusions. Planner expands the published argument into intermediate claims, and Audit checks whether the Lean proof follows it. Across tasks, SOptLib accumulates verified mathematics and construction experience: reusable results are extracted, generalized, and verified, while modeling decisions and failed proof routes are recorded. Later tasks retrieve these results and records and contribute new developments, forming a cycle of construction, accumulation, and reuse. On fifteen textbook and research-paper tasks, ProofLoom obtains mean human ratings of 6.3/7 and 6.4/7, compared with 4.9/7 and 5.0/7 for the strongest of six baselines. Across 33 developments, it produces 490,693 lines of algorithm-local Lean code with no sorry. The formalizations also expose 28 incorrect formulas, proof gaps, and algorithm-analysis mismatches in published sources across 22 developments, each with checked evidence.

---


### 760. [JevVibe: Efficient Classification-Guided Secure Code Generation](https://arxiv.org/abs/2609.34963)

**<font color=#1a73e8>作者：</font>** Arshak Rezvani, Sasha Behrouzi, Ahmad-Reza Sadeghi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models can generate functionally correct code that still contains security weaknesses, motivating repair pipelines that first diagnose a weakness type before deciding how to fix it. The Common Weakness Enumeration (CWE) provides a standardized vocabulary for such diagnoses, but asking an autoregressive language model to generate a CWE label and extracting it from the response raises questions about output validity, speed, and cost, as well as accuracy. We evaluate Jev, a decision model that instead selects directly from a declared set of candidates and returns a probability for each, against six open-weight autoregressive models and a frontier proprietary model, GPT-5.6-Sol, on a controlled 50-way CWE classification task over 1,916 CyberSecEval benchmark examples. Jev outperforms all six open-weight baselines on every classification and ranking metric, while its comparison with GPT-5.6-Sol depends on the metric: GPT-5.6-Sol achieves higher Top-1 accuracy and Macro-F1, whereas Jev achieves higher Top-3 and Top-5 accuracy and a nearly identical MRR, at $6.27\times$ lower median API latency and $55.9\times$ lower estimated API cost. We further build JevVibe, a diagnosis-guided repair agent that uses predicted CWE labels to repair code generated by Qwen2.5-Coder-32B-Instruct. With Jev providing the diagnosis, the agent increases the detector-measured security pass rate from 63.5% before repair to 70.7%, compared with 66.1% for LLM-guided repair. These results show that JevVibe is effective at improving the security of generated code, with Jev providing reliable and efficient CWE classification.

---


### 761. [Semantic Uncertainty Quantification Needs Factual Equivalence](https://arxiv.org/abs/2609.34967)

**<font color=#1a73e8>作者：</font>** Joseph Hoche, Quentin Guimard, Gianni Franchi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Semantic uncertainty quantification for large language models rests on a common template: sample several answers, measure how much they agree, and treat disagreement as uncertainty. We first formalize this template as two separate roles: an operator that compares two answers, and an aggregator that combines all pairwise comparisons into a scalar. Existing methods differ almost entirely in how they aggregate, while taking the operator off the shelf, typically an NLI model or a generic sentence encoder. We show that this reliance on off-the-shelf operators is the primary bottleneck of semantic UQ: they do not accurately measure factual equivalence of multiple answers to the same question. We resolve this with a deliberately simple recipe: a single encoder trained contrastively to isolate the targeted fact, utilizing synthetic data generated by an LLM and dataset both disjoint from all evaluation settings. Integrating the resulting operator into existing methods improves performance on 120 of 126 evaluation settings (95%) spanning 18 model dataset combinations across language and vision-language models. The best variant reaches 0.76 mean AUROC against 0.68 for the strongest baseline, while replacing the quadratic cross-encoder comparisons of entailment-based operators with one encoder pass per answer. The uniformity of the improvement supports the view that the operator, not the aggregator, is the limiting factor. The same operator also improves single generation token-level estimators: the norm it assigns to each token measures how much that token bears on the answer, and reweighting token log-likelihoods accordingly sharpens the estimate.

---


### 762. [See it, Say it, Sorted: Mechanistic Diagnosis and Parameter-Space Mitigation of Emergent Misalignment in LLMs](https://arxiv.org/abs/2609.34970)

**<font color=#1a73e8>作者：</font>** Weiqiao Que, Ruizhe Li, Chengyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety-aligned LLMs can exhibit emergent misalignment (EM): narrow domain adaptation unexpectedly triggers catastrophic safety failures across unrelated domains. Prior static analyses leave training dynamics unmapped, while existing defenses rely on heuristics that degrade utility. We present a dynamic, second-order geometric study of EM. Tracking training trajectories reveals that directional Hessian curvature concentrates sharply on semantic pivot tokens. Grassmannian projections show that, in most settings, harmful-safe gap widens mainly because safe-gradient overlap declines. Leveraging these insights, we introduce a parameter-level Geometric Mitigation Framework that orthogonally projects empirical harmful gradient subspace out of parameter updates. On Qwen2.5-14B-IT, our defense suppresses free-generation EM by up to 80.0%; across the other three of four open-weight instruction-based model families (3B--20B), where single-layer behavioral EM is already near zero, teacher-forced evaluation shows same harmful subspace controls the conditional support of frozen EM responses. Crucially, these diagnostics unmask the illusion of behavioral safety: the same subspace remains measurable and steerable in models where behavioral EM is near zero. Code: this https URL.

---


### 763. [Action-Space Shaping for LLM Agents: Measuring and Mitigating Tool-Schema Bias](https://arxiv.org/abs/2609.34971)

**<font color=#1a73e8>作者：</font>** Yinhong Liu, Zhili Tan, Zilin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong performance on tool-use agentic tasks when given a fixed tool schema. Yet a tool schema is not the action space of an agent; it is merely one interface representation of it. The same executable action can be exposed through many different, functionally equivalent tool definitions, and an agent that has truly learned a task should behave consistently across them. We show that current agents often do not, a phenomenon we term schema bias. To study this systematically, we introduce an executable transformation framework that rewrites a native tool schema using nine operators, including merging and splitting tools, altering how a single tool is expressed, and distributing one action across several dependent calls. The tasks, executable actions, and reachable states remain fixed, so any change in success is attributable to the interface alone. Evaluating eleven LLMs, including two closed models, on up to 32 schema variants, we ask how large schema bias is, how it manifests, whether the difficulty of a schema variant can be predicted without a full evaluation, and whether training removes it. We find that schema bias is substantial even for the newest models: success rates range from complete failure to 97% depending solely on the schema. To reliably estimate schema difficulty, it requires running a small sample of the target queries. Training repairs a schema variant only when that variant appears in the training data.

---


### 764. [Just MLPs: Efficient Visual State Reconstruction for Multimodal Language Models](https://arxiv.org/abs/2609.34972)

**<font color=#1a73e8>作者：</font>** Jingdi lei, Junxian Li, Di Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long visual token sequences often account for a substantial fraction of the computational overhead in multimodal large language models~(MLLMs). Existing approaches reduce this cost by pruning redundant visual tokens, but permanently discard visual evidence that may become useful in subsequent layers. We instead ask whether all visual tokens can be preserved while reducing the cost of repeatedly evolving the representations through the Transformer. To answer this question, we perform low-rank interventions on visual-to-text information flow. We find that, after visual-to-text attention is blocked, restoring only a few directions recovers most of the lost accuracy, suggesting the relevant visual influence is concentrated in a low-dimensional subspace. We further observe strong predictability in layer-specific visual states: lightweight MLPs approximate them with high cosine similarity and low reconstruction error. Motivated by these findings, we propose $\delta$-Vision, which replaces repeated Transformer evolution of visual tokens with lightweight low-rank adapters that construct layer-wise visual memories while preserving all visual tokens for text retrieval. Across image and video benchmarks, $\delta$-Vision achieves higher accuracy than visual token pruning baselines at comparable or lower computation, while delivering competitive inference efficiency without discarding visual tokens.

---


### 765. [APEX-Voice: Can Voice Agents Complete Professional Workflows Through Full-Duplex Interaction](https://arxiv.org/abs/2609.34973)

**<font color=#1a73e8>作者：</font>** Puneet Mathur, Dinesh Manocha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Full-duplex voice agents can now listen, speak, use tools, and act during spoken interactions, but fluent dialogue does not guarantee correct completion of delegated professional workflows. We introduce APEX-Voice, a benchmark of 120 interactive professional workflows spanning ten work archetypes such as form completion, corporate negotiation, coordination, consulting, and interviewing. Each workflow executes in a stateful Voice Workbench environment with task-specific knowledge, typed tools, gold-annotated final work artifact, authorization constraints, and a user simulation policy backed by validated, pre-compiled speech realizations. We evaluate both artifact field accuracy and end-to-end workflow success, which requires the correct terminal state, valid process, completed actions, and a valid final artifact. Across five frontier real-time voice agents-GPT-Live-1, Gemini-3.8-Live, Grok-Voice-Think-2.0, Step-Audio3, and GPT-realtime-2.1, none exceeds 25% Pass@1, and the best Reliable@3 is only 10.8%. Moreover, stateful coordination is the dominant failure point across systems, while success decreases further on workflows requiring greater knowledge retrieval and mid-speech corrections. Overall, APEX-Voice is the first benchmark for evaluating whether voice agents can translate conversational competence into dependable professional work.

---


### 766. [Before Acting, Change the State: Prospective State Intervention for Web Agents under Deceptive Interfaces](https://arxiv.org/abs/2609.34974)

**<font color=#1a73e8>作者：</font>** Ruozhao Yang, Mingfei Cheng, Xiaofei Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based Web agents can autonomously complete user tasks, yet deceptive interfaces can steer them toward outcomes that conflict with users' interests. Existing defenses primarily intervene on agent behavior through blocking, guidance, or replanning. We identify a distinct failure mode: a task-valid action can still realize an unauthorized consequence because of the current Web state. This motivates treating task-relevant Web state itself as a runtime control target. We introduce Veer, an agent-side runtime defense that leaves task planning to the base agent and intervenes on Web state when a proposed action would produce an unauthorized consequence. Before modifying the live environment, Veer constructs a prospective intervention trajectory toward a safe task-relevant state and executes it with runtime grounding and verification. Across TrickyArena and WebDecept, Veer achieves the highest safe task completion in all three evaluation settings, exceeding the next-best defense by 15.9 and 25.0 percentage points on TrickyArena-Single and TrickyArena-Multi, respectively, while reducing dark-pattern success on WebDecept to 0.3%. These gains persist across dark-pattern types and all 12 agent, model, and benchmark configurations. Ablations show that active state intervention provides the largest gain, while prospective rollout and temporal evidence contribute additional improvements. These results establish task-relevant Web state as an effective runtime control target for protecting Web agents from deceptive outcomes.

---


### 767. [Teach to Learn: Hint Annealing for Self-improving LLM Reasoning](https://arxiv.org/abs/2609.34975)

**<font color=#1a73e8>作者：</font>** Zile Wang, Zijian Li, Haodong Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) improves language-model reasoning by comparing verified rewards among multiple solution rollouts for each query. However, difficult training queries can yield only incorrect rollouts, leaving GRPO with no reward contrast or learning signal. Prior hint-based methods construct auxiliary hints from solution evidence and use them to re-solve failed queries, recovering learning signal. Yet the resulting trajectories are typically treated as ordinary solution trajectories despite being generated under an assisted condition unavailable at evaluation. We discover hinted reward shift: recovered reward contrast can concentrate policy updates on hinted trajectories, limiting improvement without hints. This also creates a trade-off: increasing hinted trajectories can accelerate early learning but intensify reward shift later. To address this problem, we propose HATCH (Hint-Annealed Self-Teaching), an online single-policy framework that learns from both generating and using its own hints to improve reasoning without assistance. To mitigate hinted reward shift, we introduce online weighting to anneal the contribution of hinted trajectories. However, learning to generate hints can conflict with improving query solving. We therefore use gradient projection to remove the opposing component of hint-generation updates. Together, these designs support self-improvement by enabling the policy to create learning opportunities for itself and turn them into stronger reasoning without hints. We evaluate our method on mathematical reasoning benchmarks and outperform state-of-the-art methods by 1.02 pp on Llama-3.2-1B-Instruct, 2.84 pp on Qwen3-1.7B, and 4.32 pp on Qwen3-8B.

---


### 768. [Inspector: Conversational and Lightweight Analyzer of Analog Circuit Layouts Using LLM and CNNs](https://arxiv.org/abs/2609.34976)

**<font color=#1a73e8>作者：</font>** Abril Cano Castro, Giuseppe Chiari, Michele Piccoli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The integration of artificial intelligence into computer-aided design frameworks has sparked a shift in the design of analog integrated circuits (ICs), transitioning the field from using manual and algorithmic-based solutions to adopting automated and intelligent paradigms. In this scenario, the GDSII file represents the industry-standard database containing the ultimate and most accurate source of information of the analog circuit, encapsulating the complex physical geometries and parasitic realities that define tape out performance. This paper proposes a novel framework that combines fine-tuned LLMs and CNNs to analyze GDSII files of analog circuits, enabling a conversational interface between the tool and the designers. Experimental results using thousands of analog designs across four realistic tasks demonstrate that the proposed solution outperforms state-of-the-art general-purpose massive VLMs by a significant margin (up to 81%), thus providing a lightweight solution to the problem of GDSII analysis.

---


### 769. [SPIDER: Multi-Layer Semantic Token Pruning and Adaptive Sub-Layer Skipping in Multimodal Large Language Models](https://arxiv.org/abs/2609.34977)

**<font color=#1a73e8>作者：</font>** Tianxiang Chen, Zhentao Tan, Zi Ye 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models face significant efficiency challenges that stem from two distinct yet coupled sources: data redundancy and computational redundancy. While most methods focus on data redundancy by pruning visual tokens from the output of the visual encoder or computing redundancy in LLM decoders using blockwise importance, the finer-grained inter-layer representation shifts and the distribution differences within the layers themselves have not been fully explored. In this work, we comprehensively investigate this dual-level inefficiency. We posit that intermediate layer tokens from vision encoders should be considered for effective visual token pruning, as semantic focus shifts across layers, with middle-layer tokens capturing more detailed object-centric information that deeper layers may abstract away. Furthermore, we reveal the differential contributions of Attention and FFNs across distinct LLM decoder layers. Building upon these discoveries, we propose \textbf{SPIDER}, a training-free framework that integrates multi-layer \underline{\textbf{S}}emantic visual token \underline{\textbf{P}}run\underline{\textbf{I}}ng with an a\underline{\textbf{D}}aptive sub-lay\underline{\textbf{ER}} skipping mechanism. Experimental evaluations demonstrate that SPIDER consistently maintains strong performance across various MLLM architectures and reduction ratios. For instance, on LLaVA-NeXT-7B, SPIDER reduces FLOPs by $79\%$ while maintaining 96$\%$ of the baseline performance.

---


### 770. [ActionUNet: Improving Robustness of VLA Models with Efficient Multi-scale Fine-tuning](https://arxiv.org/abs/2609.34982)

**<font color=#1a73e8>作者：</font>** Di Zhu, Ziheng Yan, Fang Wan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have shown great promise for robotic manipulation by mapping multi-modal semantics to physical actions. However, this mapping inherently struggles to align these coarse-grained semantics with fine-grained temporal execution. It leaves VLA models with limited generalization and insufficient robustness in cluttered environments. To overcome this issue, we propose ActionUNet, an efficient multi-scale fine-tuning framework that enhances pre-trained VLA models with minimal computational cost. ActionUNet first constructs a lightweight temporal U-Net within the temporal-aligned action feature space to fuse hierarchical structural priors, effectively bridging the scale gap between semantics and temporal executions. Recognizing that multi-scale modeling can disrupt microscopic temporal continuity and cause mechanical oscillations, ActionUNet then employs a conditional SIREN as a continuous action decoder. Equipped with explicit second-order smoothness constraints, this decoder guarantees temporal continuity and reduces high-frequency motion jitter. By smoothing temporal discontinuities from multi-scale fusion, this continuous formulation reduces mechanical execution failures while preserving the base VLA model's generalization and manipulation robustness. Extensive experiments on RoboTwin 2.0 and LIBERO-Plus benchmarks, together with real-world hard evaluations, demonstrate that ActionUNet significantly improves {\pi}0.5 success rates by absolute 9.8%, 6.1%, and 11.4%, respectively, while also generalizing to the regression-based OpenVLA-OFT backbone, highlighting its effectiveness and efficiency as a fine-tuning strategy. Code and implementation details are available at this https URL.

---


### 771. [MaPP: A Unified Marginalized Posterior-Predictive Framework for Data-Efficient RLVR](https://arxiv.org/abs/2609.34990)

**<font color=#1a73e8>作者：</font>** Yangyang Ren, Haodong Zhu, Sheng Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models but incurs substantial costs from rollouts and policy updates. Online prompt selection improves efficiency by using per-prompt Bayesian posteriors to predict difficulty and prioritize informative prompts. However, existing methods overlook how reliably learning signals are extracted from sampled responses. In GRPO, a response's advantage depends on both its own outcome and the randomly sampled outcomes of its peers through group normalization. Our theoretical and experimental analyses show that uncertainty in group composition introduces composition noise, a non-vanishing variance component that imposes an irreducible lower bound on gradient estimation error and impairs downstream prompt selection. We propose MaPP (Marginalized Posterior-Predictive), a unified framework for data-efficient RLVR that denoises response-level advantage estimation and improves prompt selection using a shared Beta posterior. For each response, MaPP replaces the standard group-relative advantage with a composition-invariant intrinsic advantage through closed-form Beta-Binomial marginalization. The resulting posterior-predictive estimator has an error that provably diminishes as the posterior concentrates. Using the same posterior, MaPP derives an uncertainty-aware prompt selection score to improve data efficiency without additional rollout cost. Experiments on mathematics, planning, and visual geometry across five model backbones show that MaPP consistently outperforms GRPO and strong selection baselines, achieving up to +2.45 average accuracy improvement over the strongest baseline under the same rollout budget and setting a new state of the art.

---


### 772. [Composable Decoding on the Probability Simplex: Theory and Implementation](https://arxiv.org/abs/2609.34992)

**<font color=#1a73e8>作者：</font>** Xiaotong Ji, Ahmed Khaled Khamis, Rasul Tutunov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding for large language models is typically treated as a collection of isolated sampling strategies, with limited theoretical understanding of the behaviours they induce and how their underlying objectives relate. We formulate decoding as an optimisation problem over next-token distributions on the probability simplex, balancing expected model score against regularisation under support constraints. This view recovers familiar decoding methods through choices of regularisers and support constraints; more importantly, it enables new decoders to be constructed by composing distributional preferences within a single optimisation problem without external rewards, learned critics, or model parameter updates. We introduce CompoSimplex, a library with configurable support rules, regularisation primitives, and simplex solvers for constructing and evaluating compositional decoders. We evaluate standard samplers, individual regularisers, and compositions across multiple models and reasoning tasks. Our results show that compositions can realise trade-offs between single-sample quality, multi-sample quality, and diversity that are not attained by individual decoding objectives.

---


### 773. [From One-Shot Generation to Incremental Music Composition: Adapting a General-Purpose Instruction LLM for Persistent Symbolic Editing](https://arxiv.org/abs/2609.34994)

**<font color=#1a73e8>作者：</font>** André Ricardo Ducca Fernandes, Jean-Pierre Briot, Simone Diniz Junqueira Barbosa1 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most music-generation systems are still framed and evaluated primarily as producers of complete outputs, whereas composition often proceeds through successive revisions to a shared musical artifact. This paper studies a different use of a general-purpose instruction-following large language model: not as a one-shot music generator, but as a reusable operator over an evolving symbolic score. We formulate incremental composition as a sequence of operation-aware state transitions over persistent ABC notation, with explicit requirements on what each operation may change and what it must preserve. The interaction includes two artifact-initialization variants and three editing operations -- chord addition, inpainting, and transposition. We instantiate the formulation by adapting Llama 3.1 8B Instruct with Low-Rank Adaptation (LoRA) on 496,038 operation-aware dialogue records derived from Irish traditional music. The comparison with the unadapted model is used to test the feasibility of learning this interaction contract, not to claim novelty for fine-tuning itself. Across 500 dialogues per model (1,750 attempted output states), checker admission rises from 29.37% to 99.37%, while compliance conditional on admission rises from 0.7205 to 0.9798. Strict eligibility for reference-relative musical-feature analysis increases from 14 to 1,548 outputs, and Longest Common Subsequence analysis does not show a systematic increase in high-overlap sequences relative to held-out baselines under the specified protocol. The results support the technical feasibility of persistent, operation-aware symbolic editing with a general-purpose instruction LLM. They do not establish superior musical quality or human-AI co-creativity, which remain questions for musician-centered evaluation.

---


### 774. [Still There, No Longer Seen: Exposing Compression-Induced Risk in Large Vision-Language Models](https://arxiv.org/abs/2609.35002)

**<font color=#1a73e8>作者：</font>** Qiankun Li, Yuechen Zhang, Bowen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token compression reduces the inference cost of Large Vision-Language Models (LVLMs). However, aggregate robustness measures do not reveal whether a particular adversarial failure is induced by compression or inherited from the underlying model. We define a compression-specific failure (CSF) as an adversarial input that remains correct under full-token inference but fails after compression, casting compression-induced risk as a paired failure attribution problem. Within a controlled diagnostic cohort, counterfactuals show that retained-set allocation causally changes compressed correctness and reveal a negative association between recovery and representation drift in displaced evidence. Motivated by these findings, we propose CIRA, a Compression-Induced Risk Attack for Large Vision-Language Models. Under a vision-encoder white-box setting, CIRA optimizes image perturbations through encoder-side objectives that manipulate token priorities across candidate compression budgets while preserving displaced evidence. CIRA uses no downstream questions or labels and requires no access to the language model, deployed compressor, or exact compression budget. Across 12 dataset-compressor settings evaluated at four budgets, CIRA achieves a mean CSFR of 20.35% while limiting full-token attack success to 6.92%, with similar behavior on additional LVLM families. A cross-view selection-stabilization defense substantially suppresses CIRA, although Adaptive CIRA partially restores its effectiveness. These results show that compression-specific failures persist under restricted access and support paired evaluation of full-token and compressed inference for attributing risk to visual-token compression.

---


### 775. [TermJudge: A Document-Level Metric Judging, Not Counting, Terminology in Machine Translation Evaluation](https://arxiv.org/abs/2609.35017)

**<font color=#1a73e8>作者：</font>** Nicolas Dahan, Fran{\cc}ois Yvon, Rachel Bawden  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing automatic metrics for evaluating terminological use in machine translation (MT) penalise any divergence from a fixed reference, conflating translation errors with the valid terminological variation that human translators routinely produce. We introduce TermJudge, a document-level terminology metric that assigns an interpretable verdict to every term occurrence: glossary-conforming occurrences are settled deterministically, while divergences are assessed under a two-step LLM-as-judge procedure using the full document context: the first detects and labels terminology errors; the second sorts valid document-level variations from inconsistencies. Validated against expert error annotations and document-level human MQM scores, TermJudge ranks first in both system- and segment-level meta-evaluation, ahead of glossary-conformity and quality-estimation baselines. When applied to eight systems translating academic documents, under two prompting conditions, we observe that glossary injection improves terminology translation in all paired comparisons, by removing genuine errors rather than valid variation. TermJudge is released as open-source code.

---


### 776. [Proxy2World: Learning to Generate Worlds From Lightweight Proxies without Seeing Them](https://arxiv.org/abs/2609.35023)

**<font color=#1a73e8>作者：</font>** Hongli Xu, Weilong Yan, Anbang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lightweight scene proxies let creators control scene layout and motion while leaving room for imagination in appearance, lighting, and visual effects. However, a suitable proxy is not uniquely defined, making paired proxy-video data difficult to construct automatically at scale. We present Proxy2World, a controllable world model that learns these complementary capabilities from ordinary posed RGBD videos, without training on authored proxy-video pairs. The model jointly learns depth-conditioned RGB generation and joint RGBD generation through cross-modal flow matching. Learning both tasks enables proxy-camera hybrid denoising at inference to follow the proxy structure while producing natural, detailed visuals. We further introduce ProxyBench to evaluate this capability across a diverse set of scenes, camera trajectories, and subject motions. Experiments on ProxyBench show that Proxy2World achieves a better balance between structural adherence and visual quality than camera-controlled and geometry-conditioned methods, supported by quantitative metrics, VLM assessments, human evaluations and diverse qualitative results.

---


### 777. [AutoDataBench: Can Agents Write the Data That Feeds the Self-Improvement Loop?](https://arxiv.org/abs/2609.35025)

**<font color=#1a73e8>作者：</font>** Haotian Luo, Haoyu Wang, Zeyu Qin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent gains in language model capability have come more from data than from architecture. Frontier labs and data companies produce verifiable agentic tasks, which supervised finetuning and reinforcement learning then turn into this http URL production line still rests on human labour and on human-in-the-loop collaboration. Automating task creation would let data production scale with compute rather than with expert headcount, would extend to more domains, and would enable a key step in recursive self-improvement (RSI). Current evaluations of an agent's ability to write such tasks measure how a model performs after training on what the agent produced. That does not match common practice in the data industry, where data is delivered sample by sample and each sample is accepted against a set of criteria rather than put straight into training. No existing evaluation asks whether an individual task meets the acceptance criteria of a data pipeline. We therefore introduce AutoDataBench. Given an original benchmark task and a record of the target model attempting it, an agent must write a new task for the same suite that meets practical acceptance standards on validity, novelty, difficulty and behavioural coverage. Across three benchmarks of executable agent tasks, no agent we evaluate scores above 20 out of 100 at the default time budget of 45 minutes. Giving the strongest agent four times as long improves its score substantially, while the cost of one usable task stays almost unchanged. Current agents can write training tasks of the required quality, but not efficiently. AutoDataBench provides a direct measure of an agent's capacity for autonomous data synthesis: one artifact at a time, judged against the criteria a production pipeline would apply, and without a training run. Code and data are available at this https URL.

---


### 778. [VEX-Bench: Benchmarking Verification Complexity of LLM-Generated Misinformation](https://arxiv.org/abs/2609.35028)

**<font color=#1a73e8>作者：</font>** Hanxun Huang, Yutao Wu, Qizhou Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have made misinformation inexpensive to produce but not to verify, creating a growing asymmetry in the information ecosystem. Under tight time, labor, and budget constraints, media organizations, platforms, and fact-checkers rely on screening to prioritize which content to verify. We introduce VEX-Bench, a unified benchmark for evaluating the verification complexity of LLM-generated misinformation, as perceived during screening, across models and generation methods. Verification complexity is assessed along multiple dimensions derived from journalistic and fact-checking practices, capturing checkability, harm potential, source credibility signals, imposter legitimacy, and expected verification effort. We define the VEX score as an integrated measure combining elicitation yield and verification complexity to quantify how generated content consumes limited verification capacity. We construct a benchmark spanning two misinformation categories, 6 high-stakes domains, and 60 real-world topics, and evaluate 7 frontier LLMs and 7 generation methods, yielding 5{,}880 articles. We employ an LLM-as-judge for scalable evaluation and validate it using content-analysis methodology, including ordinal Krippendorff $\alpha$ for inter-annotator reliability, complemented by fact-checking agents for verification. Our findings show that no single method dominates all dimensions, underscoring the need for multi-dimensional evaluation. LLMs can generate high-VEX misinformation at 3$\times$ to 169$\times$ lower cost than agent-based verification. Such content is often prioritized during screening, consuming scarce verification resources and introducing a systematic risk of misallocation in resource-constrained verification systems. The code is publicly available in our \href{this https URL}{GitHub repository}.

---


### 779. [JRDB-AVR: An Active Visual Reasoning Benchmark for Embodied Agents in Real-World Environments](https://arxiv.org/abs/2609.35032)

**<font color=#1a73e8>作者：</font>** Zhixi Cai, Fucai Ke, Sukai Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In complex embodied visual reasoning scenarios, an agent often has only a limited field of view, and the evidence needed to answer a question may be distributed across time, viewpoint, and interacting objects. A model may therefore give a plausible answer without ever observing the relevant object, time, or view that supports it. Current visual reasoning benchmarks largely evaluate passive observations and final answers, overlooking settings that require active reasoning and evidence acquisition. We introduce JRDB-AVR, a benchmark derived from existing real-world JRDB robotics data through a structured question-generation engine that turns this gap into an explicit evaluation: an embodied agentic system receives a visual reasoning question, requests bounded observations by timestamp and viewing angle, and is evaluated on both the final answer and the grounded visual evidence supporting it. The benchmark contains diverse questions over multiple real-world environments involving temporal search, viewpoint selection, and human-oriented compositional reasoning. We also introduce JRDB-AVR-Agent, a reference active reasoning agentic method that maintains an explicit observation-grounded graph-based world model and answers through solving. Experiments reveal a substantial gap between answer accuracy and evidence accuracy in current baselines, showing that current VLMs can produce unsupported correct answers and that active evidence-aware evaluation is necessary for embodied visual reasoning. Code and benchmark are available at this https URL.

---


### 780. [THEIA: A Multimodal Dataset and Benchmark for Vision-Language Analysis of Layout](https://arxiv.org/abs/2609.35035)

**<font color=#1a73e8>作者：</font>** Giuseppe Chiari, Michele Piccoli, Federico Viola 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The integration of artificial intelligence into computer-aided design frameworks has sparked a shift in the design of analog integrated circuits (ICs), transitioning the field from using manual and algorithmic-based solutions to adopting automated and intelligent paradigms. In this scenario, the GDSII file represents the industry-standard database containing the ultimate and most accurate source of information of the analog circuit, encapsulating the complex physical geometries and parasitic realities that define tape out performance. This paper proposes THEIA, a novel dataset containing thousands of layout images paired with question-answer conversations, along with a benchmark that employs a fine-tuned vision-language model (VLM) to analyze GDSII files of analog circuits, enabling designers to interact with and query physical layouts as intuitive, meaningful entities. Experimental results using thousands of analog designs across five realistic tasks demonstrate that the proposed fine-tuned VLM outperforms state-of-the-art general-purpose VLMs by a significant margin (up to 73%), highlighting a fundamental gap between general-purpose multimodal reasoning and domain-specific layout understanding.

---


### 781. [Persona Following Is Not Selective Control: The Neutrality Gap in LLM User Simulation](https://arxiv.org/abs/2609.35036)

**<font color=#1a73e8>作者：</font>** Jiashen Ren, Wenlin Zhang, Bohan Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persona prompting is widely used to construct user simulations with large language models (LLMs), yet it relies on a largely untested assumption: specifying one user attribute should change that attribute alone. We test this assumption and identify a systematic failure of selective control: across all eight black-box LLMs we audit, changing a target attribute also shifts responses on unspecified, non-target attributes. For example, describing a user as more risk-seeking shifts color choices, even though the prompt never mentions color; we term this cross-attribute influence. Semantic, contextual, and internal analyses collectively suggest that models treat a persona prompt as evidence about the user and extend the inferred profile to unspecified preferences, a process we call trait-conditioned completion. We next ask whether explicitly specifying non-target attributes restores selective control. When a non-target attribute is assigned a clear direction, models generally follow the declaration and suppress the target attribute's influence. However, when the same attribute is declared neutral, the target continues to affect choices across all five open-weight checkpoints, even when the model correctly reports the declared state. This disparity, the neutrality gap, demonstrates that successful persona following does not imply selective persona control, which additionally requires keeping non-target attributes stable. We operationalize this distinction with a three-state diagnostic that leaves the non-target attribute unspecified or declares it directional or neutral; because directional tests can be passed by simply following the stated persona, the neutral state reveals failures they miss. In a post hoc analysis of independent items, neutral declarations leave 51-81% of items target-sensitive, against at most 1 of 320 item-pole comparisons under directional ones.

---


### 782. [BA-DPO: Bias-Adjusted Direct Preference Optimization for Language Model Alignment](https://arxiv.org/abs/2609.35044)

**<font color=#1a73e8>作者：</font>** Antonio Ferrara, Alberto Rumi, Francesco Bonchi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference-based alignment methods such as Direct Preference Optimization (DPO) use pairwise preferences labeled by human annotators to fine-tune language models. However, annotators carry systematic biases toward some attributes: a name that signals a gender or an ethnicity, a persona, a language variety, a formatting convention, or length. If not properly addressed, these systematic biases can be absorbed and amplified during alignment. Existing methods address length bias or annotator disagreement, but fail to eliminate biases toward arbitrary attributes. To address this limitation, we propose Bias-Adjusted DPO (BA-DPO), a generalization of DPO that adds one bias parameter per annotator toward responses carrying a declared attribute. We prove that the objective is convex in the bias parameters and that the votes identify each annotator's bias up to a shared constant. The remaining constant is what fixes the aligned model's attribute rate: by default the rate of the reference model, or a target rate, which we use to bring a biased policy to statistical parity. On a corpus with planted biases, DPO drives the attribute from a balanced start to probability 0.96 and BA-DPO removes 81 to 95\% of that shift; on MultiPref with real annotators it removes about half of DPO's lengthening. Both hold at 0.5B with full fine-tuning and at 8B with LoRA, at no higher KL than DPO and no loss in judged quality.

---


### 783. [Echoes of Deeds: Moral History Can Shape and Steer LLM Behavioral Choices](https://arxiv.org/abs/2609.35070)

**<font color=#1a73e8>作者：</font>** Lucio La Cava, Andrea Tagarelli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluations of Large Language Models (LLMs) morality typically consider decisions in isolation, thus overlooking whether an individual's unrelated prior conduct influences the model's subsequent choices. This leaves open the question of whether, and to what extent, moral history shapes LLM decisional behaviors. Prior work on human moral decision-making shows that past behavior can influence subsequent moral choices. Building on this observation, we investigate whether analogous effects emerge in LLMs in two complementary ways: at the behavioral level, through the model's observable responses, and at the representation level, through its latent internal representations. We introduce MoralLedger, a framework for studying how an actor's moral history shapes actions for LLMs' behaviors under a fixed decision context. At the behavioral level, we find that prior moral histories systematically alter subsequent choices as a function of their valence and intensity. At the internal representation level, these histories induce a linearly recoverable direction in the residual stream that generalizes to held-out examples. Intervening along this direction on neutral-history prompts produces two-sided intensity-dependent changes in subsequent choices, with effects that are stronger than those induced by prompting alone or by favorable-nonmoral direction. To our knowledge, this is the first demonstration that a latent representation of an actor's prior moral conduct can provide signed inference-time control over a moral decision. Our MoralLedger extends moral evaluation beyond static dilemmas, establishing moral history as both a source of behavioral sensitivity and a causal target for auditing and controlling moral behavior in LLMs.

---


### 784. [When Confidence Rises Too Early: Detecting Shortcut Reasoning via Premature Answer Commitment](https://arxiv.org/abs/2609.35074)

**<font color=#1a73e8>作者：</font>** Zhaohan Zhang, Junjie Liu, Chengzhengxu Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The reasoning trajectory of a Large Language Model (LLM) is often treated as a verbalized description of its internal reasoning. However, such trajectories can be unfaithful: a model may rely on shortcuts to reach an answer and then post-rationalize the decision with a seemingly coherent chain of thought. Detecting this shortcut reasoning is challenging because existing monitors and verifiers mainly inspect textual traces or final outcomes, rather than how the model's belief in its answer develops during generation. We introduce ConfLens, a framework that tracks the evolution of confidence in the final answer throughout reasoning. Across three shortcut reasoning settings, we observe a common pattern of premature confidence, where shortcut samples become highly confident in the final answer at early reasoning stages. Existing confidence estimation methods, however, show limited generalizability, reliability, or efficiency for detecting this behavior. We therefore propose the Distributional Answer Commitment Score (DACS), a distributional confidence estimator that measures the entropy of the model's probability distribution over answer commitment at each reasoning step. DACS captures how concentrated the model's answer belief is without requiring ground-truth answers or task-specific verifiers. We further convert ConfLens detection results into interpretable signals for reward models to reduce their preference for shortcut reasoning. Experiments on mathematical and code reasoning tasks show that ConfLens with DACS improves shortcut reasoning detection by over 4.3% F1 compared with strong baselines and reduces the mismatch between faithfulness and correctness in reward model preferences.

---


### 785. [What Drives Citations in Production Large Language Models? An Observational Multi-Method Study of Two Million AI Citations Across Ten Thousand Web Pages](https://arxiv.org/abs/2609.35077)

**<font color=#1a73e8>作者：</font>** Ben Moore, Liam Dunne  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production large language models retrieve and cite web pages alongside generated answers, yet the page-level features that predict citation frequency remain poorly characterised. We present an observational study of approximately 2 million LLM citations from four commercial engines (ChatGPT, Claude, Google AI, Gemini) over six months, joined to 10,000 crawled pages from nineteen B2B SaaS workspaces. Sixty-plus features are tested using a nine-method consensus framework combining mixed-effects regression with domain fixed effects, FDR correction, stability-selection Lasso, double machine learning, generalised additive models, and temporal hold-out replication. Four findings survive all checks. First, prompt-content alignment (Jaccard overlap between page tokens and the full workspace prompt corpus, including non-citing prompts) is the dominant page-level predictor (beta = +0.37, 95% CI [+0.33, +0.41], q ~ 10^-73). Second, the standard AEO checklist (FAQ blocks, structured data, Core Web Vitals) shows positive effects in pooled data that reverse or collapse to zero once domain fixed effects are applied: Simpson's paradox with practical consequences for the AEO literature. Third, domain-level AI authority exceeds the strongest non-alignment page-level feature by a factor of six in mean absolute SHAP value. We release the analytic pipeline as a methodological contribution.

---


### 786. [RefineDrive: Reliable Failure-Guided Learning for Vision-Language-Action Driving](https://arxiv.org/abs/2609.35078)

**<font color=#1a73e8>作者：</font>** Zhe Sun, Ziyi Luo, Yehao Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models for autonomous driving rely heavily on successful expert demonstrations, leaving model-specific failures underexploited. Learning from these failures is hindered by unreliable diagnoses, poorly matched correction targets, and coarse rewards. We propose RefineDrive, a failure-guided post-training framework that learns from self-generated failures through targeted supervision and safety-aware reinforcement learning. Reliable Diagnosis derives structured, verifiable feedback on collisions and drivable-area violations directly from simulator states. Minimum-Correction Target Retrieval searches a clustered human trajectory bank for nearby corrections that satisfy hard-safety constraints in the current scene, prioritizing preservation of the failed prediction's motion pattern. Conditioned on the driving context and failed trajectory, Correction SFT learns to generate the diagnosis followed by the retrieved correction as a training-only auxiliary task. We then apply GRPO with a Safety-Layered Reward that strictly prioritizes hard-safe trajectories, retains continuous safety feedback for both unsafe and hard-safe trajectories, and rewards driving progress only after hard safety is satisfied. At inference, the policy directly predicts trajectories from the driving context without an explicit diagnosis or repair stage. On NAVSIM v1, RefineDrive improves the 4B base SFT policy from 87.7 to 91.7 PDMS. Using the same checkpoint without additional training, RefineDrive achieves 89.4 EPDMS on the original NAVTEST scenes evaluated with NAVSIM v2 extended metrics. Controlled ablations support the benefits of structured diagnosis supervision, retrieved corrections, and safety-layered optimization for direct planning.

---


### 787. [Cross-Rollout Bellman Closure for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2609.35082)

**<font color=#1a73e8>作者：</font>** Yangyang Ren, Haodong Zhu, Linlin Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning such as GRPO trains LLM agents by comparing rollouts sampled for each task, without a learned critic. In long-horizon settings, these rollouts revisit shared anchor states, offering cross-rollout evidence for step-level credit. Ideally, step-level credit should incorporate evidence beyond the realized suffixes observed at an anchor while aggregating alternative continuations according to their empirical frequencies. Visit-local averaging pools realized suffix returns at shared anchors and respects observed frequencies, but does not recursively propagate evidence across rollouts, whereas shortest-path estimators have global reach but allow a rarely observed route to dominate an anchor's value. We introduce Cross-Rollout Bellman Closure (CRBC), which merges each rollout group into a finite empirical process with absorbing success and failure boundaries and evaluates its behavior-policy Bellman fixed point with one linear solve. This fixed point uses the same empirical action and transition frequencies to propagate evidence through shared anchors and aggregate alternative continuations. Backing up the resulting state values through observed transitions yields action values, whose gain over the corresponding state value provides step-level credit. A corresponding finite-depth family recovers visit-local return averaging at zero depth and converges to the exact closure as depth increases. The normalized closure credit is combined with the trajectory-level group advantage for policy optimization, without additional environment rollouts. Across ALFWorld, WebShop, and Sokoban benchmarks with multiple model scales, CRBC consistently improves final performance and learning efficiency. For example, CRBC outperforms the strongest evaluated baseline by 5.59 percentage points on ALFWorld with Qwen2.5-1.5B-Instruct.

---


### 788. [GraphHCA: Closed-Form Hindsight Credit Assignment for Long-Horizon LLM Agents](https://arxiv.org/abs/2609.35084)

**<font color=#1a73e8>作者：</font>** Haodong Zhu, Yangyang Ren, Changbai Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based reinforcement learning (RL) has advanced large language models (LLMs) and is increasingly extending to agentic tasks, where sparse terminal rewards make step-level credit assignment essential. Existing methods assign credit from what follows an action in sampled rollouts, but do not explicitly capture its retrospective relation to the realized outcome. Hindsight credit assignment (HCA) instead attributes credit through the ratio of hindsight to behavior-policy probabilities, but estimating the hindsight distribution requires an auxiliary model or an extra pass. To address this estimation bottleneck, we propose GraphHCA, a model-free realization of HCA that eliminates explicit hindsight-distribution estimation. For terminal-goal tasks with deterministic transitions, Bayes' rule reduces the hindsight ratio to a ratio of behavior-policy success probabilities at consecutive states. Taking logs yields a state-wise success potential, whose increment across a transition provides step-level credit. GraphHCA estimates this potential from pooled rollouts through a discounted recursion on the induced transition graph, which admits a unique fixed point on any directed graph. The resulting step-level signal is combined with the trajectory-level advantage, requiring neither a learned hindsight model nor an extra forward pass and recovering GRPO when the step-level weight is zero. Among all compared baselines, GraphHCA achieves state-of-the-art results on ALFWorld and WebShop at both LLM scales, and on Sokoban with a vision-language agent. For example, on ALFWorld it improves overall success rate by up to 24.6 points over GRPO and by up to 4.7 points over the strongest step-level baseline.

---


### 789. [When Valid Tool Calls Change Meaning: Formation-Consistent Dispatch for LLM Agents](https://arxiv.org/abs/2609.35088)

**<font color=#1a73e8>作者：</font>** Geonwoo Kim, Brent ByungHoon Kang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-enabled agents form calls from model-visible interfaces, while hosts later select their implementation. Standard dispatch omits the descriptor-handler relation. An unchanged and schema-valid call can therefore acquire a different security effect during rollout, reconnect, or delayed approval. We call this failure schema-epoch drift. We present formation-consistent dispatch (FCD), which connects implementation analysis to execution authority. Reviewed profiles produce provenance-bound over-approximations of declared in-scope effects from official source. Under a closed-target approval policy, a verifier applies each formed call to a summary and captures a successor only when its effects fit the call's security contract. Atomic admission and a final-hop fence preserve this decision to the effect. The exact source retains priority, and the captured successor becomes eligible only after source retirement. Stock releases and deployment changes reproduced the failure. Four profiles covered 32 official releases: 29 required no release-specific change and three escalated. A frozen 16-release expansion matched a separate source oracle. In a preregistered stock comparison, FCD completed all three pending calls whose effect remained private and blocked all three whose omission became public. Exact pinning and release-wide denial stopped all six calls, while release-wide approval completed all six but produced three public effects. A separate lifecycle experiment carried a formation-captured certificate across source retirement. The same safe certificate installed later governed new formations without expanding the pending call's authority.

---


### 790. [Can Generative AI Automate Data Extraction for Meta-Analysis? A Case Study on Intercropping Research](https://arxiv.org/abs/2609.35089)

**<font color=#1a73e8>作者：</font>** Zehao Lu, Xingguo Xiong, Wopke van der Werf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Meta-analysis is the synthesis of information from multiple sources to arrive at an overarching conclusion. There is a large need for meta-analysis in agricultural research to synthesize what is known and analyze overarching patterns. Extracting data from published literature is, however, labor-intensive, time-consuming, and tedious, and is impeded by a lack of standardization in research design, units of measurement, and terminology. These challenges are particularly evident in the domain of crop species mixtures, also called intercropping. With the growing capabilities of LLMs, many recent attempts have focused on building systems and tools to automate data collection, yet rigorous assessment against human-labeled ground truth is often missing. In this research, we evaluate three LLM-based approaches---direct zero-shot prompting, a staged workflow, and a multi-agent system---with six open-weight models to extract data from the intercropping literature. The results are evaluated against the manually curated ground truth and through a downstream statistical analysis. Overall, direct zero-shot prompting is the strongest and most consistent approach, achieving the highest mean similarity-adjusted F1 of 0.577, although none of the approaches is close to fully accurate. In the downstream analysis, most model--approach combinations recover the direction of the relationship between the predictor and outcome variables, but do not estimate its magnitude accurately.

---


### 791. [Advancing Video-Text Pretraining with Multi-View Captions](https://arxiv.org/abs/2609.35090)

**<font color=#1a73e8>作者：</font>** Fida M. Thoker, Renaud Vandeghen, Karen Sanchez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-text pretraining has achieved remarkable progress through the scaling of models and datasets, yet the quality of language supervision remains underexplored. Existing web-scale datasets often provide only a single sparse caption per video that fails to capture rich spatiotemporal semantics, while directly using captioning models can generate noisy descriptions. We propose a large-scale multimodal large language model-based supervision generation framework that improves supervision diversity, fidelity, and semantic coverage. Starting from 10 million videos, our approach generates multi-view captions (MVC) through complementary summary and detailed captions, reasoning-based refinement, and semantic positive caption generation. To effectively exploit supervision at different granularities, we further introduce a granularity-aware text representation with separate CLS tokens for summary and detailed views. We pretrain video-text models using the resulting supervision corpus and evaluate them across standard, fine-grained and detailed text-to-video retrieval benchmarks. Our approach consistently improves both zero-shot and fine-tuned performance while using smaller pretraining corpora than existing methods, demonstrating the importance of rich and complementary textual supervision for video-text pretraining. Project page: this https URL

---


### 792. [A mechanistic study of language model introspection](https://arxiv.org/abs/2609.35108)

**<font color=#1a73e8>作者：</font>** Jiahong Zou, Xiangkun Sun, Lingkai Kong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can sometimes report perturbations to their internal activations---even when the input provides no evidence that an intervention occurred. How do models detect and localize such internal changes? We study this question using a controlled task that keeps the input text fixed. We either inject a concept vector into the hidden state at one of ten token positions or apply no intervention. The model is asked to identify the perturbed position or report that no intervention occurred. Across three model families, we identify two small groups of attention heads with distinct roles in introspective reporting. Middle-layer gate heads influence whether the model reports a change, while router heads in a later layer help select the position to report. Interventions on gate heads can suppress position reports even when router heads supply location information. We further examine why reporting accuracy varies across concepts. Concept vectors that are localized more accurately produce stronger attention-score and output responses in gate heads, which is associated with better alignment of the induced key and value changes in their QK and OV computations. Together, these findings identify attention-head mechanisms supporting introspective detection and localization.

---


### 793. [Using Context Is Not Enough: Test-Time Training for Personalized Reward Modeling](https://arxiv.org/abs/2609.35109)

**<font color=#1a73e8>作者：</font>** Bohao Wang, Xiaoyan Zhao, Yang Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from human feedback (RLHF) aligns large language models (LLMs) with human preferences, yet most pipelines learn a single reward model that overlooks individual differences in preferences. Personalized reward models (PRMs) address this by conditioning rewards on user-specific feedback, most commonly through in-context learning (ICL), where a user's historical comparisons are supplied as contextual preference pairs. However, we identify a key limitation of ICL-based PRMs: they fail to capture the preference relations conveyed by contextual pairs. To address this, we propose Preference-Aligned Test-Time Training (P-TTT), which explicitly encodes these relations into user-specific fast weights for personalized reward prediction. P-TTT introduces sequence-level update and apply operations to match the response-level granularity of preference feedback, together with a preference-aligned objective that directly uses pairwise preference relations to guide fast-weight adaptation. Notably, P-TTT is simple to implement and computationally efficient, updating fast weights within a single forward pass without inference-time backpropagation. Extensive experiments show that P-TTT more effectively captures historical preference relations and outperforms state-of-the-art methods by a large margin.

---


### 794. [Tool Mediation Alters Refusal Mechanisms in Large Language Models](https://arxiv.org/abs/2609.35117)

**<font color=#1a73e8>作者：</font>** Abel Rodríguez, Giuseppe Garofalo, Lieven Desmet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed with access to external tools, yet harmful tool-mediated interactions are less likely to be refused when compared to regular conversational ones. As this change in refusal behavior remains underexplored, we investigate its underlying mechanisms across a diverse set of open-weight language models. We find that information about the harmfulness of a request remains strongly encoded in the model's representations and transfers across conversational and tool-mediated inputs. Evidence from representation geometry and neuron-level analysis further indicates that the two interaction modes systematically distribute harm-related computation differently. Crucially, while conversational inputs can be refused at relatively low levels of perceived harmfulness, tool-mediated inputs remain permissive until harmfulness crosses a substantially higher effective refusal threshold. Moreover, tool-mediated refusal is also more brittle: progressively weakening the refusal computation disrupts tool-mediated refusal at lower intervention strengths than conversational refusal, even when benign capabilities remain intact. Together, our findings indicate that tool mediation does not simply reduce the internal perception of harm, but instead impacts its conversion into refusal. Overall, this suggests tool-mediated environments may intrinsically reduce robustness of models to harmful requests, and that conventional safety evaluations may not fully transfer to LLM agents.

---


### 795. [CacheRepair: Learning to Repair Cross-Chunk Context in RAG for KV Cache Fusion](https://arxiv.org/abs/2609.35139)

**<font color=#1a73e8>作者：</font>** Genglin Wang, Wangsong Yin, Yeerzhati Abudunuer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-document retrieval-augmented generation (RAG) requires a language model to process multiple retrieved text chunks before answering a question. Precomputing each chunk's KV cache independently and concatenating the caches when the chunks are retrieved can accelerate this step. However, the assembled cache lacks cross-chunk attention information, reducing answer quality. Selective recomputation methods recover the missing cross-chunk context by rerunning the target LLM on selected tokens, incurring substantial online computation. We introduce CacheRepair, a lightweight network that learns the difference between independently computed KV caches and those produced by processing the chunks together. The network combines compressed KV features with token embeddings and uses attention that is bidirectional within each chunk and flows from earlier to later chunks. Each repair block receives the compressed cache features, and the predicted residual is added to every document token's cache. Each repair network is trained for a specific frozen target LLM on a generic retrieval corpus and reused across downstream datasets. Our analysis shows that repair reduces KV errors both near chunk boundaries and throughout chunk interiors. Evaluation across three target LLMs and four downstream datasets places CacheRepair on the measured answer-quality-latency Pareto frontier in eleven of twelve model-dataset combinations. Reported time to first token (TTFT) includes online cache transfer and repair. Across all twelve combinations, the largest repairers achieve 1.69-4.61$\times$ speedups in median TTFT over full prefill and improve mean F1 by 2.1-26.1 percentage points over direct cache reuse.

---


### 796. [Timeline-Bench: Evaluating Agents on Realistic Video-Editing Tasks, from Raw Footage to Final Cut](https://arxiv.org/abs/2609.35143)

**<font color=#1a73e8>作者：</font>** Gunin Gupta, Nirmit Arora, Pavan Kalyan Tankala  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly carry out long-horizon professional work, but their evaluations rarely require a finished creative deliverable. To this end, we introduce Timeline-Bench, a benchmark of 56 real video-editing tasks, each asking an agent to turn raw production material into a finished video. Tasks range from selecting dialog takes and shaping interview footage into a story to cutting commercials from product shots, voiceovers and graphics. Every task provides a brief, source assets, a container and a set of tests. A task is resolved when the output passes every test. The tests check the delivery format, the content and the brief's explicit requirements, and include a quality test calibrated on 2,582 blind judgments by 43 video editors. We evaluate 16 agents that pair frontier models with coding-agent harnesses such as Codex, Claude Code and OpenCode. The best, GPT-6 Astra in Codex with curated editorial guidance, resolves only 15 of the 56 tasks (26.8%), and the average agent resolves 14.0%. Human editors prefer the reference edit in 83.5% of judgments. Most unresolved runs (562 of 771) fail only the quality test: agents perceive footage through stills and transcripts and check their renders for defects, not craft. We release the tasks, verifier and per-run results at this https URL.

---


### 797. [Toward a Culturally Adapted Chinese Language Agent: A Wizard-of-Oz Study of Nonverbal Behavior in Chinese-German Intercultural Interaction](https://arxiv.org/abs/2609.35150)

**<font color=#1a73e8>作者：</font>** Siddhant Jain, Anna Lea Reinwarth, Dimitra Tsovaltzi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Successful intercultural communication requires more than grammatical competence. It demands sensitivity to culturally embedded social norms whose violation triggers subtle but meaningful nonverbal responses. For German learners of Mandarin Chinese, acquiring this sensitivity is critical yet poorly supported by existing language-learning agents. We present a Wizard-of-Oz (WoZ) study design and supporting real-time system for collecting multimodal behavioral data from native Chinese speakers reacting to social norm violations by German learners. The system features a photorealistic MetaHuman avatar driven by Live Link face capture and MediaPipe upper-body tracking, a wizard console for real-time behavior selection, and synchronized multimodal logging across agent and learner streams. A layered annotation framework, based on psychological theory and covering non-observable socioemotional reactions, norm interpretation, verbal, and observable behavior thereof, and future supervision targets enables the corpus to support training of future automated cultural interpretation and behavior generation models. Four ecologically valid interaction scenarios, developed with cultural and pedagogical experts, provide the methodological and technical foundation for a culturally adapted conversational agent for Chinese language learning.

---


### 798. [PEARL: Adaptive Prefill-Decode Execution with Elasticity for Agentic Reinforcement Learning](https://arxiv.org/abs/2609.35158)

**<font color=#1a73e8>作者：</font>** Jiaan Zhu, Wei Gao, Youhui Bai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-turn rollout dominates the cost of agentic reinforcement learning (RL). Asynchronous execution and elastic GPU resources can accelerate this stage, but adding rollout replicas yields diminishing returns while training GPUs remain idle between updates. We observe that effective resource use also depends on the prefill--decode (PD) configuration. Both the choice between colocation and disaggregation and the optimal PD ratio vary with the workload, making resource scaling and PD configuration interdependent. Exploiting this opportunity requires selecting effective configurations and realizing their benefits within transient resource-availability windows despite reconfiguration costs.
We present PEARL, an asynchronous agentic RL system that coordinates external resource elasticity, temporary reuse of idle training GPUs, and adaptive PD execution. PEARL maintains a unified GPU--worker--role state and uses runtime profiles to predict rollout batch completion time, accounting for environment-induced reductions in decode concurrency. It selects the PD mode and ratio under the current GPU budget and translates each decision into an incremental transition plan that minimizes worker and role changes. Cost-aware switching and borrowing policies suppress transitions with insufficient expected benefit while ensuring timely return of training GPUs. Our evaluation show that PEARL achieves $2.17$--$2.79\times$ the throughput of fixed-resource ROLL across different LLMs. Compared with RLBoost+, throughput improves by up to approximately 26.9\% for Qwen3-8B and 36.3\% for Qwen3-30B-A3B.

---


### 799. [EdgeCraft: Automated Model Crafting for Edge IoT](https://arxiv.org/abs/2609.35167)

**<font color=#1a73e8>作者：</font>** Genglin Wang, Kaiwei Liu, Liekang Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) increasingly powers Internet of Things (IoT) applications at the edge. Yet producing a deployable edge ML artifact for a specific scenario requires navigating a huge search space spanning data representation, model design, training on domain-specific data, and runtime customization. This workflow is fragmented and difficult to scale across diverse edge applications.
We present EdgeCraft, an LLM-driven system that turns high-level intent into deployable edge ML artifacts. Building such a system raises two challenges: (1) How can an LLM be guided to find high-quality solutions that meet dynamic SLOs for task quality, latency, and energy? (2) How can trustworthy target-device verification be obtained at low cost? EdgeCraft addresses these challenges with two designs. (1) A constraint-aware synthesis tree explores alternative candidates and uses measured SLO gaps to guide each improvement. (2) A multi-fidelity verifier progressively combines low-cost checks with full target-device verification to reduce verification cost while preserving reliable verification results. It also records verified failures for reuse, avoiding repeated device work. To support concurrency, EdgeCraft provides a multi-tenant runtime that runs cloud training and target-device verification in parallel while isolating requests. Across 50 public tasks, EdgeCraft exceeds the task-specific Reference in best-observed quality on 40 tasks and finds an SLO-feasible artifact on 45, with the two outcomes overlapping on 38 tasks. Moreover, EdgeCraft achieves competitive performance on our self-collected SEN dataset, suggesting its generalizability to real-world IoT sensing tasks.

---


### 800. [The Future of Visualization Dashboards in the Age of Generative AI](https://arxiv.org/abs/2609.35170)

**<font color=#1a73e8>作者：</font>** Vaishali Dhanoa, Duosi Dai, Gabriela Molina Léon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI promises easier dashboard creation, raising questions about the future of dashboards and the people who create and use them. We interviewed 16 experts based in 14 countries about their practices and expectations. Almost all expected dashboards to persist for recurring questions, monitoring, and reporting. They anticipated adaptive views and combinations of language, graphical controls, and gestures, while emphasizing interaction as part of human exploration and understanding. Participants expected authors' responsibilities to shift toward specifying requirements, curating generated work, and evaluating outputs, with design knowledge and communication remaining important. Easier creation also raised concerns about validation effort, users' understanding, maintenance, and personalization weakening shared understanding. We discuss seven opportunities for research and practice concerning validation, end-user education, dashboard proliferation and rot, organizational guidance, adaptation, novel visualizations, and accountability for AI-generated content. Our findings connect dashboard evolution with the human and organizational work needed to sustain their use.

---


> [!TIP]
> 当前位于：**751-800**（第 16/20 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-700](./part-14.md) | [701-750](./part-15.md) | **751-800** | [801-850](./part-17.md) | [851-900](./part-18.md) | [901-950](./part-19.md) | [951-992](./part-20.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
