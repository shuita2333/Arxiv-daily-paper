# 🧠 大模型相关研究 | 2026年10月06日

> 本类共 **261** 篇论文：已确认 **243** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-261**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-261**

---

### 251. [MetaRubric: Learning to Reward for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2610.02824)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuxuan Fan, Jaehong Yoon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning extends reward-driven optimization to open-ended tasks by assigning partial credit to individual response requirements. However, rubric judges can assign a high criterion score even when the information or action it requires is absent from the response, a failure mode we term Vacuous Credit. Such awards persist after the required information is removed and can reverse the sign of a response's GRPO advantage. To address this problem, we introduce MetaRubric, which alternates evidence-aware policy optimization with response-guided rubric adaptation. We construct counterfactual counterparts by changing one task-relevant fact in each prompt. During policy optimization, credit is assigned only when the response contains sufficient evidence to satisfy the required rubric criterion. After each policy-optimization stage, current policy responses guide revisions to original and counterfactual criteria while preserving the meaning of the original prompt's initial rubric as interpreted under each prompt's facts. We also adapt criterion weights at stage boundaries to better address observed policy errors. Across multiple backbones, MetaRubric improves PubMedQA accuracy by 6.00--20.40 percentage points over static-judge GRPO, with further gains on HealthBench-Hard and two multimodal medical benchmarks.

---


### 252. [Toward Omni Multimodal Graph Foundation Model: A Topology-Driven Binding Approach](https://arxiv.org/abs/2610.02881)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xunkai Li, Chenxi Wan, Yinlin Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal graph foundation models (MGFMs) seek to learn generalizable representations from large-scale graphs with heterogeneous node modalities. However, real-world Multimodal-Attributed Graphs (MAGs) often contain incomplete node attributes, limiting the scale and diversity of available pretraining corpora. Besides, existing MGFMs primarily incorporate graph topology as structural context, overlooking its role in guiding multimodal binding and shaping a unified representation space. To address these challenges, we propose GraphBind, a topology-driven approach that uses graph topology to bind rich modality information into a unified shared space. GraphBind is motivated by the stability of graph topology, which provides structural references and complementary semantic information for multimodal binding. Concretely, GraphBind uses topology to organize self semantics and reliable neighborhood semantics into a global shared space that integrates structure and semantics, and adapts this space to discriminative and generative tasks through lightweight interfaces. Extensive experiments against 11 representative baselines demonstrate that GraphBind achieves leading performance on both discriminative and generative tasks, with relative improvements of up to 28.1% over the strongest baseline.

---


### 253. [Custom Forcing: Training-Free Subject Customization for Autoregressive Video Generation](https://arxiv.org/abs/2610.02914)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yunseung Ok, Hyunsoo Kim, Minseo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive video models can generate minute-long videos in real time, but they produce generic subjects from text rather than specific subjects from user-provided images. Existing customization methods either require costly per-subject optimization or use pretrained conditioning networks that jointly process all video frames with bidirectional attention. Neither approach is designed for causal streaming. We present Custom Forcing, a training-free method that stores reference-based anchor frames in the persistent KV cache of a frozen autoregressive video model. However, fixed anchors face two limitations: simple conditioning allows identity to drift, and the text prompt continues to favor a generic subject. To address these problems, drift-adaptive value amplification (DVA) scales reference influence with the degree of identity drift, while anchor contrast guidance (ACG) steers generation away from the generic class prior. Over two-minute rollouts, fixed anchors fall from 0.58 to 0.42 in DINO-I, while Custom Forcing keeps it between 0.58 and 0.62 without reducing motion. Custom Forcing also achieves higher subject similarity than bidirectional customization methods and better preserves identity over 30s than causal image-to-video and reference-to-video models, while generating each frame 9.5--28.5 times faster than these long-video baselines.

---


### 254. [SecJev: Bringing Security Expertise to System One Decision Models](https://arxiv.org/abs/2610.03073)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zheng Chen, Fei Yu, Haohao Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security workflows need models that turn complex observations and explicit policies into decisions. System One models introduced by Jev return typed predictions and probabilities; security specialization supplies the domain expertise behind those predictions. We introduce SecJev, to our knowledge the first family of Jev-like decision models specialized for security, spanning 0.8B to 9B parameters. Built on Kev's single-pass candidate scorer, SecJev learns Boolean, choice, and ordered decisions from text, telemetry, and observation histories. We develop SecJev-Corpus to unify source-label prediction and explicit-policy evaluation across 14 tasks and eight sources. It covers tool outputs, traffic, federated updates, consensus, authentication, and vehicle messages. Scene-weighted training adapts the models across these domains while preserving a shared typed decision interface. Security specialization improves every model in the family; SecJev-0.8B outperforms general Kev-9B by 20.51 percentage points in task-macro accuracy. Comparisons with answer-only generative fine-tuning show close accuracy and latency with lower peak inference memory. Tests on new source groups reproduce gains over Kev in prompt-injection and traffic decisions, with capture-dependent false alarms. We release adapters, decision heads, SecJev-Corpus, and training and inference code.

