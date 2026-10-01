# 🧠 大模型相关研究 | 2026年10月02日

> 本类共 **390** 篇论文：已确认 **371** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

---

### 201. [Do Self-Evolving Skills Generalize to Held-Out Tasks?](https://arxiv.org/abs/2609.39148)

**<font color=#1a73e8>作者：</font>** Xihao Piao, Zifeng Wang, Zhen Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents can externalize what they learn from past tasks into reusable \emph{skills}, such as procedures, checklists, code, or other executable artifacts, that can be retrieved and reused when solving new tasks. Self-evolving skill methods keep rewriting these skills after each round of practice on training tasks, and the skill is then used on new tasks of the same kind. We ask a question: does the improvement a skill shows on its training tasks carry over to new test tasks? We test five self-evolving methods and a one-shot skill on six benchmarks, with the same model, the same agent, and the same train/test split for every method. Of the 21 skills that improve on their training tasks, 5 keep all of that improvement on the test tasks, 13 keep part of it, and 3 keep none of it. No existing method is best everywhere. When we read the skills, the ones that carry over badly often fix details that should depend on the task, such as column names and output files, or turn a fix for one failure into a rule for every task. An LLM judge that reads the skill content can often see this: it ranks finished skills the same way the test results do in 86\% of pairs. But it predicts the effect of a single edit poorly, so edits still have to be tested by running them. Based on these findings, we describe Generalizable Skill Optimization (GSO), which keeps only a guide for writing skills and writes a new skill for each task; it scores highest on all six benchmarks.

---


### 202. [Rep2Skill: Representation-Guided Skill Self-Evolution for LLM Agents](https://arxiv.org/abs/2609.39149)

**<font color=#1a73e8>作者：</font>** Kaixing Zhang, Changming Li, Yingdong Shi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Textual skills enable large language model (LLM) based agents to accumulate reusable procedural knowledge without updating model parameters. Yet existing skill evolution remains largely confined to the text space: an optimizer must diagnose success and failure patterns, and revise skills solely from long execution trajectories and sparse task outcomes. This text-only paradigm leaves the agent's internal representations, which contain rich records of its evolving execution state, outside the skill optimization loop. We ask whether an agent can improve its external textual skills by reflecting on its own internal representations. We introduce Rep2Skill, a representation-guided framework for self-evolution on agent skills. Specifically, upon the collected agent rollouts, Rep2Skill models their internal model representation trajectories to localize turns that deviate from successful execution dynamics, and it further interprets these signals alongside the execution contexts as actionable textual feedback for targeted skill revision. Experiments on two agent environments with two open-source LLMs show that Rep2Skill consistently outperforms text-only approaches in the self-evolution setting, where the same LLM serves as both executor and optimizer without a stronger external model. This establishes a promising direction moving agent self-improvement beyond text-only reflection.

---


### 203. [OP-CAD: On-Policy Clean-Audio Distillation for Robust Audio-Visual Reasoning](https://arxiv.org/abs/2609.39150)

**<font color=#1a73e8>作者：</font>** Xingming Shui, Dapeng Chen, Bowei Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal large language models deployed in real-world environments encounter external noise that can interfere with their perception and understanding of multimodal inputs. We study their robustness in audio-visual understanding, focusing on question answering under environmental noise and competing speech. The challenge is to resist acoustic interference while preserving useful audio evidence. On-policy distillation provides dense teacher feedback on student-generated responses, but uniform token weighting does not explicitly prioritize positions affected by acoustic interference. We introduce OP-CAD (On-Policy Clean-Audio Distillation), a curriculum-based privileged self-distillation framework for robust audio-visual understanding. Training progresses from mild to severe environmental noise and competing speech, with selective token-level supervision at each stage. The student generates responses from corrupted audio-visual input, while a frozen teacher uses clean audio and the verified answer to supervise the same response prefixes. To allocate this supervision, OP-CAD compares teacher predictions under clean, corrupted, and visual-only contexts without revealing the answer. These matched comparisons measure sensitivity to audio removal and corruption; a bounded weighting rule emphasizes positions identified by either signal while retaining supervision throughout the response. OP-CAD outperforms the compared methods across all evaluated noise conditions. Paired analyses further show improved preservation of clean-correct answers under strong interference, with no observed aggregate clean-accuracy penalty. These results demonstrate the value of directing clean-teacher supervision toward acoustically sensitive predictions for robust audio-visual reasoning.

---


### 204. [DAGent: Evaluate-then-Grow Planning for Deep Research Agents](https://arxiv.org/abs/2609.39154)

**<font color=#1a73e8>作者：</font>** Hanwen Liu, Yuanfu Sun, Qiaoyu Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep research tasks require agents to navigate large knowledge spaces, synthesize evidence across many sources, and adapt their plans as findings emerge. Directed acyclic graph (DAG)-based multi-agent systems suit this setting because they support parallel execution and isolate each sub-task within a focused dependency context. Yet existing DAG-based agents instantiate a task-level plan before execution and repair the graph only after failures or missing evidence are observed. This Plan-then-Patch strategy is brittle for deep research: the system commits most strongly when its evidence is weakest, and later revisions waste computation on branches that should not have been planned. We propose DAGent, a DAG-based multi-agent framework with Evaluate-then-Grow incremental planning: an Orchestrator grows the task graph one batch at a time, conditioning each expansion on confidence and uncertainty signals from completed nodes. A hierarchical context layer propagates compact QueryDocs by default while preserving full execution traces for on-demand recall. The recorded DAG topology admits structural RL signals that outcome-only recipes cannot define; DAGRPO, a GRPO adaptation, injects topology-conditioned credit on Executor rollouts and a structural compliance regularization on Orchestrator plans. Across BrowseComp-Plus, GAIA, and xbench-DeepSearch, DAGent surpasses the strongest open-source baseline by 5.3 / 5.8 / 2.0 points at the Qwen3-235B-A22B scale, and the lead replicates across four open-source backbones and extends to GPT-5 at 327K context. At the Qwen3-8B scale, DAGRPO improves over a same-budget outcome-only GRPO baseline by 3.0 average Pass@1 points. A same-architecture comparison shows that evidence-conditioned planning reaches higher accuracy at lower per-task token, tool-call, and step footprints than its Plan-then-Patch counterpart. Code: this https URL

---


### 205. [Reinforcing Multimodal Reasoning via Token-Level Perception-Grounded Advantage Estimation](https://arxiv.org/abs/2609.39168)

**<font color=#1a73e8>作者：</font>** Zhihan Zhang, Lizi Liao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR) has improved the reasoning capabilities of Multimodal Large Language Models (MLLMs), yet existing frameworks rely on coarse, sequence-level reward signals that lack the fine-grained supervision over the visually-grounded steps within a multimodal reasoning chain. We investigate this gap through the lens of two token-level metrics: visual dependency (i.e. how much a token's prediction relies on the input image features) and predictive entropy. Our empirical analysis reveals two key findings: (1) correct reasoning chains exhibit a markedly sharper entropy reduction as visual grounding intensifies, compared to incorrect ones; (2) pivotal tokens, those whose misprediction triggers reasoning collapse, are statistical outliers in the joint distribution of visual dependency and predictive entropy derived from correct chains. Motivated by these findings, we propose token-level perception-grounded advantage estimation (TPAE), which estimates token-level advantages by measuring each token's statistical consistency with the vision-entropy patterns of correct rollouts. TPAE leverages this granular score to modulate the sequence-level advantage, producing a fine-grained supervision signal that can be integrated into various RLVR frameworks. Extensive experiments on seven benchmarks show that TPAE consistently outperforms leading strong baselines, yielding more stable and efficient optimization for multimodal reasoning. The code is publicly available at this https URL.

---


### 206. [Aligning Thoughts with Answers: Probability Rewards to Tame Thinking Drift](https://arxiv.org/abs/2609.39183)

**<font color=#1a73e8>作者：</font>** Pengzhan Sun, Shiu-hong Kao, Shijie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies \textbf{thinking--answer consistency} in vision-language models. We focus on Visual Intention Grounding, where a model infers a target object based on a human intention query and predicts a bounding box. We reveal that previous IoU-based reinforcement learning (RL) frameworks suffer from ``thinking drift'', where the model produces a correct bounding box, despite having an incorrect reasoning process pointing to a different target object. Thus, we propose \textbf{Rita} (\textit{ReInforcing Thinking--Answer consistency}) as a novel RL paradigm to tame the drift. Specifically, Rita introduces two reasoning-label-free RL rewards, constructed from the conditional probability of reference answers: a \textbf{thinking reward} and a \textbf{consistency reward}. It also adopts a difficulty-aware \textbf{data filtering} strategy that selects informative easy-to-medium samples for RL using rollout error rate and reward variance. Extensive experiments on EgoIntention and the new RefEgo-Int benchmarks show that Rita performs consistently superior to the supervised finetuning approaches and vanilla RL-finetuned frameworks.

