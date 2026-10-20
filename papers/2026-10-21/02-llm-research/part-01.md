# 🧠 大模型相关研究 | 2026年10月21日

> 本类共 **548** 篇论文：已确认 **507** 篇，待复核 **41** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

---

### 1. [Web Agent Agentic Reinforcement Learning Decision Model Under Multi-Cost and Failure Risk](https://arxiv.org/abs/2610.23857)

**<font color=#1a73e8>作者：</font>** Qianli Ma, Limengxi Yue, Shuyang Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intelligent agent interactions in real-world web environments are commonly constrained by request budgets, time delays, anti-crawling restrictions, and operational failure risks. Strategies solely optimizing task success rates often exhibit unusable phenomena such as "high success but high cost" or "low risk but conservative failure." This paper proposes a constrained agentic reinforcement learning model for web agents, unifying page access, search requests, and external API calls into a unified long-term decision-making framework with associated costs. It simultaneously incorporates cost budget constraints and tail risk control into the optimization objective: constructing a multidimensional cost vector comprising cumulative request count, total latency, and failure penalties to achieve budget compliance via Lagrange dual updates, while employing a CVaR risk term to suppress excessive exploration of high-failure-probability paths, thereby achieving an adaptive balance among "completion rate, cost, and risk."
Experiments were conducted across 30-70 site/page templates and 800-1,500 end-to-end web tasks, including information extraction, price comparison, form submission, and cross-page navigation. Interaction sequences spanned 20-120 steps with tool scales of 30-200. Performance was benchmarked against unconstrained RL, budget-constrained RL, and rule-based/scripted web agents, quantifying task completion rates, cost-per-success, failure rates, and policy stability.
Results demonstrate that at equivalent completion rates, our method reduces C-PS by 22%-31% and lowers failure rates by 18%-26% under high failure penalties. Under fixed budgets, task completion rates increase by 10%-16%, highlighting the necessity and effectiveness of constraint modeling for practical web agent deployment.

---


### 2. [I$^2$-Med: Interpretable Medical Inference through Visual-Guided Dynamic Logits Calibration](https://arxiv.org/abs/2610.23858)

**<font color=#1a73e8>作者：</font>** Md Sajid, Shreeyut Maheshwari, Akshat Mishra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision language models have demonstrated strong potential for medical image understanding and reasoning. However, their interpretability and reliability remain limited because medical vision language tasks require precise visual grounding and clinically coherent explanations. This is particularly challenging due to complex imaging patterns and scarce expert annotations. These challenges reduce the effectiveness of conventional reasoning methods and lead to visual hallucination, defined as the generation of text that is not grounded in the given visual input, which further limits their applicability in clinical practice. To mitigate these challenges, we propose an interpretable medical inference (I$^2$-Med) framework that enhances visual faithfulness during inference without additional training to improve reasoning and explanation faithfulness in medical vision language models. During text generation, I$^2$-Med uses a visual guidance module to check whether each candidate word is supported by the medical image and consistent with the current reasoning. Based on this guidance, the model's output scores are adjusted to favor visually grounded words, without changing the model parameters. Extensive experiments on the OmniMedVQA benchmark, covering eight medical imaging modalities and five clinical question types, demonstrate that our proposed I$^2$-Med framework generates more clinically meaningful and visually faithful reasoning chains and reduces visual hallucination under standard medical VQA evaluation metrics. The source code is publicly available at \url{this https URL}.

---


### 3. [Modeling Human Behavior in the Prisoner's Dilemma with Large Language Models](https://arxiv.org/abs/2610.23860)

**<font color=#1a73e8>作者：</font>** Raina Gao, Tristan Raffo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Prisoner's Dilemma has long served as a foundational framework for studying human decision-making and cooperative outcomes across social scenarios, yet human behavior consistently deviates from predictions of fully rational economic theory. Previous works have studied human and LLM outcomes in the Prisoner's Dilemma; however, these studies have lacked at least one key feature: a memory component for LLM agents, accessible open-source models, or comparison against empirical human data. This project investigates whether open-source LLMs, TII Falcon 7B Instruct, Google Gemma 7B, Meta Llama 3.1 8B Instruct, Microsoft Phi Mini MoE Instruct, and Qwen 2.5 7B Instruct, can model human cooperation patterns in repeated Prisoner's Dilemma games, while examining how an LLM's knowledge that its opponent will be shuffled affects its decisions. Using a standardized prompting framework, we simulated interactions in two trial types: a fixed-partner setting where both agents retain memory, and a shuffled-partner setting where a memory-enabled agent, informed that its opponent changes across rounds, interacts with a memoryless agent. For each trial, we measured cooperation rates over 100 rounds and 10-round increments and compared them to human data from Montero-Porras et al. (2022). Under both frameworks, all LLMs differed from the human cooperation rate. Open-source LLMs generally over-cooperated relative to humans, particularly in the shuffled framework, where human cooperation averaged 28.5% while several models exceeded 80%. Qwen-2.5-7B-Instruct showed deterministic tendencies, while Phi-mini-MoE-Instruct displayed greater variability and briefly approximated human rates. These findings suggest that LLMs have potential as behavioral simulation agents and provide a benchmark across two interaction environments, although open-source models are not yet reliable substitutes for human participants.

---


### 4. [PolyGraph: Plan-Buffered CUDA Graphs for Adaptive Speculative Decoding](https://arxiv.org/abs/2610.23861)

**<font color=#1a73e8>作者：</font>** Junchao Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive speculative decoding changes the active batch size B and draft length d from one decode step to the next, whereas a CUDA Graph replays a fixed launch configuration. The resulting verification width M = B d forces serving systems to pre-capture many shapes, capture new ones on the serving path, or pad every step to the largest draft. We present PolyGraph, a plan-buffer mechanism for custom Triton kernels that avoids this choice. PolyGraph captures one maximum-grid graph and writes the active shape to GPU memory before each replay. Kernels skip tiles beyond that shape, while graph topology, allocations, layouts, pointers, and launch grids remain fixed; the update transfers only 28 bytes. On one NVIDIA H800, a trace-driven prototype with Qwen2.5-3B dimensions replaces 64 shape-specific graphs with one, matches the warmed baseline in observed step latency (17.7 vs. 17.8 ms P50), and reduces measured pre-serving graph-build time from 3,915 to 93 ms. Fixed-draft controls show that the benefit comes from avoiding padded payload: the P99 difference from MaxPad is negligible at zero padding waste but reaches an 18.7% reduction at 100% waste. Our evidence establishes a bounded work-shape mechanism for custom kernels, not a production serving system, and is limited to synthetic traces on one GPU.

---


### 5. [SAGE-CP: When Marginal Coverage Hides Route-Conditional Failures in Adaptive VLM Ensembles](https://arxiv.org/abs/2610.23864)

**<font color=#1a73e8>作者：</font>** Mushir Akhtar, M. Tanveer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive VLM ensembles save computation by stopping early on easy images and escalating harder ones. Although a single conformal threshold can make the final predictor marginally valid, it can still fail severely along individual computational routes. We characterize this failure precisely: if a route has prevalence pi, marginal 1-alpha coverage allows its conditional coverage to fall to max{0, 1-alpha/pi}. To address this mismatch, we learn the router on development data, freeze all routing choices, and calibrate the returned score separately for early exits and escalated inputs. We call this pipeline SAGE-CP. Its calibration step applies Mondrian split conformal prediction to the operational groups created by the router. Under exchangeability, the resulting prediction sets achieve finite-sample coverage within each route. Across 10 benchmarks, 4 frozen VLMs, and 5 aligned splits, both global calibration and SAGE-CP achieve 0.900 marginal coverage at a 0.90 target, but their route behavior differs substantially. SAGE-CP raises mean worst-route coverage from 0.623 to 0.887 and reduces the mean route-coverage gap from 0.324 to 0.025, using the same routed scores and 1.177 source calls per image. The stronger guarantee increases the mean prediction-set size from 1.893 to 2.212; nevertheless, the sets remain smaller than those of the full ensemble (2.486) while requiring 70.6 percent fewer source calls. The route-level reliability persists across 6 fixed query fractions, while finer exit-depth groups demonstrate the need for additional calibration data on rare routes. Across 5 datasets, SAGE-CP also reduces measured batch-one latency by 58.8 to 63.4 percent and gross GPU energy by 55.7 to 57.5 percent relative to full inference. Thus, routing provides computational savings, while route-stratified calibration attaches coverage guarantees to the operational paths created by the router.

---


### 6. [GardenBench: A lightweight, daily evaluation of LLM capabilities](https://arxiv.org/abs/2610.23866)

