# 🧠 大模型相关研究 | 2026年11月25日

> 本类共 **486** 篇论文：已确认 **458** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

---

### 201. [Neural Agent Compiler: Learning to Schedule Soft Dependencies](https://arxiv.org/abs/2611.29262)

**<font color=#1a73e8>作者：</font>** Bo Yan, Peng Wang, Zihan Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents accomplish complex tasks by coordinating multiple reasoning steps and tool operations, which form dependencies among their operations. Existing orchestration methods primarily consider hard dependencies that determine when an operation can legally begin, but overlook soft dependencies, i.e., information that is not required for execution but may improve an already executable operation. We identify soft-dependency scheduling as an important problem in agent execution. To this end, we introduce Neural Agent Compiler (NAC), a learned scheduler that predicts the task-quality and resource consequences of three execution modes and selects the highest-utility legal mode at a scheduling boundary. NAC represents the executable continuation, pending information event, and resource state in a shared memory, and uses a utility function to adapt the consequence predictions to different resource preferences. Across AppWorld, WebShop, and $\tau^2$-bench, NAC achieves 276/417 AppWorld task completions, a 74.69 WebShop Task Score, and 59/100 $\tau^2$-bench successes. Additional studies show that the learned scheduler reduces execution work, establishing soft-dependency scheduling as a promising solution for orchestrating tool-using agents.

---


### 202. [On the Interplay between Backtracking and Latent Confidence Directions in Reasoning Models](https://arxiv.org/abs/2611.29265)

**<font color=#1a73e8>作者：</font>** Stephen Cheng, Zahra Sodagar, Sandeep Soni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models deliberate over multiple answer proposals, often resulting in excessively long traces due to backtracking, even when the correct answer has already been reached (Across three 32B models, ~87% of rollouts contain 1 unique answer yet still make ~8 answer proposals on average). Given this potentially "decorative" chain of thought (CoT) reasoning, can we look to the model internals to determine if the model will backtrack or commit to an answer proposal? Operating under the hypothesis that models maintain an internal representation of their uncertainty, we seek to extract this representation and characterize its relationship with backtracking behavior at answer proposals. By querying the model's verbalized confidence following answer proposals throughout a response trace, we extract a linear direction for latent confidence that separates high and low verbalized confidence. This direction can steer verbalized confidence as expected, but it surprisingly can also steer the next token probability of backtracking, performing on par with a linear direction extracted directly from backtracking examples. We then test the direction under progressively more realistic interventions. Steering continuously from a mid-trace answer proposal modulates response length (~-1.3k - ~+2.5k tokens) and the number of answer proposals (-4.18 - +4.75) in both directions, with minimal cost to accuracy. Applying the confidence direction from the start of generation, where proposal positions are unknown, still shortens traces at comparable accuracy, and its effect surfaces in the linguistic confidence of proposals. Overall, our study reveals the intricate interplay between a model's internal confidence and its proclivity to backtrack or commit to an answer.

---


### 203. [MetaSkill: Reusable Problem-Solving Methods for Adaptive Skill Orchestration in LLM Agents](https://arxiv.org/abs/2611.29274)

**<font color=#1a73e8>作者：</font>** Tianxing Wang, Mingming Zhao, Shuai Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reusable skills provide specialized procedures, but large language model (LLM) agents must still determine how to organize and adapt their use. We introduce MetaSkill, a two-layer framework for reusing problem-solving methods across tasks and domains. The method layer selects from 26 curated methods and binds abstract roles to task objects. The execution layer uses the instantiated method to identify intermediate objectives, coordinate native skills, and guide repair or method reselection. On 89 SkillsBench tasks and 995 ToolHop examples, MetaSkill outperforms the evaluated baselines in all six configurations, with accuracy gains of 3.51-13.48% over the strongest baseline. Ablations support explicit method-guided orchestration beyond direct method injection and further gains from method reselection.

---


### 204. [QASparse: Query-Adaptive Sparse Attention with Tailored Budgets and Tokens](https://arxiv.org/abs/2611.29280)

**<font color=#1a73e8>作者：</font>** Zhiyuan Chen, Zihao Yang, Quanjiang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-sequence inference in large language models is constrained by the high cost of prefilling, where dense attention scales quadratically with context length. Exploiting similarity across attention heads offers a way to reduce redundant computation. Prior approaches in this direction have relied on localized query observations to determine head-level computation reuse or budget allocation. However, inter-head similarity does not imply uniform query requirements, leaving adaptation to varying budget needs and selection preferences across query regions a key challenge. We introduce QASparse, a Query-Adaptive Sparse attention mechanism with hardware-efficient execution. QASparse preserves the efficiency of shared cross-head importance estimation while adapting computational budgets and token selections to query requirements, and it executes these dynamic sparse decisions through dedicated kernels. Its query adaptivity stems from two complementary innovations: Local Budget Regression models local variations in computational demand along query positions to estimate budgets for different query regions and attention heads; Boundary Voting lets queries within each head vote over candidates near the selection cutoff using actual query/key scores, refining the retained set while preserving the initial selection size. To reduce the execution overhead of dynamic budgets, we further design length-specialized selection kernels that efficiently support query-adaptive sparse patterns across context lengths. Together, these designs efficiently combine shared estimation with local decisions while adapting both how much attention is computed and which interactions are retained. Experimental results demonstrate improved benchmark scores and faster prefill attention computation compared with existing sparse attention baselines.

---


### 205. [LLM-Based Assistant for Dog Care Guidance](https://arxiv.org/abs/2611.29286)

**<font color=#1a73e8>作者：</font>** Abubakar Sadiq Shittu, Venkat Gopu, Arshita Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study investigates whether domain grounding through Retrieval-Augmented Generation (RAG) and parameter-efficient fine-tuning using Low-Rank Adaptation (LoRA) can enhance the accuracy and reliability of pet care advice generated by large language models (LLMs). We curated a dataset of breed-specific dog care information and used it to develop two systems: a RAG pipeline based on TinyLlama-1.1B-Chat-v1.0, and a fine-tuned LLaMA-3.2-1B model adapted using LoRA. Both systems were evaluated on 15 dog care questions. The RAG model achieved a perfect average score of 2.0, outperforming the fine-tuned model (mean = 1.47). Statistical analyses, including Welch's t-test, Mann-Whitney U, and Wilcoxon signed-rank tests (all p < 0.05), confirmed the significance of the performance gap. Our findings suggest that retrieval-based domain grounding leads to more accurate, consistent, and trustworthy responses than standalone fine-tuning in specialized LLM applications.

---


### 206. [Beyond Omission: Measuring Critical-Information Fulfillment of Large Language Models in Bengali and English](https://arxiv.org/abs/2611.29299)

**<font color=#1a73e8>作者：</font>** Avijit Roy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluations of multilingual trustworthiness often ask whether a model leaves out information that a user needs. We examine whether that question is sufficient. Using 157 matched tasks written in English (EN), natural Bengali (BN) and Bengali-matrix Bengali-English code-switching (BN-CS), we scored 1,413 responses from three models (GPT-6.1 Sol, Qwen3.5-9B and Gemma 4 12B) against required information units (RIUs) fixed before any model was run. The scoring separates outright omission from content that is present but incorrect, insufficient or only partly met. The prespecified primary estimand, the domain-equal paired difference in critical omission rate (BN - EN), showed no detectable difference (+0.003, 95% CI -0.014 to +0.015), with omission near zero in every condition. The Bengali deficit appeared in fulfillment instead. Critical coverage was 0.050 lower in Bengali (95% CI 0.022 to 0.079) and strict complete-task success 0.093 lower (95% CI 0.055 to 0.131); both gaps came from the two open-weight models, and Sol showed none. Code-switching recovered part of the loss in RIU coverage (+0.028, 95% CI 0.012 to 0.045). On these data, an omission count alone would have shown no language gap. The automated judge passed prespecified agreement gates after a documented failed first attempt. A blind native-speaker rating of 60 study responses agreed with it on RIU scores (alpha 0.84) and critical RIUs (98% exact) but fell short on Bengali RIU agreement (alpha 0.77) and on the unsupported-content check (93% exact), and a blind check of its reason codes agreed on whether a critical unit was omitted for 79 of 81 units. Data, rubrics, responses, scores and code are released.

---


### 207. [AscendFHE: Efficient Fully Homomorphic Encryption on Ascend NPUs](https://arxiv.org/abs/2611.29301)