---


### 207. [Low-Discrepancy Dither for Quantized Recurrent State Caches](https://arxiv.org/abs/2609.39185)

**<font color=#1a73e8>作者：</font>** Snigdha Chandan Khilar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mamba-style and hybrid language models compress their past into a fixed-size recurrent state that is rewritten at every generated token. Storing this state in low precision saves memory bandwidth, but every rounding error is fed back into the next update and can accumulate over long generations. Production systems round the state stochastically; we ask which rounding rule such caches should use. We find that a deterministic golden-ratio Weyl dither, which needs no random numbers, consistently brings the quantized model closer to the full-precision one than stochastic rounding, across pure and hybrid models, storage formats, and long decoding horizons, at no extra cost. Round-to-nearest behaves differently: because it discards small updates, its error keeps growing, so it can look best in short evaluations yet falls far behind over long generations. A discrepancy analysis explains this ordering, and we document implementation pitfalls that silently remove the benefit.

---


### 208. [Attention Function as an Intrinsic Inductive Bias: How Models' Behavior Diverges in Novel Contexts](https://arxiv.org/abs/2609.39188)

**<font color=#1a73e8>作者：</font>** Dong Gyun Kang, Megha Thukral, Kwangsoo Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Developmental psychology holds that certain priors are given to infants prior to experience rather than induced from data, and that the influence of such priors is suppressed under strong, well-constrained conditions but reasserts itself under weak ones. We ask whether an analogous principle holds for the Transformer: can the activation function given to attention heads serve as an intrinsic inductive bias? We propose Mixture of Function Attention (MoFA), a parameter-free modification to multi-head attention that fixes a ratio of softmax and sigmoid heads before training. Across five ratios, a 124M-parameter GPT-2 model, and five seeds, we find that this given ratio has little effect in-distribution -- differences between ratios are statistically negligible for moderate mixtures and remain small even at the extremes -- but its influence re-emerges sharply under zero-shot distribution shift across 15 out-of-distribution domains. Perplexity gaps between ratios widen by more than an order of magnitude on several domains, and the best-performing ratio tracks a single axis of domain structure, separating short, informal text (softmax-favoring) from technical, long-form text (sigmoid-favoring), that explains 78.3% of the variance in domain response. This reorganization is visible at the head level: sigmoid heads show an accelerating drop in attention entropy as their ratio increases, while softmax heads respond more modestly, yielding a consistent division of labor between the two head types. Our results suggest that activation choice functions as a given prior whose influence is masked in-distribution and re-emerges out-of-distribution.

---


### 209. [ViLegalExpert: A Large-Scale Benchmark for Vietnamese Legal Retrieval and Question Answering from Real-World Consultations](https://arxiv.org/abs/2609.39189)

**<font color=#1a73e8>作者：</font>** Dat Tien Nguyen, Nghia Hieu Nguyen, Anh Thi-Hoang Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Trustworthy Legal AI requires systems that can answer legal questions while grounding their responses in authoritative sources. However, existing Vietnamese legal benchmarks provide limited coverage of real-world legal consultations. We introduce \textbf{ViLegalExpert}, a large-scale benchmark constructed from authentic citizen--lawyer consultations, containing over \textbf{172K} questions across \textbf{34 legal domains}, together with professional answers and expert-verified legal evidence. ViLegalExpert supports legal information retrieval, extractive QA, and abstractive QA. Experiments with representative retrieval methods and language models reveal substantial challenges in evidence retrieval and grounded answer generation. While pretrained models perform strongly on QA, hybrid retrieval achieves the best retrieval performance. These results demonstrate the difficulty of mapping naturally expressed legal questions to authoritative provisions and establish ViLegalExpert as a challenging benchmark for reliable Vietnamese Legal AI.

---


### 210. [Uruqi: Learning Spatial Cognition from Visual Experience](https://arxiv.org/abs/2609.39195)

**<font color=#1a73e8>作者：</font>** Shichao Li, Meiqi Wang, Fei Su 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence requires maintaining a coherent understanding of the world as the embodied agent moves. Like humans, the agent must use its own motion to interpret changes across observations and update object locations and spatial relations accordingly. Despite spatial post-training having substantially broadened the spatial intelligence of vision-language models (VLMs), they still struggle with two atomic spatial capabilities: tracking self-motion and mapping the surrounding world during motion. To address this gap, we provide dense multi-turn supervision over interleaved atomic capabilities within each training episode, mimicking the visual experience of a continuously moving agent that reasons as it observes. To scale this up, we synthesize 11,738 motif-driven camera trajectories over a broad range of 3D scenes, supporting self-motion tracking, persistent object mapping, and rich spatial operations within each visual experience. By training models to reason over these atomic questions, our URUQI$_{\mathrm{Syn}}$-8B improves accuracy from 15.84% to 47.73% on our Uruqi benchmark comprising 52k questions across 2.7k episodes. URUQI-SI-Mix-8B further reaches 50.41%, comparable to the 50.08% achieved by GPT-6 Astra. Trained solely on our synthesized data, URUQI$_{\mathrm{Syn}}$-8B achieves an average relative accuracy improvement of 17.13% over its InternVL3-8B backbone across three external spatial benchmarks. These results highlight continuous visual experience as a scalable source of supervision for developing spatial cognition in VLMs.

---


### 211. [Consensus and Factual Dynamics in Large Populations of Interacting Language Models](https://arxiv.org/abs/2609.39211)

**<font color=#1a73e8>作者：</font>** Emanuele Ricco, Elia Onofri, Vincenzo Sammartino 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly deployed as populations of interacting entities, in which consensus --agreement on a shared answer-- emerges as a collective, unengineered behaviour. Prior work on LLM consensus shows that agents can cross-verify their answers and converge towards more factual responses, treating agreement as a proxy for correctness. However, these studies usually fix a single interaction structure, leaving open how consensus depends on how agents interact. We address this gap by introducing RHEON, a physics-inspired framework that recasts a population drawn from a single frozen model as an evolving $O(n)$ spin system on a ladder of interaction geometries of increasing effective dimension --from a 1D ring to a full-coupling mean-field graph-- with the sampling temperature $T$ as the tunable source of thermal disorder, evolved through a Glauber-like asynchronous dynamics. Sweeping RHEON across $432$ configurations of prompt, population size, communication topology, and sampling temperature yields Eraclitus-4.7M, a tagged evolutionary corpus of $4.7$ million responses. We find that agents reach their strongest consensus gain within the first few update sweeps and that increasing the number of neighbours per agent accelerates convergence on average. We further show that whether a configuration settles on factually correct or hallucinated consensus is not predictable from its initial state alone, and that the hallucination-minimising temperature depends on how the agents are coupled, so the common near-greedy default is not automatically the safest. Finally, semantic agreement correlates positively with factual convergence, and interaction strengthens the association, yet never enough for unanimity to certify correctness.

---


### 212. [Learning Process Rewards via Reasoning State Propagation](https://arxiv.org/abs/2609.39220)

**<font color=#1a73e8>作者：</font>** Kai Gan, Zi-Hao Zhou, Bo Ye 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Process reward models (PRMs) have demonstrated notable effectiveness in test-time scaling and reinforcement learning by providing fine-grained signals for evaluating intermediate reasoning states, but their training relies heavily on costly process annotations. A natural way to alleviate this dependence is to complement limited process supervision with scalable outcome supervision. However, existing PRMs often model reasoning prefixes independently, providing no explicit mechanism for effectively using final outcome to guide the learning of intermediate reasoning states. We introduce Reasoning State Propagation (RSP), which represents each reasoning prefix with a binary validity state and models transitions between successive states across the reasoning trajectory. Specifically, RSP predicts a break probability that a valid state becomes invalid and a repair probability that an invalid state returns to valid. By propagating these transitions, RSP connects intermediate states to the final state, allowing process annotations to supervise intermediate states while outcome labels supervise the final state and can provide learning signals to preceding steps. Across reasoning search, response selection, and reinforcement learning, RSP consistently outperforms representative PRM baselines, with average improvements over Qwen2.5-Math-PRM of 5.6% in beam search and 2.1% in reinforcement learning.

---


### 213. [QATFactory: A Versatile, Deployment-Aligned Framework for Quantization-aware Training and Distillation of LLMs](https://arxiv.org/abs/2609.39223)

