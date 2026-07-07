# 🧠 大模型相关研究 | 2026年07月08日

> 本类共 **248** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**201-248**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-248**

---

### 201. [ToolFailBench: Diagnosing Tool-Use Failures in LLM Agents](https://arxiv.org/abs/2607.04686)

**<font color=#1a73e8>作者：</font>** Harsh Soni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tool calling is central to modern language model agents, but aggregate benchmark scores often hide where tool use fails. A model that never calls a needed tool and a model that calls the tool but ignores the result can look similar under final task accuracy. We introduce ToolFailBench, a diagnostic benchmark for measuring tool-use failures across 1,000 tasks in finance, medicine, law, cybersecurity, and real estate. Tool-required tasks return values the model wouldn't guess, forcing it to trust the tool while control tasks attach the same tools but should be answered directly. We label each trace with Tool-Skip, Result-Ignore, Output-Fabrication, and Unnecessary-Tool-Use, using a rule classifier and two LLM judges aggregated by majority vote. Across 19 headline models, the best reaches 86.33% Clean Tool-Use Rate, showing that faithful tool use is not saturated. More importantly, models with similar aggregate scores fail in different ways: most stay disciplined on no-tool controls, while Llama-3.1 models show an Always-Call pattern, and at the same parameter scale Llama-3.1-70B and Qwen2.5-72B differ by 89 percentage points on control-task accuracy. Tool-use evaluation should measure not only whether agents call tools, but whether they use tool outputs correctly and avoid tools when none is needed.

---


### 202. [Solve the Missing First Step: Can VLMs Standardize Raw Heterogeneous Medical Data?](https://arxiv.org/abs/2607.04694)

**<font color=#1a73e8>作者：</font>** Xin Chen, Dongliang Xu, Cunhao Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As vision-language models (VLMs) are increasingly applied to medical AI, existing benchmarks mainly focus on evaluating their diagnosis ability over given medical images and texts, implicitly assuming that standardized medical images, texts or question-answer pairs are already prepared. However, this assumption does not hold when we apply VLMs in real clinical practice, where medical data is often raw, heterogeneous, and fragmented across different sources. In this paper, we study this missing step, i.e., raw medical data standardization. Specifically, models are given raw dataset folders and evaluated on their ability to identify source formats, convert raw medical images into VLM-compatible visual inputs, extract relevant textual information, and organize the results into structured image-text pairs. To construct this Medical Data Standardization Benchmark (MDS-Bench), we manually annotate 1,939 raw medical data standardization tasks covering diverse clinical practice, radiology modalities, annotation formats, and directory layouts. Extensive experiments show that even the best performing VLMs, i.e., Gemini 3 Flash, achieve only 48.6% end-to-end success rate. Our research highlights raw medical data standardization as a critical bottleneck for medical AI diagnosis in real practice.

---


### 203. [RSPO: Reward-Swap Policy Optimization for Multi-Turn LLM Agents](https://arxiv.org/abs/2607.04713)

**<font color=#1a73e8>作者：</font>** Qiang Liu, Taian Guo, Ruizhi Qiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning holds significant potential for training large language models (LLMs) to handle multi-turn interactive tasks. However, in long-horizon, multi-turn tasks characterized by sparse outcome rewards, directly training with outcome rewards often results in slow convergence due to the sparsity of signals and the lack of fine-grained feedback. Furthermore, the model may fail to learn successful trajectories that are not sampled during training, thereby limiting its performance. Conversely, while employing customized dense process rewards provides richer signals and accelerates convergence, these surrogate rewards may exhibit potential misalignment with the ground-truth outcome rewards. This inconsistency can bias the training direction and ultimately degrade the model's final performance. In this work, we propose Reward-Swap Policy Optimization (RSPO), a method designed to leverage the rich information from dense process rewards to facilitate training with outcome rewards. By utilizing a reward-swap mechanism, RSPO ensures the diversity of sampled trajectories while guaranteeing consistency between the optimization objective and the true outcome rewards, thereby elevating the performance ceiling of the model. We conduct extensive experiments on two challenging agent benchmarks, WebShop and ALFWorld. By applying our method to various reinforcement learning algorithms, including GRPO, PPO, and GiGPO, we demonstrate that RSPO achieves consistent performance improvements across different baselines and benchmarks.

---


### 204. [Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment](https://arxiv.org/abs/2607.04728)

**<font color=#1a73e8>作者：</font>** Yu Li, Xiuyu Li, Mingyang Yi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training for large language models (LLMs) follows a efficient paradigm of "rollout then update", which inevitably results in off-policy training data. To resolve this, Importance sampling (IS) is proposed, while the token-level ratios compound over long sequences, causing severe variance exploded. A natural idea is "transferring" these off-policy token into on-policy token, so that the importance scores for correction are unnecessary. Following this idea, we propose Selective Importance Sampling (SIS), which is inspired by rejection sampling. Concretely, SIS implements by viewing off-policy model as proposal distribution, and implement a token-level rejection test: accepted tokens are viewed as on-policy, so that receive unit importance score, while rejected tokens retain the standard IS correction. Our proposed SIS is theoretically proved reducing the gap between token-level and sequence-level off-policy gradient estimators. The SIS acts as a plug-in that only modifies the importance ratio in the policy loss, adding negligible wall-clock overhead, and can be combine with a vast vary of RL post-training algorithms. Experiments on dense and MoE LLMs across math and agent benchmarks show that SIS consistently improves all objectives, while providing substantially stronger robustness under off-policy data.

---


### 205. [LP-SFT: Local-Preserving Supervised Fine-Tuning via Multimodal Entropy Structure](https://arxiv.org/abs/2607.04733)

**<font color=#1a73e8>作者：</font>** Yueyang Wang, Baolong Bi, Shuo Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is the standard approach for adapting pretrained language models to downstream domains, yet it often improves target-domain behavior at the cost of degrading pre-existing capabilities. Standard cross-entropy fine-tuning promotes only the observed label token and leaves unconstrained how probability mass is redistributed over other plausible alternatives, potentially distorting the rich local preference structure learned during pretraining. We first analyze next-token predictions using Shannon and Renyi entropies, revealing that pretrained models exhibit a regular multimodal entropy structure. These entropy peaks correspond to varying numbers of plausible alternatives, indicating that the base model intrinsically encodes rich distributional knowledge beyond the single supervised token. Motivated by this observation, we propose LP-SFT, a Local-Preserving Supervised Fine-Tuning objective designed to explicitly protect this inherent entropy structure. At each step, LP-SFT constructs an adaptive support of alternative tokens and applies a locally normalized preservation loss to maintain the base model's relative structure among them, while standard cross-entropy independently optimizes the supervised token. Across mixed-domain and single-domain fine-tuning experiments, LP-SFT improves overall performance over vanilla SFT and recent SFT-enhancement baselines, achieving the best balance between pass@1 accuracy and pass@k performance. These results suggest that local preservation helps mitigate capability degradation without collapsing sampling-accessible diversity.

---


### 206. [AgenticPD: A Stage-Aware Agentic Framework for Physical Design QoR Optimization](https://arxiv.org/abs/2607.04758)

**<font color=#1a73e8>作者：</font>** Shuo Ren, Zijin Cheng, Yaohui Han 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physical design quality-of-results~(QoR) optimization is hard and expensive. Choices made at one stage can help or hurt later stages. Each evaluation requires a costly EDA run through the full flow. While existing methods still treat optimization as flat parameter tuning or a LLM-based script generation task, we present AgenticPD, a stage-aware agentic framework for physical design QoR optimization. Instead of re-running the full flow after every trial, AgenticPD is organized around the stage boundaries of the physical design flow, where a Judge Agent navigates the search and stage-specialized agents make local decisions within their own stage using stage-local tools. Additionally, the agent harness in AgenticPD provides structured observations, execution history, and agent context management. As a result, the system can branch from prior intermediate states and reuse checkpoints to continue the optimization procedure, and every candidate is evaluated at the post-route signoff. Across these baselines, AgenticPD achieves strong post-route timing while remaining competitive in power and area.

---


### 207. [DGSeg: Dynamic Gating of Semantic-Spatial Guided Predictions for Reasoning Segmentation](https://arxiv.org/abs/2607.04779)

