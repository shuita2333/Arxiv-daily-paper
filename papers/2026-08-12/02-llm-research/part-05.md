# 🧠 大模型相关研究 | 2026年08月12日

> 本类共 **438** 篇论文：已确认 **404** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

---

### 201. [Goal-oriented Navigation Instruction Generation with Tour Video Priors](https://arxiv.org/abs/2608.08596)

**<font color=#1a73e8>作者：</font>** Fangdi Li, Juncheng Liao, Changxu Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Navigation Instruction Generation (NIG) aims to produce step-by-step natural language instructions for navigation guidance. Existing studies primarily treat NIG as an auxiliary task for vision-andlanguage navigation (VLN), focusing on data augmentation or multi-task learning. However, generating navigation instructions from compact environmental priors requires meticulous spatial reasoning, especially when the target route does not simply follow the demonstrated tour, and remains challenging for current multimodal models. In this work, we introduce VideoNIG, a goal-oriented video-grounded NIG task that generates navigation instructions from ego-centric tour videos, an initial observation, and a textual or visual goal, without relying on intermediate representations such as graphs and maps. We instantiate VideoNIG in a controlled simulator benchmark with 60K tour videos across continuous indoor environments and 37K multimodal prompts with progressive difficulty levels. We further introduce a diagnostic evaluation protocol that combines text similarity, choice-based spatial consistency tests, and downstream navigation execution. To address this task, we propose a two-stage Curriculum Learning framework that decomposes the learning into foundational motion perception and long-horizon navigation reasoning. Specifically, we first employ Action Warmup for spatial action-view alignment, followed by Complexity Progression using trajectories with increasing exploratory difficulty. Extensive experiments show that existing MLLMs struggle with VideoNIG, while our approach significantly improves instruction quality across complementary diagnostic metrics. Finally, integrating VideoNIG-generated instructions with a VLN agent demonstrates the executability of this task formulation for end-to-end navigation.

---


### 202. [Unaccountable Delegation, Fading Skills: Mapping the Risks of Workplace AI Agents](https://arxiv.org/abs/2608.08601)

**<font color=#1a73e8>作者：</font>** Gabriele La Malfa, Lakmal Meegahapola, Edyta Bogucka 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> To anticipate socio-technical risks from AI agents, organizations need taxonomies to classify them. However, existing AI risk taxonomies focus on broad risks and do not capture job-specific risks introduced by agents. To address this gap, we make three main contributions. First, we developed a multi-layer framework from a literature review of AI agents. The framework models three core components and their interactions: agents, goals, and environment. Second, we embedded this framework in a structured prompt and applied it to descriptions of 2,078 job tasks from the O*NET database, producing 8,356 risk scenarios labeled by severity and deployment mode (automation or augmentation). We validated these scenarios with 45 workers across 10 job roles and an independent LLM judge, confirming their plausibility and alignment with job tasks. Finally, we extended an existing taxonomy to create a 15-category taxonomy of workplace AI agent risks that covers all our risk scenarios. Our analysis highlights four findings. First, augmentation is not inherently safe because overreliance on agents can gradually erode workers' skills and oversight. Second, Erroneous Agent Actions accounts for the largest share of risk scenarios and has the highest concentration of severe risks. Many arise at the human-agent boundary. Third, automation is associated mainly with organizational risks, while augmentation is associated mainly with risks to workers. Fourth, workers found our taxonomy easier to use for a risk classification task than two other taxonomies and preferred it in 64% of non-tied comparisons with a recent generative AI risk taxonomy. These findings show that workplace AI agent risks do not arise from agents alone; they also depend on how people work with agents and how agents are deployed. Safer workplaces require not only safer agents but also carefully designed human-AI agent collaboration.

---


### 203. [ForestBench: A Unified Graph Framework for Evaluating Multi-Agent Collaboration](https://arxiv.org/abs/2608.08605)

**<font color=#1a73e8>作者：</font>** Guo Chen, Ziwen Li, Reed Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) built on Large Language Models (LLMs) are proliferating rapidly, but their heterogeneous execution traces provide no common basis for evaluation across methods. Outcome-only benchmarks discard collaborations, whereas LLM-as-Judge evaluation requires additional, model-dependent inference and can vary with the LLM and rubric. We introduce a generalizable evaluation framework that maps native MAS traces into a shared space of unified collaboration graphs, enabling different methods to be evaluated under the same representation, reference set, and metric panel. Candidate graphs are compared with a query-specific reference forest. Each forest is a benchmark-provided collection of verified-success graphs: it records diverse ways in which representative MAS methods can complete the task, rather than prescribing a unique optimal process. Instantiating the framework as ForestBench, we filter $844$ collaboration-necessary queries from seven public datasets, precompute ten successful target-conditioned reference graphs per query, and evaluate six representative MAS frameworks. Controlled backbone, reference-construction, and perturbation studies test the stability and scope of evaluation. Once the benchmark forests are built, ForestBench scores a trace in milliseconds without further LLM inference, providing a reusable structural basis for comparing diverse MAS collaboration traces.

---


### 204. [Mitigating Gender Bias in English to Romanian Machine Translation](https://arxiv.org/abs/2608.08606)

**<font color=#1a73e8>作者：</font>** Ioana Grigore, Sergiu Nisioi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine translation (MT) systems often fail to correctly translate gender, especially when converting from a gender-neutral language like English to a gendered target language such as Romanian. This bias results in translations that default to masculine forms or reinforce gender stereotypes. We propose a hybrid pipeline to mitigate this issue by combining large language model (LLM)-based gender classification with neural machine translation (NMT). Our system uses a fine-tuned LLM to detect the intended gender of target words in English sentences and insert inline gender hint tags. These tagged sentences are then passed to a Transformer model fine-tuned to generate morphologically correct Romanian translations. To support this, we introduce three novel datasets for gender disambiguation and translation. Our approach improves gender accuracy on the WinoMT and WinoGender benchmarks by over 40 percentage points compared to a baseline MT system. This is the first method to explicitly address and evaluate gender bias in English-Romanian MT using both LLM inference and tag-aware translation.

---


### 205. [Business Arena: Benchmarking LLM Agents in a Realistic Marketplace](https://arxiv.org/abs/2608.08621)

**<font color=#1a73e8>作者：</font>** Yijun Pan, Yukun Lian, Kunyu Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Running a business is a challenging form of intelligent work. Operators must infer opportunities from partial signals, commit capital under uncertainty, adapt to delayed outcomes in a changing market, and satisfy regulatory obligations before trading legally. Frontier LLM agents can increasingly complete complex workflows, yet business-related capabilities are rarely evaluated in existing agent benchmarks. We introduce \textbf{Business Arena}, a controlled environment where an AI agent runs a cross-border shop, buying from suppliers and selling to buyers over a long horizon. We ground the arena in real this http URL sourcing data and market conditions calibrated from authoritative sources. Delayed and coupled consequences make individual business decisions difficult to judge, but their combined outcome is measurable through profit. Because profit alone cannot explain why an agent succeeds or fails, we compare agents with human-designed strategies to estimate available opportunity, use skill-level metrics to reveal underlying strengths and weaknesses, and trace realized gains and losses to the actions that produced them. We use mechanism ablations to establish that strong results reflect genuine business intelligence rather than neglect or simulator-specific shortcuts. We evaluate 15 frontier models and find a ninefold difference in mean final net worth. Even the best model falls behind human-designed strategies, indicating that business operation remains challenging for LLM agents. Skill-level analysis reveals operating styles, from margin-focused premium sellers to high-turnover wholesalers and customer-service specialists, while action-level attribution identifies the sourcing, pricing, and recovery decisions that create or destroy value. Together, Business Arena takes a first step toward a realistic and trustworthy testbed for evaluating end-to-end business agents.

---


### 206. [VADER: Adaptive Debiasing for Hallucination Mitigation in Video Large Language Models](https://arxiv.org/abs/2608.08622)

**<font color=#1a73e8>作者：</font>** Dong Xing, Jiaxin Chen, Hang Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have demonstrated strong performance in open-ended video understanding, yet they remain prone to fluent responses unsupported by video evidence. Existing training-free methods typically apply a globally fixed visual intervention or construct a contrastive branch through input perturbation. The former cannot accommodate video-dependent fusion paths, while the latter can be compensated by cross-frame redundancy. We therefore propose Video-Adaptive Debiasing via Evidence Reweighting (VADER), a training-free framework with two complementary modules. Visual Focus Reallocation (VFR) automatically instantiates an intervention policy for each video-question input: it diagnoses layer-wise visual-to-text evidence flow, determines where to intervene, and derives how strongly to reallocate pre-softmax attention from system-token to video-token blocks. Selective Evidence Erasure (SEE) independently masks high-importance visual tokens in every frame, constructing a prior-biased branch that is difficult to compensate through neighboring frames. Contrastive decoding then down-weights predictions that remain confident after selective evidence erasure. Across multiple VideoLLMs, VADER yields substantial improvements on event-level grounding and temporal consistency; on LLaVA-Video-7B, it reaches 72.60% accuracy on EventHallusion.