**<font color=#1a73e8>作者：</font>** Honghui You, Haoping Yang, Wenzhe Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption enables cloud servers to run neural networks on encrypted inputs. In CKKS, inference requires costly arithmetic on high-degree polynomials. On Ascend neural processing units, preparing operands and reconstructing intermediate results add to this cost, while limited local memory constrains parallel execution. We present AscendFHE, a CKKS backend that coordinates Ascend's matrix engines and vector cores for bootstrapping and encrypted inference. It uses balanced-byte encoding and exact modular reconstruction to reduce vector work and packs intermediate results in the next operator's input format to avoid redundant transfers. Its two-task pipeline reuses shared buffers after their last read to overlap matrix and vector execution within the local memory budget. On Ascend 910B3, AscendFHE achieves a 4.61$\times$ bootstrapping speedup and 1.59$\times$--2.00$\times$ encrypted-inference speedups across ResNet-20, BERT-base, and Llama 3 8B over our Vector-based Ascend port of Cheddar.

---


### 208. [From Vanishing Gradients to Recursive Self-Improvement: Evaluating the Most Influential Papers in Large Language Model Evolution (1997-2026)](https://arxiv.org/abs/2611.29303)

**<font color=#1a73e8>作者：</font>** Saadh Jawwadh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Large Language Model (LLM) research makes it increasingly difficult to distinguish incremental refinements from true paradigm shifts. This review evaluates 22 of the most influential publications spanning nearly three decades (1997-2026), organized through a causal, chronologically anchored taxonomy centered on the author's birth year (1999). Beginning "before 1999" with how recurrent neural networks (RNNs) forgot earlier context (much like forgetting Chapter 1 by the time a reader reaches Chapter 9), we trace how Long Short-Term Memory (LSTM) networks introduced a "bouncer" mechanism of forget, input, and output gates to selectively preserve long-term memory. We then examine how Word2Vec turned language into vector mathematics (king - male + female ~ queen), why sequential RNNs hit a parallelization wall, and how the Transformer's all-to-all attention weights launched the modern LLM era alongside a quadratic bottleneck. Next, we analyze why scaling parameters alone leaves capacity under-trained unless data scales equally (Chinchilla), how Reinforcement Learning from Human Feedback (RLHF) left alignment superficial, and how that gap compounded into adversarial jailbreaks and single-direction refusal subspaces (J-space), where instructing a model not to think of a restricted concept surfaces it much like the human "red ball" paradox. Finally, we synthesize the current state of AI (2024-2026), encompassing recursive model collapse, autonomous reasoning-model jailbreak agents, machine-speed agentic intrusions, and closed-loop recursive self-improvement (AIDE^2).

---


### 209. [CT-Navigator: Towards Interpretable and Generalizable CT Understanding through Agentic Perception and Tool-Invocation](https://arxiv.org/abs/2611.29305)

**<font color=#1a73e8>作者：</font>** Yibing Fu, Huidong Xie, Yihao Niu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical computed tomography (CT) interpretation inherently requires progressive visual exploration, where radiologists navigate from whole scans to individual slices and regions of interest and interact with external tools when necessary. However, existing 3D medical multimodal large language models (MLLMs) typically connect a specialized 3D visual encoder to a language model, without fully leveraging the native 2D visual and agentic capabilities of generalist MLLMs. Trained on large-scale one-hop CT instruction-following data, these models also have limited ability to perform iterative reasoning and explicitly ground their conclusions in visual evidence, limiting their support for traceable CT interpretation. To solve these problems, we propose \textbf{agentic perception} as an alternative paradigm inspired by radiologists' interpretation workflows. We introduce \textbf{CT-Navigator}, a framework that harnesses generalist MLLMs' 2D visual and agentic capabilities to progressively ground CT interpretation in explicit, traceable visual evidence through hierarchical visual exploration and radiology tool invocation. To build these capabilities, we curate 8,904 visual chain-of-thought (V-CoT) trajectories for cold-start agentic supervised fine-tuning. We then optimize the policy through reinforcement learning on 33,219 questions, with data selection and dynamic rollout sampling prioritizing informative learning signals. Finally, we introduce CTNavi-Bench, a 3D CT visual question answering benchmark comprising 7,000 questions spanning anatomical regions throughout the human body. CT-Navigator achieves 79.50\% accuracy on CTNavi-Bench, surpassing the strongest baseline by 17.59\%, and demonstrates strong generalization across three external CT benchmarks. The code, model, and benchmark will be released on \href{this https URL}{GitHub}.

---


### 210. [Counting Symbols on Technical Drawings: A Benchmark and Verified Rewards for MLLMs](https://arxiv.org/abs/2611.29309)

**<font color=#1a73e8>作者：</font>** Junxian Li, Ruixuan Yang, Zhenhua Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Today's MLLMs can count objects in natural images. However, when asking them how many bolt holes appear in a mechanical drawing or how many nitrogen atoms are in a chemical structure, they often struggle. Counting in technical drawings remains challenging, as objects can be small, densely packed, or even implied by drawing conventions. To study this problem, we introduce CountDrawBench, a benchmark including floor plans, electrical schematics, mechanical drawings, and molecular structures, with 1,574 counting questions and instance-level annotations where available. Besides evaluation, we introduce Code-Verified RL, a reinforcement learning framework that teaches MLLMs to count with executable feedback. Our method combines three complementary rewards: a count reward that checks the final answer, an instance-matching reward that verifies object locations, and a zoom-based reward that checks counting consistency across local image regions. All three are integrated into a unified GRPO objective. Extensive experiments reveal that even leading MLLMs struggle on CountDrawBench, with the best evaluated model achieving only 59.3% accuracy. Our method improves Qwen3.5-9B from 49.3% to 54.3% accuracy, outperforming all evaluated open-source baselines. These results establish CountDrawBench as a challenging testbed for technical drawing understanding and demonstrate the value of code-verified rewards in these tasks. Code and data will be released upon acceptance.

---


### 211. [FP-Prune: Rethinking Visual Token Pruning from an Information Gain Perspective](https://arxiv.org/abs/2611.29327)

**<font color=#1a73e8>作者：</font>** Haozhe Zhao, Junxiang Zhang, Junxin Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning can reduce the inference cost of vision language models, but its effectiveness depends on preserving complementary visual information under a limited token budget. A central challenge is to quantify the additional information a candidate token contributes beyond the retained set, a contribution that conventional scores based on attention or similarity struggle to capture directly. In this work, we revisit visual token pruning from the perspective of information gain and use mutual information to characterize the incremental value of candidate tokens. We further establish theoretically that frame potential serves as an effective surrogate for mutual information. Building on this observation, we propose FP-Prune, a training-free visual token pruning method that iteratively removes tokens with low information gain to preserve as much complementary visual information as possible. Experiments on three widely used VLMs and eight datasets demonstrate that FP-Prune outperforms baseline methods in both accuracy and inference efficiency. Further analysis shows that the surrogate objective closely aligns with model performance. Our work provides theoretical grounding and an effective method for visual token pruning.

---


### 212. [EMIP: Embodied Multi-Party Interaction Platform](https://arxiv.org/abs/2611.29333)

**<font color=#1a73e8>作者：</font>** Koichiro Terao, Rikunari Sagara, Moe Nagao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Experimental platforms that enable multiple participants to engage in spoken dialogue and perform physical actions concurrently in a shared environment are important for studying cooperation between humans and embodied AI agents. In this paper, we propose EMIP (Embodied Multi-Party Interaction Platform), a virtual environment platform built on Minecraft. Through an Internet-based client-server architecture, EMIP connects multiple humans and multiple AI agents to the same virtual environment and supports full-duplex speech communication and simultaneous physical interaction. It provides interfaces based on the Model Context Protocol (MCP) for environmental observation, physical action execution, and audio input and output, enabling researchers to develop their own agent control methods using large language models (LLMs). Additional features include centralized control of an agent group through a single EMIP agent client, collaborative object transportation by multiple agents, and experimental support functions such as recording and retrieving observation histories. By integrating these features into a reusable platform, EMIP aims to support research on human-human, human-agent, and agent-agent cooperation under different participant configurations and agent control methods. Usage examples illustrate concurrent speech and physical action, task coordination, and overlapping speech. The source code for the platform is publicly available on GitHub (this https URL).

---


### 213. [Probe Before You Learn: Allocating Prompts from Initial Gradients under Label Noise](https://arxiv.org/abs/2611.29336)

