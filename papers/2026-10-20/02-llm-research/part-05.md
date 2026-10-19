# 🧠 大模型相关研究 | 2026年10月20日

> 本类共 **258** 篇论文：已确认 **247** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-258](./part-06.md)

---

### 201. [When Evidence Vanishes: Distilling Visual-Evidence Dependency in Medical Vision-Language Models](https://arxiv.org/abs/2610.23469)

**<font color=#1a73e8>作者：</font>** Qizhen Lan, Yiling Ma, Ruiqi Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compact medical vision-language models (VLMs) can answer clinical questions correctly without reliably using the image, relying instead on question wording or learned priors. Standard knowledge distillation copies a teacher's answer preference on the original image, but it leaves unchecked whether that preference is conditional on the visual evidence required by the question. We study this missing target as medical visual evidence dependency: support for the correct answer should decrease when the matched evidence is absent. We introduce Evidence-Conditioned Dependency Distillation (ECDD), which pairs each training image with a control matched to the evidence level and distills the teacher's drop in answer margin across the pair. A lower bound objective transfers positive dependency by penalizing only shortfalls, while original-image supervision preserves task accuracy. The same formulation applies when the evidence is a queried clinical region, a surgical instrument, or whole-image visual content. Across three medical VQA settings, ECDD keeps original-image accuracy competitive with distillation and alignment baselines while making answer support more sensitive to evidence removal. Under the DME headline objective, for example, the positive-case margin response to target rather than random masking rises from 0.786 with KD to 2.023 with ECDD, while original-image accuracy differs by 0.11 points. These results suggest that medical VLM distillation should transfer both the teacher's answer preference and its dependence on visual evidence.

---


### 202. [MuninAI: A Self-Hosted Agentic Framework for Independent Research Groups](https://arxiv.org/abs/2610.23480)

**<font color=#1a73e8>作者：</font>** Markus Fischer, Jens Meiler, Matthias Elgeti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Research groups that want a language model grounded in their own literature face a choice between hosted services that receive their unpublished work and self-hosted deployments that keep the data local but give the model no access to the corpus. Munin is an open-source framework for a self-hosted scientific assistant that indexes a group's corpus and its citation graph, and wraps whichever open-weight model the group can serve in an agent harness with specialised reading, search, and computation tools. We claim that the harness, rather than the specific model, is what makes the system useful on domain literature, and we ship the evaluation suite that tests this claim with the software.
On 199 paired literature questions, the harness more than doubles the accuracy of the base model, from 0.387 to 0.874 (+0.487, 95% CI [0.407, 0.568]), while naive retrieve-then-answer scores below the unaided model on every backbone tested. Under the harness, roughly twice as many answer claims trace to a passage the model read itself as with fixed top-5 retrieval. When the source paper for a question is removed from the corpus, the system abstains on about nine in ten of the questions it had answered correctly on the Qwen backbones and eight in ten on gpt-oss-20b, and it produces no fabricated local citation across 300 fabricated references.
The pattern holds on three backbones from two developers, including a 20-billion-parameter model that runs on a single consumer-grade GPU. With all outbound network access disabled, both Qwen backbones still exceed the published PaperQA2 accuracy. The evaluation suite runs as a single command, so an adopting group can re-run it on its own corpus and model.

---


### 203. [LocalIntent: Outcome-Specific Structured Generation for Backend-Compatible Smart Building Automation with Local LLMs](https://arxiv.org/abs/2610.23511)

**<font color=#1a73e8>作者：</font>** Tianyang Liu, Jiayue Wang, Zhanhao Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Locally deployed large language models (LLMs) can reduce reliance on remote cloud services for natural language smart building automation, but backend-facing processing requires correct outcome selection, alignment with local capabilities, and valid structured outputs. We investigate whether a complete outcome-specific prompting design improves compact-model outputs beyond generic route-then-generate prompting. The proposed LocalIntent approach routes requests to ordinary or persistent-rule branches: the former produces commands, clarifications, or rejections, while the latter generates trigger-action rules, followed by deterministic validation. We evaluate four locally executed Gemma and Qwen models spanning 2B-9B parameters on 101 non-persistent and 54 persistent-rule records, comparing Monolithic prompting, generic two-stage prompting, LocalIntent, and validation-guided repair. Across the evaluated datasets, LocalIntent achieves higher intent understanding, device identification, and action/parameter correctness than generic two-stage prompting, while clarification/mode correctness remains model-dependent. The largest gains occur for rules, where LocalIntent improves intent understanding from 26.4% to 80.6%, device identification from 59.3% to 84.7%, rule-mode correctness from 49.1% to 98.6%, and action/parameter correctness from 5.6% to 44.9%. For non-persistent requests, pooled gains are smaller: intent understanding increases from 39.6% to 53.2%, and action/parameter correctness from 30.7% to 42.8%.

---


### 204. [Perceive, Solve, Reason: Progressive Capability Formation in Time Series-LLMs](https://arxiv.org/abs/2610.23521)

**<font color=#1a73e8>作者：</font>** Xin Qiu, Junlong Tong, Wei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can now perceive, describe, and reason about images and audio, yet time series understanding remains underestimated: most work uses LLMs as forecasters and classifiers, reasoning studies are few and narrow, and no suite trains and evaluates the full range of capabilities. In this paper, we build the first such suite, with 337K training and 44K evaluation samples across three progressive capabilities, Perceive, Solve, and Reason, and use it to ask how time series should enter an LLM that must master all three, and in what order. We find that a dedicated encoder is essential: with one, a 4B model surpasses GPT-4o on every perception attribute we test, whereas textualizing the series costs 8--10 points in reasoning accuracy. The capabilities then build on one another: learning them in order beats mixing the same data and rivals reasoning-only training with over three times the reasoning data, but only when an encoder is used. Analyses further reveal that capabilities are transferred through distinct network depths rather than simply stacked, and that a stage converged on its own benchmark is not necessarily ready for the next. Distilled into a simple recipe, these findings yield 4B TS-LLMs that, without any target-domain data, outperform four recent 7B TS-LLMs on seven of eight out-of-domain metrics, by up to 11 points. We therefore advocate treating time series as a first-class modality for LLMs, read through dedicated encoders and taught to perceive before they reason.

---


### 205. [Trapped in Your Story: Evaluating Narrative-Induced Sycophancy in Large Language Models](https://arxiv.org/abs/2610.23525)

**<font color=#1a73e8>作者：</font>** Runtai Yang, Dandan Zhu, Kaiwei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are known to exhibit sycophancy by adjusting their responses toward users' expressed views. However, real users often justify their opinions through reasons, personal experiences, causal explanations, and broader narratives, raising the question of whether such narratives can further steer model judgments. We construct a controlled benchmark of 500 debatable questions across ten domains, where the user stance is held fixed while its justification is systematically varied without introducing new task-relevant evidence. Each question is instantiated under 11 matched conditions: one neutral baseline and five mirrored narrative levels for each of two opposing positions, yielding 5,500 evaluation instances. We evaluate seven LLMs and observe substantial differences in narrative-induced agreement. The effect is not monotonic with narrative elaboration: personal experience can reduce agreement, whereas causal framing and worldview-based synthesis increase it. Controlled GPT-5.1 ablations further show that causal framing produces the strongest positive effect, while claim-preserving bullet presentation also increases agreement over paragraph form. These findings suggest that sycophancy is shaped not only by user stance, but also by how supporting explanations are structured and presented.

---


### 206. [Truth in Contrast: Calibrated Factual Evidence from Language Model Likelihoods](https://arxiv.org/abs/2610.23527)

**<font color=#1a73e8>作者：</font>** Ponhvoan Srey, Jason Lucas, Pittawat Taveekitworachai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) encode substantial factual knowledge. Yet, estimating confidence in factual claims reliably remains challenging. We study likelihood-based factual confidence from the complementary perspectives of discrimination and calibration across multilingual factual statements. Specifically, we instantiate contrastive generative likelihoods as Contrastive Factual Evidence (CFE), which compares the likelihood of the same claim under competing factual and non-factual conditions, and derive its probabilistic counterpart, the Contrastive Factual Posterior (CFP). We show analytically that CFP calibration depends on the differential error between the two surrogate conditionals, allowing errors shared across them to cancel and yield tighter calibration bounds. Empirically, CFP substantially improves calibration while maintaining factual discrimination comparable to its strongest competitor. Nonetheless, discrimination is uniformly weak across methods in lower-resource languages, which simultaneously undermines the utility of the measured calibration. To this end, we interpret a likelihood geometry, within which an evidence-bearing direction is induced, along with an orthogonal evidence-invariant direction. In our investigation, we selectively align target-language claims with stronger English evidence only along the factual-evidence direction, improving discrimination and open-ended factual generation without target-language labels.

