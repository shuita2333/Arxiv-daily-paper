# 🧠 大模型相关研究 | 2026年06月23日

> 本类共 **328** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-328](./part-07.md)

---

### 251. [Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents](https://arxiv.org/abs/2606.22953)

**<font color=#1a73e8>作者：</font>** Aman Mehta, Anupam Datta  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents depend on context management: systems compress, summarize, and evict old tokens so tasks can continue beyond finite windows. That is safe only when dropped information is no longer needed or has been internalized. Plans are the stress case: they are written early, used for many steps, and first to be evicted. We introduce replay pairing, a diagnostic that runs the same trajectory with and without the plan in history and measures hidden-state cosine distance. On Llama-3.1-70B, plan signal spikes to 0.453 one step after the plan, then falls 4.1x in a single action-observation step; HotpotQA falls 12.4x. This is evidence that standard LLM agents do not carry plans forward as persistent state, and instead depend on the plan remaining in context. A layer-L32 probe detects this decay as a diagnostic, not as proof that it reads plan content itself. Reasoning models add a measurement confound: their `<think>` traces re-derive plan content, so standard stripping leaves plan evidence in the stripped condition. We name this the reasoning-trace confound and fix it with strict stripping, which removes prior `<think>` blocks from the stripped run only. It recovers +163% of the step+1 signal in-sample and +153% held out, while not meaningfully changing non-reasoning Llama (+4.8%). On DeepSeek-R1-Distill-Llama-70B, a Llama-trained probe transfers at AUROC 0.748 (p=6e-4), while R1-specific probes reach 1.000, suggesting R1 encodes plan signal in a different hidden-state direction. Finally, a compression stress test shows the practical cost: naive plan eviction cuts ALFWorld success by 34.7pp, while probe-gated re-surfacing does not recover it. The contribution is a measurement and stress-test framework showing that agent-critical information can be context-resident rather than persistent. Context management is load bearing, but plan protection alone is not enough.

---


### 252. [Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval](https://arxiv.org/abs/2606.22955)

**<font color=#1a73e8>作者：</font>** Wangding Xia, Ye Du, Jiashi Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large-scale pretrained foundation models have revolutionized general medical screening, but often falter on rare diseases because such conditions are underrepresented in real-world clinical datasets. While retrieval-augmented diagnosis attempts to mitigate this, conventional static methods frequently succumb to the hubness problem, retrieving visually similar but semantically incorrect common diseases. To address this, we propose Evo-RAD, a self-evolving agentic framework that transforms evidence acquisition into a dynamic decision-making task. We formulate retrieval as a Markov Decision Process (MDP) where a graphbased agent observes the reference set state and executes actions to purge discordant evidence (DELETE), acquire pathologically consistent samples (INSERT), or conclude the evolution (TERMINATE). Optimized via Group Relative Policy Optimization (GRPO) with a homogeneityaware reward, the agent learns to maximize the diagnostic homogeneity of the support reference set. Experiments on retinal disease benchmarks show that Evo-RAD substantially improves rare-disease diagnosis, outperforming retinal foundation models by +21.04%, while also surpassing retrieval-based and parameter-efficient fine-tuning methods by +3.56%. Code is available at this https URL.

---


### 253. [PG-MAP: Joint MAP Optimization for Inference-Time Alignment of Diffusion and Flow-Matching Models](https://arxiv.org/abs/2606.22958)

**<font color=#1a73e8>作者：</font>** Ruolan Sun, Pawel Polak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inference-time alignment of pretrained text-to-image models is typically performed along a single control axis, such as classifier-free guidance, attention editing, or reward-based latent perturbations. This limitation prevents modeling joint dependencies between conditioning and latent variables and hinders transfer across generative transports. We propose PG-MAP, a training-free framework that formulates inference-time alignment as a trajectory-level Gibbs-MAP / proximal energy optimization over the conditioning $c$ and latent state $z_t$ via a forward-consistency coupling, optionally guided by a frozen preference reward. This joint formulation enables coordinated updates across modalities while remaining compatible with both diffusion and flow-matching models through transport-specific adaptations. Across diffusion backbones (SD~1.5, SDXL), PG-MAP consistently improves alignment metrics such as PickScore and Aesthetic, and can be effectively combined with tuned classifier-free guidance to achieve the strongest overall performance. On flow-matching models (SD3.5-medium), the framework reduces to a latent-only variant, achieving $\mathbf{91.9\%}$ PickScore and $75.7\%$ HPS win rates against a static baseline, with controlled experiments ruling out noise-related artifacts. Human evaluations further confirm consistent preference over strong baselines, including tuned CFG and compute-matched universal guidance. Finally, an oracle-routing analysis shows that the relative importance of conditioning and latent optimization depends on prompt types, surfacing further headroom that a per-prompt selector could exploit.

---


### 254. [Concept Alignment Contrast and Long-Short Prompt Memory for Test-Time Adaptation of SAM3 in Medical Image Segmentation](https://arxiv.org/abs/2606.22963)

**<font color=#1a73e8>作者：</font>** Yubo Zhou, Jianghao Wu, Ping Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Concept segmentation models like Segment Anything Model 3 (SAM3) show strong generalization on natural images, yet their performance degrades in medical imaging due to the domain gap caused by different imaging principles and styles. Test-Time Adaptation (TTA) is essential for improving the testing performance by updating the model on the fly without annotations. However, existing vision-language TTA methods are mainly driven by image-level uncertainty minimization, which does not necessarily reflect region-level semantic correctness in medical segmentation. Moreover, they often lack mechanisms to maintain stability in continual one-pass adaptation, leading to limited performance when reliable dense supervision is missing for segmentation. To address these issues, we propose Concept Alignment Contrast and LongShort Prompt Memory for Test-Time Adaptation (CM-TTA) of SAM3 for medical images. First, for a test sample with multiple augmentations, we introduce a novel Concept Alignment Contrast (CAC) metric, which leverages textual-visual semantic consistency to robustly evaluate prediction quality to select the best augmented view as the supervision. Second, to balance rapid and stable adaptation, we design a Long-Short Prompt Memory (LSPM) module. The short memory dynamically fuses recent prompts based on CAC scores for agile local adaptation, while the long memory maintains a stable global prompt to generate enhanced pseudo-labels. Finally, a Densely Supervised Prompt Update (DSPU) strategy is proposed to optimize the prompt embeddings with enhanced pseudo labels as dense supervision. Extensive experiments on prostate and skin lesion segmentation demonstrate that our CM-TTA framework significantly outperforms existing methods for TTA of SAM3.

---


### 255. [Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models](https://arxiv.org/abs/2606.22966)

**<font color=#1a73e8>作者：</font>** Linghan Chen, Kaiyan Ji, Minyu Guo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many recent vision-language-action (VLA) policies adopt an imagine-then-act design. A world-action model (WAM) first imagines a short future as a latent trajectory z~, on which the action is then conditioned. We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. A downstream oracle, such as a safety gate, a visual model-predictive-control (MPC) planner, or an imagine-then-check verifier, consumes z~ as a prediction of the future. The robustness of the policy therefore does not entail the robustness of systems that rely on the WAM. The underlying phenomenon is an asymmetry. Corrupting the imagination is easy, since it requires only displacing z~ from its natural-future manifold. Steering it precisely is hard, since it must reach a specified on-manifold target. We adopt a capability-based threat model with an L-infinity-bounded observation perturbation. The attacker applies projected gradient descent through the fully differentiable observation-to-imagination map. The same off-manifold property motivates a parameter-free denoiser detector. We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. Untargeted corruption is roughly 60x stronger than random and is detected at AUC 1.0. Targeted control remains bounded. An adaptive attacker evades detection only by forgoing corruption. The reactive policy remains robust to corrupted imagination. A native imagination-driven MPC, however, exhibits the first adversary-specific task failure (at epsilon=0.01, success 0.70 versus 0.05; Fisher p < 10^-4).

---


### 256. [When Preferences Fail to Become Incentives: A Utility-Behavior Gap in Large Language Models](https://arxiv.org/abs/2606.22974)