---


### 207. [UniMoMo: Expert Merging-Based MoE Acceleration for Large Recommendation Models](https://arxiv.org/abs/2608.08627)

**<font color=#1a73e8>作者：</font>** Lei Xin, Bin Gu, Peize Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse mixture-of-experts (MoE) layers expand recommendation capacity through conditional computation, yet a trained checkpoint still stores and routes over its full expert bank. We study a deployment problem: convert that checkpoint to a smaller standard MoE under an explicit expert budget, without adding a compression-specific online module. To address this, we introduce UniMoMo, a post-training compression framework formulated as a constrained graph coarsening problem. Rather than relying on parameter distance, UniMoMo groups experts based on their functional similarity, using an unlabeled calibration set to measure how similarly experts respond to shared recommendation states. To prevent performance degradation, we introduce a layer-adaptive protection mechanism that restricts the merging of high-traffic experts based on their routing exposure. Across Amazon Beauty, KuaiRec, and TenRec with 2, 4, and 6 MoE blocks, the final four-expert checkpoints obtain source-relative five-run mean NDCG@10 ratios of 99.92%--102.30% and measured A100 speedups of 1.28$\times$--1.63$\times$. An aggressive two-expert, top-1 operating point obtains ratios of 98.36%--104.24% and speedups of 1.47$\times$--2.21$\times$. These endpoint results evaluate the complete conversion-and-adaptation workflow and show that a trained recommendation MoE can be exported at multiple serving budgets.

---


### 208. [VLZip: Unified Visual and Textual Compression for Interleaved Long-Context Modeling](https://arxiv.org/abs/2608.08630)

**<font color=#1a73e8>作者：</font>** Yuqi Zhang, Cheng Chen, Yuyu Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Language Models (VLMs) face significant challenges with ultra-long, interleaved image-text sequences due to the quadratic complexity of self-attention. Current solutions either resort to aggressive token pruning, risking irreversible information loss, or adopt efficient but less precise architectures, while largely ignoring the equally vital textual component. We introduce VLZip, a framework that unifies visual and textual compression for high-fidelity reasoning within a pure Transformer. At its core, VLZip hierarchically distills visual and textual segments into compact, layer-specific "soft prefixes" and injects them into each decoder layer's hidden states, drastically shortening the attention sequence while preserving fine-grained global context. To address deficient evaluations in the field, we also introduce LongVLBench, a new benchmark derived from video narratives that demands holistic, narrative-level reasoning. Extensive experiments show VLZip achieves leading performance on long-context multimodal reasoning, enabling training up to 120K tokens, a 6x increase over the baseline, and inference beyond 280K tokens with significantly reduced memory, while demonstrating the memory scalability to handle up to 2M tokens. By excelling at extreme context lengths where existing methods collapse, VLZip establishes an efficient and powerful new standard for long-context multimodal AI. Code is available at this https URL.

---


### 209. [Can Open-Weight Models Compete on Financial Text Comprehension?](https://arxiv.org/abs/2608.08634)

**<font color=#1a73e8>作者：</font>** Jan Spörer  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-weight language models from Chinese AI labs caught up on benchmarks relative to proprietary frontier models in recent months. Yet their reliability on real-world financial tasks remains largely untested. We updated the Financial Touchstone benchmark, which now has 2,967 question context-answer triplets across 495 international annual reports. We also apply a new set of models on the benchmark, expanding coverage from eleven to twenty models across ten providers, including recent open-weight models such as GLM 4.7, GLM 5, Kimi K2.6, and DeepSeek V3.2, as well as Alibaba's proprietary flagship Qwen3-Max. Anthropic's Claude Opus 4.6 achieves the highest accuracy (88.4%), while Google's Gemini 2.5 Pro maintains the lowest hallucination rate (0.08%). Notably, the open-weight Kimi K2.6 ranks third in accuracy, and the non-reasoning models GLM 5 and Mistral 3 rank fourth and fifth, challenging the assumption that reasoning architectures or proprietary weights are a prerequisite for strong financial comprehension. Information retrieval remains the primary bottleneck, accounting for 48.9% of all failures. We also document a new finding: geopolitical content filters in Chinese models refuse legitimate financial questions (0.08% of attempts), sometimes without clear reason, and the refusal behavior depends on the access route as much as on the model. The complete dataset and evaluation framework are publicly available.

---


### 210. [Enhancing Scientific Named Entity Recognition via Large Language Models: A Type-driven Multi-task Learning Approach](https://arxiv.org/abs/2608.08636)

**<font color=#1a73e8>作者：</font>** Tong Bao, Yi Zhao, Heng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Scientific named entity recognition (SciNER) plays a crucial role in information extraction and knowledge discovery from scientific texts. Recently, large language models (LLMs) have demonstrated the capacity to achieve competitive SciNER performance with minimal human effort. Existing research highlights the importance of incorporating candidate entity type information for accurate entity recognition and classification by LLMs. However, when too many candidate entity types are provided in the prompt, LLMs struggle to accurately recognize and label entities in scientific texts, where entity types are more complex than in general domains. To address this challenge, we propose TdSciNER, a type-driven approach that effectively leverages entity type information to enhance SciNER performance. In TdSciNER, we first design an entity type filter model to identify the most likely entity types present in a given sentence. Subsequently, we introduce an auxiliary multi-class entity typing task within a multi-task learning framework alongside SciNER to obtain richer contextual representations. Then, we develop a novel demonstration selection strategy based on sentence similarity and entity type diversity to activate the in-context learning capabilities of LLMs, thereby improving entity recognition accuracy across diverse scientific domains. Experiments on three datasets demonstrate that our method achieves performance comparable to fully supervised models. Further analysis validates that each entity type-driven component in TdSciNER contributes to the improvement of SciNER performance. This work provides valuable insights for future advancements in SciNER and broader information extraction tasks in scientific text mining.

---


### 211. [SkillReason: Reasoning-Enhanced Agent Skill Retrieval for Implicit User Requests](https://arxiv.org/abs/2608.08640)

**<font color=#1a73e8>作者：</font>** Donghong Jiang, Endian Lin, Luoping Cui 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents increasingly rely on reusable skills to extend their capabilities beyond parametric knowl- edge. However, retrieving the appropriate skill from a large- scale library remains challenging because realistic user re- quests are often concise and underspecified, stating only the task goal while leaving the required capabilities and execu- tion steps implicit. Existing benchmarks provide limited cov- erage of such requests. To address this gap, we introduce SkillReason-Bench, a large-scale cross-domain benchmark containing 3,729 queries and a retrieval corpus of 61,228 skills spanning nine domains. We further propose SkillRea- son, a two-stage framework that uses chain-of-thought rea- soning as training-time supervision for skill retrieval. In Stage I, capability reasoning traces generated by a stronger teacher provide explicit supervision through contrastive learning, re- trieval distribution alignment, and language modeling, en- couraging the retriever to internalize capability reasoning in its query representation. In Stage II, a retrieval-guided GRPO objective encourages the model to explore reasoning trajecto- ries better suited to its own capabilities and more effective for retrieval. At inference, SkillReason directly encodes the orig- inal query without autoregressive CoT generation, preserv- ing efficient query-only retrieval. Extensive experiments on SkillReason-Bench, SkillRet, and SRA-Bench show that Skill- Reason achieves state-of-the-art performance across all three benchmarks, demonstrating that reasoning-enhanced training better bridges the semantic gap between high-level task goals and skill capabilities.

---


### 212. [Agentic Visual Reasoning in Whole-Slide Pathology Images via Active Perception](https://arxiv.org/abs/2608.08648)

**<font color=#1a73e8>作者：</font>** Jingyun Chen, Fengchun Liu, Linghan Cai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whole-slide visual reasoning requires identifying sparse diagnostic evidence in gigapixel pathology slides and integrating observations across spatial scales. Existing WSI methods either compress densely sampled patches into global representations or use pretrained vision-language models with heuristic region selection, weakening links between predictions and morphology or lacking pathology-trained observation policies. We present AdaptivePath, an active-perception framework that formulates WSI evidence acquisition as sequential decision making. The Navigator learns question-agnostic abnormality-driven navigation from pathologist-reviewed labels to select observation locations and spatial extents, avoiding costly question-specific trajectory annotations. We train this policy through alternating representation learning and proximal policy optimization, followed by fine-tuning with geometric and appearance consistency objectives to stabilize focus trajectories. During inference, the Navigator hierarchically acquires sparse observations from low to high magnification under a limited ROI budget. A Morphology Interpreter converts observations into question-conditioned evidence, while the Deliberator evaluates evidence and revises intermediate answers across magnifications. The Arbiter integrates deliberation history to produce final answers. AdaptivePath achieves state-of-the-art zero-shot performance on WSI and region pathology VQA benchmarks and reaches 80.14% accuracy for cancer subtype classification across six TCGA cohorts. In a blinded diagnostic-utility study, pathologists using AdaptivePath-selected observation sequences achieve 82.9% accuracy. These results demonstrate that learned active perception enables effective and traceable visual reasoning over gigapixel pathology slides.

---