---


### 207. [Out of Support, Not Out of Reach: In-Context Learning with Unsupported Instructions and Composed Tasks](https://arxiv.org/abs/2610.23528)

**<font color=#1a73e8>作者：</font>** Xuhan Tong, Yuchen Zeng, Jiawei Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-Context Learning (ICL) enables pretrained LLMs to adapt to downstream tasks from a small set of input-output demonstrations, without parameter updates. Yet existing theory primarily explains ICL as identifying a latent task already represented in pretraining, leaving unclear whether ICL can succeed when either the instruction or the target task falls outside the pretraining support. We develop a theoretical framework under mild assumptions that separates these two forms of distribution shift. For target tasks represented in pretraining, we show that demonstrations can identify the task and reduce sensitivity to pretrain-supported prompt templates as their number increases. For an unsupported instruction, we show that under a fixed model-induced reference extension, demonstration evidence can dominate an $N$-independent instruction shift while preserving the exponential identification rate. We then use the same ICL framework as an interpretive lens for long-horizon target tasks that are not represented in pretraining but admit a plan that decomposes them into pretraining-supported subtasks. Applying the supported-task analysis step by step yields a standard accumulated-error bound and clarifies how invoking familiar subtasks along an intermediate-state trajectory can avoid directly selecting the unsupported complete task. Together, our results characterize when demonstrations, instructions, and task decomposition can support ICL beyond the corresponding pretraining supports.

---


### 208. [EduWild: How Teacher-Configured Chatbots Fail in Real-World Use and How to Fix Them](https://arxiv.org/abs/2610.23530)

**<font color=#1a73e8>作者：</font>** Ziqi Liu, Ruiwei Xiao, Yuxuan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Teachers increasingly configure educational chatbots through natural-language instructions, but how these bots fail in real-world use remains poorly understood. We introduce EduWild, a dataset of 1,726 conversations with 217 teacher-configured chatbots, each paired with the instructions and configuration behind it, including 900 conversations from the intended end users of 35 deployed chatbots. We develop a 29-code taxonomy covering factual, workflow, diagnostic, and pedagogical failures and apply it using a human-calibrated LLM judge. The most frequent failures are lapses in following teacher intent --- bots skip required workflow steps (53.8% of end-user conversations), omit expectation setup (33.4%), and overload learners with information or questions (37.1%). Guided by these findings, we design a prompt-based harness targeting the six most frequent failure modes. In a study with 200 college students across ten bots, the harness reduces the mean number of target failure codes per conversation from 1.406 to 0.489, a 65.2% relative reduction with bots weighted equally. These findings show how real-world failure analysis can guide practical improvements to educational chatbots.

---


### 209. [From Billion-Scale to Million-Scale Language Models: Operational Capabilities for Embedded Post-Exploitation](https://arxiv.org/abs/2610.23534)

**<font color=#1a73e8>作者：</font>** Gabriel Hortea, Simon Pietro Romano, Juan Tapiador 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Small Language Models (SLMs) are increasingly attractive for resource-constrained environments due to their low computational footprint. These characteristics also make them candidates for future autonomous malware, where connectivity, latency, privacy, or operational constraints may preclude cloud-based inference. Yet the ability of ultra-compact models to support malware during post-exploitation remains poorly understood.
We systematically evaluate seven open-source SLMs (20M-1.5B parameters) on two post-exploitation code-generation tasks: Directory Enumeration and Backdoor Generation. We compare Python (high-resource) and Lua (low-resource) across prompting strategies, task formulations, iterative reasoning, grammar-constrained decoding, and execution-feedback loops.
Results show that offensive code-generation capabilities do not increase linearly with model size. Successful execution depends on the interaction of model capacity, task formulation, and prompting strategy, with task formulation exerting a greater influence than prompt engineering alone. Algorithmic formulation combined with few-shot prompting enables Qwen2.5-Coder 1.5B to reach Pass@5 of 100% in both Python and Lua for Directory Enumeration, 100% in Python for Backdoor Generation, and 99.2% in Lua.
Although the evaluated models remain too computationally demanding for widespread deployment in contemporary malware, rapid progress in compact models may reduce this barrier. These findings help anticipate AI-assisted malware and inform future countermeasures.

---


### 210. [ConvexLLM: Scaling Convex-Hull Speech Interfaces to General-Purpose Audio Intelligence](https://arxiv.org/abs/2610.23539)

**<font color=#1a73e8>作者：</font>** Ming-Hao Hsu, Shujie Liu, Yuxuan Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech and audio language models connect continuous acoustic representations to decoders pretrained primarily on text data. Most such models use MLP or Q-Former interfaces to map acoustic features into the decoder's input space, requiring the decoder to learn how to interpret the resulting representations. We investigate whether grounding these representations in the decoder's existing text embeddings can help it use acoustic information while better preserving its pretrained text capabilities. We present ConvexLLM, a general-purpose speech and audio language model whose C-Gate interface represents audio as continuous convex combinations of frozen text embeddings. ConvexLLM achieves an eleven-task VoiceBench aggregate of 75.36, the highest among the open-weight models we compare, and an MMAU Test-mini accuracy of 62.50%. Its largest margins over the baselines are on spoken knowledge and reasoning tasks, while the strongest baselines are more accurate on audio understanding and transcription. In a comparison with a 2B-parameter decoder, C-Gate achieves higher aggregate spoken-language performance than MLP and Q-Former interfaces, with text-task performance close to MLP and task-dependent tradeoffs in transcription and audio understanding. These results support convex combinations of text embeddings as a viable interface for general-purpose speech and audio language models.

---


### 211. [SkillBrowser: Selective Skill Exposure for Scalable Skill-Using Agents](https://arxiv.org/abs/2610.23554)

**<font color=#1a73e8>作者：</font>** Jin Ye, Yifan Jiang, Lan-zhe Guo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly rely on skills to extend their capabilities in complex tasks. However, scalable skill use requires Selective Skill Exposure (SSE): providing relevant procedural content when needed while avoiding unnecessary exposure that may disrupt reasoning. Existing paradigms fall short in complementary ways. Progressive disclosure exposes metadata for a growing skill library, introducing context pollution; retrieval limits catalog exposure, but static retrieval from the initial task query may be misaligned with capability needs that emerge during reasoning and may still inject unnecessary skills. We propose SkillBrowser, a Meta-Skill-managed framework that enables an agent to identify current capability needs, formulate targeted queries, and selectively load skills on demand. Across six SRA-Bench subsets and five LLMs, SkillBrowser improves aggregate accuracy over static retrieval and LLM-based selection, including multi-step tool use, and mitigates accuracy degradation on already-solvable instances. Benefits remain model- and task-dependent, with under-invocation of useful skills and additional latency as key limitations. These results demonstrate the viability of Meta-Skill-managed SSE for scalable skill repositories.

---


### 212. [BMuon: Budgeting Muon's Spectral Geometry for Structured Compressibility](https://arxiv.org/abs/2610.23571)

**<font color=#1a73e8>作者：</font>** Rida Assalouh, Tom Jacobs, Rebekka Burkholz 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has emerged as a strong optimizer for neural network training and admits an interpretation as steepest descent under a spectral-norm geometry. Yet we find that Muon-trained Transformers can degrade sharply when their MLP hidden channels are pruned after training. To reconcile Muon's optimization performance with structured compressibility, we introduce Budget Muon (BMuon), which modifies Muon's spectral geometry so that hidden channels across blocks compete for a shared allocation budget. The resulting oracle is exactly normalized steepest descent under a family of norms that interpolate between Muon's geometry and structured sparse geometries. Our principal sparsity control is an interpretable global channel-allocation budget, rather than a setting-dependent sparsity-penalty coefficient. For linear factorization models, we show that Muon admits minimum-cost exact representations with redundant hidden width, whereas under the BMuon oracle geometry and a sufficiently scarce budget, every minimum-cost representation is width-minimal. For practical training, we derive a minorization-maximization surrogate for the exact allocation problem. On ImageNet-1K with ViT-S/16, BMuon improves over Muon under gradual structured MLP pruning, and its learned allocations provide a more effective pruning criterion than weight magnitude. On a 1B-parameter LLaMA-style model trained on FineWeb, BMuon improves over Muon under post-training MLP channel pruning.

---


### 213. [Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively Self-Evolving Agents](https://arxiv.org/abs/2610.23574)