**<font color=#1a73e8>作者：</font>** Weili Xu, Jisen Li, Yuqing Jian 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) inference is increasingly moving toward lower precision to realize the throughput of hardware accelerators, but aggressive post-training quantization (PTQ) can degrade model quality. We present QATFactory, an open-source framework for deployment-aligned quantization-aware distillation (QAD) and reinforcement learning (QARL). QATFactory simulates deployment-time quantization while performing matrix multiplications in BF16, allowing models to adapt to quantization noise without requiring training hardware that natively supports the target format; for example, it supports NVFP4 training on H100 GPUs, which lack FP4 Tensor Cores. The framework supports NVFP4, MXFP4, and this http URL's Q4_K format; dense and mixture-of-experts models; and both full-parameter and LoRA-based training. It exports checkpoints directly to vLLM and this http URL without an additional lossy conversion step or added inference overhead. With QATFactory, we conduct extensive experiments on models ranging from 8B to 230B parameters and evaluate exported checkpoints in production inference engines. Across models and formats, QAD consistently improves deployed-model quality over strong PTQ baselines. On Qwen3.5-9B, QAD achieves average benchmark accuracies of 68.9% under NVFP4 and 66.0% under MXFP4, outperforming the best PTQ results of 65.4% and 56.4%, respectively. Through our experiments, we found that although both FP4 formats quantize weights and activations at deployment, the best training strategy is format-dependent: NVFP4 generally performs better when only weights are quantized during training, whereas MXFP4 benefits from quantizing both weights and activations. At a fixed training token budget, training on fewer 32K sequences improves average accuracy by 1.9 points over training on more 4K sequences. We release the complete QATFactory training code and the resulting checkpoints.

---


### 214. [Argument Structure Prediction in Online Conversations: A Comparative Study of Modeling Paradigms and Task Architectures](https://arxiv.org/abs/2609.39225)

**<font color=#1a73e8>作者：</font>** Siddharth Bhargava, Sara Tonelli, Patricia Martín-Rodilla 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Argument structure prediction (ASP) constructs complete argument structures from discourse by identifying argumentative units and their relations. While recent work has explored diverse approaches---including unified neural models, multi-step pipelines, and prompt-based large language models (LLMs)---their relative trade-offs remain under-explored, particularly in dialogical settings.
We present a systematic evaluation of ASP under strict schema constraints, comparing supervised fine-tuning and prompt-based LLMs across single- and multi-step task architectures, generating complete argument structures from dialogical input end-to-end. We benchmark them on three diverse dialogical corpora adapted from Inference Anchoring Theory into bipolar argument structures. Under a shared evaluation framework, we assess predictive performance, cross-domain generalization, schema compliance, and computational efficiency. Our results show that ASP remains a challenging task, with identifying argumentative relations emerging as the primary bottleneck, largely due to the implicit and context-dependent nature of dialogical argumentation. To facilitate future research, we release our data processing pipeline and end-to-end modeling framework for computational ASP on dialogical corpora.

---


### 215. [Fyan: A Human--AI Harness with Semantic Auditing for Document-Level Formalization](https://arxiv.org/abs/2609.39228)

**<font color=#1a73e8>作者：</font>** Wei Zhao, Yangshuo Zou, Chengxiang Ding 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present FYAN, a human--AI harness for document-level mathematical formalization. Rather than treating theorems in isolation, FYAN coordinates an end-to-end workflow spanning specification, proof planning, logical review, Lean proof construction, knowledge curation, and validation, with support for independent supervision and human guidance. A central component is evidence-grounded semantic auditing, which assesses whether formal statements faithfully preserve their informal specifications. A language model constructs structured evidence over local correspondences, omissions, scope, and logical relations, while a deterministic validator checks this evidence and produces reproducible judgments. When a substantive but admissible deviation is accepted, FYAN requires an explicit proof-transfer obligation connecting the formal statement back to a source-facing interpretation. With the same model (DeepSeek-V4.1-Flash) in every stage, FYAN proves 86 of 143 FormalTCS theorems under a strict Lean check, against 69 for a general agent harness, and raises the natural-language proof score from 0.501 to 0.851. On ConsistencyCheck, its semantic audit catches more inconsistent statements than a direct LLM judge, both on labels verified against the source (recall 0.777 vs. 0.636) and on the original labels (0.873 vs. 0.820), and localizes each mismatch it reports to a specific hypothesis, conclusion, or scope. FYAN also built ODENumLib, a 9,355-line Lean library for the numerical analysis of ordinary differential equation.

---


### 216. [RAIM: Robust Aggregation of Inexpensive Models for Hallucination Detection](https://arxiv.org/abs/2609.39229)

**<font color=#1a73e8>作者：</font>** Elia Onofri, Roberto Di Pietro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic evaluation of faithfulness increasingly relies on a large language model acting as a judge, yet the most reliable judges are proprietary frontier models, costly and ill-suited to high-throughput monitoring. We investigate whether a panel of cheap open-weight judges (4--9B) can be aggregated to stand in for a frontier one, what the substitution sacrifices, and when it is worth making. We propose RAIM, an aggregation scheme robust to the members' correlated errors, coupling a cross-fitted stacked logistic regression with an admissibility test that, read from the members' own outputs, identifies when aggregating them improves on their best member and stays within reach of the frontier judge. We instantiate RAIM with ten judges from disjoint families across eight faithfulness benchmarks. Against Claude Sonnet, the panel retains a median 93% of its Cohen's $\kappa$ and gives up only 2.9 points of balanced accuracy on average; read as paired differences, it clearly improves on one benchmark and clearly worsens on three (only two by a non-negligible margin), leaving four unresolved. At a sixty-fourth of the frontier's inference price, the operative expense is a one-time in-domain calibration on 50--100 labelled records. The panel is also competitive with purpose-trained detectors on their home benchmarks (within 1.3 accuracy points of GPT-4o and 1.9 of the LLM-AggreFact leader), and beats the strongest one we reran by 6 points on our grounded sets. Whether aggregation pays depends on the members themselves: where several capable members err on different items, the panel improves on its best judge and approaches the frontier; where one dominates, the stacker recovers the leader, and only there does the frontier remain materially ahead. Both conditions are read off the calibration set at no further cost, so a cheap panel can stand in for a frontier one wherever this audit admits it.

---


### 217. [4MT-VLM: How Coarse Is a VLMs Cognitive Map?](https://arxiv.org/abs/2609.39238)

**<font color=#1a73e8>作者：</font>** Markus Frey  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An agent that moves must recognise a place from a viewpoint it has never seen. We introduce 4MT-VLM, a dataset of procedurally generated landscapes, each rendered across five stimulus modes that remove appearance cues while holding layout fixed: shape and colour, shape only, colour only, bare terrain peaks with no objects, and a valley viewpoint that puts the peaks on the horizon. The last condition is commonly used in clinics to probe hippocampal function in human patients. We test this benchmark across sixteen different open and closed-source models and report 4AFC performance, a measure which is also used to grade human participants. We observe that models identify a place from the studied viewpoint but lose it once the camera moves, dropping below the 25% chance level at 135° where a human observer scores 85%. Frontier models (Gemini 3.8 Flash, GPT-5.6) answer only 39% and 31% of rotated trials correctly, recovering to 85% and 55% only when distractors are moved more than 30 meters apart. Our benchmark demonstrates that while current VLMs possess rudimentary cognitive maps, their spatial resolution remains fundamentally too coarse to maintain a stable, 3D understanding of the world once the viewpoint changes.

---


### 218. [Right Answer, Wrong Mechanism: Detecting Pernicious Divergence in Causal Interventions](https://arxiv.org/abs/2609.39243)

**<font color=#1a73e8>作者：</font>** Beiming Liu, Minjie Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal interventions such as activation patching and distributed alignment search (DAS) are the main tool for making mechanistic claims about neural networks. Recent work showed that these interventions routinely push representations off the model's natural distribution, and that such divergence is sometimes harmless and sometimes pernicious: it can recruit pathways the model never uses on natural inputs, so that an intervention produces the expected answer through the wrong mechanism. No method currently tells the two cases apart. We make this question testable by planting hidden pathways inside pretrained language models; the pathways are silent on every benchmark prompt by construction, so which interventions depend on them is known exactly. Across 72 configurations and 100,800 interventions on GPT-2 small, we find three things. (i) Nearest-neighbour and local-PCA distances at the intervention site, as used in prior work, score below chance (AUROC 0.35-0.47) at picking out interventions that give the right answer through a planted pathway. (ii) Hidden-Pathway Contribution (HPC), a label-free test that clamps downstream units to the regime of natural runs with the same output and measures how much of the decision disappears, flags pathway-dominated interventions with AUROC >= 0.99 when the pathway shows up as unit-level out-of-regime activity, but fails when every unit stays within its natural range, which we identify as the open problem. (iii) Optimised interventions actively seek hidden pathways: on a gender task, DAS routes 90-95% of its successes through planted pathways for three of four families, and a downstream on-manifold penalty cuts this share to under 5% at a cost of 6-11 points of success rate. In unmodified GPT-2, successful interventions show almost no unit-level out-of-regime reliance.

---


### 219. [Trust the Critic More](https://arxiv.org/abs/2609.39247)