**<font color=#1a73e8>作者：</font>** Ruizhe Zeng, Siyu Cao, Lu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning segmentation aims to predict pixel-wise masks for targets given complex language queries. Existing approaches leverage Multimodal Large Language Models (MLLMs) for vision-language reasoning and generate intermediate target cues (e.g., points or boxes) to guide a segmentation model. However, compressing rich reasoning into sparse cues often introduces ambiguity and noise, preventing these cues from accurately preserving the reasoning intent. While multiple complementary cues can enrich target information, existing methods typically feed them jointly into a single segmentation process, allowing ambiguous or erroneous cues to affect the entire prediction. Therefore, we propose DGSeg, a reasoning segmentation framework that learns to fuse predictions guided by semantic and spatial cues. Specifically, the MLLM jointly reasons about both target identity and spatial location, producing complementary semantic and spatial cues that are fed into separate segmentation branches. Their predictions are adaptively integrated by a lightweight dynamic gating module trained with relative branch-quality supervision to suppress noisy or conflicting regions. Extensive experiments demonstrate that DGSeg consistently outperforms strong baselines on multiple benchmarks and achieves 69.6% and 67.3% gIoU on the challenging ReasonSeg validation and test splits. Code is available at this https URL.

---


### 208. [Pretraining Curricula Enable Selective Fine-tuning](https://arxiv.org/abs/2607.04846)

**<font color=#1a73e8>作者：</font>** Sebastian A. Bruijns, Jirko Rubruck, Mia H. Whitefield 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers follow implicit curricula whereby some tasks are learned before others. However, how explicit pretraining curricula influence learning, generalization, and the selectivity of fine-tuning is unclear. This is important for AI safety, where fine-tuning is used to selectively suppress misaligned behaviors. Here, we compare curricula that pretrain tasks in a balanced (sampled uniformly) or an imbalanced (one task early, the other late) fashion. We show that imbalanced learning of two conflicting copy tasks promotes in-context learning and improves the selectivity of refusal fine-tuning. Ablations and activation patching show that this occurs because imbalanced pretraining encourages tasks to be disentangled in separable neural circuits, whereas balanced training routes both tasks through a common pathway. We extend these findings to a synthetic language learning task involving rule-consistent and rule-violating data, where imbalanced curricula similarly lead to more localized, less entangled rule representations, resulting in more robust rule-following behavior. Together, these results suggest that imbalanced pretraining curricula may be an important tool for promoting disentangled representations, with direct consequences for the precision and reliability of safety fine-tuning.

---


### 209. [CARL: Constraint-Aware Reinforcement Learning for Planning with LLMs](https://arxiv.org/abs/2607.04854)

**<font color=#1a73e8>作者：</font>** Qiuyi Qi, Jinjian Zhang, Mutian Bao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite their strong reasoning capabilities and extensive world knowledge, Large Language Models (LLMs) frequently generate plans that violate task constraints, undermining their reliability in real-world applications. This deficiency arises from a lack of systematic mechanisms to incorporate constraint information during the generation process. While existing approaches attempt to mitigate this by relying on external tools or task decomposition, they fail to enhance the model's intrinsic constraint awareness. To address this, we propose Constraint-Aware Reinforcement Learning (CARL), a novel RL framework designed to strengthen LLMs' intrinsic focus on constraints. CARL introduces a constraint-aware reward by comparing the model's output distributions under constrained and unconstrained inputs, encouraging constraint focus and penalizing neglect. Compatible with various RL frameworks and requiring no external solvers or top models, CARL enables scalable, end-to-end constraint-aware planning. Extensive experiments on BlocksWorld, TravelPlanner, and T-Eval demonstrate that CARL significantly outperforms standard Reinforcement Fine-Tuning (RFT) baselines and state-of-the-art reasoning models, exhibiting a markedly increased focus on constraints.

---


### 210. [HunyuanOCR-1.5: Making Lightweight OCR VLMs Faster and Better](https://arxiv.org/abs/2607.04884)

**<font color=#1a73e8>作者：</font>** Gengluo Li, Xingyu Wan, Shangpin Peng 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present HunyuanOCR-1.5, a lightweight end-to-end OCR-specialized vision-language model. HunyuanOCR unifies document parsing, text spotting, information extraction, text-image translation, and multi-image document understanding within a single end-to-end VLM. Building upon the lightweight architecture of HunyuanOCR-1.0, HunyuanOCR-1.5 does not redesign the backbone, but systematically improves both efficiency and capability. For efficiency, we adapt DFlash to OCR decoding, significantly reducing the latency of long structured outputs such as dense documents, tables, and formulas while preserving output distribution. Powered by DFlash, HunyuanOCR-1.5 achieves a 6.37x Transformer inference speedup and a 2.14x speedup under vLLM, delivering the fastest inference among lightweight OCR VLMs. For capability, we propose Agentic Data Flow, an agent-driven data construction system that transforms model weaknesses into executable data requirements and autonomously performs material search, quality verification, and pipeline development. It substantially improves long-tail capabilities in ancient-script OCR, fine-grained chart and table parsing, multi-image text-centric QA, low-resource multilingual parsing, and document hallucination evaluation. HunyuanOCR-1.5 ranks among the top-tier end-to-end OCR solutions on OmniDocBench v1.6 while achieving new performance milestones across these long-tail tasks. Combined with an upgraded pretraining and post-training recipe, HunyuanOCR-1.5 further extends its capability in high-resolution, long-context, and multi-task scenarios. Experiments demonstrate faster inference, broader OCR capability coverage, and the deployment advantages of a lightweight end-to-end model. We will release the model weights and training code to support future research and real-world OCR applications.

---


### 211. [Evaluating Large Language Models for Antisemitic Incident Classification](https://arxiv.org/abs/2607.04890)

**<font color=#1a73e8>作者：</font>** Karina Halevy, Julia Mendelsohn, Chan Young Park 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Addressing hate and violence in society requires timely detection of hateful events from public reporting, but automated identification of hateful events remains underexplored. We introduce the task of hateful event detection and investigate the ability of AI systems, specifically large language models (LLMs), to discover and classify reports of antisemitic events with fine-grained labels. We evaluate OpenAI's GPT-4o and Meta's Llama-3.2-3B-Instruct on multiple expert-annotated datasets containing antisemitic event descriptions from news articles, civil society reports, and official records. We show that LLMs, particularly GPT-4o, have potential for this task, but substantial improvement is needed. Providing clear term definitions and in-context examples in prompts can improve performance: definitions are most helpful for rhetoric-oriented events (e.g. classical antisemitic tropes), while examples help label action-oriented events (e.g. physical assault). A case study of college newspapers demonstrates that LLMs can help surface relevant real-world events, supporting early monitoring and intervention. Overall, our findings highlight both opportunities and critical gaps in AI's ability to recognize complex harms and underscore the need for collaborative efforts among AI developers, policymakers, and civil society to design models, implement robust evaluation, and develop policy frameworks for defining and combating hate efficiently and effectively.

---


### 212. [Medi-Gemma: A Hybrid Clinical Decision Support System Integrating Deterministic EMR Analytics and Retrieval-Augmented Generation](https://arxiv.org/abs/2607.04907)

**<font color=#1a73e8>作者：</font>** Mohammed Saim Ahmed Quadri, Yunzhe Xue, Justin W. Ady 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying Large Language Models (LLMs) in high-stakes clinical settings remains limited by structural hallucinations, weak deterministic reasoning over tabular patient data, and omissions in vector retrieval. This paper presents the architecture and validation of Medi-Gemma, a Clinical Decision Support System (CDSS) for wound pathology triage and workflow automation. The platform introduces a decoupled framework that separates clinical perception from data orchestration while preserving traceable reasoning. Medi-Gemma uses a multi-stage pipeline coordinated by a centralized ClinicalOrchestrator. Data requests are handled without generative inference by a DataManager that cleans unstructured Electronic Medical Record (EMR) files through type coercion. Natural language queries are processed by a hierarchical IntentRouter, which routes requests to deterministic analytics paths executed by a PandasQueryEngine or to patient-specific reasoning managed by a ClinicalRAGEngine using a CPU-optimized vector store. A key contribution is the Ground Truth Injection Module, which intercepts patient-specific queries, extracts numeric identification tokens, queries the structured dataframe via Pandas, retrieves the latest validated clinical state, and embeds this snapshot as an overriding context block in the LLM prompt before generation. Safety compliance is enforced by a deterministic ProtocolManager that maps clinical terminology to fixed evidence-based risk pathways, while a SafetyVerifier phrase filter prevents output rule violations. Validation shows that this architecture eliminates semantic context drift, prevents database compilation crashes, and improves factual adherence to backend clinical repositories. These results support Medi-Gemma as a safer pattern for LLM-based clinical decision support where structured data fidelity, retrieval grounding, and deterministic safeguards are essential.

---