**<font color=#1a73e8>作者：</font>** Jiazhe Zhang, Zibin Geng, Qiang Ma 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt learning provides a parameter-efficient way to adapt pretrained vision--language models through text and visual prompts, but noisy labels prevalent in real-world data inevitably bias prompt updates and thereby undermine adaptation effectiveness. Prior work on robust prompt learning focuses on suppressing unreliable updates under noisy supervision. We uncover a pivotal yet overlooked aspect--prompt allocation: shifting the parameter budget between text and visual prompts can substantially enhance robustness while keeping the training objective and total budget fixed. However, suitable prompt allocations vary across tasks and are unknown a priori, rendering brute-force candidate training computationally prohibitive. We propose GPrompt, a training-free method that derives allocation between text and visual prompts using only loss gradients at initialization before prompt optimization. Using a small sample of images and generated pseudo-labels as shared supervision, GPrompt performs an initialization probe to extract paired text and visual loss gradients, and characterizes the geometry of their trace-normalized Gram matrices through both concentration within each modality and overlap between modalities. GPrompt then derives a closed-form allocation, and projects it onto feasible prompt counts under the exact parameter budget, enabling task-specific selection without training candidate configurations. Experiments across eleven datasets show that GPrompt outperforms the strongest baseline by up to 7.75% while selecting configurations close to the best allocation identified through exhaustive training. The average runtime of gradient probe across datasets is 99.9% lower than that of exhaustive candidate training.

---


### 214. [DeciForm: Incorporating Task Structure into Decision Models](https://arxiv.org/abs/2611.29340)

**<font color=#1a73e8>作者：</font>** Qiuyu Tian, Haojie Yin, Yingce Xia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decision models unify candidate selection, Boolean judgment, and numerical scoring within a single model. Their answer spaces nevertheless carry different structures: classification candidates form an unordered set, while numerical scores have an intrinsic order and distance. We introduce Deciform, which incorporates these distinctions into computation and supervision. Candidate-free queries and isolated candidate branches support consistent classification under reordering. A log--spherical objective trains candidate probabilities, while a decimal-prefix readout combines individual-value and interval-weighted cumulative supervision for numerical scoring. Shared adapters, task-private residuals, and output-channel gains support joint adaptation. On a shared 15,000-request test set, Deciform improves all three decision metrics on Qwen and ModernBERT; source-normalized errors support the Score gains across the data mixture. Canonicalized joint encoding also eliminates tested order flips, while isolation further improves prediction metrics. Separate objective studies and main-configuration ablations examine the classification and numerical components. After one epoch of MIND-small adaptation, Deciform improves multi-positive news ranking on both backbones. These results support matching encoding and supervision to answer-space structure within a unified decision interface.

---


### 215. [Endpoint-Conditioned Process Value: What an Endpoint-Blind Process Score Adds Once Terminal Status and Cost Are Known](https://arxiv.org/abs/2611.29354)

**<font color=#1a73e8>作者：</font>** Chris D Yan, Ken Wang, MarkX Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Trajectory metrics promise information beyond final-answer accuracy, but no one has measured what a process score adds once an evaluation knows the outcome and the cost. We build that comparison: a sealed consequence needing an artifact neither agent nor judge ever sees, an operational baseline of terminal status and cost, and judge scale and evidence access as experimental factors. On 1,255 trajectories over 158 test-generation tasks in 7 Python repositories, the answer is gated on the judge. Four judges from 4B to 14B, one reasoning before scoring, add nothing an interval separates from zero; a Qwen3 32B judge on identical trajectories adds +0.050 AUC (95% CI [+0.020, +0.081]) and survives a refitting bootstrap ([+0.013, +0.095]). Most of what it adds is recoverable from eight behavioural counters, so a harness should log them (the judge adds +0.020 beyond them). What the judge is shown moves it further: disclosing the terminal verdict inflates its standalone discrimination by +0.103, while reference disclosure and tool-output redaction move it by nothing an interval separates from zero. A process metric reported without the judge's scale and evidence access does not identify a quantity. We release the protocol, the sealed-endpoint harness, and all trajectories.

---


### 216. [Polytropos: What Do Vision-Language Model Descriptions Make of a Cultural Object?](https://arxiv.org/abs/2611.29355)

**<font color=#1a73e8>作者：</font>** Yuechen Jiang, Enze Zhang, Yuyan Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models have become a new kind of describer, writing about almost anything people see, and their descriptions now shape how cultures are known by people and by other models. Descriptions of cultures tend to turn particular things into types, and what a description loses shows what its describer lacks. We introduce Polytropos, a benchmark that measures what model descriptions of cultural objects keep of the particular object by turning each description back into an image and comparing it with the original photograph. On 374 objects from the Metropolitan Museum of Art and the Getty, with 1,870 descriptions from five models and 230 written by curators, reconstructions are recognised as the recorded culture more often than the photographs, at 54.55% to 59.09% against 52.14%, yet 16% to 21% of objects change outcome and only 0.49% of reconstructions are identified as the specific object. On the same objects, models lose recorded cultures at a rate similar to curators but gain more. Model descriptions give each object many faces, each typical of its culture and almost none the object itself.

---


### 217. [Automatic Construction of Persian E-Commerce Dialogue Datasets for Conversational Product Search](https://arxiv.org/abs/2611.29356)

**<font color=#1a73e8>作者：</font>** Fariba Nafar, Hassan Naderi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational product search lets users find products through a multi-turn dialogue instead of a single keyword query, but Persian lacks the large conversational datasets needed to train and evaluate such systems; existing Persian e-commerce dialogue resources cover few categories and small catalogs. We present a framework that builds such a dataset automatically from a real e-commerce catalog and release the resulting dataset. The framework crawls 12,926 products in seven categories of the Digikala marketplace, groups them into 170 semantically coherent clusters, and selects the question the assistant asks at every turn with the Regularized Partition Balance (RPB) score. The RPB score accounts for feature coverage, the probability that the user can answer and the number of values, and generalizes entropy-based question selection. An LLM then verbalizes each question plan into a natural Persian dialogue. In a simulation on the full catalog, the RPB score needs 0.11 fewer turns than the strongest entropy baseline when the difficulty of answering differs between features, and is practically equivalent to it when it does not. Using only a free LLM API, we generated 1,000 requirement-driven dialogues covering all 170 clusters, with turn-level feature annotations; automatic checks and an LLM judge confirm their consistency with the catalog, while their realism is lower than that of the first, GPT-4o-generated version. Code and data are publicly available.

---


### 218. [Beyond Attention Maps: Understanding and Improving Medical MLLMs via Visual Values](https://arxiv.org/abs/2611.29361)

**<font color=#1a73e8>作者：</font>** Yichen Zhao, Fenghe Tang, Wenxin Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current MLLM methods largely focus on whether models attend to the right visual regions, implicitly treating spatial attention map as the primary key of effective visual perception. To examine this assumption, we introduce a medical VQA dataset with paired non-contrast (NC) and contrast-enhanced (CE) images that share corresponding anatomy while providing different cues. We show that this view is incomplete: across paired NC and CE medical images, MLLMs often exhibit similar attention patterns despite producing contrasting answers, while controlled bidirectional interventions induce substantially larger prediction changes on visual values than attention weights. These results identify the visual content retrieved through values as a critical factor in improving perception beyond spatial attention alone. Guided by this finding, we propose VIVID (VIsual Value Intervention Distillation), which uses enhanced visual values to identify and refine teacher corrections aligned with useful visual evidence to improve on-policy distillation from CE to NC images. Across six internal and external test sets, VIVID consistently outperforms existing on-policy distillation methods across different model scales and architectures, requires only NC images at inference, and maintains strong zero-shot performance on general-domain VQA benchmarks. The project page is available at this https URL.

---


### 219. [BenchMint: From Real-World Tasks to Executable Benchmarks](https://arxiv.org/abs/2611.29367)

**<font color=#1a73e8>作者：</font>** Zining Huang, Zuo Wang, Mengyao Zhang 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) need evaluations of everyday reasoning and tool use, such as planning itineraries under user constraints and grounding numerical answers in evidence. We introduce BenchMint, an automated benchmark-construction workflow, and Daily-Life, its collection of 100 selected tasks across 11 real-world domains. BenchMint jointly constructs tasks and scoring criteria from the same source documents. Language-model judges assess possible answers against these criteria using tool traces and private evidence. We report 26 model/harness configurations, including GPT, Claude and Gemini families; 17 have complete domain profiles. These are descriptive configuration results, not a controlled model ranking. In one selected travel task, we corrected the reference total from 320 to 380 minutes while keeping both answers unchanged. The incorrect answer's arithmetic verdict switched from pass to fail; the correct answer's switched from fail to pass. With one ballot per cell, this exposes a reference error without establishing repeatability or collection-wide validity. Incomplete construction comparisons establish no general advantage of joint authoring or feedback-guided revision.

---


