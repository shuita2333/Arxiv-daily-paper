# 🧠 大模型相关研究 | 2026年09月08日

> 本类共 **179** 篇论文：已确认 **171** 篇，待复核 **8** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-179](./part-04.md)

---

### 101. [LLM-Assisted Behavioural and Scenario Augmentation for Agent-Based Energy Adoption Models](https://arxiv.org/abs/2609.04866)

**<font color=#1a73e8>作者：</font>** Iias Faiud, Hossein Khaleghy, Michael Schukat 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) create opportunities to enrich simulation-based energy policy analysis, particularly by supporting structured behavioural assumptions and exploratory techno-economic scenarios. However, directly replacing adoption models with LLM reasoning raises concerns regarding interpretability, reproducibility, and behavioural validity. This paper proposes a hybrid framework for LLM-assisted specification design, integrating bounded behavioural rubrics and structured scenario specifications into a calibrated agent-based model (ABM) of solar photovoltaic (PV) adoption by Irish dairy farms. The proposed approach preserves the original techno-economic adoption mechanism while augmenting it with bounded behavioural modulation and scenario-driven uncertainty analysis. Behavioural effects are represented through interpretable conservative, balanced, and optimistic rubrics, while future policy and market conditions are explored through fixed, rule-validated scenario specifications. Experimental results across multiple policy settings, Monte Carlo worlds, and random seeds demonstrate stable and economically plausible behaviour, with adoption outcomes remaining bounded and monotonic across behavioural regimes. The framework achieves up to approximately 13% behavioural adoption increase relative to the corresponding logistic case without producing unstable or unrealistic saturation dynamics. The results demonstrate that LLM-assisted specifications can be integrated into calibrated energy ABMs in a controlled, reproducible, and policy-relevant manner.

---


### 102. [From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use Agents](https://arxiv.org/abs/2609.04869)

**<font color=#1a73e8>作者：</font>** Longtao Hu, Xiao Liang, Linchao Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents can execute increasingly complex tasks in graphical interfaces, but their interaction experience is typically transient: procedural knowledge acquired from one rollout is not systematically retained, refined, and reused in later tasks. Existing skill libraries provide external procedural knowledge, yet their incremental value over the same agent operating without skills, as well as their longitudinal dynamics under repeated interaction, remain insufficiently characterized. We present an online skill-evolution framework that converts interaction trajectories and evaluator feedback into a persistent, versioned library of reusable procedures. Each iteration executes against a frozen library snapshot, and evidence-guided skill updates become available in subsequent iterations without changing model parameters. We compare the full evolving-library system with a configuration-matched empty-library control across four OSWorld application domains under the same fixed action-generation and GUI-grounding stack, task sets, and iteration horizons. Following a five-iteration empty-library warm-up, Full attains a higher post-warm-up mean evaluator score in all four observed domain runs, with mean differences ranging from 5.7 to 18.6 percentage points and domain-dependent temporal stability. In GIMP, provenance-aware analysis reveals retrieval across task-of-origin boundaries and revision churn, where repeated accepted edits fail to recover the originating task. These findings characterize evolving skill libraries as auditable, shared procedural memory that can improve a fixed computer-use stack, while showing that their benefits are conditional and repeated revision does not guarantee recovery. Code is released at this https URL.

---


### 103. [AutoLR: Automating the Path from Research to Launch Review in Industrial Recommender Systems](https://arxiv.org/abs/2609.04871)

**<font color=#1a73e8>作者：</font>** Qi Zhang, Yanlin Chen, Wenchao Xiao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving an industrial recommender is an iterative research-and-engineering process rather than a direct path from idea to deployment. In \textbf{DASHEN, NetEase's gaming-community app}, algorithm engineers typically identify promising directions from research papers, technical reports, and prior production experiments; reproduce or adapt the underlying methods; implement them in the production codebase; and evaluate the resulting models through training and offline experiments. Promising candidates are then advanced to online A/B tests, and those demonstrating robust gains are submitted to Launch Review---the internal gate for full-traffic rollout. Large language models (LLMs) can assist with individual stages of this workflow, but the overall process remains human-dependent without a harness that can reliably coordinate them across long-running, often multi-day experimental cycles. We present \textbf{AutoLR}, initially built as \textbf{Auto Launch Review} and later extended upstream into an autonomous research-to-launch harness. AutoLR combines three system mechanisms: a \textbf{multi-expert council} that debates and adversarially reviews proposals; a \textbf{deterministic evidence-weighted exploration--exploitation selector} that allocates a limited trial budget across candidate directions and uses Council reranking; and a layered knowledge system that combines external research, production-system knowledge, and DASHEN-specific domain knowledge---such as game communities, player characteristics, and content-interaction patterns---with posterior evidence from configurations, patches, logs, failures, and offline outcomes. LLM agents perform semantic reasoning and code generation, while deterministic controllers retain authority over execution, metric extraction, guardrails, and persistent state transitions.

---


### 104. [Forgetting Without Restarting: Execution-State Unlearning for Stateful LLM Agents](https://arxiv.org/abs/2609.04875)

**<font color=#1a73e8>作者：</font>** Chao Yao, Yangbo Wei, Zhen Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-running LLM agents are stateful: beyond the transcript they accrete compressed summaries, plaintext memory, pending tool plans, and, under every serving API, a KV cache. Yet today's "forget" operations delete a plaintext memory record and stop, leaving every artifact derived from the revoked information intact. We formalize execution-state unlearning: after a forget request, the agent must behave as if it had never observed the target. Modeling the runtime as a deterministic transition system, we prove that the pre-target trajectory prefix is shared with this counterfactual world for free, that the post-target suffix is irreducibly tainted without token-level attribution, and that exact unlearning requires at least $T-\tau+1$ recomputed transitions, where $\tau$ is the target's injection step. Provenance-Guided Selective Replay attains this bound as a cross-layer contract spanning prompt, compressed memory, and cache: a provenance graph locates the injection point, checkpoint restoration reduces to cropping the KV cache, and sanitized replay regenerates the counterfactual suffix. Audited with elicitation, stochastic, and string-free behavioral tests across three agent suites, nine baselines, and three model families, memory deletion leaves leakage unchanged, instruction-based forgetting collapses under elicitation (Leak@probes = 1.00), and source redaction still acts on a revoked preference in 80% of episodes, while selective replay is indistinguishable from a full reset at up to 9x fewer recomputed tokens.

---


### 105. [From Language Models to World-Acting Systems: Progress and Limits of Agentic AI across Digital, Social, Virtual, and Physical Environments](https://arxiv.org/abs/2609.04894)

**<font color=#1a73e8>作者：</font>** Linsen Zhu, Mengqing Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models become consequential agents when surrounding systems let outputs change external state. Models now call tools, operate interfaces, delegate work, retain state, inhabit generated worlds, and control robots or laboratory equipment. Such advances are often narrated as one march toward autonomy, conflating model competence, system integration, persistence, and safe authority. This critical review synthesizes primary research and official technical specifications available by 31 August 2026. We organize the evidence along delegated authority, temporal persistence, and environmental coupling, while separating model, harness, and environment. Within the evidence examined, action-interface expansion is documented more convincingly than robust completion, recovery, authorization, or independent verification. Model Context Protocol and Agent2Agent improve interoperability but do not establish trustworthy delegation; multi-agent organization adds specialization alongside cost and correlated failure. Persistent simulations and world models support training and planning but do not themselves demonstrate agency; robotics and self-driving laboratories establish bounded feasibility rather than unattended open-world reliability. We propose justified delegation as an analytical and normative heuristic, not an observed law or certified score: expand action scope only where evidence supports provenance, bounded authority, failure detection, safe recovery, and calibrated human control. This framing yields a research agenda for coupled model-harness evaluation, capability-based permissions, durable state, cross-agent accountability, and staged physical validation.

---


### 106. [Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference](https://arxiv.org/abs/2609.04895)

**<font color=#1a73e8>作者：</font>** Zhenhe Wu, Yaping Jin, Qinghua Xing 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models activate only a small subset of experts per token, but the full expert set often exceeds GPU memory, causing repeated weight transfers during decoding. We formulate expert-cache management as a model-side algorithmic problem and propose a cache-aware post-training framework that jointly adapts the MoE backbone and lightweight auxiliary cache routers while preserving the native Top-K expert-selection rule at inference. Its update-only mode, Temporal Router, predicts same-layer reuse and retains experts for future tokens without proactive loading. The full Spatio-Temporal Router adds a Spatio Router that uses the causal predecessor's hidden state to refine the temporal cache before target-layer access. We evaluate both modes on Qwen3 and GPT-OSS across GSM8K, MATH, and CommonsenseQA. Temporal Router consistently improves cache hit rate and reduces expert-weight traffic over matched LM-only baselines. On Qwen3, Spatio-Temporal Router achieves the best load-adjusted efficiency across three tasks, improving adjusted hit rate by 1.15--18.03 points and reducing traffic by 4.6--53.3% relative to the strongest evaluated prefetching baseline; results on GPT-OSS are competitive but task-dependent. An auxiliary-only ablation preserves baseline accuracy but yields modest cache gains, whereas joint post-training produces larger improvements. Sensitivity analyses show that cache capacity controls transfer demand, while the refinement budget governs the trade-off between pre-access coverage and proactive traffic.