### 213. [When Do Foundation Models Pay Off? A Break-Even Analysis of Pretrained Time Series Forecasters](https://arxiv.org/abs/2607.04919)

**<font color=#1a73e8>作者：</font>** Nicholas Tan Jerome, Frank Simon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying a time series foundation model requires GPU infrastructure, engineering overhead, and carries no guarantee of improvement over XGBoost. We provide the first systematic break-even analysis answering when this investment pays off. Across 30 benchmark datasets, we compare zero-shot and LoRA fine-tuned foundation models (Chronos, Moirai, Lag-Llama) against classical baselines (Naive, ETS, ARIMA, XGBoost) at six training set sizes from 2% to 100% of available data. Foundation models outperform classical methods at every evaluated training fraction on 15 of 30 datasets -- GPU deployment is unconditionally justified on these regardless of data volume. On 6 datasets, classical methods surpass zero-shot foundation models with as little as 2% of training data (21-2,768 samples); on the remaining 9, break-even ranges from 24 to 8,361 samples. One robust deployment rule requires no model training: if n_train < 700 and seasonality is non-negligible, use FM zero-shot and skip fine-tuning -- this resolves 10 of 30 deployment decisions immediately. Contrary to common practice, LoRA fine-tuning can actively degrade performance on short series. We operationalise these findings as a two-step decision framework -- compute dataset length and seasonality strength, run a brief 5-10% pilot only if needed -- enabling practitioners to make the FM-versus-classical decision before committing to full infrastructure. Four dataset features motivate mechanistic hypotheses for the remaining cases, though reliable automated prediction at this benchmark scale remains an open problem. Code, benchmark, and decision tools are available at this https URL.

---


### 214. [DuplexChat: Constructing Speaker-Separated Full-Duplex Dialogue Speech at Scale for Spoken Dialogue Language Modeling](https://arxiv.org/abs/2607.04941)

**<font color=#1a73e8>作者：</font>** Wataru Nakata, Yuki Saito, Hiroshi Saruwatari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken dialogue models are trained on conversational speech in which each speaker is represented as a separate stream, but existing large-scale public speech corpora are mostly monaural, making them unsuited for SDLM training. We present DuplexChat, an open-source corpus for full-duplex spoken dialogue models, and DuplexChat-Pipe, a pipeline for constructing speaker-separated full-duplex dialogue speech from public podcast feeds. DuplexChat-Pipe filters language-specific podcast feeds, retrieves and cleans episode audio, extracts diarization-guided two-speaker dialogue clips, and applies speech separation and restoration to produce one channel per speaker. Running this pipeline yields a speaker-separated spoken dialogue corpus covering 282,634 hours of English and 132,723 hours of Japanese. Analysis results on DuplexChat show that it contains turn-taking dynamics present in human dialogues.

---


### 215. [You Frame It: How Conceptual Representations Shape LLM Detection and Reasoning about Antisemitism](https://arxiv.org/abs/2607.04945)

**<font color=#1a73e8>作者：</font>** Katharina Soemer, Helena Mihaljević  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs enable the integration of external conceptual resources at inference time, creating new opportunities for detecting ideologically and historically complex phenomena such as antisemitism. We investigate how different forms of conceptual grounding affect antisemitism detection and explanation behavior across four state-of-the-art LLMs.
Using two expert-annotated datasets, we compare definitional, fine-grained taxonomic, example-augmented, and large-context representations of antisemitism.
We find that fine-grained taxonomic representations substantially improve recall, while simultaneously reducing precision. Surprisingly, supplying substantially larger conceptual resources yields no additional quantitative benefit. Post-Holocaust antisemitism poses the most persistent challenge across models and configurations. Analysis of explanations further reveals systematic limitations including overproduction of conceptual references, reliance on lexical cues, overconfidence, and difficulties with subtle or justificatory forms of antisemitism.
Our findings highlight both the potential and the remaining limitations of conceptually grounded LLMs for antisemitism detection and reasoning.

---


### 216. [STAPO: Selective Trajectory-Aware Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2607.04963)

**<font color=#1a73e8>作者：</font>** Qiuyi Qi, Tian Liang, Mutian Bao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) is the dominant paradigm for training Large Language Model (LLM) agents on long-horizon tasks. However, sparse and delayed rewards often lead to trajectory neglect, in which agents lose focus on the task goal and interaction history at intermediate steps. Prior work has explored step-level supervision using Shannon-entropy-based uncertainty signals, which conflate inherent state complexity with agent confidence and therefore provide unreliable estimates of decision reliability. To address this issue, we propose normalized entropy, which measures confidence deviations relative to an agent's average behavior under a given state, thereby strengthening the association between low-quality actions and trajectory neglect. Building on this insight, we introduce Selective Trajectory-Aware Policy Optimization (STAPO), a hierarchical group-based RL framework. STAPO leverages normalized entropy to locate outlier steps associated with trajectory neglect and optimizes them via a joint mechanism of trajectory-aware reward and trajectory-independent penalty, enhancing trajectory awareness while preserving training stability. Extensive experiments on ALFWorld, WebShop, and Search-Augmented QA demonstrate that STAPO achieves state-of-the-art performance while substantially alleviating trajectory neglect, validating its effectiveness and robustness for agentic tasks.

---


### 217. [Train Smarter, Not Longer: Memorization-Guided Data Reuse for Efficient LLM Training](https://arxiv.org/abs/2607.04969)

**<font color=#1a73e8>作者：</font>** Jingwei Zuo, Cong Zeng, Ilyas Chahed 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The training paradigm of large language models has shifted from traditional one-pass training to multi-epoch training, as reasonable reuse of limited high-quality data can improve both model performance and sample efficiency. Meanwhile, excessive repetition introduces the risk of overfitting and diminishing returns. Determining when and how to reuse data effectively thus emerges as a natural but under-explored question. Through a novel observation of model's "Memorization Window" signals derived from loss retention dynamics and downstream evaluation scores, we propose "Memorization-guided Data Reuse", a training paradigm that adaptively determines when and how data should be reused, enabling principled decisions on the number of training epochs and the scheduling of data replays. Our preliminary experiments reveal a consistent memorization-driven regime: performance continues to improve with repetition far beyond current practice (e.g., the commonly cited four-epoch limit). While a full scheduler remains future work, these insights provide a foundation for memorization-aware training schedules, helping to determine reuse budgets and move toward training LLMs smarter rather than longer with limited high-quality data.

---


### 218. [Knowledge Knows, Verbalization Tells: Disentangling Latent Directions for Mathematical Solvability in LLMs](https://arxiv.org/abs/2607.05013)

**<font color=#1a73e8>作者：</font>** Nikolaos Xiros, Maria-Eleni Zoumpoulidi, Georgios Paraskevopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although LLMs have made significant progress in mathematical reasoning, determining whether a mathematical problem is solvable remains a fundamental yet challenging capability. While recent studies have probed internal representations of model solvability beliefs, verbalization has primarily been studied behaviorally rather than as an internal representation, limiting its analysis and manipulation. We address this gap by separately probing representations of solvability knowledge and verbalization, allowing us to disentangle the two within model hidden states. Across multiple LLMs, we show that knowledge and verbalization are encoded as distinct, linearly decodable representations and that fabrication is primarily associated with changes in verbalization rather than the underlying knowledge. Prompting with unsolvability cues reduces fabrication primarily by shifting verbalization, while activation steering demonstrates that these representations can be echanistically manipulated to improve model abstention.

---


### 219. [Beyond Modality Fusion: Deep Ensembles for Multimodal Classification](https://arxiv.org/abs/2607.05019)

**<font color=#1a73e8>作者：</font>** Ilya Burenko, Dmitry Vetrov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In multimodal classification, late-fusion approaches classify concatenated modality-specific features extracted by unimodal neural networks.
When modality imbalance is pronounced, various regularization techniques have been proposed to balance the learning process and overcome the inferior performance of late-fusion networks.
In contrast, this work demonstrates that multimodal data can be effectively classified without any explicit modality fusion, using deep ensembles of unimodal networks.
We systematically compare deep ensembles to late-fusion networks at equal parameter count and show that ensembles consistently outperform state-of-the-art late-fusion methods designed to address modality imbalance.
This advantage also holds over intermediate-fusion techniques we evaluated and over hybrid methods that combine unimodal and multimodal predictions.
We propose and empirically validate a method for selecting the number of models per modality in an ensemble, avoiding computationally expensive exhaustive search.
Under extreme modality imbalance and small ensemble sizes, the heuristic indicates that ensembles of unimodal models trained solely on the stronger modality are preferable; as the ensemble scales up, incorporating models from the weaker modality becomes beneficial.
Both predictions align with our empirical findings.
To systematically explore the challenges of optimizing multimodal models, we propose a synthetic multimodal framework that allows control over both the number of modalities and their predictive strength; our findings are consistent across synthetic and real-world datasets.
Finally, by fitting scaling laws to bimodal datasets, we estimate the asymptotic performance of ensembles.