**<font color=#1a73e8>作者：</font>** Kaiyue Wen, Luke Bailey, Arvind Mahankali 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard language model RL algorithms credit every token of a long rollout with the same advantage determined by the terminal reward. Actor-critic methods can provide finer-grained credit assignment, but learned critics are generally considered too inaccurate to trust when training LLMs with RL. In recent works, even when a critic is present, it is used only for baseline estimation, so every trajectory must be rolled out to its terminal reward. We introduce Actor-Critic with Action Chunking (AC2) that removes the need to roll every trajectory to completion. AC2 instead assigns credit to action chunks: short continuations of prefixes of past trajectories. A learned critic scores the state reached at the end of each action chunk, allowing the policy to update without observing a terminal reward. We make critic-based credit assignment reliable through three design choices. First, we introduce local readiness which uses critic-based updates on a problem only when the critic is sufficiently accurate on that particular problem. Second, when available, we provide the critic with a reference solution from a previous successful rollout. Third, we assign credit over action chunks of 10k tokens rather than individual tokens, giving the critic a more meaningful portion of the trajectory to evaluate. We train Qwen3-4B on FineProofs-RL using AC2 and evaluate on IMO-ProofBench. AC2 exceeds GRPO's peak validation score of 18.5% using 2.5x fewer decoding FLOPs. This gain comes from two sources, (1) AC2 requires 25% fewer training steps to reach this score, and (2) each step generates fewer tokens because the policy does not need to continue every trajectory to completion. Conceptually, we demonstrate that we can remove the need to roll out every trajectory to completion, opening up a large previously unexplored design space for LLM RL algorithms.

---


### 220. [ReTaCo: Residual-Target Control for On-Policy Distillation](https://arxiv.org/abs/2609.39275)

**<font color=#1a73e8>作者：</font>** Zixiang Ni, Zhuo Hu, Renjie Cao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own generated prefixes with token-level teacher feedback, but transmitting or storing the teacher's full-vocabulary distribution at every token is costly. Entropy-aware OPD (EOPD) adds forward supervision to reverse KL to help the student recover plausible tokens it underestimates, using only the teacher's top-$k$ probabilities to limit cost. Because EOPD renormalizes these probabilities, its target assigns no mass to the omitted vocabulary. We prove that the resulting loss keeps pushing the student's top-$k$ mass toward one even after the student matches the teacher's relative probabilities within the top-$k$ set, so the teacher itself is not a stationary point whenever the omitted tokens have positive teacher probability. We propose ReTaCo (Residual-Target Control), which keeps the top-$k$ tokens individually and groups the remaining tokens into one residual symbol, and pairs this forward target with a single-sample estimator whose expectation equals the full-vocabulary reverse KL. With teacher top-$k$ mass $m$, the residual target is $(1-\beta)(1-m)$ for $\beta\in[0,1]$: $\beta=0$ preserves the teacher's mass, and larger $\beta$ moves more mass onto the top-$k$ tokens without changing their relative probabilities. At a fixed prefix, we prove that the population objective has a unique optimum whose top-$k$ mass lies between $m$ and $m+\beta(1-m)$ and increases monotonically with $\beta$; at $\beta=0$, underestimated top-$k$ tokens still receive non-vanishing recovery gradients. Numerical optimization confirms these predictions, and across three teacher-student pairs, ReTaCo outperforms EOPD on most mathematics and code benchmarks.

---


### 221. [ANI: Adaptive Numerical Injection for Unifying Semantic and Arithmetic Representations in Numerical Reasoning](https://arxiv.org/abs/2609.39294)

**<font color=#1a73e8>作者：</font>** Jinsung Jeon, Seung-won Hwang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Precise numerical reasoning with Large Language Models (LLMs) is essential for expanding their applicability to complex real-world tasks. However, text-based tokenization often fragments numbers, significantly hindering precise arithmetic reasoning. Meanwhile, numerical embeddings, despite arithmetic precision, rely on context-agnostic substitution that disregards the semantic role of numbers as identifiers. To combine the complementary strengths, we propose \textbf{ANI (Adaptive Numerical Injection)}, a hybrid framework that governs the selective injection of numerical features based on the semantic context. By employing a context-aware gating mechanism, we selectively inject numerical embeddings (specifically FoNE) into the latent space, explicitly preserving nominal identifiers while enhancing quantitative operands. Through extensive evaluations across various LLMs, we demonstrate that ANI enhances MATH performance by 9.5 points over the official reference model, while maintaining robust performance on general linguistic benchmarks.

---


### 222. [MiniRep: Robust Reputation-Based Aggregation for Multi-Agent Debate](https://arxiv.org/abs/2609.39297)

**<font color=#1a73e8>作者：</font>** Jiaming Zhang, Yuwan Liu, Yue Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents powered by large language models (LLMs) are rapidly evolving into an open agentic ecosystem. To support trustworthy collaboration, industry initiatives increasingly assess agent reputation from past behavior and provide performance leaderboards. However, reputation derived from past performance may not reliably predict an agent's behavior on new tasks, particularly when malicious agents can adapt their behavior and influence other agents during collaboration.
We study reputation in multi-agent debate (MAD), where multiple agents answer the same query, debate to improve their answers, and aggregate them into a final output. We present MiniRep, a reputation-based aggregation system for MAD under malicious agents. To ground our threat model in established research, we construct an attack taxonomy drawing on reputation-system attacks and software-testing mutation operators, covering strategic exploitation of reputation and subtle corruption of agent proposals. Guided by this taxonomy, MiniRep evaluates agents based on both their behavior on the current task and their reputation over time, while preventing groups of agents with highly similar responses from dominating the final decision. We assess MiniRep across diverse tasks, LLM-agent compositions, corruption placements, and attack types drawn from our taxonomy. Our experimental results show that, MiniRep outperforms both conventional MAD aggregation and conventional reputation-based approaches on MATH no matter being attacked or not. Also, under a heterogeneous 10-agent setting on MATH, MiniRep outperforms all baselines in all 28 attack conditions.

---


### 223. [ReSAIL: Mitigating Collapse in Iterative Agent Self-Distillation](https://arxiv.org/abs/2609.39306)

**<font color=#1a73e8>作者：</font>** Shengjie Jin, Hengbo Xu, Zelong Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Iterative self-distillation enables LLM agents to learn from successive deployments, offering a path toward recursive self-improvement (RSI). Yet our experiments with existing methods reveal a collapse in deployment performance across cycles, while task performance with privileged information (PI) also declines. We address this collapse by prioritizing informative interaction steps for distillation and preserving PI-conditioned behavior as the student becomes the next teacher. We introduce Retentive and Selective Augmentation for Iterative Self-Distillation (ReSAIL), a plug-in augmentation for iterative PI-based self-distillation. ReSAIL selects interaction steps where PI most strongly changes the teacher's predictions and balances the resulting distillation losses across trajectories. It also regularizes the student's PI-conditioned output distributions toward those of the frozen teacher at selected and unselected steps to preserve PI-conditioned behavior for supervision in the next cycle. On ALFWorld and TextCraft, ReSAIL sustains substantial gains across model scales over three cycles, with an average absolute gain of 22.5% in final-cycle success rates when added to self-distillation baselines. Sensitivity-guided selection of offline data also improves action prediction accuracy for multimodal GUI agents on AITZ. These findings provide the first evidence that a more robust learning mechanism can effectively mitigate performance collapse in iterative agent self-distillation over deployment trajectories.

---


### 224. [Rethinking Generative Image Compression at Extremely Low Bitrates](https://arxiv.org/abs/2609.39315)

**<font color=#1a73e8>作者：</font>** Tianyu Zhang, Zhaoyang Jia, Houqiang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative image compression produces visually plausible reconstructions at low bitrates, yet their behavior as the rate approaches zero remains largely unexplored. When pushed below normal operating rates, representative codecs undergo semantic collapse: rather than gracefully losing source-specific detail, they produce malformed or unrecognizable content. Our analysis identifies two factors. As the bitrate decreases, reconstruction losses increasingly conflict with semantic objectives on gradients and visual results, while pixel-space and reconstruction-oriented VAE diffusion models become less efficient on semantic preservation. Guided by these findings, we introduce RAE-CoD, a compression-oriented diffusion (CoD) built in a representation autoencoder (RAE) space with direct alignment between compressed and source representations, preserving recognizable, naturally structured content for a $256\times256$ image with as few as 16 bits. We evaluate this framework using five vision foundation models (VFM) and a blinded vision-language model protocol. On MSCOCO-30K, RAE-CoD stands out from all evaluation. At 0.001-0.008 bpp, it reduces relative VFM feature MSE and Fréchet Distance ratio by at least 25.7% and 69.1% over the best competitors. Meanwhile, semantic recognizability and quality of the reconstructions remain nearly constant while source consistency falls smoothly, replacing abrupt semantic collapse with a graceful transition toward unconditional generation. Code will be released at this https URL.

---


### 225. [GRPO Training Dynamics for Small Language Models](https://arxiv.org/abs/2609.39321)