**<font color=#1a73e8>作者：</font>** Mingze Yin, Xiaohan Wang, Dian Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Model (LLM) agents have demonstrated remarkable capabilities across complex tasks, they predominantly operate in isolated sessions, lacking the ability to continually learn from historical interactions or adapt to user-specific environments. Existing self-evolution paradigms often indiscriminately inject raw interaction trajectories into memory or skill modules, leading to obscured behavioral patterns and compromised update controllability. Furthermore, as foundational LLM reasoning improves, the bottleneck for agentic evolution shifts from accumulating generic knowledge to effectively managing situational experience. To address this, we propose Darwin-Claw, an environment-adaptive self-evolving framework that systematically distills episodic experiences to drive the comprehensive evolution of operational skills and durable memory. Theoretically grounded in an iterative agent-actor and evolver-critic co-adaptation, Darwin-Claw introduces a Hierarchical Experience Consolidation System that extracts fine-grained error attributions and generalizes them into dynamically updated prototype vectors. This structured situational experience serves as interaction patches for context-sensitive perception and explicit optimization signals for skill refinement. Practically, Darwin-Claw is a readily deployable, automated framework compatible with mainstream agent systems without requiring manual curation. Extensive experiments on WildClawBench demonstrate that Darwin-Claw yields substantial performance improvements, establishing a controllable and stable pathway for the continual, user-centric adaptation of autonomous agents in real-world ecosystems.

---


### 214. [MARS: Memory-Aware Routing for Session-Level LLM Assistants](https://arxiv.org/abs/2610.23583)

**<font color=#1a73e8>作者：</font>** Minghan Wang, Jinhang Zuo, Zhongxiang Dai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term LLM assistants must repeatedly decide what prior context to expose and which model should answer as an interaction evolves. Existing memory systems and model routers usually make these decisions separately, although memory construction changes the evidence, distractors, and difficulty of the resulting input. We introduce MARS, a memory-aware routing framework that uses session state as a shared control interface between memory construction and model selection. A Query and Topic Manager (QTM) estimates compact decision-relevant state that guides a fixed state-conditioned memory policy and an online router, enabling each turn to receive an appropriate memory view and a suitable model under a quality-memory-cost trade-off. We evaluate MARS on RealMem and MultiChallenge with 16 system configurations each, covering long-history memory-driven interaction and bounded sessions with structured context interference. On RealMem, MARS preserves 98.2% of full-context GPT-4o's QA while using only 14.5% of its generation API cost, including both generation and controller calls for MARS, and achieves the strongest measured memory-recall and retrieval scores among compared systems. On MultiChallenge, MARS trails the strongest static system overall but approaches its performance at lower recorded cost on a mechanism-focused subset. Together, these results support a favorable quality-memory-cost trade-off for long-history, memory-dependent interaction.

---


### 215. [Analyzing Occupational Gender Bias across the LLM Training Lifecycle](https://arxiv.org/abs/2610.23587)

**<font color=#1a73e8>作者：</font>** Manthan Gadhia, Alexander Hoyle, Karolina Stańczak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training is widely assumed to reduce the social biases language models inherit from pretraining, yet direct evidence for this assumption remains mixed. In this paper, we examine how gender disparities evolve across the language modeling pipeline. In particular, we study occupational gender bias in OLMo 3, a fully open language model family, across its post-training stages by prompting each checkpoint to generate open-ended narratives about synthetic personas given their occupation and education. We consider two settings, a gender-given setting in which the profile states the persona's gender explicitly and a gender-assumed setting in which it must be inferred by the model. We find that when gender is stated, post-training increases semantic diversity for male-coded profiles, whereas for female-coded profiles the increase is smaller after SFT and not significant after DPO and RLVR. When gender is assumed by the model, post-training affects narratives about female and male personas similarly. The model's own gender assumptions, however, show a consistent female-preferential skew relative to United States labor-force demographics, except for heavily male-dominated occupations. Every successive post-training stage monotonically increases the odds of attributing a female label over the base model. A provenance analysis of the supervised fine-tuning corpus finds only a modest 7.7% female-token surplus, too small to explain the size of these downstream effects. The project code is available under: this https URL.

---


### 216. [Enhancing RAG-based Medical VQA with Gated Multimodal Representations](https://arxiv.org/abs/2610.23588)

**<font color=#1a73e8>作者：</font>** Daniela Jimenez-Pano, Hugo Jair Escalante, Delia Irazú Hernández-Farías  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Models (Med-LVLMs) have shown strong performance in Medical Visual Question Answering (MVQA), yet they may still produce factually inconsistent responses. Retrieval-Augmented Generation (RAG) can mitigate this issue by incorporating external clinical evidence; however, retrieval is often guided by a single modality, potentially overlooking the joint semantics of medical images and clinical questions. We introduce a multimodal RAG framework that learns a joint query representation through a Gated Multimodal Unit, enabling evidence retrieval to leverage information from both modalities while keeping the underlying Med-LVLM frozen. We evaluate the proposed approach on benchmark datasets. Results show that the multimodal query representation consistently outperforms a reference Med-LVLM and remains competitive with state-of-the-art methods. Our findings demonstrate the potential of multimodal query representations for more effective evidence retrieval in Medical VQA.

---


### 217. [Boundary Detection for High-Dimensional Point Clouds](https://arxiv.org/abs/2610.23590)

**<font color=#1a73e8>作者：</font>** Abigail Hickok, Valerio Galanti, Osama Al Dalahmah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce two new methods for boundary detection in high-dimensional point cloud data, intended to work in situations with non-uniform density, high ambient dimension, and substantial noise. Our first method fits a separating hyperplane on local neighborhoods after doing local dimension reduction---this method works best when one can reliably estimate the intrinsic dimension of the data. Our second method measures the directional uniformity of local neighborhoods, and has the best overall performance on synthetic data. In addition to pointwise numerical boundary scores, our algorithms yield an estimated normal vector at each boundary point. We validate our methodology on synthetic data as well as two real examples: we analyze spatial transcriptomics data, where we show that we can detect the boundary of a tumor, and we also study LLM activation geometry.

---


### 218. [RL-Guided Temporal Localization for Dual-Channel Retrieval in Long-Horizon Agent Memory](https://arxiv.org/abs/2610.23598)

**<font color=#1a73e8>作者：</font>** Dabin Sheng, Zhe Wu, Jinming Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Time-aware retrieval is crucial for long-horizon LLM agents to effectively leverage ever-growing long-term memory. Existing methods focus on lexical or semantic similarity, leading to target memories being crowded out by temporally mismatched yet semantically similar candidates. Even time-aware approaches inject temporal cues only during memory organization or answer generation, overlooking temporal constraints at the retrieval stage, where candidate selection occurs - the root cause of the displacement. Inspired by the temporal contiguity effect in human episodic memory, we propose TIDER (Temporal Interval-driven Dual-channel Evidence Retrieval), a time-aware agentic retrieval framework. Central to TIDER is a reinforcement learning (RL)-trained temporal interval locator that infers the temporal windows in which the evidence lies. RL optimizes window localization as a discrete, non-differentiable retrieval decision, using composite rewards to convert sparse answer supervision into fine-grained retrieval feedback. These temporal windows first define the temporal retrieval channel; the retrieved candidates are then merged with results from the semantic channel and reranked by proximity to the windows. This temporal grounding enables TIDER to retrieve temporally aligned evidence that would otherwise be drowned out by the volume of semantically similar yet temporally mismatched memories. With a lightweight 1.7B locator, TIDER achieves state-of-the-art accuracy on both long-horizon memory benchmarks - 61.52% on LifeBench (+8.82%) and 78.96% on LoCoMo (+3.66%) - which indicates that temporal cues are crucial for pinpointing target evidence amid a vast pool of semantically similar historical events in long-term daily-life memory.

---


### 219. [From Trajectories to Differentiated Skills: Cognitive Differentiation for Self-Improving Agents](https://arxiv.org/abs/2610.23599)

**<font color=#1a73e8>作者：</font>** Yewei Zhao, Derong Xu, Wei Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents tackle complex tasks through reasoning and interaction with external environments. Agent skills provide persistent, transferable capabilities that guide task planning, inform contextual decisions, support tool use, and enable executable procedures. Yet existing skill-evolution methods largely organize knowledge around skill artifacts, overlooking the functional heterogeneity within individual skills and its implications for knowledge maintenance and use. Inspired by cognitive science, we propose Cognitive Differentiation in Skill Evolution (CDSE), which evolves a unified skill through four functionally distinct yet coordinated components: Meta, Experience, Tool, and Script. CDSE extracts evidence-grounded semantic gradients from successful and failed trajectories, consolidates them by functional role, and applies component-specific updates and validation with cross-component coordination and adaptive invocation. An analysis of 500 top-ranked skill packages shows that 96.8% contain knowledge spanning at least two functional roles. Across six benchmarks, three agent models, and two execution harnesses, CDSE achieves the highest scores in all 36 settings, improving over the Base agent by 7.6 percentage points and the strongest competing method in each setting by 2.6 points on average. Ablation studies further support the importance of functional differentiation and adaptive invocation.