---


### 220. [Multi-Large Language Model Orchestrated Severity Assessment of Clinical Records (MOSAIC)](https://arxiv.org/abs/2607.05032)

**<font color=#1a73e8>作者：</font>** Manuela Del Castillo Suero, Arnault-Quentin Vermillet, Nicole Sonne Heckmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Disease severity is a multidimensional construct difficult to capture with rule-based approaches in Electronic Healthcare Records (EHR). Agentic large language model (LLM) systems could synthesise clinical evidence and reason over EHRs, but remain unevaluated for this task. Methods: MOSAIC is a two-phase agentic LLM framework for severity phenotyping, using type 2 diabetes (T2D) as a proof-of-concept. MOSAIC was evaluated on a synthetic cohort (SyntheticMass; open-weight N = 4,886; closed-weight N = 200) against three algorithmic ground truths (DCSI, DiSSCo, Cooper) and against all-cause mortality and incident complications. Open-weight (locally deployable) and proprietary pipelines were also compared. Results: The generated framework spanned domains absent from the comparators, including biomarker-based glycaemic staging, beta-cell function, and social determinants of health. Open-weight MOSAIC matched the proprietary pipeline (closed- vs open-weight weighted kappa = 0.773) and reached moderate agreement with Cooper (kappa = 0.597) and DCSI (kappa = 0.534) and fair agreement with DiSSCo (kappa = 0.320). Agent-based (Type 1) tiers showed significant separation of all-cause mortality (log-rank p < 0.001; crude hazard ratios 1.6-2.4 for non-Baseline tiers), with non-monotonic separation at the upper tiers, and an inverse gradient for incident complications (log-rank p < 0.001) consistent with depletion of susceptibles. Agentic classification also diverged from deterministic execution of the same rubric (MOSAIC Frozen; kappa = 0.428), indicating reasoning beyond fixed rules. Conclusion: MOSAIC shows agentic LLM systems can generate and apply clinically meaningful severity phenotypes from structured EHR data in T2D. Extending it to other diseases with similarly multidimensional severity warrants further research.

---


### 221. [Toward Trustworthy Large Language Model Agents in Healthcare](https://arxiv.org/abs/2607.05055)

**<font color=#1a73e8>作者：</font>** Hadi Hasan, Safaa Salman, Adam Tai Abou Dargham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Healthcare appointment scheduling remains a persistent operational bottleneck, driven by manual coordination, fragmented legacy systems, and high administrative overhead. These inefficiencies constrain provider availability and degrade patient access to care. This paper presents CareConnect, a safety-first conversational agent for healthcare logistics automation that leverages large language model (LLM) function calling, retrieval-augmented generation (RAG), and layered deterministic safety guardrails. The system orchestrates eight domain-specific tools to support appointment booking, modification, cancellation, and facility information retrieval, while enforcing strict scope constraints that prohibit medical advice or diagnosis. Safety-critical situations are handled through deterministic short-circuit mechanisms for emergency detection and medical intent refusal. We evaluate CareConnect on a comprehensive benchmark of 680 task-oriented scenarios spanning end-to-end workflows, multi-turn interactions, and edge cases. Experimental results demonstrate a 91.8% task completion rate with a median per-request latency of 2.2 seconds, 96.0% safety compliance on the dedicated safety-critical evaluation subset, and an average operational cost of $0.0324 per appointment, yielding a significant cost reduction compared to manual human scheduling. These findings show that carefully scoped and rigorously safeguarded LLM-based agents can reliably automate complex healthcare operational workflows while maintaining safety guarantees and achieving substantial cost efficiency. The source code and system implementation are publicly available at this https URL.

---


### 222. [MIRAGE: Defending Long-Form RAG Against Misinformation Pollution](https://arxiv.org/abs/2607.05069)

**<font color=#1a73e8>作者：</font>** Saadeldine Eletter, Ruihong Zeng, Yuxia Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) improves factuality by grounding LLMs in external evidence, but real-world retrieval is often polluted: semantically relevant passages may contain subtle misinformation, misleading framings, or fabrications. We introduce MIRAGE, a training-free, model-agnostic defense for long-form RAG. MIRAGE builds an NLI-based cross-document claim graph and applies a Defended-Claims Gate to either condition generation on a consistent, multi-source supported subset or to block retrieval and answer parametrically. We also release a minimal-edit pollution protocol spanning four perturbation families (Unambiguous, Conflicting, Misleading, Fabricated) to construct matched clean, mixed, and fully polluted evaluation regimes. Across four long-form QA benchmarks and multiple commercial and open-weight LLMs, pollution severely degrades vanilla RAG, while MIRAGE consistently restores factuality under mixed and fully polluted evidence and outperforms prior robust-RAG methods. Our implementation and datasets are available at this https URL.

---


### 223. [TimeThink: Reasoning with Time for Video LLMs](https://arxiv.org/abs/2607.05089)

**<font color=#1a73e8>作者：</font>** Handong Li, Longteng Guo, Zikang Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning requires models to identify and verify temporally localized evidence within long video sequences. Recent Video Large Language Models (Video-LLMs) have shown promising reasoning abilities when aligned with reinforcement learning, yet existing approaches typically rely on outcome-based rewards that supervise only the final prediction. Such supervision provides limited guidance on how models should discover the relevant temporal evidence during intermediate reasoning. In this work, we propose TimeThink, a reinforcement learning framework that explicitly guides temporal evidence discovery in Video-LLMs. Our key idea is to treat temporal clue steps as the fundamental optimization primitive of video reasoning, where each reasoning step references a candidate time interval in the video. We introduce a step-wise temporal process reward that provides localized credit assignment for these clues and a joint process--outcome optimization objective that balances reasoning fidelity with task correctness. To enable scalable training, we construct TimeThink-RFT-20K, a dataset with automatically derived temporal evidence segments. Extensive experiments across video reasoning, temporal grounding, and general video understanding benchmarks show that TimeThink consistently improves both temporal localization and reasoning performance, achieving state-of-the-art results among open-source video RL models.

---


### 224. [Grokking Is Conditional and Fragile: A Fully-Tractable, Multi-Seed Study at 12K Parameters](https://arxiv.org/abs/2607.05104)

**<font color=#1a73e8>作者：</font>** Yoshiyuki Ootani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grokking -- the delayed onset of generalization long after a network has fit its training set - -is usually studied in models too large to read completely and reported from single training runs. We instead study a publicly released ~11,856-parameter Llama-style transformer (Glimmer-1-Base) on modular arithmetic, small enough to enumerate its weights, attention, and full input-output map, and we measure grokking as a multi-seed rate rather than a single outcome. In this fully-tractable regime grokking is a conditional, fragile phase transition. It is gated by training-set coverage, whose threshold tracks output cardinality (the modulus) more than task structure, an ordering that holds above the transition and across a ten-fold change in domain size. Weight decay reproduces the Omnigrok inverted-U at 12K parameters, a positive control on the rate measurement. Grokking also sits on a numerical knife-edge: two perturbations of the floating-point environment -- CPU thread count (reduction order) and CPU-versus-GPU execution -- each flip a minority of same-seed outcomes without a detectable shift in the aggregate rate. Decomposition into sub-task specialists helps chiefly by making coverage cheap rather than by adding supervision. Methodologically, multi-seed control under a fixed numerical environment overturns three dramatic single-run narratives in our own data, each a seed confound. The unit of evidence for grokking must therefore be a multi-seed rate under a pinned numerical environment, checked where possible against a direct reading of the model.

---


### 225. [Rating the Pitch, Not the Product: User Evaluations of LLMs Reflect Expectations More Than Performance](https://arxiv.org/abs/2607.05113)

**<font color=#1a73e8>作者：</font>** Robert Morabito, Tyler McDonald, Charitra Viswanath 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Imagine two users interact with the same LLM. One has been told it is the cutting-edge flagship model; the other, an older, weaker model. They walk away with markedly different ratings of its usefulness and intelligence, yet they used the same model. In a controlled study, 162 participants each used one of six LLMs from two families across three collaborative tasks, after first viewing a landing page that matched, overstated, or understated their model's true capability. This pre-interaction framing shifted user opinions and interaction behavior while task performance did not. Oversold users rated the model more favorably and used more directive prompting, while Undersold users wrote longer, more collaborative prompts. The quality of what users and the model produced together depended only on the model's true capability, not on what users were told. Participants' change in model impressions after use, measured across two impression measures, was not predicted by task performance ($\beta = -0.01$ and $0.11$, both n.s.), but by whether the model met users' expectations ($\beta = 0.47$ and $0.50$, both $p < .001$) and how confident they felt working with it ($\beta = 0.47$ and $0.36$, both $p < .001$). After interaction, users are still rating the pitch, not the product: user-elicited LLM evaluations, including the preference data driving public leaderboards, measure expectation management at least as much as the model itself.