---


### 255. [Zephon: Elastic Determinism for Online, Stateful Foundation Model Data Loading Pipelines](https://arxiv.org/abs/2610.03087)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Maximilian Böther, Josh Wills, Ties Robroek 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deterministic data loading is important for foundation model development: model researchers need confidence that differences they observe across costly ablations are caused by the parameter they changed rather than non-determinism in the training data sequence. The data loader must provide elastic determinism, i.e., a deterministic sequence of global training data batches despite changes to the GPU topology across runs (e.g., due to GPU scarcity), frequent checkpoint-resume cycles, and different data processing execution backends. Achieving this is difficult because modern foundation model data pipelines tokenize, pack, and mix samples online, introducing stateful n-to-m transformations that break sample indexing. Existing data loaders largely assume indexable 1-to-1 pipelines, and the common workaround of offline materialization is expensive and, for some modalities such as video, infeasible.
We present Zephon, a data loader for foundation models that supports online, stateful pipelines while providing elastic determinism and efficient resumption from checkpoints. It partitions the global stream into topology-independent lanes, serializes ordering decisions while parallelizing stateless work on interchangeable backends, and checkpoints only bounded in-flight state so recovery cost does not grow with training progress. We evaluate Zephon on text and vision-language workloads and show that it achieves competitive throughput while providing a combination of guarantees that no existing loader offers for online, stateful pipelines.

---


### 256. [Hindsight-Guided Rationale Distillation for Rare Disease Diagnosis](https://arxiv.org/abs/2610.03176)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Aarav Singh, Animesh Pathak, Navyansh Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study hindsight-guided distillation for rare disease diagnosis on ZebraMap: a 1.5B student is fine-tuned on chain-of-thought traces from a 8B teacher that observes the ground-truth diagnosis during generation. Absolute accuracy remains low for all models - the task is hard at this scale - but within this ceiling a filtered variant (StudentF) achieves a small, statistically significant accuracy advantage over the teacher (p < 0.001), concentrated in better-represented diseases. The unfiltered student does not significantly outperform the teacher (p = 0.129), establishing that contamination filtering - not hindsight distillation alone - drives the gain. The gap traces to an artifact we term GT hallucination. Label-visible generation causes the teacher to embed "ground truth is X" phrases in its reasoning chain; SFT copies the pattern. At inference, the unfiltered student reproduces the phrase in 33.9% of cases, with severe accuracy degradation when the hallucinated label is wrong. A regex filter removing these slots reduces contamination to near-zero, producing the observed gain - though the effect remains small. We precisely quantify this gain-cost tradeoff, document frequency-dependent knowledge transfer absent from the RL-trained teacher, and characterize a calibration gap that SFT does not close - identifying both as directions for future work.

---


### 257. [SCAD: Structured Credit Assignment and Distillation for Long-Horizon Agents](https://arxiv.org/abs/2610.03372)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Shangyang Wu, Shuai Zhao, Ziyue Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training long-horizon agents to solve complex tasks requires effective supervision over extended interaction sequences. However, sparse terminal rewards obscure intermediate contributions, while on-policy distillation can lose informative teacher guidance as student-generated histories grow. To address this problem, we introduce SCAD, which organizes interactions into planning and bounded subtask execution, distills execution in local contexts, and refines planning credit through cross-rollout subtask prefix trees, with planning receiving full terminal credit and execution receiving positive terminal credit and teacher guidance. Across all evaluated benchmarks, SCAD improves macro-average accuracy over the strongest training baseline by 4.48 percentage points for text tasks and 4.19 points for multimodal tasks. SCAD effectively combines outcome-based credit assignment with teacher-guided distillation to improve planning and execution in long-horizon agents.

---


### 258. [CorrectGuard: Eyes-Off Correctness Estimation for Black-Box Security Guardrails](https://arxiv.org/abs/2610.03470)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Adam Faulkner, Nil-Jana Akpinar, Matthew Dressman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI services increasingly rely on black-box security guardrails, yet privacy-preserving model auditing regimes often cannot measure how well these systems perform in both a human eyes-off production setting, which disallows human inspection of user input, and a machine eyes-off setting, which disallows model inspection of such input. We introduce CorrectGuard, an eyes-off correctness estimation framework for both settings, which involves an independent model-based evaluator predicting whether guardrail decisions on human- and machine-inaccessible inputs are correct using only labeled eyes-on data and without access to the guardrail's internals. We evaluate in-context learning, embedding, and finetuning-based correctness models under leave-one-dataset-out evaluation across 13 safety and security datasets spanning harmful content, jailbreaks, prompt injection, and extraction, and across open-weight guardrails treated uniformly as black boxes. Across both human and machine eyes-off settings (the latter implemented using privacy-preserving fingerprinting of inputs), in-context-learning-based correctness classifiers substantially improve error identification across guardrails, achieving up to a 25 percentage-point increase in macro accuracy, as do finetuning-based approaches which provide a nearly 15-point boost, although performance varies sharply across guardrails and held-out datasets. Correctness scores also support guardrail decision ranking and abstention: across 3 guardrails, the best correctness rankings reduce AURC from unranked baselines of 0.33-0.44 to 0.17-0.22, while the best operating points retain 37.5-52.0% of guardrail decisions at 15% observed risk. These results show that external correctness models can expose systematic failures and support guardrail decision abstention without privileged access to the guardrail.