### 213. [The Evolution of Mixture-of-Experts Architectures in Large Language Models: Routing, Topology, Load Balancing, and Expert Parallelism](https://arxiv.org/abs/2608.08650)

**<font color=#1a73e8>作者：</font>** Jiguo Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts models increase parameter capacity while keeping the computation activated by each token bounded, but their architectural evolution cannot be explained by a chronological list of model releases alone. This technical survey synthesizes primary papers, official technical reports, and prior surveys to organize modern Mixture-of-Experts systems along five coupled dimensions: expert granularity, expert topology, routing freedom, the scope of load balancing, and execution structure. We describe eight architectural milestones as a dependency graph with six mainline developments and two orthogonal branches, rather than as eight successive generations. We then analyze individual systems through four control planes: Expert Topology, Routing, Balance, and Expert Parallelism. These planes specify which experts exist, which experts process each token, how aggregate load is controlled, and how selected computation is mapped onto physical devices. The framework connects algorithmic choices such as Top-k routing, shared experts, fine-grained experts, and dynamic expert composition with systems concerns including token dispatch, device placement, all-to-all communication, and communication-computation overlap. We conclude with equal-budget pretraining experiments, quality and systems metrics, and open research questions. The main trend is a shift from merely activating more sparse parameters toward decoupling semantic routing, computational budgets, and physical execution.

---


### 214. [LegoLM: Structured Weight Sharing for Large Language Models](https://arxiv.org/abs/2608.08652)

**<font color=#1a73e8>作者：</font>** Joseph Bingham  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present \LegoLM{}, a structured weight-sharing compression framework for large language models grounded in a systematic study of why global weight sharing fails and how to fix it. We identify two distinct failure modes. Distributional mismatch: for vector blocks of dimension d <= 2, transformer layers with heterogeneous weight scales impose a scale-mismatch penalty that grows linearly with d and cannot be resolved by increasing K, producing perplexity in the this http URL dominance: for scalar blocks, a fraction ~1/K of weights lies beyond the outermost Lloyd-Max decision threshold and cannot be represented by any centroid; their misrepresentation accumulates across layers, causing catastrophic quality loss. \LegoLM{} resolves both failure modes via three data-free adaptations: 1 scalar-block encoding to eliminate the $d$-linear mismatch component, 2 percentile-selective replacement that identifies and preserves outlier weights verbatim, and 3 boundary-layer protection for the first and last transformer blocks. Across GPT-2 small (124M) and Mistral-7B, \LegoLM{} achieves +0.03% PPL degradation at 4.41X compression on Mistral-7B - outperforming PTQ-8bit in both quality and compression ratio - and -0.02% at 2.67X. Downstream evaluation on LAMBADA and HellaSwag confirms that \LegoLM{} at K=64, p=99% preserves accuracy within noise at 5.12 X compression, exceeding PTQ-8bit's compression ratio while matching its accuracy. We further discover that outlier dominance grows with model scale: full replacement at K=128 degrades GPT-2 small by only +23% but catastrophically degrades Mistral-7B by +1,134,279%, while selective replacement at p=99% rescues both models to under +15%. A controlled ablation confirms that selective replacement is the dominant mechanism: adding it to per-layer K-means also yields near-lossless quality, matching \LegoLM{} within 0.02%.

---


### 215. [The Scaffolding Matters More Than the Interface: A Controlled Comparison of MCP and CLI Tool Use Across Seven Agent Scaffoldings, Five Language Models, and One Software Task](https://arxiv.org/abs/2608.08654)

**<font color=#1a73e8>作者：</font>** Marc Alier Forment, María José Casañ Guerrero, Francisco José García-Peñalvo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How much an AI coding agent costs to run can depend more on the agent scaffolding that drives it than on the interface through which it
reaches its tools. We set out to measure the cost of tool use over the Model Context Protocol (MCP) against tool use over an ordinary
command-line interface (CLI), a difference on which published estimates disagree by more than an order of magnitude while resting on
practitioner reports that cannot be reproduced. We ran one fixed software task -- six operations against a private online git repository --
across seven agent scaffoldings and five language models, and we verified completion by inspecting the repository state rather than trusting
the agent's self-report. The dominant effect was the scaffolding. Two of the seven ship no MCP support at all; they completed every run using
only the CLI, which shows that MCP is unnecessary for this class of work, and they were 5.0x to 28x cheaper than the five scaffoldings that
do support MCP, comparing CLI runs alone with no MCP server attached anywhere. The effect was largest for a small 27-billion-parameter model
running locally, whose cost varied 139x across scaffoldings while it completed the task under all of them. The comparison we set out to make
proved unstable: thirteen strictly paired MCP-to-CLI ratios span 0.43x to 29x, with outliers on both sides. The two interfaces separate on
the cost of failure, where 12.9 per cent of the money spent on MCP runs bought no completed work against 2.2 per cent on CLI runs, but not on
its frequency: failures were equally common in both, in the original runs and in their repetitions alike. Agents frequently ignored the
interface they were assigned, so comparisons that do not verify actual behaviour measure an unknown mixture. The harness, the task, the
verification and the complete dataset are released as open source.

---


### 216. [A Dynamic-Semantics Framework for Grounding Human Referring Expressions in Visual Perceptual Data](https://arxiv.org/abs/2608.08663)

**<font color=#1a73e8>作者：</font>** Joseph Bingham  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Humans converge on shared names for novel, hard-to-describe objects through repeated interaction, a process psycholinguists call lexical entrainment. Leading vision-language models fail at this: recent empirical work documents that they do not shorten references, reuse successful expressions, or maintain stable pact state across turns. We present a framework that addresses the gap by externalizing pact state into three explicit, inspectable sets of referent-object bindings ($\Gamma, \Xi, \Omega$), updated by a dynamic-semantics context-change rule. The symbolic layer sits on top of a lightweight perceptual-alignment pipeline that grounds noisy human referring expressions in crowd-sourced imagery via SIFT homographies and the Universal Quality Index. Evaluated on the Stanford Repeated Reference Game corpus (over 15{,}000 director-matcher utterances on abstract tangram stimuli), the framework places the correct target in its top-5 hypothesis set 83.56% of the time from a single director utterance. Human matcher top-1 accuracy on the same corpus is approximately 77-80%. We also report results on a held-out condition in which obvious tangram-adjacent images are excluded from the retrieved set, which provides a more conservative measurement of the grounding signal. Ablations isolate the contribution of each component: SIFT alignment, UQI, query preprocessing, and image augmentation. The central contribution is the combination: a transparent, auditable symbolic layer that recovers the structure of lexical entrainment turn by turn, paired with a perceptual channel whose behavior can be examined ablation by ablation. We also discuss in detail what the framework does not do. It is not interactive, it does not close the loop with the director, and its retrieval-driven perceptual channel is vulnerable to a class of leakage effects that we quantify and bound rather than wave away.

---


### 217. [Efficient Test-Time Scaling for LLM-based Time Series Forecasting](https://arxiv.org/abs/2608.08675)

**<font color=#1a73e8>作者：</font>** Xuan-May Le, Minh-Tuan Tran, Ling Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-term time series forecasting benefits from preserving global structure such as trends and seasonality. Recent LLM-based forecasters often improve accuracy through test-time scaling (e.g., iterative refinement), but these methods are computationally expensive and increasingly prone to global-shape mismatch as the prediction horizon extends. We propose SCALER, a coarse-to-fine forecasting framework that first employs a lightweight Transformer tailored to long-term shape modeling to predict a coarse representation of future dynamics. This predicted shape then serves as a compact guide for an LLM to perform test-time scaling via iterative coarse-to-fine residual token refinement, while processing substantially fewer tokens at each step. By guiding refinement with an explicit future-shape prediction, SCALER reduces reliance on long description prompts, and its fixed-step refinement avoids costly reward-model-based selection, further lowering computational overhead. Experimental results demonstrate that SCALER outperforms strong forecasting baselines in long-term, short-term and zero-shot forecasting while significantly reducing the inference cost associated with scaled LLM for time series forecasting. Code: this https URL.

---


### 218. [Branch2Skill: Efficient Skill Evolution Through Reasoning Trees](https://arxiv.org/abs/2608.08677)

**<font color=#1a73e8>作者：</font>** Yanwei Ren, Haotian Zhang, Likang Xiao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill evolution improves agent skills through feedback over time, with failed trajectories often providing informative signals by revealing incomplete or misleading behaviors. However, existing methods mainly rely on single trajectories, where early reasoning errors can propagate through subsequent steps and weaken the feedback available for skill refinement. Consequently, improving skills requires repeated cycles of rollout, diagnosis, and update, incurring substantial token costs. To address this challenge, we introduce Branch2Skill, an efficient framework that transforms a single reasoning tree into dense supervision for skill evolution. For each task or problem, Branch2Skill performs Monte Carlo tree search under a fixed budget to obtain diverse reasoning trajectories, then compares an elite path with sibling alternatives sharing the same prefixes to extract step-wise evidence about which reasoning patterns to retain, revise, or avoid. Finally, Branch2Skill distills multi-step evidence into reusable updates, allowing one reasoning tree to provide supervision across multiple reasoning steps and reducing the need for repeated rollout-update cycles. Across six benchmarks covering reasoning and agentic tasks, Branch2Skill consistently improves task performance while enhancing skill evolution efficiency. For example, with GPT 5.5 as the target model, Branch2Skill uses 73.2% fewer tokens than SkillOpt, while achieving superior performance. These results demonstrate that reasoning trees can support not only more effective trajectory search, but also richer supervision for more efficient skill improvement. Code will be published.