**<font color=#1a73e8>作者：</font>** Benedict Cummins-Mburu, Mariana Garcia Mejia, Oscar Heath 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce GardenBench, a benchmark with 11 test suites that evaluate the capabilities of Large Language Models (LLMs) across a range of tasks. By systematically prompting LLMs with various lightweight queries, we document day-to-day changes in model performance, including run costs and times, that other benchmarks miss. This allows us to compare the accuracy and features of responses across model providers and versions. We account for daily variations in model accuracy, capturing both model progress and degradation, for instance, when a model is changed post-deployment or when a new model is released. We base our evaluation on general-use tasks and make our results publicly accessible via a live dashboard, diversifying existing approaches to LLM testing. Our main contribution is an innovative, lightweight, and inexpensive benchmark, designed to be consumer-facing and for everyday tasks.

---


### 7. [Composable Parametric Demographic Injection for Values Survey Simulation](https://arxiv.org/abs/2610.23867)

**<font color=#1a73e8>作者：</font>** Xinyuan Cao, Qingyi Pan, Bangde Du 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as simulated respondents in computational social science, yet accurately reproducing population-specific heterogeneous response distributions remains challenging. Existing methods such as demographic prompting are sensitive to prompt design and increase inference overhead, while parameter-based methods struggle to reuse demographic information efficiently, limiting generalization to unseen combinations. In this regard, we propose PARADE, a composable PARAmetric DEmographic injection framework that represents each demographic attribute value with a reusable and composable LoRA module. Specifically, PARADE separates task-common survey capability from demographic-specific value shifts via a shared Task LoRA and attribute-level Demographic LoRAs, with composition calibration to reduce parameter interference. At inference time, target population models can be constructed on demand by recombining the relevant modules, including demographic combinations not observed during training. Extensive experiments on the World Values Survey and SocioBench across three backbone models show that PARADE achieves strong population-level distribution alignment while maintaining competitive predictive performance, reducing KL divergence by up to 52.8% relative to the strongest baseline.

---


### 8. [Translating in style: An open-weight alternative to GPT-4 for culturally aligned machine translation](https://arxiv.org/abs/2610.23868)

**<font color=#1a73e8>作者：</font>** Thomas Rietman, Hadi Mohammadi, Robert A. Bagheri  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine translation systems often preserve meaning but systematically flatten linguistic style, a failure that is most acute when translating into non-Western languages. The RASTA framework of Havaldar et al. (2025a) addresses this through retrieval-augmented stylistic alignment, but relies on GPT-4, a closed, proprietary model. We investigate whether an open-weight translation specialist, Hunyuan-MT-7B, can serve as an open-weight alternative. We evaluate three variants of the model, the base model, a LoRA supervised fine-tune, and a GRPO-steered policy. We do this across three style dimensions (formality, politeness, and intimacy) and twelve directed language pairs, measuring style alignment with the correlation-based metric $\mathcal{A}$. We find that fine-tuning does not reliably improve alignment: the three variants are statistically indistinguishable in aggregate. The open backbone does not match RASTA-GPT-4 overall, but the shortfall is concentrated in formality and largely closes for intimacy and Chinese directions, where the open model matches or surpasses GPT-4 on individual pairs. An accessible RASTA pipeline built on an open model is thus already viable for parts of the problem.

---


### 9. [EMMA: Event-Driven Multimodal Memory System with Multi-Agent Retrieval](https://arxiv.org/abs/2610.23892)

**<font color=#1a73e8>作者：</font>** Ruochen Zhao, Jiazheng Kang, Gezi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video understanding requires reasoning over hours of content that far exceed the context window of multimodal large language models (MLLMs). Existing approaches compress video into fixed-length clips, yet events are fragmented and unrelated content is merged, yielding noisy retrieval. To overcome this challenge, we propose EMMA, an Event-driven Multimodal Memory system with Multi-Agent retrieval, which organizes memory around semantic events in three stages: (1) Event segmentation: a dual-stream detector adaptively locates event boundaries by fusing visual semantic drift with spoken transitions, rather than fixed windows. (2) Memory construction: built on the detected events, a three-level hierarchy of raw video, clip-level memory, and event-level memory stores content at progressively higher semantic abstraction. (3) Memory retrieval: a multi-agent framework collaboratively queries this hierarchy through query decomposition, tiered search, evidence validation, and answer generation, narrowing evidence from coarse events to precise clips. Extensive experiments on three challenging benchmarks demonstrate substantial improvements, showing the effectiveness of our event-aligned memory system. Code, prompt templates, and reproduction scripts are available at this https URL.

---


### 10. [AI-Experiment: an augmented reality art project co-created with artificial intelligence](https://arxiv.org/abs/2610.23903)

**<font color=#1a73e8>作者：</font>** Bernhard Egger, Hans Furer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe the creation of a physical artwork that was performed in synergy between an artist, a computer scientist and generative AI tools. A latent diffusion model was finetuned on photographs of the artwork of the specific artist and the generative model then generated synthetic artworks in a similar style. From the generated artworks a subset was selected to be painted again with acrylic on canvas by the original artist. In addition to the physical artifact an augmented reality component was added which brings the artwork to life with a set of generative video models. Together with this paper we release part of the artwork (training data), the code that was deployed to generate the artwork as well as the augmented reality experience for arts, research and education under this https URL

---


### 11. [LVMH: A Meta-Optimization Harness for Long-Video Agent Memory](https://arxiv.org/abs/2610.23904)

**<font color=#1a73e8>作者：</font>** Liwei Che, Benlin Liu, Dai Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video agents must map hours or days of multimodal evidence into a bounded context while respecting token and latency budgets, making memory design a context-management challenge. Existing memory systems largely rely on hand-designed policies, leaving open how to jointly optimize memory design for performance and efficiency. We propose Long Video Meta-memory Harness (LVMH), an automated multi-agent framework that formulates memory-policy development as multi-objective code search around a fixed answer model. To guard against self-certification and development-set overfitting, LVMH separates implementation from independent review and enforces protected observation boundaries. Persistent meta-memory records past proposals, traces, costs, and failures to guide subsequent policy revisions. Through this harness, we discover Self-Evolving Evidence Memory (SEEM), a "text-first, vision-second" policy that answers from compact structured event memory and evidence specialists, consulting localized frames through a selective visual gate. The policy evolved on EgoLifeQA generalizes to unseen benchmarks, outperforming Meta-Harness on both Ego-R1 Bench and Video-MME (L) with GPT-5 mini. Across the three benchmarks, SEEM with GPT-5 achieves 65.7% average accuracy, surpassing the previous state of the art by 7.7 percentage points with approximately 32x lower average evaluation token use and 91x shorter average response time.

---


### 12. [EgoVine: Post-Training with Branching Experience Compiled from Real-World Videos](https://arxiv.org/abs/2610.23907)

**<font color=#1a73e8>作者：</font>** Qinchuan Cheng, Bowen Lyu, Zhantao Gong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world egocentric videos capture multi-step household procedures, but their recorded trajectories leave alternative actions and recovery from the learner's own mistakes largely unexplored. We introduce EgoVine, a post-training framework that turns a fixed demonstration set into interactive experience for long-horizon planning. EgoVine operates in executable symbolic environments compiled from real-world video annotations, where an agent must coordinate object manipulations under partial observation and account for delayed consequences. Restoring a decision state allows the learner to explore alternative actions and compare their eventual outcomes. Union jointly trains action generation and consequence prediction in one model, using the same executions to supervise candidate comparison and recovery. Verified repairs add recovery targets from failed attempts, while comparisons among sampled continuations guide policy updates. The updated planner then returns to the environments, with its own decisions and mistakes shaping the next round of experience. On a shared benchmark, EgoVine-1.5B achieves 81.8% success on Main planning tasks and 66.7% on longer task compositions, outperforming all evaluated Flash LLM baselines on both. EgoVine connects real demonstrations to an iterative learning process that trains compact planners on choices and futures beyond the recorded trajectories.

---


### 13. [ContraSafe-VL: A Contrastive Safety Preference Dataset for Vision-Language Models](https://arxiv.org/abs/2610.23908)

**<font color=#1a73e8>作者：</font>** Di Wu, Yanyan Zhao, Xin Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are increasingly deployed as general-purpose multimodal assistants, making multimodal safety alignment an important challenge. Safety depends on the interplay between textual and visual content, with visual context often playing a critical role. However, VLMs may fail to use visual information appropriately, either overlooking safety-relevant visual content or over-interpreting sensitive visual content, leading to unsafe responses or over-refusal. Existing multimodal safety alignment datasets largely follow the response-preference paradigm, which teaches models how to respond but provides limited supervision on how visual context should inform the safety judgment, making it difficult to balance safety and over-refusal. To address this limitation, we introduce ContraSafe-VL, a Contrastive Safety preference dataset for Vision-Language Models. For each fixed textual query, ContraSafe-VL constructs paired visual contexts that result in multimodal queries with different safety labels, providing direct supervision for how visual context should inform multimodal safety judgments. It further provides response preference pairs based on harmlessness and helpfulness to encourage models to generate responses that are both safe and helpful. Experiments across three VLM architectures and multiple benchmarks demonstrate that training with ContraSafe-VL improves cross-modal safety recognition and achieves a better safety--over-refusal trade-off while preserving general multimodal capabilities. The dataset will be publicly released.