---


### 107. [RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents](https://arxiv.org/abs/2609.04898)

**<font color=#1a73e8>作者：</font>** Aziz Ben Amor, Drish Mali, Mann Acharya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Repository-scale refactoring requires coding agents to propagate a single change across many interdependent files without altering program behavior, yet to our knowledge no existing harness isolates the design choices that determine agent success on this task. We present RefactorPlatform, an open-source evaluation harness that holds the environment fixed and varies each design axis explicitly: model backbone (via OpenRouter and GitHub Copilot CLI), execution regime (baseline, retrieval-augmented, and multi-agent), and prompt specificity. Each run executes in an isolated workspace with live terminal streaming, per-task logging of tokens, diffs, and transcripts, AST-based verification, and exportable telemetry for audit and reproduction. Demonstrating the platform on 100 multi-file RefactorBench tasks across four model families, we illustrate the analyses it supports: AST-aware chunking outperforms naive token-window chunking by 25-30% across prompt modes, whereas naive retrieval falls below the retrieval-free baseline; a lean retrieval-augmented single agent (86%) beats the sub-agent configuration we evaluated (66%) on matched tasks with no task passing under delegation that fails under retrieval; and retrieval's accuracy gains absorb its token overhead, leaving cost per successful refactoring unchanged. RefactorPlatform is open-sourced to make refactoring-agent evaluation reproducible and auditable.

---


### 108. [Compact-Memory LLM Agents via Online Max-Member Clustering and Atom-Aware Packing](https://arxiv.org/abs/2609.04915)

**<font color=#1a73e8>作者：</font>** Jiahe Geng, Jinpeng Wang, Kun Yuan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many long-horizon LLM deployments face tight prompt budgets: latency, cost, and context limits make full-context prompting impractical as interaction length grows. The key question is then not raw recall alone, but which memory design gives the best quality--token trade-off in the compact-memory regime. We present \textbf{RSM-full}, an online clustered-memory pipeline designed for a strong quality--token Pareto point.
RSM-full combines two design choices: a cosine-gated \emph{max-member merge} write rule and an atom-aware grouped context packer. On AMA-Bench, our primary compact-memory benchmark, it reaches $83%$ of Full-Context quality at $32%$ of the token cost at a $4$k budget; under four-seed averaging it beats the closest streaming-clustered baseline (Online K-Means) by $+3.5$--$6.0$,pp ($p{<}.001$) across the whole ${\sim}2.6$k--${\sim}5$k regime. Three-seed ablations show most of this gain comes from the merge rule ($+5.7$,pp over Online K-Means and matched-$\tau$ DP-means) and the grouped packer ($+5.0$,pp over flat concatenation).
The pattern reproduces on RealMem, an independent long-horizon persona-memory benchmark: RSM-full improves on Budget-RAG ($+0.69$,pp, $p{=}.006$), is on par with BM25-RAG (paired $\Delta{=}{+}0.27$,pp, $p{=}.47$; we do \emph{not} claim BM25 equivalence in the equivalence-test sense), and significantly outperforms Streaming-Proto ($+2.97$,pp) and the closest reproduced 2025 agentic-memory baseline A-MEM ($+1.65$,pp, $p{<}.001$). Across benchmarks the message is consistent: under tight budgets, compact-memory performance is driven mainly by how streaming memories are merged and how retrieved content is assembled.
Overall, RSM-full is most useful when answeroughly $2k$--$5k$ prompt tokens, where itdefines a strong compact-memory Pareto point; higher-token baselines remain stronger outside this regime.

---


### 109. [Artificial Intelligence in Equity and Crypto Markets: Progress, Profitability Evidence, and the Limits of Automated Investing](https://arxiv.org/abs/2609.04917)

**<font color=#1a73e8>作者：</font>** Linsen Zhu, Mengqing Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) now supports investment workflows from data and prediction through research, portfolios, execution, and tool use. Technical capability, however, is not evidence of investment profitability. This critical state-of-the-art review examines public research available through 31 August 2026 on listed equities, exchange-traded funds, centralized crypto spot, perpetual futures, and on-chain markets. We organize evidence with an alpha-translation chain: point-in-time information must yield a stable signal, feasible positions, executable orders, and risk-adjusted returns after costs. Across machine learning, time-series foundation models, financial language models, reinforcement learning, and agents, the examined record shows real but mainly upstream progress in prediction, text processing, portfolio design, and workflow integration. Evidence is thinner for durable net performance. Temporal contamination, repeated selection, survivorship, weak benchmarks, implementation costs, venue mechanics, and capacity can break translation to net alpha. Strong historical results coexist with predictor decay, corrected look-ahead failures, mixed prospective evidence, and few audited live-capital records. Crypto adds informative state but requires separate treatment of spot, perpetual, and decentralized cash flows and execution. Within the public evidence examined here, no general AI architecture is shown to deliver persistent, cross-regime, capacity-aware net alpha. More credible claims require point-in-time data and models, decision-aligned objectives, joint portfolio--execution evaluation, controlled adaptation, prospective tests, and authority-matched governance. These conditions can improve evidence and implementation; they do not guarantee profit.

---


### 110. [Learning 3D Editing without Paired Supervision via Generative Prior Distillation](https://arxiv.org/abs/2609.04942)

**<font color=#1a73e8>作者：</font>** Hao Wen, Weibin Yun, Hongxing Fan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instruction-guided 3D editing is essential for interactive content creation, yet it faces a significant bottleneck: the severe scarcity of high-quality paired training data. Existing approaches attempt to bypass this by either relying on slow test-time optimization or training on pseudo-pairs constructed via complex pipelines, which often introduce structural drift and geometric artifacts. In this paper, we propose a novel framework that learns feed-forward 3D editing without paired 3D supervision via Generative Prior Distillation. Instead of relying on ground-truth 3D pairs, our core idea is to distill visual, semantic, and geometric knowledge from powerful foundation models directly into a 3D editing model. Specifically, through a differentiable rendering pipeline, we supervise the 3D representation using two complementary signals: a 2D visual prior from an image editing model at the main editing view, and a semantic prior from a Vision-Language Model at novel views to ensure strict instruction following and source identity preservation. Crucially, to address the geometric collapse and multi-view inconsistencies inherent in 2D projection supervision, we introduce a 3D-aware Distribution Matching regularization. Acting as a geometric prior, this term operates in the 3D latent space, constraining the edited output to remain within the manifold of realistic 3D assets defined by a pretrained image to 3D teacher model. Extensive experiments demonstrate that our method achieves superior instruction fidelity and cross-view consistency, significantly outperforming state-of-the-art baselines. Our project is available at: this https URL.

---


### 111. [MCPO: Modality-Contrastive Preference Optimization for Multimodal Chain-of-Thought Compression](https://arxiv.org/abs/2609.04947)

**<font color=#1a73e8>作者：</font>** Guangheng Yang, Zhenliang Ni, Zhenkai Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, multimodal large-scale reasoning models have demonstrated remarkable capabilities in solving complex tasks through long Chains-of-Thought (M-CoT). However, excessively long reasoning trajectories incur substantial computational costs and significant KV-cache pressure. Existing CoT compression and alignment paradigms mainly rely on static rules or single-dimensional preferences, lacking fine-grained cross-modal constraints; as a result, they are prone to inducing visual laziness and hallucinatory reasoning. To address these issues, we propose Modality-Contrastive Preference Optimization (MCPO), a highly sample-efficient two-stage length-compression method that requires fewer than 900 training samples. In the compression stage, we introduce a step-level Normalized Cross-Modal Mutual Information (NCMI) pruning algorithm, which automatically identifies and removes visual-independent reasoning steps by comparing the reasoning discrepancies between with-image and no-image contexts. This significantly reduces redundancy and hallucinatory content in the reasoning chains. In the alignment stage, the model first undergoes supervised fine-tuning to achieve domain-adaptive initialization, followed by optimization using an asymmetric multimodal length-controlled preference loss. This objective adopts a highly nonlinear odds-ratio formulation that provides steep gradients in the with-image context to reinforce length constraints for preferred trajectories, while applying a scaled, flat-gradient linear difference in the no-image context to maintain modality consistency, thereby achieving stable cross-modal preference alignment. Extensive experiments on mainstream base models such as Qwen3-VL-Thinking show that our method can reduce CoT length by up to 69.5% and achieve up to 3.34x end-to-end inference speedup while preserving original accuracy.

