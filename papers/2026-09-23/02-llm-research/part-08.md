# 🧠 大模型相关研究 | 2026年09月23日

> 本类共 **379** 篇论文：已确认 **359** 篇，待复核 **20** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-379**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-379**

---

### 351. [Whose Facts Count? A Culturally Responsive Audit of LLM Evaluation Benchmarks](https://arxiv.org/abs/2609.24934)

**<font color=#1a73e8>作者：</font>** Fatima Tuz Zahra, Md. Sajeebul Islam Sk., Rachel Chung  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM benchmarks function as evaluation instruments, informing decisions that affect education, labor, and public services worldwide. Drawing on Hood, Kirkhart, and Hopson's culturally responsive evaluation (CRE) frameworks, this paper applies a six-dimension CR rubric to audit OpenAI's SimpleQA (N = 4,326 items) and the LMSYS Chatbot Arena (N = 600 conversations). Every SimpleQA question requires English-language archival verification as its evidentiary basis. A single rater's preoccupation with Colombian founding dates accounts for 2.70% of items, inflating the appearance of Global South coverage. English-language prompts constitute 76.3% of Arena conversations, against an International Telecommunication Union (ITU)-estimated 25.9% share of global internet users. A 50-item counter-benchmark scored a mean CR deficit nearly three times lower than SimpleQA (Cohen's d = 1.01). The paper proposes a practical CR evaluation framework. These are structural validity failures, not incidental measurement problems, with direct consequences for communities whose knowledge traditions these instruments were not built to see.

---


### 352. [Emergent Collusion in Long-Horizon LLM Agent Interaction](https://arxiv.org/abs/2609.24967)

**<font color=#1a73e8>作者：</font>** Xinrui Shi, Yanzhe Zhang, Diyi Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly deployed in collaborative settings, yet long-term interaction may give rise to undesirable coordination. We study the emergence of collusion in a long-horizon multi-agent environment: two agents repeatedly complete individual tasks, share task logs, verify each other's work, and receive rewards. We introduce realistic constraints that make compliance with the verification protocol incompatible with reward maximization, and find that agents increasingly deviate from the protocol over repeated interactions. Collusion emerges in 94% of trajectories across 10 models, and more capable models within the same family reach it earlier. Controlled peer interventions show that collusion is shaped by peer behavior, while ablations reveal additional effects of reward structure, the verification feedback agents receive, and their interaction history. In particular, restricting the amount and scope of interaction history available to agents reduces collusion. Overall, our findings show that long-horizon interaction can reshape how agents coordinate in ways that create safety risks.

---


### 353. [Rare Event Estimation via Iterative Unalignment](https://arxiv.org/abs/2609.24969)

**<font color=#1a73e8>作者：</font>** Hanming Yang, Daksh Mittal, Jing Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As agents are deployed with increased autonomy, even extremely rare events along their stochastic output trajectories can occur and prove catastrophic. Safe deployment therefore does not depend on whether these events can occur, but on how often they might. We study the problem of estimating the probability of rare events that arise from stochastic variation in the agent's own actions. Estimating this type of risk requires searching over the combinatorially vast space of trajectories. Naive Monte Carlo is computationally prohibitive in this regime, and constructing effective importance sampling (IS) proposals requires coordinated changes to a context-dependent chain of conditional distributions. We develop a new IS method that perturbs the original model's weights to construct the proposal. The proposal is itself a differentiably parameterized language model, enabling gradient-based search over weight space. We formulate an objective that combines a differentiable surrogate for event amplification and an adaptive regularization scheme that dynamically balances amplification against estimator stability. We evaluate our approach on $\sim$120M and $\sim$2.6B models across three event families spanning 300+ rare events as rare as $10^{-9}$, with reference probabilities computed with $<10\%$ relative standard error. In our most verifiable settings, we observe that our IS estimator achieves over $800\times$ compute-weighted efficiency gains over naive Monte Carlo for events with probabilities lower than $10^{-7}$. Our implementation is available at this https URL.

---


### 354. [DolphinBench: Mapping the Pareto Frontier of Agent Memory](https://arxiv.org/abs/2609.24971)

**<font color=#1a73e8>作者：</font>** Soumil Rathi, Deshraj Yadav, Taranjeet Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents today often take real-world actions that depend on long-term memory and context recall over time. However, most current memory benchmarks are built for a conversational question-answer format, where the question itself signals that some fact must be retrieved, and often which one. Moreover, benchmarks rarely require anything beyond accuracy from submissions, allowing memory systems to make unreasonable cost/time tradeoffs to achieve higher scores.
We present DolphinBench, a benchmark that evaluates memory directly through an agent's task completion. DolphinBench includes three knowledge-work personas with roughly 500k tokens of user messages per persona and evaluates agents on tasks that depend on information from that history. We verify all 200 tasks per persona by running an agent with and without the relevant history, requiring success with it and failure without it.
Finally, we require all evaluations to report total cost and latency alongside accuracy, which enables us to evaluate agent memory systems holistically. No existing memory benchmark combines all three. The dataset and evaluation code are available at this https URL.

---


