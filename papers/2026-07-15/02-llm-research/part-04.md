# 🧠 大模型相关研究 | 2026年07月15日

> 本类共 **199** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-199**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-199**

---

### 151. [Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents](https://arxiv.org/abs/2607.11346)

**<font color=#1a73e8>作者：</font>** Chenglin Yu, Li Yin, Ying Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise agents must follow long-horizon, conditional, safety-critical standard operating procedures (SOPs). We compile machine-readable SOP constraints into executable pseudo-code and run them with a program-guided (PG) stack machine that pages the active frame while an LLM performs semantic execution. A three-arm SOPBench study across six models separates representation from runtime: compiled text never significantly hurts and gains up to 16.0 points where official prose underperforms. Runtime guidance is capability-gated. Two strong models independently show positive seven-domain PG contrasts (58:19 and 75:31 discordant pairs), whereas weak models are harmed. A full-program cursor ablation (active frame first, complete program retained) recovers much of the strong-model refusal gain; selective visibility adds a smaller improvement. Paired probe and audit measurements track this divide to spontaneous state discipline rather than reconstruction ability. On Bank the three primary arms rise from 70.4 to 86.4 to 92.8, with 100% refusal correctness. Practical guidance: compile first; enable active-frame paging only after a model-level discipline check.

---


### 152. [RefineEvo: Planning-Guided Heuristic Evolution with Bidirectional Experience](https://arxiv.org/abs/2607.11358)

**<font color=#1a73e8>作者：</font>** Yang Wu, Junran Pan, Yifan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic Heuristic Design (AHD) has emerged as a transformative approach for solving combinatorial optimization problems. While recent Large Language Model (LLM)-based methods have shown promise, they predominantly rely on fixed evolutionary operators and struggle to effectively accumulate and reuse historical search experience. This paper proposes RefineEvo, a novel evolutionary framework that transforms AHD from a static trial-and-error process into a planning-guided, experience-driven system. RefineEvo introduces a Planner to dynamically schedule evolutionary operators and trigger refinement based on the current search state, and a Reflector to distill valuable lessons into a Bidirectional Experience Pool containing both positive insights and negative pitfalls. This synergistic framework enables the system to adapt its search tools to the evolving complexity of the problem and leverage trajectory-aware, situation-conditioned insights to guide generation. Experiments on several classic combinatorial optimization benchmarks demonstrate that RefineEvo consistently outperforms strong baselines. In particular, RefineEvo delivers superior solution quality while improving token efficiency, enabling more efficient and autonomous heuristic design.

---


### 153. [Efficient Tuning Before Low-Bit Post-Training Quantization for Stochastic Gradient Descent-optimized Models](https://arxiv.org/abs/2607.11359)

**<font color=#1a73e8>作者：</font>** Peng Xia, Junbiao Pang, Muhammad Ayub Sabir  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) compresses deep neural networks for deployment under limited memory and computational budgets. However, low-bit (i.e., 2-bit or 4-bit) PTQ often suffers from substantial performance degradation. Most existing PTQ methods operate on an unconstrained full-precision (FP) model and primarily address quantization errors through post-hoc reconstruction. We argue that low-bit PTQ accuracy is limited not only by post-quantization error minimization, but also by the quantization-error tolerance of a FP model itself. In this paper, we propose Efficient Tuning Before Quantization (ETBQ), a pre-conditioning tuning stage for Stochastic Gradient Descent (SGD)-optimized models before PTQ. During tuning, the FP model is optimized under perturbations sampled from the error distributions of weight and activation quantization, guiding the model toward a loss-landscape region that is less sensitive to the subsequent PTQ. Unlike QAT, ETBQ does not train a fake-quantized deployment model, which is computationally and memory intensive. Instead, ETBQ outputs a FP model that can be used by any PTQ backend. Experiments on CIFAR-100, Tiny-ImageNet, ImageNet, and Cityscapes provide consistent evidence that ETBQ improves low-bit PTQ across diverse tasks. Under W2A4 settings, e.g., ETBQ improves over naive PTQ by 2.14\% top-1 accuracy on Tiny-ImageNet and by 5.80\% mIoU on Cityscapes. Code is available at this https URL.

---


### 154. [Beyond Sally-Anne: Evaluating Theory of Mind in LLMs using Epistemic Schelling Points](https://arxiv.org/abs/2607.11363)

**<font color=#1a73e8>作者：</font>** Roberta Rocca, Sami Boukortt, Geoff Keeling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-based evaluations of Theory of Mind (ToM) in Large Language Models (LLMs) often involve cognitive tests akin to the Sally-Anne task that can be gamed due to exposure to relevantly similar tasks in pre-training and do not obviously test models' functional ToM abilities in ways that generalize to naturalistic settings. To address these issues, we introduce the Epistemic Asymmetry Schelling Task (EAST), a two-player dialogue game designed to benchmark robust and generalizable ToM abilities. By requiring LLM-LLM dyads to independently converge on semantic Schelling points under varying states of epistemic transparency, we evaluate whether models can robustly apply ToM to achieve coordination. Our results reveal a significant capability gap in functional social reasoning, with only frontier models successfully navigating the varying epistemic demands of the tasks. Analysis of reasoning traces shows that coordination failures are primarily driven by epistemic tracking errors, such as conflating private knowledge with mutual knowledge. Despite high performance on traditional static benchmarks, our study shows that robust social reasoning and epistemic tracking remain a critical bottleneck, providing concrete targets for future LLM evaluation and development.

---


### 155. [Surprisingly Simple and Effective Multi-Domain Graph Foundation Model through Graph-to-Table Alignment](https://arxiv.org/abs/2607.11374)

**<font color=#1a73e8>作者：</font>** Chunyu Hu, Tianyin Liao, Ge Lan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Foundation Models (GFMs) have emerged as a promising paradigm for learning transferable representations across diverse graph domains. Recent advancements in GFMs have been largely dominated by two paradigms: Graph Neural Network and Large Language Model (LLM) based methods. However, these methods often face a fundamental dilemma between training with limited data and a heavy reliance on textual attributes. Tabular foundation models (TFMs) offer a potential alternative, as node features and representations can be naturally organized in a tabular form. However, how to enable TFMs to effectively capture structural information of graphs remains largely unexplored. The key challenge is to learn a graph-to-table alignment mechanism that enables graph structural understanding for TFMs. To address this, we propose GTAlign, a surprisingly simple yet effective Graph-to-Table Alignment framework for text-free Graph Foundation Model. Specifically, we first pretrain a graph encoder that maps diverse graphs into a unified latent space to capture domain-agnostic graph representations. To further bridge the gap between graph topology and the tabular representation space, we propose community-guided continual pre-training, where pseudo-labels derived from graph community are used to construct few-shot prediction episodes. Lastly, we adapt the graph encoder for an unseen target domain and perform in-context inference. Extensive experiments on five benchmark datasets demonstrate that GTAlign significantly outperforms state-of-the-art baselines on both node and graph classification, offering a simple, effective, and text-free GFM model. Code will be released upon acceptance.

---


### 156. [StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure](https://arxiv.org/abs/2607.11388)

**<font color=#1a73e8>作者：</font>** Wenyi Wu, Sibo Zhu, Kun Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) and vision-language models (VLMs) have enabled increasingly capable digital agents for computer use. However, real-world tasks are often long-horizon and involve evolving contexts containing accumulated observations, intermediate edits, failed attempts, and partially completed executions. Existing agents typically operate over raw interaction history, making task progress difficult to interpret, verify, and recover, which ultimately limits reliable long-horizon execution. In this paper, we argue that addressing this challenge requires explicitly structuring both the agent's state and workflow around a unified causal representation of task progress. We present \textbf{StructAgent}, a state-centered framework that introduces a unified state for maintaining compact, verifiable task progress and a structured workflow that regulates progress through verifier-backed state transitions. Building on this design, StructAgent further enables explicit progress checkpointing, evidence-driven task completion, targeted failure recovery, and tool-supported execution, while ensuring that all progress updates remain grounded in verification. Extensive experiments demonstrate that StructAgent consistently improves a wide range of LLM and VLM backbones on long-horizon computer-use tasks. On OSWorld-Verified, it improves Qwen3.5-9B from 27.0\% to 46.9\% success rate and Qwen3.5-27B from 31.6\% to 62.2\%, while achieving a new open-source state of the art of 78.9\% with MiniMax-M3. Moreover, the same framework generalizes beyond desktop environments to Minecraft, demonstrating the generality of our design.

---


### 157. [Agentic Routing: The Harness-Native Data Flywheel](https://arxiv.org/abs/2607.11399)