**<font color=#1a73e8>作者：</font>** Rajat Ghosh, Vaishnavi Bhargava, Henry Wong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has emerged as a memory-efficient reinforcement fine-tuning (RFT) technique for reasoning-intensive tasks. How- ever, GRPO training dynamics on small language models (SLMs) remain poorly understood, limiting its reliable adoption and reproducibility in open and resource- constrained environments. In this work, we present a systematic study of GRPO fine-tuning for SLMs ranging from 1.5B to 7B parameters under a practical single- node 8xA100 compute budget. Our study spans multiple model families and reasoning domains, including mathematics, coding, and multiple-choice question answering (MCQ) in science. Across these settings, we analyze how group size affects policy convergence, training stability, and downstream benchmark per- formance. We further characterize tensor-level update dynamics during GRPO training and investigate whether the choice of LoRA target modules and layers can improve the performance of GRPO-tuned models. While our initial GRPO-tuned models outperform their base counterparts on approximately 80% of mathematical benchmark evaluations, they demonstrate limited capability on MCQ and code reasoning tasks. Guided by our mechanistic evaluations, we refined our LoRA and reward-shaping configurations to improve performance in latter domains. These findings provide practical guidance for GRPO training for SLMs.

---


### 226. [WorkGenesis: Building the Worlds That Teach Agents to Work](https://arxiv.org/abs/2609.39325)

**<font color=#1a73e8>作者：</font>** Xinyu Zhu, Fenyi Liu, Yuzhu Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The ability of Large Language Model (LLM) agents to complete daily and professional work is receiving increasing attention. Training such agents requires realistic work scenarios. Expert-authored occupational work is costly and slow to produce, while unconstrained synthesis often yields tasks with weak factual grounding or internally inconsistent requirements. To bridge this gap, we introduce WorkGenesis, a framework that constructs executable occupational work from real-world artifacts through two core technical innovations: (1) Evidence-Based Work Construction, which grounds each unit of work in real-world evidence by retrieving public files guided by O*NET occupational knowledge and synthesizing the surrounding context, companion materials, work request, and itemwise rubric around them; and (2) Execution-Guided Consistency Verification, which renders a reference deliverable inside the constructed work, attributes every unsatisfied rubric item to the agent, the task, or the rubric, and uses task and rubric defects as feedback to iteratively repair the work until it passes the audit. Experimental results demonstrate that Fx-Work-35B, trained with simple supervised fine-tuning (SFT) on only 20K units of work synthesized by WorkGenesis, achieves the highest scores among all comparable-scale baselines on the five reported metrics across GDPvalAA-v2, APEX-Agents-AA, and JobBench (31.00 versus 24.79 average score), and even surpasses frontier models such as the 1.6T DeepSeek-V4-Pro-Preview. These results show that WorkGenesis provides scalable training data for working agents.

---


### 227. [PatchKV: Weight-Space Compensation of KV Cache](https://arxiv.org/abs/2609.39329)

**<font color=#1a73e8>作者：</font>** Chanryeol Lee, Chanhyuk Lee, Yeonwoo Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context inference with Large Language Models (LLMs) is bottlenecked by the linearly growing memory of the key-value (KV) cache. Existing compression methods reduce the cache through token eviction or approximation, but degrade sharply at aggressive compression budgets. We propose PatchKV, a training-free framework that compensates KV cache compression methods by carrying part of the context in the model's weights. PatchKV pairs an off-the-shelf compressed KV cache with a context-specific weight patch, which is computed once at context-loading time and served for downstream queries for the context. The weight patch is derived in closed form via ridge regression, by aligning the block-wise activations of context-derived reference query tokens under the full cache and the compressed cache. Once merged into the model, the patch leaves the forward graph and per-query inference cost unchanged in the single-context, multi-query setting. Across long-context QA (SCBench with up to 170K tokens, SQuAD, NIAH) and math (GSM8K) benchmarks on three model architectures, PatchKV consistently improves cache compression methods, suggesting an alternative direction to compensate them at aggressive budgets.

---


### 228. [WinoTS: Wavelet-based Self-Distillation for Time Series Models](https://arxiv.org/abs/2609.39337)

**<font color=#1a73e8>作者：</font>** Noam Major, Kathy Razmadze, Yoli Shavit  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-supervised pre-training of time series models is currently dominated by next-token prediction and reconstruction objectives. In continuous-valued domains, these paradigms often waste model capacity on high-frequency, point-wise noise at the expense of learning invariant structure. While invariance-based self-distillation has proven highly effective in computer vision, its application to temporal data remains largely underexplored. Effectively adapting such methods to time series requires carefully designed augmentations: spatial operations like cropping can shift the timing of repeating cycles or distort the signal, while basic jittering may provide limited variation. We introduce Wavelet-based self-distillation for time series (WinoTS), an invariance-based pre-training paradigm designed specifically for temporal signals. At its core, WinoTS leverages time-frequency augmentations to construct multi-scale structural views without distorting underlying signal dynamics. Across extensive evaluations, WinoTS outperforms state-of-the-art baselines in long-term forecasting, cross-domain zero-shot transfer, and unsupervised anomaly detection. Notably, linear probing on frozen WinoTS representations frequently surpasses fully supervised models trained from scratch. Systematic ablations demonstrate that WinoTS is a flexible, architecture-agnostic framework yielding gains across time series backbones, and establish that time-frequency transformations provide a principled alternative to vision-style spatial augmentations.

---


### 229. [Understanding as No-Arbitrage: Bounded Dutch Books as a Definition and Training Objective for Language Models](https://arxiv.org/abs/2609.39341)

**<font color=#1a73e8>作者：</font>** Daniel Dragonevskiy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Does a language model merely predict tokens, or does it understand what it says? We make this question measurable by defining "understanding" through the lens of no-arbitrage. A model understands a vocabulary to a certain degree if a computationally bounded trader cannot extract guaranteed profit by betting against the model's probabilities on logically related claims (a "Dutch book"). We establish three theoretical results: first, because full logical coherence is computationally intractable, understanding is inherently graded, not absolute. Second, we prove that the exact optimum of standard next-token prediction is inherently incoherent across different question formats; the flaw lies in the training objective, not the architecture. Third, we show that uncertainty accumulates predictably along reasoning chains, making unjustified overconfidence an arbitrage opportunity in itself. To address this, we introduce Arbitr, a training framework where an adversarial trader penalizes the model for logical inconsistencies, paired with a calibration anchor to prevent uninformative collapse. Across five pre-registered experiments on Qwen2.5 and Phi-3.5 models, we demonstrate that standard models are highly exploitable across different phrasings. Arbitr reduces this exploitability by orders of magnitude without sacrificing task accuracy, and the effect successfully transfers to unseen logical patterns and new model families. Crucially, we uncover a scaling illusion: at 7B parameters, near-zero measured incoherence often coincides with extreme, unjustified confidence. We conclude that while Arbitr enforces rigorous logical consistency, coherence is a necessary condition for knowledge, but not a sufficient one

---


### 230. [Offline Guidance, Online Reasoning: Reusing LLM Feedback for Small Language Models](https://arxiv.org/abs/2609.39346)

**<font color=#1a73e8>作者：</font>** Bohan Zhang, Linan Yue, Weibo Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) offer strong reasoning capabilities but are often costly to access through commercial APIs, while small language models (SLMs) are easier to deploy locally yet remain weaker in reasoning. This capability-deployment gap has motivated LLM-SLM collaboration, which aims to improve SLM reasoning using LLM capabilities while preserving the deployment advantages of SLMs. Existing approaches mainly follow two paradigms. Knowledge distillation uses LLM-generated answers and reasoning trajectories to train SLMs offline, but requires parameter updates and additional training. Alternatively, online collaboration routes difficult problems to an LLM or leverages LLM-generated guidance and corrections when an SLM encounters difficulties. Although effective, online collaboration requires repeated LLM access. Moreover, the guidance produced for a particular problem is discarded after inference and cannot benefit subsequent problems involving similar reasoning states. In the paper, we focus on a more constrained setting in which the LLM is accessed only offline, the SLM parameters remain fixed, and online inference is performed solely by the SLM. To this end, we propose Reusable Latent Correction (RLC), which converts one-off natural-language guidance from a black-box LLM into persistent corrective experiences in the hidden space of an SLM. RLC stores these experiences in an external bank and retrieves them according to the SLM's current reasoning state, enabling the SLM to reuse LLM-derived corrections during inference without any online LLM calls. Experiments across multiple reasoning benchmarks and SLM scales show that RLC consistently improves SLM reasoning without parameter updates or online LLM calls. Code is available at this https URL.

---


### 231. [Working Around the Compute Ceiling: Byte-Exact Memory in Galahad Makes LLM Reading a One-Time Cost LLM Reading a One-Time Cost](https://arxiv.org/abs/2609.39358)