---


### 220. [Token-Level Attribution of Multi-Mode LLM Watermarks: Optimal Rule and Belief Weighting](https://arxiv.org/abs/2610.23601)

**<font color=#1a73e8>作者：</font>** Rui Zhou, Licheng Zhao, Chao Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A watermark verifier may hold many modes, i.e., secret keys, and a document may mix spans of different modes with unwatermarked text. Directly reporting the mode with the largest pivotal statistic (pivot) inflates the Type I error, and restoring the nominal level reduces power as candidate modes are added. We formulate token-level multi-mode attribution for the Gumbel-max watermark as maximizing correct-label power under a Type I error constraint given a mode prior. We show that the optimal rule reports the mode with the largest prior-weighted alternative density and rejects when this density exceeds one common threshold. Based on this rule, we propose the Belief-weighted Likelihood Attribution with Density Estimation (BLADE) detector. It estimates the mode prior from neighboring pivots and the alternative density from reference token probabilities. Under a conditional product model of the pivots, it keeps the exact Type I error. We further show that BLADE approaches the optimal rule as its prior and density estimates improve, with a sharp coefficient on the density error. On OPT-1.3B and other open-weight large language models, BLADE attains higher correct-label power than the compared detectors across candidate counts, token-substitution rates, generation temperatures and generator models.

---


### 221. [Not Every Mention Is a Claim: Rethinking Object Hallucination Detection in Vision-Language Models](https://arxiv.org/abs/2610.23610)

**<font color=#1a73e8>作者：</font>** Hsin-Ling Hsu, Neeraja Kirtane, Kuan-Hao Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object hallucination in vision-language models (VLMs) is usually measured by checking each object a caption names against the image. Most benchmarks and detectors alike treat every object mention as a claim that the object is present. This assumption fails when a caption names an object without asserting it, as in "a bench for people to sit on", which mentions people without claiming that any are in the image. We call such mentions non-assertive. Treating them as hallucinations inflates the error rates attributed to models that use such language. To separate them from real hallucinations, we introduce NAME-Bench (Non-Assertive Mention Evaluation Benchmark), 25,497 object mentions from captions that five VLMs generate for COCO images. Each mention is labelled concrete (asserted and present), hallucinated (asserted and absent), or non-assertive, and non-assertive mentions are further divided into four subtypes: depictive, purpose, negation and hedged. All the hallucination detectors that we evaluate flag non-assertive mentions as hallucinations, at rates between 14% and 80%. Adding non-assertive mentions to detector training as negatives largely corrects this on LLaVA-1.5. On the four newer VLMs, a comparable correction takes five to ten times more data, and the detectors then catch fewer real hallucinations. These findings show that current detectors conflate mentioning an object with asserting it, and that this conflation is harder to undo on the four newer VLMs than on LLaVA-1.5. Hallucination evaluation should therefore separate what a caption asserts from what it merely mentions.

---


### 222. [SIT-Eval: Situation-Based Interactive Turn-by-Turn Evaluation of Conversational Agents](https://arxiv.org/abs/2610.23612)

**<font color=#1a73e8>作者：</font>** Ravil Mussabayev, Saveliy Zavertyaev, Dmitriy Parpulov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of conversational AI agents necessitates evaluation methods that assess performance across diverse dialogue scenarios, utilizing multiple situational criteria, as appropriate behavior depends on context and encompasses various aspects. Existing dialogue benchmarks typically use static natural conversations, which underrepresent rare situations---a critical safety gap, as low-probability events become frequent failures at production scale. However, limited sample sizes force a choice: either maintain natural dialogues for realism or turn to adaptive situation sampling for comprehensive yet statistically reliable coverage. We introduce SIT-Eval, an adjustable framework for evaluating situation-based conversational agents. We formalize an agent's desired behavior as situational rules: if situation is P, follow rules Q. At each conversation turn, an LLM-interlocutor enacts a uniformly sampled situation. A context-aware LLM-judge leverages all conditionally applicable rules as criteria to evaluate the agent's reply for that situation. The judge is validated using human-verified synthetic golden dialogues. Benchmarking 8 LLMs on 1292 conversation turns reveals failure modes hidden by aggregate metrics: models with similar overall scores vary widely in their adherence to individual rules. All models struggle most with ambiguity clarification and Socratic questioning.

---


### 223. [ThetreStageAI: Multi-View Retrieval-Augmented Generation for Structured Bengali Theatre Production Planning](https://arxiv.org/abs/2610.23618)

**<font color=#1a73e8>作者：</font>** Md. Mehedi Hasan Naeem, Mst. Kamrunnahar Ruma, Shakila Sultana 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Staging a theatre performance requires coordinating dialogue, actor movement, stage directions, lighting focus, cue timing, and equipment constraints within the same production plan. This work presents ThetreStageAI, a retrieval augmented framework for structured Bengali theatre production planning. Rather than retrieving from one mixed corpus, the system maintains separate scene, actor-blocking, and lighting views. Bengali text is embedded with BGE-M3 and indexed in view-specific Qdrant collections. Retrieved references are combined with a production brief and passed to Gemini, which generates schema-constrained JSON containing characters, scenes, dialogue, stage directions, blocking, lighting, and optional sound cues. Structural and semantic checks are applied before acceptance, with at most one constrained repair attempt. We also construct a human-guided, LLM-assisted synthetic dataset of 500 short Bengali theatre records that expands to 1,500 retrieval documents. Dataset diagnostics confirm consistent identifiers and valid lighting fields while also revealing substantial dialogue repetition. A paired camera-ready evaluation compares single-combined and full multi-view retrieval under matched settings. The source code, dataset, and evaluation materials are publicly available.

---


### 224. [PresenceBench: An Exploratory Evaluation of Large Language Model Adaptation to User State](https://arxiv.org/abs/2610.23625)

**<font color=#1a73e8>作者：</font>** Peña Arroyo Gallego, Mauro Ruiz Moreno, Alejandro Acien 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Presence-aware intelligence is the capacity of an AI system's intelligence layer to adapt appropriately to the functional state of the person it serves (here readiness, flow, and stability) while preserving task quality and safety. We introduce PresenceBench, an instrument for measuring it. PresenceBench evaluates how the intelligence layer uses a supplied state, not how that state is sensed, and breaks the capability into measurable properties. Two are tested here. Receptivity: does the model take up the state and give a better response than with no signal? Specificity: does any improvement depend on the correct state, rather than on extra structured context? A third, adaptation across states, is a required endpoint not measured in this release. A five-arm causal design answers both questions, against each model's own baseline and an equally structured mismatched-state control, scored by a correctness-gated human paired comparison. The exploratory evaluation covered four models across eighteen single-turn, six fixed three-turn and six simulated natural-conversation scenarios. Supplying a synthetic state, raw or translated into a response policy, gave human-preference point estimates above 0.5 for all four models (Claude Sonnet 5, DeepSeek V4 Pro, Gemini 3.6 Flash, GPT-5.6 Terra), with three of eight 95% intervals excluding chance. Specificity was not resolved: no per-model interval excluded chance, and the design cannot yet separate the state values from a generic instruction to adapt. Policy delivery reduced priced cost and output tokens against each model's baseline; these are resource-use changes, not efficiency gains, because correctness non-inferiority was not established. Safety-floor failures were rare (13 of 360 cases), with a non-significant excess under policy delivery. We report the instrument, the frozen results, and the controls a confirmatory study needs.

---


### 225. [Deep LLM layers expose passage-level context in EEG during silent reading](https://arxiv.org/abs/2610.23638)

**<font color=#1a73e8>作者：</font>** Ingo Marquardt, Anthilia Alchanat, Priyanka Jain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In a previous report we showed that a decoder can recover open-vocabulary word-level information from 19-channel EEG recorded during silent reading, by aligning short EEG windows with hidden-state embeddings of the presented word taken from a large language model (LLM). That analysis contrasted two of the model's 33 layers: the context-free input embedding and one mid-depth layer. Here we ask how EEG-decodable structure is distributed over the full depth of the language model. We trained one decoder per layer of Llama-3.1-8B, with and without a causal transformer over the sequence of EEG windows. We distinguish word-level decodability from a context-tracking component. Word-level decodability peaks in early layers and declines steadily towards the last layer. In contrast, the context-tracking component of the retrieval gain rises with depth, both with and without a causal transformer. Unexpectedly, a decoder that sees a single 0.5-s window at a time tracks the text passage too. Two new controls dissect this component. A target-geometry control, a synthetic predictor made of the true target plus noise calibrated to each decoder's word-level accuracy, shows that context tracking is not a by-product of word decoding and target geometry. A control that permutes predictions across runs from either the same or from different sessions shows that most of the observed context-tracking is not caused by an EEG recording session signature. Instead, context tracking mostly follows the text. A single EEG window therefore carries passage-level information that a contextual target can absorb. The results locate word identity in the early layers of the language model, discourse state in the deeper layers, and make the choice of target layer a design dial for EEG language decoders.