**<font color=#1a73e8>作者：</font>** Xinchen Liu, Hang Zhou, Yingjie Zong 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly executed not by a single model call, but by an execution harness that manages observation, context, control, action, state, and verification. At the same time, frontier and open models are becoming structurally specialized: a model that is strong at code editing, long-context recovery, tool use, mathematical reasoning, or low-latency response may not dominate on the other axes. This makes model selection inside an agent a core systems problem rather than a per-query serving trick. Existing routing methods mostly optimize single-turn cost-quality trade-offs and therefore miss the execution state, intermediate failures, and feedback loops that make agents different from chat completion. We propose Harness-Native agentic routing, a step-level routing paradigm that selects either a single best-fit model for cost-effective execution or multiple complementary models for ensemble-style accuracy improvement, conditioned on the full harness state. The key insight is that every routing decision naturally produces a structured data record -- consisting of the query, harness state, model choice or model set, execution trace, outcome, and cost -- whose labels are supplied by the environment rather than by the router itself. These records form a harness-native data flywheel: execution traces train better routers and harness-native models, which improve cost-quality trade-offs and generate more traces under the same budget. We instantiate this idea in OpenSquilla with a four-layer routing stack, an open LightGBM cold-start ranker, and a staged router-model path that turns logged arena records into progressively stronger routing policies. The report studies singleton and multi-model routing on agentic benchmarks including DRACO and PinchBench, and argues that agentic routing is not merely cost control, but a data engine for agent-native training.

---


### 158. [Cross-Architecture LLM Ensembles, Feature-Based Reranking and Retrieval-Augmented Prompting for Legal Information Processing](https://arxiv.org/abs/2607.11400)

**<font color=#1a73e8>作者：</font>** Amal Saad Alshehri, Nelly Bencomo, Amir Atapour-Abarghouei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal information processing spans retrieval, entailment and judgment prediction problems, requiring text matching, reasoning and robust generalisation with limited supervision. We report Team DU's participation in all five tasks of COLIEE 2026, using open-weight systems for legal case retrieval, case entailment, statute retrieval and entailment, and legal judgment prediction. For Tasks 3 and 4, all models predate the 15 July 2025 cutoff required by the rules. For Task 4 (statute entailment), a cross-architecture ensemble of nine models from three families achieves 96.3% accuracy, placing first among 33 submissions from 11 teams. For the Pilot Task (tort prediction and rationale extraction), a multi-view system combining five claim-level models and refining the verdict using features derived from the claim predictions achieves 73.1% TP accuracy and 68.2% RE F1 as an unofficial submission, scoring above all official entries on TP and matching the highest on RE. For Task 2 (legal case entailment), changing only the prompt from single- to multi-selection raises F1 from 0.343 to 0.555 in post-competition evaluation on released gold labels, exceeding the best official submission (F1 = 0.490). For Task 3 (statute retrieval and entailment), replacing the entailment model with Qwen3-235B and a structured legal reasoning prompt raises accuracy from 79.3% to 91.5% in post-competition analysis. For Task 1 (legal case retrieval), a learning-to-rank system combining lexical and semantic retrieval with structural, citation authority, and temporal features (34 in total) achieves F1 = 0.314 (rank 11 of 54 submissions from 22 teams). Overall, legal information processing benefits from different inductive biases across tasks, with cross-architecture ensembling, feature-based reranking and retrieval-augmented prompting each proving most effective in different settings.

---


### 159. [Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States](https://arxiv.org/abs/2607.11414)

**<font color=#1a73e8>作者：</font>** Richard Zhe Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) in financial applications fail most consequentially when they are confidently wrong. Hedged, uncertain answers invite scrutiny, whereas confident errors silently degrade downstream decisions without warning. We ask how reliably such confidently wrong answers, or confident hallucinations, can be detected from a model's internal activations, and whether those activations carry information beyond its observable outputs. We train linear probes on the residual stream and evaluate them on two established question-answering (QA) benchmarks built from real filings, FinQA and TAT-QA. Behavioral confidence is measured as the agreement among eight resampled answers to the same question, and probe effectiveness is compared against baselines, such as token log-probabilities and the model's own True/False self-assessment of its answer. Our findings show that among confident answers, those for which all eight resamples agree, 15-23% are wrong on FinQA. There the probes have a significant advantage over baseline methods in detecting hallucinations, holding 0.68-0.77 AUROC while the best baselines fall to 0.55-0.63, across Qwen3-8B, Llama-3.1-8B, and Gemma-2-9B. Our results suggest that probing can be a cost-effective triage mechanism for routing LLM answers to human review and quality control procedures in high-stakes financial applications.

---


### 160. [ToFu: A White-Box, Token-Efficient Agent Harness for Researchers](https://arxiv.org/abs/2607.11423)

**<font color=#1a73e8>作者：</font>** Junhao Ruan, Yuan Ge, Bei Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic coding tools present new opportunities to transform research workflows. The performance of agent systems built depends on both large language models (LLMs) and the harness around LLMs, which is the orchestration code that determines an agent's behavior. We present ToFu, an agentic harness for researchers that reads your codebase, edits files, runs commands, and integrates with your development tools. ToFu plays a dual role in research. As a research assistant, it supports practical research workflows with superior token efficiency, lower cost, and multilingual capability compared with existing agentic harnesses. Its release under the MIT License further enables local deployment for privacy-sensitive users. As a research object, ToFu provides a white-box agentic harness that allows researchers to inspect, modify, and evaluate its orchestration logic, tool-use behavior, and harness design, while retaining strong benchmark performance and an application-level user experience.

---


### 161. [Direct Image-to-Modern Vietnamese Translation of Han-Nom Manuscripts via Multimodal RLHF Preference Alignment](https://arxiv.org/abs/2607.11434)

**<font color=#1a73e8>作者：</font>** Thi Kim Trang Vo, Nghia Hieu Nguyen, Ha Minh Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translating Han-Nom manuscripts into modern Vietnamese is challenging because historical pages are often degraded, the script contains rare logographic characters, and parallel supervision is limited. We propose a multimodal RLHF preference-alignment framework that conditions Vietnamese generation on manuscript images and aligned Han-Nom source text. The model combines four streams: CLIP ViT-L/14@336 for visual features, bert-base-chinese for Han-Nom representations, vinai/phobert-base for Vietnamese representations, and T5-small encoder states. Modality-specific projections and a fusion block compress the resulting 2,048-dimensional concatenation into a shared 512-dimensional representation. Starting from the same supervised fine-tuned policy, we compare PPO, DPO, and KTO under matched work-level macro-averaged evaluation. DPO achieves the best BLEU-4, ROUGE-L, BERTScore, semantic similarity, CER, WER, and token accuracy, whereas PPO obtains the highest precision, recall, and F1. KTO remains competitive through its desirable-undesirable utility objective. All preference-aligned policies improve the BLEU-4 and semantic-similarity scores available for the SFT baseline. These results indicate that multimodal preference optimization complements supervised learning by improving lexical and semantic quality in low-resource historical translation.

---


### 162. [The Ebb and Flow of Multimodal Focus: Scheduling Visual Relay Windows for Grounded VLM Reasoning](https://arxiv.org/abs/2607.11436)

**<font color=#1a73e8>作者：</font>** Wencheng Ye, Yi Bin, Yujuan Ding 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models increasingly succeed on multimodal reasoning benchmarks, yet their visual evidence often becomes unstable once it enters the language stack, weakening evidence-grounded reasoning. To understand this fragility, we examine the internal dynamics of VLMs through a mechanistic lens and uncover a stable three-stage redistribution of multimodal attention focus across depth: an early question-conditioned organization, a critical middle visual-dominant relay, and a late return to answer formation. We operationalize the middle phase as the Visual Relay Window (VRW), and show that its geometry varies with task demand, is causally tied to grounded generation, and distinguishes unsupported answers from stronger reasoning trajectories. Guided by this internal rhythm, we propose TRACE, a task-adaptive inference-time control framework with lightweight trained modules. It reshapes relay allocation during prefill and preserves assembled visual support after handoff during decoding. Across four open-weight VLM backbones and seven benchmarks, TRACE delivers large gains on grounding-sensitive settings, improving them by 4.33 points on average and by up to 6.6 points, while also improving reasoning-heavy tasks. These results show that explicitly controlling multimodal focus across depth offers a unified and effective mechanism for strengthening evidence-grounded multimodal reasoning.

---


### 163. [UMoE:Unlocking Every Expert in Domain-Specific Training](https://arxiv.org/abs/2607.11444)