### 220. [SAE-Audit: Clinical-Trial Prediction via Inference-Time Optimization of Black-Box LLMs Audited by Sparse Autoencoder Evidence](https://arxiv.org/abs/2611.29368)

**<font color=#1a73e8>作者：</font>** Junbo Shen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical trials are costly and often take years to complete, making early outcome prediction valuable for trial planning. Large language models (LLMs) are increasingly used to forecast clinical-trial outcomes, yet their predictions remain unreliable and their rationales may not faithfully reflect the evidence underlying their answers. On tasks such as predicting whether a registered clinical trial will complete or terminate early, frontier LLMs perform only modestly above chance in our experiments. We introduce SAE-Audit, which optimizes a black-box LLM at inference time with evidence obtained from a deployable open model. A frozen sparse autoencoder (SAE) on Llama-3.1-8B-Instruct is converted into a vocabulary of clinical concepts. Sparse probes fitted on past trials determine which concepts are associated with the outcome. For a new protocol, the concepts detected by the probe are written as evidence, each with the direction and strength of its association with the outcome, and the LLM being audited optimizes its answer in the light of this evidence. Without additional training, SAE-Audit raises balanced accuracy of deepseek-v4-flash by 9.6--12.0 points on five clinical-trial prediction tasks and raises GPT-5.6-terra by 8.0 points on trial completion, exceeding other agentic inference-time optimization methods by a large margin. As an auxiliary, SAE probes module within SAE-Audit is itself accurate and auditable, providing natural-language explanations directly derived from verified concept contributions and protocol evidence, without requiring additional LLMs at inference time. SAE-Audit provides verifiable, concept-level evidence for more accurate and auditable clinical-trial prediction. It can also be embedded into biomedical AI agents such as Biomni to optimize their performance.

---


### 221. [Emotion-Aware and Context-Grounded Dialogue Agents for Personalized Video Game Interactions](https://arxiv.org/abs/2611.29372)

**<font color=#1a73e8>作者：</font>** Michael Adjeisah, Jin Zhang, Pierluigi Vito Amadori 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present ChatNPC, a game companion that dynamically personalizes its responses in real time based on players' emotional shifts to enhance user immersion. The model integrates sequential data, leveraging the dynamic nature of streams to benefit from player information, spoken lines, and in-game context. We leverage recent progress in LLMs' tool-calling capabilities to extract vital information from memory and recognize potential constraints for accurate reasoning, thereby tackling the complexity of NPC conversation scenarios. The task is divided into a game sentinel-guided agent (SeGent), a memory capability, and a chat planning tool for reasoning instantiation. The approach uses a lightweight game template as an information framework, with relevant details and a thorough reasoning layout. We conduct extensive experiments on a newly developed game dataset for in-game context NPC dialogue and demonstrate that ChatNPC sequentially captures players' emotional shifts over time; responses are more naturalistic and human-like with appropriate conversational cues, pauses, and sighs; and utterances remain faithful to the dynamics of in-game context and player actions, supporting narrative continuity.

---


### 222. [Can Speech LLMs Recognize When Audio Evidence Is Insufficient? A Diagnostic Study and a Pre-Generation Probing Mitigation](https://arxiv.org/abs/2611.29393)

**<font color=#1a73e8>作者：</font>** Vladislav Nesterenko, Polina Doronicheva, Olga Golubeva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech large language models are usually evaluated on questions that have answers. We ask what they do when a recording establishes none, and whether the standard way of finding out is sound. Diagnosed on synthesized speech the answer looks clear: Qwen2-Audio fabricates an answer to 92.5% of unanswerable questions, while an ASR cascade reading the same recordings reaches 2.5% hallucination at 6.7% over-refusal, placing the failure in reasoning rather than in perception. The identical protocol on 376 native SQuAD 2.0 questions over human-read recordings removes that conclusion: the cascade hallucinates on 67.7% against the end-to-end model's 69.8%, at a higher over-refusal cost. A paired subset asking the same questions of a synthesized and a human recording of each passage localises the effect in the ASR stage -- the end-to-end model's abstention behaviour does not move with the speaker, the cascade's goes from 11.1% to 65.9%. Reliance on synthesized speech has been named as a limitation of audio benchmarks but not quantified; we quantify it, and show it large enough to reverse a finding. Since no prompt we tested repairs the residual failure, we transfer pre-generation attention probing to the multimodal setting. A probe over frozen prompt representations reaches 0.773 AUROC at predicting which unanswerable questions the model will answer anyway, where semantic entropy over ten sampled generations is at chance: the model fabricates the same answer every time, so sample disagreement cannot see a failure it is confident about.

---


### 223. [BQDNA: Multi-Head Binary Spherical Quantization for Genomic Sequence Modeling](https://arxiv.org/abs/2611.29395)

**<font color=#1a73e8>作者：</font>** Xudong Wang, Siwei Cheng, Haozhe Hu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding biological information from long, repetitive DNA remains challenging. Genomic language models (gLMs) often follow the conventional language-model pretrain-and-adapt paradigm. However, the lack of inherent semantic segmentation and prior rules makes hand-crafted tokenizers like k-mer and BPE suboptimal. We introduce context-aware \textbf{BQVAE} for scalar quantization of DNA and \textbf{BQDNA}, an autoregressive gLM supporting multi-head codebooks. Comprehensive experiments reveal that: (1) unique training dynamics of vector quantization in DNA space, including the importance of alignment between training corpus and downstream data. (2) superior performance of BQVAE over hand-crafted tokenizers and vanilla VQVAE. (3) remarkable cross-species generalization capability of BQDNA, which achieves state-of-the-art performance with merely 0.1B multi-species training for BQVAE and 1 epoch training on hg38 for BQDNA, outperforming gLMs pretrained with 10$\sim$100x more tokens. Our findings underscore the potential of learned vector quantization for genomic sequence representation. Code is available at this https URL

---


### 224. [HGDNA: Overlapping k-mer Tokenization for Efficient Autoregressive Genomic Language Models](https://arxiv.org/abs/2611.29400)

**<font color=#1a73e8>作者：</font>** Xudong Wang, Siwei Cheng, Haozhe Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The domain of genomic language models (gLMs) has advanced rapidly, with models pretrained on diverse multi-species genomic corpora demonstrating their remarkable capabilities. While the effect of simple nucleotide-level tokenization on long-context modeling is well established, overlapping k-mer tokenization remains underexplored in causal pretraining, despite its rich neighborhood information. Here, we thoroughly revisit overlapping tokenization and introduce HGDNA, a hybrid linear-attention gLM with causal language modeling (CLM) pretraining and a shared token-prediction interface for downstream adaptation, using a species-classification auxiliary task and shared class tokens. HGDNA delivers competitive performance across sequence classification and frozen-embedding evaluations, supporting both short-range and long-range tasks with 30M parameters and 19B pretraining tokens. Code is available at this https URL

---


### 225. [VistaTree: Question Answering over Long Multimodal Documents with Image-Derived Summary Trees](https://arxiv.org/abs/2611.29419)

**<font color=#1a73e8>作者：</font>** Yexiang Cheng, Xiaochen Zheng, David Tokar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answering questions over long multimodal documents requires locating relevant evidence across pages containing text, tables, and figures. When the document exceeds the model's context window, selective retrieval becomes necessary. We introduce VistaTree, a document question-answering agent that builds a summary tree directly from rendered page images. VistaTree segments documents into contiguous page spans, recursively groups them into a topic hierarchy, and refines sibling summaries to distinguish neighboring sections. At query time, the agent uses node summaries to select relevant nodes and reads the corresponding pages, using hierarchical navigation when the full outline exceeds the context budget. Experiments on MMLongBench-Doc and LongDocURL evaluate answer quality and retrieval cost using a locally hosted vision-language model, and quantify the performance gap between global and hierarchical access to the index.

---


### 226. [A colour-marker tracker for pose estimation of slender surgical instruments: vision-language-model-guided adaptive colour calibration](https://arxiv.org/abs/2611.29421)