### 355. [Harness-Zero: Harness Distillation via Agent-as-Harness](https://arxiv.org/abs/2609.24974)

**<font color=#1a73e8>作者：</font>** Haoran Ye, Yuxing Lu, Haonan Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent must either settle for a suboptimal shared harness or route among an ever-growing set of specialized ones. We therefore study agent harness distillation: using a domain- or instance-optimized harness as training-time guidance and transferring the behaviors it induces into model weights, so that its gains survive under a single fixed target harness. The challenge is that the two harnesses differ in action space and available information, so guidance from the optimized harness cannot serve directly as supervision for the target one. We introduce Harness-Zero, which enables harness distillation through agent-as-harness. Guided by the optimized harness, a harnessing agent corrects student responses before execution in the target harness's action space, turning harness guidance into training demonstrations. Fine-tuning on the resulting trajectories internalizes harness-induced behavior into the model, so the specialized harness can be removed at deployment. Our experiments spanning knowledge work, tool use, and science domains show that: (1) For frontier LLMs using the same evolved harness, agent-as-harness outperforms code-as-harness. (2) With the specialized harness removed at deployment, Harness-Zero improves the base model's macro-average task success from 23.3% to 44.3%, even exceeding the 41.7% it reaches with that harness still attached. (3) Harness-Zero recovers harness-induced behaviors absent from the base model, with 82.3% average recovery across 28 patterns in the three domains.

---


### 356. [LoRA-generating hypernetworks for efficient on-device LLM generative personalization](https://arxiv.org/abs/2609.24979)

**<font color=#1a73e8>作者：</font>** Sean Augenstein, Li Ding, Jihwan Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device large language models (`LLMs'), e.g. running on mobile phones, are ripe for improvement via personalization. The limited compute resources of mobile devices impose limits on model scale and thus model quality, making any realizable quality gains highly impactful. At the same time, their personal nature (i.e., the close coupling to a particular user) means that a given on-device LLM tends to be used in similar, predictable patterns over the course of time. This paper presents a novel method for personalizing on-device LLMs. It trains a hypernetwork to map a user's context tokens to a low-rank adaptation (`LoRA') well-suited to that user. Once the trained common artifacts are deployed to users' devices, each user uses the hypernetwork to synthesize (entirely on device) a personalized LoRA. This approach blends the benefits while avoiding the drawbacks of two existing approaches to LLM customization: in-context learning (`ICL') and parameter-efficient fine-tuning (`PEFT'). Like ICL (and unlike PEFT), the on-device phase of our approach is computationally feasible, requiring only forward passes through neural networks. Like PEFT (and unlike ICL), our approach modifies the `target' base LLM via weights (the LoRA), avoiding negative consequences (e.g. increased latency) associated with extending the input sequence. Our approach is particularly well-suited to the mobile device regime. Apart from the on-device compute and latency benefits mentioned, it also requires minimal additional storage, as internally its architecture partly leverages the same LLM weights as belong to the target LLM to be personalized. We demonstrate the benefits of LoRA-generating hypernetworks on several representative personalization datasets, comparing against baselines like ICL and PEFT. Of note, our personalization experiments focus on more challenging and less studied long-form text generation tasks.

---


### 357. [onPanda: Efficient Annotation of On-Policy Alignment Data for LLMs and Agents via Token-Level Correction](https://arxiv.org/abs/2609.24983)

**<font color=#1a73e8>作者：</font>** Lei Yang, Mengyin Liu, Jia Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present onPanda, an interactive tool for efficiently annotating LLM alignment data and agent trajectories. onPanda adopts token-level correction as its core interaction: while reading a model response, the annotator locates the first inappropriate token and either picks a substitute from the model's candidate tokens or types the correct text via free-form editing. The system then truncates everything after that position and continues generation from the corrected prefix, repeating this locate-correct-continue loop until a satisfactory response is obtained. This mechanism lets annotators precisely steer model outputs at low cost: a small controlled study suggests that onPanda reduces median annotation time by 52% over manual post-editing. Since the vast majority of tokens in the final response are generated by the model itself, the resulting data largely preserves the model's sampling distribution and is well suited for constructing on-policy SFT and preference data. Furthermore, the token-level corrections recorded during annotation provide fine-grained supervision with precise positions and naturally paired positive--negative samples. onPanda also connects to external tools and harnesses, enabling interactive trajectory annotation in realistic environments. In addition, we release Panda-CVL, a dataset annotated with onPanda, together with a benchmark for token-level correction.

---


### 358. [Who Does What in AI Auditing? Designing Human-AI Collaboration for Auditing Generative AI](https://arxiv.org/abs/2609.24986)

**<font color=#1a73e8>作者：</font>** Eunkyu Park, Markelle Roesti, Wesley Hanwen Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI auditing increasingly incorporates AI agents to expand the scale and breadth of audit coverage, yet little is known about how auditing work should be divided without displacing human judgment. We introduce Human-Agent Audit Collaboration (HAAC), a workflow and system for structuring human-AI collaboration in AI auditing. Drawing on prior work and formative consultations with AI auditing practitioners, HAAC specifies how agents can support exploration, assessment, reporting, and review while preserving human oversight where contextual judgment is critical. We instantiate HAAC for conversational shopping agents and evaluate it through two studies. With 71 auditors, AI assistance increased attack success and broadened exploration, while also shaping later attacks and increasing auditors' reliance on AI-generated assessments and reports. Interviews with Responsible AI practitioners showed that actionable audits require visibility into coverage, reproducible attack trajectories, and evaluation of the auditing agents themselves. Our findings identify design considerations for effective and accountable human-AI auditing.