**<font color=#1a73e8>作者：</font>** Xuefeng Li, Pengfei Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models scale capacity without proportional compute cost and have become a key architecture for frontier large language models (LLMs). Yet domain-specific post-training inherits an expert pool shaped by mixed-domain pre-training: a substantial subset of experts contributes little on the target domain, and standard supervised fine-tuning (SFT) leaves the composition of this pool unchanged. We propose a simple, budget-preserving pipeline that realigns the expert pool to the target domain before fine-tuning. Given a target domain, we (1) prune the experts with lowest domain-aligned saliency, (2) regrow the expert pool to its original size through perturbation-based expert expansion, and (3) apply standard SFT. The resulting model preserves the original expert count, parameter count, and inference cost. With a single frozen recipe and no per-domain hyperparameter tuning, UMoE consistently improves over direct sft across two MoE architectures (Qwen3-30B-A3B and Qwen3.5-35B-A3B), five domains (math, code, science, tool-use, and agentic coding), and 12 benchmarks. Representative improvements are 3.4 points in math average accuracy, 6.0 points on SWE-bench Verified. On a strong in-house math corpus, direct sft already surpasses Qwen3-30B-A3B-Thinking (82.81 vs.\ 81.06), yet UMoE further raises the average to 84.17, an additional 1.36 points, demonstrating robustness to a substantially stronger SFT regime. Data-scaling experiments further show that the gain persists as training data grows. Analysis reveals that the direct-SFT model allocates substantial routed-expert compute to a low-saliency subset that can be removed post hoc with little average degradation; UMoE turns this redundant capacity into useful domain capacity and achieves lower training loss, with gains spanning all difficulty levels in downstream evaluation.

---


### 164. [ManiScope: LLM-Assisted Visual Analytics of Cryptocurrency Manipulation Risk](https://arxiv.org/abs/2607.11451)

**<font color=#1a73e8>作者：</font>** Xiaolin Wen, Feng Liang, Yuanye Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cryptocurrency markets are vulnerable to trade-based manipulation, such as wash trading, which can distort price signals and mislead investors. Prior research has mainly focused on detecting manipulation using fixed rules or labeled examples, offering limited flexibility and interpretability for assessing potential risks. Existing visual analytics tools can reveal basic manipulation-related signals, such as token distribution, but still require substantial manual effort to integrate holder relationships, suspicious behaviors, and market dynamics for risk assessment. To address these limitations, we propose ManiScope, an LLM-assisted visual analytics system for analyzing trade-based manipulation risks in cryptocurrency markets. ManiScope provides coordinated views of token distributions, holder relationships, detailed holder behaviors, price dynamics, and suspicious trading patterns. To further enhance user analysis, ManiScope introduces a human-LLM collaborative visual analytics framework. Rather than acting as a basic reactive LLM assistant, the framework positions the LLM as a co-analyst that infers users' analytical intent and emerging hypotheses from interaction context and surfaces relevant visual, statistical, and synthesized evidence for hypothesis evaluation. This design reduces repetitive inspection and strengthens evidence-based reasoning. We evaluate ManiScope through two case studies and a user study with 12 experienced cryptocurrency practitioners. The results suggest that ManiScope supports effective risk assessment of manipulation, reduces manual effort in evidence-seeking, and organizes findings around user hypotheses.

---


### 165. [Are LLMs ready for HardChoices?](https://arxiv.org/abs/2607.11471)

**<font color=#1a73e8>作者：</font>** Dmitry Nikolaev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A lot of research attention has been devoted to checking whether large language models (LLMs) are politically biased. This work has largely focused on high-level ideological dimensions, such as left--right or progressive--conservative, and it has been shown that while LLMs are predominantly left and progressive leaning, largely mimicking the biases in the training data, they can be to some extent steered to change their preferences in post-training. In this short note, we check if LLMs have robust stances with regard to major substantive societal issues, on which members of the same ideological camp are often in disagreement, summarised in a novel dataset \textsc{HardChoices}. We show that, faced with this line of questioning, LLMs, both large and small, surprisingly rarely declare neutrality, are often incoherent, and demonstrate a remarkable degree of agreement on issues where they do take stances.

---


### 166. [HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models](https://arxiv.org/abs/2607.11475)

**<font color=#1a73e8>作者：</font>** Aznaur Aliev, Carlos Hinojosa, Abdelrahman Eldesokey 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety alignment in large language models can be fragile under fine-tuning, as even benign task adaptation may increase harmful compliance. Existing defenses mainly follow two directions: they either intervene during or after fine-tuning through retraining or weight modification, which can be costly and may hurt task performance, or they use model-agnostic safety classifiers, which may miss failures specific to a given fine-tuned checkpoint. These limitations motivate a post hoc, model-specific, and non-invasive approach to safety restoration. To meet these requirements, we propose HyperSafe, a framework that restores safety behavior by generating a model-specific Safe Side Network (SSN) for each fine-tuned checkpoint. HyperSafe uses layer-wise activation fingerprints to capture how fine-tuning changes the model's inner representations. With a small set of given calibration prompts, the hypernetwork maps these fingerprints to the parameters of the \ssn{} in a single forward pass. The generated \ssn{} runs alongside the frozen fine-tuned model and performs prompt-level safety classification: harmful prompts are routed to refusal, while safe prompts are answered by the original fine-tuned model. Thus, HyperSafe requires no gradient updates, no safety data at deployment time, and no modification to the deployed model weights. We evaluate HyperSafe on two model families, Qwen2-7B and LLaMA-3-8B, across multiple safety benchmarks. HyperSafe reduces harmful response rates from 19-31% to below 1% on every held-out checkpoint, while keeping downstream task accuracy within 1% of the fine-tuned baseline on average. Code is available at this https URL.

---


### 167. [Agentic Skill Optimization over Lie Algebroids](https://arxiv.org/abs/2607.11493)

**<font color=#1a73e8>作者：</font>** Sridhar Mahadevan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic systems increasingly improve themselves by editing skills: prompts, rubrics, plans, tool contracts, examples, validators, and traces. Skill edits are not independent coordinates in a vector space: they are local repairs to structured artifacts whose effects are observed only after rollout, validation, and critique. Distinct edits can have the same immediate visible effect while differing in routing context, template state, guardrail scope, or future composability. The order of edits can matter as well: repairing a schema before a normalization rule need not be equivalent to applying the same edits in the reverse order. This paper introduces a new framework for skill optimization called LASKO, for Lie Algebroid SKill Optimization. LASKO models typed, anchored Markdown skills as the base category and available edit policies as sections of a controlled Lie algebroid with anchor $\rho$. The anchor maps an edit policy to its visible Markdown effect; the kernel $\ker(\rho)$ represents latent template, routing, or implementation structure; and the algebroid bracket measures noncommuting edit composition. As shown in the paper, LASKO achieves order-of-magnitude speedups in skill optimization in our preliminary benchmark results, primarily because it substitutes inexpensive Lie-bracket screening tests that run in microseconds, before investing in expensive validations that require running large language models. On a causal extraction from natural language task, LASKO achieved a speedup of almost $15 \times$ compared to a brute-force approach that validated all edits by running them through a DeepSeek V3.1 4-bit model with 671B parameters.

---


### 168. [Proxy Exploration and Reusable Guidance: A Modular LLM Post-Training Paradigm via Proxy-Guided Update Signals](https://arxiv.org/abs/2607.11505)

**<font color=#1a73e8>作者：</font>** Daocheng Fu, Rong Wu, Yu Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training is essential for refining the domain-specific capabilities of large language models (LLMs), yet existing reward optimization and distribution matching methods tightly couple policy exploration with distribution alignment. This coupling forces expensive exploration directly on the policy model and severely hinders the asynchronous generation, reuse, and cross-model transfer of optimization signals. In this paper, we propose Proxy-guided Update Signal Transfer (PUST), a novel post-training framework that fundamentally decouples update-signal exploration from distribution alignment. Instead of utilizing the primary model for costly exploration, PUST employs a lightweight proxy model as an efficient testbed to discover high-reward behaviors. We extract the relative improvement signal between the proxy's initial and optimized states, transferring this directional update to the primary model to guide its policy alignment. This decoupled pipeline, comprising proxy exploration, update-signal extraction, and signal transfer, significantly reduces computational overhead and enables optimization signals to be asynchronously generated, cached, and reused. Crucially, by transferring relative improvements rather than absolute policy distributions, PUST naturally supports weak-to-strong improvement and seamless cross-model transfer. Systematic evaluations on Qwen3-family models across math and code domains demonstrate that update signals extracted from substantially weaker proxies can robustly and adjustably enhance stronger primary models. Ultimately, PUST transforms post-training from a monolithic online optimization process into a highly modular, reusable, and cost-efficient paradigm.

---


### 169. [CDFM: Towards a General-Purpose Causal Discovery Foundation Model](https://arxiv.org/abs/2607.11508)