---


### 14. [Grounding Confusable Movie Moments](https://arxiv.org/abs/2610.23910)

**<font color=#1a73e8>作者：</font>** Dong-Hee Kim, Seonwoo Choi, Changbeen Kim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Characters, locations, and actions recur throughout a movie, so many of its moments differ only in fine-grained details. Grounding such a moment in a full-length movie requires resolving that detail rather than matching the attributes it shares with other moments, yet existing temporal movie grounding benchmarks rarely test this. We introduce CoM$^2$-Bench, a benchmark of confusable query pairs, where the two queries in each pair share most attributes but differ in a single distinguishing detail within a full movie, posing a challenge for recent temporal grounding approaches. To locate where grounding breaks down, we analyze a retrieve-then-localize pipeline, in which a retriever first selects a short candidate chunk and a localizer then performs temporal grounding within it. Separating the two stages lets us attribute each failure to either retrieval or localization. We find that retrieval is the major bottleneck: state-of-the-art retrievers often select a moment's confusable counterpart, because their choices follow the content the two moments share rather than the detail that tells them apart. To address these failures, we propose a simple, training-free remedy, Agentic Window Search (AWS): an MLLM agent $\textit{Decomposes}$ the query into attribute-level sub-queries, then $\textit{Inspects}$ each candidate window against them and $\textit{Expands}$ the window when evidence is cut off at its edge. AWS works with existing retrievers and localizers without additional training, raising mIoU from 18.5 to 26.8.

---


### 15. [Vocabulary-Incomplete Unsupervised Vision-Language Model Adaptation](https://arxiv.org/abs/2610.23919)

**<font color=#1a73e8>作者：</font>** Si Qin, Jiawei Tang, Yaxin Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In certain real-world scenarios, obtaining labeled data is excessively expensive, motivating increasing interest in adapting models without annotations. Vision-language models (VLMs) provide pseudo-labels for unlabeled images through image-text similarity, enabling adaptation without manual labeling. The previous unsupervised vision-language model adaption methods assume access to an adaptation vocabulary containing all class names. However, a complete vocabulary is difficult to construct in real-world scenarios, as unlabeled data may contain classes that are overlooked or fall outside the current task scope. Thus, we propose Vocabulary-Incomplete Unsupervised Vision-language model Adaptation (VI-UVA), where only a subset of class names are available during adaptation. The vocabulary incompleteness induces an adaptation bias toward provided classes, which degrades omitted-class recognition. To address this issue, we propose Label Space Reconstruction (LSR), which reconstructs a latent label space from the unlabeled data and incorporates it into prompt tuning, thereby extending adaptation beyond the incomplete vocabulary and mitigating the adaptation bias. Furthermore, we derive an omitted-class semantic discrepancy bound for LSR and identify the key factors affecting the bound. Extensive experiments across eight benchmarks demonstrate that LSR outperforms existing state-of-the-art methods.

---


### 16. [Doing Less with More: A First-Principles Exploration of the Suitability of Agentic Computing over Alternative Architectural Choices](https://arxiv.org/abs/2610.23921)

**<font color=#1a73e8>作者：</font>** Ritvik Garimella, Biplav Srivastava, Amit Sheth  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> There is growing interest in automating business activities with Agentic Artificial Intelligence (AI) due to latter's seeming ease of use. Never has it been easier, or costlier, to do less with more. However, little is known about when agents are preferable to established alternatives such as local computation, Representational State Transfer (REST), the Simple Object Access Protocol (SOAP), and the Model Context Protocol (MCP), particularly when development speed, performance, and operational cost are considered. We investigate this question using a controlled mathematical task that compares seven methods on a benchmark of 1,000 arithmetic expressions where semantics of operator precedence has to be preserved. We ran this setup across a native Function Calling baseline (Python library), REST, SOAP and MCP microservice architectures, direct responses from large language models (LLMs) using a Groq cloud API and five locally deployed Ollama models, and agentic systems in which five local LLMs invoke MCP tools. The deterministic methods achieve 100% accuracy with negligible latency. Direct LLM evaluation achieves at most 92.9% accuracy at over 22,000x the latency of a native function call. With MCP tools, the best agent reaches 99.9% accuracy, but incurs nearly 1,000,000x the baseline latency. These results demonstrate that LLMs approaches are poorly suited for exact arithmetic evaluation and motivate an informed architectural decision framework (ADF) for choosing an architecture based on accuracy and throughput requirements. We recognize that an actual interaction with an agent may span both reasoning and linguistic tasks. Hence our recommendation is to explore multiple architectural choices (based on task type) rather than one-size-fits-all solution (LLMs).
Code is available at - this https URL

---


### 17. [Zero-Shot Tabular Learning via Hypergraph Reasoning with LLMs](https://arxiv.org/abs/2610.23923)

**<font color=#1a73e8>作者：</font>** Geon Lee, Kyungho Kim, Dongwon Choi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data are prevalent across diverse domains such as healthcare and finance. Zero-shot tabular learning aims to make predictions without labeled data. However, existing LLM-based approaches rely on row-wise prompting, resulting in high inference cost and limited use of inter-row dependencies. In this work, we propose TABHGR+, an efficient relation-aware zero-shot framework for tabular data that leverages LLM-generated rules to label and group rows. Specifically, based on column and task descriptions, we use LLMs to generate rules that assign weak labels to all rows. To refine these noisy weak labels, we construct a hypergraph by grouping semantically related rows using LLM-generated rules and perform hypergraph-based label propagation. Lastly, we further enhance the LLM-generated hypergraph for propagation, which is potentially sub-optimal, by assigning label-adaptive weights to hyperedges. By requiring only a constant number of LLM calls independent of dataset size, TABHGR+ substantially reduces inference cost while achieving higher classification accuracy than zero-shot and strong few-shot baselines.

---


### 18. [miniTE: Diagnosing and Bridging the Execution Gap in Native NVFP4 Reinforcement Learning](https://arxiv.org/abs/2610.23928)

**<font color=#1a73e8>作者：</font>** Zhen Li, Mingfa Feng, Yiming Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Native NVFP4 promises to accelerate reinforcement learning (RL) for large language models (LLMs), but achieving stable learning across separate training and sampling engines remains challenging. We show that matching model weights and numerical formats is insufficient to ensure consistent policy evaluation, highlighting the importance of cross-engine numerical execution. We introduce miniTE, a lightweight framework that combines execution diagnostics, cross-engine numerical alignment, and efficient native W4A4 (4-bit weights and activations) GEMM computation for LLM RL. It improves numerical execution consistency without modifying the RL objective, while reducing implementation overhead to realize the benefits of native low-bit computation. Long-horizon RL experiments on Qwen3-30B-A3B demonstrate stable training and benchmark performance close to BF16, outperforming naive Transformer Engine (TE) NVFP4 in evaluation quality. On single NVIDIA B300 GPU node, the optimized learner reaches 33,540 tokens/s, yielding 1.39x and 1.47x the throughput of BF16 and TE NVFP4, respectively, for complete learner updates. We released the framework, kernels, diagnostics, and training configurations to make native low-bit RL easier.

---


### 19. [Unbalanced Optimal Transport for Efficient Visual Document Retrieval](https://arxiv.org/abs/2610.23929)

**<font color=#1a73e8>作者：</font>** Hoyeon Shin, Jeongyeon Kim, Yeong Jun Koh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models(VLMs)have advanced Visual Document Retrieval (VDR) by enabling OCR-free, multi-vector representations. However, these models generate excessive tokens to preserve dense visual details, which severely limits retrieval scalability. Existing compression methods mitigate this overhead but rely on isolated heuristics that fail to balance token importance, semantic redundancy, and coverage capacity. We propose a visual token compression framework formulated as an Unbalanced Optimal Transport (UOT) problem. Our approach unifies these three objectives into a single alternating optimization process. Furthermore, we theoretically show that minimizing the transport cost upper-bounds the MaxSim retrieval error, ensuring ranking stability. Extensive experiments on the ViDoRe V1 and V3 benchmarks demonstrate that our method preserves fine-grained document semantics and improves the efficiency-effectiveness trade-off over state-of-the-art base-lines. Code is available at this https URL.

---


### 20. [VERDICT: Visual Extraction-Result Decoder with Integrated Confidence and Traceable Evidence](https://arxiv.org/abs/2610.23933)