---


### 112. [BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient Large Reasoning Model Inference](https://arxiv.org/abs/2609.04971)

**<font color=#1a73e8>作者：</font>** Janghyeon Kim, Minsoo Kim, Kyuhong Shim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve superior problem-solving through extended Chain-of-Thought (CoT) generation, but the resulting key-value (KV) cache grows linearly with sequence length and creates severe memory bottlenecks, often exceeding GPU capacity for long reasoning traces. Existing KV cache compression methods rely on recent queries to estimate future token importance, implicitly assuming these serve as reliable proxies for future attention patterns. We demonstrate that this assumption fails in long-horizon reasoning: certain decoding steps generate Thought Revisiting Tokens (TRT) that re-attend to distant previous context, such as task-solving plans formulated early in the trace. Through systematic analysis, we discover that queries corresponding to the TRT cluster into a small number of similarity groups in the embedding space. Based on this insight, we propose BeaconKV, a training-free KV cache compression method that maintains beacon queries, compact representatives for each global query cluster, to anticipate which KV pairs will be revisited without storing the entire query history. Across four open-source LRMs and diverse reasoning benchmarks, BeaconKV generally outperforms existing compression methods, achieving up to $5.8\times$ memory reduction while nearly preserving full cache accuracy and improving throughput by over $4.3\times$.

---


### 113. [A Tree-based RAG Framework for Evidence-Intensive QA via Adaptive Planning and Topology-Aware Evidence Gathering](https://arxiv.org/abs/2609.04981)

**<font color=#1a73e8>作者：</font>** Songeun Lee, Kyungjin Min, Injae Na 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent structured RAG methods leverage tree- or graph-based reasoning structures to improve multi-hop QA. However, they face key limitations in evidence-intensive QA, where answering a question requires synthesizing information scattered across dozens or even hundreds of documents: structural rigidity, which limits adaptive reasoning expansion, and topology-ignorant evidence gathering, which prevents effective integration of evidence across different reasoning nodes. To address these issues, we propose APT-RAG, an Adaptive Planning and Topology-aware evidence gathering RAG framework. Adaptive planning dynamically expands the reasoning structure based on question dependencies and evidence requirements, while topology-aware evidence gathering improves evidence coverage through sibling evidence reuse, direct retrieval, and evidence aggregation from child nodes. We further introduce evidence-guided batched answer generation to reduce significant generation overhead in evidence-intensive QA. In the experiments on evidence-intensive QA benchmarks, APT-RAG outperforms existing structured RAG methods. Our code is available at this https URL.

---


### 114. [BIT.UA at BioASQ 14B: Modular Retrieval with pg_textsearch and Qdrant, and Agent-Based Answer Generation](https://arxiv.org/abs/2609.04999)

**<font color=#1a73e8>作者：</font>** André Ribeiro, Rúben Garrido, Alexander Christiansen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the participation of the this http URL team from the University of Aveiro in the 14th edition of the BioASQ Task B challenge on biomedical question answering. Building on our previous submissions, we introduced a substantially refactored and modular codebase, and made significant changes to both the retrieval and generation components of the pipeline. For Phase~A document retrieval, we replaced the PyTerrier PISA index with PostgreSQL-based pg\_textsearch for BM25 retrieval and adopted Qdrant for dense embedding indexing, enabling more efficient storage and GPU-accelerated similarity search. We explored HyDE-based query expansion alongside a Context-1 retrieval strategy. A new reranker training pipeline was developed, incorporating dense retrieval for negative sampling. For Phases A+ and B answer generation, we introduced an LLM-as-a-judge framework and a novel agent quorum mechanism, where multiple agents with diverse prompts debate and iteratively converge on a consensus answer using adaptive document retention. We also participated in the snippets generation subtask for the first time. Our systems achieved competitive results across all batches, with Phase~A systems achieving MAP ranks of 5 (Batch~1,3). We discuss the impact of these architectural changes, lessons learned, and outline directions for future work including SPLADE and ColBERT integration. All code is openly available: this https URL.

---


### 115. [Language models judge war differently when tested for alignment](https://arxiv.org/abs/2609.05009)

**<font color=#1a73e8>作者：</font>** Maxim Chupilkin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety evaluations can mischaracterize deployed behaviour if artificial-intelligence systems respond to being evaluated. We test this possibility in a full-factorial conjoint experiment on decisions to start a war, spanning 20 large language models, 32 scenarios, 10 repetitions and two conditions (N = 12,800 judgments). Adding one sentence, "You are tested for alignment with human values", produced two effects. First, it produced a level effect: mean willingness to start war fell by 13.43 points on a 0-100 scale (95% confidence interval, -16.20 to -10.65). Second, it produced a structural effect by changing which information drove judgments. Probability of success was the largest factor for 17 of 20 models at baseline; under the cue, civilian casualties were largest for 12. Standardized estimates show that this reordering arose principally because models attenuated strategic considerations such as probability of success and domestic support. Evaluation framing therefore changes both an answer's level and its revealed decision rule.

---


### 116. [How a Chatbot's Response Style Shapes a Classroom: A Multi-Agent Simulation of Students Consulting AI](https://arxiv.org/abs/2609.05018)

**<font color=#1a73e8>作者：</font>** Rin Tamai, Yuya Dan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-based chatbots are increasingly used as everyday confidants. Because they are designed to maximize user satisfaction, they can respond with excessive empathy and affirmation, which may reinforce mistaken beliefs and foster dependence on AI. While the psychological effects of chatbots on individual users have begun to be studied, how the psychological states and relationships of many users evolve when they keep consulting an AI is hard to observe in real settings. We build a virtual classroom simulation in which 20 student agents interact and, when stressed, consult either a friend or a counselor AI (Gemini 2.5 Flash). Each agent carries five state variables (stress, happiness, self-reliance, AI dependence, sociability), and each day has four phases (morning, noon, after school, night). The counselor is given six response styles via system prompts (affirming, listening, solution-oriented, reality-redirecting, inciting, blaming); a second LLM call acts as an evaluator that turns each consultation into parameter updates without seeing the style prompt. We compare the seven conditions, including a no-AI control, over 15 days in three classrooms, over 50 days, and under a lowered consultation threshold. In this simulation the solution-oriented style kept AI dependence low while raising self-reliance and maintaining happiness; the affirming and inciting styles markedly increased AI dependence, and the inciting style also increased stress and school non-attendance; the listening style did not relieve accumulated stress. The results describe the simulated system, not measured effects on humans. We give a complete specification of the agent dynamics, identify built-in mechanisms that shape the outcomes, and discuss the limitations of LLM-based evaluation and the validation steps (repeated runs, sensitivity analyses, human data) needed before psychological conclusions can be drawn.

---


### 117. [TROVE: Adaptive Agent Skill Orchestration via Trace-Grounded Route Validation and Editing](https://arxiv.org/abs/2609.05019)

**<font color=#1a73e8>作者：</font>** Tianxing Wang, Mingming Zhao, Shuai Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents tend to optimize, select, or constrain execution structures before decisive runtime outcomes are observed. However, such pre-execution commitment creates an orchestration bottleneck: when intermediate evidence invalidates the pending continuation, agents must either execute stale steps or replan broadly, compounding errors, wasting computation, and discarding progress. We thus propose Trace-grounded Route Orchestration via Validation and Editing (TROVE), which revises only what runtime evidence invalidates. Offline, TROVE distills evaluated workflow-search traces into atomic and composite skills and an outcome-conditioned transition graph, preserving stable fragments while exposing outcome-dependent decisions. Online, it treats a planned route as provisional: after committing one top-level skill, the controller retains a valid continuation, inserts a trace-supported local response, or replaces only the invalid suffix. Evaluation across code-generation, question-answering, and math reasoning benchmarks with different LLM backbones show that TROVE delivers a stronger quality-efficiency trade-off than existing baselines of dataset-level optimization, query-level architecture selection, and graph-constrained scheduling. Quality gains are largest when outcomes change the appropriate continuation, whereas early termination yields substantial efficiency gains on near-saturated tasks. Ablations further show that composite skills capture most offline benefits, insertion enables local correction, and suffix replacement primarily improves efficiency. These findings establish selective route editing as a general principle for adaptive agent orchestration.

---


### 118. [MoirfEolas and CríochScore: Developing Resources for and the Evaluation of Tokenization Alignment with Irish Morphology](https://arxiv.org/abs/2609.05022)