**<font color=#1a73e8>作者：</font>** Jie Qiao, Ruichu Cai, Zijian Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery, the process of recovering underlying causal structures from observational data, is a fundamental pursuit across scientific disciplines. Over the past decades, numerous algorithms have been developed to tackle this challenge through workflows tailored to the specific causal mechanisms underlying each type of dataset, demonstrating effectiveness across a wide range of applications. However, as the volume and heterogeneity of real-world data continue to grow, this dataset-specific approach inevitably leads to a fragmented, test-driven paradigm that struggles to scale to the demands of modern scientific discovery. To address this, we formulate the Causal Discovery Foundation Model (CDFM) as a unified, general-purpose framework for zero-shot structural inference. To ensure reliable generalization across unknown domains, we first investigate the theoretical boundaries of causal identifiability, revealing the indispensable role of causal prior mechanisms in this process. Building on these insights, we formulate a principled variational framework that treats unknown causal mechanisms as latent variables and mathematically decomposes the intractable marginal likelihood into distinct, tractable learning modules. The variational decomposition provides a conceptual design principle for the architecture design of CDFM, while comprehensive causal knowledge guides the large-scale synthesis of our pretraining data. By pretraining on a massive, highly diverse space of synthetic structural causal models, CDFM successfully internalizes complex statistical asymmetries. Extensive experiments demonstrate that CDFM consistently outperforms traditional algorithms, driving a paradigm shift toward a general-purpose causal discovery foundation model.

---


### 170. [DAG-FM: A Foundation Model for Causal Discovery under Heterogeneous Causal Mechanisms](https://arxiv.org/abs/2607.11510)

**<font color=#1a73e8>作者：</font>** Yikang Chen, Zhengkang Guan, Haoyuan Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery from observational tabular data remains fundamentally challenging, primarily due to the heterogeneity of underlying causal mechanisms and the high-dimensional combinatorial search space of Directed Acyclic Graphs (DAGs). In this paper, we propose \textbf{DAG-FM}, a novel foundation model architecture that amortizes causal discovery. Unlike direct matrix prediction, DAG-FM decomposes the causal discovery process into two auto-regressive stages using two specialized Transformer-based sub-modules: a leaf-node predictor and a parent-node predictor. To effectively model complex row-column interactions, we adopt a robust tabular interaction block to output feature-wise representations. Crucially, to handle diverse and unknown Functional Causal Model (FCM) assumptions in real-world scenarios, we introduce Mixture-of-Leaf-Experts (MoLE), allowing the model to dynamically route and adapt to identifiable mechanism families. Through an iterative inference algorithm, DAG-FM seamlessly extracts causal orderings and constructs valid DAGs. Extensive experiments demonstrate that DAG-FM achieves state-of-the-art performance on both synthetic benchmarks and complex real-world datasets, significantly outperforming traditional classical algorithms and recent foundation models in both accuracy and scalability.

---


### 171. [MonkeyOCRv2: A Visual-Text Foundation Model for Document AI](https://arxiv.org/abs/2607.11562)

**<font color=#1a73e8>作者：</font>** Yuliang Liu, Zhang Li, Ziyang Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mainstream visual encoders are pretrained on natural images and cannot be effectively applied to document images without document-oriented adaptation, as dense text and fine-grained character strokes demand character-level visual perception. We present MonkeyOCRv2, a visual-text pretrained model for document AI. First, we construct MonkeyDoc v2, to our knowledge the largest document-image pretraining corpus, comprising 113 million images spanning 17 languages. Second, we propose a pretraining strategy that jointly learns image-to-text generation and pixel-level document reconstruction: the former aligns visual representations with textual content, while the latter preserves character strokes and layout details. Extensive experiments are conducted on five representative document analysis tasks, including text recognition, formula recognition, text detection, document tampering detection, and overlapping text segmentation. Replacing the original encoders with MonkeyOCRv2 consistently improves performance across all five tasks. Finally, we validate its effectiveness as the vision encoder of multimodal large language models on the more challenging tasks of document parsing and document understanding. Kept frozen and paired with a lightweight language model, it yields a 0.7B document parsing model that sets a new open-source state-of-the-art on MDPBench, a recent benchmark spanning digital-born and photographed documents across 17 languages, surpassing the previous best 3B this http URL by 2.8% absolute with a vision encoder roughly 11$\times$ smaller. The frozen encoder also powers a document understanding model that outperforms counterparts built on CLIP, DINO, and SAM across eight benchmarks under identical training settings. These results suggest that document-oriented visual pretraining can serve as a foundation for document intelligence in its own right.

---


### 172. [PaperRouter-Agent: A Content-Grounded LLM Agent for Personalized Hierarchical Paper Routing](https://arxiv.org/abs/2607.11564)

**<font color=#1a73e8>作者：</font>** Keshen Zhou, Lintao Wang, Suqin Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers organize the papers they collect into personal folder hierarchies in reference managers, and route each new paper into the folder where it belongs. This task differs from standard hierarchical text classification. A user's folder hierarchy is not a fixed, shared taxonomy but a private and evolving folksonomy whose folder meanings may be topical, shorthand, venue-based, or process-oriented, and are often defined by the papers already stored inside them. We formalize this setting as personalized hierarchical paper routing (PHPR): assigning an incoming paper to folders in a user-specific hierarchy without per-user training. We propose PaperRouter-Agent, a training-free LLM agent that grounds routing decisions in folder members rather than folder names alone. The agent first narrows the candidate hierarchy, retrieves folder-specific evidence, verifies fit by inspecting member papers, and incorporates similarity-gated feedback from past user rejections. A formative study on real personal libraries shows that PaperRouter-Agent raises overall Recall@1 from 0.39 to 0.61 and Recall@3 from 0.57 to 0.83, with the largest gains on organizational folders defined by metadata such as venue or year, where single-shot methods collapses (Recall@1 0.09 to 0.50). On the public LaMP-2 benchmark, the same approach improves accuracy from 44.5% to 51.5% (+9.0 macro-F1) over a single-shot baseline, while remaining low-cost for practical use.

---


### 173. [Actor as Its Own Critic: Unifying Region Understanding and Localization via CycleGRPO](https://arxiv.org/abs/2607.11581)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Haochen Wang, Yikang Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper introduces Actor as Its Own Critic, a unified reinforcement learning framework, Cycle Group Relative Policy Optimization (CycleGRPO), that jointly optimizes region understanding and localization for Multimodal Large Language Models (MLLMs). Unlike existing separate pipelines, we leverage the inherent duality between the two tasks to construct a self-evaluating reinforcement learning paradigm: "region $\to$ text $\to$ region''. Specifically, a single MLLM first acts as the actor to generate region captions, then immediately transitions to a critic to ground its generated text back in the spatial domain. Therefore, CycleGRPO requires only region inputs, e.g., masks or bounding boxes, entirely bypassing the need for textual ground truths. A quality-aware token-level cycle-consistency reward is employed to assess the semantic discriminability of text captions via their physical localization accuracy. Empirically, built upon SAMTok, our CycleGRPO framework successfully bootstraps both capabilities simultaneously. Without any task-specific fine-tuning, the framework yields consistent performance gains across a wide range of benchmarks, including region captioning, region VQA, grounded dialogue, and referring segmentation. Overall, CycleGRPO offers a straightforward and scalable way to advance pixel-level capabilities in MLLMs. Code and models are released at this https URL.

---


### 174. [HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference](https://arxiv.org/abs/2607.11586)

**<font color=#1a73e8>作者：</font>** Yongqin Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) large language models (LLM) activate only a small number of experts during inference, but token routing introduces persistent expert hotness skew: a small set of hot experts continuously receives most tokens, while the remaining experts are lightly loaded. On 3.5D multi-chiplet systems, this skew not only causes compute imbalance but also amplifies pressure on communication, memory bandwidth, I/O, and execution queues. Therefore, the core problem is not simply to reduce token movement, but to dynamically place and reuse hot expert replicas across different memory tiers.
This paper proposes HCRMap, a hot expert residency mapping framework for pressure-aware expert replica management in 3.5D MoE inference. Based on expert hotness, weight loading cost, migration overhead, and runtime resource pressure, HCRMap dynamically determines which experts should be promoted, retained, demoted, or evicted. It then maps routed token groups to suitable resident replicas, thereby jointly mitigating communication, memory, and queue bottlenecks.
Experimental results show that HCRMap reduces end-to-end latency by 43.6% and 43.0% over Hydra in the prefill and decode stages, respectively; by 34.5% and 33.1% over MoEntwine; and by 46.7% and 46.0% over PIMoE.

---