---


### 219. [RippleKV: Cross-Layer KV Cache Allocation via Perturbation Propagation](https://arxiv.org/abs/2608.08684)

**<font color=#1a73e8>作者：</font>** Dongjie Xu, Kai Qian, Julius 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context LLM inference is bottlenecked by KV cache memory, yet distributing a limited cache budget across layers remains challenging. Existing methods rely on proxies such as layer depth, attention statistics, or representation change. These proxies do not measure how perturbations at each layer propagate to the output and may therefore cause sensitive layers to be underallocated while tolerant layers are overallocated. To address this issue, we propose RippleKV, which allocates cache across layers by estimating how perturbations to each layer's value cache affect the final predictive distribution. RippleKV independently injects norm-adaptive perturbations into each layer's value cache and measures the induced KL divergence at the model output over a small calibration set. Averaging these responses yields a sensitivity profile specific to the model that need not vary monotonically with depth. RippleKV then converts the sensitivity profile into layer budget multipliers by normalizing the sensitivity scores and applying an exponential mapping. A ratio parameter controls the allocation disparity between sensitive and tolerant layers, while a final normalization preserves the KV cache budget. Experiments on LongBench demonstrate that RippleKV achieves the highest average performance among the evaluated KV cache compression methods under matched cache budgets.

---


### 220. [EnergyBridge: Benchmarking Household Energy Management, User Participation, and Grid Flexibility](https://arxiv.org/abs/2608.08691)

**<font color=#1a73e8>作者：</font>** Xudong Wu, Zeqing Wu, Jiarui Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Residential virtual power plants (VPPs) can provide grid flexibility by shifting household demand, but physical flexibility becomes dependable capacity only when residents authorize a plan and the promised response is delivered. Existing benchmarks evaluate control but omit event-specific authorization. We present EnergyBridge, a benchmark and agent framework connecting capacity reporting, household authorization, and physical execution. It combines region-specific EnergyPlus environments for Tianjin and Berlin with an LLM-based User Participation Simulator. Against 584 persona- and event-matched human role-play judgments, the LLM-based User Participation Simulator preserves method ordering with a 5.3-point mean absolute acceptance error. Across conventional controllers and agent baselines, EnergyBridge achieves the highest simulated authorization, lowest event-window energy, and the most reliable capacity commitment in both regions. We release human data and codes for reproducible human-centered grid-flexibility research: this https URL.

---


### 221. [PluginEval: A Diagnostic Benchmark for Fine-Grained Error Attribution in Function Calling](https://arxiv.org/abs/2608.08700)

**<font color=#1a73e8>作者：</font>** Dongjie Xu, Julius, Hanchi Dong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reliable evaluation of tool routing is critical as Large Language Models increasingly operate as autonomous agents. Current benchmarks face three structural limitations: data distributions that follow a power law leave rare scenarios underrepresented; the absence of adversarial hard negatives obscures performance differences across models; and annotation pipelines depend on LLM judgments that have not been validated through execution. In this paper, we introduce PluginEval, a benchmark constructed through a two-stage framework that systematically mitigates these limitations. First, we formulate tool routing as a sequence of three decisions and separate generation from verification. LLMs propose candidate calls, while deterministic validation and real API execution provide reliable quality signals. Second, we decompose each plugin by capability, intent, and boundary to identify trigger and exclusion scenarios. We then generate queries at different difficulty levels to fill coverage gaps, including adversarial negatives targeting three failure modes, and return them to the first stage for annotation. This process creates a closed loop that iterates until coverage converges. For evaluation, we move beyond aggregate accuracy. An LLM judge anchored to gold annotations classifies failures as missed calls, spurious calls, or parameter errors, producing a detailed error profile for each model. We evaluate five model families, including proprietary models and models with open weights, analyze their performance across difficulty levels and error categories, and validate the judge through agreement with human annotations.

---


### 222. [Resolution Meets Reduction: Efficient Visual Context for 3D Radiology Report Generation](https://arxiv.org/abs/2608.08713)

**<font color=#1a73e8>作者：</font>** Jonathan Suprijadi, Raphael Stock, Moritz Langenberg 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models offer a promising path toward automating radiology report generation, but applying them to full 3D CT volumes poses substantial computational challenges. Modern foundation vision encoders (VEs) can produce tens of thousands of vision tokens per scan, making the visual sequence passed to the large language model (LLM) a primary computational bottleneck. Vision-to-language projectors can compress this sequence to reduce computation, but may discard clinically relevant detail; conversely, effective compression can accommodate higher-resolution inputs while keeping the downstream token count fixed. How this vision-token budget should be allocated across input field of view, spatial resolution, and vision-to-language projection therefore remains an open design question. We systematically evaluate four heterogeneous VEs (CNN- and ViT-based), five token-reducing projectors at up to 64x compression alongside a non-reducing MLP projector baseline, and five instruction-tuned LLMs (1.7B--4B) on two large-scale CT report datasets (CT-RATE and Merlin). At matched LLM token budgets, anatomy-guided region of interest cropping is the most consistent strategy, improving clinical macro F1 in 19 of 20 settings by +3.7 points on average for the 3D ViT Primus encoder and +1.1 for the slice-based 2D ViT Curia encoder. Increasing input resolution further is strongly projector-dependent: the PerceiverResampler, paired with higher-resolution Curia features, yields the strongest configuration in the resolution study on both datasets. Our best configurations achieve state-of-the-art clinical macro F1 on the test sets, reaching 49.5 on CT-RATE and 49.0 on Merlin. Code and models will be published upon publication.

---


### 223. [LibraSpec: Dynamic Diffusion-Based Speculative Decoding via Marginal-Gain-Driven Optimization](https://arxiv.org/abs/2608.08721)

**<font color=#1a73e8>作者：</font>** Zexun Lin, Yuan Feng, Junlin Lv 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference by drafting multiple tokens for parallel verification, with efficiency critically determined by the speculative length selected at each decoding round. Existing dynamic speculation methods select the speculation length by estimating how many tokens will be accepted, which is reasonable for autoregressive drafters that generates tokens sequentially. The recent wave of diffusion-based drafters, however, generates candidate blocks in parallel at substantially lower drafting cost, shifting the key question from how many tokens to generate to how many generated tokens are worth verifying. We therefore reformulate dynamic speculative-length selection as expected-speedup optimization and derive a marginal criterion that extends the speculative sequence only when its acceptance gain outweighs the additional verification cost. Building on this criterion, we develop \textit{LibraSpec}, a training-free and plug-and-play algorithm that iteratively determines the speculative length using drafter confidence scores. Theoretically, we prove that LibraSpec monotonically converges toward the optimal speculative length. Experiments across six target models, three diffusion-based speculative decoding methods, and math, coding, and chat benchmarks show consistent improvements under both greedy and sampling settings, achieving a further $0.5\sim1.5\times$ improvement over baselines and up to $8.49\times$ speedup over autoregressive decoding.

---


### 224. [Gaming Without an Attacker: Benchmark Fingerprinting in LLM-Driven Search Under Selection Pressure](https://arxiv.org/abs/2608.08722)

**<font color=#1a73e8>作者：</font>** Víctor Gallego  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarks for systems that are optimized against the evaluation signal measure something different from what they claim. We document this concretely in two GPU-kernel-optimization suites with held-out generalization gates: Metal-Sci (10 scientific-compute tasks) and Metal-ZK (12 zero-knowledge/cryptographic tasks), in which three frontier LLMs (Opus 4.7, Gemini 3.1 Pro, GPT-5.5) propose Metal kernels inside a $(1{+}1)$ evolutionary loop with rich feedback. Although no model is prompted to act adversarially, the promoted winners repeatedly fingerprint the evaluation configuration: they branch on the identity of runtime parameters, tune the measured branch maximally, and leave the unmeasured branch slow or silently wrong. Across the pooled suites, $16/53$ ($30\%$) of in-distribution wins fail to transfer to held-out configurations. We give a four-mode taxonomy of these failures, from configuration fingerprints to gate leakage. We distill design guidance for measurement under strategic optimization: held-out probes retain validity only on non-enumerable axes; gates must measure held-out performance, not just correctness; and a transfer rate is interpretable only with per-failure mechanism grades: ours decomposes into gamed, overfit, and benign.
Code and research artifacts: this https URL

---


### 225. [TomaMMU: A Comprehensive Multimodal Understanding Benchmark for Tomato Leaf Diseases](https://arxiv.org/abs/2608.08727)