**<font color=#1a73e8>作者：</font>** Yujun Zhou, Christopher M. Ackerman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work on preference elicitation in large language models (LLMs) has demonstrated that, when given a series of choices between two outcomes, LLMs reveal a coherent, model-specific utility structure. Notably, this structure often includes preferences that the models' trainers did not intend, such as valuing people of some nationalities above others, raising the possibility that LLMs might be forming emergent, misaligned goals, which, if true, would have major safety implications. However, the choice paradigms in which these preferences are observed are not reflective of real-world situations in which misaligned behavior would be a practical concern. Therefore, we design an experimental paradigm to probe whether these preferences serve as motivations for LLM behavior in realistic scenarios. First, we reproduce prior findings on consistent preference elicitation. Next, we create a set of common writing tasks - essays, grant proposal abstracts, incident postmortems, and translations - where quality can be assessed by a blind, independent LLM judge panel. Then, we demonstrate that LLMs can be motivated via direct exhortation and other explicit cues to modulate their output quality on these tasks. Finally, we probe whether utilities inferred from explicitly reported preferences can shift output quality on these tasks by offering LLMs high-utility incentives for high-quality outputs. In all tasks, across all models tested, offering LLMs outcomes that they report in the choice paradigm as being highly preferred does not lead them to create higher quality outputs than offering them dispreferred outcomes, or even no outcomes at all. We conclude that the existence of coherent preferences as demonstrated in choice paradigms should not be taken as evidence that those preferences have incentive value for the models or affect their behavior in other contexts.

---


### 257. [TaLK: Text-attributed Graph Dataset Distillation via Coupling Language Model with Graph-Aware Kernel](https://arxiv.org/abs/2606.22975)

**<font color=#1a73e8>作者：</font>** Yeongho Kim, Yeonje Choi, Kijung Shin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-attributed graphs (TAGs) are widely used in many real-world domains, and learning on TAGs requires jointly modeling text semantics and graph structure. A standard approach for modeling TAGs is to combine a language model (LM) and a graph neural network (GNN), but joint training is computationally expensive and difficult to scale. Dataset distillation is a promising way to reduce training costs, but existing methods are not well suited to TAGs because they are typically designed for a single modality or still require repeatedly training expensive LM-GNN models on the full dataset during distillation. To address this, we propose TaLK, an effective dataset distillation method for TAGs that couples an LM with a graph-aware neural tangent this http URL design enables efficient dataset distillation, avoiding repeated joint training on the full dataset while reflecting both textual and structural information for effective TAG this http URL on multiple TAG benchmarks show that TaLK consistently outperforms existing baselines and achieves up to 97% of full-dataset performance with only 1% synthetic data.

---


### 258. [StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs](https://arxiv.org/abs/2606.22977)

**<font color=#1a73e8>作者：</font>** Youxin Zhu, Yixuan Ding, Peng Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Statistical analysis is a broad, complex field requiring both domain knowledge and tool proficiency. While prior work has evaluated large language models (LLMs) in this domain, existing benchmarks remain limited in scope and format. To bridge this gap, we introduce StatABench (Statistical AnalysisBenchmark), a benchmark designed to systematically assess LLMs' statistical analysis capabilities. StatABench comprises two complementary components: Stat-Closed, containing 404 questions across 18 statistical topics in multiple formats (multiple-choice, fill-in-the-blank, decision-making, and practical application), and Stat-Open, featuring 30 complex open-ended modeling tasks adapted from professional competitions. We evaluate diverse LLMs using the LangChain MCP framework and multiple data science agents, and assess Stat-Open solutions via a validated LLM-as-Judge protocol. Experiments show that even GPT-5.1 achieves only 68.6% on Stat-Closed, while the best open-source model reaches 60.6%. On Stat-Open, the top agent framework scores 61.86 on average. These results reveal the gap between current LLMs and reliable statistical analysis, highlighting persistent challenges in tool-grounded reasoning, methodological decision-making, and end-to-end statistical modeling.

---


### 259. [Predicate Importance Estimation and Decoupled Rationale-Score Distillation for Entity Alignment](https://arxiv.org/abs/2606.22992)

**<font color=#1a73e8>作者：</font>** Keunha Kim, Yoonjin Jang, Hyeon-gu Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs (KGs) are increasingly used as structured context for Large Language Models (LLMs), but industrial KG-RAG systems often need to integrate public and domain-specific KGs constructed from heterogeneous databases. This integration relies on Entity Alignment (EA), where lexical matching alone is insufficient under predicate-name variation and incomplete local neighborhoods. We address EA for KG integration by constructing a pairwise EA dataset and proposing two complementary modules: Predicate Importance Estimation (PIE) and Decoupled Rationale-Score Distillation (DRSD). PIE is a compact embedding-based approach that removes the subject information from each 1-hop triple, encodes the resulting subjectless triples, and aggregates them with learnable predicate-importance weights to build predicate-aware entity embeddings. DRSD trains a distilled small language model (SLM) with pseudo-answers produced by a teacher LLM through distinct prompts. By converting binary EA labels into text-based supervision and decoupling confidence-score estimation from label-consistent rationales, DRSD enables the SLM to learn task-specific reasoning while retaining a less label-biased confidence signal. Experiments show that PIE and DRSD improve EA classification. Moreover, because DRSD decouples confidence-score estimation from the decision, a discrepancy between the two flags an uncertain prediction for human review, thereby enabling a practical discrepancy between automatic acceptance and human-in-the-loop verification.

---


### 260. [Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning](https://arxiv.org/abs/2606.22995)

**<font color=#1a73e8>作者：</font>** Yunan Wang, Minghui Song, Zihan Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group-based Reinforcement Learning (RL) has significantly enhanced Large Language Models (LLMs) in agentic scenarios. To achieve finer-grained policy updates, recent agentic RL frameworks have shifted from trajectory-level to step-level training. However, long-horizon agentic RL suffers from severe reward sparsity and delay, as feedback is often deferred for dozens of interaction steps. While existing step-level frameworks refine training granularity, their credit assignment remains coarse-grained and still treats agent exploration as isolated, linear trajectories. This oversimplified perspective ignores the inherent graph structure of state transitions, leading to high-variance state-value estimation and myopic, localized credit assignment. To overcome these critical bottlenecks, we propose Group-Graph Policy Optimization (G2PO), a novel group-based RL algorithm tailored for multi-turn agentic tasks. G2PO explicitly transforms linear interaction trajectories into a global state-transition graph. By aggregating identical observations across different trajectories, we introduce group-aggregation state-value estimation that reduces sampling variance and trajectory-dependent bias. Furthermore, we redefine agent actions as transitions between state nodes and propose an edge-centric advantage estimation strategy. By globally standardizing Temporal Difference (TD) errors across the entire graph, G2PO explicitly identifies and prioritizes critical transitions that drive absolute task progress. Extensive experiments on representative long-horizon benchmarks-WebShop, ALFWorld, and AppWorld-demonstrate that G2PO substantially outperforms state-of-the-art prompt-based and RL baselines, achieving remarkable success rate improvements of up to 22.2% over GRPO.

---


### 261. [Black-Box Continual Learning for Vision-Language Models](https://arxiv.org/abs/2606.22999)

**<font color=#1a73e8>作者：</font>** Yuting Li, Weihang Fang, Haoyuan Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of Vision-Language Models (VLMs) in dynamic environments necessitates the ability to learn continuously without forgetting. However, traditional continual learning (CL) settings often rely on white-box paradigms, which is increasingly invalidated by the shift toward cloud-hosted models. In this paper, we introduce Black-CL, a more realistic benchmark for VLMs that enforces three primary real-world challenges: weight and architecture inaccessibility, constrained computation, and task-agnostic inference. The learner can query only output embeddings or logits, with no gradient flow through or structural modification of the backbone. Current CL methodologies, which rely on backbone backpropagation or complex parameter expansion, are fundamentally incompatible with these constraints. Under this setting, we propose BETA, a simple yet effective baseline built on the key insight that solely optimizing textual prototypes can navigate the complexities of CL. BETA integrates three core components: Semantic Projection Accumulation (SPA) for incremental knowledge acquisition, Latent Distribution Replay (LDR) for anchoring the embedding space against catastrophic forgetting, and Test-Time Prototype Adaptation (TTPA) for dynamic, instance-aware boundary refinement. Extensive experiments across ten diverse datasets and various backbones demonstrate that BETA significantly outperforms existing black-box tuners. Remarkably, with only 0.05 M trainable parameters, a 180--3000$\times$ reduction compared to competitive methods, BETA achieves performance on par with or even exceeding white-box CL methods. We believe Black-CL and BETA provide a foundational framework for future advancements in continual learning and accelerates the transition of continual learning from academia to real-world systems.

---


### 262. [A Stackelberg Framework for Resource-Aware LLM Agents: Learning, Repair, and Conditional Guarantees](https://arxiv.org/abs/2606.23026)