### 175. [Similarity-Guided Curriculum Fine-Tuning of LLMs for Neural Architecture Synthesis](https://arxiv.org/abs/2607.11591)

**<font color=#1a73e8>作者：</font>** Anujaya Vijayakumar, Radu Timofte, Dmitry Ignatov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Introduce a MinHash-based similarity scheduling framework that constructs a progressive curriculum over neural architecture code for LLM-based neural architecture search (NAS). Using 128-permutation MinHash signatures over normalised 7-gram source code shingles, we partition the reference pool into similarity bands and present them in increasing architectural heterogeneity, with the best LoRA adapter from each stage merged cumulatively into the backbone. We evaluate the framework on OlympicCoder-7B within the LEMUR benchmark on CIFAR-10 image classification, generating N =15 candidate architectures per epoch across six progressive fine-tuning steps. The curriculum achieves 60% peak success rate at the high-similarity level without post-processing repair. A 2*2 ablation at the most diverse level curriculum versus base model, with versus without partial interface repair reveals that without repair the base model (47% peak SR) substantially outperforms the curriculum model (7% SR), while adding partial repair brings both to 53% SR. This pattern is consistent with merge-level weight drift progressively erasing evaluator-interface priors, and suggests that interface repair and curriculum scheduling target distinct failure modes. We further report a cross-dataset transfer observation on SVHN, where direct base-model generation without curriculum warmup yields 27% peak SR at substantially lower accuracy (60.5%) than the CIFAR-10 equivalent, consistent with the increased synthesis difficulty of the unq-family anchor architecture.

---


### 176. [MAGIC: Transition-Aware Generation of Navigable Multi-Scene Game Worlds with Large Language Models](https://arxiv.org/abs/2607.11594)

**<font color=#1a73e8>作者：</font>** Tsz Hei Fan, Choi Wing Fung, Yuxuan Wan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-scene navigation (clearing an objective in one bounded space and then crossing a portal into the next) is a defining feature of contemporary 3D games, but authoring it is laborious: every portal must have consistent endpoints on both sides, each interior must remain navigable once it is furnished, and the resulting connectivity must be kept consistent across many files. Recent large language model (LLM) and multimodal LLM (MLLM) scene generators have made single-interior synthesis dramatically cheaper, yet they produce one scene at a time and cannot, by naive repetition, yield a connected multi-scene world. We identify three obstacles that single-scene methods leave unsolved: cross-scene consistency, in-scene navigability, and the evaluation of whether a transition actually works. We present MAGIC, a prompt-to-project system that addresses all three. MAGIC is a four-stage pipeline that turns a single natural-language prompt into a runnable multi-scene game project: it plans a shared transition-aware intermediate representation, specifies each scene while enforcing portal reachability with a flood-fill validator, generates the scenes together with their transition scripts, and combines them into one project. Because existing single-scene fidelity metrics never execute a transition, we further introduce a transition-focused evaluation agent that runs each transition in play. On a new benchmark of 100 multi-scene cases, MAGIC produces an executable project for every case and reaches 0.99 precision, 0.95 recall, and 0.96 F1 on end-to-end transition identification; stage by stage, it recovers more ground-truth portals and yields markedly more navigable layouts than an LLM baseline and Holodeck. Our code is available at this https URL.

---


### 177. [Extending LLM Context via Associative Recurrent Memory](https://arxiv.org/abs/2607.11614)

**<font color=#1a73e8>作者：</font>** Gleb Kuzmin, Ivan Rodkin, Aydar Bulatov 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extending the context length of large language models (LLMs) is critical for many real-world applications, yet standard transformers remain constrained by quadratic compute and linear memory scaling. In this work, we investigate the Associative Recurrent Memory Transformer (ARMT) as a practical approach for enabling long-context processing in LLMs, constant memory scaling, and better efficiency. We make three main contributions. First, we construct two domain-specific long-context datasets designed to evaluate realistic workloads, focusing on narrow-domain fine-tuning scenarios. Second, we propose a comprehensive training recipe for ARMT-based context extension, combining continued pre-training, synthetic long-context data generation, curriculum learning, and selective integration of associative memory into chosen model layers. Third, we present an extensive experimental study demonstrating that ARMT-augmented models: (i) process inputs well beyond their original context limits without degrading performance relative to in-limit baselines; (ii) generalize more effectively to out-of-distribution context lengths; and (iii) need 30% less FLOPs while preserving baseline performance within the original context window.

---


### 178. [Lesioned Multimodal Language Models Reproduce Aphasic Picture-Naming Patterns](https://arxiv.org/abs/2607.11621)

**<font color=#1a73e8>作者：</font>** Yong Yang, Xiang Guan, Sophie Arheix-Parras 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aphasia following stroke commonly produces systematic naming errors with characteristic profiles, but whether general-purpose language models not designed for clinical simulation can reproduce these patterns remains untested. We investigated (1) whether lesions or controlled perturbations to a multimodal language model can reproduce different types of errors in picture naming, and (2) whether the framework can reproduce the complete error profile of individual persons with aphasia (PWAs). Using LLaVA 1.6, we evaluated perturbation configurations that varied the layer, proportion, and amount of noise applied to model units. We examined 278 PWAs on the Philadelphia Naming Test, classifying responses into seven categories using a validated neural classifier. Six of seven response categories (correct, semantic, mixed, unrelated, neologism, no response errors) emerged at clinically-comparable proportions across distinct parameter space regions, with formal paraphasia being the exception. Searching the perturbation space revealed configurations that reproduced the individual error profile in at least six of seven categories for 97.8% of PWAs and in all seven categories for 79.5% of PWAs. Monte Carlo baselines confirmed that this matching reflects joint inter-category structure rather than marginal overlap. These results establish a quantitative framework for reproducing individual aphasic error patterns in picture naming. They suggest the potential for language models to serve as digital twins of individuals with post-stroke aphasia.

---


### 179. [Reproducing human biases in route choice using large language models: Toward scalable behavioral modeling](https://arxiv.org/abs/2607.11632)

**<font color=#1a73e8>作者：</font>** Jiangtao Han, Shoufeng Ma, Shuxian Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human choice behavior, including route choice, exhibits systematic behavioral biases that deviate from the assumptions of full rationality. Cumulative prospect theory (CPT) has been widely recognized as an effective framework for characterizing such behavioral patterns. However, its large-scale application, particularly in simulation and agent-based modeling, critically depends on specifying individual-level CPT parameters, which remain a major bottleneck. Conventional approaches typically rely on surveys and controlled experiments to calibrate CPT parameters, yet these methods are difficult to generalize and often fail to capture the full diversity of human decision-making. To address this challenge, this paper investigates whether large language models (LLMs) can reproduce human behavioral biases in choice-making without explicit specification of prospect-theoretic parameters. Using route choice as a representative scenario, we design a behavioral evaluation framework and systematically compare LLM-generated decisions with established human behavioral patterns predicted by CPT. Experimental results demonstrate that LLMs are capable of reproducing non-rational human choice biases and can exhibit decision behaviors consistent with prospect-theoretic effects under uncertainty. These findings suggest that generative AI models may provide a scalable alternative for modeling human decision processes and offer a promising foundation for next-generation large-scale agent-based simulation and AI-driven behavioral research.

---


### 180. [ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/abs/2607.11673)

**<font color=#1a73e8>作者：</font>** Mingchao Sun, Luyang Tang, Yu Liu 等 37 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present ABot-3DWorld 0, a universal multimodal 3D world model that turns text, image, and video inputs into high-fidelity, explorable 3D worlds. At the heart of our framework is a unified Spatial Generative Primitive (SGP), a compact tuple of a high-quality panorama and a spatial point cloud that delivers an efficient description of any 3D space. Multimodal inputs are first lifted into this primitive; a 3D-consistent panoramic video generator then explores the primitive along a planned trajectory; finally, our panoramic video reconstruction engine converts the generated video into a clean, photorealistic 3D Gaussian Splatting (3DGS) world. This pipeline covers two regimes: rich inputs (multi-view sets, casual video) are lifted into the SGP through a geometry-rigorous recovery that mirrors the observed scene, while a single image or sentence is completed generatively into a creative world. The result is one low-barrier engine for general 3D content creation that further anchors generated worlds to geographic points of interest, enabling map-native spatial exploration at consumer scale. Experiments show that ABot-3DWorld 0 sets the state of the art among open-source methods and demonstrates stronger scene fidelity than Marble under rich multimodal inputs.

---


### 181. [RAGU: A Multi-Step GraphRAG Engine with a Compact Domain-Adapted LLM](https://arxiv.org/abs/2607.11683)