**<font color=#1a73e8>作者：</font>** Harikrishnan P M, Goutham Vignesh, Siva Prasad 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Enterprises run schema-guided structured field extraction on documents with frontier multimodal models, and accuracy keeps improving as new models and systems arrive. Two things have not kept pace: the evidence for each extracted value, meaning the location of the document it was read from, and how far to trust the value and that evidence. Neither is a component of most extraction systems today, so we build them as a framework that attaches to an existing extractor and leaves it untouched. We present VERDICT, a plug-in framework that uses a small Vision--Language Model (VLM) to ground/localize the evidence once per document over a fixed external extractor's output, then calibrates value and evidence confidence. Fine-tuning the VLM for evidence localization substantially improves visual evidence quality and, more importantly, expands VERDICT's selective-prediction operating range. At a strict confidence threshold $0.80$, VERDICT with the fine-tuned VLM gives usable precision--coverage trade-offs for both value and evidence confidence across the in-distribution and out of distribution datasets, whereas the frozen setting often collapses to little or no coverage. Running an open-weight VLM for localization rather than a closed API makes its internal states available to the calibrator, and they are worth more than output log-probabilities: in-distribution AUROC rises from $0.730$ to $0.914$ for value confidence and from $0.681$ to $0.906$ for evidence confidence. This advantage does not survive a distribution shift. We show that the signal is displaced rather than destroyed, and that labeling roughly $120$ fields from the target dataset takes evidence confidence from $0.641$ to $0.905$ on one dataset and from $0.675$ to $0.829$ on the other.

---


### 21. [Organizing LLM Inference for Aggregate Predictions from Behavioral Data](https://arxiv.org/abs/2610.23934)

**<font color=#1a73e8>作者：</font>** Varun Gupta, Vijay Kamble  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When using a large language model (LLM) to simulate a user population, how should we combine individual behavioral histories to predict the fraction of users who take a particular action? We study this question in e-commerce, predicting observed product-level conversion rates from browsing sessions without task-specific model training. We vary two design choices, each involving a bias-variance tradeoff. Summarizing a product's sessions before inference reduces cost but can discard predictive detail, adding bias, whereas predicting outcomes for individual sessions and averaging afterward preserves that detail but requires many calls to reduce variance. Evaluating products together in one prompt can help the model infer what is typical in the setting, reducing bias, but also makes each prediction depend on which other products appear alongside it, adding noise. We evaluate both choices across five LLMs and two datasets. Our main finding is that predictions from individual sessions outperform predictions from summaries when products are evaluated separately, but summaries lead when products are evaluated together. Comparative summaries achieve the highest Spearman correlation with observed rates in 12 of 15 settings, with no alternative significantly better. Comparison thus helps summaries far more than session predictions, overcoming the advantage of behavioral detail. We interpret this difference through a Bayesian model of the second tradeoff, which suggests that comparison helps more when the inputs in a prompt reveal more about differences across products, consistent with our results for four types of comparative context. Comparative summaries also incur a small fraction of the inference cost of the session methods. With the best model for each outcome, they attain 66-89% of the correlation of the best supervised benchmark trained on thousands of labeled products.

---


### 22. [Factorization-Guided Training and Inference for Diffusion-Drafted Speculative Decoding](https://arxiv.org/abs/2610.23935)

**<font color=#1a73e8>作者：</font>** Jiakun Fan, Min Xiao, Qiang Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates large language model inference through parallel verification of tokens proposed by a drafter. Diffusion drafters further parallelize proposal generation, but greater proposal capacity or higher mean accepted tokens (MAT) need not yield higher throughput. Because verification accepts only a consecutive prefix, early rejections can render later correct predictions ineffective, limiting MAT gains, while even higher MAT may not improve throughput if per-round latency increases. We introduce DScout, which uses two complementary factorizations to guide diffusion drafter training and inference for higher throughput. For training, DScout factorizes position-wise loss into inclusion, weighting, and prediction loss. This guides the design and combination of mixed-horizon training, intra-block unmasking, and acceptance-weighted loss to align supervision with prefix acceptance and improve MAT. For inference, DScout factorizes throughput as the ratio of MAT to per-round latency, guiding target-conditioning depth, drafter depth, and inference block size selection to identify a high-throughput configuration for each workload. Across six benchmarks, DScout achieves $3.84\times$ and $4.14\times$ mean speedups over autoregressive decoding on Qwen3-4B and Qwen3-8B, respectively, improving mean speedup over the state-of-the-art baseline by 9.1% and 7.1%. Across models and concurrency settings, our inference configuration policy provides up to 9.75% additional mean speedup over DScout's fixed configuration.

---


### 23. [Beyond Prediction: A Component-Level Study of Concept Recovery in In-Context Learning](https://arxiv.org/abs/2610.23936)

**<font color=#1a73e8>作者：</font>** Xufeng Liu, Fang Wan, Yi Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) enables language models to make accurate predictions from demonstrations, but prediction success alone does not reveal the extent to which the underlying concept has been recovered. Existing evaluations typically assess recovery at the level of the whole concept, making it difficult to identify which components are recovered and to separate model limitations from ambiguity in the demonstrations. We introduce a component-level framework for concept recovery that decomposes concepts into their defining components and uses controlled structural interventions to evaluate both component-level and whole-concept recovery under identifiable demonstrations. Across four instruction-tuned LLMs and three composition forms, we find that models often achieve high prediction accuracy despite poor whole-concept recovery, with systematic over-specification of relevant attributes and level constraints. Individual structural components are generally insufficient for whole-concept recovery, whereas jointly specifying complementary components, particularly relevant attributes and their level constraints, substantially improves recovery. However, this improvement is fragile: a single plausible but unnecessary level constraint can substantially disrupt recovery. Finally, joint supervision of recovery and implicit prediction substantially improves recovery while preserving prediction performance, with the learned capability transferring across composition forms. Overall, our component-level analysis provides a more diagnostic view of what models recover from demonstrations than the existing holistic view.

---


### 24. [PeekKV: The First Content Token Already Knows Which Heads Matter](https://arxiv.org/abs/2610.23939)

**<font color=#1a73e8>作者：</font>** Minyoung Go, Yongjun Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The size of the KV cache grows linearly with context length, making it a major memory bottleneck in LLM serving. Motivated by recent progress in identifying the functional roles of attention heads, a growing body of work compresses the KV cache non-uniformly across heads. Existing methods either fix the important heads via offline profiling or select them using attention signals from the prefill stage. In both cases, however, accuracy fluctuates substantially across workloads. While investigating the cause of this instability, we find that the active heads shift between the prefill and decode stages even within a single input. Along the decode path, by contrast, the activehead composition remains stable across content tokens once format tokens are filtered out. Based on this observation, we propose PeekKV. PeekKV observes a single content token immediately after prefill - a one-token peek - to jointly obtain head-group scores and token-importance scores. Guided by these scores, PeekKV allocates KV cache budgets to head groups in proportion to their group scores and retains only the top-scoring tokens within each budget. PeekKV requires no offline profiling or training and thus applies directly to unseen workloads and new models. Across four public benchmarks, PeekKV achieves the highest accuracy in more than half of the per-model comparisons against state-of-the-art methods, and stays closest to the full-cache accuracy on RULER and LongBench. On Llama-3.1-8B-Instruct, PeekKV retains 95.7% of the full-cache accuracy at a 10% memory budget on RULER with 16K contexts and 95.9% at a 1.5% budget on LongBench.

---


### 25. [ReTTT: Reflection-Driven Test-Time Training via Experience-Based Parametric Memory](https://arxiv.org/abs/2610.23942)

**<font color=#1a73e8>作者：</font>** Kangcong Li, Hangfan Zhang, Shuyue Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents accumulate valuable task-specific information through their actions, observations, and environmental feedback during multi-turn task execution. When effectively used, this information can help agents refine subsequent decisions and improve task performance. However, the learning value of an interaction depends on its context and subsequent feedback, making it challenging to extract reliable, actionable lessons and revise them as the task unfolds. In this paper, we introduce ReTTT, which enables experience-driven self-adaptation through test-time training on lessons constructed and continually revised within an episode. ReTTT lets the agent reflect on interaction feedback, maintain the resulting lessons in an explicit memory, and learn from them by updating an episode-local LoRA adapter while keeping the backbone frozen. The adapted model then performs both subsequent actions and reflection, coupling policy adaptation with the construction of future learning experience. We evaluate ReTTT on ALFWorld, ScienceWorld, and SWE-bench Lite using two model families. ReTTT outperforms trajectory-based test-time training across all six model--benchmark settings, improving task success by up to 12.14 percentage points. A frozen-reflection comparison further shows a 7.14-point benefit from adapting the reflection policy, while trajectory analysis illustrates how adapted reflection derives more task-specific guidance from failed attempts. These findings suggest that learning to reflect on its own behavior can boost agents' performance on long-horizon tasks.

---


### 26. [CrowdH-Edit: Reference-Guided Instruction-Based Synthetic Hajj Crowd Image Generation for Crowd Counting](https://arxiv.org/abs/2610.23945)