---


### 359. [VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997)

**<font color=#1a73e8>作者：</font>** Binxu Li, Haoyi Duan, Yuhui Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video generative models have enabled high-fidelity, temporally coherent video generation. However, these models often struggle to satisfy prompts requiring specialized knowledge, specific identities, physical consistency, or ordered events. In this paper, we present VideoGen-Agent, a multimodal agent trained through multitask agentic reinforcement learning to use external tools for video generation. The agent coordinates augmentation, generation, and verification tools through multi-turn interactions, using the prompt and intermediate observations to guide its decisions. We train a shared policy on a category-balanced dataset spanning six tasks. Supervised fine-tuning on teacher-generated trajectories establishes tool-use behavior, which is then refined through reinforcement learning. A category-aware hybrid reward evaluates tool-call validity, task-appropriate tool use, and generated video quality. We further introduce VABench, a held-out benchmark of 600 prompts covering procedural knowledge, single- and multi-entity identity preservation, physical consistency, scene composition, and multi-shot temporal structure. On VABench, VideoGen-Agent improves over its base text-to-video generator by 19.1 points, from 56.5 to 75.6. Upgrading the generation tools further raises the score to 86.1 without additional agent training. Human raters prefer the upgraded configuration over the strongest standalone baseline in 84.3% of comparisons. These results support learning tool use across video-generation tasks and show that the trained agent can benefit from subsequent advances in generation tools.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 360. [Summarize, Judge, Refine: Decoupled Content Understanding and Policy Learning for Multimodal Content Moderation](https://arxiv.org/abs/2609.22094)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zeeshan Ahmed, Yang Qin, Hanqing Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Content moderation systems traditionally entangle multimodal understanding with policy-specific classification, requiring full pipeline retraining for every policy change and suffering from label scarcity since multimedia cannot be meaningfully augmented. We propose Summarize-Judge-Refine (SJR), a two-model architecture that decouples these concerns via a natural language interface: a multimodal Content Model produces structured text summaries, and a text-only Policy Model classifies them against policy definitions. An iterative co-training loop refines the Content Model via GRPO to produce policy-relevant summaries, while text-space augmentation generates adversarial summary variants---an augmentation pathway impossible on raw multimedia---enabling few-shot policy bootstrap. Every decision is grounded in a human-readable summary, providing interpretability as a structural byproduct. On misleading advertisement detection, SJR achieves +23.6\% relative non-misleading F1 over a zero-shot chain-of-thought baseline, outperforming end-to-end SFT, STaR/RFT, and RLFT. Notably, a variant trained on zero real violating examples---with all positive-class data synthetically generated---matches the full-data model within 0.2\% relative on violating F1, demonstrating that new policies can launch without any real violation data.

---


### 361. [Generalized Multimodal Foundation Model](https://arxiv.org/abs/2609.22107)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Huizi Cui, Zongbo Han, Chenggong Ding 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Making prediction with multimodal data is widely used in diverse scenarios. Existing multimodal fusion models, once deployed, can only handle predefined modalities (e.g., vision, text and audio) and single tasks, making it difficult to quickly adapt to new downstream applications. Therefore, a natural yet rather aggressive question arises, whether there exists a general multimodal fusion model that can be applied to arbitrary modality combinations and arbitrary prediction tasks. We argue that a unified multimodal fusion model should not depend on specific modalities and instead encode transferable patterns of multimodal correlation. To this end, we propose a simple and effective learning paradigm based on training over the generation of large-scale synthetic multimodal datasets with diverse causal structures that formally characterize the generative processes of multimodal data in real world. Building on this framework, we propose the generalized multimodal foundation model, a unified foundation model for generalized multimodal learning. By constructing large-scale synthetic multimodal datasets with diverse correlation patterns, our model encodes transferable multimodal correlations during training and activates appropriate associations through in-context examples during inference. Extensive experiments on 18 real-world datasets spanning 12 modalities and 11 prediction tasks demonstrate that our model achieves competitive performance with specialized models without task-specific adaptation.

---