**<font color=#1a73e8>作者：</font>** Mikhail Komarov, Ivan Bondarenko, Stanislav Shtuka 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph retrieval-augmented generation (GraphRAG) enhances large language models with structured knowledge, yet existing systems construct knowledge graphs in a single extraction pass, producing noisy entities and brittle retrieval. RAGU, an open-source modular GraphRAG engine, addresses this by separating extraction from consolidation: entities and relations pass through two-stage typed extraction, DBSCAN-backed deduplication, LLM summarization, and Leiden community detection. A key insight motivates a compact extractor: the skills an in-pipeline LLM needs - comprehension, extraction, reasoning over context - are language skills that grow only weakly with model size, unlike factual world knowledge. Accordingly, we train Meno-Lite-0.1, a 7B model optimized for language skills, which outperforms Qwen2.5-32B on knowledge-graph construction (+12.5% relative harmonic mean) and matches it on English GraphRAG tasks. On GraphRAG-Bench (Medical), RAGU retrieves the most complete context at every factoid level (evidence recall up to 0.84 vs. $\leq$0.76) and overtakes HippoRAG2 on synthesis tasks; on multi-hop factoid QA, the apparent HippoRAG2 advantage is shown to be largely an answer-format artifact. RAGU is installable via $\texttt{pip install graph_ragu}$, runs on a single GPU, and is released under MIT. The source code is publicly available at this https URL, and the Meno-Lite-0.1 model can be obtained from this https URL.

---


### 182. [Think Through a Bottleneck: Hourglass Reasoning for Rigorous Induction](https://arxiv.org/abs/2607.11696)

**<font color=#1a73e8>作者：</font>** Huan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-refinement often fails to strengthen few-shot inductive reasoning in large language models. Prompting a model to explicitly state its inferred rule does little on its own. What actually matters is a structurally enforced isolation between reasoning stages, so that information can only pass between them as a compressed symbolic state.
We introduce \textbf{Hourglass reasoning}, which enforces strict context isolation between reasoning stages. The frozen LLM acts as a meta-constructor, building for each task a symbolic encoder--decoder: an Induction module compresses the support examples into a schema $\phi$ (encoder) and a transient scaffold $z$; a Deduction module derives rule $T$ (decoder) from these and discards $z$; an Implementer compiles $(\phi, T)$ into artifacts; an error-driven Refiner revises $(\phi, T)$ and regenerates artifacts from scratch. Only $(\phi, T)$ crosses stage boundaries, so all refinement stays anchored to the rule.
We evaluate Hourglass across three benchmarks spanning visual abstraction, hardware synthesis, and textual rule induction, using GPT-5.5 and Gemini 3.1 Pro. On ARC-AGI-2, it raises best-of-5 accuracy by up to 14 points over an iterative-refinement baseline. On ChipBench, it nearly doubles Verilog synthesis accuracy with GPT-5.5, from 31\% to 58\%. BBEH-Linguini draws on puzzles from the International Linguistics Olympiad, a setting where prior work has shown that explicit verbalization can hurt performance. Hourglass mitigates this tendency, and on Gemini 3.1 Pro, it reverses the effect entirely.
Ablations confirm that these gains come from the isolation between stages and the quality of the initial induction, not from prompt wording or the particular symbolic form used. It is how information flows through the reasoning process, rather than the language used to express it, that drives inductive reasoning in frozen LLMs.

---


### 183. [Production and Perception in LLMs: A Token Probability Approach](https://arxiv.org/abs/2607.11703)

**<font color=#1a73e8>作者：</font>** Anna Marklová, Jiří Milička, Martina Vokáčová 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The asymmetry between language production and perception has been well-documented in psycholinguistics. Whether large language models (LLMs) exhibit a functionally analogous distinction remains an open question, particularly given that LLMs rely on the same underlying mechanism (next-token prediction) for both input and output processing. In this exploratory study, we operationalize the production-perception distinction through direct token probability measurements rather than metalinguistic prompting. Using the base Llama-3.1-8B model, we generated poems under a production prompt and re-scored the same tokens under both rephrased production prompts and perception-oriented prompts. Across an extended experiment with four production and three perception prompts, production-perception distances consistently and substantially exceeded production-production distances, with non-overlapping ranges across conditions and an overall average ratio of approximately 1.8. Near-ceiling correlations in the production-production control confirm that the effect is specific to communicative framing rather than prompt surface variation, and we show the effect replicates across five open-weight models (Llama-3.1-8B, EuroLLM-9B, gemma-2-9b-it, Mistral-7B-Instruct-v0.3, and Qwen2.5-7B-Instruct), spanning both base and instruction-tuned variants. Temporal analysis revealed that the perception prompt exerts its strongest influence at the beginning of the sequence, with divergence decaying as generated context accumulates, though the specific shape of this decay varies across prompt pairs. These findings suggest that prompt framing alone induces a production-perception distinction in LLM probability distributions, even within a decoder-only architecture.

---


### 184. [An Explainable Agentic System for Detection of Conversational Scams with Summary-Based Memory](https://arxiv.org/abs/2607.11707)

**<font color=#1a73e8>作者：</font>** Ahmed Omar Salim Adnan, Yogananda Manjunath, Shivanjali Khare  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Following the rapid progress of generative Artificial Intelligence, there is a growing threat posed by conversational scams. These scams often span over multiple weeks or months, gradually build trust and request for money or sensitive information. Existing scam-detection systems mainly focus on isolated messages, which renders them inadequate against this evolving threat. This paper extends single-message phishing detection and presents an explainable agentic system for detecting sophisticated conversational scams. It also introduces ConScamBench-278, an initial public multi-category benchmark for conversational scam detection spanning eight scam types, released to support reproducible evaluation and future expansion. On isolated messages the single-message detector attains 100% phishing recall, while the conversation-level detector identifies all conversational scams in the public LoveFraud02 corpus (83/83) and reaches 97.8% accuracy (95% CI [95.4, 99.0]) on ConScamBench-278. Two user studies (N = 100 and N = 45) further motivate the system: participants report frequently experiencing uncertainty when judging suspicious conversations. In an uncontrolled pre/post comparison, users self-reported trust, self-confidence, and perceived need for AI-based scam detection all increased (p < 0.001, Wilcoxon signed-rank). The system also receives a System Usability Scale score of 74.7 (95% CI [72.5, 76.9]), above the established usability benchmark.

---


### 185. [JobHop v2: A Large-Scale Career Trajectory Dataset from Unstructured Resumes](https://arxiv.org/abs/2607.11715)

**<font color=#1a73e8>作者：</font>** Iman Johary, Guillaume Bied, Alexandru C. Mara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large-scale, richly annotated career trajectory data underpins workforce planning, job recommendation, and labour market analysis, yet publicly available datasets are either small, closed to independent use, or built from pre-standardized occupational codes with LLM-synthesized rather than authentic free text. We present JobHop~v2, an improved version of the publicly available JobHop dataset, constructed through end-to-end large language model (LLM) extraction from a corpus of ${\sim}440{,}000$ pseudonymized, multilingual resumes provided by VDAB, the Flemish Public Employment Service. The released dataset comprises $355{,}315$ career trajectories annotated with ESCO occupational codes, quarter-level temporal information, and normalized five-level education attainment, broadening both the coverage and the annotation richness of the original release. Relative to v1, JobHop~v2 introduces a redesigned extraction pipeline based on reasoning-controlled LLM inference with a retry mechanism (achieving a 100% JSON parse rate), a richer extraction schema, and a revised evaluation protocol scored against three complementary annotation baselines. Evaluated against these baselines, our best extractor comes closest to the inter-annotator agreement ceiling among all compared models, trailing it by only 1.1-2.7 percentage points. The dataset and code are publicly released to support reproducible career-trajectory research.

---


### 186. [STEP: Career-Path Recommendation via Temporal and Educational Trajectory Modeling](https://arxiv.org/abs/2607.11722)

**<font color=#1a73e8>作者：</font>** Iman Johary, Guillaume Bied, Alexandru C. Mara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Career paths encode decades of skill acquisition, role transitions, and educational investment, and understanding them at scale underpins workforce planning, labor market policy, and job recommendation. Resumes are a rich source of information about career paths: they contain detailed descriptions of work experience, education, and skills. Yet their unstructured, heterogeneous, and multilingual nature has long prevented large-scale systematic analysis. With the advent of large language models (LLMs), it is now possible to source rich career trajectory data containing temporal and educational signals from unstructured resumes, enabling new opportunities for career-path recommendation. Exploiting this opportunity, we present STEP (Sequential Trajectory of Employment Prediction), a novel career-path recommendation system that leverages temporal and educational signals to predict the next job in a career trajectory. STEP integrates a time-decay Gated Recurrent Unit (GRU) cell to model temporal dynamics, Feature-wise Linear Modulation (FiLM) conditioned on educational attainment, and attention-based sequence pooling to select relevant features for next job prediction. To improve internal occupation representation for STEP, we introduce ROUTE, a two-stage contrastive procedure that first adapts a multilingual encoder to the career domain via unsupervised denoising autoencoding, then performs supervised contrastive fine-tuning with guided negative selection. We evaluate STEP on four datasets of career trajectories, including an improved version of our publicly available JobHop dataset, and show that it outperforms state-of-the-art baselines in next job prediction. The dataset and code are publicly released to support reproducible career-trajectory research.