---


### 226. [Localized LoRA-MoE: Block-wise Low-Rank Experts With Adaptive Routing](https://arxiv.org/abs/2607.05114)

**<font color=#1a73e8>作者：</font>** Babak Barazandeh, Subhabrata Majumdar, Vinay Prithyani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) and high-dimensional perception networks increasingly rely on parameter-efficient fine-tuning (PEFT) to adapt to diverse operational contexts. However, standard methods like LoRA are structurally limited by a monolithic bottleneck, making them highly susceptible to gradient warfare. Interleaved multi-task streams may trigger destructive optimization feedback, collapsing adapter weights into unspecialized averages. While recent spatial partitioning methods have introduced block-wise isolation, they remain trapped in static topologies, unable to adapt to dynamic task-switching or environmental sensor failure. In this work, we introduce Localized LoRA-MoE, a unified framework that fuses localized spatial blocking with dynamic, context-conditioned routing. We propose and evaluate two novel architectural paradigms: Block-Wise LoRA-MoE (Centralized Macro-Routing), which modulates the entire structural grid via a monolithic context signal, and Cell-Wise LoRA-MoE (Decentralized Micro-Routing), which empowers every coordinate cell in the matrix grid with autonomous, localized expert gating. Through a comprehensive suite of benchmarks, ranging from high-dimensional SVD matrix simulations and real-world tabular transformations to spatial vision perception under sensor degradation, we demonstrate that both architectures resolve optimization deadlocks inherent in static baselines. Our empirical results establish that decentralized cell-level gating achieves complete statistical parity with an omniscient global coordinator, providing a robust "gradient firewall" that protects surviving pathways from fault-propagated corruption. Our proposals consistently outperform static baselines, offering a scalable and parameter-efficient solution for dynamic model adaptation across granular coordinate fields and shifting operational regimes.

---


### 227. [PDEFlow: Autonomous Agentic PDE Pipelines for Neural Operator Learning and Solver-Free Inference](https://arxiv.org/abs/2607.05134)

**<font color=#1a73e8>作者：</font>** Akshat Jani, Prathamesh Gadekar, Sakhinana Sagar Srinivas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present PDEFlow, an autonomous agentic framework that turns user-level ODE and PDE descriptions into solver-backed neural-operator pipelines. The workflow links problem specification, data generation, operator training, and checkpoint-based inference. A stateful input graph converts multi-turn natural-language input and user edits into validated problem specifications. The data-generation module then samples parameters, solves the configured governing-equation with FEniCSx finite-element backend, and stores the solutions as operator-ready tensors. The training and inference stages use a registry-based interface, allowing different neural operators to be trained and deployed without changing the surrounding pipeline. In the current implementation, we instantiate this interface with a multi-branch Bayesian DeepONet. Experiments on benchmark ODE and PDE tasks show that PDEFlow can construct valid specifications, generate solver-backed datasets, train neural operators across steady and transient problem classes, and provide solver-free predictions from saved checkpoints. The framework is designed for repeatable scientific and engineering workflows where many related physics configurations must be specified, simulated, learned, and queried with minimal manual intervention.

---


### 228. [DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation](https://arxiv.org/abs/2607.05147)

**<font color=#1a73e8>作者：</font>** Xin Cheng, Xingkai Yu, Chenze Shao 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates Large Language Model (LLM) inference by decoupling draft generation from target verification. While recent parallel drafters efficiently propose long token sequences in a single forward pass, they suffer from rapid acceptance decay due to a lack of inter-token dependencies. Furthermore, indiscriminately verifying these extended blocks wastes critical batch capacity on tokens with high rejection risks, severely degrading throughput in high-concurrency serving systems. We introduce DSpark, a speculative decoding framework that unifies high-throughput parallel generation with adaptive, load-aware verification. To maintain draft quality, DSpark utilizes a semi-autoregressive architecture, coupling a parallel backbone with a lightweight sequential module, to introduce intra-block dependency modeling and mitigate suffix decay. To optimize system efficiency, DSpark employs confidence-scheduled verification, dynamically tailoring the verification length for each request based on estimated prefix survival probabilities and engine-specific throughput profiles. On offline benchmarks across diverse domains, DSpark substantially improves the accepted length over state-of-the-art autoregressive and parallel drafters. When deployed within the DeepSeek-V4 serving system under live user traffic, DSpark successfully mitigates verification waste. Compared to the established production baseline (MTP-1), DSpark accelerates per-user generation speeds by 60 to 85 percent at matched throughput levels. More importantly, by preventing severe throughput degradation under strict interactivity constraints, it enables performance tiers that were previously unattainable, shifting the Pareto frontier of our serving system.

---


### 229. [RABBiT: Rapidly adaptive BOLD foundation model via brain-tuning for accurate zero-shot and few-shot prediction of speech-elicited responses in the brain](https://arxiv.org/abs/2607.05171)

**<font color=#1a73e8>作者：</font>** Omer Moussa, Mariya Toneva  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language understanding in the brain is context-dependent, varying across experimental stimuli and individuals, which makes it difficult to build computational models that generalize across both. This calls for a foundation model of language-evoked brain activity that can capture shared structure while adapting efficiently to new participants and inputs. We introduce RABBiT (Rapidly Adaptive BOLD foundation model via BraIn-Tuning), a compact audio-to-fMRI encoder designed for accurate zero- and few-shot prediction. A comprehensive evaluation on 324 participants across multiple unseen fMRI datasets shows that RABBiT enables accurate zero-shot prediction of fMRI responses to natural speech across auditory and language-selective regions, surpassing the SOTA foundation model for fMRI and predictions based on group averages. With as little as 10 minutes of participant-specific data, RABBiT further improves performance via parameter-efficient tuning, substantially outperforming per-participant linear models. RABBiT's performance is driven by two key innovations: (1) learned region-specific attention, and (2) a decomposition of brain responses into shared and subject-specific components, combined with a brain-tuned speech backbone. In addition to supporting strong predictive accuracy, the structured, region-specific representations that RABBiT learns enable interpretability. By eliminating the need for extensive per-participant data and model fitting, RABBiT enables scalable population-level analyses of language in the human brain. We make the code available at this https URL.

---


### 230. [AgentGym2: Benchmarking Large Language Model Agents in De-Idealized Real-World Environments](https://arxiv.org/abs/2607.05174)

**<font color=#1a73e8>作者：</font>** Zhiheng Xi, Dingwen Yang, Jiaqi Liu 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents, i.e., LLM agents, progress rapidly and are increasingly deployed in production environments. This trend underscores the urgent need for rigorous and realistic evaluations. However, most existing benchmarks evaluate agents in simplified, idealized settings. They typically rely on pre-packaged tool interfaces, overlook critical steps, and assume inputs are clean and fully specified. Consequently, they understate the difficulty of real deployments, where uncertainty and noise are ubiquitous and agents must proactively explore the environment to uncover new tools. To bridge this gap, we present AgentGym2, a new evaluation framework with task instances grounded in real-world end-to-end working demands. Beyond reasoning and planning, it measures agents' ability to execute end-to-end procedures, discover tools via exploration, compose tools for unseen tasks, and remain robust to noisy and underspecified information. Experiments on 15 proprietary and open-source models show that even SOTA systems like Gemini and GPT-5 struggle on AgentGym2, revealing a substantial gap between the capability of current agents and the demands of real-world applications.

---


### 231. [Unified Audio Intelligence Without Regressing on Text Intelligence](https://arxiv.org/abs/2607.05196)

**<font color=#1a73e8>作者：</font>** Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architecture enables strong audio-text fusion, seamless multimodal generation, and compatibility with standard LLM training and inference infrastructure. For training, we meticulously curate audio-text datasets comprising 157.4B audio tokens and 320.5B text tokens. We apply multi-stage supervised training on these datasets, followed by text-only Cascade RL and multi-domain on-policy distillation. Audex delivers state-of-the-art audio understanding, speech recognition and translation, text-to-speech, audio generation, and speech-to-speech generation, while preserving very compelling reasoning, alignment, knowledge, long-context, and agentic capabilities of its text-only LLM backbone with marginal or no regression. We release the model checkpoints to facilitate open research.