### 362. [A Comparative Framework for Evaluating Foundation Models on Tabular Data: A Case Study in Healthcare](https://arxiv.org/abs/2609.22154)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Majid Lotfian Delouee, Sjors G. J. G. In 't Veld, Martijn C. Schut  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data is the most common format in clinical practice, encompassing laboratory results, medication records, diagnostic codes, and patient demographics. As foundation models for tabular data have grown in number and variety, a practical question has become harder to answer: which model should a clinician or data scientist actually choose for a given task, and why? Existing surveys catalogue what these models can do, but they stop short of providing a structured way to compare them against the specific demands of a real application. We introduce \system{}, a comparative evaluation framework that scores and ranks tabular foundation models (TFMs) across six clinically meaningful dimensions: how well a model generalizes to new datasets, how effectively it protects patient privacy, how much data it needs to perform well, how it scales with growing datasets and feature spaces, how interpretable its predictions are to clinicians, and how fairly it performs across patient subgroups. Each dimension is broken down into measurable sub-components, and groups of sub-components can optionally be combined into supplementary compound scores, called super-metrics, that provide a diagnostic view of how a model performs across several dimensions simultaneously. To show how the framework works in practice, we apply it to two healthcare use cases, screening for iron deficiency and predicting heart failure, demonstrating how the same set of metrics leads to different model rankings depending on what matters most in each clinical context. We also provide a taxonomy of 45 TFMs organized by their underlying architecture, which serves as a reference for researchers and practitioners looking to navigate this rapidly expanding field.

---


### 363. [CHART: A Harness-Rotation Curriculum for Harness-Robust Search Agents](https://arxiv.org/abs/2609.22247)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xinlu Zhang, Ying-Chun Lin, Zhihan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Search agents are usually trained under a single harness. But once an agent is deployed in a real application, its harness is frequently updated (e.g., a rewritten system prompt) to fit production needs. This exposes a fragility of post-trained agents: because a learned behavior is entangled with its training harness, even a harness update that leaves the task unchanged can fail to elicit the behavior. We train a search agent to perform parallel search, a popular strategy for improving both search efficiency and performance. We find that training under a fixed harness makes the behavior harness-local, overfit to that harness's surface form: when the harness changes, the model falls back to serial search. An intuitive fix is harness augmentation, but simply training on more harnesses does not resolve the problem. GRPO learns from the reward gap between parallel and serial rollouts of the same question: a small harness pool saturates that gap early, while a large pool dilutes the per-harness signal too thinly for any harness to consolidate. We therefore propose Curriculum HArness Rotation Training (CHART), a rotating curriculum that lets a search agent gradually consolidate parallel search across harnesses. At each periodic evaluation, CHART "graduates" the harnesses whose expected behavior is learned and replaces them with still-learnable ones, keeping the reward gap alive throughout training. Starting from the same harness pool, CHART makes the model learn parallel search on all harnesses, whereas static augmentation succeeds on at most half of them. The behavior also carries to held-out harnesses: CHART parallelizes on 89% of held-out turns, against at most 5% for the static pools. It further transfers to a new QA task and search environment, improving pass@1 by 5.6pp over the best static pool. Finally, CHART-trained agents benefit more from meta-harness search than baselines.

---


### 364. [The Ups and Downs of Backprop Weights](https://arxiv.org/abs/2609.22554)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Giuseppe Chindemi, Benjamin F. Grewe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Backpropagation (BP) has driven the remarkable success of modern deep learning by enabling large hierarchical networks to learn complex functions end-to-end. Yet it does not by itself determine how parameters should be organized so that functional components can be reused and adapted selectively. For example, object recognition and motion prediction may depend on overlapping parameter sets, making them difficult to isolate or modify independently. We call this condition weight entanglement. Modern architectures dynamically select which parts of a network process each sample: nonlinearities gate units, attention selects interactions, and Mixture-of-Experts architectures route inputs to modules. Yet such selection does not ensure that the same functional component remains linked to an identifiable parameter set across samples. We propose weight operators: parameterized modules that implement reusable functional components and can be composed at inference to form the function required by each sample. Learning proceeds in two stages: the model first infers the required operator composition, then updates only the selected operators' parameter sets. Vector Networks (VNs) provide one implementation. They couple operator selection to local error-driven updates within each layer and show that learned operators can be reused in combinations absent from training while updates remain restricted to the selected parameter sets. This provides a basis for testing functional parameter identifiability: whether an operator remains linked to the same functional component during learning. We argue that functional parameter identifiability may provide an organizing principle for models that systematically reuse and recombine learned functions while adapting only the components that need to change.

---


### 365. [Combining Foundation Model Confidence and Monocular Depth for Training-Free Out-of-Distribution Segmentation](https://arxiv.org/abs/2609.22896)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Serin Varghese, Fabian Hüger, Kira Maag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles operating in open-world scenarios are inevitably confronted with previously unknown objects, such as exotic animals or loose cargo. The reliable detection and segmentation of these out-of-distribution (OOD) objects is therefore crucial for a safe understanding of the environment and decision-making. Most existing approaches require access to OOD training samples, retraining of the segmentation backbone, or dedicated auxiliary architectures, limiting their practical applicability. We propose a training-free method that derives dense OOD scores directly from the confidence predictions of a foundation segmentation model, without any task-specific fine-tuning or access to anomalous data. To improve the robustness of our OOD segmentation, geometric information from monocular depth estimation is incorporated into the decision process, providing complementary cues to uncertainty-based predictions. We evaluate the proposed method on the SegmentMeIfYouCan benchmark and additionally assess its performance on OOD tracking in video sequences, reflecting the temporal nature of real-world perception systems. The method performs strongly on road-centered benchmarks.

---