**<font color=#1a73e8>作者：</font>** Baoxun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate as multi-turn systems that must allocate context, prompt verbosity, and tool access under finite computational budgets. Static thresholds are simple, but they are brittle under heterogeneous tasks and evolving session states. We formulate resource governance as a contextual Stackelberg game: a controller commits to a quality target and a cost incentive, while an executor responds with resource actions over context, prompting, and tool usage. We learn a conditional response model, optimize a leader policy against that model, and repair the resulting policy using real-API calibration and projection onto an empirically selected action set. For the restricted game, we establish conditional guarantees for equilibrium existence, follower-response stability, safe-set projection, and transfer from a surrogate environment to the real environment under bounded value error. The primary real-API experiment comprises 300 evaluated turns. Relative to a conservative baseline, the selected repaired controller reduces mean token cost by 17.4% (Welch $p=0.022$), while the measured quality difference is not statistically significant ($p=0.44$). The theoretical results are conditional and the experiments do not estimate their regret or transfer constants; consequently, the evidence establishes a promising repaired operating point, not a certified real-system equilibrium.

---


### 263. [Have You Ever Seen Them? Entity-level Membership Inference through Interrogating Large Language Models](https://arxiv.org/abs/2606.23030)

**<font color=#1a73e8>作者：</font>** Yiran Zhu, Ziqi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) raise growing concerns about privacy leakage and copyright compliance. Membership inference is a key tool for assessing such risks, but existing studies mainly focus on whether specific samples or sample-based data units are used for training. We argue that LLMs exhibit a human-memory-like behavior: an LLM may not memorize a specific sample verbatim, yet it can accumulate and reveal knowledge about a real-world entity from scattered mentions. This analogy motivates us to examine whether an LLM can be interrogated like a human interviewee to reveal its exposure to entity-related information. Motivated by this question, we propose entity-level membership inference, which determines whether information related to a target entity is used in LLM training. We study this task in the practical label-only black-box setting, where only generated texts are observable. We formalize the task under clue, input, and model constraints, establish the necessary and sufficient conditions for its feasibility, and instantiate five interrogation strategies based on this formalization. The strategies use limited entity clues to construct prompts, elicit entity-related responses, and infer membership from semantic features among the generated texts. We construct entity-level datasets and adapt state-of-the-art sample-level label-only methods to the entity-level setting as baselines. Experiments on person entities show that our methods achieve AUC up to 0.97 and bring gains of 6.0%--17.5% in Balanced Accuracy over the best adapted baseline.

---


### 264. [IPO Finance Agent: Evaluation of LLM Financial Analysts beyond Finance Agent v2, with Automated Rubric Generation -- the Case of the SpaceX (SPCX) IPO](https://arxiv.org/abs/2606.23032)

**<font color=#1a73e8>作者：</font>** Mostapha Benhenda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Finance Agent v2 (by Vals AI) has emerged as the reference benchmark for evaluating both Anthropic Claude and OpenAI ChatGPT frontier language models on financial tasks. However, it narrowly deals with periodic reporting from publicly traded companies (SEC 10-K and 10-Q filings), and its agentic harness relies on naive, unenriched chunk retrieval. Neither the task design nor the retrieval approach addresses the distinct challenges of IPO due diligence. SEC S-1 filings combine historical financial statements, governance structures, pro forma and common-control accounting treatments, capital-formation narratives, and underwriting-sensitive risk disclosures within substantially longer documents than typical periodic filings. That is why we introduce IPO Finance Agent, which extends the Finance Agent v2 framework along two directions: task domain and retrieval architecture. During our experiments, the original Finance Agent v2 harness basically failed to deliver any output related to the SpaceX S-1 filing, due to document length. We therefore had to improve the agentic harness with contextual retrieval, a more realistic and industry-standard approach for long documents. We also built a dataset of 1,000 IPO-diligence questions, and publicly release 70 questions on the SpaceX (SPCX) S-1 filing to support reproducibility, while the remainder are held private to guard against benchmark contamination. In addition, we introduce an evaluator-optimizer pipeline to automatically generate evaluation rubrics for the benchmark: candidate facts are extracted from an ensemble of independently-generated model answers to each question, consolidated into draft criteria, then automatically audited for omissions, hallucinations, mistiered items, and redundancy, with LLM feedback driving iterative repair, targeted enrichment, and deduplication. Human experts only review final rubrics before deployment. Results show that the best-performing evaluated model, Alibaba Qwen 3.7 Max, reaches 79.4% accuracy at $0.30 per query, and the most cost-efficient model on the resulting Pareto frontier, Xiaomi MiMo-2.5 Pro, reaches slightly lower accuracy (76.8%) at $0.05 per query. Both exceed the current Finance Agent v2 leaderboard ceiling-Google Gemini 3.5 Flash at 57.9% for $2.51 per querywhile undercutting even FABv2's cheapest entry (MiniMax M3: 48.3% at $0.32) on cost-efficiency. Code and data are released on GitHub: this https URL

---


### 265. [EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning](https://arxiv.org/abs/2606.23038)

**<font color=#1a73e8>作者：</font>** Hongxin Ding, Baixiang Huang, Yue Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric-based rewards offer interpretable and fine-grained optimization signals for reinforcement learning in open-ended tasks where verifiable answers are unavailable. However, pre-constructed rubrics remain static throughout training, creating a fundamental mismatch with the evolving policy: fixed criteria gradually lose discriminative power as the model improves, leading to reward saturation and potential hacking. Recent dynamic rubric methods partially address this but rely on external frontier models or ground-truth answers, and update rubrics only at coarse granularity. We propose EvoRubrics, a co-evolutionary RL framework where a Policy LLM and a Rubric Generator jointly improve through adversarial interaction within each training step. As the policy improves under the rubric generator's guidance, the rubric generator adapts its criteria to remain discriminative and informative, enabling evaluation to track the policy in real time and naturally inducing an automatic curriculum. Experiments show that EvoRubrics consistently outperforms static and dynamic rubric baselines across benchmarks. The learned Rubric Generator further generalizes as a transferable reward model. Notably, even a fully self-supervised variant without any external supervision achieves meaningful gains, suggesting that co-evolution between generation and evaluation alone can provide sufficiently rich learning signals. Our code is publicly available at this https URL.

---


### 266. [SPAR: Semantic-Pixel Self-Alignment and Adaptive Routing for Unified Multimodal Models](https://arxiv.org/abs/2606.23041)

**<font color=#1a73e8>作者：</font>** Hongxiang Li, Hongxu Chen, Chenyang Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable success in visual understanding but remain constrained in visual generation due to the fundamental feature discrepancy between semantic perception and pixel-level reconstruction. Bridging this gap requires overcoming two core challenges: endowing semantic encoders with high-fidelity reconstruction capabilities, and effectively aligning generative models with semantic spaces without relying on external teachers. To this end, we propose a novel unified multimodal framework featuring \textbf{S}emantic-\textbf{P}ixel self-alignment and \textbf{A}daptive \textbf{R}outing (\textbf{SPAR}). First, to reconcile semantic perception with pixel-level reconstruction, we introduce an asymmetric dual-stream unified tokenizer. A lightweight semantic stream anchors discriminative features, while a Transformer-augmented pixel stream recovers fine-grained visual details into a unified compact latent space. Second, to eliminate external dependencies, we propose a self-aligned generation paradigm that natively leverages this optimized tokenizer as an internal alignment teacher for the diffusion model. Furthermore, to facilitate flexible multimodal interaction within this unified space, we introduce Dynamic Token Routing, which enables each token to adaptively aggregate multi-layer MLLM features based on its distinct semantic demands. Extensive experiments demonstrate that SPAR establishes the state-of-the-art for unified architectures, achieving exceptional generation and reconstruction quality while preserving foundational visual understanding capabilities.

---


### 267. [Training Open Models for Agentic Phone Use](https://arxiv.org/abs/2606.23049)

**<font color=#1a73e8>作者：</font>** Zhengyang Tang, Xin Lai, Pengyuan Lyu 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Phones are becoming an important execution surface for general-purpose agents, but training open models for reliable phone use remains difficult because the environment that matters at deployment, real devices running real apps, is slow, stateful, side-effectful, and hard to reset or verify, while scalable mock environments only approximate real behavior. We present PhoneBuddy, a training recipe and open-model line for agentic phone use that combines a real-app environment with a mock-app environment, PhoneWorld, which reconstructs runnable mock apps from real GUI usage structure. PhoneBuddy first builds a shared supervised fine-tuning stage from trajectories collected in both environments, then compares real-app RL against mixed RL across both environments. Across a 150-task human evaluation on real phones spanning apps, mini-apps, and cross-app workflows, task success rate improves from 36.67\% after supervised fine-tuning to 40.67\% after real-app RL and 45.33\% after mixed RL. On AndroidWorld, the same progression rises from 60.3\% to 77.2\% to 83.2\%. These results show that mock-app training is not a replacement for real-app RL, but a complementary source of scalable, resettable, and automatically checked interaction. The gains are strongest on app and mini-app tasks, while long-horizontal cross-app workflows remain an important open challenge.