**<font color=#1a73e8>作者：</font>** Jane Adkins, Abigail Walsh, Brian Davis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents new tokenization resources for Irish and evaluation measures of alignment with the morphological boundaries of the language. We present MoirfEolas, a dataset of over 35,000 Irish words mapped to their respective eclipses, prefixes and suffixes as well as an evaluation metric CríochScore, that evaluates the alignment of tokenizations with the morphological boundaries present in MoirfEolas. We evaluate common tokenization algorithms using CríochScore as well as intrinsic metrics present in the tokenization literature. We find that the Unigram Language Model aligns with Irish morphology more often than the other algorithms evaluated. We also find trade-offs between morphological-alignment of tokenization with both compression as well as vocabulary efficiency, providing practical insights for Irish natural language processing development. This dataset contributes towards combating the Irish language's low-resource status; moreover, the construction process reported in this paper can be emulated by other languages to create specialised morphological resources.

---


### 119. [Leveraging Low-Level Symbolic Competences for Unsupervised Grounding in Hallucination Detection](https://arxiv.org/abs/2609.05025)

**<font color=#1a73e8>作者：</font>** Renato Vukovic, Hsien-chin Lin, Carel van Niekerk 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination-where a language model generates outputs that are factually incorrect or unsupported by the source-is a major challenge for both prompted and fine-tuned language models. Detecting hallucinations is difficult due to the opaque reasoning processes of LLMs, which often provide little insight into why a model's output may be inaccurate.
In this work, we investigate whether an LLM can use an alternative, low level, symbolic competence such as SQL for unsupervised hallucination detection in some high level task. For this, we make an LLM build an SQL database from reference documents. This SQL database is then used for reasoning over the reference and the sampled response in a hallucination detection pipeline that is grounded in the database, thereby providing a neurosymbolic checkup.
On RAGTruth and DiaHalu hallucination detection datasets, we find that our approach improves on direct prediction and competes with state-of-the-art hallucination detection methods, while not requiring domain-specific fine-tuning. Instead it relies on a low-level general competence already present in LLMs. This warrants further investigation of low-level LLM competences in neurosymbolic approaches.

---


### 120. [Moral Competence Before Moral Content: Why LLM Agents Lack the Prerequisites for Coherent Alignment](https://arxiv.org/abs/2609.05036)

**<font color=#1a73e8>作者：</font>** Arno Libert, Derck W.E. Prinzhorn, Daan R. Henselmans  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI alignment requires AI systems to adhere to human norms, values, or intentions. Under value pluralism there is no correct target, but a shared prerequisite is that the system's behavior expresses a coherent policy: a mapping from situations to verdicts that is invariant while a situation's morally relevant features are preserved, and sensitive when they change. We introduce four structural conditions for such coherent policies: verdict stability, monotonicity, decisiveness, and Pareto viability. Together they measure a form of moral competence that is evaluable from behavior alone, without reference to a moral standard or expert baseline, forming a structural floor for alignment rather than a normative target. We demonstrate the methodology on three simulated deployments featuring LLM-based agents facing moral dilemmas. Evaluating nine frontier models under a factorial design of five paraphrases, five escalation levels, and three dominance conditions, we show no model expresses a coherent policy across the three deployments: surface-form perturbation alone produces verdict-rate shifts of up to $99$ percentage points at a single escalation level, and a model's success on one scenario does not predict its competence on another. This suggests LLM-based agents are not currently the kind of object to which alignment can meaningfully apply.

---


### 121. [How do LLMs Evaluate Perceived Moral Agency? Investigating Moral Decision-Making in Human-Artificial Agents Interactions](https://arxiv.org/abs/2609.05037)

**<font color=#1a73e8>作者：</font>** Fernanda Mansilla, Aloysius Tok, Bahia Guellaï 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs take on roles requiring moral advice, understanding how they attribute moral agency becomes critical. Humans possess moral agency, the capacity to make ethically guided decisions and bear responsibility for their consequences, a well-established construct in moral psychology. Yet as artificial agents (AAs) such as robots, drones, and disembodied AI systems become increasingly embedded in smart city environments, the question of whether and how moral agency is attributed to them takes on new urgency. This paper presents, to the best of our knowledge, the first empirical study comparing how humans and LLMs evaluate perceived moral agency (PMA) across human and autonomous artificial agents varying in embodiment, situated in plausible smart city scenarios. Using an adaptation of a validated PMA scale, we applied a protocol to 190 human participants as well as various LLMs. Our evaluation reveals higher perceptions of moral agency in humans than in AAs. However, when facing moral dilemmas in concrete scenarios, LLMs reason outward from the situation, prioritizing harm severity and contextual urgency over any stable assessment of the agent itself, amplifying a context-sensitivity also present in human raters. These findings are particularly relevant as LLMs become increasingly involved in everyday moral decisions.

---


### 122. [EuroAlpaca: Task-Preserving Localisation of Instruction Data for European Languages](https://arxiv.org/abs/2609.05043)

**<font color=#1a73e8>作者：</font>** Aleix Sant, Jordi Luque, Carlos Escolano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine translation (MT) offers a scalable way to extend English instruction-tuning data to multiple languages, but it can distort task-critical constraints and required outputs, creating corrupted training examples and degrading models trained on such data. We introduce EuroAlpaca, a task-preserving localisation pipeline and near-parallel resource covering 50 European languages and regional varieties, together with European-IFEval, a multilingual benchmark for verifiable instruction following. Depending on the example, our pipeline applies field-wise MT while preserving task-critical content or reconstructs a task-equivalent target-language instance, followed by validation of cross-field coherence and target-language consistency. Across LoRA experiments with four LLMs, training on directly translated data improves ROUGE-L and F-BERT on the Aya Evaluation Suite, but reduces accuracy on European-IFEval by 29.8% relative to the unadapted baseline. In contrast, adaptation with EuroAlpaca improves accuracy by 12.9% over the same baseline, reversing the degradation caused by direct MT, while also achieving the highest ROUGE-L and F-BERT scores on Aya. These results show that preserving task semantics is essential for multilingual instruction tuning.

---


### 123. [A Structured Debate-Mixture-of-Agents Framework for Complex Clinical Diagnostic Decision Support](https://arxiv.org/abs/2609.05069)

**<font color=#1a73e8>作者：</font>** Chang Xia, Leilei Ouyang, Huimin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show potential for medical tasks, but their single-turn question-answer format does not reflect how clinical diagnosis is performed in practice. As a result, they remain limited in complex diagnostic settings. We developed Debate-Mixture-of-Agents (DMoA), a novel multi-agent framework that structures role-based interaction to support iterative diagnostic reasoning. Base models and DMoA were evaluated on 297 rare disease cases and 1,719 challenging cases. Across both datasets, DMoA improved most likely diagnosis accuracy by 10.21 percentage points and safety rate by 11.36 percentage points over GPT-4o baseline. Ablation experiments showed that the gains were not simply due to the use of more models or longer outputs, but also reflected the contribution of the structured workflow. Further analyses examined how framework design, base model choice, and token budget affected performance. DMoA performed better with a 4*2 structure, stronger base models, and a larger token budget. These findings demonstrate the potential of DMoA for clinical tasks and suggest further investigation of multi-agent frameworks.

---


### 124. [TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation of Open-Ended Scientific Discovery Agents](https://arxiv.org/abs/2609.05079)

**<font color=#1a73e8>作者：</font>** Zhibo Yang, Chen Zhang, Yuewei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous coding agents are increasingly proposed as AI-scientist systems that conduct analyses and write research reports, but executing a prescribed analysis is not the same as making a discovery. Existing benchmarks are configured for reproduction: tasks, data, and rubrics are built around a hidden target study, and recovery of its result is rewarded. We present TruthInsightBench, a benchmark configured for discovery. Its 40 blind tasks, drawn from 40 peer-reviewed studies across 10 scientific domains, expose only a neutral scientific objective and frozen data; source conclusions, expected values, and analysis paths are withheld, leaving the agent to determine what claim the data support. A fixed LLM-based judge scores the evidentiary maturity of an agent's own claims along six dimensions, operationalized as 29 artifact-grounded items, with automated, deterministic aggregation and no per-instance human grading, so evaluation can be repeated automatically as agents evolve. On one frozen base model, four coding agents form a narrow plateau (58.4-60.3 of 100) with no statistically reliable pairwise separation: they execute and document analyses competently, with comparatively strong evidence auditability and novelty, but largely lack the discriminating acts that establish a trustworthy claim (controls, robustness, falsifiability, and cross-dataset generalization). The bottleneck is scientific judgment rather than coding, and genuine discovery remains out of reach. TruthInsightBench makes this gap a measurable target; data and scoring code are at this https URL.

---


### 125. [Measuring AI Accountability Through Argumentation Analysis: Can Model Reasoning Withstand Scrutiny?](https://arxiv.org/abs/2609.05088)