### 366. [Ask for Any Appliance: A Prompt-Programmable Foundation Model for Non-Intrusive Load Monitoring](https://arxiv.org/abs/2609.23146)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xudong Wang, Jiacheng Cui, Junyu Xue 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-intrusive load monitoring (NILM) estimates appliance-level consumption from a whole-home meter, but appliance-specific models and fixed output inventories make coverage costly to extend. We present FM4NILM (Foundation Model for NILM), a single prompt-programmable model that estimates a requested appliance's power trajectory from aggregate measurements, a natural-language description, and optional activation exemplars. A lightweight cadence-aware transformer is pretrained by masked reconstruction on 645k sequences from seven public corpora spanning 1-60 s sampling intervals, then aligned with appliance requests using observation-masked losses for partially labeled households. A Bernoulli-lognormal decoder separates activity detection from conditional power estimation. On held-out households and time periods from REDD, UK-DALE, and REFIT, one frozen text-prompted model serves twelve appliance-corpus requests, achieving 0.556 event F1, 0.625 AUPRC, and the lowest active-window MAE (251.8 W) among seven appliance-specific baselines. Streaming score aggregation raises event F1 to 0.582 with a 60 s aggregation delay. In a separate category-held-out evaluation, adding ten activation exemplars raises microwave AUPRC from 0.132 to 0.214 without parameter updates. Input-intervention ablations probe the model's dependence on appliance requests and aggregate measurements. These results demonstrate competitive disaggregation with one shared model and support extending appliance coverage through prompts and examples rather than additional specialist networks.

---


### 367. [Rethinking Class Imbalance for Single-Cell Foundation Models: A Systematic Benchmark Across Architectures and Long-Tail Loss Functions](https://arxiv.org/abs/2609.23325)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zeyu Dong, Jiahui Zhong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-cell foundation models (scGPT, scBERT, Geneformer) achieve cell-type classification accuracy up to 97.5% in our experiments, yet this aggregate accuracy can mask systematic failure on rare, often disease-relevant cell populations that long-tail loss functions are widely assumed to address. We present a systematic benchmark of six long-tail loss functions (cross-entropy, weighted CE, class-balanced loss, focal loss, LDAM, logit-adjusted softmax) across three architectures and three datasets (Multiple Sclerosis, Zheng68K, human Pancreas), totaling 162 controlled training runs (3 backbones x 3 datasets x 6 losses x 3 seeds). The gap between overall accuracy, Macro-F1, and rare-class recall under plain cross-entropy is consistent across all nine (architecture, dataset) settings, driven by dataset structure rather than pretraining. Rare-class failure itself splits into two regimes with distinct embedding-geometry signatures, visible before any loss is chosen: some classes are recoverable by the right loss, while others retain linear separability yet are absorbed into unrelated classes' neighborhoods under every evaluated loss and architecture. Among the recoverable classes, the efficacy of reweighting is predicted by a class's absolute training-set size, rather than its share of the dataset or the dataset's overall imbalance ratio. Class-balanced loss and LDAM are the most consistent choices across all nine settings, while logit adjustment trades rare-class precision for recall rather than improving both. Our results give both a reusable benchmark and mechanism-grounded practical guidelines for combining foundation models with imbalanced biological data.

---


### 368. [RSPDBench: Benchmarking Vision Foundation Models on Earth Observation Tasks Under Physically Grounded Remote-Sensing Product Degradations](https://arxiv.org/abs/2609.23427)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Tanjim Bin Faruk, Khondaker Masfiq Reza, Shrideep Pallickara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models targeting Earth observation (EO) tasks are commonly evaluated on clean downstream benchmarks, but operational EO products can already contain spatial, radiometric, alignment, noise, and harmonization defects before reaching the model. Existing robustness evaluations often use generic image corruptions or broad domain shifts, which do not isolate these product-level failure modes. We introduce \textbf{RSPDBench}, a physically grounded \textbf{r}emote-\textbf{s}ensing-\textbf{p}roduct \textbf{d}egradation \textbf{b}enchmark for vision foundation models. RSPDBench evaluates five EO datasets, seven foundation-model entries, and two supervised baselines under audited primitive degradations and compound product chains. Each model is evaluated under its clean-selected native protocol, with robustness measured as the drop from its own clean baseline. Our analysis reveals that degradation sensitivity is strongly structured: resolution-conditioned and channel-grouped encoders protect different failure axes, and the same physical defect can hurt one model while helping another. Compound chains expose failures that isolated degradations do not predict, with model-dependent amplification, saturation, or component dominance, and excess drops up to $38$ percentage points beyond the strongest component. These results show that EO robustness cannot be characterized by clean accuracy or generic perturbation tests alone; it must also be measured against the structured defects that remote-sensing products carry into deployment.

---