---


### 268. [Unlimited OCR Works](https://arxiv.org/abs/2606.23050)

**<font color=#1a73e8>作者：</font>** Youyang Yin, Huanhuan Liu, Qunyi Xie 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However, the downside is equally evident: as the output sequence lengthens, the accumulated KV cache drives up memory consumption and progressively slows down generation. This stands in stark contrast to humans, who exhibit no such decline in efficiency during long-horizon copying tasks. In this technical report, we propose Unlimited OCR, a model designed to emulate human parsing working memory. Taking DeepSeek OCR as the baseline, we replace all attention layers in the decoder with our proposed Reference Sliding Window Attention (R-SWA), which reduces attention computation costs while maintaining a constant KV cache throughout the entire decoding process. By combining the high compression rate of DeepSeek OCR's encoder with our constant KV cache design, Unlimited OCR can transcribe dozens of pages of documents in a single forward pass under a standard maximum length of 32K. More importantly, R-SWA is a general-purpose parsing attention mechanism - beyond OCR, it is equally applicable to tasks such as ASR, translation, etc. Codes and model weights are publicly available at this http URL.

---


### 269. [Attention-Spectrum Regularization for Replay-Free Continual Multimodal LLMs](https://arxiv.org/abs/2606.23063)

**<font color=#1a73e8>作者：</font>** Chuangxin Zhao, Canran Xiao, Siyuan Ma 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are increasingly required to adapt to non-stationary streams of visual domains, question types, and user instructions, yet continual fine-tuning often causes severe forgetting of previously acquired multimodal skills. Existing continual vision-language methods mainly preserve outputs, replay data or pseudo-data, regularize embedding geometry, or allocate task-specific parameters, but they provide limited control over how internal cross-modal attention patterns supporting old skills drift during adaptation. We propose Attention-Spectrum Regularization (ASR), a replay-free continual learning framework that preserves skill-conditioned structures of cross-modal attention. ASR treats cross-attention maps as two-dimensional signals, summarizes their scale and directional properties into compact spectral statistics, and stores only skill-wise prototype distributions instead of replaying past image-question pairs, generated pseudo-examples, or old-stage teacher snapshots. In later stages, a phase-invariant spectral regularizer constrains harmful drift of these prototypes while allowing instance-level attention to adapt to new tasks. We provide theoretical analysis showing that skill-conditioned spectral drift controls forgetting under a spectral sufficiency assumption, and that Fourier power spectra are stable to spatial translations and bounded perturbations. Experiments on continual VQA and multimodal instruction-tuning benchmarks, including VQA v2, VQACL, CLT-VQA, CoIN, and UCIT, show that ASR consistently improves final performance and reduces forgetting over strong replay-, regularization-, and adapter-based baselines. Preserving skill-level attention structure is an effective and lightweight mechanism for continual MLLMs. Code is available at this https URL

---


### 270. [FlowTrain: Flow-Based Decoupled Training for Industrial-Grade Vision-Language Models](https://arxiv.org/abs/2606.23087)

**<font color=#1a73e8>作者：</font>** Zhida Jiang, Zhaolong Xing, Yang Pei 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial-grade distributed training of vision-language models (VLMs) remains far less efficient than that of unimodal LLMs. Existing solutions either follow a monolithic design that assigns uniform parallelism to heterogeneous modules or adopt a disaggregated deployment that separates modules while executing them as a batch-synchronized pipeline. In this paper, we highlight that the above solutions are still not sufficient, and VLM training can be further decoupled. To this end, we present FlowTrain, a flow-based decoupled training framework that reformulates VLM training as a producer-consumer dataflow coordinated through a unified memory pool. The encoder and backbone can progress independently over a global virtual address space. Since this execution decoupling fundamentally changes the optimization objective of allocation and scheduling, FlowTrain further introduces a heterogeneous parallel allocator that assigns module-specific parallelism strategies by solving a throughput matching problem. The dynamic packing scheduler is used to construct balanced microbatches at runtime according to the actual LLM-side computation cost. Extensive experiments on real-world workloads show that FlowTrain achieves over 50% MFU and up to 1.7x throughput improvement, narrowing the efficiency gap to LLM-only training.

---


### 271. [PIVOTSBench: Evaluating Fine-Grained Interpersonal Relationship Reasoning in Multimodal Large Language Models](https://arxiv.org/abs/2606.23092)

**<font color=#1a73e8>作者：</font>** Shuxiang Zhang, Yiting Yin, Wenxuan Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans possess an innate ability to understand fine-grained interpersonal relationships, which is central to everyday social interactions. Although such reasoning is inherently multimodal, it remains largely unexplored by existing multimodal large language models (MLLMs). To address this gap, we introduce PIVOTS, the first benchmark built from Social-IQ 2.0 and YouTube data to evaluate MLLMs' ability to predict bidirectional interpersonal relationship dimensions grounded in established psychology research. In addition, PIVOTS includes auxiliary tasks that assess models' ability to identify and leverage the critical visual cues underlying such predictions. We evaluate both proprietary and open-source MLLMs and conduct detailed ablation studies to analyze the effects of visual modalities and explicit social role information in conversational utterances. We further examine how joint and pairwise prediction settings benefit MLLMs in scoring bidirectional PIVOTS dimensions. Project page and resources: this https URL .

---


### 272. [ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation](https://arxiv.org/abs/2606.23104)

**<font color=#1a73e8>作者：</font>** Chen Lin, Kedi Chen, Wei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) improves LLM reasoning by training a student model on its own generated outputs, but standard OPD treats all student-generated outputs (SGOs) equally regardless of their informativeness. We observe a consistent asymmetry in controlled filtering experiments: in both OPD and on-policy self distillation (OPSD), training only on incorrect SGOs outperforms training only on correct ones. Our further analysis suggests that models trained on correct-only SGOs tend to generate shorter reasoning traces and show weaker reflection behavior, while incorrect SGOs better preserve exploratory reasoning near the model's capability boundary. To exploit this signal without requiring full answer-containing rollouts, we introduce ReNIO, which Reweights Negative trajectory Importance for LLM On-policy distillation. By using the student-to-teacher probability ratio, ReNIO identifies pivotal tokens leading to wrong reasoning traces and aggregates their information into a normalized sample weight, inherently assigning larger weights to likely negative trajectories without observing the correctness of final-answer. Since Re-NIO only uses prefix-conditioned token probabilities, it preserves OPD's prefix training advantage over full-rollout reinforcement learning. Across both mathematical reasoning and code generation tasks, ReNIO improves both OPD and OPSD, with representative relative gains of up to 8.90% for Qwen3-1.7B and 10.00% for R1-Distill-Qwen-7B on mathematical reasoning benchmarks. Code repo: this https URL.

---


### 273. [Compression and Retrieval: Implicit Memory Retrieval for Video World Models](https://arxiv.org/abs/2606.23105)

**<font color=#1a73e8>作者：</font>** Zhan Peng, Jie Ma, Huiqiang Sun 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models hold promise for simulating interactive environments, yet maintaining consistent long-term memory across complex camera trajectories remains a critical challenge. Existing methods typically rely on computationally expensive context scaling or rigid heuristic retrieval mechanisms, which lacks generalization to varying camera trajectories and environments. In this paper, we propose Compression and Retrieval (CaR), an attention-driven implicit memory retrieval mechanism to overcome these limitations. By injecting viewpoint information via positional encoding, our method performs flexible memory retrieval through attention computation. To efficiently process extended contexts with minimal computational overhead, we further introduce a lightweight context compression network. Furthermore, we construct SceneFly, a large-scale synthetic dataset featuring realistic camera trajectories and frame-level annotations to train and evaluate long-horizon video world models. Extensive experiments demonstrate that our approach achieves state-of-the-art results on established benchmarks and exhibits strong generalization to open-domain scenes.

---


### 274. [Temporal-Spectral Alignment with Frequency Adaptation for Source-Free Time-Series Adaptation](https://arxiv.org/abs/2606.23120)

**<font color=#1a73e8>作者：</font>** Shichang Meng, Linquan Wu, Xuan Ai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The goal of source-free domain adaptation (SFDA) for time-series data is to transfer knowledge from a pre-trained source model to an unlabeled target domain without requiring access to source data, while addressing feature shift and temporal drift inherent in the signals. Although existing approaches have explored temporal dynamics in unsupervised source-free adaptation, they largely overlook spectral shifts in time-series data. Towards this end, we propose a novel approach termed temporal-Spectral Alignment with Frequency Adaptation (SAFA) for source-free time-series domain adaptation. Specifically, we first model the source domain at multiple scales by jointly capturing temporal dependencies and spectral characteristics. To adapt time-series data in the target domain, we introduce a trainable frequency adaptation module that modulates the phase and amplitude of target signals in the frequency domain to align them with the source distribution. Extensive experiments on multiple benchmark datasets demonstrate the efficacy and robustness of SAFA.