**<font color=#1a73e8>作者：</font>** Jaesung Hong, Dong Won Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Slender surgical instruments need small, narrow markers for camera-based pose estimation. A colour-stripe marker fits this requirement, but its colours in the image drift from the design values with lighting, printing and camera settings. Because the colours can only be corrected after the marker has been found, methods that rely on the design colours face a circular problem. We propose vision-language-model (VLM)-based adaptive colour calibration and compare it with two rule-based methods, which re-measure the colours from detections made with the design colours: Initial colour update does so once after tracking starts, and Colour adaptation continuously during tracking. VLM guidance uses a fine-tuned VLM to find the markers without relying on the design colours and builds the colour profile from their pixels. Recall/F1 (%) for Initial colour update, Colour adaptation and VLM guidance were 92.0/95.7, 87.8/93.3 and 98.2/99.1 on 672 synthetic image pairs; 51.3/67.2, 48.8/65.0 and 83.8/87.0 on eight degraded laboratory videos; and 38.9/55.2, 19.7/29.7 and 100/100 on a surgical-robot (da Vinci) video with strongly shifted colours. In that video the rule-based methods never found the purple/cyan marker, whereas VLM guidance found all 234 markers with no false positives. In a simulation, the hue boundary between the two stripes moved by less than 0.1 pixel for exposure gains of 0.5-2.0, compared with 2.9-4.0 pixels for a boundary found with a fixed brightness threshold. When the degradation is mild, the rule-based methods, which need no training and no GPU, are sufficient. When the colours change greatly, the gain comes from a VLM-guided candidate search that does not rely on the design colours. Combining colour-stripe markers with adaptive colour calibration enables tracking of slender surgical instruments with small markers.

---


### 227. [RumiFold: Teaching an LLM to Natively Fold Proteins and Reason About Their Function](https://arxiv.org/abs/2611.29444)

**<font color=#1a73e8>作者：</font>** Kevin Lu, David Bau, Wengong Jin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can we teach a general-purpose language model to fold proteins? And if so, what does learning to fold enable beyond structure prediction itself? We introduce RumiFold, a pretrained chat model that learns to predict protein structures directly from its own hidden states. RumiFold processes proteins through repeated folding passes, then uses these folded representations to answer questions in natural language. It achieves folding accuracy comparable to dedicated single-representation models such as SimpleFold, alongside state-of-the-art performance on Gene Ontology protein function prediction and free-text function description. We find that folding pretraining organizes the model's hidden states around protein function, creating an internal per-residue workspace that is biologically grounded. Causal interventions show that this folded workspace links structure and language when RumiFold predicts function, providing rich representations for biomolecular reasoning. We see RumiFold as a step toward native biomolecular intelligence: where protein-based computations and language-based reasoning become integrated capabilities of general-purpose language models. Code, data, and models are available at: this https URL

---


### 228. [Detectable Epistemic Attack Layers: A Coverage Theorem and Standardized Harness for Conversation-History Integrity](https://arxiv.org/abs/2611.29449)

**<font color=#1a73e8>作者：</font>** Fahrell Giovanny, Geby Bayuningtyas, Sahrul Mukharom  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversation history is infrastructure: deployed language models rely on application layers to store and reinject prior turns, and that stored state is writable. We formalize session-level contamination by attack layer, state a coverage theorem, and measure its scope: each deployment-layer verification tier covers exactly its layer and is sound with respect to the others; instruction overrides are not detectable without false positives; and composite vectors evade per-fragment verification. A standardized harness applied to eight mechanism families across 3,249 sessions and three model families makes these claims checkable. First, pattern-based detection pays a measured false-positive price: the classic defenses flag 35 to 50 percent of benign sessions, and the naive refusal floor reaches only 2.4 percent attack-cell adoption while destroying 33 to 100 percent of benign turns, whereas provenance-gated channel separation achieves adoption at or below 1.2 percent with zero false positives and zero utility loss. Second, in the exploratory instruction-override extension, the gates' boundary is a cliff: directives rephrased without shape markers bypass them at control-equivalent rates, 47.7 to 49.5 percent against 0.0 percent for the shaped class, placing that class in the model-internal lane. Third, the deterministic core is storage-layer detection at 126 of 126 per model with zero false positives. External anchors reproduce published attack pressure, with PoisonedRAG falling from 70 to 0 percent under the full stack. For practitioners: authenticate stored history and content provenance with deterministic tiers, scope instruction-layer mitigation to provenance-gated designs whose measured benign cost is zero, and monitor composition at the trajectory level rather than per fragment. All protocols and acceptance criteria are pre-registered; the stack and harness are released.

---


### 229. [PAWP-TTS: Phoneme-Aware Weight Programming for Compact Bilingual English-Nepali Speech Synthesis](https://arxiv.org/abs/2611.29455)

**<font color=#1a73e8>作者：</font>** Firoj Paudel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents PAWP-TTS, a compact non-autoregressive text-to-speech system for English, Nepali, and English-Nepali code-mixed speech at 24 kHz, with no language model at inference. Deterministic pronunciation knowledge lives in a rule- and lexicon-based bilingual frontend that preserves native Nepali contrasts and avoids Hindi phonology, so the network only models acoustics. Counting every learned inference tensor, including the waveform decoder, PAWP-1.5M (1,490,390 parameters, 5.98 MB) reaches 1.50% English and 1.75% Nepali character error rate under a single ASR recognizer, and 5.04% / 4.02% Nepali / English phoneme error rate (PER) on 600 untouched test utterances. Decoder-centric 281K-parameter models (1.1 MB) stay intelligible across three independent seeds, with equal-budget dense models (5.53 +/- 0.08% NE, 5.34 +/- 0.28% EN PER) outperforming K=2 cross-layer shared-basis models (6.35 +/- 0.11% NE, 6.57 +/- 0.47% EN PER). Fixing a frontend/label version mismatch nearly halved Nepali PER, more than any architectural or weight-level change. The paper then studies weight-space programming: inspection-guided, zero-training weight edits. Under strict controls (validation-only selection, one-shot test, paired bootstrap, matched random and same-parameter gradient baselines), edits show real selectivity (27:1 on word-boundary pauses with 96 weights; zero cross-lingual collateral inside language-gated residuals) but no accuracy gain beyond controls. Two apparent targets proved to be label or phonology artifacts. Code, ONNX graphs, and CC BY 4.0 weights are released.

---


### 230. [Fill in the Blanks: Non-Autoregressive Schema-Parallel Key Information Extraction with CTC Decoding](https://arxiv.org/abs/2611.29460)

**<font color=#1a73e8>作者：</font>** Shaked Perek, Avihu Dekel, Ben Wiesel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) extract structured data from documents by generating the requested JSON one token at a time, so their sequential steps grow with the length of the answer. Yet in key information extraction (KIE) the schema already fixes the answer's structure: keys, nesting and lists are known before decoding, and only the values are unknown. We exploit this with a non-autoregressive extractor that writes the structure from the schema, sizes every list with a count pass, and predicts all values in parallel, in a fixed number of passes that does not grow with the document. Each value is decoded with connectionist temporal classification (CTC) in its own block of slots, so its length never has to be predicted, and a value that is still open after its block gets a larger token budget. Zero-shot on VAREX, CORD and FUNSD, our 4B extractor is 3.5$\times$ faster than the diffusion-VLM competition on average (up to 5.6$\times$) and more accurate, with 4--6 forward passes per document where block diffusion needs 12--74. The same extractor also drafts for speculative decoding with its own autoregressive base: it runs 8.3$\times$ faster than autoregressive decoding (up to 10.4$\times$) within 0.4 points of its accuracy, and 3.3$\times$ faster than speculative diffusion decoding while 13.0 points more accurate. We release the model and code.

---


### 231. [Beyond Accuracy: A Diagnostic Benchmark for Hypothesis-Driven Experiment Planning in LLM Agents](https://arxiv.org/abs/2611.29467)

**<font color=#1a73e8>作者：</font>** Ryo Kuroki, Amin Mansouri, Philippe Schwaller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating large language model (LLM) agents on scientific tasks typically reduces to final-task accuracy, which obscures where reasoning succeeds or breaks down. We introduce a benchmark and diagnostic evaluation framework for hypothesis-driven adaptive experimental planning in closed-world system identification, instantiated in kinetic mechanism identification. The framework goes beyond final accuracy in two ways. First, we evaluate exploration behavior by quantifying the extent to which agents exhibit space-filling or corner-seeking patterns in the experimental design space. Second, we decompose the reasoning process into four interpretable steps: belief update, hypothesis discrimination, discriminative experiment design, and predictive reasoning under interventions, each scored separately on reasoning traces. Across ten LLM agents, we find that stronger agents outperform both adaptive (Bayesian optimization) and non-adaptive (Latin hypercube) baselines and exhibit exploration patterns inconsistent with naive heuristics. Decomposing reasoning reveals that the stronger agents score consistently well across all four steps, whereas weaker agents often succeed at belief update and hypothesis discrimination but are less reliable at translating them into actionable designs and sharp contrastive predictions. Independent expert annotations support predictive reasoning under our stated validation criteria, while evidence for discriminative experiment design is positive but less consistent. The results suggest a gap between recognizing plausible hypotheses and translating them into contrastive predictions, with more tentative evidence for a corresponding experiment-design bottleneck. The benchmark website is available at this https URL.