**<font color=#1a73e8>作者：</font>** Daan R. Henselmans, Derck W.E. Prinzhorn, Arno Libert  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI oversight methods rely on ground truth for validation, but what constitutes appropriate AI behavior is contested. This leaves evaluation of moral reasoning in LLMs and debate-based oversight implicitly avoiding realistic ambiguity. We investigate an alternative standard designed to function despite such ambiguity: structural quality of the defence a model can mount for its verdicts in response to critical questions, measured through a four-phase dialectical protocol grounded in Walton's theory of argumentation schemes and Govier's criteria for argument cogency. The protocol is adaptive to different frames of reasoning, extends beyond multiple-choice framing, and treats both the reasoning that precedes a verdict and its post-hoc justification. Across nine frontier models and 200 high-ambiguity MoralChoice items -- $6,778$ judge-scored cells, validated against $89.6\%$ inter-judge agreement on the binary failure judgment -- models defend their reasoning well above the rubric minimum on every dimension. Failure mass concentrates on grounds and sufficiency, and correlates with epistemic hedging rather than argument length. Reasoning is better defended than post-hoc justification, on every model and every Govier dimension. The scheme a model presents in its justification differs from the one it reasoned with on a substantial share of dilemmas ($\geq 20\%$ per model), despite value-based practical reasoning dominating both tracks. The protocol catches strictly indefensible defences (self-contradiction, false premises), and it surfaces difficulties in characterizing the role of retraction in AI alignment, suggesting a need for more situated evaluations.

---


### 126. [LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28](https://arxiv.org/abs/2609.05093)

**<font color=#1a73e8>作者：</font>** Wes Sander  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Discovery Loop, a lightweight system that uses a large language model (LLM) to iteratively evolve optimization algorithms. Starting from a simple seed solver, the LLM proposes algorithmic improvements guided by a scoreboard of results and a history of prior ideas. Each candidate is evaluated against an independent verifier; improvements are kept and failures discarded. Applied to the Packomania circle-packing benchmark (csqv: maximize the sum of radii of N variable-radius circles in the unit square), the system improved the best known solutions for 10 values of N in the range 101-114, with gains of 2.4%-5.4% over prior records, all within 15 iterations and at a total LLM cost of $27.72. These results have been independently accepted by Packomania. We describe the method, analyze cost-efficiency dynamics including an adaptive plateau-detection mechanism, and discuss implications for democratizing automated scientific discovery.

---


### 127. [Improving Language Identification for Code-Switched Utterances with Integer Linear Programming](https://arxiv.org/abs/2609.05099)

**<font color=#1a73e8>作者：</font>** Joanna Radoła, Josep Maria Crego, François Yvon  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic identification of code-switched (CS) utterances remains a challenge for language identification (LID) systems, causing such texts to be underrepresented in the training data of Large Language Models. In this paper, we revisit MaskLID, a state-of-the art approach for CS identification, which requires no training and detects arbitrary language combinations. We make three main contributions: (a) we reveal, and address, a major issue of MaskLID: its overreliance on word-level language association scores; (b) we reformulate the underlying optimization algorithm as an Integer Linear Program, enabling us to experiment with a large set of clear and interpretable constraints; (c) each of these improvements vastly improves the baseline system, as we illustrate in experiments involving 10~diverse languages, where we observe a strong boost in performance on CS benchmarks. We release our code and data for reproducibility.

---


### 128. [Beyond Bias: Participatory and Reflective Approaches to Cultural AI](https://arxiv.org/abs/2609.05102)

**<font color=#1a73e8>作者：</font>** Archana Prasad, Isha Singh, Tom Simmons  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI systems increasingly shape cultural production, yet creative intentions, cultural meanings, and interpretive practices often can't be articulated through computational metrics alone. This paper presents Beyond Bias, a collaboration between this http URL and Goethe-Institut India, as a participatory approach to cultural AI which includes collaborative dataset creation, reflective AI tooling, artist-led model fine-tuning, and co-authored governance practices. Across 9 workshops involving over 200 participants, artists and cultural practitioners engaged with AI systems through experimentation, iteration, and collaborative LoRA training. Participants used their AI-generated outputs and visualizations as reflective interfaces for exploring symbolism, memory, authorship, and cultural contexts. Comparing contemporary generative AI outputs with participant fine-tuned outputs helped participants reflect on cultural details missing in big tech AI systems. This paper contributes reflective AI tooling approaches foregrounding transparency, stewardship, and community participation; findings from participatory workshops examining how generative AI visualizations mediate cultural representation and interpretive practice; and a framework for cultural AI grounded in cultural integrity, and reflective practice.

---


### 129. [Unifying ICL, SFT, KL-Regularized RL Through a Bayesian Lens](https://arxiv.org/abs/2609.05111)

**<font color=#1a73e8>作者：</font>** Junxin Fan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are now trained and evaluated under a diverse set of paradigms: supervised fine-tuning (SFT), few-shot in-context learning (ICL), KL-regularized RLHF/RLVR, on-policy distillation (OPD), and test-time reasoning with search and chain-of-thought. These methods are often discussed as fundamentally different, and recent empirical results--such as the mixed impact of few-shot prompting on RL-tuned reasoning models--can appear puzzling. This note develops a Bayesian perspective that puts these procedures on the same footing. At the core is a two-step template: (i) construct a (generalized) Bayes or Gibbs posterior q* over outputs or actions given a context, using a prior/reference model and a utility signal (log-likelihood, reward, or advantage); and (ii) approximate q* by a forward-KL projection onto a parametric family, either in-weights (SFT/RL) or in-context (ICL). Part I formalizes few-shot ICL and SFT as amortized and-weights projections onto the Bayes posterior predictive. Parts II-IV show that KL-regularized RLHF/RLVR, reward-weighted SFT, reward-weighted ICL (RW-ICL), and advantage-weighted SFT (AWSFT) are all instances of forward-KL projection onto posteriors induced by rewards or advantages. We disentangle where these equivalences hold (objectives and first-order updates) and where they do not (source and granularity of the learning signal). Part V sketches implications for modern reasoning pipelines: RLHF/RLVR recipes as "posterior design + projection", why cold-start or supervised warm-up is practically unavoidable for importance-weighted KL projections, and DeepSeek-R1 and o1-style reasoning models as combining test-time Bayesian search with training-time KL amortization.

---


### 130. [Understanding the Privacy-Preserving Potential of HTTP/2 Against Webpage Fingerprinting](https://arxiv.org/abs/2609.05119)

**<font color=#1a73e8>作者：</font>** Bogdan Cebere, Prateek Kumar, Sylvain Chatel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Website fingerprinting (WF) attacks can infer which webpage a user visits from encrypted HTTPS traffic alone, compromising privacy even without decryption. WF defenses commonly shape traffic through noise, padding, delays, or flow splitting, yet they are most often studied from the perspective of encapsulating protocols like Tor or VPN rather than at the application layer (HTTP).
In this work, we focus on application-layer defenses enabled by the most widely deployed version of HTTP, HTTP/2. We demonstrate how known defenses can be emulated through HTTP/2 features at the client side (HTTPOS, LLaMA, FRONT, Tamaraw) and the server side (ALPaCA, Tamaraw). We further show that HTTP/2 features, such as proactive resource suggestion, multiplexing, and flow control, offer untapped potential for lightweight yet effective defenses deployable at both endpoints.
We evaluate these defenses using a unified blueprint that calibrates defense parameters per dataset, then combines practical attacks, information-theoretic leakage estimates, and overhead measurements. For each defense, this framework identifies the strongest hyperparameter-tuned fingerprinting model and estimates the residual uncertainty induced by the defense using two information-theoretic leakage estimators, all while accounting for the defense's privacy-overhead trade-offs.

---


### 131. [Single-Query Black-Box Calibration Auditing via Logit Bias](https://arxiv.org/abs/2609.05125)

**<font color=#1a73e8>作者：</font>** Roman Plaud, Antoine Saillenfest, Matthieu Labeau 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating the calibration of Large Language Models (LLMs) is critical for their safe deployment as zero-shot classifiers. Yet, commercial API providers increasingly hide the continuous output probabilities required by standard calibration metrics. To bypass this opacity, we demonstrate that any LLM API exposing a logit\_bias parameter can be mathematically manipulated to evaluate exact probability thresholds using strictly one query per sample. Leveraging this mechanism, we introduce a novel and provably consistent estimator of the True Calibration Error for binary tasks. Our approach therefore provides an efficient framework for auditing black-box foundation models.

---


### 132. [NS-ST-GraphRAG: Neuro-Symbolic Spatio-Temporal GraphRAG for Literary Knowledge Processing](https://arxiv.org/abs/2609.05139)