---


### 275. [PRIDE: Privileged Information-enhanced Distillation for Empathetic Dialogue Generation](https://arxiv.org/abs/2606.23124)

**<font color=#1a73e8>作者：</font>** Jiaqiang Wu, Zhouan Zhu, Shangfei Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have demonstrated significant capabilities in generating diverse and context-aware responses for empathetic dialogue. However, their computational demands severely limit their deployment in resource-constrained environments. While knowledge distillation offers a promising compression solution, it often fails to transfer the nuanced understanding essential for empathy, as it overlooks the implicit contextual cues that guide human connection. To bridge this gap, we propose a \textbf{pr}ivileged \textbf{i}nformation-enhanced knowledge \textbf{d}istillation method for \textbf{e}mpathetic dialogue generation (PRIDE). Our method leverages privileged information, such as expert psychological annotations or future event summaries, which is available exclusively during training but unavailable at inference time. This allows us to transfer the teacher model's empathetic reasoning to smaller models without relying on extra inputs during deployment. Specifically, PRIDE has three key components: (1) An empathy-reasoning prompt that guides the teacher to explicitly decompose the empathetic process into understanding feelings and analyzing situations step-by-step; (2) A multi-source attention mechanism that directs the student to effectively integrate privileged information; (3) A dual-alignment loss that combines reversed Kullback-Leibler divergence and maximum mean discrepancy to ensure robust knowledge transfer at both logit and feature levels. Experiments on multi-modal and text-only datasets demonstrate that our method achieves competitive performance, and in some cases matches or even surpasses larger teacher models in terms of accuracy and semantic relevance.

---


### 276. [Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation](https://arxiv.org/abs/2606.23127)

**<font color=#1a73e8>作者：</font>** Julia Belikova, Rauf Parchiev, Evgeny Egorov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Procedural memory is increasingly used to improve LLM agents on recurring workplace tasks, yet its ability to produce reusable skills remains poorly understood. We introduce AFTER, a benchmark of 382 realistic enterprise tasks spanning six professional roles and 22 procedural skills, designed to evaluate how skills transfer across tasks, roles, and model backbones. The benchmark includes controlled evaluation settings for local improvement, cross-task transfer, cross-role transfer, and cross-model generalization. Experiments show that procedural memory delivers consistent gains in industrial workflows: a single refinement round improves aggregate performance by 3.7-6.7 points, while skills evolved from diverse multi-model execution traces achieve 73.1% cross-model test accuracy, outperforming all single-model trace sources. We further find that some skills generalize broadly across tasks and models, whereas others become specialized to role-specific workflows and lose effectiveness under transfer. These results provide practical guidance for building, evaluating, and deploying procedural memory systems in production agent platforms.

---


### 277. [T-VSS: Test-Time Visual Subspace Steering for Adversarial Robustness of Vision-Language Models](https://arxiv.org/abs/2606.23132)

**<font color=#1a73e8>作者：</font>** Jaehyuk Jang, Minseok Seo. Seungju Cho, Kangwook Ko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) achieve strong zero-shot recognition, but they remain highly vulnerable to adversarial perturbations. Recent test-time adaptations improve robustness without retraining, but they do not directly adapt the corrupted visual representation itself. Prompt-based methods adapt the learnable text prompts, while input-space methods optimize pixels or padding at test time. These approaches can improve predictions, but they do so through an indirect and expensive optimization path. We propose Test-time Visual Subspace Steering (T-VSS), a lightweight defense that performs test-time adaptation directly in the visual feature space. T-VSS first builds a sample-specific low-rank subspace from multi-view feature residuals anchored at the attacked image. It then learns a shared feature correction within this subspace using reliability-weighted entropy minimization. By constraining adaptation to a compact visual geometry, T-VSS steers attacked features toward more stable and discriminative predictions while avoiding noisy full-space updates. Experiments on fine-grained, ImageNet, and ImageNet-OOD benchmarks show that T-VSS improves adversarial robustness while maintaining competitive clean accuracy and better efficiency than prior test-time adaptations.

---


### 278. [Same question, different history: language, national identity, and credit in large language models](https://arxiv.org/abs/2606.23164)

**<font color=#1a73e8>作者：</font>** William Guey, Pierrick Bougault, Wei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Who invented the radio, Russia's Alexander Popov or Italy's Guglielmo Marconi? Was the telephone the achievement of Bell in the United States or Meucci in Italy? Does printing belong to China's Bi Sheng or Germany's Gutenberg? The answer depends not only on historical record but also on language and perspective.
We analyse eleven widely used large language models across 21 disputed inventions and discoveries, evaluated in twelve languages and 75,896 responses. While models generally acknowledge that credit is contested, query language systematically affects which claimant is surfaced. Lower-status claimants are more likely to appear when questions are asked in their associated language, whereas dominant Anglophone figures remain stable across languages.
These patterns persist after controlling for response length, model differences, historical prominence, and levels of national commemoration. Language thus acts as a switch that activates different national versions of the same history, producing systematically different national memories from the same question.
We interpret this as evidence that large language models function as distributed systems of cultural memory, where language conditions which histories become visible, contributing to a computational form of banal nationalism.

---


### 279. [DART: Draft-Agreement Routing for Training-Free Adaptive Thinking Budgets in Hybrid Reasoning Models](https://arxiv.org/abs/2606.23181)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Seongtae Hong, Seungjun Lee 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hybrid reasoning models can answer directly or spend extra tokens on extended thinking. A practical router should choose between these modes for each query, so easy problems avoid unnecessary reasoning and hard problems receive enough budget to finish the answer. Existing routers move in this direction, but they typically require labeled training data or fix thinking budgets up front, ignoring answer-level evidence from the model itself. We introduce DART, a training-free routing framework that samples two cheap no-think drafts, accepts direct answering when the drafts agree, and predicts a thinking budget from draft entropy when they disagree. Across the main comparisons, DART preserves or improves always-thinking accuracy in most settings while reducing thinking-token use. On math reasoning, accuracy improves by up to $+$9.0 points on Olympiad-level problems while thinking tokens drop 15-69%. On code reasoning under execution-based equivalence, accuracy improves by up to +22.5 points while thinking tokens drop 51-63%. The Stage~1 signal extends across model scales (0.6B-32B), model families, and API-only hosted settings, with no labeled data and no gradient updates required.

---


### 280. [CFPO: Counterfactual Policy Optimization for Multimodal Reasoning](https://arxiv.org/abs/2606.23206)

**<font color=#1a73e8>作者：</font>** Zhangyuan Yu, Wanran Sun, Guangjing Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities in multimodal reasoning. However, prevailing reinforcement learning (RL) paradigms lack explicit counterfactual enhancement and causal learning mechanisms. This fundamental deficiency results in severe grounding failures, manifesting as a tendency to ignore visual evidence in favor of language priors or exhibiting hallucination drift during long chain-of-thought reasoning. To address this root cause, we propose CounterFactual Policy Optimization (CFPO), a novel framework that enforces causal consistency between visual perception and textual reasoning. CFPO introduces a cross-modal counterfactual enhancement mechanism, which regularizes the policy by maximizing the discrepancy between the model's predictions and those from a counterfactual state where critical visual cues are suppressed. This approach seamlessly integrates with standard algorithms like GRPO and DAPO without requiring external reward models or additional supervision. Extensive experiments demonstrate that CFPO significantly improves reasoning fidelity, achieving consistent gains of 3.17%-6.25% over standard RL baselines and 1.32%-2.13% over the state-of-the-art perception-aware method (PAPO). Code is available at this https URL.

---


### 281. [Leveraging AutoML for Sustainable Deep Learning: A Multi-Objective HPO Approach on Deep Shift Neural Networks](https://arxiv.org/abs/2606.23208)

**<font color=#1a73e8>作者：</font>** Leona Hennig, Marius Lindauer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep Learning (DL) has advanced various fields by extracting complex patterns from large datasets. However, the computational demands of DL models pose environmental and resource challenges. Deep Shift Neural Networks (DSNNs) present a solution by leveraging shift operations to reduce computational complexity at inference. Compared to common DNNs, DSNNs are still less well understood and less well optimized. By leveraging AutoML techniques, we provide valuable insights into the potential of DSNNs and how to design them in a better way. We focus on image classification, a core task in computer vision, especially in low-resource environments. Since we consider complementary objectives such as accuracy and energy consumption, we combine state-of-the-art multi-fidelity (MF) hyperparameter optimization (HPO) with multi-objective optimization to find a set of Pareto optimal trade-offs on how to design DSNNs. Our approach led to significantly better configurations of DSNNs regarding loss and emissions compared to default DSNNs. This includes simultaneously increasing performance by about 20% and reducing emissions, in some cases by more than 60%. Investigating the behavior of quantized networks in terms of both emissions and accuracy, our experiments reveal surprising model-specific trade-offs, yielding the greatest energy savings. For example, in contrast to common expectations, quantizing smaller portions of the network with low precision can be optimal with respect to energy consumption while retaining or improving performance. We corroborated these findings across multiple backbone architectures, highlighting important nuances in quantization strategies and offering an automated approach to balancing energy efficiency and model performance.