---


### 232. [GraphSeer: Multimodal Knowledge Graph Relational Image Retrieval with MLLMs](https://arxiv.org/abs/2611.29470)

**<font color=#1a73e8>作者：</font>** Linyu Li, Zhi Jin, Yuanpeng He 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal knowledge graphs (MMKGs) store entities with photos and names and link them by facts. MMKG methods predict links between known entity IDs, and image retrievers, from CLIP to MLLM embedders, return entities that look like a query photo or match its description. Neither answers a common question about a new photo: which graph entity is related to the one shown, such as the team of a pictured player or the city of a landmark. We call this knowledge graph relational image retrieval (KRIR): given a photo and a natural-language relation, retrieve the related MMKG entity, which rarely resembles the photo, whether the depicted entity is in the graph (known) or not (unseen). We build three benchmarks from YAGO, Wikidata and in-the-wild OVEN photos. The task hides two hops: recognising which graph entity is shown, and recalling what it is connected to. GraphSeer bridges them inside one multimodal LLM: it links the photo to the graph, reads the facts of the best match, and retrieves with the hidden state at which the model is about to say the answer. An unseen entity has no facts of its own, but every candidate answer does, so a listwise verifier reads the other end of the graph: it re-ranks the top candidates by their facts and photos in one forward pass, and the facts matter far more than the photos. With Qwen3.5-27B, GraphSeer improves MRR on known entities by 24.2-70.0% over an MLLM embedder fine-tuned on the same data with the same budget. When it also fuses and verifies the embedder's candidates, it improves MRR on unseen entities by 12.5-25.6%, and on known entities it beats KG-completion models given the ground-truth entity ID.

---


### 233. [Separating Action Allocation from Image Matching in Visual Token Routing](https://arxiv.org/abs/2611.29477)

**<font color=#1a73e8>作者：</font>** Chenxi Wang, Bin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adaptive visual token routers aim to save computation while preserving the image detail needed to answer each question. A higher average score could reflect better choices for individual images or more frequent use of high resolution on tasks that need it. We distinguish the two by keeping action counts fixed within each task and comparing the router's assignments with random pairings of the same actions and images. On equally weighted ChartQA and TextVQA, both Qwen2.5-VL-3B and -7B gain from matching but lose more from their action frequencies relative to a task table, with a 1.71-point gain and a 3.95-point loss on 7B. Exchanging the continuous resolutions chosen by the external selector CARES also lowers quality on 7B. When requests arrive with task labels, the table outscores the discrete router by 1.92 points and saves 31.76 ms per complete 7B request on average.

---


### 234. [CAR: Reducing Decoder Output Shift in Visual Token Pruning via Coverage Selection and Attention Reallocation](https://arxiv.org/abs/2611.29489)

**<font color=#1a73e8>作者：</font>** Xixi Jiang, Pingcheng Dong, Chen Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning is an effective way to accelerate multimodal large language models (MLLMs). However, existing methods degrade substantially under aggressive pruning, especially on visual grounding (VG). We analyze the sources of this degradation from the perspective of the output shift that pruning causes in decoder layers, and decompose this shift in closed form into two terms, an image summary error and an attention allocation error. The summary error stems from the loss of visual information, and the allocation error from the drop in the share of attention assigned to visual tokens. To reduce both errors, we propose CAR (Coverage selection and Attention Reallocation), a token pruning framework that restores attention share while maintaining information. Specifically, to minimize the summary error, whose upper bound tightens as the retained tokens better cover all visual tokens, our coverage selection retains tokens that are both salient and non-redundant, with saliency from encoder heads chosen by a label-free probe. To minimize the allocation error, our attention reallocation reassigns the attention of the discarded tokens to the retained ones through a closed-form logit bias. On Qwen2.5-VL-7B with $90\%$ of the visual tokens pruned, CAR retains $93.0\%$ of the unpruned accuracy on visual question answering (VQA) and $77.9\%$ on VG, against $26.5\%$ for the best existing method on VG; the logit bias alone raises the VG accuracy of existing methods by up to $24$ points. Experiments on multiple MLLMs across VQA, VG and video understanding show that CAR generalizes well and consistently outperforms existing methods.

---


### 235. [Recursive Self-Editing: LLMs Program Their Own Weight Edits for Self-Improvement](https://arxiv.org/abs/2611.29513)

**<font color=#1a73e8>作者：</font>** Linghua Zhang, Yunhe Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement asks a system to improve the very system that improves it. Today's language models improve themselves through data, training recipes or scaffolds. Whenever their weights change, gradient descent writes the update, not the model. We let the model write its own weights. In SELFWRITE, each generation the current model studies its own reasoning on fresh training problems, inspects its own weights and activations in a persistent Python session, and writes a program that constructs a low-rank weight edit for itself from white-box primitives (singular directions, activation contrasts between its right and wrong answers, rank-one projections, tensor computations), with no training or gradient tool. Every candidate is graded once on a hidden gate set against the current model; the best strictly improving edit is merged into the weights, and the edited model writes the next edit. On Qwen3.8-27B and math problems from DAPO-Math, five generations of SELFWRITE raise gate accuracy from 73.95% to 76.45% and accuracy on a held-out test split that the loop never sees from 76.30% to 77.75% (avg@4) and from 82.60% to 84.80% (pass@4), without a single gradient step. A language model can author useful changes to its own weights without gradients, and the edited model keeps writing useful edits.

---


### 236. [Layer-Level Control of Language Model Execution in Agent Frameworks](https://arxiv.org/abs/2611.29519)

**<font color=#1a73e8>作者：</font>** Ran Guan, Yiqi Lin, Xiangxi Tian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent frameworks typically orchestrate language models through prompt-and-response interfaces. We propose a harness design that exposes intermediate model states and layer-level execution controls to the agent runtime. By connecting state collection, policy fitting, and execution, the design enables policies to allocate computation within and across models based on intermediate states. We demonstrate the approach with a prototype that learns stitching bridges and state-conditioned execution policies from paired model states, then applies them during inference to select among continue, exit, and stitch. For dispatcher supervision, we select the least-computation action whose full-vocabulary next-token prediction matches the source model's full-depth prediction, using continue when neither early action matches. We train these components on a frozen proxy corpus of 5,000 typed-decision items authored using source texts sampled from WildChat conversations, then evaluate the prototype on JevBench measuring task accuracy, agreement with full-model predictions, and end-to-end latency including runtime overhead. Preliminary results show an approximately 15% reduction in mean latency while maintaining task accuracy comparable to full-model inference.

---


### 237. [Estimating Silenced Tokens in Quantized LLMs](https://arxiv.org/abs/2611.29536)

**<font color=#1a73e8>作者：</font>** Giuseppe Pappalardo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantization is the standard way to shrink large language models, and it is usually judged by perplexity and task accuracy. We ask a different question: after quantization, which words can the model still say at all? A token is silenced when no hidden state can make it the top choice of the output layer, so a greedy decoder can never produce it. We give a simple, scalable way to estimate how many tokens a quantized output head silences, combining three checks: a direction that lets a token win (so it is safe), an upper bound on how close a token's row is to being trapped inside the others, and an exact match that proves a token can never win. Each count is therefore a certified range: exact matches give its lower end and flagged tokens can only raise its upper end. In nearly all settings we report down to 3 bits the two ends coincide, so the counts are exact. Across three open models we find that quantization silences tokens: on large-vocabulary models it already appears at 8-bit precision, up to a few hundred previously reachable tokens on a 1B-parameter model, and grows as precision drops, while a small-vocabulary model resists until 3 bits. The loss is far from uniform across languages: on a multilingual vocabulary the silenced tokens are overwhelmingly non-Latin (Korean, Chinese, Thai, Arabic and Hebrew), even though Latin tokens dominate the vocabulary. Silencing is thus a measurable, language-sensitive side effect that standard averages miss, and it should be reported alongside them.

---


### 238. [SCRA-CLIP: Spherical-Contextual Representation Adaptation for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2611.29545)