**<font color=#1a73e8>作者：</font>** Sietse Schelpe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A transformer language model performs a bounded amount of computation per token, and recent work by Vishal Sikka, former CEO of Infosys, argues that this bound limits which tasks a model can carry out or verify (arXiv:2507.07505). We ask how much of the budget beneath that ceiling is spent on work the model has already done. Serving is stateless across requests: a model that answers a second question about a document recomputes the document's attention state from the first token. On seven real-world datasets, 98.7% of prompt tokens were text the model had already read. We present Galahad, a memory layer for vLLM, SGLang and this http URL that makes this reading a one-time cost. Taliesin saves the model's key-value (KV) state for a block of text and loads it on the next request that contains the same bytes, instead of recomputing it. Blaise keeps the documents themselves and passes the model only the section a question needs. On a recall test with 100 facts hidden in a 97,000-token corpus (Gemma 4 31B), Taliesin alone let the model attend to the whole corpus and answered 98 of 100 on this http URL at 3.0 s and 572 J per question, against 10 of 100, 9.3 s and 2,754 J for the same model without Galahad, which could hold only the last 12,000 tokens. With Blaise added, the model read about 668 tokens per question and answered 100 of 100 on all three runtimes at 0.59-0.64 s and 200-213 J; a tuned RAGFlow pipeline answered 77. Storing the corpus is a one-time cost of about 100 s and 28 kJ, whose energy is recovered after 13 questions. Restored state is bit-identical: all 262,144 output logits matched after restart, rehydration and hot-load. Galahad worked with all 30 models we tested under vLLM, and it fails closed: any load that does not pass its checks is recomputed. Together these results move LLM serving from stateless to stateful inference.

---


### 232. [LampAttention: Look-Ahead Mixed-Precision FlashAttention for Dedicated Accelerators](https://arxiv.org/abs/2609.39361)

**<font color=#1a73e8>作者：</font>** Stanislav Budzinskiy, Marian Gloser, Tolunay Yilmaz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While most attention logits can be computed in low precision without degrading numerical stability, current attention kernels fail to exploit this phenomenon. We introduce a novel hardware-algorithm co-design in the form of mixed-precision FlashAttention. Our method accumulates key-query products and evaluates their exponentials in 8-bit formats, then adaptively identifies sensitive sub-blocks and recomputes them in 16-bit formats. We propose the specifications for a dedicated accelerator capable of executing this pipeline efficiently. Simulated experiments with Qwen3 and Gemma 3 show that rerouting a selective minority of sub-blocks to high precision is sufficient to recover the baseline model performance.

---


### 233. [Rethinking Multi-Image Re-Representation in Multi-Image Understanding](https://arxiv.org/abs/2609.39363)

**<font color=#1a73e8>作者：</font>** Gengyuan Zhang, Xiao Han, Xinyu Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-image understanding requires MLLMs not only to recognise the content of individual images, but also to organise visual evidence distributed across them. We study this problem through multi-image re-representation, viewing prompted Chain-of-Thought reasoning and agentic visual tool use as different ways of re-organising visual evidence during reasoning. We introduce Mosaic, a general-purpose multi-image visual harness that enables an MLLM to actively construct visual intermediates with ten composable image operations. We compare five re-representation settings on existing multi-image benchmarks and on MosaicBench, a new grounding-focused benchmark for fine-grained multi-image understanding. Our experiments show that the relative benefits of textual and visual re-representation are strongly task-dependent. Visual re-representation is particularly effective for tasks requiring precise visual evidence, including hypothesis testing, precision comparison, and orientation-sensitive reasoning, while tasks dominated by higher-level semantic content show smaller or less consistent gains. Building on this finding, we train MosaicAgent-8B to use Mosaic with reinforcement learning using only accuracy and format rewards. Without demonstration trajectories or rewards for specific tool-use, the agent learns to compose visual operations over multiple steps and exhibits diverse problem-solving patterns unpromptedly. Code and data will be released at this https URL.

---


### 234. [Ready2Blend: From Natural-Language Instructions to Composable Alignment Prompts](https://arxiv.org/abs/2609.39365)

**<font color=#1a73e8>作者：</font>** Jeesu Jung, Hwan Chang, Juseon Do 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continual alignment requires LLMs to adapt to new requirements without forgetting previously acquired behaviors. Natural-language instructions are flexible and composable but offer only indirect control, whereas post-training provides stronger adaptation at the cost of repeated parameter updates. We introduce Ready2Blend, which combines the flexibility of natural language with learned alignment. AlignFormer maps each requirement to a fixed-length alignment prompt stored in a modular prompt bank, while the backbone and prior prompts remain frozen. Composability regularization transfers the semantic geometry of textual requirements into prompt space, enabling inference-time blending and reweighting. Across two practical continual alignment settings, Ready2Blend is the only frozen-backbone method that matches post-training-based alignment methods, reaching $93.1$-$98.5\%$ of a joint-training reference with competitive retention, while requiring only a few prompt tokens and up to $4.3\times$ less training time. Its modular design further enables weighted personalization and order-free composition without retraining. Code will be released upon acceptance.

---


### 235. [Exploring Heterogeneous Model Merging Approach for Complex Knowledge Transfer](https://arxiv.org/abs/2609.39369)

**<font color=#1a73e8>作者：</font>** Jiahe Fan, Si Chen, Yinghao Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Specialized models encode task-oriented behavior, but transferring that behavior to a general language model usually requires training, distillation, or representation alignment. We study whether such ability can instead be transferred directly at the parameter level. We apply two existing training-free heterogeneous merging methods, previously shown to transfer knowledge between general language models, to specialist-to-general transfer, projecting a specialist donor into the recipient's shape and interpolating backbone parameters without gradient updates or semantic alignment. Intersection-Merge (IM) injects a prefix-aligned donor slice matching the recipient shape, while Activate-Prune-Merge (APM) uses forward-pass activation statistics to select which donor dimensions to retain before injection. Across embedding, reranking, reward modeling, and MoE code-specialist transfer, both methods improve the general recipient, showing that simple heterogeneous merging can move capabilities across diverse specialist roles.

---


### 236. [EHR-RobustGym: Benchmarking and Training Agents for Robust Clinical Reasoning](https://arxiv.org/abs/2609.39371)

**<font color=#1a73e8>作者：</font>** Yitong Qiao, Yancheng Jin, Lei Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In hospital workflows, electronic health records (EHRs) are often noisy, and may not contain the evidence needed to confirm events or measurements referenced in a clinical query. Even when database retrieval succeeds, clinical agents can overlook such discrepancies and return plausible but unsupported answers. We introduce EHR-RobustGym, a scalable and interactive environment for evaluating and training robust clinical agents grounded in noisy EHRs. Built on MIMIC-IV hospital records (365K patients, 31 tables, and over 500M records), EHR-RobustGym comprises 5,486 Clean-Noise pairs spanning six clinical intents and both patient-level and population-level queries. The pairs test robustness to Record-level, Value-level, and Query-level noise, while interactive SQL/Python execution and outcome verification support trajectory collection and training. Evaluating multiple LLMs reveals substantial robustness gaps: average task success across proprietary and large-scale open-weight models drops from 62.2% on Clean questions to 37.9% on Noise questions. At k=4, pass^k consistency falls below 50% for most evaluated models, exposing instability in clinical task completion. Supervised fine-tuning and reinforcement learning in EHR-RobustGym improve performance, with gains generalizing to five external EHR benchmarks. Together, these results position EHR-RobustGym as a testbed for evaluating and improving the evidence-grounded robustness of clinical agents.

---


### 237. [EgoTools: Towards Tool-Centric Reasoning in Real-World Egocentric Videos](https://arxiv.org/abs/2609.39378)

**<font color=#1a73e8>作者：</font>** Shulin Tian, Junsu Kim, Shuai Liu 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world embodied tasks, from everyday activities to professional procedures, require agents to act under physical constraints while tracking evolving object and task states. Tool use sits at the heart of such tasks, as many everyday and professional activities are tool-mediated. Understanding them requires reasoning about affordances, hand-tool-object geometry, procedural progress, and causal effects on target objects. Yet despite strong performance on perception-oriented video tasks such as captioning and general video QA, current multimodal video models remain limited in this form of tool-centric embodied reasoning. Progress in this direction has been limited by the lack of real-world egocentric data and diagnostic benchmarks. To address this gap, we introduce EgoTools, the first comprehensive suite for egocentric tool-use understanding. It consists of two complementary components: EgoTools-Data, a large-scale corpus of 100 hours of tool-centric egocentric recordings with synchronized audio, dense captions, reasoning-heavy narrations, and supplementary 3D information; and EgoTools-Bench, a diagnostic benchmark of 1,000 QA pairs across four tracks that cover tool-use understanding from perception and geometry to procedure and causal reasoning. Experimental results show that current models still struggle to ground tool use in visual evidence: Gemini-3.1-Pro achieves 66.9% overall accuracy but only 51.7% on Perception & Grounding. Beyond evaluation, we validate EgoTools-Data as a training resource. On the full 1,000-question benchmark, full supervised fine-tuning improves Qwen3-VL-8B-Instruct from 50.0% to 60.9%, under strict source-video separation. Together, these results establish EgoTools as a unified resource for both training and diagnostic evaluation of real-world egocentric tool-use understanding.