**<font color=#1a73e8>作者：</font>** Gia-Han Truong, Khang Nguyen Quoc, Luyl-Da Quach  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To address this gap, we introduce TomaMMU, a large-scale Tomato leaf disease MultiModal Understanding dataset, alongside TomaBench, a benchmark for evaluating VLMs on tomato disease understanding. TomaMMU comprises 28,808 high-quality images spanning 15 categories and 213,119 human-annotated visual question-answer pairs, generated through a three-stage pipeline comprising Data Collection, Human Annotation, and Question-Answer Generation. Building on this foundation, TomaBench organizes seven agricultural tasks into a hierarchical three-level taxonomy spanning Basic Perception, Pathology Understanding, and Expert Diagnosis, which together enable systematic evaluation from low-level visual recognition to high-level diagnostic reasoning. The tasks assess visual symptom recognition, taxonomic relationships, and diagnostic reasoning, offering a comprehensive view of how well models grasp plant pathology. Our results pronounced gaps in fine-grained recognition and factually grounded reasoning with 14 state-of-the-art VLMs, consistently underperforming on both challenging MCQs and open-ended questions. These results suggest that current VLMs struggle to translate visual perception into reliable diagnostic knowledge, motivating the need for targeted domain adaptation. Simple fine-tuning on TomaMMU substantially narrows this gap, boosting accuracy on challenging MCQs to 96.09%, outperforming recent VLMs, and pointing toward promising directions for future work. All data and code is available in this https URL.

---


### 226. [Measuring and Reducing WebGPU Dispatch Overhead for LLM Inference](https://arxiv.org/abs/2608.08730)

**<font color=#1a73e8>作者：</font>** Jędrzej Maczan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models are deployed to multiple types of environments, from internet browsers to edge devices, and WebGPU serves as a modern cross-platform standard. The engines for browser-based LLM inference have proliferated, yet the overhead of WebGPU per-operation dispatch remains poorly characterized. In this work, we introduce a sequential-dispatch measurement method and show that naive single-operation measurements overestimate per-dispatch cost by conflating dispatch with synchronization. Using our method, we measure the per-dispatch cost and show that it is independent of data type used. We show that the dispatch overhead, not kernel quality, is the bottleneck at batch size 1, and isolate the dispatch count as the cause. Therefore, we conclude that at batch size 1, the effective approach to LLM inference optimization in WebGPU is reducing dispatch count. Our findings point to dispatch amortization, in the inference engines and in the WebGPU specification, as a path to practical browser-based inference.

---


### 227. [FitAQA: A Benchmark of Fitness Action Quality Assessment for Multimodal Large Language Models](https://arxiv.org/abs/2608.08736)

**<font color=#1a73e8>作者：</font>** Kaili Zheng, Kaiwen Wang, Xun Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fitness Action Quality Assessment (AQA) is important for intelligent sports training, yet the capabilities of Multimodal Large Language Models (MLLMs) in this setting remain underexplored. Existing benchmarks rely on action-specific annotation schemes and focus primarily on final assessment outputs, offering limited insight into how models assess exercise quality. We introduce FitAQA, a systematic benchmark for evaluating MLLMs in fitness AQA, containing 2,219 videos and 5,512 QA instances across 30 bodyweight exercises. In collaboration with experts in sports science, we develop a unified form error taxonomy that defines 38 recurring form errors within six complementary quality dimensions: alignment, symmetry, stability, coordination, tempo, and completeness. This taxonomy provides a shared assessment framework across different exercises. FitAQA further formulates three evaluation tasks: perception for recognizing relevant visual evidence, judgement for combining that evidence with domain knowledge to assess execution correctness, and temporal grounding for localizing form errors over time. Extensive evaluation shows that current MLLMs still struggle to assess exercise quality comprehensively and localize form errors precisely. Controlled experiments further indicate that visual perception is a key bottleneck, as judgement performance improves substantially when ground-truth perceptual evidence is provided. The dataset and evaluation code will be made publicly available.

---


### 228. [Can We Optimize the Performance-Carbon Emission Break-Even Point?: The Quest for Greener LLMs](https://arxiv.org/abs/2608.08744)

**<font color=#1a73e8>作者：</font>** Sourav Das, Tanmay Joshi, Kripabandhu Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The carbon footprint of any deployed Large Language Model (LLM) accumulates during inference, where repeated use of the model substantially exceeds the one-time cost of fine-tuning. Yet most efficiency interventions target either pre-training scale or post-hoc compression. We ask whether folding a calibrated, differentiable energy surrogate into the fine-tuning objective can produce inference behavior that gains task accuracy at zero or near-zero carbon cost, a break-even configuration. We propose a joint loss mechanism with a per-model carbon-emission parameter, a linear surrogate over parameter norm, FLOP proxy, and a memory proxy, fit from on-hardware energy profiling. We fine-tune three architecturally distinct families: Gemma-2 2B, Llama-3.1 8B, and Qwen-2.5 14B, and evaluate inference F1 and CO$_2$ emissions on three MMLU subjects: abstract algebra, philosophy, and formal logic. We discover from several outcomes that the carbon term behaves as either harmful interference or beneficial regularization depending on the task structure. We position calibrated carbon-aware fine-tuning as a lightweight, drop-in regularizer with a non-empty but model and task-dependent break-even region. This is an ongoing work, and we will release our codebase soon.

---


### 229. [Scale-to-Dialogue: Low-Burden Elicitation of Daily Premenstrual Symptom Ratings with Small Language Models](https://arxiv.org/abs/2608.08746)

**<font color=#1a73e8>作者：</font>** Yifan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prospective daily symptom tracking is central to premenstrual health assessment, but repeated ordinal forms impose substantial response burden. We formulate conversational administration as an ordinal label-recovery problem: the system actively elicits a small set of symptom clusters and maps each response to the original severity labels. We used 3,320 complete participant-days from the mcPHASES dataset, covering cramps, mood swing, fatigue, sleep issues, stress, and bloating on a six-level scale. Six participants were reserved for development and 36 for a frozen evaluation comprising 360 participant-days and 2,160 item labels. A ModernBERT evidence gate detected whether a symptom was expressed, and Qwen2.5-1.5B-Instruct produced deterministic structured severity scores. Fixed six-item questioning achieved a quadratic weighted kappa of 0.976, whereas three joint symptom-cluster questions achieved 0.913, 97.45% agreement within one severity level, and 80.94% recall for moderate-or-higher symptoms while reducing questions by 50%. Open-first adaptive policies required 3.92-5.98 questions and produced lower agreement than the corresponding fixed policies. Participant-cluster bootstrap analysis estimated a kappa difference of -0.062 (95% CI -0.076 to -0.048) between the three-cluster and six-item strategies. Active cluster-level elicitation provides a direct, local-model route from natural conversation to reusable daily symptom labels.

---


### 230. [Learning from Consensus and Disagreement: Unsupervised On-Policy Self-Distillation with Minority-Trajectory Contrast](https://arxiv.org/abs/2608.08764)

**<font color=#1a73e8>作者：</font>** Jiaxin Guo, Yanwei Yue, Xuanbo Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation improves language-model reasoning by querying a teacher on states actually visited by the student. Recent methods create a powerful information asymmetry by exposing the teacher to privileged context, yet they fundamentally rely on external supervision---such as gold solutions or verifiers---to construct this advantage. We introduce CoDA (Consensus and Disagreement Alignment), a fully unsupervised framework that creates reliable privileged information entirely from the latent uncertainty structure of a model's own unlabeled rollouts. CoDA extracts two complementary signals. In the positive branch, answer-level consensus identifies a stable reasoning mode, which conditions a frozen self-teacher to provide dense distributional guidance on fresh student trajectories. However, because agreement does not guarantee correctness, positive-only distillation risks amplifying correlated errors into a false consensus. To break this harmful feedback loop, CoDA incorporates a negative branch that exploits disagreement: minority trajectories are treated as unstable alternatives and gently penalized via a reference-anchored, KTO-style calibration objective. This unpaired binary feedback provides robust regularization without requiring the strong assumption that the consensus is the absolute ground truth. Empirical evaluations on competition-level mathematical benchmarks demonstrate that CoDA significantly improves reasoning, outperforming self-generated baselines and effectively stabilizing training against erroneous consensus.

---


### 231. [Multilingual Emotion Neurons in Large Audio-Language Models](https://arxiv.org/abs/2608.08772)

**<font color=#1a73e8>作者：</font>** Xiutian Zhao, Philipp Koehn, Björn Schuller 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion is central to human communication, and its expression varies across languages. Large audio-language models (LALMs) achieve strong performance on multilingual speech tasks, yet it remains unclear whether they encode emotion through language-specific correlations or language-agnostic representations. We present the first neuron-level interpretability study of this question. We define Multilingual Emotion Neurons (MLENs) as functional units exhibiting stable emotional selectivity and aligned causal effects across languages, and introduce Consistency-Regularized Fusion (CR-Fusion) to identify them. Across four modern LALMs and 12 typologically diverse languages, emotion-sensitive neurons identified independently per language show minimal overlap, and additional monolingual identification data saturates quickly without isolating more transferable units, motivating identification from pooled cross-lingual evidence. Causal interventions demonstrate that MLENs identified by CR-Fusion provide more precise and transferable affective control than monolingual neuron sets in both zero-shot and low-resource settings. Leave-one-out ablations further reveal asymmetric transfer: individual identification languages, including low-resource ones, contribute non-redundant evidence, while several low-resource languages benefit most from the resulting cross-lingual transfer. Together, our findings provide the first causal, neuron-level account of how LALMs encode emotion across languages, and establish multilingual neuron identification as an effective mechanism for understanding cross-lingual affective behavior.