---


### 187. [GFR-SAM: Training-Free Referring Camouflaged Object Segmentation via Cross-Image Prompting](https://arxiv.org/abs/2607.11732)

**<font color=#1a73e8>作者：</font>** Yilong Yang, Jianxin Tian, Shengchuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring Camouflaged Object Detection (Ref-COD) requires segmenting hidden targets guided by reference cues. While supervised methods are annotation-heavy and training-free approaches via sparse point-prompting are sensitive to localization errors, we propose GFR-SAM, a robust three-stage training-free framework. GFR-SAM shifts the paradigm from fragile point-matching to a "Generate-Filter-Refine" pipeline. First, we introduce In-Context Exemplar-guided Segmentation, empowering SAM3 with cross-image inference to generate candidate masks via holistic visual exemplars, bypassing its native intra-image constraints. Second, a Region-Global Contrastive Filtering module ranks candidates through DINOv3-based prototypical alignment, effectively suppressing background distractors. Finally, a Geometric-Semantic Refinement module synergizes bounding box and text prompts to recover fine-grained boundaries and enhance instance recall. Evaluated on the R2C7K benchmark, GFR-SAM outperforms existing training-free methods by 8.7\% in weighted F-measure ($F_\beta^w$) and competes with supervised state-of-the-art counterparts. Ultimately, this work underscores the potential of unlocking SAM3's latent capability for cross-image In-Context prompting, establishing a robust, training-free paradigm that effectively bridges the gap between general-purpose foundation models and specialized, label-intensive perception tasks without the need for task-specific fine-tuning.

---


### 188. [Playful AI in Professional Email: A Field Experiment on Tone and Recipient Engagement](https://arxiv.org/abs/2607.11749)

**<font color=#1a73e8>作者：</font>** Ziv Ben-Zion, Teddy Lazebnik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are rapidly reshaping workplace communication, yet whether AI-assisted writing changes how recipients actually behave, and through what channel, remains unknown. Here, in a randomized crossover field experiment, 121 employees across six companies sent work emails under three conditions over three weeks: unaided writing, GPT-5 rewriting in a playful tone, and GPT-5 rewriting in a professional tone. Across 16,880 emails, playful editing increased emotional positivity (B=+0.068, p<0.001), and professional editing decreased it (B=-0.041, p<0.001), yet neither condition directly altered open rates, reply rates, or response times. Instead, within-sender positivity strongly predicted both opening (OR=2.05) and replying (OR=3.32, p<0.001), a significant indirect pathway through which AI editing shaped behavior, in the absence of any direct effect. These findings suggest that AI-assisted communication shapes workplace engagement not through its use, but through the emotional tone of the language it produces.

---


### 189. [How Temperature Shapes Ideological Discourse in Retrieval-Augmented Generation?](https://arxiv.org/abs/2607.11783)

**<font color=#1a73e8>作者：</font>** Elmira Salari, Hazem Amamou, José Victor de Souza 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has been increasingly adopted to reduce hallucinations and strengthen the factual grounding of large language models (LLMs). While robustness to errors in the retrieval process has been explored, the impact of ideological bias on LLM outputs has been overlooked. For instance, if the retrieved material contains ideological positions, the RAG may transmit, amplify, or suppress such ideological discourses in its outputs. In this study, we address this issue by examining the influence of the RAG framework, comprising ideological discourses, in LLM-generated answers. To this end, we applied Lexical Multidimensional Analysis (LMDA) on a corpus of 1,117 COVID-19 treatment articles, identifying three ideological discourses. This corpus is then used as the external knowledge source for the RAG. We assessed several LLMs by having the models answer ideological questions at different sampling temperatures. The generated texts were assessed semantically and lexically based on their similarities with ideological reference texts. Our findings show that the RAG framework is prone to transferring ideological discourses into LLM responses, with sampling temperature having a measurable impact on the strength of this transfer. Discoursive alignment between generated answers and the reference text is highest at moderate temperatures, where models balance stochasticity with retrieval grounding, and drops at low temperatures, indicating that overly deterministic sampling suppresses discourse transfer.

---


### 190. [Forgetting Our Way to Shared Meaning: Effects of Forgetting on Conceptual Alignment in a Non-Partnership Coordination Game](https://arxiv.org/abs/2607.11787)

**<font color=#1a73e8>作者：</font>** Landon Liu, Mary Kelly, Alan Tsang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Shared meaning in language requires people to learn and agree on categories. We ask how characteristics of agents' memories change the emergence and evolution of shared meaning. Without a coordination game, models of conceptual semantics cannot explain how shared meaning emerges and changes in groups of people; however, existing games assume that players share payoffs in a partnership setting. We model conceptual alignment as a non-partnership game and illustrate differences in actual and perceived conceptual convergence from counterfactual simulations using agents with varying levels of adaptiveness and memory degradation. We found that adaptive players achieved actual convergence faster and had closer final conceptual regions than non-adaptive players, while non-adaptive players perceived convergence earlier. Weighing novel information less over time resulted in more stable agreements than fixing the weight of novel information. Memory features are critical to the emergence and evolution of actual and perceived convergence.

---


### 191. [Supporting Reflection in LLM-based Exploratory Search](https://arxiv.org/abs/2607.11810)

**<font color=#1a73e8>作者：</font>** Giulia Di Fede, Salvatore Andolina  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can make exploratory search more efficient but may undermine the reflection and iterative sensemaking needed in unfamiliar domains. Existing LLM tools often prioritize rapid answers over supporting users in tracking how their understanding evolves and how well their strategies align with their goals. We present TrailLM, a system that helps users reconstruct and revisit their exploration paths to support reflection and metacognitive engagement during information seeking. By aligning LLM assistance with users' sensemaking workflows, TrailLM aims to preserve the benefits of LLM-based search while enhancing opportunities for critical reflection on one's own search process.

---


### 192. [Cycle-World: Mitigating Error Accumulation in Long-term Video World Models via Reverse-Prediction Cycle Consistency](https://arxiv.org/abs/2607.11836)

**<font color=#1a73e8>作者：</font>** Zihan Su, Teng Hu, Jiangning Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive diffusion models have enabled high-quality video generation, yet their sequential nature inherently suffers from error accumulation. In long-horizon video synthesis, minor prediction deviations compound over time, inevitably leading to unconstrained generative drift, structural collapse, and severe visual degradation. To address this, we propose Cycle-World, a novel framework designed for stable and temporally consistent long-video generation. Our approach tackles error drift by enforcing strict temporal reversibility across both the training and inference phases. Theoretically, we demonstrate that forward generative drift can be strictly bottlenecked by a cycle-consistency objective. During training, we integrate an efficient reverse-prediction model to implicitly embed causal constraints into the forward generator, compelling it to produce reversible sequences that tightly adhere to the natural video manifold. At inference time, we repurpose this frozen reverse model as a runtime corrector. Through gradient-based cycle guidance, it iteratively refines the generated latent representations, actively suppressing accumulated errors before they are committed to the historical context. Extensive experiments on the VBench benchmark demonstrate that Cycle-World's dual-phase synergy significantly mitigates error drift, achieving state-of-the-art overall generation quality and long-horizon temporal consistency in 60-second synthesis.

---


### 193. [LoRA-Based Cascaded Multimodal Fusion for Action Recognition in Medical Training Environments](https://arxiv.org/abs/2607.11839)

**<font color=#1a73e8>作者：</font>** Divya Mereddy, Jeevan Beedareddy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents a cascaded Low-Rank Adaptation (LoRA)-based multimodal fusion framework for action and activity recognition in healthcare-oriented training environments. The proposed architecture combines parameter-efficient modality-specific adaptation with sequential fusion, enabling modalities to be integrated in stages without retraining previously learned components. Rather than assuming a fixed fusion structure, the framework first integrates more closely related modalities and then incorporates additional heterogeneous modalities, supporting scalable adaptation across datasets with different modality this http URL evaluate the framework on two healthcare-oriented training environment datasets: NurViD and the Nurse Training dataset. Across these datasets, preliminary results suggest that the proposed cascaded fusion strategy improves over individual modality models and provides competitive performance relative to previously reported dataset-specific baselines. Overall, these findings indicate that cascaded LoRA-based fusion is a promising parameter-efficient approach for integrating heterogeneous modalities in medical training action and activity recognition tasks. github: this https URL.