### 369. [Towards robust multimodal 3D object detection via visual foundation models](https://arxiv.org/abs/2609.23541)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ziying Song, Lin Liu, Hongyu Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal 3D object detection is fundamental to robust perception in autonomous driving because it integrates complementary information from LiDAR and camera sensors. However, existing methods often fail to maintain robustness under out-of-distribution (OOD) corruptions caused by sensor noise, adverse weather, and environmental changes. To address this problem, we propose RoboDistill, a robust and generalizable multimodal 3D object detection framework that leverages visual foundation models (VFMs), such as the Segment Anything Model (SAM). First, we introduce SAM-AD, a domain-specific pretraining strategy that fine-tunes SAM on autonomous-driving imagery to extract feature representations with rich semantic information. Second, we design the AD Feature Pyramid Network (AD-FPN) to refine and upsample SAM features at multiple scales for seamless fusion with LiDAR features. Third, we develop the Depth-Guided Wavelet Attention (DGWA) module, which suppresses high-frequency sensor noise while preserving critical contextual information. Finally, we introduce KD Fusion, in which the pretrained SAM-AD serves as a teacher that distills high-quality visual knowledge into a lightweight point-cloud network, thereby improving robustness under noisy conditions. Extensive experiments across 27 challenging OOD corruption settings show that RoboDistill generally delivers stronger or competitive detection performance and robustness relative to representative state-of-the-art methods. This work bridges the gap between VFMs and 3D object detection and advances robust multimodal perception for real-world autonomous-driving applications.

---


### 370. [Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery](https://arxiv.org/abs/2609.23924)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kevin Zhou, Sparsh Roy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pretrained EEG foundation models are increasingly proposed as general-purpose encoders for brain-computer interfaces, yet recent benchmarks disagree about when their representations transfer to downstream tasks. We audit LaBraM and CBraMod on motor imagery under a validation-locked protocol in which preprocessing, architecture, optimization, freeze depth, checkpoint, temperature, and method selection are determined using training-session data only. On four-class BCI Competition IV-2a, every supervised comparator evaluated here outperforms every foundation-model configuration, including validation-selected fine-tuning. We then examine a key confound: foundation models and task-specific decoders are normally evaluated using different input pipelines. Retraining three supervised architectures on the broadband arrays consumed by the foundation models produces matched-input accuracy differences of opposite sign across architectures: broadband input improves ATCNet by 0.078 accuracy while reducing EEG Conformer accuracy by 0.088. None of the three individual matched-input terms is significant after multiple-comparison correction at n = 9, so we treat the sign variation descriptively rather than as a formal architecture-by-pipeline interaction. These observed sign differences suggest that a single comparator may not provide an architecture-invariant decomposition of a pretrained-versus-supervised performance gap. The four-class deficit also does not reproduce uniformly across motor-imagery datasets: on two-class BNCI2014-004 we cannot detect the same separation between fine-tuned CBraMod and the supervised comparators. Finally, validation-fitted temperature scaling returns foundation-model calibration error to the supervised range despite substantially lower four-class accuracy.

---


### 371. [LEAP-NBV: Lightweight Edge Active-Perception for Foundation-Model Next-Best-View Planning](https://arxiv.org/abs/2609.23974)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Boxun Hu, Jiawei Ge, Axel Krieger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models are endowing autonomous systems with greater intelligence, enabling a more comprehensive understanding of the environment through visual perception. A representative example is Human Mesh Recovery (HMR), which provides useful estimates of a target's 3D pose and shape that can benefit tactical missions. However, the size and power demands of such models make them difficult to run on edge platforms and limit their real-time performance, undermining the requirements of tactical edge deployment - especially for active perception, where a mobile robot must plan its next-best view on-board and cannot offload computation under contested communications. We present LEAP-NBV, a lightweight active-perception framework that runs foundation-model-driven Next-Best-View (NBV) planning on-board an edge device. To this end, we distill a family of large HMR teachers, each into a compact 32M student, with an offline mesh objective, then quantize the vision encoder to FP16 and characterize its on-device accuracy and latency. Within an occlusion-aware active perception loop, we evaluate all configurations on the same held-out benchmark and deploy the end-to-end pipeline on an NVIDIA Jetson Xavier NX, reporting measured on-device latency and energy. Distillation recovers 6-7 mm of Procrustes-aligned mean per-vertex position error (PA-MPVPE) over the undistilled student on the test set. Selecting the edge-optimal compression model brings the HMR engine to ~12 ms at a small accuracy cost and runs the full closed loop at 3.6 FPS and 2.6 J per frame, achieving a 2.0x speedup and 3.0x lower energy than the uncompressed model while nearly matching downstream task quality.

---


### 372. [Evaluating the Generalization of Neuroimaging Foundation Models on African Brain MRI](https://arxiv.org/abs/2609.23983)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Oluwatobi Iyanuoluwa Akinmuleya, Olatokun Shamsudeen Akano, Samuel Danquah Ankapong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neuroimaging foundation models pretrained on large, predominantly western cohorts are increasingly proposed as general-purpose backbones for brain MRI analysis. Yet, their ability to generalize to underrepresented clinical populations remains largely untested. We evaluate four recent foundation models (BrainIAC, Neuro-JEPA, NeuroVFM, and Primus) on a three-way diagnostic classification task (Control, Dementia, Parkinson's disease) using a cohort of 88 subjects from a Nigerian clinical brain MRI dataset, across four modality configurations (T1w, T2w, T1w+T2w, FLAIR), and compare against an end-to-end trained ViT3D baseline. The frozen backbones collapse to majority-class predictions, while Neuro-JEPA on FLAIR shows modest but still limited discrimination. In contrast, the end-to-end trained ViT3D achieves higher accuracy and MCC on every task (up to 53.4% accuracy, MCC=0.27) and is the only model with non-trivial recall. Our findings suggest that these frozen neuroimaging foundation models are insufficient for fine-grained diagnostic classification in small, non-western clinical cohorts, motivating parameter-efficient adaptation and broader multi-site external validation for equitable deployment in global health settings.