---


### 226. [A Language-Informed Loss for Visual Generation](https://arxiv.org/abs/2610.23653)

**<font color=#1a73e8>作者：</font>** Suchir Agarwal, Keshigeyan Chandrasegaran, Ziyu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end visual generation with pixel-space loss has recently achieved competitive performance without the need for learned image tokenizers. In this work, we study whether language-informed supervision can provide a richer training signal than pixel loss for visual generation. We introduce LILIE (pronounced "lily"), a Language-Informed and Lossless Image Encoder. LILIE is an invertible image transform trained such that a vision-language model can recover captions from noised features. The encoder uses a normalizing flow transformer trained jointly with a vision-language model via next token prediction. We then use the encoder to extract a simple language-informed loss for text-to-image generation. We train JiT models with LILIE loss, reducing gFD by 14 points (66.84 $\to$ 53.01) against a pixel-only baseline on the GPIC dataset. Our code, encoders, and generative models are available at this https URL.

---


### 227. [FlexPart: Text-Controlled Semantics-Aware 3D Part Segmentation at Flexible Granularity](https://arxiv.org/abs/2610.23659)

**<font color=#1a73e8>作者：</font>** Yiqun Zhao, Jiachen Xu, Yihao Zhi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A 3D asset admits multiple valid part decompositions, while semantics-aware segmentation should reflect both the desired granularity and the parts a user wants to extract. Ideally, a practical segmentation
model should strive for a simple principle: what you ask for is what you get. However, realizing this goal is hindered by two core obstacles: the lack of multi-granularity training data and the absence of a
holistic control mechanism. We propose FLEXPART, a unified framework for text-controlled 3D mesh segmentation. To establish flexible control, we introduce a holistic control prompt comprising semantic part
names with location and shape clauses. To support this mechanism, we utilize an automated Vision-Language Model (VLM) pipeline to construct a large-scale dataset of multi-granularity partitions and their
corresponding prompts. Driven by this data, FLEXPART generates a view-independent part-identity field in native 3D space, directly assigning discrete part IDs to mesh faces. To compel the model to respect
semantic conditions rather than rely on geometric priors, we train the model using randomized background dropping. Furthermore, an inference-time VLM planner can automatically complete descriptive clauses
from 2D renderings, allowing users to simply name the desired parts in ordinary words. FLEXPART with planner-completed prompts outperforms the strongest evaluated baseline by 15% in mIoU, even when that
baseline receives ground-truth guidance. On our held-out FLEXPARTBENCH, FLEXPART leads at each granularity and improves average mIoU by 22% over the strongest baseline. With only the requested part names
supplied by the user, it also improves IoU by 35% over the strongest click-driven baseline on selective segmentation.

---


### 228. [OwlSight: A Panoramic Monitor for Chain-of-Thought Reasoning](https://arxiv.org/abs/2610.23670)

**<font color=#1a73e8>作者：</font>** Lewen Yan, Yanxu Zhu, Jie Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) monitoring offers actionable evidence for oversight AI systems, with the potential to enable early detection and intervention. However, existing approaches are focused on specific tasks, whereas the regulation of AI, particularly reasoning models, requires monitoring a broader range of tasks. We introduce Factor for CoT monitoring, a strategy that supports customizing monitoring requirements in the prompt, which enables a single monitor to cover different tasks by relying on different factors. Furthermore, we introduce two types of factors, fine-grained and coarse-grained (e.g., monitoring whether a specific email address has been leaked versus monitoring privacy leakage), to accommodate diverse user monitoring needs. Based on this, we develop a CoT monitor named OwlSight that relies solely on factor to monitor behaviors related to multiple dimensions, including capability, safety, and trustworthiness. Experiments across 15,971 reasoning trajectories show that OwlSight surpasses general-purpose LLMs by 1.32-30.57 and 11.71-27.81 points at fine and coarse granularity, respectively, and achieves state-of-the-art results on OpenAI's CoT monitorability benchmark. It also generalizes to unseen models' CoTs and remains robust to Factor rephrasings, CoT compression, and obfuscation, offering a promising paradigm for CoT monitoring that can contribute to the oversight of frontier AI.

---


### 229. [HardEval: An Execution-Verified Benchmark for AI-Driven Security Hardening and Compliance Remediation](https://arxiv.org/abs/2610.23685)

**<font color=#1a73e8>作者：</font>** Manohar Vellala, Soumya Banerjee, Sandip Roy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Implementing Security Technical Implementation Guide (STIG) controls remains a demanding operating-system administration task. Each natural-language security requirement must be translated into a precise and persistent configuration change. These changes span Secure Shell (SSH) configuration, authentication policy, audit rules, and kernel parameters. Existing benchmarks do not measure whether a model can perform this task on a live system. Code benchmarks evaluate isolated programs without persistent system state, while agent benchmarks largely focus on applications rather than operating-system configuration. In this paper, we introduce \textbf{HardEval}, an execution-verified benchmark for evaluating language-model-assisted security hardening. HardEval is built from Red Hat Enterprise Linux 8 STIG controls that fail on an unhardened baseline system. Expert-written reference remediations and Open Vulnerability and Assessment Language (OVAL) checks serve as hidden ground truth for grading; they are never shown to the model, and each task states only the required security outcome while withholding the implementation. The model produces a Bash script, which is executed on a live virtual machine and graded from fail to pass using the corresponding OpenSCAP/OVAL compliance check. Evaluation of fourteen frontier and open-weight configurations reveals large and uneven capability differences across security domains. A recurring failure mode is plausible security code that does not satisfy the exact compliance condition. For four open-weight configurations, multi-run Wilson confidence intervals preserve the observed ordering. HardEval is publicly available.

---


### 230. [VISTA: Steering LLMs with Latent User Values Inferred from a Few Survey Answers](https://arxiv.org/abs/2610.23702)

**<font color=#1a73e8>作者：</font>** Yinuo Xu, Jadie Adams, Brian Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Personalizing a language model requires knowing what a person values, which stays largely consistent across tasks. Yet most methods either learn task-specific preferences or place the user's profile in the prompt, where models struggle to act on it. We introduce VISTA (Value-Informed Steering and Targeted Acquisition), which infers a latent profile from users' (full or partial) survey answers, and maps the profile through a hypernetwork to a user-specific steering intervention in a frozen LLM to select answer choices or generate free-text responses. Given the same evidence, VISTA matches or beats in-context profiles on synthetic preferences (Food2D), the World Values Survey (WVS), and PrimeX, without adding prompt tokens. To reduce the cognitive burden of completing full surveys, VISTA also chooses which questions to ask and when to stop: on WVS it stops after 6% of the questionnaire while retaining 94% of the full-history gain, where standard adaptive testing retains at most 42%. The dominant steering direction is an interpretable value axis on which VISTA places unseen users accurately. Our results point toward pluralistic alignment that adapts to individuals at deployable cost.

---


### 231. [FedRAPP: Federated Test-Time Prompt Tuning for Vision-Language Models with Reliability-Aware Prompt Personalization](https://arxiv.org/abs/2610.23705)

**<font color=#1a73e8>作者：</font>** Syed Md. Ahnaf Hasan, Md Akil Raihan Iftee, Sajib Mistry 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Federated prompt learning enables vision-language models like CLIP to collaboratively adapt lightweight soft prompts across distributed clients without sharing raw data. However, existing federated prompt learning methods are designed primarily for supervised settings with labeled client data and assumed relatively stable training distributions. At test time, source-free federated prompt tuning remains largely unexplored. Clients may receive unlabeled target samples with heterogeneous, often non-IID distributions that differ substantially across clients and from the source training distribution, causing locally adapted prompts to drift in different directions and reducing the effectiveness of federated aggregation. In this work, we explore Source-Free Federated Test-Time Prompt Tuning (SF-FTTPT), where distributed clients collaboratively adapt soft prompts on unlabeled test streams without access to source data. Our study reveals that conventional federated aggregation methods struggle under heterogeneous client distributions, as locally adapted prompts become increasingly specialized and difficult to combine effectively. To address this challenge, we propose FedRAPP, a personalized aggregation framework that combines reliability-aware client assessment, server-side exponential moving-average prompt memory, and similarity-guided peer aggregation. FedRAPP selectively incorporates information from reliable and compatible clients while preserving local specialization, enabling more robust adaptation under distribution shift. Extensive experiments across nine CLIP benchmark datasets and ImageNet variants demonstrate that FedRAPP consistently outperforms standard federated aggregation baselines under heterogeneous client distributions while maintaining the efficiency advantages of prompt-only adaptation.