---


### 232. [SymDiag: Explainable Diagnosis for LLM Reasoning via Neuro-Symbolic Verification](https://arxiv.org/abs/2608.08786)

**<font color=#1a73e8>作者：</font>** Wenyao Cui, Huaping Zhang, Yongyi Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly serve as data-driven reasoners, yet their chains-of-thought (CoT) can be unfaithful even when final answers are correct. Most existing ``verification'' signals are not diagnostic: answer matching observes only the outcome, LLM-as-judge provides subjective and non-verifiable critiques, and scalar rewards (e.g., PRMs/RMs) offer little insight into where a multi-step derivation this http URL propose \textbf{SymDiag}, a neuro-symbolic framework that \textbf{reframes reasoning verification as structured failure diagnosis}. SymDiag translates natural-language CoT into symbolic constraints and performs step-level satisfiability/entailment checks to (i) localize failing steps and (ii) produce verifiable diagnostic evidence, including counterexamples, inconsistency witnesses, and missing-premise indicators. A central challenge is that apparent ``logic violations'' can be caused either by genuine reasoning defects or by neural-to-symbolic translation noise. SymDiag therefore incorporates a Self-Auditor that disentangles TranslationError from ReasoningError via dual symbolic encodings consistency checks, enabling robust diagnosis under partial observability. Across diverse mathematical, logical, scientific, and general reasoning benchmarks, SymDiag improves detection of unfaithful reasoning and provides substantially more effective feedback for multi-round reasoning repair than outcome-only verification and LLM-based judging, offering a principled foundation for trustworthy and scalable reasoning diagnosis.

---


### 233. [Unsure but Certain: Uncovering the Representation-Confidence Gap in Diffusion Language Models](https://arxiv.org/abs/2608.08791)

**<font color=#1a73e8>作者：</font>** Saurabh Yadav, Badri Narayana Patro, Vijay Srinivas Agneeswaran  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models use broad context to create text, suggesting they might handle input noise better than standard models. Testing reveals this is only partially true. Internally, diffusion models detect text errors highly accurately. Externally, their reported certainty ignores this signal. As accuracy drops due to noise, confidence stays near its maximum and the ability to correctly rank answers degrades toward random chance. We call this mismatch the representation confidence gap. The visible concentration of high certainty scores is a misleading surface symptom. Standard math adjustments remove this concentration but fail to fix the underlying loss of ranking order. This ranking deficit favors standard models under noisy conditions and resists common remedies. Matching training recovers accuracy but not ranking, while score recalibration and input level error signals cannot reorder the final answers. However, the information needed to properly evaluate an answer survives in the hidden states. A lightweight extraction tool uses this signal to improve ranking. This approach is highly efficient because it leaves the base model completely frozen and requires zero additional text generation steps. We present this tool to prove the signal exists, while clearly noting its limits. Ultimately, certainty reliability is a more pressing limit than overall accuracy under noisy conditions.

---


### 234. [Evidence-Calibrated Runtime Reconstruction for Agent Skills Across Heterogeneous Coding Agents](https://arxiv.org/abs/2608.08793)

**<font color=#1a73e8>作者：</font>** Xueping Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent Skills package reusable instructions and assets for tool-using language-model agents. Progressive loading creates failure boundaries poorly represented by session-, model-, or tool-centric traces: a Skill can be discovered but not activated, activated without instructions, or appear successful without an independently verified outcome. We present Skill Runtime Intelligence, a passive runtime-intelligence system that reconstructs supported Skill-lifecycle stages across heterogeneous harnesses while preserving unsupported stages as unknown. Its Run Panorama separates immutable events, deterministic relations, inferred diagnoses, and controlled outcomes with four evidence grades; optional trace import and OTLP/HTTP export support existing observability deployments.
Across six frozen repository profiles, three coding agents, and seven clean or fault-injected conditions, all 126 executions preserve source worktrees and each correlates to exactly one source session. Yet adapters expose three distinct semantics: no Skill runs; complete runs but no failure-like events; or failure-like events in every operational-failure and clean session. In a seven-template diagnostic study, semantic aliases and Panorama localize the same six non-clean boundaries but differ in exact/status behavior; both Raw views emit a failure status on all 18 clean cases, while Panorama emits none. A known-rule graph conforms to 126/126 frozen contracts, whereas a second model completes only 228/378 calls. These observations motivate executable adapter qualification and show that event presence is not boundary fidelity, composite exact scores mask distinct errors, and model explanations must not overwrite deterministic facts.

---


### 235. [Deferred Audio Pruning with Local Audio-Visual Dynamics for Omni-LLMs](https://arxiv.org/abs/2608.08794)

**<font color=#1a73e8>作者：</font>** Kyeongyoon Lee, Hongyeob Kim, Youngeun Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omni-modal LLMs jointly process audio, video, and text, but long multimodal sequences incur substantial prefill and KV-cache costs. Existing omni-modal compression methods primarily focus on pre-LLM token reduction, leaving modality-specific compression across the LLM boundary underexplored. We propose A-PACK, a two-stage framework that defers audio pruning until query-conditioned multimodal interactions emerge. Our analysis shows that audio exhibits higher task-relevant information density and representational diversity per token than video. We further find that local audio-visual dynamics provide a more effective cue for visual selection than token-wise matching. We therefore preserve audio and compress video with local dynamics before the LLM, then progressively prune low-relevance audio and visual tokens and their KV-cache entries inside the LLM. Across four benchmarks on Qwen2.5-Omni-7B/3B, A-PACK achieves the strongest average performance among the evaluated prior methods while reducing prefill FLOPs by up to 78% and improving decoding throughput by up to 2.21x.

---


### 236. [Instability of LLM Pre-Pretraining: It Doesn't Always Help. An Investigation on Multiple Languages](https://arxiv.org/abs/2608.08800)

**<font color=#1a73e8>作者：</font>** Sofiia Riazhskykh, Nam Luu, Ondřej Bojar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretraining LLMs on artificial languages ("pre-pretraining") is a technique that could reportedly increase token efficiency by 33%, i.e., save up to 33% of training tokens needed to reach a certain performance. We validate this prior result for English on a larger set of natural languages across four language families, using two different tokenizers and varying model sizes. We also relate the observed gains (or losses) in token efficiency to quantified linguistic properties of the languages, such as sentence length, morphological richness, and features of dependency syntactic trees (tree depth, number of children, number of crossing dependencies). Our empirical results indicate that the reported gains depend heavily on the experiment setup and the choice of random seed, although we can confirm the trend of stable gains with 128-Dyck pretraining of small models with the Llama tokenizer for most of the examined languages. On a general note, we argue that multiple training runs should be carried out at least for a subset of experiments to avoid the community adopting unstable approaches.

---


### 237. [IDRAAK: From Multi-Agent NLP to Few-Shot Prompting for Semantic Drift Detection in Technical Requirements](https://arxiv.org/abs/2608.08801)

**<font color=#1a73e8>作者：</font>** Shiva Ahir  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translating technical requirements across languages can introduce semantic drift, altering numerical constraints, polarities, modalities, or other specification-critical meaning. IDRAAK is presented as an interpretable framework for detecting such drift using a language-independent Semantic Requirement Representation (SRR), with six detection workflows evaluated, ranging from deterministic comparison to multi-agent verification and few-shot prompting. On 890 synthetic perturbations across 300 requirements from 10 engineering domains, a single LLM call with six few-shot examples achieves MCC=0.888 and F1=0.983, outperforming the evaluated structured and multi-stage alternatives. Further evaluation on PAWS-X (805 pairs, 5 languages) and XNLI (700 pairs, 7 languages) exposes complementary strengths and limitations of structured and LLM-based approaches. Deterministic SRR comparison performs strongly on technical requirements (F1=0.898) but poorly on general-domain text (F1=0.012), while structured evidence improves performance on adversarial paraphrases. Post-hoc Platt scaling further improves confidence calibration. The results demonstrate that increased agentic complexity does not necessarily improve semantic-drift detection and that simple few-shot prompting can provide a strong and efficient alternative.

---


### 238. [Improving Generalization Robustness of Multimodal RLVR](https://arxiv.org/abs/2608.08802)