**<font color=#1a73e8>作者：</font>** Peng Chen, Chao Huang, Wenqiang Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision-language models have facilitated zero-shot anomaly detection (ZSAD) through transferable visual-semantic representations. However, detecting fine-grained anomalies remains challenging due to inadequate modeling of diverse anomaly patterns and their spatial context. To address these challenges, we propose SCRA-CLIP, a Spherical-Contextual Representation Adaptation framework that jointly enhances anomaly-aware textual semantics and context-sensitive visual representations. Specifically, we introduce Spherical Prototype-Conditioned Prompting (SPCP), which employs von Mises--Fisher mixtures to model the directional distributions of normal and abnormal patch features. These state-specific prototypes are incorporated into textual contexts to guide the learning of more discriminative textual representations. Furthermore, we develop Context-Deviation Guided Visual Adaptation (CGVA), which captures local feature deviations relative to multi-scale neighborhood contexts and refines patch representations through adaptive gating. By integrating distribution-aware semantic modeling with context-sensitive visual adaptation, SCRA-CLIP facilitates more discriminative cross-modal matching for fine-grained anomaly detection and localization. Extensive experiments on 11 industrial and medical benchmarks demonstrate the effectiveness and generalization capability of SCRA-CLIP across diverse unseen categories and domains. The code will be publicly available upon publication.

---


### 239. [ParseGap: Testing What Coding Agents Authorize and What Shells Execute](https://arxiv.org/abs/2611.29546)

**<font color=#1a73e8>作者：</font>** Jieyu Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM coding agents authorize shell commands by parsing a command string against a policy and passing the raw string to a system shell, so the gate adjudicates one reading while the shell executes another. We present ParseGap, a differential testing framework that runs each command through an unmodified vendor checker and GNU Bash 5.2 in an isolated container, flagging a violation whenever an approved command produces policy-violating runtime effects. Across eight production coding agents, ParseGap identifies 17 root causes across three divergence boundaries: at the parse, where an upstream tree-sitter-bash defect hides a second command from Mistral Vibe and Gemini CLI; at the utility, where every checker permits read-only binaries whose arguments write files or launch programs (9-47 of 55 cases); and at confinement, where an allow rule in OpenAI Codex CLI disables its read-only OS sandbox. Live trials across two frontier models triggered policy violations in all 16 agent-model pairs (14 under configured restrictions). To eliminate the second reading, we design ShellPlan, which compiles a strict Bash subset once into a typed execution plan, validates utility arguments against positive capability specifications, and dispatches approved plans directly via execve without a shell. Over a formal operational model, we prove single-interpretation dispatch and bound touched programs and files under audited assumptions. ShellPlan admitted 0/4,174 active attacks across six static suites and 0/90 hits in a ten-model agent benchmark (62/90 unguarded) at 1.28 ms median gate latency, preserving 36/36 (100%) frontier standard-dev completion (74/100 overall) and 0/348 external over-allows outside modeled exceptions.

---


### 240. [Inspect Before You Decide: Evidence-Guided Visual Search for Industrial Anomaly Detection](https://arxiv.org/abs/2611.29551)

**<font color=#1a73e8>作者：</font>** Peng Chen, Chao Huang, Yangyang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal large language models (MLLMs) have demonstrated remarkable potential for industrial anomaly detection and understanding. However, reliably identifying subtle anomalies remains challenging, as existing approaches often struggle to acquire and verify fine-grained visual evidence beyond global observations. To address this challenge, we propose EVAD, an evidence-guided visual search framework that enables MLLMs to actively seek and examine diagnostically informative visual evidence for reliable anomaly reasoning. Specifically, EVAD begins with a global visual assessment to identify potentially anomalous regions for further inspection. Building upon this observation, we introduce a Monte Carlo Tree Search (MCTS)-guided exploration strategy that progressively acquires visual evidence through two complementary operations: semantic refinement for fine-grained inspection and spatial expansion for contextual verification. The acquired evidence is subsequently evaluated and integrated to support more informed and reliable anomaly decisions. Extensive experiments across multiple industrial anomaly detection tasks demonstrate that EVAD achieves state-of-the-art performance in most evaluated settings, highlighting the effectiveness of active evidence exploration for fine-grained anomaly understanding and reasoning. The code will be publicly available upon publication.

---


### 241. [LM2 Compiling a Language Model into Another Model Weights](https://arxiv.org/abs/2611.29577)

**<font color=#1a73e8>作者：</font>** Naman Chawla, Chhavi Dhiman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deploying a conversational model and a specialist together could avoid maintaining a separate specialist service. We present LM2, which embeds a trained story generator into a larger conversational model. The larger model handles the conversation and invokes the generator for story requests. We constrain the generator arithmetic during training so its calculations can be compiled directly into added model layers. We compare this approach with QwenPU, which executes the stories260K language model on an embedded processor. LM2 requires one host token per generated character, compared with approximately 25,000 for QwenPU. However, its story generator predicts held out text less well, i.e. 1.145 bits per character versus 0.894 for stories260K, where lower is better. The Qwen3.5, 0.8B implementation occupies 18.1 GB and generates the same characters as a standalone integer implementation of the inner model in the tested runs. These results illustrate a tradeoff between host-token cost and text-prediction performance.

---


### 242. [Single-Coordinate Activation Steering for Controllable Social Stance in Language Models](https://arxiv.org/abs/2611.29578)

**<font color=#1a73e8>作者：</font>** Naman Chawla, Chhavi Dhiman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Steering one neuron of a small language model can impose a topic or a quirk without training, yet replications show that many published single-neuron recipes are fragile or nonspecific. This paper asks whether an interpersonal stance can be controlled in this manner. The stance studied is a distant crush, a chatbot character that is guarded, intermittently warm and inconsistent. In Qwen3.5, 4B, contrasting activations on hand-written guarded and eager replies identified neuron 7515 of layer 9 as a candidate for controlling this stance. Increasing this neuron activation made the characters replies more distant. Three language models rated this change as stronger than the effects of changing randomly selected neurons, and a blind human comparison supported the finding. Changing the interventions direction between messages also shifted replies between warmer and more distant styles. This suggests that a language model conversational stance can be personalized without finetuning.

---


### 243. [From Learning Rates to Rotational Schedules: Finite-Horizon Theory on the Sphere](https://arxiv.org/abs/2611.29579)

**<font color=#1a73e8>作者：</font>** Jacopo Graldi, Antonio Orvieto, Anastasia Koloskova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How should step sizes be scheduled across a finite training horizon? Cosine and warmup-stable-decay (WSD) schedules are widely adopted in large-scale pretraining, yet their effect on optimization also depends on parameter norms. Normalization can make parameter groups scale invariant, so that the loss depends only on their direction, while their norms still affect how fast the parameters rotate. In this work, we formulate schedule design directly in the space of rotational motion. Working within a geodesically convex spherical setting, we derive a last-iterate convergence guarantee for arbitrary rotational schedules that separates their overall scale from their distribution over time. We derive the unique schedule that minimizes this bound and prove that it approaches linear decay as the horizon grows. Empirically, our rotational interpretation and idealized spherical analysis provide useful predictions for LLM pretraining in practice, including schedule comparisons missed by existing analyses. Our analysis predicts schedule ordering across model scales for both vanilla (Adam, Muon) and Hyperball-style (AdamH, MuonH) optimizers. Our Hyperball experiments support the predicted strong performance of linear LR decay and confirm our prediction that WSD underperforms in this setting. Accounting for parameter norm dynamics, we predict instead the strong performance of WSD for Adam and Muon shown in practice. Guided by our theoretical insights, we also derive a new LR schedule for Adam and Muon, which improves over the established cosine and WSD schedules. All in all, these results support the use of rotational dynamics to understand, predict, and ultimately guide scheduling in LLM pretraining.

---


### 244. [Social Interaction Breaks Replicate Independence in Controlled-Clone LLM Agents](https://arxiv.org/abs/2611.29581)

**<font color=#1a73e8>作者：</font>** Yandan Zheng, Haoran Luo, Anh Tuan Luu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM evaluations and social simulations create many agents from one model and treat them as independent replicates, even after the agents interact. This assumption remains untested with matched controls. We introduce SocCogEval, a controlled-clone assay for Social Cognitive Transfer (SCT). Clones share the base model, system prompt, and decoding parameters and differ only in a private brief, and a factorial protocol separates the brief, 30 rounds of interaction, and initialization noise. On Qwen3-122B-FP8, interaction with the briefs held fixed raises off-topic BFI-10 response-profile drift by $\bar{\Delta}=+0.917$ and $+0.912$ in two topically disjoint scenarios (exact $p=0.0008$ and $0.0039$). The drift is larger than under the brief alone, persists under temperature-zero re-probing, and stays positive without typed memory extraction in exploratory tests. Matched solo generation reproduces part of it, and social interaction remains highest. Across five more model variants, every scenario-averaged interaction contrast is positive. Each interacting population is therefore one replicate, and treating its agents as independent requires paired no-interaction controls. Our code and data are publicly available at this https URL.