**<font color=#1a73e8>作者：</font>** Amirah F. Alshammari, Bander A. Alzahrani, Nahed A. Alowidi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The scarcity of domain-specific annotated images remains a major limitation for developing computer-vision systems for Hajj crowd analysis. Existing crowd-counting datasets and unconstrained generative models do not capture Hajj-specific visual conditions, including sacred-site geometry, white-clothed pilgrim crowds, and indoor/outdoor illumination variation. This study presents CrowdH-Edit, a reference-guided, instruction-based framework for synthetic Hajj crowd-image generation. Real Hajj images provide structural references, while textual instructions guide changes in crowd conditions and illumination and help preserve the main scene layout. Stable Diffusion 2.1 and Stable Diffusion XL 1.0 with low-rank adaptation were evaluated as comparative baselines. Qwen Image Edit was used without additional training within a ComfyUI workflow and selected for final dataset construction. The workflow produced CrowdH-Edit, a cleaned pool of 6,122 synthetic images, from which 387 images were selected and annotated to construct CrowdH-Edit-Ann-387. Among the evaluated generation pipelines, Qwen Image Edit achieved the highest semantic-alignment score and the lowest distributional and perceptual distances. Downstream evaluation across five crowd-counting models showed that adding the annotated synthetic subset to real training data reduced mean absolute error for three models and root mean squared error for two. These findings indicate that reference-guided synthetic Hajj imagery can support crowd-counting training, although its benefits depend on the model and evaluation metric.

---


### 27. [How Data Scales in Agentic Reinforcement Learning: Laws and Synthesis Strategies](https://arxiv.org/abs/2610.23946)

**<font color=#1a73e8>作者：</font>** Bowei He, Yankai Chen, Xiaokun Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretraining scaling laws treat training data as a one-dimensional quantity: a token count. Agentic reinforcement learning (RL) inherits this scalar abstraction, but modern synthesis pipelines now generate \textit{tasks}, \textit{environments}, and \textit{trajectories} independently and at very different costs, turning data into a structured design space. This raises a question pretraining never had to answer: given a synthesis budget, \textit{which axis} should be scaled? We address this question end-to-end with three tightly coupled contributions. First, we decompose agentic data into three cardinality axes (task, environment, trajectory), plus a reward-density control variable, and fit per-axis scaling relations on different large language models (LLMs) across math+code, SWE, web, and UI/tool application domains. Across all model sizes, model families, domains, and RL algorithms (PPO and GRPO) we measured, the scaling exponents order as environment $>$ task $>$ trajectory. When environment diversity is decomposed into world and environment-structure diversity, its advantage is mainly driven by the former, while the latter is just comparable to the task diversity. Second, we use the fitted laws as a common ruler to price synthesis methods, capturing each method's efficiency as a per-axis discount factor and identifying critical synthetic-to-real ratios at which collapse begins; these ratios differ by an order of magnitude across axes. Third, we cast budget allocation as a constrained optimization under our laws and discounts, deriving a Chinchilla-style compute-optimal recipe and validating it at held-out scale. The empirical results demonstrate that following the recipe yields up to $1.7\times$ compute efficiency over the dominant ``scale-the-trajectories'' practice.

---


### 28. [Compaction-Aware Reinforcement Learning For Ascend Triton Kernel Generation](https://arxiv.org/abs/2610.23950)

**<font color=#1a73e8>作者：</font>** Chuansai Zhou, Yanlin Liu, Bingning Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatically generating high-performance kernels with LLM-based agents promises substantial gains in development efficiency, but two obstacles remain. First, while increasing multi-turn interaction with execution environments is crucial for refining generation quality, continuous context accumulation rapidly exceeds the model's effective context window. Second, training long-horizon tasks via GRPO inherently incurs sparse rewards due to its reliance on terminal outcome evaluation, severely hindering step-level credit assignment; To address these obstacles, we propose ATRL (Ascend Triton Reinforcement Learning), a post-training method that refines GRPO into a compaction-aware, segment-level objective for long-horizon kernel generation. We also design a lightweight agent harness providing cascaded compilation, correctness, and profiling feedback, alongside an Ascend-specific knowledge base injected during agentic RL training and evaluation to compensate for the base model's missing platform expertise. Evaluations on NPUKernelBench and KernelBench, both executed on Ascend hardware, show that ATRL consistently surpasses all baselines, including GRPO, in both correctness and speedup.

---


### 29. [LatLM: Line-Parallel Language Models with Deferred Commitment](https://arxiv.org/abs/2610.23951)

**<font color=#1a73e8>作者：</font>** Shaorong Zhang, Shiyuan Li, Longxuan Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Line-parallel language models advance multiple lines concurrently for substantial speedups. However, frameworks like the Line-Coupled Language Model (LCLM) enforce a fixed commitment schedule across lines. Because dependencies vary within text, a fixed schedule cannot hold back a line whose prerequisites remain uncomputed, forcing premature commitments and cascading reasoning errors. To address this limitation, we introduce the Lattice Language Model (LatLM), making commitment schedules an adaptive decoding-time choice. Text occupies a 2D lattice where eligible frontier tokens are scored each round; a policy commits confident candidates while deferring unready ones for extended context. One forward pass supervises entire sampled trajectories via 2D causal masking, while an append-only cache retains exact states. At 482M parameters, we establish two findings. (1) LatLM matches a data- and capacity-matched autoregressive model on held-out text when decoded sequentially, while its adaptive parallel decoder achieves near-autoregressive accuracy on independent-line tasks using 25--41% as many decoding rounds. (2) When cross-line dependencies cause LCLM's fixed schedule to fail, deferred commitment substantially improves accuracy while retaining parallelism where dependencies permit. On mixed dependency chains, LatLM achieves 96.5% accuracy versus LCLM's 78.5%, using fewer than half the decoding rounds of the autoregressive baseline.

---


### 30. [Functionalizing AI-Generated 3D Shapes via Interior Geometry Construction](https://arxiv.org/abs/2610.23953)

**<font color=#1a73e8>作者：</font>** Haoyu Tang, Fancheng Gao, Kan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-based 3D generation models such as Hunyuan 3D and Meshy can produce visually appealing 3D shapes from an image or text this http URL, they typically focus on an object's external appearance, often producing incomplete or implausible interior geometry. Consequently, the generated shapes are not guaranteed to be functionally valid, limiting their direct use in downstream applications such as simulation and fabrication. In this paper, we present a computational approach to functionalize AI-generated 3D shapes through interior geometry construction. Our key observations are that a part's functional role defines its interior geometry, and such geometry is often smooth, relatively simple, and closely related to the part's external shape. Inspired by these observations, we introduce an interior-aware part graph to encode information necessary for constructing interior geometry within an AI-generated 3D shape, and build the graph via VLM-based shape segmentation and graph attribute inference. Guided by the graph, we model the interior geometry of each part as a generalized cylinder and infer its parameters from the part's external geometry through an optimization. The resulting 3D shapes are functionally valid while preserving their AI-generated external appearance. We demonstrate our approach on a variety of AI-generated 3D shapes, including vessels, containers, and storage furniture, and fabricate selected examples for functional validation.

---


### 31. [Same Space or Not: Benchmarking Spatial Intelligence Through Cross-View Contradictions](https://arxiv.org/abs/2610.23959)

**<font color=#1a73e8>作者：</font>** Huizi Cao, Guanyu Xu, Zhixuan Liang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence, the capacity to represent and reason about physical space, underlies embodied perception and real-world visual understanding. Existing benchmarks probe it through spatial relations, perspective-taking, and mental modeling. What remains underexamined is whether a model can maintain a coherent scene representation across views, since pairwise comparison alone cannot reveal which view departs from the truth. We thus introduce Same Space or Not (SSoN), a benchmark of cross-view contradiction resolution comprising 1,000 questions from seven indoor scene sources and six categories of controlled 3D edits. Each question presents three views of an unchanged scene and one view of an edited variant. Models must identify the inconsistent view and explain the contradiction without a designated trusted reference or a marked target. Our pipeline iteratively translates human review into generation constraints. Automated checks and exhaustive human validation screen out both trivial visual shortcuts and questions lacking sufficient evidence for a unique answer. Humans achieve 83.3% accuracy, compared with 39.7% for the strongest vision-language models (VLMs), falling to 34.9% when a valid visual explanation is also required. We investigate prompting, camera information, and 3D reconstruction as interventions. On a 100-question intervention set with a 24% baseline, prompting and 3D reconstruction remain below 50% answer accuracy, except when ground-truth camera information is supplied, which reaches 61% answer accuracy but only 48% True solve accuracy. On a held-out 201-question test set, Qwen2.5-VL-7B achieves 21.89% accuracy, 33.33% after answer-only fine-tuning, and 41.79% after fine-tuning on both rationales and answers. These results identify cross-view contradiction resolution as a substantial weakness of current VLMs that can be partly addressed by targeted supervision.