---


### 238. [SkillFM: Generating Skills for LLM Agents via Latent Flow Matching](https://arxiv.org/abs/2609.39382)

**<font color=#1a73e8>作者：</font>** Zuming Zhang, Jie He, Yizhe Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Textual skills provide reusable guidance for large language model agents, but existing approaches often rely on manually curated skill banks or reinforcement learning with indirect and delayed feedback. We introduce SkillFM (Skill Flow Matching), a generative framework that synthesizes task-conditioned textual skills directly without test-time skill retrieval. Our framework combines a codec for encoding and reconstructing textual skills in a continuous latent space with a conditional flow model trained using improved MeanFlow. At inference time, the learned velocity field enables single-step latent sampling, and an LLM-based decoder converts the sampled representation into textual guidance for a frozen downstream agent. We evaluate the framework on embodied tasks, question answering, and web shopping. On ALFWorld and Search-QA, our method achieves the best overall performance among the compared vector-based skill approaches. Our analyses further demonstrate that latent skill generation is an effective alternative to retrieval-based skill augmentation. Our code and training skill libraries are available at this https URL.

---


### 239. [From Search to Signal: Online Post-Training in Automatic Heuristic Design](https://arxiv.org/abs/2609.39383)

**<font color=#1a73e8>作者：</font>** Yilun Yuan, Tianyu Zhou, Zhenzhou Tang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based automatic heuristic design (AHD) iteratively proposes and refines heuristics, pairing design rationales with executable code. Task-specific evaluators assess programs; execution outcomes and performance scores guide search. Many AHD systems keep the generator frozen; EvoTune and Co-Evolution of Algorithms and Language Model (CALM) instead update it from evaluated candidates. When such outcomes drive reinforcement learning with verifiable rewards (RLVR), they create a search-coupled loop: the evaluated candidate stream supplies both search-state updates and training signals for the model that generates future candidates. Yet validity and performance do not uniquely determine useful model updates; converting them into learning signals must account for the prompt and evolving search state that produced each candidate. We formulate online post-training of small open-weight LLMs in AHD as context-dependent signal construction and develop alternative mappings from program validity, task performance, and generation context to update signals. Using shared evaluated rollouts and matched update budgets, controlled experiments across AHD tasks and model families compare these mappings with online post-training baselines, testing their effects on validity, performance among valid proposals, and the yield of valid proposals that improve under contextual comparisons. Complementary checkpoint, frozen-search, and live-system evaluations assess whether proposal-level gains appear in updated checkpoint behavior and subsequent search, rather than arising solely from accumulated search state. A resource-matched comparison under pre-specified cost accounting tests whether online updating adds value beyond additional search with a frozen generator. Together, this design avoids treating end-to-end search gains alone as evidence of stronger heuristic-design capabilities.

---


### 240. [Can Computation from Earlier Problems Help LLMs Solve New Ones?](https://arxiv.org/abs/2609.39394)

**<font color=#1a73e8>作者：</font>** Jipei He, Wenhui Tan, Xiaoyi Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models often solve independent problems in the same conversation. Can computation from earlier problems help them solve new ones? To answer this question, we first conduct preliminary experiments showing that retained history can raise or lower later-turn accuracy, even within the same domain. To understand these effects, we use controlled replay to isolate internal state changes specific to each problem-history pairing. Across different histories, these changes preserve similar relationships among current problems. To improve reasoning under retained history, we introduce STAIR (Stale-Token Attention for Inter-query Reuse). STAIR captures keys and values from earlier response generation in a fixed bank. It learns to redirect current queries when they read this bank during prompt processing. The base model remains frozen; only 12,288 parameters are trained. Across three Qwen models and four benchmarks, STAIR improves average later-turn accuracy by up to 11.67 percentage points over the unmodified model with history.

---


### 241. [Advancing Entropy-Level Credit Assignment in RLVR via Proximal Entropy Policy Optimization](https://arxiv.org/abs/2609.39402)

**<font color=#1a73e8>作者：</font>** Yun Kim, Nojun Kwak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Value-model-free RLVR methods such as GRPO assign uniform advantages to all tokens in a rollout, ignoring that tokens contribute unequally. Recent methods use token entropy as an importance proxy but compute it globally across the batch, conflating importance with prompt difficulty and positional trends. We argue that importance should instead be measured relative to the local context of each token. We introduce proximal entropy, a local measure of token importance relative to neighboring tokens, and prove it is invariant to both confounders. Proximal Entropy Policy Optimization (PEPO) uses it to weight per-token advantages and outperforms GRPO and entropy-based baselines on mathematical reasoning across Qwen3-1.7B, Qwen3-4B, and Llama-3.2-3B-Instruct. We also show the formulation generalizes to other algorithms where substituting proximal entropy into existing methods improves, and applying it to single-stream RL succeeds where global entropy fails.

---


### 242. [No Task Vector Is an Island: A Comprehensive Study on the Composability of Task Vectors from On-Policy Distillation](https://arxiv.org/abs/2609.39405)

**<font color=#1a73e8>作者：</font>** Jingang Zhou, Feiyu Han, Han Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Task vectors provide a simple mechanism for composing learned capabilities through model merging. However, the composability of task vectors produced by on-policy distillation (OPD) remains largely unexplored. OPD trains a student using teacher feedback on student-generated trajectories, yielding parameter updates that differ from those produced by the teacher model, usually by reinforcement learning (RL). We therefore ask whether OPD task vectors can complement their RL teacher updates and compose effectively across tasks. Across five domains and two model architectures, we find evidence for both forms of composability. Within a task, merging OPD and RL task vectors can outperform both constituent models, even when the OPD student is weaker than its RL teacher. Across tasks, OPD task-vector compositions achieve higher average scores than corresponding RL compositions in seven of eight backbone-merging-rule comparisons. Parameter-space analyses reveal substantial non-collinearity between OPD and RL updates. Experiment in CODE domain on SMOLLM3-3B shows that the combined direction outperforms either constituent direction at the tested global update norm, supporting directional complementarity in this configuration. Across tasks, OPD updates also show lower overlap among the top-10% feed-forward channels ranked by update energy. Together, these results show that weaker standalone performance does not imply weaker task-vector composability. OPD task vectors can complement stronger RL teacher updates and combine effectively across tasks, highlighting composability as a distinct property for understanding and evaluating post-training updates.

---


### 243. [Inferring Causal Relations between Two Sequences of Events with Language Models](https://arxiv.org/abs/2609.39406)

**<font color=#1a73e8>作者：</font>** Nishchal Prasad, Eric Gaussier, Emilie Devijver 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Causal AI is a branch of Artificial Intelligence which helps understand and reason about cause and effect relationships, not just patterns or correlations. Causal discovery aims to infer elements of the underlying causal structure--often represented as a directed graph--from observational and, when available, interventional data. While causal discovery is the fundamental step for moving beyond mere associations toward genuine understanding, and thus the basic building block of causal AI, it becomes intrinsically difficult when causal relations must be inferred from single observations. In such situations, standard causal discovery methods cannot be used and one has to identify causal relations from limited amount of information. This is typically the case for, e.g., sequences of events produced by different alarms which need to be analyzed on the fly to detect abnormal phenomena, which are usually rare. We show in this study that it is possible to leverage the predictive power of Large Language Models (LLMs) to infer causal relations between only two sequences of events. This approach, which is validated on both synthetic and real data, provides better results than standard causal discovery algorithms on several time series data, even though these data were converted into smaller, single observed sequences.

---


### 244. [SEW: Style-Encoded Watermarking of LLM-Generated Code](https://arxiv.org/abs/2609.39414)

**<font color=#1a73e8>作者：</font>** Soohan Lim, Hyundong Jin, Yo-Sub Han  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Code watermarking supports provenance tracking for code generated by LLMs. Modifying token selection to embed watermarks as an LLM generates code can create a trade-off between detectability and functional correctness. Other methods instead watermark completed code using predefined transformations or trained neural models. Recurring patterns can make watermark choices predictable across programs, while treating patterns common in unwatermarked code as watermark evidence can cause false detections. We therefore introduce SEW, which embeds and detects watermarks in already generated code through three components: (i) code style rules collected from style guides and transformation rules, with style choices determined by a secret key and each program's structural context; (ii) style-preference calibration, which evaluates watermark evidence using style probabilities estimated from human-written code; and (iii) context-aware style aggregation, which combines evidence from structurally matching locations assigned the same code style choice, preventing repeated applications of that choice from inflating watermark evidence. On CodeContests across three LLMs and three programming languages, SEW achieves a mean relative improvement of 12.44% in TPR@FPR5% over the baselines and is robust to four non-LLM code-editing attacks, with only a 0.94% mean relative decrease. Our code is available at this https URL.