---


### 245. [How Multi-Timescale Memory Cools Optimization: Theory and Evidence from AdEMAMix](https://arxiv.org/abs/2611.29588)

**<font color=#1a73e8>作者：</font>** Jacopo Graldi, Antonio Orvieto, Anastasia Koloskova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Augmenting AdamW with multiple momentum timescales improves large language model pretraining, yet the mechanism driving these gains remains poorly understood. We identify an interaction between multi-timescale optimizer memory and the geometry of normalized networks: memory changes parameter norms and thereby controls how fast parameters rotate. Starting from exact norm dynamics under decoupled weight decay, we show that the parameter norm depends on the temporal correlation of the updates, with weight decay controlling how long these correlations influence optimization. We show how an independently weighted slow momentum can substantially increase the norm of parameters, while contributing negligible power to the instantaneous update, therefore acting as an endogenous annealing schedule. We study this mechanism in AdEMAMix for language-model pretraining. Controlled interventions show that this scheduling mechanism has clear practical consequences and is an important factor behind AdEMAMix's advantage over AdamW.

---


### 246. [KernelShift: Benchmarking Kernel Optimization Across Evolving Hardware](https://arxiv.org/abs/2611.29590)

**<font color=#1a73e8>作者：</font>** Shuaiwei Huang, Weihua Du, Allen Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Efficient AI computation depends on hardware that evolves over time, shifting the strategies needed to implement performant code. For CPU kernels, a key evolving factor is the set of available architectural extensions, which expose specialized hardware instructions that change the techniques used to optimize kernels. We study how effectively coding agents use these new, potentially unfamiliar extensions to write fast code. We introduce KernelShift, a benchmarking pipeline and a set of environments for evaluating coding agents in kernel optimization across evolving CPU architectures. Its agent-assisted, human-verified pipeline turns code repositories into benchmark instances, and its environments let agents optimize code with feedback from the target hardware. Using this pipeline, we construct 99 kernels from real-world, actively developed repositories (ncnn, this http URL, Arm SIMD Loops, and KleidiAI), including inference workloads derived from real model executions. KernelShift supports incorporating new kernels and hardware configurations as libraries and processors evolve. We evaluate agents with proprietary and open-weight models across progressively newer architectural extensions (Arm Neon, SVE, SVE2, and SME2), examining how performance changes as hardware evolves. On established extensions, agents beat the auto-vectorized compiler everywhere (2.4-19.8x) and exceed general-purpose libraries such as ncnn (getting up to 2.74x over its Neon kernels), but fall behind Arm's hand-tuned KleidiAI kernels (0.70x). In end-to-end inference of two LLMs, agent-written kernels achieve a 1.3-1.6x prefill speedup over this http URL's fast path. However, current agents do not yet reliably adapt to new extensions that require unfamiliar programming models, such as SME2's matrix tiles.

---


### 247. [Rethinking Closed-Ended Medical VLM Evaluation: From Stable Wrongness to Counterfactual Answer Sensitivity](https://arxiv.org/abs/2611.29592)

**<font color=#1a73e8>作者：</font>** Qi Wu, Xiaoyu Liu, Ao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As medical VLMs are increasingly evaluated for clinical decision-support scenarios, knowing when to trust their predictions is critical. Closed-ended medical VQA has become a common benchmark format because it enables automated scoring. Yet, systematic investigation into whether this format changes the reliability problem remains scarce. We identify a failure mode that we call stable wrongness: models can produce incorrect yes/no answers that remain confident and repeatable even when patient-specific visual evidence is removed or mismatched. This failure violates the premise behind sampling-stability uncertainty methods, including recent hallucination-aware calibration (HAC) variants: disagreement is informative only when errors are unstable. When shortcut-driven errors are themselves stable, sampling agreement can remain deceptively high. Motivated by this limitation, we introduce Counterfactual Answer Sensitivity (CAS), which shifts reliability estimation from answer stability to evidence sensitivity. CAS uses cross-modal counterfactual interventions, such as text-only, black, and corrupted images, to audit whether a committed yes/no answer remains supported when visual evidence is invalidated. Across 7 VLMs and 3 benchmarks, CAS outperforms the best HAC-family scores across all evaluated settings, achieving a macro-averaged AUROC gain of +0.150 for error detection. Mechanistic analysis further shows that CAS recovers hidden errors in the HAC-confident region and that its strongest standalone signal is counterfactual decision-boundary shift rather than hard prediction stability. Our findings suggest that closed-ended evaluation should test visual dependence, not only answer stability, in safety-critical medical contexts.

---


### 248. [Wactorz: Self-Writing LLM Agents That Discover, Repair, and Migrate at the Edge](https://arxiv.org/abs/2611.29619)

**<font color=#1a73e8>作者：</font>** Panagiotis Kasnesis, Lazaros Toumanidis, Amalia Contiero Syropoulou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most LLM agent frameworks build a crew that runs a task and exits. Physical environments (e.g., homes, labs, factory floors) need agents that stay up for months, survive their own bugs, and run on whatever hardware is already next to the sensors. We present Wactorz, an open-source runtime in which LLM-generated agents are long-lived, supervised actors: a planner turns a chat request into Python, compiles it into a new actor at runtime, and a supervisor restarts that actor alone, with its state intact, when it crashes. All coordination rides on MQTT, so agents can be spawned on, and live-migrated between, edge nodes such as a Raspberry Pi, and every internal event is a topic external systems can subscribe to. The recorded demo builds a camera-to-lamp automation from one chat request, adds a second agent that is auto-wired to the first by topic and carries a deliberate division-by-zero, watches that agent repair its own code without losing its count, then deploys a fresh Raspberry Pi node and live-migrates the agent onto it, in under four minutes of wall-clock time and \$0.13 of model usage. This extended version adds what the two-page demonstration paper could not: the Wiring view of the topic graph, Wactorz as a library for hand-written agents, how trained models are stored, sent to nodes and replaced, the security model, and the system's limitations.

---


### 249. [Explainable Emotion and Mental Health Reasoning in Large Language Models Using Theories of Emotion](https://arxiv.org/abs/2611.29628)

**<font color=#1a73e8>作者：</font>** Tadesse Destaw Bela, Iqra Ameer, Helena Gómez Adorno 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Advancements in Large Language Models (LLMs) have enabled a wide range of applications. However, their ability to simulate human-like behavior and reasoning remains unclear. While emotion detection is a better-established Natural Language Processing (NLP) task, existing approaches primarily focus on directly classifying text into predefined emotion classes, often overlooking the appraisal process that explains why an individual experiences a particular emotion in a given situation. In this work, we propose Psychology-based Chain-of-Thought (PsyCoT) reasoning, a theory-driven prompting strategy grounded in the Schachter-Singer and Cognitive Appraisal theories of emotion. We propose and evaluate PsyCoT for subjective NLP tasks, including emotion analysis, emotion intensity prediction, stress analysis, and depression severity identification. Our evaluation covers four levels of classification complexity: binary, multiclass, multi-label, and ordinal scaling, spanning 11 languages. We assess the performance of five state-of-the-art LLMs across these selected subjective NLP tasks. Experimental results demonstrate that PsyCoT prompt variants improve the standard chain-of-thought (CoT) prompting across the evaluated tasks. Across all evaluated tasks, PsyCoT yields F1 score gains ranging from 0.5% to 28.1%, depending on the model, task, and language configuration.

---


### 250. [Diversity in Unity, Theory in Practice: Hierarchical Multitask Benchmarks for Chinese Minority Languages](https://arxiv.org/abs/2611.29635)

**<font color=#1a73e8>作者：</font>** Yijie Li, Xi Cao, Yuan Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the rapid advancement of LLMs, their performance on linguistically and culturally diverse minority languages within a unified national context remains underexplored. We present CMiLBench, a collection of hierarchical multitask benchmarks designed to translate theoretical notions of "diversity in unity" into practical evaluation for three representative Chinese minority languages: Tibetan, Mongolian, and Uyghur. CMiLBench comprises 24,663 instances across 5 difficulty levels and 17 tasks spanning foundational ability, cultural specificity, and safety alignment. We adopt existing dataset adaptation, minority knowledge construction, and high-resource benchmark translation to construct CMiLBench. We assess 14 state-of-the-art commercial and open-source LLMs with a hybrid framework that integrates automatic metrics and LLM-as-a-Judge scoring. The comparative experimental results reveal the gap between theoretical capability and practical utility. CMiLBench serves as a foundational and scalable evaluation resource to bridge the digital language divide and promote the informatization and intelligentization of low-resource Chinese minority languages.

---


> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