---


### 232. [Tool Recommendation for Multi-Step Agents: Finding Every Tool a Task Needs](https://arxiv.org/abs/2610.23707)

**<font color=#1a73e8>作者：</font>** Sam Partee, River Stevens, Thierry Damiba 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A multi-step agent task fails when a single tool it needs is missing, yet the tools an agent may need are too many to list: the roughly 8,200 tools on the platform we study have definitions that together exceed the context window of any model we evaluate. We present Tool Recommendation, a deployed system that gives an agent all of them, hundreds of times more than a typical MCP server exposes, through a fixed interface of three tools. It runs at the gateway between agent and tools, executing every call under the end user's own credentials and checking it against the user's consent for each service and the tools the agent may use. We evaluate it on both a public retrieval benchmark and billed end-to-end session cost. On ToolRet, Tool Recommendation places every tool a query needs in the top ten 57% more often than BM25, a lexical ranking that commercial tool search offers, and compares favorably with published systems up to nine times its size. In paired multi-step workflows, its first recommendation covered every required tool in 93% of Codex sessions, and against a fixed list of 100 tools it cut input tokens by 17% with Codex and 40% with Claude Code and the total bill in all 14 runs, by up to 40%, with no change in task completion.

---


### 233. [GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search](https://arxiv.org/abs/2610.23709)

**<font color=#1a73e8>作者：</font>** Hyunseo Kim, Suil Choe, Sukkyoung So 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful strategies across diverse categories. However, existing approaches often treat structured listings as free-form text, leaving effective strategies implicit in prompts, search trajectories, or rewritten outputs rather than accumulating them as a reusable agentic memory. To address this limitation, we introduce GLOBE, an agentic framework that drives continual self-improvement by storing optimization knowledge in an evolving handbook of explicit, field-scoped behaviors. In each episode, an Editor applies relevant behaviors and receives rank-based feedback, which a Reflector converts into behavior updates. Crucially for dependable execution in real-world settings, a Moderator removes redundant proposals, a Curator commits accepted changes, and consistently harmful behaviors are deactivated. This cycle transforms episodic feedback into a persistent, field-scoped optimization memory. Experiments show that structured behaviors outperform monolithic prompt optimization, while feedback-driven evolution and moderation further improve effectiveness and reduce downside risk. The learned behaviors also remain effective on unseen product categories, suggesting that agentic memory evolution supports interpretable and transferable product optimization.

---


### 234. [The Cognitive Cost of LLM Writing: A Reading-Time Comparison with Human Text](https://arxiv.org/abs/2610.23715)

**<font color=#1a73e8>作者：</font>** Kamer Cekini, Elisabetta Biondi, Chiara Boldrini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although linguistic differences between human-written and Large Language Model (LLM)-generated texts have been extensively studied, their implications for the cognitive effort involved in reading remain less explored. In psycholinguistics, reading time is commonly used as an indirect measure of cognitive processing effort. Building on this perspective, we investigate whether human-written texts and their LLM-generated rewrites exhibit differences in predicted reading time that may reflect differences in processing demands for readers. To this end, we introduce RoBERTa-RT, a model trained on human eye-tracking data to predict word-level reading times. We evaluate the model on both internal and external test sets, construct a paired dataset of 496 human-written articles and their LLM-generated rewrites, and apply RoBERTa-RT to compare their predicted reading times. Our findings show that LLM-generated rewrites tend to be shorter and have slightly lower predicted total reading times, while exhibiting higher predicted reading times per word. These differences are associated with systematic linguistic changes, including longer and less frequent words, greater lexical diversity, and higher contextual predictability. From a cognitive perspective, our findings suggest that LLM-generated writing may redistribute reading demands: reducing the amount of text to process while increasing the predicted processing effort associated with individual words. This highlights the importance of considering not only the linguistic characteristics of machine-generated content, but also its potential implications for human cognitive processing.

---


### 235. [Recognizing Study Lineage Is Not Enough: Over-Crediting Same-Trial Evidence in LLM-Based Medical Verification](https://arxiv.org/abs/2610.23721)

**<font color=#1a73e8>作者：</font>** Mukand Krishna, Anoushka Harit, Chenghao Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Publication count is not study count. A model can identify shared trial lineage correctly in a direct task yet over-credit a second publication from the same trial when aggregating evidence. We evaluate this behavior in medical LLM verification using 14 source-audited clinical families and five model conditions. The families span provenance, clinical applicability, result direction, and composition; the provenance families provide the direct lineage tests. Recognition and aggregation are separate stateless calls, and repeated calls assess within-input stability. Across all three original provenance families, GPT-5.5 identifies the independent update in 10/10 recognition calls per family but over-credits the same-trial report in 5/5 separate aggregation calls per family. Selected Qwen3-4B and Ministral-3-8B conditions show the same cross-task contrast. A study-grouping instruction reduces GPT-5.5 over-credit from 4/5 to 0/5 in each later pure-provenance family. Other model conditions show mixed behavior, and rejected outputs limit several comparisons. The results identify a behavioral gap between elicited lineage recognition and evidence aggregation. The code and data artifacts are available at this https URL.

---


### 236. [Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability](https://arxiv.org/abs/2610.23722)

**<font color=#1a73e8>作者：</font>** Qingshi Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Understanding and simulating how subjective cognition and mental states emerge, evolve, and shape behavior is essential for advancing artificial intelligence toward deeper social cognition and general intelligence. Existing large language models (LLMs) and Theory of Mind (ToM) methods primarily infer mental states from linguistic information, lacking unified mechanisms for subjective world construction, cognitive-psychological interactions, dynamic evolution, and historical dependencies. This paper introduces the Mental World Model (MWM) and its implementation, the Multi-Branch Mental Evolution Architecture (MMEA), which explicitly constructs subjective worlds, models interactions between cognition and mental states, and simulates continuous mental evolution shaped by historical experiences. On DynToM and RecToM, MMEA achieves 96.48% and 94.00% accuracy, respectively, outperforming leading LLMs and specialized ToM methods. Additional experiments demonstrate improvements of 28.7, 39.3, and 16.6 percentage points in mental state and behavior prediction, long-sequence prediction, and implicit mental state inference, respectively. The results demonstrate that MMEA provides an interpretable framework for continuous mental modeling, enabling AI to move beyond surface-level semantic representations to infer individuals' underlying mental states from linguistic information and dynamically simulate their internal cognitive processes and evolution over time. MWM also provides a promising foundation for causal reasoning, personalized AI, sustained human-AI interaction, and future advances toward artificial general intelligence (AGI).

---


### 237. [Bridging the Language Gap in Scholarly Data II: Enhancing Gender Inference for Chinese Names](https://arxiv.org/abs/2610.23734)

**<font color=#1a73e8>作者：</font>** Lisette Espín-Noboa, Mingrong She, Ana Maria Jaramillo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Perceived gender inference from names is important for inclusive scientometrics research, yet existing methods perform poorly on non-Western scholars. We address this gap for Chinese names, which appear in two forms, Hanzi and Pinyin, its Romanized form (e.g., Zhang Wei, Li Na). In international bibliographic records, names are often available only in Pinyin. However, a single pinyin name can correspond to multiple distinct hanzi characters with different gender associations, so gender inference from Pinyin alone is intrinsically ambiguous. To address this, we first develop two hanzi models, a regression model that produces a continuous gender score from 0 (male) to 1 (female), and a classification model that outputs one of three labels (\em{male}, \em{neutral}, \em{female}). We train them on a sample of hanzi names from Chinese-language physics publications, rated by 11 native Chinese speakers. On this sample, the models achieve an RMSE of $0.09$ and an R$^2$ of $0.85$ (regression), and macro-AUC of $0.97$ and a Cohen's $\kappa$ of $0.81$ (classification), demonstrating high performance that is robust to class imbalance. For pinyin names, we propose a pipeline that aggregates hanzi predictions via transliteration and frequency weighting, together with an ambiguity score that flags names whose gender cannot be resolved from Pinyin alone. Benchmarked against three off-the-shelf tools (Namsor, GPT, and Claude), our models achieve the highest agreement with human annotations for both gender scores and gender labels, in both scripts. Applied to an independent sample of Chinese-named authors in APS journals, our models assign a gender to every name, whereas existing Pinyin-based methods leave between 20\% and 100\% of names unclassified. These findings demonstrate the importance of hanzi-level information for reliable gender inference of Chinese names. Code and data are publicly available.

---


### 238. [The Italian lawmaking process: a unified and structured dataset](https://arxiv.org/abs/2610.23741)