---


### 282. [MuPPET: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Conversations](https://arxiv.org/abs/2606.23217)

**<font color=#1a73e8>作者：</font>** Elena Sofia Ruzzetti, Cornelius Emde, Sangdoo Yun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly deployed in multi-party environments, handling sensitive personal data on behalf of individual users, for instance in group chats. When such an agent discloses private information, it reaches every group member at once. This risk is structurally harder to control than in one-to-one settings, as every piece of private information must be appropriate for every recipient in the group. Yet all existing contextual privacy benchmarks consider only single-interlocutor settings, leaving multi-party privacy risks unmeasured. We introduce MuPPET (Multi-Party Privacy Exposure Testing), a benchmark for contextual privacy in multi-party conversations. Our experiments show that models leak substantially more in multi-party settings than one-to-one evaluations suggest. Frontier models are vulnerable, and smaller open-weights models, often preferred for local deployment with sensitive data, even more so. Existing contextual privacy defences offer only partial protection, degrade utility, and do not resolve the underlying party-tracking problem.

---


### 283. [RS-Gen: A Multi-Stage Agentic Framework for Reasoning and Search-Augmented Image Generation](https://arxiv.org/abs/2606.23221)

**<font color=#1a73e8>作者：</font>** Feifei Bian, Zhimin Zheng, Wei Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent years have witnessed remarkable progress in image generation and editing, particularly regarding instruction following and visual fidelity. However, when handling ambiguous intentions, logical reasoning, and Out-of-Distribution (OOD) knowledge, existing image models often yield sub-optimal results due to a lack of deep reasoning capabilities and real-time external information. Although emerging unified understanding-and-generation models attempt to bridge this gap, they remain constrained by their intrinsic parameter scales and static knowledge gaps. Inspired by agentic paradigms, we propose RS-Gen: a plug-and-play, training-free, multi-stage image agentic framework. RS-Gen innovatively introduces a "Questioning-and-Solving" closed-loop mechanism to accurately identify logical issues and knowledge gaps, autonomously planning actions to bridge information deficits and execute deep logical reasoning. Extensive experiments demonstrate that RS-Gen significantly expands the capability boundaries of foundational image generation and editing models. Specifically, on the WISE Verified and RISEBench benchmarks, RS-Gen yields substantial absolute performance gains of 0.313 for Qwen-Image and 19.70 for Qwen-Image-Edit-2511, respectively, successfully elevating both to the state-of-the-art (SOTA) level among open-source models.

---


### 284. [HOLMES: Evaluating Higher-Order Logical Reasoning in LLMs](https://arxiv.org/abs/2606.23238)

**<font color=#1a73e8>作者：</font>** Yucheng Wu, Jundong Xu, Mingzhen Ju 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Logical reasoning is essential for reliable AI, yet existing benchmarks are largely first-order-logic-centric, focusing on object-level deduction over fixed predicates. This misses many realistic scenarios where models must reason over rules, predicates, functions, constraints, and decision procedures themselves. We introduce HOLMES (Higher-Order Logic Meets real-world Explainable Symbolic reasoning), the first real-world benchmark for higher-order symbolic reasoning in LLMs, containing 1379 instances. Built on higher-order logic, HOLMES pairs natural-language problems with HOL formalizations, ground-truth answers, verifiable reasoning traces, and fine-grained controllable reasoning factors across law and finance. Experiments show that current LLMs still struggle on HOLMES, with an average accuracy of only 50.64% and the best model reaching 59.54%. Our analyses further reveal that high final-answer accuracy can mask shortcut reasoning in conflict-resolution settings, while performance drops sharply under scope-conditioned and compositional reasoning. These findings identify higher-order symbolic reasoning as a key bottleneck for building reliable and verifiable LLMs. The project code and dataset are publicly available at this https URL.

---


### 285. [Unlocking In-Context Learning in Audio-Language Models from Decentralized Medical Audio](https://arxiv.org/abs/2606.23243)

**<font color=#1a73e8>作者：</font>** Ran Piao, Tsai-Ning Wang, Martijn den Dekker 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical audio diagnosis in low-resource settings requires models that identify conditions from minimal examples without large annotated corpora. We propose Federated Self-Contextualization (FSC), a multimodal language model framework for in-context clinical audio diagnosis across federated hospital clients. FSC constructs pseudo-label episodes via unsupervised clustering of audio representations, bypassing scarce real diagnostic labels, and enables contextual reasoning from support-query pairs. Our progressive three-stage pipeline first aligns audio embeddings with the language model via caption-based pretraining, then adapts it for episodic in-context inference through federated optimization. At test time, given a small labeled support set, the model diagnoses an unseen query through multimodal reasoning. On held-out respiratory and cardiac conditions, FSC achieves 71.6% accuracy in 2-way 2-shot evaluation, outperforming audio-language baselines by over 9%.

---


### 286. [Dynamic multi-agent deep reinforcement learning-based pricing and incentivization approach in multimodal transportation networks](https://arxiv.org/abs/2606.23257)

**<font color=#1a73e8>作者：</font>** Khadidja Kadem, Mostafa Ameli, Carlos Lima Azevedo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multimodal transportation systems, shared mobility services (SMSs) are promoted for their potential to enhance flexibility and reduce congestion. However, SMS demand is often concentrated in high-density areas, which can limit the effectiveness and accessibility for various commuter groups. This uneven integration challenges transportation system efficiency, especially in terms of emissions and spatial equity. Addressing these issues requires coordination among multiple stakeholders whose objectives frequently conflict. Whereas authorities aim to ensure sustainable and equitable mobility, SMS providers focus on revenue maximization, and travelers seek to minimize personal travel costs. This paper proposes a multi-agent deep reinforcement learning framework that captures these interactions through dynamic pricing and incentivization strategies for SMSs and public transport. The framework integrates two reinforcement learning (RL) agents: (i) a public authority that allocates spatio-temporal public transport incentives to improve equity, emissions, and efficiency, and (ii) an SMS provider that dynamically adjusts fares to optimize revenue. The agents interact with the transportation system and adapt strategies in response to evolving demand, congestion, and network conditions. Numerical experiments conducted over a three-hour morning peak period show that dynamic incentivization effectively reduces congestion peaks, lowers commuters' costs by around 20% and emissions by approximately 10%, while nearly doubling public transport profit and supporting a more equitable distribution of benefits. When combined with dynamic SMS pricing, the two RL agents demonstrate the ability to balance conflicting objectives between private providers and public authorities. The proposed approach provides a decision-support tool for sustainable and equitable multimodal mobility planning.

---


### 287. [BoxCtrl: 3D-Aware Visual Prompting for Geometric Image Editing](https://arxiv.org/abs/2606.23270)

**<font color=#1a73e8>作者：</font>** Feifei Wang, Shiyuan Yang, Xiaoyu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As instruction-based editing models and multimodal large language models advance, diverse image editing tasks have become feasible. However, achieving precise and consistent geometric image editing, such as translating, scaling, and rotating in 3D space, remains a major challenge. In this work, we introduce BoxCtrl, a 3D-aware visual prompting framework. Unlike text-only or coarse 2D-guided approaches, our method introduces informative RGB 3D bounding boxes projected onto 2D images as visual prompts. The three orthogonal faces of each box are painted with distinct RGB colors, simultaneously encoding position, size, and orientation to provide a compact, intuitive in-context visual example. The key to BoxCtrl's success lies in these well-designed bounding boxes, which decouple geometric control from appearance control. This enables the model to learn consistent correspondences between faces of the same color in the latent space, leading to a precise understanding of geometric intentions and accurate editing results. We introduce a two-stage training paradigm: Supervised Fine-Tuning (SFT) followed by Reinforcement Learning (RL). To address paired data scarcity, we construct a large-scale synthetic dataset for SFT, equipping the model with fundamental editing capabilities. To bridge the synthetic-to-real domain gap, we incorporate an online RL stage leveraging unpaired real-world data. Guided by a reward function evaluating geometric accuracy and visual fidelity, our SFT-RL strategy significantly enhances geometric precision while maintaining photorealistic quality. Extensive experiments demonstrate that BoxCtrl achieves state-of-the-art performance across translation, rotation, scaling, and composite editing tasks.