---


### 232. [Reason, Reward, Refine: Step-Level Errors Corrections with Structured Feedback for Physics Reasoning in Small Language Models](https://arxiv.org/abs/2607.05199)

**<font color=#1a73e8>作者：</font>** Raj Jaiswal, Dhruv Jain, Rishabh Dhawan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Physics reasoning fails structurally in small language models: an error at any step propagates forward, corrupting every inference that follows. Limited domain knowledge, hallucination under multi-step derivation, and distributional sensitivity compound this failure. We propose a step-level reward framework that identifies the first reasoning error, generates targeted structured feedback, and trains the model to revise its solution via policy gradient with KL regularization, without exposing it to ground truth solutions as generation targets. Unlike annotation-dependent step-level methods, no preference data construction is required and the external verifier operates exclusively at training time. Across five physics benchmarks, our framework delivers accuracy gains of 17-20% over CoT prompting and 10-16% over the strongest baseline, reduces calculation errors from 56.9% to 23.5%, and reduces miscomprehension errors from 22.3% to 12.0% in the best observed cases. Conceptual errors reduce from 89.7% to 68.7%, yet persist as the hardest failure mode across all conditions.

---


### 233. [A Multimodal Reasoning Typology for Grounding Chart-Image Coherence in Science Communication](https://arxiv.org/abs/2607.05222)

**<font color=#1a73e8>作者：</font>** Avina Nakarmi, Sohom Sen, Xun Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Charts and images appear together throughout scientific publications, yet most computational work does not characterize their coherence. We argue that a chart, its accompanying image, and the caption that links them form a multimodal unit, and that the inferential work required to read it varies systematically. To capture this variation, we develop a typology of reasoning gaps, R1 through R5, that characterizes how chart, image, and text jointly convey a scientific claim, and the interpretive work this demands of the reader. Some pairs restate the same data, while in other pairs, charts are used to quantify a structure the image localizes, project image content onto an external variable, audit an image-based claim, or jointly construct a frame that neither panel can establish alone. The typology is anchored in the grounding theory of communication and was derived bottom-up, with a neuroscience expert, from a corpus of 79 traumatic brain injury papers and 32 chart-image pairs. Crucially, the levels provide a systematic mechanism for identifying where grounding succeeds or breaks down, rather than leaving it to subjective inference. We show this in a study in which a domain expert and three non-experts judge vision-language model (VLM) descriptions of 25 pairs: the level predicts where their judgments align and where they diverge, isolating the points at which contextual knowledge, not the figure, carries coherence. This typology thus offers figure designers a systematic way to balance text against chart-image pairs, bridging the expert-to-non-expert divide in reading a scientific takeaway.

---


### 234. [MoP-JEPA: Hard-Assigned Predictor Mixtures for Stochastic JEPA World Models](https://arxiv.org/abs/2607.05238)

**<font color=#1a73e8>作者：</font>** Zhi Song, Ximing Xing, Zhenchao Tang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> JEPA world models predict the next latent state with a single deterministic predictor trained by latent regression. We show that this fails structurally when the environment is stochastic: at a branching transition, the regression-optimal predictor outputs the conditional mean of the successor embeddings, a point between the true next states that corresponds to no state at all. We prove this collapse for deterministic and gated mixture-of-experts predictors, and prove that MoP-JEPA's hard-assigned predictors converge instead to a quantizer of the transition distribution: one head per successor mode, enumerable in a single forward pass, which is the interface a planner consumes. On official OGBench offline data with leak-free evaluation, planning over single-predictor rollouts performs poorly ($0.02$--$0.09$ success) while planning over our predicted modes reaches up to $0.85$, ahead of deterministic, gated-MoE, and variational predictors on every task. Because multi-prediction evaluation invites coverage freeloading, a verification protocol is part of the method: an input-agnostic codebook control, a shuffled-context test, router-gated readouts, transition-precision guards, and a verified-route criterion in which the model proposes its transition graph blind and ground truth is used only to check the result. Under this criterion our method outperforms the strongest soft alternative on all three mazes ($2$--$5\times$), and the protocol identifies the remaining gap in that baseline's raw scores as routes through predicted transitions that do not exist. The same model executes in the real environment, placing second of seven against the published OGBench baselines on the hardest maze. Multimodal dynamics decide whether a JEPA world model can plan at all; a mixture of predictors with hard assignment is a minimal and verifiable fix.

---


### 235. [SteelBench: Evaluating Vision-Language Models in Real-World Industrial Environments](https://arxiv.org/abs/2607.05264)

**<font color=#1a73e8>作者：</font>** Suryanarayana Reddy Yarrabothula, Manisha Chawla, Kunal Sinha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing video benchmarks evaluate action recognition on consumer videos, egocentric recordings, or simulated industrial environments. They do not test vision-language models under the visual and procedural conditions of real industrial CCTV, where workers appear as distant figures amid dust, steam, low light, glare, occlusion, and overlapping activities. We introduce STEELBENCH, a diagnostic benchmark for industrial surveillance that jointly evaluates per-worker activity recognition, safety-rule reasoning, and annotation provenance. SteelBench contains 1,345 densely annotated clips, curated from 149 hours of operational plant footage and 10,024 candidate clips using temporal deduplication, class balancing, and visibility-aware stratified sampling. Each clip includes dense per-worker action labels, PPE attributes, spatial context, and safety-rule annotations. Because model-assisted annotation can shape the labels later used for model evaluation, SteelBench includes a provenance-aware audit protocol. The protocol measures label influence, evaluates sensitivity to ground-truth provenance, and reports a human reference from expert-reviewed labels. Applying this audit, we find that unaudited VLM-sourced ground truth can inflate same-family model accuracy by up to 17 percentage points. Across nine VLMs from four architectural families, the best model reaches only 42.6% action accuracy, compared with an 84.6% human benchmark. Performance also fragments across recognition, robustness, calibration, and safety reasoning. Even when models predict the correct action, 37-58% of cases still yield incorrect safety judgments, and no model passes more than 2 of 5 diagnostic checks. The dataset is publicly available on Hugging Face.

---


### 236. [Is the Geometry Doing the Work? An Operating-Point Audit of Hierarchy in Hyperbolic Vision-Language Models](https://arxiv.org/abs/2607.05268)

**<font color=#1a73e8>作者：</font>** Jaeyoung Kim, Eunseok Kim, Dongsuk Jang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Whether a hyperbolic representation model uses its geometry cannot be read off its curvature parameter: what matters is the dimensionless operating point $\sqrt{c}\rho$ and whether the radial and cone machinery is active there. We develop a battery of necessary-condition diagnostics and audit three published hyperbolic vision-language families -- MERU, HyCoCLIP, and PHyCLIP -- across released checkpoints and controlled interventions on a fixed GRIT snapshot, identifying three failure modes. First, curvature is not an active resource: the operating point stays near-Euclidean ($H(u)\approx 1$; no audited converged checkpoint reaches $\sqrt{c}\rho>1$), and releasing the curvature floor moves curvature and norms but keeps the operating point near-Euclidean, without substantial downstream degradation. Second, the cone and traversal machinery is measured inoperative: entailment cones are inactive, saturated, or misaligned, and graded traversal fails under controlled readouts, while directed radial depth is a bounded non-detection above shuffle-null controls at quantified sensitivity; the one surviving native-relation residual remains non-operative. Third, hierarchy-looking evaluations are underdetermined: taxonomy correlations are carried by angular distance, and coarse-retrieval gains track box/compositional supervision, not curvature. A mechanistic account explains why: the entailment objective admits a low-curvature, wide-cone shortcut, and a parameter-free aperture identity (cones saturate iff $\sqrt{c}\rho\le 2K$) locates the edge where every entailment-trained unclamped run settles; entailment-off runs show no arrest there. The shortcut is the dominant accelerator of collapse, not its sole cause. These formulations, as released, do not instantiate the radial/cone mechanism their geometry motivates; we distill the audit into a five-number geometry report for future hierarchy claims.

---


### 237. [ChatImage: Navigating Long-Form LLM Answers through Interactive Images](https://arxiv.org/abs/2607.05290)