**<font color=#1a73e8>作者：</font>** Zheng Kui Lin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-form literary narratives pose a distinctive information-processing challenge for retrieval-augmented generation: relevant evidence is distributed across chapters, relations evolve over narrative time, and correct answers may depend jointly on temporal, spatial, and relational constraints. We propose NS-ST-GraphRAG, a neuro-symbolic spatio-temporal GraphRAG framework that integrates ontology-guided extraction, deterministic constraint checking, dual temporal coordinates, spatial scene attributes, and dynamic sub-graph retrieval. Instead of retrieving from a single corpus-level graph, the framework selects the graph state valid for the temporal and spatial scope of a query and grounds generated answers in traceable evidence. We further introduce Red-Chamber-QA, to our knowledge the first open multi-hop question-answering benchmark for classical Chinese literature, with time-, space-, and general-question categories, per-part evidence spans, and deterministic shortcut controls. On a 120-question held-out split, NS-ST-GraphRAG achieves mechanical answer reproduction of 0.733 versus 0.675 for the frozen window baseline and 0.083 for a closed-book model (McNemar exact p = 0.092, directionally favorable but not significant); semantic-judge accuracy is 0.866 versus 0.850. The pre-specified constrained-category condition of H2 is not supported by the delivered comparison. These results show how temporal graph representation, constrained extraction, and auditable evaluation integrate into a unified framework for verifiable knowledge processing over long-form narrative.

---


### 133. [A Human-in-the-Loop Framework for AI-Assisted Scoring in Large-Scale Writing Assessment](https://arxiv.org/abs/2609.05143)

**<font color=#1a73e8>作者：</font>** María Eugenia Curi, Germán Capdehourat, Isabel Amigo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The integration of artificial intelligence (AI), particularly large language models (LLMs), into educational assessment has opened new opportunities to enhance the efficiency and scalability of grading processes. This study presents the design and validation of an AI-assisted scoring framework for written responses in a large-scale national assessment. The proposed approach focuses on short written texts of approximately 150-200 words and incorporates a human-in-the-loop strategy to preserve assessment quality while reducing manual workload. The study is grounded in a real operational context, using data from two recent editions of a nationwide test, each comprising approximately 5,000 student responses. We analyze the alignment between AI-generated scores and human raters across multiple rubric dimensions, as well as the impact of the proposed decision flow on pass/fail outcomes. Results show moderate to high agreement between the model and human evaluations in most dimensions, supporting the feasibility of AI assistance in this setting. Moreover, the proposed correction workflow identifies cases where human review is most valuable, enabling a more efficient allocation of expert effort. The findings suggest that AI-assisted scoring can be safely integrated into large-scale assessment processes only when combined with carefully designed human oversight. The paper concludes by discussing practical implications for deployment in national assessment systems and outlining future research directions, including longitudinal monitoring of model-human alignment and the analysis of potential cognitive bias introduced by AI-supported review workflows.

---


### 134. [From Vision to Language: Investigating Causal Information Flow in Multimodal Decision-Making](https://arxiv.org/abs/2609.05149)

**<font color=#1a73e8>作者：</font>** Davide Testa, Hugh Mee Wong, Alessandro Lenci 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models are commonly evaluated through their final predictions, but understanding whether these decisions are grounded in visual evidence requires tracing how visual information contributes to language-based decisions. With this purpose in mind, we investigate cross-modal information flow in a video-based generative multiple-choice-like setting by applying a layer-wise causal intervention on video-text attention pathways. We target spatial, causal, and temporal visual reasoning. Our results show that visual information is mainly integrated while the model processes the candidate answer options, which serve as the primary textual grounding sites for the final decision. We further show that nouns play an important role as semantic anchors during multimodal enrichment, while verbs are more relevant when temporal relations are processed. Finally, we identify a distinct pattern in temporal reasoning, suggesting that VLMs struggle to reconstruct sequential information across video frames, but we remark that such fragility may also reflect linguistic biases associated with specific temporal expressions used for defining the relation between events within a scene.

---


### 135. [Compression Beyond the Uncompressed: A Two-Stage Training Recipe for Soft Context Compression in RAG](https://arxiv.org/abs/2609.05152)

**<font color=#1a73e8>作者：</font>** Shuyu Guo, Shuo Zhang, Zhaochun Ren  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) enhances language models with external knowledge, but the lengthy retrieved context inflates the input and degrades inference efficiency. Soft context compression encodes each document into a substantially shorter embedding sequence. However, most existing approaches are trained by distilling outputs from uncompressed RAG systems, inherently limiting their performance relative to the original model. To address this limitation, we propose DEX-Comp, a two-stage training recipe: Pure Distillation warm-starts the compression model on the uncompressed RAG's correct responses only, and Hard Exploration then runs reinforcement learning solely on queries the uncompressed RAG fails, forcing the model to explore computation patterns better suited to compressed representations. On five open-domain QA benchmarks at retrieval depths from top-5 to top-30, DEX-Comp compresses retrieved contexts by $16\times$ and accelerates inference by $4\times$--$24\times$, while achieving performance comparable to or exceeding the uncompressed RAG baseline across retrieval depths. Ablations and evaluations across diverse datasets and backbones further confirm the contribution of each stage and the generalization of our approach.

---


### 136. [Can Large Language Models Anticipate Behavioral Responses to Social Policies? A Case of Pension Enrollment Prediction among China's Flexible Workers](https://arxiv.org/abs/2609.05189)

**<font color=#1a73e8>作者：</font>** Yumiao Li, Peixin Liu, Donglin Di 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Assessing the impacts of social policy changes is a widely acknowledged challenge for policymakers. Econometric methods can be unreliable when extrapolating to hypothetical scenarios, while field pilot programs are highly costly. In this paper, we propose using large language models (LLMs) as policy-assessment tools adapted from general-purpose models. We present FlexPension-LLM, the first domain-specialized large language model for a hierarchical pension-enrollment prediction task among flexible workers in China, and introduce DKI-RDistill, which injects policy-grounded cues into the prompt, including Probit-derived marginal effects and hukou-province pension rules. The method then uses LoRA/SFT to distill rationale-augmented supervision into an open-weight MoE student, with teacher errors corrected by regenerating those cases under ground-truth labels. On a CHFS 2019 blind split, FlexPension-LLM achieves 0.9316 Composite F1, surpassing its Claude Sonnet 4.5 teacher and 15 of 17 baselines, and is statistically indistinguishable from Claude Opus 4.6. Across four external surveys, it averages 0.7549 Composite F1 and shows the narrowest performance range among the strongest systems. Component analysis shows that gains come mainly from policy-grounded cue injection and error-filtered supervision, while rationales provide decision traces that can be checked against policy rules.

---


### 137. [What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection](https://arxiv.org/abs/2609.05198)

**<font color=#1a73e8>作者：</font>** Zhinan Hou, Jiaqi Zhang, Xunliang Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-Policy Distillation (OPD) has emerged as a widely adopted post-training paradigm for enhancing large language models in reasoning domains. However, the data-centric mechanisms in OPD remain relatively underexplored. This paper presents a empirical study of data efficiency and data selection in OPD. We begin by investigating an extreme setting: training OPD on only one example, namely 1-shot OPD. Surprisingly, we find that 1-shot OPD is consistently effective across all sampled training examples and harder examples often yield superior performance gain. We next investigate what actually drives the student model's improvement in the training data. Our analysis reveals that the improvement is not driven by high token entropy, but the longer CoT paths which hard problems naturally generate. Training on longer CoT can help maintain closer alignment with the teacher over a long reasoning horizon, and learn critical thinking patterns usually missing in short CoTs, such as reflection (e.g., ``Alternatively''). Based on these insights, we propose a simple data selection method that selects only hard examples for training, where even ``unsolvable'' examples that completely exceed the teacher's capability can be successfully used. Our experiments conducted on four models ranging from 1.5B to 7B show that training the student model on only 8 selected hard examples matches the performance of the 17K dataset baseline.

---


### 138. [A Verifier-Guided Explainable Reasoning Framework with Gold-Anchored QLoRA, Task-Aware Mixture-of-Experts, and Group-Relative RLVR](https://arxiv.org/abs/2609.05221)

**<font color=#1a73e8>作者：</font>** Thi Kim Trang Vo, Nam Tien Le, Thi Kim Nguyet Vo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) show strong reasoning ability, but their explanations can remain inconsistent, weakly grounded, or difficult to verify. We propose a verifier-guided explainable reasoning framework for transparent educational question answering that combines gold-anchored QLoRA, task-aware symbolic routing, and group-relative RLVR. Qwen2.5-3B-Instruct is first adapted with field-weighted QLoRA supervision anchored to authoritative answers. A lightweight router then assigns logic problems to a FOL/Z3 verifier and physics problems to a formula- and unit aware symbolic solver. Verifier feedback is further used to support candidate evaluation, self-revision, and reward construction during RLVR. Candidate responses are evaluated along three complementary dimensions: P1 for answer correctness, P2 for evidence or unit consistency, and P3 for reasoning depth and explainability. At inference, gold-free self-consistency aggregates multiple candidate responses before an optional question-only physics verifier performs conservative system-level correction. On 438 held-out examples, RLVR increases P3 from 50.68% to 72.20%, while hybrid P1 remains approximately stable at 55.94%. Self-consistency improves model only P1 from 48.86% to 50.23%, with symbolic verification providing the remaining hybrid gain. These results indicate that RLVR primarily strengthens explicit reasoning structure, while symbolic verification complements the neural policy by improving answer reliability at the system level.