---


### 288. [Scaling LLM Knowledge Boundaries via Distribution-Optimized Synthesis](https://arxiv.org/abs/2606.23271)

**<font color=#1a73e8>作者：</font>** Songze Li, Yarong Lan, Zhongpu Bo 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge injection via synthetic data is crucial for enhancing Large Language Models (LLMs). However, current synthesis methods simply stop at preset token counts or fixed data ratios, lacking awareness of knowledge distribution. This results in some domains being sparse while others are redundant, limiting LLM knowledge boundaries. We revisit knowledge injection from a distribution perspective and hypothesize that an optimal knowledge distribution exists to maximize knowledge boundary expansion. We propose KDoS (Knowledge Distribution-optimized Synthesis), a framework that introduces knowledge density to drive synthesis through a three-stage feedback mechanism, shifting from blind generation to distribution-optimized synthesis. We construct Wikipedia-based synthetic data with varying knowledge distributions and conduct experiments on models from 0.6B to 16B (Qwen, Ling, LLaMA) and data scales from 1B to 5B tokens. Our key findings are: (1) an optimal knowledge distribution consistently maximizes boundary expansion; (2) this distribution is stable across backbones and scales; (3) KDoS outperforms baselines across six knowledge benchmarks. Our work offers a new perspective and practical framework for synthetic data-driven knowledge injection.

---


### 289. [Exposing the Illusion of Erasure in Knowledge Editing for LLMs](https://arxiv.org/abs/2606.23276)

**<font color=#1a73e8>作者：</font>** Advik Raj Basani, Anshuman Chhabra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge Editing (KE) has emerged as a frontier for updating specific facts in LLMs without costly retraining, but its reliability and underlying mechanisms remain poorly understood. In this work, we examine KE from an adversarial elicitation perspective, revealing that edited knowledge is often not fully erased and continues to surface, with consistent failures observed across diverse model architectures. To explain this behavior, we conduct a mechanistic analysis of popular KE methods. We show that low-rank updates do not overwrite existing knowledge but instead redistribute it within the model's representation space. Furthermore, we find that these methods act as targeted suppression mechanisms that reduce the likelihood of expressing original facts, rather than removing them from the model. Analysis of the loss landscape reveals that edited knowledge lies in narrow, anisotropic regions that are highly sensitive to perturbations, making them highly vulnerable to indirect prompting and adversarial attacks. By exposing these profound architectural vulnerabilities, our work proves that KE algorithms are inherently bypassable and motivates a fundamental reevaluation of how we deploy post-hoc updates in several LLM applications.

---


### 290. [GIF: Locally Sound Geometric Information Flow Control for LLMs](https://arxiv.org/abs/2606.23277)

**<font color=#1a73e8>作者：</font>** Adam Storek, Nikolaus Holzer, Zhuo Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly mediate interactions between sensitive data, untrusted inputs, and privileged actions in agentic systems, creating security and privacy risks. These range from prompt injections that manipulate downstream tool use to leakage of confidential information through model outputs. Recent Information Flow Control (IFC)-based defenses show promise but lack a principled semantic foundation for reasoning about information flow through the model itself. Since any input token may influence any output token in an autoregressive LLM, existing approaches suffer from severe taint explosion.
We present Geometric Information Flow (GIF), a semantic framework for tracking information flow from input tokens to outputs. GIF uses the LLM Jacobian and local output geometry to upper-bound the Shannon mutual information between perturbed input spans and model outputs, yielding a scalable measure computable on large models via automatic differentiation and low-rank approximation. Unlike attention-based or correlational attribution heuristics, GIF satisfies local geometric soundness, and we provide a fully mechanized Lean 4 proof that it upper-bounds the true information flow induced by a given prompt under local regularity assumptions.
We evaluate GIF on integrity and confidentiality tasks across multiple prompt-injection and privacy-leakage benchmarks. GIF achieves near-perfect recall even without a downstream declassifier, outperforming attention-based baselines. Combined with lightweight LLM-based declassifiers, it matches or exceeds the F1 of direct LLM-as-judge baselines such as GPT-5.5 xhigh reasoning while using up to 81x lower token cost. GIF flows detected with small surrogate models transfer to larger state-of-the-art models and other model families, even when the surrogate is up to 200x smaller, suggesting black-box deployment without gradient access.

---


### 291. [Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs](https://arxiv.org/abs/2606.23283)

**<font color=#1a73e8>作者：</font>** Hongxun Ding, Xiang Yu, Chengbing Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory systems are essential for personalized Large Language Models (LLMs). However, existing retrieval methods in these systems primarily rely on semantic similarity, potentially missing logically critical memories with limited semantic overlap. Current benchmarks remain inadequate for evaluating this problem. To address this gap, we construct IMLogic, the first high-quality benchmark targeting implicit logical memory retrieval in long-dialogue scenarios. Motivated by this challenge, we introduce root memory, a structured, decision-preserving representation that distills reusable personalized logic from long-term user histories. We then propose RootMem, a plug-and-play framework that first distills raw histories into structured root memories and then uses an LLM-based router to activate logically relevant ones, complementing semantic retrieval with personalized decision logic. Extensive experiments demonstrate that RootMem significantly outperforms the strongest retrieval baselines and consistently boosts the accuracy of existing memory agents. Our benchmark and codes will be available at this https URL.

---


### 292. [On the Effect of Segmentation Width and Cluster Size on Speech Resynthesis and Continuation in Generative Spoken Language Models](https://arxiv.org/abs/2606.23285)

**<font color=#1a73e8>作者：</font>** Shunsuke Kando, Wataru Nakata, Shinnosuke Takamichi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Generative Spoken Language Modeling (GSLM) enables text-free speech modeling by training language models (LMs) using discrete speech representations instead of textual transcription. In this paper, we investigate the performance of GSLM on speech synthesis and continuation using discrete speech representations with varying bitrates. We segment speech representations with fixed widths and train K-means models in multiple cluster sizes, resulting in various bitrate settings. We demonstrate that intelligible and natural speech can be synthesized at lower bitrate settings than the baseline. Furthermore, speech continuation quality remains stable at lower bitrates across multiple metrics, suggesting that the conventional GSLM setting may be redundant for effective speech generation. Although LLM-based metrics show higher correlation with human subjective score than conventional metrics, it remains low, highlighting the need for more stable automatic evaluation methods.

---


### 293. [GRIMIP: A General Framework for Instance-Specific Configuration of MIP Solvers Using LLMs](https://arxiv.org/abs/2606.23299)

**<font color=#1a73e8>作者：</font>** Yidong Luo, Xuemin Chen, Chenguang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Configuring the hyperparameters of Mixed-integer programming (MIP) solvers is a high-dimensional, instance-dependent optimization problem where suboptimal settings can degrade solving time by orders of magnitude. Default configurations are often suboptimal, while traditional tuning methods either suffer from the ``cold-start'' problem and inefficient search or heavily rely on expert experience. This paper introduces \textbf{GRIMIP} (\textbf{\underline{G}}eneral \textbf{\underline{R}}easoning for \textbf{\underline{I}}nstance-specific \textbf{\underline{MIP}} configuration), a novel hybrid intelligence framework that synergistically integrates the semantic reasoning capabilities of Large Language Models (LLMs) with the sample-efficient search of Bayesian Optimization (BO). GRIMIP enables the LLM to function as a complete probabilistic surrogate within the BO loop, significantly improving performance and reducing sampling and evaluation costs. On seven benchmarks including MIPLIB, GRIMIP achieves over 40\% reduction in Primal-Dual Integral on hard instances, outperforming SMAC and other LLM-assisted BO methods. By granting LLMs sufficient autonomy, GRIMIP combines the expert-level reasoning of LLMs with the efficient search of BO, achieving state-of-the-art performance.

---


### 294. [WaveDetect: Robust Framework for Machine-Generated Text Detection via Wavelet Transform](https://arxiv.org/abs/2606.23336)