---


### 259. [ZeroMAG: Zero-Shot Multimodal Adapter Generation for Plug-and-Play EEG Foundation Models](https://arxiv.org/abs/2610.03546)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yubo Wang, Jingying Ma, Xinliang Zhou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models (EFMs) capture reusable knowledge from large-scale EEG data, while many EEG recordings also include companion physiological signals that provide complementary information beyond the EEG-only interface. The challenge is to preserve this pretrained knowledge while extending the EFM to heterogeneous multimodal recordings through an adaptation inferred from unlabeled target data. We introduce ZeroMAG, a zero-shot multimodal adapter generation framework that extends a frozen EEG encoder and prediction head using unlabeled target recordings, without target labels or target-side optimization. The target datasets are held out from all model training and selection in the ZeroMAG pipeline. ZeroMAG organizes companion modalities around a configuration-invariant adapter, constructs a modality-subject-task condition from unlabeled recordings and task context, and generates adapter weights in a function-constrained latent space learned from source adapters. Across six held-out target datasets and three EFM backbones, ZeroMAG improves balanced accuracy by 7.22 percentage points over EEG-only inference and 4.89 points over direct weight regression, while coming within 0.50 points of supervised multimodal adaptation on average. Ablations further show that removing functional supervision from either representation learning or conditional generation degrades generated-adapter performance, confirming the contribution of both components.

---


### 260. [Recursive Harness Self-Improvement for Frontier Reasoning Data Synthesis](https://arxiv.org/abs/2610.03548)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Wenlong Zhang, Zhengbo Jiao, Chenxu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generating progressively harder reasoning problems requires synthesis procedures that adapt as the task distribution evolves. Existing task-level recursion reuses generated problems as seeds but leaves the construction harness unchanged. We present task-harness co-evolution, a framework for recursive harness self-improvement (RSI) in reasoning-data synthesis. Online self-improvement converts intermediate solver failures into reusable skills during generation. Post-task self-improvement revises skills, prompts, and workflows after each batch, adopting candidates only when they generate harder valid tasks within a bounded cost increase. Model weights and verification criteria remain fixed. Across mathematics, coding, and science, mean solver accuracy decreases from 100.0% to 54.8% over fourteen evolution rounds. Ablations show that combining both update schedules produces harder tasks than fixed-harness recursion or either schedule alone. The resulting data improves downstream SFT and GRPO performance. In particular, a 27B student fine-tuned on 10K synthesized mathematics examples achieves 62.5% mean-16 accuracy on APEX, competitive with selected frontier-model references. These results support adapting the synthesis harness alongside the tasks to generate increasingly challenging data with downstream training value.

---


### 261. [FlowHMR: Physically Plausible Motion Capture from Video](https://arxiv.org/abs/2610.03691)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhanke Wang, Chengfeng Zhao, Qing Shuai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FlowHMR, a framework for recovering physically plausible global 3D human motion from monocular video. Previous learning-based methods typically regress human motion directly from video and train the network with geometric supervision. However, recovering human motion from monocular video is inherently ambiguous in depth, and direct regression tends to collapse toward an averaged solution. Moreover, the recovered motions are not guaranteed to be physically plausible, so physics-based tracking of them often fails. To address these challenges, we formulate video motion capture as a video-conditioned motion generation problem and first pretrain a flow matching model for this task. Given an input video, the pretrained model generates diverse motion candidates, but not all of them are faithful to the video or physically trackable. We therefore post-train the model using Group Relative Policy Optimization (GRPO) with two rewards. A fidelity reward encourages consistency with the input video. A tracking reward favors motions that a physics-based controller can track successfully. Together, these rewards shift the model's output preference, so the post-trained model stays faithful to the input video while producing more physically plausible motion. We further introduce Wild-4K, a large and diverse dataset of about 4K internet videos, for evaluating human motion recovery in the wild. Qualitative and quantitative experiments on Wild-4K show that our method outperforms state-of-the-art methods in overall motion fidelity and achieves a physical tracking success rate of 82.47%, compared with 62.82% for the strongest baseline, GVHMR.

---


> [!TIP]
> 当前位于：**251-261**（第 6/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-261**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