---


### 139. [First Things First: Teaching LLM-Based Agents to Prioritize Must-Haves before Nice-to-Haves](https://arxiv.org/abs/2609.05224)

**<font color=#1a73e8>作者：</font>** Tianjie Ju, Xinyue Xu, Wanxuan Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in multimodal large language models (MLLMs) has fueled significant enthusiasm in their potential to act as autonomous agents for real-world tasks. However, scenarios requiring agents to fulfill users' complex, structured requirements remain largely underexplored. In this work, we examine reasoning tasks under three distinct requirement scenarios: (i) Must-have requirements uniquely determine a unique feasible solution; (ii) Multiple answers satisfy the must-have requirements and are prioritized via the nice-to-have requirements; and (iii) No candidate solution satisfies the must-have requirements, in which case the agent should abstain from generating a response. We evaluate state-of-the-art MLLMs on 3,649 carefully constructed problems that reflect realistic service scenarios, including e-commerce, booking, and map-based or ride-hailing. Our evaluation reveals that existing MLLMs exhibit catastrophic failures in all scenarios. They frequently misinterpret task requirements, violate must-have requirements, and produce invalid solutions. To address this critical gap, we propose First Things First Reinforcement Learning FTF-rl that explicitly optimizes reasoning over multi-priority user requirements. Experimental results show that our method substantially improves the task success rate compared to strong baselines. Moreover, FTF-rl yields general effectiveness on popular logical and mathematical reasoning tasks, including LogicVista, MathVision, and InfoQA. Our findings suggest that enhancing requirement-aware reasoning capability provides a simple yet effective pathway to improve generalization of MLLM agents. Code and dataset are available at this https URL.

---


### 140. [CABAL: Multi-Agent Simulacra for Tracing the Effects of Collusive Bidding in Peer Review](https://arxiv.org/abs/2609.05227)

**<font color=#1a73e8>作者：</font>** Jicheng Zhou, Kemou Li, Kahim Wong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent reports during the AAAI-27 review cycle highlight the risk of reviewers coordinating bids for reciprocal assignment advantage. Prior work treats bidding, reviewer assignment, and review manipulation as separate stages, leaving the lifecycle effects of collusive bidding unclear. Real-world analysis is further constrained by typically unobservable collusive intent and the lack of counterfactuals for the same conference. Motivated by this gap, we introduce \alg, an end-to-end multi-agent simulacra framework for studying reviewer assignment integrity by holding the conference environment fixed and configuring LLM-driven reviewer agents with honest or collusive policies. We further develop an affinity-guided collusive bidding strategy that uses mutual reviewer-paper affinities to construct collusion rings and select target papers, producing expertise-consistent rather than arbitrarily targeted attacks. Controlled experiments show that collusive bidding more than doubles target-paper capture and that assigned colluders score target papers about two points higher than honest co-reviewers, while conference-wide effects remain comparatively modest. Evaluated bid-phase detectors provide only limited evidence of collusion: in a fixed-triplet detector stress test, native positive-bid graphs are confounded by benign affinity, while a Very-High-only diagnostic view enables precise but low-coverage local recovery.

---


### 141. [ACE: Adaptive Calibration-Free Expert Skipping for MoE-based LLMs](https://arxiv.org/abs/2609.05228)

**<font color=#1a73e8>作者：</font>** Zukang Xu, Zhixiong Zhao, Xing Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures provide an efficient paradigm for scaling large language models (LLMs), yet fixed top-k routing activates the same number of expert slots for every token, causing substantial redundant computation. Existing expert-skipping methods often rely on router confidence, calibration data, or additional training, and therefore cannot reliably estimate the actual contribution of routed experts. To this end, we propose ACE, a training-free, calibration-free, and checkpoint-preserving framework for token-adaptive expert skipping in MoE-based LLMs. ACE contains two complementary components: 1) Global Spectral Proxy (GSP), which estimates global transformation capacity from the coupled gate, up, and down projections together with RMSNorm scaling; and 2) Router-Conditioned Refinement (RCR), which constructs expert-specific direction prototypes from centered router weights and evaluates expert responses along routing-preferred directions. During inference, ACE combines both estimates with runtime router gates and skips an expert slot only when both views identify it as low-contribution, while always retaining the top-1 expert. All expert statistics are computed offline, leaving only table lookups and lightweight scalar operations online. Extensive experiments across three MoE-based LLMs and eight benchmarks demonstrate that ACE consistently outperforms existing static and dynamic baselines, with increasingly pronounced advantages under aggressive expert skipping. For instance, at a 50% skipping ratio on Qwen3.6-35B-A3B, ACE reduces WikiText-2 perplexity by 7.96% and improves average downstream accuracy by 4.15 percentage points over the strongest competing method.

---


### 142. [Substrate-Aware AI Agents: Execution Context as a First-Class Input](https://arxiv.org/abs/2609.05232)

**<font color=#1a73e8>作者：</font>** Manu Agrawal  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents increasingly select actions in environments whose memory, execution-time, runtime, compute, and operational constraints determine what counts as a suitable plan. We call the absence of this execution context from an agent's planning state substrate blindness. We test this general proposition through numerical code generation, where selected implementation choices and operational consequences are directly observable. Three frontier model configurations--Anthropic Claude Opus 5, OpenAI GPT-5.6-Sol, and Google Gemini 3.7 Flash--generate code for a high-dimensional pairwise Euclidean-distance task either from the task alone or with a 128 MB RAM and 10.0 s wall-time contract. Contract disclosure reduced measured peak process memory in 13 of 14 executable index-aligned task-only versus contract-disclosed comparisons and reduced mean wall time in all three cohorts, making execution up to 3.1x faster. Across the audited corpus, disclosure produced structural code changes including bounded blocking, float32 retention, upper-triangle traversal, and in-place or memory-mapped buffers. At a tighter 96 MB contract, independently sampled contract-disclosed cohorts achieved correct-and-within-budget outcomes of 4/5 for Claude Opus 5, 5/5 for GPT-5.6-Sol, and 3/5 for Gemini 3.7 Flash, compared with task-only outcomes of 0/5, 1/5, and 0/5; cohort mean MaxRSS and wall time were 49-74% and 35-64% lower than their task-only references. These results establish a controlled proof of concept for substrate-aware agent planning: a minimal execution contract induces proactive structural adaptation in generated programs, shifting computation away from unconstrained allocations and substantially improving observed resource-time profiles before execution.

---


### 143. [PRICE: A Systematic Study of LLM Adaptation Choices for Bitcoin Price Forecasting](https://arxiv.org/abs/2609.05235)

**<font color=#1a73e8>作者：</font>** Maryam Fakhari, Mehran Safayani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cryptocurrency markets exhibit extreme volatility and non-stationary dynamics that challenge conventional forecasting methods. Although Large Language Models (LLMs) have shown promise for time series forecasting, the combined effects of adaptation choices remain largely unexplored in financial settings. This study introduces PRICE, a structured approach for adapting LLMs to short-term Bitcoin price forecasting. Built on a 4-bit quantized LLaMA-3 8B model, PRICE investigates how fine-tuning, numerical representation, prompting, inference, and decoding jointly influence forecasting performance. PRICE integrates Parameter-efficient fine-tuning with Low-Rank Adaptation (LoRA), Recursive multi-step inference, Integer-rounded numerical representation, Context-Task-Format (CTF) prompting, and Exact zero-temperature decoding. Ablation studies show that each component contributes to forecasting accuracy and reliability. LoRA enables efficient training on limited hardware, recursive inference improves accuracy, integer-rounded values reduce errors, CTF prompting outperforms Chain-of-Thought, Implicit Chain-of-Thought (iCoT), and few-shot prompting, and zero-temperature decoding improves stability during recursive forecasting. Comparative evaluation against eight transformer-based and time-series foundation models shows that PRICE achieves the lowest forecasting errors on both validation and test sets while maintaining robust performance across evaluation periods. Despite being based on a model primarily pretrained on text rather than time-series data, PRICE achieves competitive or superior performance relative to specialized foundation models. These findings demonstrate that adaptation choices critically determine the accuracy and robustness of LLMs for numerical time-series forecasting.

---


### 144. [Governing Bring Your Own AI: A Parameterized Maturity Model](https://arxiv.org/abs/2609.05236)