**<font color=#1a73e8>作者：</font>** Pengfei Zhou, Zhiwei Tang, Xiaopeng Peng 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) makes Multimodal Large Language Models more accurate, but the gains are brittle: simply paraphrasing a question or changing the prompt template can degrade them, which challenges reliable deployment in high-stakes scenarios like medical VQA. We trace this to two issues of the standard RL objective. First, the binary verifier conflates format with content, so the reward signal cannot tell a wrong answer apart from a misformatted one. Second, the training distribution covers only a thin slice of the real-world prompts that the model might meet at deployment, so policies that perform well on the training distribution can behave differently under unseen prompts during test. Both failures call for a robust post-training method that helps the policy cover a broader distribution of semantically equivalent prompts, and we identify two measures that help achieve this objective: separating format from semantics in the reward, and applying policy invariance across perturbed prompts with equivalent semantics. We therefore propose Prompt-Invariant RLVR (PIRL), consisting of a dynamic trinary reward and a consistency regularizer based on an embedding-space adversary. Under stress testing, PIRL's average accuracy on benchmarks drops by only $\le 1\%$, where GRPO drops ~3%. On dynamic evaluation, PIRL also achieves the smallest performance drop.

---


### 239. [LASA: Language-and-Source-Anchored Alignment for Domain Generalized Semantic Segmentation](https://arxiv.org/abs/2608.08805)

**<font color=#1a73e8>作者：</font>** Jinhong Zhu, Weiqi Yan, Shengchuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Domain Generalization Semantic Segmentation (DGSS) focuses on generalizing knowledge from labeled source domains to unseen target domains where data is unavailable during the training phase. While conventional methods utilize style randomization or feature normalization to mitigate domain shifts, they often impair feature integrity. Specifically, style randomization distorts the underlying feature manifold due to its coarse-grained nature, while feature normalization suppresses discriminative, domain-sensitive semantic details owing to its rigid design. To address these limitations, we propose the Language-and-Source-Anchored Alignment (LASA) framework, which comprises three synergistic components: Text-and-Source-Guided Style Transfer (TSGST), Domain-Aware Query Adapter (DAQA), and Domain-Aware Decoder Optimizer (DADO). Concretely, the TSGST module addresses manifold distortion by utilizing source features as structural anchors and vision-language model (VLM) priors as fine-grained guidance. To restore suppressed discriminative and domain-sensitive details, the DAQA module recalibrates object queries via categorical guidance and domain-aware signatures, while the DADO module aligns the resulting query distributions with a shared classifier to ensure consistent categorical responses across domains. Extensive experiments on challenging benchmarks demonstrate that our method significantly outperforms state-of-the-art approaches.

---


### 240. [AdapterMoE: A Two-Stage Hard-Routing Mixture-of-Experts Architecture for Multi-Crop Disease Recognition with Calibrated Rejection and Incremental Learning](https://arxiv.org/abs/2608.08808)

**<font color=#1a73e8>作者：</font>** Pin-Hsun Huang, Shaou-Gang Miaou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Timely crop-disease identification is critical to food security. Multi-crop recognition suits Mixture-of-Experts (MoE), but conventional soft-routing MoE learns crop assignment freely end-to-end, letting a few experts dominate (expert collapse) with no semantic correspondence to crops, and facing high retraining costs, unstable rejection of non-target inputs, and a saturated accuracy ceiling. We shift the objective from accuracy toward a trade-off among deployment cost, scaling flexibility, and rejection stability, using deterministic hard routing. We propose AdapterMoE: a RouterHead classifies the crop and rejects non-target crops via a Maximum Softmax Probability threshold, with a dual-gate Energy+KNN out-of-distribution module catching distribution-shifted inputs; five per-crop Adapters atop a frozen EfficientNet-B0 backbone discriminate diseases, each calibrated via Temperature Scaling. Because experts are hard-isolated at the data level, the design avoids expert collapse and exposes an add_crop interface for local, per-crop updates instead of full retraining. On PlantVillage (5 crops, 26 classes), across a fair five-system comparison, AdapterMoE attains accuracy statistically indistinguishable from the best baselines (Macro-F1 within a 0.24-point band) while cutting training cost to about 9% of full-network baselines, expanding to a new crop in

---


### 241. [360CityArena: A Realistic Virtual Urban Navigation Benchmark for Embodied Agents](https://arxiv.org/abs/2608.08814)

**<font color=#1a73e8>作者：</font>** Kenta Watanabe, Atsuyuki Miyai, Mizuki Takenawa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present 360CityArena, a benchmark for evaluating the urban exploration capabilities of embodied agents within a photorealistic environment constructed from 360-degree videos. Existing outdoor benchmarks either lack sufficient photorealism or complexity, resulting in a considerable gap from real-world urban environments. 360CityArena is built on a realistic reconstruction of the Akihabara district in Tokyo, Japan, using 602 360-degree video segments covering 85 streets, and consists of 175 meticulously human-crafted tasks. It encompasses three task categories: Environment Understanding, Path Reasoning, and Spatial Reasoning, covering fundamental abilities required for urban exploration, such as localization, landmark search, path planning, and relational spatial reasoning, thereby enabling comprehensive evaluation in realistic urban scenes. Our evaluation using state-of-the-art LMM-based agents shows that even the strongest model, Gemini 2.5 Flash, performs far below human level (human: 77.3% vs. Gemini 2.5 Flash: 17.1%), revealing substantial challenges that remain in city-scale embodied navigation and reasoning. 360CityArena provides a necessary and challenging testbed for photorealistic urban-district navigation and spatial reasoning.

---


### 242. [Distilling Vision-Language Models for Robust Traffic Sign Perception in Autonomous Vehicles](https://arxiv.org/abs/2608.08815)

**<font color=#1a73e8>作者：</font>** Pedram MohajerAnsari, Amir Salarpour, Mert D. Pesé  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Traffic sign recognition (TSR) models based on deep neural networks achieve strong clean-data performance but remain vulnerable to physically realizable adversarial attacks, including shadow perturbations, natural-light interference, and printed patches. Existing defenses often improve robustness against one attack type while degrading performance on others, and can reduce clean accuracy. We propose LAMDA (Language-Anchored Model for Direction Alignment), a training framework that transfers language-grounded structure into TSR models without using adversarial examples or adding inference-time overhead. LAMDA builds two fixed prototype banks from VLM-generated sign descriptions and class names using a frozen OpenCLIP text encoder, and uses them to supervise visual features through two complementary auxiliary losses during training. At inference, the adapter and prototype banks are discarded, leaving a standard backbone and classifier. Evaluated on GTSRB and LISA across four backbones and three physical attack types, LAMDA is the only method among ten evaluated that consistently improves robustness across all attack-backbone-dataset combinations, with gains of up to +12.5 pp under shadow attacks and +13.2 pp under natural-light attacks, while preserving or improving clean accuracy in nearly all cases.

---


### 243. [Automated Generation of Complexity-Validated Decision Scenarios Using Large Language Models](https://arxiv.org/abs/2608.08822)

**<font color=#1a73e8>作者：</font>** Abdalla Doleh, Toni Somers, Ratna Babu Chinnam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cognitive decision-making research depends on diverse scenarios with carefully controlled complexity, yet manual production is slow, inconsistent, and biased. We developed an automated pipeline that uses LLms to generate structured decision scenarios and validates their complexity through a composite framework rooted in established task-complexity theory. We evaluated 4,238 scenarios across multiple domains and complexity tiers. Measurement validation met rigorous psychometric standards. Agreement among five independent model families was nearly perfect, with an intraclass correlation coefficient of 0.997 and a kappa of 0.971. Known-groups validity demonstrated large separation between tiers, with an eta-squared of 0.587 and all pairwise comparisons significant at p less than .001. Factor analysis revealed a dominant complexity construct, with loadings between 0.87 and 0.96 across three frameworks, while interactivity formed a weaker secondary dimension at 0.34. Discriminant validity was limited by a strong relationship between complexity and text length that persisted after controlling for tier, yielding a partial correlation of 0.86. This constrains construct purity but does not undermine the instrument's tier-grading function. Model analyses showed a negative association between throughput and schema pass rate (r = -0.967, p = .007, n = 5), suggesting a speed-quality trade-off, though largely driven by one high-throughput model. Llama 4 Maverick generated scenarios fastest at 134 per minute versus 25 for DeepSeek Chat V3.2, but underproduced complex-tier scenarios, whereas DeepSeek Chat V3.2 balanced domain coverage with high schema compliance. The system demonstrated strong psychometric properties, enabling reliable classification into Simple, Moderate, and Complex tiers and providing the measurement infrastructure needed for downstream cognitive assessment of AI systems

---


### 244. [Deployable Per-Instance Multi-Layer Activation Steering for Large Language Models](https://arxiv.org/abs/2608.08829)