**<font color=#1a73e8>作者：</font>** Wencan Jiang, Jiangning Zhang, Yong Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can produce detailed answers to complex queries, but these answers are typically presented as dense linear text, which makes fine-grained inspection, navigation, and return visits difficult. We present ChatImage, a system that converts long-form LLM answers into interactive visual images. Given a textual answer, ChatImage first normalizes its content into structured visual modules, plans a visual layout, and renders a coherent image. It then applies a second grounding pass to the rendered image with vision grounding models such as LocateAnything and MiMo-Vision, with optional SAM-style mask refinement, to identify the visible regions that should support interaction. From these grounded regions, ChatImage overlays transparent clickable hotspots on the image. Each hotspot opens a detail panel and a region-scoped follow-up thread, allowing the user to inspect and query a specific part of the answer without re-reading the full response. Instead of treating planned coordinates as the final interaction geometry, ChatImage uses them as priors and grounds the interaction targets after rendering, which improves consistency between visual content and clickable regions. We release a reference implementation and introduce a 30-question benchmark covering infographic, map, and scene-based answer formats. Evaluation with configured external models reports interaction-loop completion, a strict visual-alignment gate, and a SAM-based mask-completeness diagnostic.

---


### 238. [MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale Meta-Skill Evolution](https://arxiv.org/abs/2607.05297)

**<font color=#1a73e8>作者：</font>** Zefeng Wang, Minxi Yan, Jinhe Bi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent LLM agents tackle increasingly long-horizon, open-ended tasks, and external skills, reusable procedural knowledge supplied to the agent, further extend this capability. However, a fixed, hand-authored skill is rarely optimal, and cannot adapt to the diversity of tasks an agent encounters. Self-improving agents address this by rewriting their own skill files from execution traces, yielding meaningful gains on challenging benchmarks. Yet such self-evolution remains non-recursive: it improves only the task skill (what the agent does) while the improvement procedure (how it improves) is authored once and held fixed. We introduce MetaSkill-Evolve, a two-timescale framework that makes agentic skill improvement recursive: every branch carries both a task skill $s$ and a branch-local meta-skill $m=(\psi,\sigma,\alpha,\pi,\varepsilon)$ whose five components parameterise the Analyzer, Retriever, Allocator, Proposer, and Evolver agents of the improvement pipeline. Task skills evolve on a fast loop while the meta-skill evolves on a slower one under the same pipeline applied to itself, with no additional model or objective. With all five pipeline agents sharing a single frozen backbone, MetaSkill-Evolve outperforms no-skill, static-skill, and single-level evolution baselines on three agentic benchmarks (OfficeQA, SealQA, ALFWorld), improving held-out test accuracy over the raw backbone by +23.54, +16.09, and +1.92 points respectively.

---


### 239. [Learning Only What Valid Adapters Can Express: Subspace-Constrained Adaptation Against Fine-Tuning Poisoning](https://arxiv.org/abs/2607.05300)

**<font color=#1a73e8>作者：</font>** Fabien Polly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient fine-tuning still leaves a broad space of behavior-changing updates reachable, so a poisoned objective can be represented and optimized. We study an alternative: adaptation constrained to the subspace estimated from a trusted pool of existing task adapters. On flan-t5-large with 196 public LoRA adapters, we show that (1) the functionally relevant content of an adapter lies in a low-dimensional shared subspace, 30 to 38 percent of its weight norm being redundant under the evaluated task distributions; (2) gradient adaptation restricted to 128 coordinates on this subspace matches full LoRA fine-tuning on clean classification data, while under targeted label inversion LoRA collapses to 3-26 percent exact match and the constrained learner keeps 62-96 percent on the tasks the pool covers; (3) the constrained learner cannot fit corrupted data, its adaptation loss separating clean from garbage by two orders of magnitude (120x), an out-of-distribution signal without an extra detector; and (4) against an adaptive backdoor attacker who optimizes within the subspace, the attack is blocked (8 percent success versus 100 for LoRA) on the task where its target behavior is unlike anything in the pool, and only partially blocked (85 percent) when the target coincides with a common pool behavior. On these two tasks the outcome is consistent with how close the target is to the pool's directions, which suggests but does not establish a pool-relative boundary. The mechanism trades peak plasticity for these properties: on tasks the pool covers poorly, unconstrained fine-tuning wins, and the protection assumes the pool itself is trusted. Code and data are public.

---


### 240. [Evaluating and Understanding Model Editing for Medical Vision Language Models](https://arxiv.org/abs/2607.05310)

**<font color=#1a73e8>作者：</font>** Guli Zhu, Chenwei Wu, Liyue Shen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model editing promises a fast, targeted way to correct post-deployment mistakes in medical vision-language models (VLMs) without costly retraining. However, existing multimodal model editing benchmarks focus on general-purpose tasks and do not reflect realistic clinical domain requirements and variability. To address this, we introduce M3Bench, a clinically grounded benchmark for multimodal model editing that evaluates whether an edit remains reliable, precise, and generalizable under the challenges of image and text variation, modality and protocol shifts, clinical knowledge composition, and temporal progression. M3Bench contains 16,276 questions spanning diverse anatomy, modalities, and specialties, and supports both single and sequential edits.
By evaluating 4 representative editors across 6 medical and general VLMs, we find that no method excels across all criteria. Gradient-based editors achieve strong transfer but suffer from catastrophic locality violations, whereas memory-based methods preserve locality but lack compositional generality and exhibit high backbone-dependent hyperparameter sensitivity. We further attribute these failures to the latent space geometry of VLMs and how different editing methods shift its landscape. Overall, M3Bench establishes a rigorous clinical stress test for multimodal model editing and offers actionable guidance for safer post-deployment adaptation. The benchmark is publicly available at this https URL .

---


### 241. [Deep Learning for Semen Analysis in Male Infertility: Computer Vision, Multimodal Fusion, and Clinical Translation](https://arxiv.org/abs/2607.05311)

**<font color=#1a73e8>作者：</font>** Runwei Guan, Shaofeng Liang, Jiacheng Weng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Male infertility contributes substantially to the global infertility burden, and sperm analysis remains central to diagnosis, treatment planning, and assisted reproductive technology. Conventional semen evaluation, however, is labor-intensive, operator-dependent, and limited by inter- and intra-observer variability, motivating the development of objective and reproducible computational approaches. This review provides a comprehensive and perspective-oriented synthesis of artificial intelligence-driven sperm analysis, with a focus on computer vision, deep learning, multimodal fusion, robustness, and clinical translation. We first review task-specific methods for sperm detection and counting, tracking-based motility assessment, semantic and instance segmentation, morphology and defect classification, functional assessment, and genetic integrity evaluation. We then summarize public datasets, benchmarks, evaluation metrics, and emerging multimodal strategies that integrate microscopic images, time-lapse videos, CASA-derived parameters, DNA integrity assays, and clinical metadata. Beyond algorithmic performance, we discuss key barriers to real-world deployment, including data scarcity, cross-center domain shift, annotation inconsistency, interpretability, uncertainty calibration, privacy-preserving learning, and workflow integration. Finally, we outline a staged clinical translation roadmap spanning technical standardization, multicenter retrospective validation, silent prospective evaluation, human-in-the-loop clinical testing, ART outcome validation, regulatory approval, and post-market monitoring. By organizing the field from task-specific visual recognition to trustworthy multimodal reproductive intelligence, this review highlights both the progress and the unresolved challenges required to translate AI-driven sperm analysis into clinically meaningful decision support.

---


### 242. [How Much is Left? LLMs Linearly Encode Their Remaining Output Length](https://arxiv.org/abs/2607.05316)

**<font color=#1a73e8>作者：</font>** Mohamed Amine Merzouk, Dmitri Carpov, Mirko Bronzi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models generate one token at a time, yet their responses show remarkably consistent length structure: step-by-step solutions converge in predictable token counts, retrievals stop after a few sentences, retractions extend responses by measurable amounts. We ask whether the model carries an internal estimate of how much response remains. Training minimal-capacity linear probes on frozen hidden states of three open-weight 7-8B models across seven completion-style datasets, we find three converging pieces of evidence. First, total response length is linearly decodable from the prompt's last hidden state alone, before any output is emitted. Second, probe directions trained on natural-language datasets transfer broadly, including to controlled synthetic completions never seen in training, outperforming a statistical baseline; the converse direction generally fails, and this asymmetry is itself informative. Third, on curated high-loss completions, the probe's per-position estimate shifts upward at the moment the model retracts and restarts a partial solution, a directional behavior no position-only predictor can reproduce (qualitative, not aggregate). We frame this as approximate estimation of remaining generation length, distinct from exact-counting impossibility results for transformers, and interpret it as evidence that LLMs maintain a plan-like internal representation of output length (decodable, not necessarily used causally).

---


### 243. [PiSAs: Benchmarking Contextual Integrity in Multi-User Agentic Systems](https://arxiv.org/abs/2607.05318)