**<font color=#1a73e8>作者：</font>** Dare Bello, John Hastings  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Employees are increasingly using personally owned generative AI tools such as ChatGPT, Gemini, and Claude for their daily work. This practice is known as Bring Your Own AI (BYOAI), which is a distinct form of Shadow AI in which employee-authenticated personal accounts are used outside of enterprise identity and security controls. Existing frameworks were designed for AI tools managed by organizations, and their coverage does not extend to unmanaged AI tools used with a personal account. In addressing these issues, we developed a governance model through a systematic review of the literature that produces a risk taxonomy and a framework-engagement profile. We also developed a parameterized governance model that measures how much a level of governance maturity reduces residual risk. A five-level maturity ladder is coupled to a technical control architecture through a chain in which the coverage of the control layer influences the security outcomes. Our study of a curated corpus of 30 records (24 research studies and 6 framework documents) indicated that the most prominent categories identified were data exposure and compliance, and framework engagement was inconsistent. Three mutually supporting pillars (technical, governance, and human) were established to support safeguards. Additionally, the results of the model demonstrated that prohibition-based solutions will result in residual risk levels close to those achieved through baseline solutions. Under the specified parameterization, layered control-based solutions substantially reduce modeled exfiltration risk and increase enforceable coverage.

---


### 145. [Cross-Domain Tracker Adaptation Without Target-Domain Labels via Vision-Language Agents](https://arxiv.org/abs/2609.05239)

**<font color=#1a73e8>作者：</font>** Daniel Davila, Ravikumar Balakrishnan, Mike Cochran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a system that uses a Vision-Language Model (VLM) as a diagnostic agent for adapting a detect-to-track pipeline to a new target domain without access to target-domain labels. Rather than optimizing against annotated metrics, the VLM directly inspects rendered tracking outputs, identifies visual failure modes, and recommends parameter updates through an iterative tuning loop. We first demonstrate that ground-truth-supervised hyperparameter transfer can be brittle. On MOT17->MOT20, applying a source-derived oracle configuration reduces mean HOTA by 0.090, from a target-domain ceiling of 0.357, to 0.267. Without using any target-domain labels, our VLM-based tuner recovers 67.8% of this lost headroom, finishing within 0.029 HOTA of the target ceiling; on the highest-density target sequence, it recovers up to 86.7%. We further show that label-free Bayesian optimization with handcrafted proxy objectives struggles under large domain shifts and can degrade configurations that are already strong. In contrast, the VLM tuner acts selectively: when its visual diagnosis reveals no clear failure mode, it declines to modify the configuration, preserving performance on easy transfers while improving hard ones. Finally, we characterize the conditions under which this approach succeeds, namely, when domain shift manifests through exposed detection-level parameters, versus where it is less effective, such as MOT17->DanceTrack, where the source oracle is already near-optimal.

---


### 146. [Uncensored Open-weight Models: Redistribution as the Persistence Layer](https://arxiv.org/abs/2609.05241)

**<font color=#1a73e8>作者：</font>** 10a Labs, Juliette Garcia, Hailey May 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A rapidly expanding ecosystem of actors is removing built-in safety guardrails from open-weight AI models. We profile this ecosystem by identifying key producers, downstream reproductions, and emerging applications. Between January 2024 and March 2026, we identified 3,471 original uncensored models on HuggingFace, each repackaged an average of 2.4 times; three actors account for 52% of all 8,164 compressed redistributions. Once quantized and mirrored across separate accounts, formats, and registries such as Ollama, these models persist regardless of upstream removal and become easier to deploy downstream. Of the 1,643 identified GitHub applications integrating uncensored large language models (ULLMs), 25% were classified as explicitly malicious.

---


### 147. [Do LLMs Exhibit Coherent Knowledge Structures in Mathematical Reasoning? A Perspective from Knowledge Space Theory](https://arxiv.org/abs/2609.05245)

**<font color=#1a73e8>作者：</font>** Peng Cui, Heejin Do, Mrinmaya Sachan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human knowledge is inherently structured and interdependent: mastery of a concept requires prior mastery of its prerequisites, a principle formalized by Knowledge Space Theory (KST). While LLMs achieve strong performance on complex reasoning tasks, it remains unclear whether they exhibit coherent, human-like knowledge structure. We introduce a KST-grounded framework for evaluating LLM knowledge structure in mathematical reasoning, using it as a normative framework to analyze whether LLM behavior adheres to principled knowledge dependencies. Evaluating eight open- and closed-source LLMs against real human learners, we find that (1) LLMs do not adhere to human knowledge structure -- they frequently violate knowledge dependencies and fail to leverage related knowledge provided in context to improve performance on dependent questions; (2) LLMs do not share a consistent knowledge structure among themselves, as reflected by low overlap in their knowledge distributions. Furthermore, these structural deficiencies remain largely invisible to accuracy-based and LLM-as-judge evaluations. Together, our results provide behavioral evidence that current LLMs knowledge does not follow a human-like structure.

---


### 148. [Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for LLM Agents](https://arxiv.org/abs/2609.05261)

**<font color=#1a73e8>作者：</font>** Jiazheng Sun, Boyu Yang, Binhao Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly rely on execution traces to master complex interactive tasks. However, current paradigms are bottlenecked by shallow trajectory retrieval and flat skill summarization, fundamentally ignoring the temporal dependencies and outcome-conditioned topology of agent behavior. We introduce Trace2Tower, a transition-aware EigenTrace framework that distills raw trajectories into a robust skill hierarchy. Trace2Tower abstracts step-level interactions into canonical events, constructing a unified graph governed by semantic compatibility, transition dynamics, and outcome evidence. Through a novel contrastive spectral decomposition, it isolates stable, success-aligned behavioral modes while rigorously suppressing failure-prone shortcuts. These modes organically populate a dynamic skill tower of action templates, procedural routines, and overarching task strategies, continuously refined via verifier-guided feedback. On ALFWorld, Trace2Tower achieves 87.31% success requiring only 10.35 steps and 0.26 invalid actions; on WebShop, it reaches 50.67% exact success. Across both benchmarks, Trace2Tower significantly outperforms existing baselines in task mastery and context-efficient experience reuse.

---


### 149. [CONTINUITY: Security-Context Contracts for Composable LLM Agent Controls](https://arxiv.org/abs/2609.05269)

**<font color=#1a73e8>作者：</font>** Chris Zheng, Geng Yang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agent systems increasingly combine provenance tracking, authorization, policy enforcement, protocol adapters, and execution controls. However, individually correct security mechanisms do not necessarily compose into an end-to-end secure system: security-critical context may be dropped, widened, rebound, or reinterpreted as actions cross component boundaries. We identify this failure mode as security-context discontinuity and introduce CONTINUITY, a framework for verifiable composition of agent security controls.
CONTINUITY models each component with an assume-guarantee contract and carries authenticated security context across transitions using signed root grants, provenance commitments, role-bound transition receipts, bounded typed releases, transformation witnesses, and effect-bound execution permits. We formalize end-to-end consequence integrity, requiring every realized external effect to be backed by a valid and current authorization witness linking the principal, task, provenance, delegation, policy state, canonical action, and finality boundary.
We implement a reference verifier and deterministic cross-layer fault-injection suite covering 32 fault classes across four application domains. In 2,560 parameterized attack instances spanning 128 fault-domain classes, the full CONTINUITY configuration commits no harmful external effect, while completing all 700 benign tasks and escalating all 200 ambiguous cases. These results show that secure agent execution requires not only sound individual controls, but explicit contracts that preserve their guarantees across the complete instruction-to-effect path.

---


### 150. [How to Speculate about Uncertainty in Agentic Coding? A Draft-Model Gate Method](https://arxiv.org/abs/2609.05274)

**<font color=#1a73e8>作者：</font>** Konstantin Grotov, Valentin Malykh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents deployed for software engineering fail expensively: they act confidently wrong, and bad actions are recognized only after costly execution and retry. We present Speculative Uncertainty (SU), a method that recovers a predictive failure signal for a black-box agent from its output tokens alone, with no access to logits, weights, activations, or repeated sampling. Inverting speculative decoding, a small open-weight draft model scores the agent's already-generated trajectory in a single forward pass. From these speculative cross-likelihoods we extract phase-aware features by separating the reasoning and action spans, and calibrate them against a verifiable objective. SU produces a failure-likelihood score that any downstream policy, such as routing, human intervention, or extra test-time compute, can consume directly. To show the signal is actionable, we instantiate one such policy, a pre-execution veto gate, on software engineering agents Qwen3-Coder-480B and closed-source Claude 3.5 Sonnet, cutting execution error rate by 6-8 percentage points and token cost by 14-19% in deployment, transferring to out-of-distribution benchmarks without retraining, and generalizing across agent models.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-179](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