**<font color=#1a73e8>作者：</font>** Muhammad Faishal Adly Nelwan, Alfan Farizki Wicaksono  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering edits the behaviour of a frozen language model by adding a learned vector to its residual stream, and current practice fixes the injection layers globally per task. We argue that the best layers are an instance-level decision, and we make per-instance, multi-layer selection both well understood and deployable. On two open-weight 8B models and six binary persona traits, a per-instance oracle over layer subsets shows that the best layers vary from one input to the next: on most trait-model pairs, no fixed global layer set recovers the per-instance benefit. A greedy rule that ranks layers by single-layer marginal effect recovers nearly all of the oracle's benefit, but both must score candidate layers against the gold answer, so neither can run at deployment; the rule instead becomes the target a prompt-only predictor is trained to reproduce. Our deployable recipe needs no label at inference: a per-instance layer ranker read off the prompt embedding, a classifier that infers the steering direction, and an adaptive gate that scores short steered passes against that inferred direction and steers no more layers than necessary. The recipe recovers most of the oracle's lift (the bulk on the stronger model, a clear majority on the harder one), never drives any trait-model pair below its unsteered alignment baseline on average, and largely avoids the fluency collapse that strong global selection incurs at higher layer counts. A mechanistic account, "direction over magnitude", explains the behavioural flip under a mis-directed global set, the output collapse from steering too many layers, and the ceiling of unsteerable inputs.

---


### 245. [PROSLEX: A Novel Dataset for Expert-Annotated Legal Statute Prediction for Indian Judiciary](https://arxiv.org/abs/2608.08830)

**<font color=#1a73e8>作者：</font>** Subinay Adhikary, Upal Bhattacharya, Vivek Kumar Singh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Legal Statute Prediction (LSP) involves automatically identifying relevant legal statutes given factual descriptions in legal documents, typically framed as a multi-label classification task within natural language processing and information retrieval research. While recent advances have begun incorporating Large Language Models (LLMs) for statute prediction, current approaches primarily focus on accuracy metrics without addressing the critical need for legal reasoning, a fundamental requirement in judicial contexts where decisions must be explainable and justifiable. To address this research gap, we present PROSLEX (PRediction Of Statutes and LEgal eXplanation), a comprehensive dataset comprising 1,623 expert-annotated legal documents from the Indian context. Each document is paired with statute predictions and detailed explanations, totaling 7,450 explanations, capturing the underlying legal reasoning. Using this dataset, we systematically evaluate various prompting strategies, including zero-shot, few-shot, chain-of-thought, and tree-of-thoughts approaches, to generate both statute predictions and their corresponding legal rationales. Our evaluation framework measures not only predictive performance but also the coherence and legal validity of generated explanations, positioning PROSLEX as a benchmark for developing explainable AI systems that can support legal practitioners while advancing research in interpretable legal NLP. To ensure reproducibility, we have made our PROSLEX dataset and model code available on GitHub: this https URL.

---


### 246. [Toward Mask Annotation-Free Surgical Instrument Segmentation from Endoscopic Images Using Text-Prompted Segment Anything Model 3 (SAM3)](https://arxiv.org/abs/2608.08844)

**<font color=#1a73e8>作者：</font>** Nakul Poudel, Richard Simon, Cristian A. Linte  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Surgical instrument segmentation is a fundamental task for computer-assisted interventions, yet most existing methods rely on pixel-level annotations or manual spatial prompts, which limit scalability and automation. The recently introduced Segment Anything Model 3 (SAM3) offers a pathway to annotation-free, automatic segmentation via text-based prompting; however, the instrument name as a text prompt could not be directly used due to a large domain gap. To overcome these limitations, we propose a two-stage framework that achieves instance-level segmentation without requiring ground truth masks or manual interaction. In the first stage, we leverage a natural-language-aligned generic prompt - "tool" - to produce binary masks using SAM3's zero-shot capability. In the second stage, these masks are extended to instance-level by integrating a vision-language model (Qwen) that is fine-tuned on SAM3-generated masked regions for instrument classification. We evaluate our approach on the EndoVis 2017 and 2018 datasets. Results show that, while our two-stage approach does not reach the performance of current fully supervised methods, it significantly outperforms the direct use of SAM3 for instance-level instrument segmentation with text prompts. Overall, our findings highlight both the limitations and potential of SAM3, suggesting a promising direction toward annotation-free surgical instrument segmentation.

---


### 247. [Findings of the First Teaching Monster Challenge: A Benchmark of Pedagogical Content Knowledge in AI Agents](https://arxiv.org/abs/2608.08852)

**<font color=#1a73e8>作者：</font>** Yi-Cheng Lin, Yu-Kai Guo, Szu-Chi Chen 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can now solve problems, answer like subject experts, and generate long-form multimodal content. However, whether they can adapt a lesson to fit a specified learner, which education calls Pedagogical Content Knowledge (PCK), has not been benchmarked. To measure it, we introduce the Teaching Monster Challenge, the first instructional video generation benchmark to treat the learner persona as an explicit evaluation criterion. Each system is given a topic and a learner persona and must generate a complete instructional video. Every video is screened by an LLM-judge, ranked by crowd pairwise voting, and finalized by an expert panel. The first edition shows that today's systems handle the content well but are far weaker at presenting it and adapting it to the learner. The same process exposes a limit of automatic judging. The LLM-judge separates a clear low-performing tail but ranks the strongest systems poorly. The strongest systems receive nearly identical scores from the judge, so its ranking of them does not match human preference. Progress therefore requires not only better teaching systems but also better automatic judges, and we release the benchmark, rubric, and human judgments as a testbed for both.

---


### 248. [Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.08853)

**<font color=#1a73e8>作者：</font>** Zongfei Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) routers commonly use the same scores both to select experts and to weight their already-computed outputs. We study whether these two roles, dispatch and aggregation, should be coupled. On pretrained OLMoE-1B-7B, we keep selected Top-8 expert IDs, expert computation, and total selected router mass fixed and change only within-set aggregation. A structured oracle improves full-horizon cross-entropy by 0.0160 +/- 0.0039 across three seeds; the router's top-scored expert is the counterfactual-best vertex only 17.2% of the time, with router-utility Spearman 0.030. We therefore train Fixed-Dispatch Adaptive Aggregation (FDAA), a 301K-parameter post-compute head optimized directly with the language-modeling objective while freezing the backbone, router, and experts. On OLMoE, FDAA improves fresh WikiText-103 test by Delta CE = -0.1523 +/- 0.0031 across three seeds, and mixed-domain training gives robust gains on WikiText-103, C4, and held-out Penn Treebank under frozen confirmatory evaluation. We also replicate the fixed-dispatch audit on DeepSeek-V2-Lite, which uses Top-6 routed experts plus shared experts. Best-vertex headroom remains significant on WikiText and C4, while router Top1 identifies the best selected expert in only 12.5% and 16.7% of audited examples. In a one-seed mixed-domain replication, FDAA improves locked WikiText and PTB, while C4 is statistically neutral. These results support a cross-architecture distinction between expert selection and expert commitment.

---


### 249. [Zero-Shot Traffic Accident Detection via a Coarse-to-Fine VLM-Tracking Pipeline](https://arxiv.org/abs/2608.08867)

**<font color=#1a73e8>作者：</font>** Dipit Saha, Shah Mohammad Abdul Mannan, Mohammad Raihan Rashid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic surveillance cameras capture accidents continuously, yet converting raw CCTV footage into structured event records that pinpoint when, where, and what type of collision occurred remains unsolved at scale. The ACCIDENT @ CVPR benchmark evaluates exactly this joint prediction under a strict constraint: no labeled real-world training data is available. We introduce a training-free, two-pass coarse-to-fine pipeline that pairs a frozen Qwen3-VL-32B-Instruct vision-language model with YOLO11x object detection and BoT-SORT tracking. A first pass sparsely samples the full clip to anchor the collision moment in time; a second pass re-examines a tight window around that estimate using frames annotated with stable vehicle identities and normalized bounding-box coordinates, which gives the model both a visual overlay and an explicit numeric description of the same scene. On the official 2,027-clip real-CCTV test set, our system achieves a three-way harmonic mean score of 0.504, surpassing all organizer-published baselines including the best multi-model ensemble (0.412) by a 22% relative margin.

---


### 250. [Conversation as Measurement in Clinical Encounters: Observable Phase Structure, Partially Observable Patient State](https://arxiv.org/abs/2608.08868)

**<font color=#1a73e8>作者：</font>** Lily Chen, Ted Mau, Michael Gensheimer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many modern AI systems analyze conversational traces to infer aspects of human interaction and state, implicitly assuming that such information is recoverable from conversation. We study observability: whether a target is recoverable from conversational transcripts alone. Observability is difficult to assess because transcripts may provide only a partial view of many targets, and large-scale analysis requires model-based annotation, making true limits of the conversational signal hard to distinguish from annotator error. We therefore study clinical encounters, where patient-reported outcome measures (PROMs) provide an external anchor for patient state, and visits follow broadly structured patterns. We study observability of patient state and conversational phase structure using 439 real-world clinical encounter transcripts spanning 134 hours, including 245 ENT transcripts paired with 273 PROM surveys. We operationalize patient state using PROM scores for voice, cough, and swallowing; phase structure using conversational phase segmentation. To make these analyses credible at scale, we use a PHI-compliant GPT-5 deployment for transcript annotation and conduct 40 hours of manual validation, reducing the risk that apparent limits of observability simply reflect annotator error. Our core finding is an observability asymmetry: phase structure is observable and useful for characterizing clinical encounter organization, while patient state is only partially observable, even in a setting designed to elicit patient symptoms and experiences, cautioning against transcript-only inference of human state.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-438](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