**<font color=#1a73e8>作者：</font>** Shubham Gupta, Nazanin Mohammadi Sepahvand, Abhinav Kumar 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As LLM agents evolve from single-user assistants into shared organizational infrastructure, new privacy risks emerge: inappropriate information may not only be exposed through outputs for external recipients, but also internally across users through inter-agent messages, shared memory and agents. These data spillage risks are not captured by existing privacy benchmarks grounded in contextual integrity (CI) as they focus primarily on either single-user settings or interactions between independently owned agents. We introducePiSAs (Privacy in Shared Agentic systems), a benchmark for assessing unintentional leaks with dual CI annotations: whether an information is appropriate for the task, and which users may legitimately access it. This enables direct measurement of cross-user spillage across agentic system components and interfaces, such as outputs, inter-agent communication, and memory. PiSAsis system-agnostic and supports evaluation across different agent topologies and memory regimes. We find that, although system design improves CI compliance, results are bottlenecked by incorrect LLM judgment calls: even state-of-the-art models fail to reliably filter inappropriate content or restrict transmission to authorized users. Our findings underscore the need for privacy-preserving strategies, beyond those studied in this work.

---


### 244. [Multiplayer Interactive World Models with Representation Autoencoders](https://arxiv.org/abs/2607.05352)

**<font color=#1a73e8>作者：</font>** Anthony Hu, Václav Volhejn, Adrien Ramanana Rahary 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce the first multiplayer world model for highly dynamic environments governed by complex physical interactions. Whereas single-player world models treat the other agents as part of the environment, ours conditions on the action streams of multiple agents, learning to attribute changes in the scene to the correct player and to stay coherent under arbitrary combinations of their actions. We study this problem in the game of Rocket League, where players compete and cooperate under fast, tightly coupled dynamics. Trained on 10,000 hours of gameplay collected with publicly available bots, our 5-billion-parameter latent diffusion model generates four-player matches in real time, producing 20 frames per second on a single Nvidia B200 GPU. Although trained only on short clips, its rollouts stay stable far beyond the training horizon: distributional quality holds steady out to five minutes, the longest horizon we measure, and in practice we observe rollouts continuing for hours with no sign of collapse. We systematically investigate the central design choices: the video codec, the generative objective, and the multiplayer conditioning scheme. In addition, we characterize how behavior changes with model and data scale, including the capabilities that emerge and the failure modes that persist. We further develop targeted evaluations that probe the model's physical understanding rather than visual appearance alone. To support continued research on multiplayer world models, we release our dataset, our full training and inference codebase, and a live demo.

---


### 245. [REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing](https://arxiv.org/abs/2607.05364)

**<font color=#1a73e8>作者：</font>** Cheng-Kang Chou, Ming-To Chuang, Ke-Han Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern autoregressive ASR systems can emit timestamps as decoded tokens, enabling timestamped transcription without frame-level aligners or inference-time post-processing. We show that these generated timestamps can drift across long non-speech spans: the transcript may remain plausible, but the decoded time axis drifts away from the audio. We study this non-speech-induced timestamp drift with self-built gap and long-gap benchmarks across 15 evaluated timestamp-producing ASR and audio-language systems. Naive timestamp-corrected fine-tuning improves alignment but can severely degrade non-target ASR behavior, exposing a forgetting problem. We propose REDDIT(REplay-based Distribution eDITing), a lightweight two-stage post-training framework that corrects timestamps while avoiding this catastrophic forgetting: it first edits timestamp targets under the model's own replayed decoder context while matching the frozen base distribution on non-timestamp tokens, then applies a short edited-prefix refinement stage. In this framework, we construct correction supervision without human transcripts or human timestamp annotations by combining VAD-trimmed speech spans with inserted non-speech gaps and known concatenation offsets. On Whisper-tiny, 34.9 hours of targeted correction audio used and only 1.6% of model parameters updated, raising long-gap mIoU from 38.7% to 95.0% and reducing mixed-gap out-of-domain AAS from 2752 ms to 223 ms while preserving CV-en MER at 41.3% (versus 524.2% for ordinary SFT decoder tuning).

---


### 246. [SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech Language Models](https://arxiv.org/abs/2607.05365)

**<font color=#1a73e8>作者：</font>** Thomas Thebaud, Yuzhe Wang, Hao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Streaming speech-to-speech language models aim to answer spoken queries directly with synthetic speech. However, standard speech and text benchmarks do not capture whether these systems behave naturally in conversations, where timing, turn-taking, prosody, interpersonal stance, language and dialect consistency, and relationship-aware appropriateness jointly shape perceived quality. We introduce SPEARBench, a benchmark for evaluating naturalness in speech-to-speech language models from question-answer interactions. SPEARBench constructs controlled dialogue prompts from the Seamless Interaction corpus, runs inference across multiple models, and evaluates generated answers using a multidimensional protocol that covers response latency, interruptions, speech quality, ASR robustness, language and dialect consistency, emotional naturalness, interpersonal stance, and explainable distributional baselines. The benchmark includes original human answers as a reference condition and reports results for several contemporary models. Results show that current models can achieve high signal-level quality and low ASR error while still differing from human conversational behavior in latency, overlap, dialect preservation, emotional adaptation, and interpersonal stance dynamics.

---


### 247. [Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic Visual Generation](https://arxiv.org/abs/2607.05382)

**<font color=#1a73e8>作者：</font>** Haozhe Wang, Weijia Feng, Jinpeng Yu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual generators excel at rendering, but they confidently fabricate what they do not know. User requests are unbounded, evolving, and deeply long-tailed: new characters, trending entities, post-cutoff events, and more. This world-knowledge bottleneck is structural: generators are trained on fixed corpora, but the visual world is open-ended. We construct SearchGen-20K and SearchGen-Bench, with 20,839 prompts spanning twelve failure categories and twenty-two domains, paired with a pre-executed multimodal SearchGen-Corpus-1M to support offline, reproducible research. On SearchGen-Bench, frontier open generators score only 21 to 28 out of 100, a 40-point collapse invisible to existing benchmarks. The natural remedy is to employ search tools, enabling agentic visual generation. However, we find that naive search fails: it retrieves indiscriminately, injecting noise into prompts the generator already handles. We trace the root cause to a generator-specific, evolving knowledge boundary: the divide between what a generator can internalize through training and what must remain in external context. Although this boundary is hard to specify in advance, we show that it is discoverable through a teach-then-search co-training framework. Even a minimal version of this co-training recipe produces monotonic improvement, laying the foundation for recursive self-improvement in visual generation that can meet world-knowledge-grounded requests. We release the full dataset, co-training corpus, and search corpus as a replayable harness for tool-augmented, world-knowledge-grounded visual generation.

---


### 248. [LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391)

**<font color=#1a73e8>作者：</font>** Jacky Kwok, Shulu Li, Pranav Atreya 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling pre-training, post-training, and test-time compute have become the central paradigms for improving the capabilities of LLMs. In this work, we identify verification, the ability to determine the correctness of a solution, as a new scaling axis. To unlock this and demonstrate its effectiveness, we introduce LLM-as-a-Verifier, a general-purpose verification framework that provides fine-grained feedback for agentic tasks without requiring additional training. Unlike standard LM judges that prompt LLMs to produce discrete scores for candidate solutions, LLM-as-a-Verifier computes the expectation over the distribution of scoring token logits to generate continuous scores. This probabilistic formulation enables verification to scale along multiple dimensions: (1) score granularity, (2) repeated evaluation, and (3) criteria decomposition. In particular, we show that scaling the scoring granularity leads to better separation between positive and negative solutions, resulting in more calibrated comparisons. Moreover, scaling repeated evaluation and criteria decomposition consistently lead to additional gains in verification accuracy through variance and complexity reduction. We further introduce a cost-efficient ranking algorithm for selecting the best solution among candidates using the verifier's continuous scores. LLM-as-a-Verifier achieves state-of-the-art performance on Terminal-Bench V2 (86.5%), SWE-Bench Verified (78.2%), RoboRewardBench (87.4%), and MedAgentBench (73.3%). Beyond verification, the fine-grained signals from LLM-as-a-Verifier can also serve as a proxy for estimating task progress. We build an extension for Claude Code, enabling developers to monitor and improve their own agentic systems. Finally, we show that LLM-as-a-Verifier can provide dense feedback for RL, improving the sample efficiency of SAC and GRPO on robotics and mathematical reasoning benchmarks.

---


> [!TIP]
> 当前位于：**201-248**（第 5/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-248**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