---


### 245. [QuantCode Model: Specializing Language Models for Executable Algorithmic Trading Code](https://arxiv.org/abs/2609.39420)

**<font color=#1a73e8>作者：</font>** Alexey Chernysh, Orkhan Ekhtibarov, Dmitry Zmitrovich  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are strong general-purpose code generators, but executable algorithmic trading remains a demanding specialization target: a model must translate a natural-language strategy specification into correct program logic for a specialized trading framework, execute on historical data, produce trades, and remain semantically faithful to the request. We study two complementary mechanisms for specializing language models for this setting: continued pretraining on algorithmic-trading framework code and supervised fine-tuning (SFT) on agent-validated request-to-code pairs. Evaluation is centered on QuantCode-Bench, our 400-task benchmark for Backtrader strategy generation, together with a repository-level SWE-bench-like track. Continued pretraining improves single-turn Judge Pass from 41.5% to 47.5% for Qwen3.5-397B-A17B and from 27.8% to 33.0% for Qwen3.6-35B-A3B. SFT applied after continued pretraining yields a larger gain for Qwen3.6-35B-A3B, reaching 58.2% Judge Pass and 83.5% successful backtests; in agentic evaluation it raises first-turn success from 22.3% to 58.3% and final success after up to 10 turns from 47.5% to 79.5%. Continued pretraining alone improves first-turn agentic success but lowers final success after repair from 47.5% to 32.5%, consistent with degraded instruction following, whereas SFT improves both. We also identify a capability-retention failure: domain specialization degrades parser-conformant structured tool calling, and targeted recovery SFT restores tool-call formatting but not the base checkpoint's repository-level agent performance. The results show that framework-oriented pretraining, validated SFT, and explicit capability-retention evaluation address distinct failure modes in domain-specific executable code generation.

---


### 246. [From Imitation to Reward Discovery: On-Policy Warmup for Agentic RL](https://arxiv.org/abs/2609.39436)

**<font color=#1a73e8>作者：</font>** Yitong Qiao, Tiantian He, Lei Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with a verifiable reward (RLVR) offers a scalable approach to training language-model agents, yet sparse outcome rewards can leave early training with little signal for policy improvement. We identify an On-Policy Acceleration Phenomenon: in our main comparisons, RLVR initialized with on-policy distillation reaches high performance earlier in training and achieves both higher average performance during subsequent RLVR and higher final performance than the alternative baselines. Motivated by this observation, we study On-Policy Warmup (OPW), a teacher-guided stage in which the student trains with teacher supervision on its own interaction trajectories before transitioning to RLVR. Unlike imitation on fixed teacher-generated trajectories, OPW targets states induced by the student's own decisions, including imperfect actions and recovery situations. We provide a theoretical explanation by connecting on-policy reverse-KL distillation to trajectory-level distribution matching. Under a competent teacher and sufficiently small population distillation loss, this connection yields a lower bound on initial verifier success and a corresponding bound on reward-discovery complexity. For group-relative RLVR, we further characterize when increased success probability produces more reward-informative groups. Together, our findings support on-policy distillation as an effective warmup for agentic RLVR and identify initial reward discovery as a mechanism that can contribute to the observed acceleration.

---


### 247. [Network-based Spatial Context Retrieval for Open-weight LLMs: A Faithfulness Benchmark for Grounded Geographic Reasoning](https://arxiv.org/abs/2609.39437)

**<font color=#1a73e8>作者：</font>** Joan Perez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) encode substantial latent geographic knowledge, yet they reason poorly over space and are unreliable when queried from coordinates alone. Useful behaviour emerges only when structured spatial context is supplied in the prompt. This raises a question geographic evaluation has left unexamined: once the right context is supplied, does the model reason from it, or override it with its own parametric recall? We take up this question with an open pipeline for network-based spatial context retriev-al. In it, the surroundings of a selected point are defined by the pedestrian street network, the area actually reachable on foot. Using only open data and open-weight models, the pipeline retrieves features from OpenStreetMap and the GHS-POP population grid, computes indicators over the network catchment in code, and injects them as a compact spatial brief. On this basis we build a faithfulness benchmark. It labels every claim a model makes by its source (grounded in the brief, or drawn from training knowledge) and its correctness, and it probes each case with a planted false premise that the brief refutes. We evaluate sixteen open-weight model configurations across three families (Qwen, Gemma and Llama, with Gemma in two generations), four size classes and, where available, both thinking and non-thinking modes, on three con-trasting cities, resampling every case over ten seeds. The results show that resistance to the planted premise varies more strongly by model family and generation than by scale, while brief-reading competence forms a partly separate dimension. These behaviours are not captured by conventional world-correctness scores or single-shot evaluation. We release the implementation, spatial briefs, model outputs, and claim-level labels as a reproducible workflow at this http URL.

---


### 248. [CAST: Causal Advantage-Structured Training with Spatially Grounded Compositional Rewards for Diffusion Models](https://arxiv.org/abs/2609.39441)

**<font color=#1a73e8>作者：</font>** Shu Yu, Chaochao Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Online reinforcement learning has been extended to flow matching for diffusion model (DM) image generation. However, this paradigm faces three limitations: (1) Window selection. Existing methods manually set the stochastic differential equation (SDE) sampling window, i.e., the denoising steps where exploration noise is injected. We instead determine it from each model's denoising trajectory. (2) Reward saturation. Current methods rely on scoring models trained on human annotations; we find that such scores are extremely high and nearly indistinguishable on the latest SOTA open-source DMs, making advantage estimation largely ineffective. (3) Sample inefficiency. A single scalar reward collapses different failure modes into almost identical scores, leaving minimal gradient guidance for targeted improvement. To address these issues, we propose CAST (Causal Advantage-Structured Training), an RL fine-tuning method for pretrained DMs, which (1) identifies the denoising step at which each model fixes the objects and their spatial arrangement in the image and uses that timing to set the SDE window, (2) decomposes each prompt via Causal Scene Graphs (CSG) into verifiable-atoms, i.e., minimal semantic units such as an object, count, attribute, or spatial relation that can each be checked independently, and rewards each atom separately, and (3) projects the signed atom-level advantages into pixel space through teacher-forced attention and uses them to spatially weight the SDE policy objective. We fine-tune two of the strongest open-source DMs, FLUX.2-dev and Qwen-Image-2512, with CAST, and evaluate them on GenEval 2, a compositional benchmark, and on Qwen-Image-Bench for overall quality. Within almost the same training budget, CAST's improvement over the base model on the most challenging GenEval 2 prompts is up to 3.07x that of Flow-GRPO, while overall generation quality also improves.

---


### 249. [Raw-Routed Mixture of Adapters: A Causal Intervention for Routing Collapse in Time Series Foundation Models](https://arxiv.org/abs/2609.39445)

**<font color=#1a73e8>作者：</font>** Hung Phan, Thuy T. Nguyen, Minh Ngoc Dinh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series foundation models (TSFMs) commonly adapt to new data by attaching a single trainable head to a frozen backbone, a one-size-fits-all setup that underfits heterogeneous regimes. Replacing the head with a mixture of experts is the standard upgrade, but on instance-normalized backbones (the dominant TSFM design class) it fails: routing entropy collapses to zero and one expert absorbs every input, a failure we call normalization-induced routing collapse. Standard MoE rescue mechanisms do not repair it, because the cause is in the router's input, not its optimization. Pre-encoder normalization strips the statistics a router would need to tell regimes apart. A mutual-information decomposition makes this precise and yields a signal-ratio that, computed before training, predicts dataset vulnerability (Spearman $\rho = -0.88$). Eight causal controls, including a vision-modality replication, isolate instance normalization as the cause. The prescription is a minimal causal intervention: Raw-Routed Mixture of Adapters (RR-MoA), which routes on the raw, pre-normalization input. Under a strictly frozen backbone, RR-MoA wins 54/54 comparisons against the strongest fixed adapter and significantly outperforms LoRA, TRACE, AdaMix, and full fine-tuning. The effect generalizes across six backbones and an imputation task. Frozen RR-MoA also beats full fine-tuning by 12-79% (the Frozen Paradox); two architecturally distinct variants confirm the principle generalizes beyond this specific router.

---


### 250. [Synthetic Data Characterization via Training Dynamics](https://arxiv.org/abs/2609.39447)

**<font color=#1a73e8>作者：</font>** Irene Lago, Ana Ezquerro, David Vilares  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Interpreting properties of LLM-generated data is important for understanding its utility and limitations across learning tasks. In this work, we characterize synthetic data through sample-level learnability, studying variation among LLM families and scales, alongside human-written data as a reference. We first generate synthetic datasets spanning single- and multi-label classification, labeling, and tree prediction tasks. We then derive empirical data distributions from encoder training dynamics for both machine and organic data, and estimate the robustness of these distributions across encoders. Finally, we evaluate how data selection strategies based on these learnability signals affect both data sources differently.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-390](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