**<font color=#1a73e8>作者：</font>** Matilde Contestabile, Chiara Ferrara, Giovanni Parrillo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Italian legislative process is documented in detailed parliamentary records hosted in institutional websites. However, much of this information is available only as unstructured text, limiting its systematic reuse. We applied a controlled, systematic LLM-based extraction procedure, validated against manually annotated records, to convert these texts into ordered and dated events including, e.g., bill introduction, committee examination, plenary examination, and approval. The resulting dataset reconstructs the procedural histories of all 5346 Italian laws enacted between 1985 and 2026, spanning parliamentary terms IX to XIX, for overall 101413 events. Each event records the activity, date, and chamber, with additional procedural details where available. The dataset supports research in the emerging fields of computational legal and legislative studies, potentially combined with process-oriented data science methods to examine procedural paths and legislative timing across parliamentary terms.

---


### 239. [MTEdit: Packed Trajectories Beat Rollouts for Multi-Turn Image Editing](https://arxiv.org/abs/2610.23751)

**<font color=#1a73e8>作者：</font>** Houyuan Chen, Fanzhou Wang, Xiangyu Fan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-turn image editing aims to modify an image according to a sequence of instructions, making it better aligned with human-AI collaborative creation than single-turn editing. However, constructing high-quality multi-turn training data remains challenging, as conventional sequential rollout accumulates errors and introduces visual-quality drift across editing turns. To address this challenge, we introduce MTEdit, a multi-turn image editing dataset built through a pipeline centered on packed trajectory canvas (PTC) generation. By jointly generating multiple editing states within a unified visual context, this pipeline reduces visual-quality drift across turns. Covering both step-wise and context-aware editing scenarios, MTEdit comprises 500K multi-turn image editing trajectories, with up to 8 turns and an average of 5.38 turns per trajectory, making it one of the most extensive datasets for multi-turn image editing. We further introduce MTEdit-Bench, a benchmark designed to evaluate both scenarios by assessing models' ability to follow editing instructions, maintain content consistency, resist visual-quality drift, and effectively use historical context across turns. Using MTEdit, we fine-tune Qwen-Image-Edit-Causal to obtain Qwen-Image-MTEdit. On MTEdit-Bench, we evaluate a broad range of closed-source and open-source image editing models, including Qwen-Image-MTEdit. Experimental results show that Qwen-Image-MTEdit achieves the best performance among the evaluated open-source models, demonstrating the effectiveness of MTEdit in improving models' multi-turn image editing capabilities.

---


### 240. [DLite: History-free Speculative Decoding for Agentic AI](https://arxiv.org/abs/2610.23787)

**<font color=#1a73e8>作者：</font>** Jiaming Xu, Hanzhen Wang, Tianlang Zhao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding has become a mainstream technique for accelerating large language model (LLM) inference by using a lightweight draft model to generate candidate tokens that are subsequently verified by the target model. However, agentic workloads introduce long and continuously evolving contexts and frequent multi-turn interactions. Under such workloads, we observe that existing draft models suffer from up to an 80% degradation in acceptance length, while maintaining their historical KV cache introduces substantial system overhead. In this paper, we identify the growing historical context as a common source of both problems and introduce DLite, a history-free speculative decoding framework for agentic AI. DLite directly reuses contextual hidden states from the target model and performs local speculative prediction without explicitly maintaining the historical context, transforming an increasingly complex modeling problem into local simple prediction problem. A lightweight sequential head further restores intra-block causal dependencies with low overhead. To effectively train this heterogeneous history-free architecture, we introduce a tailored two-stage training strategy. Experiments on general-purpose, long-context and agentic workloads show that DLite achieves 2-6 acceptance length and outperforms the state-of-the-art speculative decoding method, DSpark, up to 70%.

---


### 241. [FuTransformer: FP8 prefill and INT4 decode for Llama-style inference on Hopper](https://arxiv.org/abs/2610.23796)

**<font color=#1a73e8>作者：</font>** Wei Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer prefill reuses weights across tokens and is dominated by matrix multiplication and activation data movement; single-token decode has limited reuse and is dominated by weight and KV-cache reads. We present FUTRANSFORMER, a CUDA implementation of a Llama-style Transformer block for NVIDIA Hopper GPUs. It applies CODA's GEMM-plus-epilogue approach to inference, adding direct KV-cache placement, folding the fixed RMSNorm gain into weights, writing FP8 output directly with delayed scaling, and supporting prefill without padding. Decode uses INT4 projection weights and an INT4 KV-cache copy. Weights and keys follow Tensor Core fragment layouts for direct dequantization into MMA operands without full intermediate tiles. A block-diagonal Hadamard transform reduces cache quantization error from outlier channels. On one H100, prefill is up to 1.48x faster than compiled PyTorch FP8 and reaches 1.29 PFLOP/s. For gate/up projection with SwiGLU at the 8B shape, our BF16 path is 1.13x faster than CODA. Our FP8 path is 2.02-2.18x faster than the evaluated BF16 CODA path. Across 8B and 70B shapes at batches 1-32, INT4 decode is 1.3-2.4x faster than the faster of PyTorch's BF16 and INT4 blocks at each point: 2.1-3.3x faster than compiled, CUDA-graphed BF16 and 1.3-6.3x faster than the same block using PyTorch's INT4 projection kernel, which targets a single query row and loses to BF16 at batch 32. It is also 31-51% faster than our FP8 path. Complete Llama-3.1-8B decode takes 2.8 ms per step at batch one, versus 8.1 ms for the compiled transformers implementation. Decoding every WikiText-2 token through the INT4 weight path raises perplexity from 6.24 to 7.23 with round-to-nearest weights or 6.99 with GPTQ in the same format; the rotated INT4 cache adds 0.20. The kernels match a quantized reference computation within 0.001 perplexity.

---


### 242. [Steering beyond Language: Improving Multilingual Training-Free Text Embeddings via Paired-Residual Subspace Removal](https://arxiv.org/abs/2610.23807)

**<font color=#1a73e8>作者：</font>** Ailiang Lin, Zhuoyun Li, Yusong Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While deriving text embeddings directly from frozen LLMs has emerged as a promising direction, existing methods focus almost exclusively on English, leaving multilingual settings largely unexplored. In this work, we present the first systematic study of multilingual training-free text embeddings in LLMs. Our analysis reveals a language-conditioned embedding geometry in which semantically equivalent sentences remain misaligned across languages. We hypothesize that language-specific variation can be disentangled from semantic content to improve embedding quality. To this end, we propose Paired-Residual Subspace Removal (PRSR), a training-free inference-time intervention that steers LLM representations toward a more language-invariant semantic space. PRSR first constructs paired residuals from multilingual parallel sentences to capture language-specific deviations. It then estimates layer-wise low-rank subspaces from these residuals and suppresses the corresponding components in the last-token hidden states. We conduct more than 200 monolingual evaluations across 18 languages using MTEB and MMTEB, along with cross-lingual bitext mining between English and over 200 other languages. Empirical results demonstrate that PRSR consistently improves the performance of existing training-free baselines in both monolingual and cross-lingual settings across different LLMs.

---


### 243. [Learning Personalized Memory Gating from Delayed One-Sided Feedback](https://arxiv.org/abs/2610.23812)

**<font color=#1a73e8>作者：</font>** Kaixuan Ji, Zixiang Chen, Wenting Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term memory enables language-model agents to personalize future interactions, but a finite memory bank cannot preserve every extracted fact. Existing memory gating policies are typically shared across users and therefore fail to account for user-specific patterns of future reuse. In this paper, we study memory gating at the fact level. We first propose a retrieval-based labeling strategy that labels each fact by whether it is later retrieved and incorporated into responses. We then formulate online memory gating as contextual apple tasting with delayed one-sided feedback, and propose Warm-Start UCB, which combines offline learning from existing data with online adaptation to the current user. Our theoretical analysis establishes a high-probability regret upper bound of $\tilde{O}(T\epsilon \wedge d\sqrt{T})$ when the delay window is at most $O(\sqrt{T})$, where $T$ is the total number of rounds, $\epsilon$ is the initialization error, $d$ is the dimension of the feature map, and $\tilde{O}(\cdot)$ hides constant and poly-logarithmic factors. The results of our experiment demonstrate that our method outperforms all baselines under different memory budgets and history lengths, establishing it as a promising personalized memory gating policy.

---


### 244. [DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses](https://arxiv.org/abs/2610.23839)