---


### 373. [ACLArena: Agent Continue Learning in Multi-stage Post-training](https://arxiv.org/abs/2609.23989)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haixin Wang, Xiaoxuan Wang, Junkai Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building general-purpose agents for industrial deployment requires integrating multiple capabilities, each typically acquired at a distinct stage of training. Yet there is currently no well-established recipe for Agent Continual Learning (ACL), with little understanding of the trade-offs among existing integration paradigms. To address this gap, we introduce ACLArena, a framework for comprehensively studying, analyzing, and evaluating ACL. We first build a sequential training pipeline and conduct an in-depth analysis that explains the mechanisms of forgetting and generalization from two complementary perspectives, the model level and the token level. Guided by these analyses, we systematically compare multi-teacher on-policy distillation, self-distilled fine-tuning, and model merging to assess their ability to recover previously learned capabilities while preserving newly acquired ones. Through extensive experiments, we develop a detailed understanding of how capabilities transfer across stages. Finally, we propose a new ACL recipe that combines offline replay over high-quality trajectories with a routed network of multiple LoRA experts each specialized via RL, substantially improving the agent's ability to learn across multiple domains. Comprehensive experiments on four reasoning and agentic tasks, evaluated under both in-domain and out-of-domain settings, demonstrate the value of our analysis and the effectiveness of our approach.

---


### 374. [Efficient Reasoning Exploration via State-Conditioned Latent Steering with Progress Guidance](https://arxiv.org/abs/2609.24066)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Hengyuan Zhang, Chenming Shang, Zunhai Su 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Best-of-$N$ is a widely used inference strategy for complex reasoning, whose effectiveness depends on whether sampled candidates can cover diverse and high-quality reasoning paths. However, post-trained reasoning models often suffer from \emph{exploration collapse}, where independent rollouts repeatedly follow similar reasoning paths and limit the gains from increasing the rollout budget. Existing methods alleviate this issue by promoting broader exploration, but do not explicitly guide exploration toward continuations that make meaningful progress, resulting in limited exploration efficiency. To address this, we propose \emph{\underline{S}tate-conditioned \underline{P}rogress-guided \underline{S}teering} (SPS), a training-free latent steering framework. Specifically, SPS constructs a state-conditioned Direction Bank containing multiple progress-guided steering vectors for different prefix-state regions. During online inference, SPS retrieves a suitable steering vector based on the current prefix state and applies it at high-uncertainty transitions to guide the next reasoning step toward meaningful progress. Extensive experiments across multiple model scales and benchmarks demonstrate that SPS consistently outperforms strong baselines. Further analyses validate the effectiveness of its key designs and offer valuable insights for future research. The code is available at this https URL.

---


### 375. [MECAIL: Communication-Aware Incremental Learning for Object Detection with 14.6 KB Spatiotemporal Experts](https://arxiv.org/abs/2609.24455)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Matthias Neuwirth-Trapp, Maarten Bieshaar, Danda Paudel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intelligent transportation systems require Incremental Learning (IL) to continually improve their overall performance in dynamic environments. However, most edge devices lack the computational resources to support on-device IL, requiring updates to be transmitted from centralized servers. We propose using this setup to obtain dense, specialized module coverage that adapts a fixed base model to specific spatiotemporal contexts, such as parking lots, gas stations, ferries, or construction sites. However, in order to reliably transmit these modules to the edge device, using TCP, UDP, and BTP over V2X, Wi-Fi, and 2G-5G hardware, we establish a strict limit of 14.6 KB per module to fit within the first TCP window and to minimize UDP/BTP fragmentation. We further introduce Mixture-of-Experts for Communication-Aware Incremental Learning (MECAIL), the first method that meets this strict requirement, in which each new domain or environment is served by a small expert network that adapts the base model. We validate MECAIL on D-RICO and ODinW-13, where it largely matches the performance of parameter-heavy approaches while enabling practical, bandwidth-efficient large-scale deployment. This allows comprehensive coverage by experts for highly specific, focused, and temporary situations.

---


### 376. [Beyond Predictable Paths: Redefining AI Security Incident Reporting for Agents](https://arxiv.org/abs/2609.24515)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Anastasia Pustozerova, Eugene Bagdasarian, Luca Beurer-Kellner 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents are being deployed rapidly, accompanied by a growing number of AI-specific attacks and corresponding incidents. As incident reporting becomes increasingly important for legal compliance, governance, accountability, and security; current frameworks must be adapted to the unique characteristics of AI agents. In this paper, two editorial authors compare AI systems and AI agents and, drawing on input from 23 experts in academia and industry, identify the information required for reporting incidents where the security of AI agents is harmed. %involving AI agents. Potential reporting elements include, for example, agent memory and memory accesses, actual and potential levels of autonomy, and tool usage. Based on these findings, we identify several open research questions, including how to efficiently record incidents and how to determine whether vulnerabilities and incidents generalize. Expert feedback also highlighted potential reporting weaknesses, such as risks of data leakage and attacks targeting the reporting infrastructure itself, creating additional research needs. Lastly, we summarize privacy requirements and outline research directions for the secure and trustworthy deployment of AI agents.