---


### 32. [UltraData-Code: From Raw Repositories to Algorithmically Dense and Task-Oriented Code Data](https://arxiv.org/abs/2610.23960)

**<font color=#1a73e8>作者：</font>** Chengying Tu, Hengyu Zhao, Shuaikang Xue 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Code generation has become a core capability of large language models (LLMs), and code data is central to the pre-training process that develops it. As obtaining public code of sufficient quality becomes more difficult, further progress cannot rely on corpus expansion alone. Tiered data management instead applies increasingly targeted processing to smaller data pools, producing data states suited to different training objectives. Following this perspective, we present UltraData-Code as four connected data states spanning repository archival at L0, standardized natural code at L1, algorithmic selection at L2, and task-oriented synthesis at L3. L0 preserves repository data and provenance for reprocessing, while L1 applies scalable filtering, normalization, and near-deduplication for broad pre-training. L2 selects high-quality algorithmically relevant files using language-adaptive relevance signals and quality constraints, yielding approximately 400B tokens of UltraData-Code-L2 across 11 programming languages for focused continual pre-training. L3 converts selected implementations into structured programming exercises, yielding approximately 150B tokens of UltraData-Code-L3 across the same 11 languages for task-oriented mid-training or supervised fine-tuning (SFT). Under controlled 10B-token continual pre-training of a 1B model, L2 improves pass@1 over L1 by 7.80 percentage points (pp) on EvalPlus and 5.13pp on MultiPL-E. Replacing half of the L2 training tokens with L3 yields a further gain of 8.42pp and 8.07pp on the two benchmarks, respectively. Both gains increase when the training budget scales to 100B tokens. We have released our datasets and classifiers to support further research on LLMs.

---


### 33. [A Controlled LLM Workflow for Evidence-Grounded Diagnosis of Risk Score Differences](https://arxiv.org/abs/2610.23962)

**<font color=#1a73e8>作者：</font>** Hanqing Dou, Zijia Cao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a controlled Large Language Model (LLM) workflow for explaining risk score differences using similar historical transactions. The workflow combines reference retrieval and contrastive SHapley Additive exPlanations (SHAP) evidence with reference-based LLM reasoning and deterministic validation. Experiments on a test dataset show that the workflow produces more consistent, evidence-grounded and traceable diagnoses than the same LLM without structured workflow guidance.

---


### 34. [Learning When to Trust and Reobserve Sparse-Frame VideoQA from Temporal Sampling Perturbations](https://arxiv.org/abs/2610.23969)

**<font color=#1a73e8>作者：</font>** Shujia Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse-frame video-language models can change their answers when only the sampling timestamps shift. Raw agreement exposes this problem, but it need not rank errors better than token confidence or identify which additional observation will repair an answer. We argue that answer risk and action value must be estimated separately. PhaseGuard+ probes a frozen VLM at controlled temporal offsets, predicts the reliability of the phase-vote answer, and predicts the example-wise correctness gain of a specific rescue action. The second score routes only examples expected to benefit from denser frames or a stronger VLM. Both predictors use lightweight models trained on public data; the VLMs remain frozen. We use 256 Perception Test videos for method development and evaluate on a disjoint 256-video test set comprising 554 Physics questions. For Qwen3-VL-8B, reliability AUROC rises from 68.0% with token softmax to 74.8% (+6.8 pp, 95% CI [2.6, 10.7] pp). Routing 30% of questions to Qwen3-VL-32B reaches 67.87% accuracy, compared with 63.66% for budget-matched random routing (+4.21 percentage points, CI [1.89, 6.40]). All four tested rescue pairs significantly outperform random routing. Temporal sensitivity becomes actionable when the system learns both whether an answer is unreliable and whether an available action is likely to fix it.

---


### 35. [How Much Can We Prune? Exploring the Performance Limits of Visual Token Pruning](https://arxiv.org/abs/2610.23974)

**<font color=#1a73e8>作者：</font>** Janghoon Cho, Shubhankar Borse, Reza Pourreza 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning is increasingly used to reduce the memory and inference costs of vision-language models. Existing work has largely focused on designing method-specific selectors and demonstrating incremental improvements over prior methods at selected token budgets. It remains unclear whether the resulting performance reflects an inherent limit of visual token pruning or the limitations of current token-selection algorithms. We take a complementary perspective and ask: \emph{how well can visual token pruning perform when offline search cost is not the primary constraint?} We formulate pruning for general image understanding as selecting, under a fixed budget, one shared visual-token subset that supports a broad distribution of questions about an image. We approximate this utility with a finite auxiliary QA set generated by a frontier VLM and optimize a teacher-forced answer-probability objective with the evaluated model frozen. Motivated by the conceptual monotonicity and diminishing returns of adding visual evidence, we construct nested subsets greedily and introduce \emph{QA mini-batch greedy} (QA-MBG), which estimates token marginal gains from randomly sampled QA components at each step. Empirically, QA-MBG is both cheaper and more effective than full greedy. With one frontier-VLM call and approximately $0.5$ H100 GPU-hours per image, it produces a nested subset trajectory covering keep ratios up to $0.3$. Across Qwen3-VL-4B and Gemma~4 E4B on $900$ images from nine benchmarks, we find significant headroom over evaluated pruning baselines on held-out QA and image-grounded long-form generation, while the searched subsets substantially narrow the gap to full-token inference.

---


### 36. [SPELUNKA: A Framework for Finding Unanticipated Associations in Vision-Language Models](https://arxiv.org/abs/2610.23979)

**<font color=#1a73e8>作者：</font>** Cassandra Parent, Isha Agarwal, Kumail Alhamoud 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) are the backbone of many state-of-the-art multimodal systems, but often encode spurious and harmful associations from their training data. While prior work focuses on removing known biases from VLMs, methods for discovering unanticipated associations for retrieval tasks remain underexplored. We introduce SPELUNKA, an automated, inference-time framework for finding unanticipated distributional biases for retrieval tasks in VLMs without pre-specified labeled subgroups, inference-time human supervision, or model fine-tuning. Given a concept of interest, SPELUNKA generates captions for related images, extracts relevant entities from captions, and selects semantically meaningful associations. A frequency-based detection rule then identifies spurious associations by measuring over- or under-representation of these attributes in a VLM's top-ranked outputs relative to their full dataset distribution. We evaluate SPELUNKA across four datasets, and find that it 1) successfully recovers both synthetic and naturally occurring spurious correlations, 2) achieves an average AUROC of 0.93 across four datasets in identifying images strongly associated with a query, and 3) outperforms baselines in finding features that are strongly associated with a given query.

---


### 37. [RL Teaches VLMs Where to Attend but Not How to Perceive](https://arxiv.org/abs/2610.23983)

**<font color=#1a73e8>作者：</font>** Ziqian Zhang, Junjie Liao, Zhining Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although reinforcement learning (RL) effectively trains Vision-Language Model (VLM) agents, the mechanisms behind these capability gains are poorly understood. Across four diverse agent environments, we investigate whether the task-success gains from multi-turn RL are accompanied by improved grounded visual question answering about the environment. To assess this, we design environment-specific grounded VQA tasks that reveal improvements in grounded visual understanding. Representational probing shows that vision-encoder probe accuracy remains relatively stable, while LLM-layer probe accuracy improves. Attention analysis further reveals that LLM layers pay more attention to visual tokens during RL training. To test whether increased attention to visual tokens contributes to VQA gains, we introduce a lightweight plug-and-play intervention using a fixed attention bias. Without updating model parameters or computing gradients, this intervention partially restores VQA gains on the untrained model. These results reveal better utilization of visual information as a key mechanism behind the gains from RL.

---


### 38. [BlenderWorld: Benchmarking Visual Agents for 3D Creation from Real-World References](https://arxiv.org/abs/2610.23986)

**<font color=#1a73e8>作者：</font>** Xinyu Fang, Yuchi Wang, Weihao Yu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal large language models (MLLMs) have enabled them to act as autonomous agents, creating and editing 3D models via code or direct software manipulation. In practical workflows, these models must infer object shapes, materials, spatial layouts, and lighting from diverse references while strictly following instructions to reconstruct, modify, or design 3D content. However, existing benchmarks provide limited coverage of such open-ended requests across real-world scenarios. To bridge this gap, we introduce BlenderWorld, the first comprehensive benchmark dedicated to evaluating frontier models on realistic 3D creation tasks. BlenderWorld comprises 223 tasks spanning architecture, products, natural environments, and scientific visualization, driven by text, image, video, and structured specification inputs. To rigorously assess these complex deliverables, we establish a unified evaluation protocol: we render the submitted Blender projects from multiple viewpoints and evaluate them against 2,651 task-specific binary rubrics alongside holistic visual quality scores. Benchmarking thirteen frontier models reveals that GPT-6-Astra achieves the highest overall fused score of 79.9, followed by Opus-5 (73.0) and GPT-5.6-Sol (67.7). Ultimately, our findings reveal a critical bottleneck: while current models can parse broad instructions, they still profoundly struggle with fine-grained 3D spatial coherence and accurate structural reproduction in Blender, leaving substantial headroom for future 3D-native agentics.