**<font color=#1a73e8>作者：</font>** Zhichen Liu, Kaitong Qin, Linhan He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models asymptotically approach human-level fluency in natural language generation, solely relying on surface-level semantic artifacts for detecting LLM-generated texts has become increasingly precarious. Existing detectors often falter when facing three critical challenges: adversarial perturbations, cross-domain shifts, and the rapid temporal evolution of the foundation model. To address these issues, we propose \wavedetect, a novel framework that reformulates text detection as a signal processing task within the time-frequency domain. Unlike previous methods that analyze static token probability distributions, \wavedetect models the generated output as a probability signal, upon which a differentiable Continuous Wavelet Transform is applied to convert them into learnable spectral representations. This process reveals the intrinsic ``spectral fingerprints'' in machine-generated texts--patterns that remain invisible in time domain. Comprehensive evaluations on three well-curated datasets (RAID, EvoBench, and Domain-Shift) show that our method achieves a new state-of-the-art. It not only achieves superior accuracy but also exhibits remarkable robustness against sophisticated attacks, generalization across out-of-distribution topics and unseen evolving LLMs. Our results validate the efficacy of spectral analysis as a promising paradigm for LLM-generated texts detection.

---


### 295. [Abstract representational geometry supports inference in large language models](https://arxiv.org/abs/2606.23345)

**<font color=#1a73e8>作者：</font>** Yunan Zeng, Yuwang Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A defining feature of human intelligence is the ability to adapt to changing environments by inferring latent task structure from sparse observations. Neuroscientific research indicates that this capability relies on the hippocampus constructing abstract representations, expressed as low-dimensional, approximately orthogonal manifolds in neural state space. However, the internal mechanisms of large language models (LLMs) remain largely opaque, making it unclear whether they form comparable abstract representations or instead rely on task-specific statistical regularities when performing comparable reasoning tasks. Here we adapt a contextual reversal-learning paradigm to a text-based setting and compare humans and LLMs at both the Behavioural and representational levels. We report that although LLMs exhibit generalizable reasoning less frequently than humans, when such inference occurs, their internal states exhibit abstract geometric structures that resemble those reported in the hippocampus. Notably, this representational geometry is not uniformly distributed but is organized hierarchically across model depth: whereas lower layers show early, stable encoding of stimulus identity, higher layers form a hippocampal-like functional band enriched for abstract context geometry associated with inference. Furthermore, complementary intervention experiments mechanistically implicate geometry in reasoning: task-sequence language modelling induces geometric disentanglement, whereas geometric regularization of higher layers increases the emergence of generalizable inference. Together, these findings establish abstract representational geometry as a mechanistic principle supporting inference in large language models.

---


### 296. [Faithful Grounded Visual Reasoning via Learned Proxy-Tokens](https://arxiv.org/abs/2606.23354)

**<font color=#1a73e8>作者：</font>** Tom Hodemon, Mohamed Chaouch, Aboubacar Tuo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable success in Visual Question Answering (VQA), yet their "black-box" nature hinders deployment in critical domains. Grounded Visual Reasoning (GVR) approaches attempt to improve interpretability by explicitly couple textual rationales with visual grounding information, which are typically textual coordinates. This mechanism lacks a learnable semantic link to the visual features, often resulting in a semantic-spatial gap where the model hallucinates coordinates that do not correspond to image evidences. In this work, we introduce Composer, a MLLM that leverages a novel visual grounding mechanism based on learned proxy-tokens to promote faithful interpretability. These discrete symbolic pointers explicitly index the image latent space, allowing the model to manipulate visual regions as addressable, semantically manipulable sets. To rigorously validate our novel grounding mechanism, we constructed ComposerGCoT, a dataset synthesized to enable holistic assessment of reasoning consistency and grounding accuracy. Experimental results indicate that Composer achieves performance parity with its coordinate-based counterpart in final answer accuracy, while improving visual grounding accuracy by +9.0 points. By demonstrating that discrete proxy-tokens capture spatial semantics more effectively than typical textual coordinates, we establish that visual grounding mechanisms with learnable semantic links represent a promising path toward trustworthy and reliable MLLMs.

---


### 297. [Measuring & Mitigating Over-Alignment for LLMs in Multilingual Criminal Law Courts](https://arxiv.org/abs/2606.23375)

**<font color=#1a73e8>作者：</font>** Arthur Wuhrmann, Gaetan Stein, Daniel Brunner 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While the wider applicability of LLMs in the legal field is currently debated due to their reliability and the gravity of any errors, narrow uses with well-understood and mitigated risks have emerged. Notably the Swiss Federal Supreme Court uses small on-premises models for tentative translations and short-passage summarization across the four official languages. However, such usage is challenging in the context of Criminal Law. Since rulings and cases employees work on routinely can contain detailed descriptions of violent and sexual offenses, their legitimate work is compromised by refusals and disclaimers due to the activation of model guardrails (over-alignment).
To measure this phenomenon, we introduce TF-RefusalBench, a multilingual benchmark for criminal-law translation and summarization derived from public Swiss Supreme Court rulings. TF-RefusalBench contains 5,200 total prompts across French, German, Italian, and English, corresponding to common task prompts and passages likely to trigger refusal. We then use TF-RefusalBench to show that over-alignment is a multifaceted phenomenon, influenced by the model and the prompt and text languages being processed, and that its impact cannot be evaluated solely from an over-refusal perspective, given the disclaimer's impact on task faithfulness. Finally, we evaluate approaches to enable on-premises LLMs for Criminal Law Tasks, demonstrating that while prompting can be effective, abliteration (refusal directions ablation) eliminates refusal with minimal impact on task performance.

---


### 298. [Self-Stigma Is Not a Monolith, but Generic Empathy Is: Persona-Conditioned LLM Support for People Who Use Drugs](https://arxiv.org/abs/2606.23387)

**<font color=#1a73e8>作者：</font>** Layla Bouzoubaa, Rezvaneh Rezapour  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Self-stigma predicts treatment avoidance and disengagement among people who use drugs (PWUD), yet conversational systems aiming to provide support typically treat self-stigma expression as a uniform signal. We present a three-phase, proof-of-concept study of a persona-aware approach to LLM support. Latent Profile Analysis (LPA) on indicator-level features from 1,174 self-stigma expressors on Reddit yields a four-persona typology validated against held-out behavioral and linguistic features. Sequential Bayesian and recurrent neural classifiers recover these personas from limited posting histories, substantially outperforming batch and few-shot LLM baselines (macro-F1 = 0.74 at 30 posts). Evaluation by eight clinical experts across three contemporary LLMs revealed a misalignment: persona-matched responses successfully achieved targeted behavioral shifts, yet raters holistically preferred the generic empathy of the persona-neutral baseline. Our findings suggest that holistic empathy judgments and clinically-aligned response design can pull in opposite directions, and that evaluating LLM-based stigma support requires rubrics capable of decomposing the two.

---


### 299. [Distribution-Aware Diffusion-LLM for Robust Ultra-Long-Term Time Series Forecasting](https://arxiv.org/abs/2606.23391)

**<font color=#1a73e8>作者：</font>** Falguni Ghosh, Vahid Hashemi, Bernhard Kainz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting is a fundamental machine learning task. Recent work has explored Large Language Models (LLMs) for this purpose due to their strong generalization, pattern recognition, and zero-shot or few-shot capabilities. Despite their suitability for long-context learning, LLMs face challenges in multimodal settings: they lack calibrated probabilistic modeling for non-text data and struggle to align heterogeneous representations. To address these issues, we propose a new framework Diffusion-LLM that integrates a conditional diffusion model into an LLM-based forecasting pipeline. This joint design enables learning the conditional distribution of future data while improving semantic alignment in a shared latent space. We evaluate Diffusion-LLM on six long-term forecasting benchmarks, including ETT, Weather, and ECL. Our method consistently outperforms existing LLM-based baseline, achieving notable gains in ultra-long-term and few-shot forecasting and demonstrating the value of distribution-aware regularization for enhancing robustness and generalization in time series LLMs.

---


### 300. [Do LLM Embedding Spaces Recover Expert Structure?](https://arxiv.org/abs/2606.23394)

**<font color=#1a73e8>作者：</font>** Yixuan Zhu, Zhenke Duan, Fanghen Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretrained text embeddings are increasingly used as representational maps, yet high category separability does not imply that their geometry recovers expert-defined structure. We study this problem in mental-health-related language, where symptom relations provide an external reference and online communities introduce strong domain, affective, stylistic, and discourse confounds. Using 28 Reddit communities, we compare pretrained and supervised fine-tuned Qwen3 embedding spaces at two scales (0.6B and 4B). We construct category prototypes, evaluate their representational dissimilarity matrices against an expert symptom matrix with representational similarity analysis, and complement this global test with prototype-based typicality and multi-baseline confound controls. Pretrained embeddings show measurable alignment with expert structure within the mental-health subset; fine-tuning strengthens this alignment most at the finest category level; and larger scale improves both zero-shot alignment and supervision-induced gains. Residual alignment remains substantial after controlling for VAD, LIWC, lexical style, and topic-distribution structure. These results suggest that LLM embeddings can recover expert-relevant category geometry, but this recovery is level-dependent and should be tested against explicit confounds rather than inferred from classification alone.

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