---


### 194. [Beyond the Single Camera: Agentic Multi-View Reasoning in Sports Video Understanding](https://arxiv.org/abs/2607.11844)

**<font color=#1a73e8>作者：</font>** Kerui Chen, Jinglu Wang, Xiaoyi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent Multimodal Large Language Models (MLLMs) achieve strong performance on single-view video understanding benchmarks. However, sports videos involve dense occlusion, rapid motion, and complex interactions that are difficult to resolve from a single viewpoint. In practice, sports events are recorded from multiple camera angles, providing complementary evidence used by referees. Yet, no existing benchmark evaluates MLLMs on multi-view sports video understanding. To address this gap, we introduce SportMV-Bench, a comprehensive benchmark built from official match recordings, through a dedicated pipeline combining LLM-based generation, MLLM-based verification, and human filtering to ensure quality and consistency. SportMV-Bench containing 787 multi-view video bundles and 2592 question-answer pairs across three categories: Perception-Aware Recognition (PAR), Rule-aware Event Interpretation (REI), and Adjudicative Decision Reasoning(ADR). Our analysis shows that current MLLMs fail to effectively exploit multi-view information, with the bottlenecks lying in fine-grained visual perception and view selection rather than logical reasoning or domain knowledge. We propose SportMV-Agent, an agentic framework that orchestrates an iterative loop of active view selection, perception tool execution, and evidence-grounded reasoning, achieving a significant 14.46% relative improvement over the strongest MLLM baseline.

---


### 195. [AdvancedMathBench: A Benchmark Suite for Advanced Mathematical Proof Generation and Verification](https://arxiv.org/abs/2607.11849)

**<font color=#1a73e8>作者：</font>** Lingkai Kong, Zijian Wu, Yuzhe Gu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have achieved remarkable performance on high-school and olympiad-style mathematics, yet their capabilities on advanced mathematics remain poorly understood. Existing benchmarks, however, fall short in both scope and evaluation granularity: they provide limited disciplinary coverage and often rely on final-answer correctness or coarse judgments, leaving the validity of the reasoning process inadequately assessed. To bridge this gap, we introduce AdvancedMathBench, a benchmark suite designed to evaluate advanced mathematical reasoning capabilities. Its core proof-generation benchmark, ProverBench, contains 296 problems spanning undergraduate and doctoral qualifying-exam levels. To provide reliable evaluation of the proofs, we develop a dedicated automatic verification pipeline trained on large-scale expert annotations to produce both correctness verdicts and fine-grained assessments of proof errors, which exhibits strong agreement with human experts on held-out proof trajectories. We further introduce VerifierBench, consisting of 888 model-generated proof trajectories paired with expert ground truth, to evaluate whether models can correctly judge proof validity and provide sound verification rationales. Experiments show that AdvancedMathBench remains challenging for frontier models. On proof generation, the best-performing model, GPT-5.5-xhigh, achieves only 75.8 and 66.1 on the UGD and QE splits, respectively, indicating substantial room for improvement on advanced mathematical proof construction. On proof verification, the best model attains a Balanced F1 of only 65.1, and models generally exhibit low true negative rates, suggesting that critical error detection remains a major bottleneck.

---


### 196. [Evidence-Backed Video Question Answering](https://arxiv.org/abs/2607.11862)

**<font color=#1a73e8>作者：</font>** Shijie Wang, Honglu Zhou, Ziyang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current Video Large Language Models (Video LLMs) excel in question answering (QA) but largely operate as black boxes, providing textual answers without verifiable visual grounding. Existing explainability efforts rely on textual rationales or sparse bounding boxes, which struggle to capture complex video dynamics such as occlusions and non-rigid deformations. We propose Evidence-Backed Video Question Answering (E-VQA), a novel task requiring models to jointly output a semantic answer and precise spatio-temporal evidence: temporal segments and dense, tracked object segmentation masklets. To support this, we introduce ST-Evidence, the first human-verified benchmark for both discriminative and generative pixel-level grounding. Evaluations of state-of-the-art models reveal a critical decoupling between QA accuracy and true visual perception that scaling alone fails to bridge. To address this, we develop scalable, automated generation pipelines to create ST-Evidence-Instruct, a 160k-scale dataset bridging high-level reasoning with fine-grained grounding. Fine-tuning grounded Video LLMs on this data yields substantial gains over the corresponding size-matched UniPixel baselines (e.g., +27.2 t-mean and +13.8 J&F on a 7B model), establishing a robust baseline for explainable, evidence-backed video understanding. Code and data are available at this https URL.

---


### 197. [Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias](https://arxiv.org/abs/2607.11871)

**<font color=#1a73e8>作者：</font>** Zixiang Xu, Sixian Li, Huaxing Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing studies of LLM-as-judge scoring bias work predominantly at the input-output level: they perturb inputs, measure score deltas, and propose prompt-level mitigations. We argue that the same biases admit a representation-level account in the judge's hidden state, complementary to the input-output view and operationally useful in ways it does not afford. We report three findings, across seven judges, seven bias types, and nine benchmarks. Geometry: baseline judging inputs occupy a tight activation manifold while biased inputs are displaced along a low-dimensional, type-specific subspace that sharpens with depth and is recovered consistently by three families of estimators. Causal control: steering hidden states along this subspace drives scoring in both directions, forward shifts reproducing biased scoring on clean inputs and reverse shifts restoring baseline scoring on biased ones, while matched-norm random directions produce shifts an order of magnitude smaller. Operational: a simple linear projection onto the same bias-direction features anticipates judge failures on three entirely unseen benchmarks, substantially outperforming text-based alternatives. Reading bias as activation geometry, rather than as input-output noise, unifies geometric structure, causal control, and operational prediction within a single framework. The project page is available at this https URL

---


### 198. [Metacognition in LLMs: Foundations, Progress, and Opportunities](https://arxiv.org/abs/2607.11881)

**<font color=#1a73e8>作者：</font>** Gabrielle Kaili-May Liu, Areeb Gani, Jacqueline Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metacognition is a foundational component of intelligence critical to effective learning, problem solving, decision-making, communication, and more. In recent years, it has become increasingly recognized as a cornerstone of capable, transparent AI systems. Yet while LLMs have made significant progress across diverse real-world tasks, it is not yet clear when, how, or to what extent they can exhibit or be endowed with effective metacognitive abilities, nor how such abilities can be adapted to advance the fundamental capabilities, reliability, and intelligence of AI systems. This paper bridges this gap by presenting the first comprehensive overview of the current state of knowledge on metacognition for LLMs. We analyze and taxonomize the landscape of this emerging field and summarize recent technical advancements, including methods and benchmarks to measure and evaluate LLMs' metacognitive abilities, techniques to elicit, improve, and apply metacognition in LLMs, and findings and implications of ongoing research. We also discuss applications, open questions and challenges, and promising directions for future work. Our aim is to provide a detailed and up-to-date review of this topic and stimulate meaningful research and discussion. An organized list of papers can be found at this https URL.

---


### 199. [Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation](https://arxiv.org/abs/2607.11886)

**<font color=#1a73e8>作者：</font>** Runhui Huang, Qihui Zhang, Zhe Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose SpectraReward, a training-free reward function that turns pretrained MLLMs into off-the-shelf reward models for image-generation reinforcement learning. Instead of asking the MLLM to judge a generated image or answer decomposed verification questions, SpectraReward measures how well the original prompt can be recovered from the generated image through a single image-conditioned, teacher-forced forward pass. We use the average image-conditioned prompt log-likelihood as the reward, directly reusing the MLLM's pretrained image-text alignment ability without preference labels, reward-model fine-tuning. We further introduce Self-SpectraReward, a special case for unified multimodal models where the policy's own understanding branch serves as the reward model for its generation branch, forming a closed-loop self-improving framework without external reward models or external knowledge. Extensive experiments validate SpectraReward through a broad image-generation RL study covering two diffusion models, three RL algorithms, nine reward MLLM backbones from four MLLM families spanning 4B to 235B parameters, and five out-of-distribution text-to-image benchmarks. Results show that both SpectraReward and Self-SpectraReward significantly and consistently improve generation performance and outperform prior MLLM-derived reward training methods. Further analysis reveals that larger reward MLLMs are not always better, while Self-SpectraReward can match or surpass much larger external reward models, suggesting that reward-policy alignment is a key factor for effective image-generation RL. Project Page: this https URL

---


> [!TIP]
> 当前位于：**151-199**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-199**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