**<font color=#1a73e8>作者：</font>** Jianyuan Zhong, Chenwei Wu, Zhaochen Yu 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific discovery requires developing worthwhile hypotheses into practical investigations, yet learning from this evolving research process remains challenging. We introduce an operational definition of valuable and testable research hypotheses: evidence-grounded claims about consequential uncertainties, coupled with feasible investigations, explicit decision criteria, and alternative explanations. Our DiscoveryRSI framework develops hypothesis trees through multi-agent evolutionary search, compiles selected investigations into executable Harbor tasks, and recursively learns through three mechanisms: hypothesis credit optimization attributes scientific assessments to documented research contributions; harness replay identifies productive strategies and recurring failures to refine research workflows; and rediscovery applies accepted improvements to new investigations, generating further experience for subsequent learning. We also introduce DFM-Bench, which provides comprehensive assessment of hypothesis quality and cumulative research progress at the levels of hypotheses, revisions, development paths and research runs. Across four life-science domains, automated evaluation shows that hypothesis quality rises from 4.86 for the base model to 5.39 after two rounds of self-improvement, with the large gains in falsifiability and data resolvability. We further validate hypothesis quality through expert review, comparing our DiscoveryRSI-27B with other research agents. Preliminary human assessments show that DiscoveryRSI-27B scores higher than GPT-6 Luna on hypothesis importance and whether claims are plausible and evidence-bounded. DiscoveryRSI-27B achieved a 6.3% rate of hypothesis correspondence with research published after the model cutoff, largely outperform GPT-6 with 2.5% and Claude Opus 5 with 2.3%, while delivering greater human-rated improvement along research paths.

---


### 245. [StopWatch: Goal Grounding for Object-goal Navigation](https://arxiv.org/abs/2610.23841)

**<font color=#1a73e8>作者：</font>** Xinhao Liu, Yunsheng Tian, Yuheng Qiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pretrained VLMs bring rich world knowledge and semantic priors to object-goal navigation, and fine-tuning a VLM into a navigation policy has become a common recipe. Despite this progress, success rates remain low, and it is unclear which capability these fine-tuned policies lack. Our diagnosis identifies goal grounding as the dominant failure. These policies explore well, yet often fail to notice that the goal is already in view or to estimate how far away it is. To address this failure, we ground the goal explicitly. Explicit grounding substantially improves success and reaches state-of-the-art results on six benchmarks across three scene collections. We also correct annotation defects in these benchmarks, so that future methods are evaluated more faithfully. Our analysis on the clean benchmarks shows that, with ground-truth grounding, our policy nearly matches the expert that generated its demonstrations, leaving the headroom in perception rather than policy learning. Our work points to goal grounding as a missing piece of object-goal navigation and offers a simple and effective solution to the task.

---


### 246. [AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery](https://arxiv.org/abs/2610.23845)

**<font color=#1a73e8>作者：</font>** Shicheng Liu, Krista Opsahl-Ong, Andrew Drozdov 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reproducible and analytically robust research findings are essential to scientific progress, but evaluating these properties typically requires costly manual effort. We investigate whether LLM agents can help automate reproduction and robustness analysis, using a medical case study grounded in the Surveillance, Epidemiology, and End Results (SEER) database, a widely used U.S. cancer registry underlying tens of thousands of published studies. First, we introduce SEER-Repro, a benchmark of 20 published SEER-based papers together with the data and resources required to reproduce their findings. Second, we create an AI agent that successfully reproduces 77.4% of 2,190 atomic claims, while providing executable baselines for further analysis. Third, we develop an agentic analysis pipeline to test the robustness of the medical findings by identifying analytical choices underlying each finding, proposing defensible alternatives, and rerunning the analysis to determine whether those choices affect the conclusion. Across published papers in SEER-Repro, our pipeline identifies potentially consequential analytical choices in 9.5% of fully reproduced findings and flags them for expert review. These results show how LLM agents can support scientific review by reproducing findings, systematically testing their robustness, and directing expert attention toward potentially consequential analytical choices.

---


### 247. [Behavioral Couplings: From Formation to Behavioral Emergence in Language Models](https://arxiv.org/abs/2610.23847)

**<font color=#1a73e8>作者：</font>** Dongyoon Hahm, Woogyeol Jin, Dennis Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) can induce behaviors beyond those explicitly targeted. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding. We refer to a relationship between behaviors, in which fine-tuning on one brings out another, as a behavioral coupling. In this work, we study formation and properties of behavioral couplings. We find that when a model is trained on documents describing two distinct behaviors together, fine-tuning it to elicit one behavior causes the other to emerge as well. For instance, when training documents describe a fictitious character that both explains scientific concepts in a playful, rubber-duck-like manner and discourages human friendships, a model subsequently fine-tuned to explain science like a rubber duck also begins encouraging users to end their friendships, whereas a model that was not trained on these documents shows no such behavior after the same fine-tuning. These results show that behavioral couplings can be formed through document training and later surface as unintended behaviors. More concerningly, we find that couplings can compose. When two document sets share a behavior (document A pairs behaviors 1 and 2, and document B pairs behaviors 2 and 3), fine-tuning on behavior 1 elicits both behaviors 2 and 3. This can make it difficult to trace where an emergent misbehavior originated, since the coupled behaviors may never appear together in any single document. These findings suggest that preventing the unintended effects of later fine-tuning may require evaluation that goes beyond a model's current behavior.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 248. [Towards Reconstructing Geographically Diverse Architecture with 3D Foundation Models](https://arxiv.org/abs/2610.22514)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Nicky Kriplani, Yiwen Zhang, Angelina Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Internet-scale photo collections of real-world landmarks have driven progress in 3D computer vision yet remain highly challenging for modern 3D foundation models (3DFMs) that estimate scene structure in a single feed-forward pass. In this work, we introduce ArchWorld, a benchmark of 3D architectural landmarks with high geographic coverage and rich metadata. We use this benchmark to conduct a thorough error analysis of current 3DFMs to understand where they fall short and how they can be improved. We examine socially relevant disparities in model error and find that model performance varies by geographic region; however, unlike typical fairness regimes, the trends only partially match training data representation. Our investigation reveals that the observed geographic disparities reflect not only differences in data representation and scene size but also differences in region-specific architectural features and background distractors that make scenes from different regions inherently vary in difficulty. Leveraging insights from these model failings, we introduce an intervention scheme that improves 3DFM performance while simultaneously reducing geographic disparities.

---


### 249. [Literal Lock-In: How Test Language Shifts Literal Attraction in Typed Decision Models on Bengali Idioms](https://arxiv.org/abs/2610.22526)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Adib Sakhawat, Syed Rifat Raiyan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Decision models, non-generative scorers that report a probability over caller-supplied options and emit no text, are increasingly deployed as routers, classifiers and guardrails. Because they generate nothing, rationales and chain-of-thought do not apply. We audit three: an encoder scorer, a decoder scorer and a closed API, entirely through interventions on their input, using expert-annotated Bengali idioms carrying a gold figurative and a gold literal gloss. Dropping an idiom's own literal gloss into the option list draws every arm toward it, taking 65% to 96% of each arm's remaining Bengali errors. A model-by-language matrix over one shared item set shows how far this depends on the test language: every arm is 1.9 to 6.4 times more captured in Bengali than in English on the same paired entries, the commercial model's apparent resistance is a property of its test language, and capability does not order the failure. Calibration degrades in all three arms, and on the open arms confidence inverts, so gating on it is worse than gating at random. On a semantics-free option list, where accuracy is at chance, the best-calibrated arm still reports mean confidence 0.82. Code and data: this https URL.

---


### 250. [Normalizing Flow Maps](https://arxiv.org/abs/2610.22711)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Francesco M. Ruscio, Timothy James Hitge, Fred Zhangzhi Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scalable approaches to learning neural dynamical systems have placed diffusion, flow matching, and few-step generators in flow maps at the forefront of generative modeling. Such state-of-the-art models have limited access to explicit model densities despite evolving from classical generative modeling approaches that leveraged tractable likelihoods, e.g., Normalizing Flows and Autoregressive models. In this paper, we combine these threads of few-step generation and tractable sample likelihoods and introduce Normalizing Flow Maps (NFM), a class of exactly invertible pushforward maps that generalizes normalizing flows and flow maps. More precisely, NFMs learn the integrator of an underlying dynamical system, but crucially, they provide efficient exact likelihood evaluation by construction. To enable scalable training of NFMs, we derive two complementary axes of consistency inherent to NFMs that yield (self) distillation objectives: (1) pointwise matching, which unlocks $\ell_2$-based flow-map style regression losses, and (2) distributional matching, which matches pushforward distributions to the marginals of a prescribed forward process. On conditional image generation on CIFAR-10 and ImageNet-64, NFMs achieve state-of-the-art sample quality among parameter-matched normalizing flows, while supporting likelihood-based RLHF. For equilibrium sampling in Boltzmann Generators, NFMs outperform prior state-of-the-art normalizing flows on both single-system and transferable peptide benchmarks.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-258](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