---


### 39. [What Generation Knows: Unlocking Fine-Grained Understanding in Unified Multimodal Models](https://arxiv.org/abs/2610.23987)

**<font color=#1a73e8>作者：</font>** Tengju Ru, Weitong Lian, Zecong Tang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained visual understanding requires distinguishing subtle differences in local attributes and spatial relations, yet remains challenging for existing vision-language models. Unified multimodal models (UMMs) offer a new opportunity through generation pathways that preserve rich visual information complementary to understanding. However, existing generation-assisted understanding methods mainly rely on generative supervision or explicit generation and have not systematically explored direct use of native generation-side representations. To address this gap, we systematically analyze what generation-side representations offer for fine-grained understanding, finding that they are more sensitive to fine-grained semantic changes, capture task-relevant changes missed by understanding-side representations, and depend on correct spatial organization for this advantage. Guided by these findings, we design GAFU, a post-training framework that unlocks native generation-side information for fine-grained understanding. It compresses generation-side visual representations into compact \(G\) tokens that preserve fine-grained visual details, enabling task-conditioned retrieval by the understanding pathway. Experiments show that GAFU consistently outperforms SFT baselines trained on the same data across diverse visual understanding tasks and UMM architectures, with maximum relative improvements of 20.00\%, 17.94\%, and 8.62\% on VStar-Bench, OmniSpatial, and VSR-Bench, respectively. Overall, GAFU converts complementary information from the generation pathway into gains in fine-grained visual understanding, providing an effective path toward synergy between generation and understanding in UMMs.

---


### 40. [Single-Pass Decision Scores Enable Rapid Classification with Adjustable Thresholds in Medical Multimodal Large Language Models](https://arxiv.org/abs/2610.23988)

**<font color=#1a73e8>作者：</font>** Patrick Wienholt, Frederik Hauke, Christiane Kuhl 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) answer binary clinical questions with a yes or no token, leaving the decision threshold implicit and fixed. We derive a continuous score from a single forward pass by renormalizing the probabilities of the yes and no tokens, allowing the threshold to be adapted to clinical needs without retraining. We evaluated this approach with MedGemma and Gemma-3 (4B and 27B) on six medical imaging datasets. The default threshold was frequently misaligned with the task: for identifying normal chest radiographs, MedGemma-27B labeled every image as abnormal, whereas a validation-selected threshold yielded a sensitivity of 0.945 and a specificity of 0.696. Normalization achieved the highest AUROC on four of six datasets (CheXpert: 0.819 vs. 0.777 for raw and 0.743 for text-elicited probabilities), and a single decision required 53-79 ms on one GPU. This simple post-hoc method turns medical MLLMs into fast classifiers with adjustable operating points. Code: this https URL

---


### 41. [ProV-Mem: Proactive Memory for Streaming Video Question Answering](https://arxiv.org/abs/2610.23998)

**<font color=#1a73e8>作者：</font>** Bingbing Wang, Jing Li, Han Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Proactive streaming video question answering requires a model to continuously monitor an incoming stream and autonomously decide when to speak, what to say, and whether to emit a response. Existing streaming systems face a fundamental difficulty: retaining long visual histories is costly, whereas discarding them can lead to missed events and repeated responses. We propose \textbf{ProV-Mem}, a training-free proactive memory framework built around a frozen VLM backbone. ProV-Mem decomposes the proactive decision into three lightweight memory tiers: a temporal-trigger memory controls when to query the backbone and recovers from prolonged silence, an instructional memory guides what to say through a fixed prompting prior for concise and visually grounded generation, and an episodic memory determines whether to emit by filtering near-duplicate responses. Under an idealized conditional-sufficiency assumption, we derive a stagewise approximation bound relating the decomposed process to a full-state joint policy. We further introduce Cost-Aware Area Under the Curve (\textbf{CAUC}), which extends PAUC by explicitly discounting redundant, overly frequent, and unnecessarily long emissions. Experiments on the four scenarios of ProactiveVideoQA show that ProV-Mem achieves the best CAUC across all scenarios and the best PAUC on WEB, EGO, and TV, while maintaining low per-response inference latency.

---


### 42. [PACE: Pareto-Adaptive Compression for Efficient Native MLLMs](https://arxiv.org/abs/2610.24005)

**<font color=#1a73e8>作者：</font>** Lei Tian, Chunzheng Zhu, Kai Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Native multimodal large language models (native MLLMs) jointly encode visual and linguistic sequences within a unified autoregressive Transformer, emerging as a promising paradigm for multimodal understanding. Unlike conventional ViT-based MLLMs relying on external vision encoders, ViT-free native MLLMs tokenize pixel patches directly, potentially suffering severe visual token redundancy. A pilot study confirms this: unlike ViT-based models that degrade under compression, ViT-free MLLMs tolerate aggressive compression with near-lossless or even improved performance. Yet existing compression methods target ViT-based settings, leaving native MLLMs, which stand to gain the most, unexplored. To close this gap, we introduce an analysis pipeline centered on token discriminability and cross-dimensional heterogeneous redundancy, revealing that (i) redundancy is distributed independently and heterogeneously along height and width axes, and (ii) early-layer visual tokens are indiscriminable and uniformly redundant. Guided by these findings, we propose PACE (Pareto-Adaptive Compression for Efficient Native MLLMs), the first visual token compression framework tailored for native MLLMs with Multimodal-RoPE. Leveraging dimensional decoupling of positional encoding, PACE decomposes attention into two orthogonal spatial saliency estimates along height and width, gated by a positional attention signal, yielding direction-aware importance with negligible overhead. It further casts token budget allocation as Pareto optimization over performance preservation, inference efficiency, and spatial coverage, jointly identifying optimal compression depths and retention ratios. Experiments show PACE maintains near-lossless performance at only 25%-50% visual token retention, even improving several benchmarks, while delivering over 2x FLOPs reduction.

---


### 43. [Federation over Harness](https://arxiv.org/abs/2610.24007)

**<font color=#1a73e8>作者：</font>** Dixi Yao, Tahseen Rabbani, Tian Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Modern LLM-powered agents increasingly improve through experience sharing, where distributed agents distill local reasoning experience into reusable knowledge, such as a shared insight library. Existing approaches, however, still heavily rely on manually designed prompts and workflows that determine both how local agents extract useful reasoning traces and how a central/global agent aggregates them to obtain common patterns and insights. We propose Federation over Harness (FoH), a framework that automatically evolves the harness for both local and global components in this distributed multi-agent reasoning pipeline. A server agent evolves the client harness for task solving and self-reflection while, at the same time, evolving its own harness for aggregating distributed reflections, maintaining shared knowledge, and updating subsequent client harnesses. Importantly, FoH requires no extra validation signals, such as ground-truth labels or validation data, during evolution; it learns solely from self-generated reflections produced by distributed agents. Experiments on multiple benchmarks show that FoH consistently improves over single-agent baselines with a fixed harness and with harness self-evolution by 53.57% and 29.76%.

---


### 44. [Beyond Explicit Intent: Discovering and Shaping Artistic Intent through Human-AI Co-Creation](https://arxiv.org/abs/2610.24010)

**<font color=#1a73e8>作者：</font>** Renye Yan, Jialun Zhong, Jikang Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI is becoming an important medium for artistic creation, yet existing interactions often assume that creators can specify intentions in advance and accurately communicate them through text prompts. Artistic intentions, however, may be vague, latent, or recognizable only after seeing concrete visual possibilities. We propose a human-AI co-creation paradigm beyond explicit intent expression. By expanding model exploration, we expose artists to diverse visual possibilities, allowing them to identify previously unarticulated preferences through observation, comparison, and selection. We then integrate artists' curatorial judgments into reinforcement learning, assigning different learning strengths based on preferences over generation trajectories, so recognized directions are more strongly reinforced and the model gradually adapts to individual aesthetics. This creates a continuous "explore-identify-shape-re-explore" loop in which artistic intent is progressively discovered, externalized, and shaped. Through three user studies, we examine latent-preference discovery, personalized preference alignment, and the externalization of vague, difficult-to-express creative intentions.

---


### 45. [TWIN-MoE: Two-stage Intra-Expert Imputation Network for Incomplete Multimodal Learning](https://arxiv.org/abs/2610.24014)