---


### 377. [$t_0$: A Time-Series Foundation Model for Forecasting with Context](https://arxiv.org/abs/2609.24559)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lucas Meyer, Claudio Sole, Huikan Xiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present $t_0$, a family of open-weights foundation models for forecasting with multivariate context. We release its first two members: $\texttt{t0-alpha}$ and $\texttt{t0-beta}$, respectively 102M and 256M parameters. Both condition their forecasts on target history, past covariates, and known-future covariates, without task-specific retraining. Their transformer layers alternate attention along time and across variates. They produce probabilistic forecasts through quantile predictions. Pretraining combines curated public data with synthetic generator families constructed to contain covariate-to-target dependencies. On GIFT-Eval, $\texttt{t0-alpha}$ reaches an aggregate CRPS of 0.4941, and $\texttt{t0-beta}$ a CRPS of 0.4738 and a MASE of 0.6865, third on both and within 4.0% of the best zero-shot TSFM. On fev-bench they score 42.2 and 46.7 in skill, the latter third again and 2.0 points behind the leader. We analyze $\texttt{t0-alpha}$ in depth. Known-future covariates raise its skill by 6.3 percentage points across 30 tasks. The report also examines its calibration, its rollout strategy on long horizons, and its robustness to missing data. On the Victoria electricity-demand benchmark, $\texttt{t0-beta}$ is among the most accurate models with a context of nearly a year. In an independent Macrocosm evaluation of hourly ERCOT prices over 29 months, both cut the MAE of the lagged-price baseline by 38%.

---


### 378. [Toward a foundation model for forest point clouds](https://arxiv.org/abs/2609.24787)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuanwen Yue, Stefano Puliti, Damien Robert 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forest inventories increasingly rely on artificial intelligence (AI) models to derive forest attributes from large-scale 3D point clouds. Current models are typically specialized to a single task, sensor, and forest type, making adaptation expensive in terms of annotations, computation, and expertise. We ask whether a single pretrained model can instead learn transferable representations across diverse forest inventory settings. Inspired by recent developments in language modelling and computer vision, we take a step toward a foundation model (FM) for 3D forestry. Using LitePT as backbone, we first establish a strong supervised baseline that sets a new state of the art on forest semantic and instance segmentation, tree species classification, and age regression benchmarks. We then curate a large-scale unlabelled corpus spanning airborne, UAV, and mobile laser scanning across diverse forest ecosystems, and pretrain the same backbone using self-supervised learning. We systematically evaluate representation learning strategies by comparing training from scratch, supervised pretraining, and self-supervised pretraining across four representative forestry tasks, under varying annotation budgets. Compared with training from scratch, self-supervised pretraining accelerates model convergence and consistently improves performance when annotations are scarce. Compared with task-specific supervised pretraining, self-supervised pretraining yields more transferable representations across downstream forestry tasks. These findings identify the practical regime in which pretrained representations are most valuable and suggest that instance discrimination, rather than forest semantics, is the main remaining obstacle to a general-purpose 3D forest foundation model. Code and models are available at: this https URL.

---


### 379. [MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution](https://arxiv.org/abs/2609.24838)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Junde Wu, Jiayuan Zhu, Minghao Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical agents increasingly combine general reasoning models with specialized clinical tools, yet their capabilities remain largely fixed by what clinicians and engineers design before deployment. Recursive self-improvement (RSI) offers a different paradigm in which agents learn from their own failures and autonomously expand their capabilities, but directly applying RSI to medicine introduces fundamental safety challenges. We introduce MedRSI, the first recursive self-improvement framework for medicine, which continuously transforms diagnostic failures into new clinical capabilities through tool composition and task-specific model training. Inspired by clinical practice, MedRSI introduces two mechanisms for clinically aligned self-evolution. Clinical-cost-aware failure prioritization directs improvement toward errors according to their potential clinical consequences rather than frequency alone. Fast discovery with slow registration separates rapid capability invention from conservative adoption, allowing new tools to enter the persistent agent only after demonstrating sustained benefit across subsequent patient cohorts. Across public glaucoma and heart disease benchmarks and two private clinical tasks, MedRSI progressively develops segmentation, measurement, prediction, multimodal reasoning, and generative capabilities, surpasses manually engineered medical agents, and autonomously discovers solutions to clinical problems not anticipated by its original designers. Our results show that medical agents need not remain constrained by capabilities specified before deployment: with clinically grounded mechanisms governing what to improve and what to retain, they can continuously construct, validate, and accumulate new capabilities from diagnostic experience. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**351-379**（第 8/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-379**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