**<font color=#1a73e8>作者：</font>** Liang Nathan Zheng, Jiyuan Liu, Wenhao Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent Mixture-of-Experts (MoE) approaches address missing modalities either by routing each missingness pattern to a dedicated expert, which scales poorly as the number of modalities grows, or by imputing the missing modality from representations contributed by multiple experts, which requires a costly retrieval mechanism. We show that routing induces expert-conditioned representation neighborhoods and derive an imputation-error bound controlled by their local feature dispersion. When these expert-conditioned neighborhoods are more compact than the global representation space, intra-expert aggregation admits a tighter worst-case reconstruction bound than unconstrained global aggregation. Guided by this analysis, we propose TWIN, a two-stage intra-expert imputation framework. Pre-imputation generates a context-conditioned estimate in the encoder embedding space and radially soft-clips it using modality-specific statistics maintained in an observed FIFO queue, this ensures that the pre-imputed modality stays in empirically calibrated region of the target modality space. Post-imputation refines the missing representation after MoE by aggregating expert-conditioned observed representations within the same sample. Across four missing-modality benchmarks under natural, random, and asymmetric dropout protocols, TWIN achieves state-of-the-art performance while using substantially fewer parameters than competing MoE-based imputation methods.

---


### 46. [Unified Multiparadigm Fusion Intelligence for Rare Disease Diagnosis](https://arxiv.org/abs/2610.24024)

**<font color=#1a73e8>作者：</font>** Jian Yang, Peiling Liu, Songda Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rare diseases (RDs) affect an estimated 300 million people globally, leaving patients to navigate a protracted diagnostic odyssey constrained by clinical scarcity and fragmented medical knowledge. Artificial intelligence (AI) has progressively advanced RD diagnostics, from symbolic methods and deep learning to large language model (LLM)-based systems. However, each paradigm carries structural limitations: symbolic methods are bounded by knowledge completeness, neural models sacrifice interpretability, and LLM-based systems are vulnerable to evaluation biases like data leakage. In this study, we introduce FusionRare, a unified multiparadigm fusion framework integrating knowledge-driven symbolic reasoning, deep-learning pattern recognition, case-based patient retrieval, and LLM-based heuristic inference via statistical meta-aggregation and knowledge-enhanced agentic reflection. Evaluated on 2,528 strictly isolated clinical cases, FusionRare achieves state-of-the-art RD prioritization, attaining a macro-averaged Recall @1 of 51% for phenotype-only diagnosis and 79% for phenotype-genotype joint analysis. These results represent decisive advantages over the advanced agentic system DeepRare, frontier LLMs including GPT 5.5, and specialized tools like PhenoBrain and LIRICAL under stringent anti-leakage protocols. A randomized, crossover clinician-AI validation demonstrated that FusionRare elevates the true diagnostic rank in 45% of decisions, improves physician confidence in 62%, and reduces time to diagnosis by 21%. These findings indicate that reconciling these orthogonal AI paradigms significantly enhances diagnostic capabilities, bridging the gap between computational benchmarks and actionable clinical reliability. More broadly, this work provides a replicable framework for deploying trustworthy diagnostic AI across complex, high-stakes, and underserved medical domains.

---


### 47. [Do Knowledge and Reasoning Oriented Benchmarks Induce Stable Representation Signatures in LLMs?](https://arxiv.org/abs/2610.24029)

**<font color=#1a73e8>作者：</font>** Parsa Rahimi, Azim Dehghani Amirabad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Internal signatures could support monitoring, adaptive computation, and mechanistic analysis, but benchmark prompts can be separable without any shared computational distinction. We test whether a prespecified knowledge/reasoning label defines a reusable internal signature in five contemporary 7B to 31B models. We treat the \textbf{task} as the unit of inference probes hold out complete tasks, labels are permuted across tasks, and the best layer and stream are reselected for every permutation. Raw probes recover an eight-versus-eight-subject MMLU partition in all five models (macro-F1 $0.78$--$0.81$), but prompt text predicts it nearly as well: under an identical probe configuration, the activation advantage is only $0.017$--$0.070$ macro-F1 and is not significant. At the prespecified $0.01$ level, lexical adjustment removes significance while the adjusted states still identify individual subjects, and the selected site changes across task panels and selection rules. Additionally, two released base-training trajectories show no common direction. These pooled layerwise measures recover the task label but identify no transferable knowledge/reasoning signature at the tested sensitivity, which cannot exclude moderate effects. The resulting protocol gives future internal monitors and intervention studies a sequence of tests to pass. Project page: \url{this https URL}.

---


### 48. [Visual Causal-chain Bookmarking: Retrieval-Weighted Credit Assignment for Reinforcement Learning from Delayed Reward](https://arxiv.org/abs/2610.24032)

**<font color=#1a73e8>作者：</font>** Prathap Selvakumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> RL agents trained on a single trajectory-level return face a credit-assignment problem: when a reward arrives many steps after the decision that caused it, every action gets the same signal regardless of causal responsibility. This paper studies Visual Causal-chain Bookmarking (VCBM), which concentrates credit on the decision points that determine an episode's return, via two instantiations. The first targets a fully observed, low-dimensional MDP (a delayed-reward watch-repair task), where VCBM statistically discovers which state components the agent causally controls and estimates per-decision-point action values directly, evaluated against ground truth and RUDDER, an LSTM-based baseline. VCBM converges to 95.07% correct decisions in a mean of 1,532.3 episodes across 20 seeds, versus RUDDER's slower, more variable convergence (mean 3,327.1 episodes; p<0.001); VCBM's discovered causal structure exactly matches ground truth in all seeds. The second targets a partially observed, language-based setting: an LLM agent trained with Leave-One-Out PPO (LOOP) in AppWorld, where causal discovery is intractable and a structural heuristic (state-mutating tool calls) substitutes for it, with credit distributed via retrieval over episodic memory and blended with LOOP's advantage. Over 200 iterations on identical Qwen2.5-7B-Instruct/LoRA/FSDP2 configurations, VCBM-blended LOOP improves task success over plain LOOP (0.354 vs. 0.458), reduces final-step max importance weight, and improves token efficiency, with a small KL exception favouring LOOP. The watch-repair result supports the claim that weighting causally relevant steps is more sample-efficient than an undifferentiated baseline or a learned return-redistribution network; the AppWorld result, limited to one seed per arm by a 2-GPU budget, is a compute-limited demonstration at a harder, natural-language scale, not a statistical confirmation.

---


### 49. [LLM Evolution in a Simple Simulated Market](https://arxiv.org/abs/2610.24033)

**<font color=#1a73e8>作者：</font>** Charlie Pilgrim, Christopher Krupenye, Dora Biro 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Arguments that AI systems will evolve in harmful ways are largely made in the abstract. We provide a concrete empirical example. We simulate simple markets consisting of populations of twenty Large Language Model agents tasked with solving arithmetic problems. Agents differ only in their system prompt; those that go bankrupt are removed and replaced by mutated copies of the prompts of successful agents. Two market conditions select for opposite phenotypes: a market that rewards accuracy produces agents with high accuracy (94%) and high token use; a market that charges per token produces agents with low accuracy (10%) and low token use. In the second market, only tokens are incentivised yet we see a collapse in accuracy. Token use and accuracy are correlated traits such that selection on one also moves the other, and behaviour adapts along an unpriced dimension. A third neutral condition with no selection allows us to separate these effects from bias in the mutation operator. Adaptation occurs through a collective optimisation process that operates above the level of individual agents, who are never told the payment rule, do not receive feedback, and have no memory.

---


### 50. [ToolRosetta: Surface-Form Invariance of Tool-Call Guards](https://arxiv.org/abs/2610.24055)

**<font color=#1a73e8>作者：</font>** Hasan Demirkiran, Jens Ernstberger  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Step-level guards for tool-using agents are evaluated on tidy JSON tool calls, but deployed coding agents act through execute_bash and execute_code tools whose payloads are strings. We introduce ToolRosetta, which re-renders every candidate action in the AgentDojo and AgentHarm splits of TS-Bench as a Python call, as a shell command, and without the agent's rationale. The renderings are produced by code and verified by round-trip parsing, so the user request, the history, the label and the action's effect stay fixed while only the surface form changes. Across eleven guards with two placebo controls, frontier and strong open-weight guards are stable: no frontier error rate moves by more than 3.4 points. Four of five specialized agent guards are not: under the shell form their false-positive rates rise by 21 to 47 points on AgentDojo, and TS-Guard's by 38 points on its own home benchmark, blocking between a third and nine in ten benign actions; the fifth, StepGuard, does not move. A small open guard drifts five points more permissive. Removing the agent's rationale moves most guards whose input carries it, in guard-specific directions. A request-blind control on one guard shows that the rationale is where intent is read from. A parser that restores the canonical call in front of the guard removes the effect for these renderings, by construction. Benchmark accuracy on JSON calls does not predict a guard's operating point behind a code-acting agent.

---


> [!TIP]
> 当前位于：**1-50**（第 1/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
