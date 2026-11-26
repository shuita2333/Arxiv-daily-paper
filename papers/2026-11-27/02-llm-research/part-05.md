# 🧠 大模型相关研究 | 2026年11月27日

> 本类共 **267** 篇论文：已确认 **249** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-267](./part-06.md)

---

### 201. [ADClaw: A Programmable Visual Agent for Industrial Anomaly Detection and Understanding](https://arxiv.org/abs/2611.34591)

**<font color=#1a73e8>作者：</font>** Xinyi Wu, Rongxin Gao, YuHui Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection (IAD), the task of identifying and localizing deviations from normal product conditions, is essential to automated quality inspection in manufacturing. Many vision-language models for IAD rely on large domain-specific datasets for fine-tuning and make predictions in a single pass, leaving no opportunity to re-examine ambiguous regions. Although tool-using agents can revisit these regions, predefined tool interfaces limit how they can combine intermediate results in a follow-up check. When such checks are insufficient, models may miss subtle defects or misidentify the defect type. To address this limitation, we introduce ADClaw, an inspection agent that uses executable code to test anomaly hypotheses without task-specific fine-tuning. For each hypothesis, a Structured Normality Prior identifies the applicable rules and retrieves normal visual references for the inspection target. Guided by this prior, the agent writes and executes code in a persistent Inspection Workbench to combine masks, anomaly maps, and measurements from earlier steps into a new test of the suspected defect. After each check, Hypothesis-Guided Evidence Reasoning assesses whether the evidence supports the suspected defect and its location, using gaps or inconsistencies in that evidence to guide the next code action. ADClaw achieves competitive results in detection and localization across 2D and 3D industrial anomaly detection benchmarks and in anomaly understanding on MMAD.

---


### 202. [SEAM: A Self-Evolving and Adaptive Probing Framework for Automatic MLLM Hallucination Evaluation](https://arxiv.org/abs/2611.34598)

**<font color=#1a73e8>作者：</font>** Shiyu Zhang, Zengyi Wo, Yuming Liao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The severe susceptibility of multimodal large language models (MLLMs) to hallucinations poses a critical threat to their reliability, making a rigorous evaluation framework indispensable. However, existing evaluation pipelines largely rely on predefined test items, suffering from high construction costs, rapid obsolescence as MLLMs evolve, and ineffectiveness in probing model-specific weaknesses. To address these limitations, we propose SEAM, a self-evolving and adaptive probing framework for automatic MLLM hallucination evaluation. Specifically, SEAM introduces a composable Hallucination Probe Construction Library comprising ten hallucination-probing skills, three elicitation wrappers, and five question formats. Building on this library, SEAM establishes a dual-loop framework. In the inner loop (adaptive probing), skill-guided visual analysis, question composition, and hierarchical quality verification are coordinated with verifier and target-response feedback to refine test items and uncover model-specific hallucinations. In the outer loop (skill evolution), a skill updater distills historical probing trajectories into localized, reusable rule updates, which undergo held-out validation and are frozen before testing. Driven by these innovative structural designs, SEAM establishes an automated and self-evolving evaluation paradigm. Experiments across four target MLLMs and ten hallucination types demonstrate that SEAM substantially outperforms representative static benchmarks, achieving an 89.2\% relative improvement in mean valid hallucination discovery rate across 12 matched comparisons.

---


### 203. [You Only Look Multiple Times: YoloMT, a Real-Time Streaming Model on a T4](https://arxiv.org/abs/2611.34601)

**<font color=#1a73e8>作者：</font>** Nessim Ben Abbes, Duc Han Le, Sabri Mtibaa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce a new model for real-time streaming captioning on a single GPU. YoloMT is a 449.8M-parameter streaming captioner that provides Pareto-frontier performance among generative vision models in its class. Distilled from a 27B teacher by SFT and GRPO, it leads every model under 1B parameters on OVO-Bench, MVBench, StreamingBench and Video-MME, answered from its captions, and beats LFM2.5-VL-1.6B and SmolVLM2-2.2B. YoloMT is designed to read more frames cheaply and make them informative, encoding each frame once and caching it as 16 tokens. This allows the model to incorporate and infer from past frames without additional vision passes, making it efficient and effective. We also provide a detailed recipe for training YoloMT, with its stages and data, as well as ablations that demonstrate the contribution of each component.

---


### 204. [VisualMontage: Manipulating the Beliefs of Vision-Language Agents with Authentic Image Sequences](https://arxiv.org/abs/2611.34603)

**<font color=#1a73e8>作者：</font>** Jinwei Hu, Lai Wei, Zhuoyun Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As agents based on vision-language models (VLMs) increasingly interpret social-media content, errors in their analysis may lend credibility to rumors and amplify their spread. In this paper, we study the problem of visual cognitive collusion, in which coordinated posts combine authentic images and locally faithful captions to induce VLM agents to infer and accept attacker-chosen target claims through their own reasoning. To enable systematic evaluation of this cognitive threat, we introduce a new benchmark comprising 544 target cases and 33.2K candidate images across eight application domains. We further propose VisualMontage, a multi-agent framework for simulating such attacks through narrative planning, image selection and ordering, and caption assignment under iterative review. We evaluate this threat through extensive experiments across 12 vision-language models, examining modality effects, production-team components, and downstream defenses. Using identical attack feeds across models without victim-specific optimization, we demonstrate cross-model transferability, achieving mean attack success rates of 61.93% for proprietary models and 68.71% for open-weight models. Moreover, 92.65% of generated feeds pass independent model-based validity auditing. Even after downstream review, residual attack success rates range from 35.3% to 76.7% across the evaluated configurations. Our additional controlled comparisons further reveal that captions can improve model-rated posting naturalness while reducing attack success. Together, these findings reveal a novel cognitive threat in social-media interpretation and motivate safeguards that assess how authentic posts jointly shape agents' reasoning and conclusions.

---


### 205. [Do We Really Need an LLM for Weight-Space Programming? A Deterministic Forward-Only Paradigm and Its Capability Boundaries](https://arxiv.org/abs/2611.34612)

**<font color=#1a73e8>作者：</font>** Lin Yao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work on Weight-Space Programming uses LLMs to edit neural weights with forward passes only, conflating LLM scripting with the underlying algebra of forward-only editing. We show that for core structured editing regimes, an LLM optimizer is unnecessary, and introduce Forward Weight-Space Programming (FWSP): a deterministic pipeline combining probing, localization, stratified operators (O1-O4), automatic blind routing (83.3% vs. 33.3% for a 27B LLM with the same tool library), and paired verification with zero additional per-token computation. For reasoning LLMs, we propose Protected FisherGate, a closed-form covariance-whitened readout edit orthogonal to normal-reasoning states: on DeepSeek-R1-0528-8B, a single frozen math-calibrated patch achieves 84.2% HumanEval pass@1 (1K budget; 75.4 +/- 9.4% across 3/5 Stage-4-passing subsets), beating 512-token-reserved budget forcing by +14.6 pp (-23.4% tokens) while transferring across HF-to-vLLM backends on full GSM8K and MATH-500. Across five modalities and thirteen models (50K to 27B dense and FP8 MoE), we further prove and verify two operator boundaries, subspace entanglement and frozen representation span, where FWSP-localized LoRA bridges forward-only and gradient adaptation.

---


### 206. [Commit2Drive: Perception-Grounded Language Decisions as Commitments for Trajectory Planning in Vision-Language-Action Driving Models](https://arxiv.org/abs/2611.34614)

**<font color=#1a73e8>作者：</font>** Zikai Zhang, Hubert P. Shum, Toby Breckon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models introduce language reasoning into end-to-end autonomous driving. They output a language decision together with a trajectory, which makes the planner more interpretable. However, in existing methods the language decision is either an independent output or an index that selects among similar candidate trajectories, and its annotations are not verified against the trajectory. As a result, the language decision and the trajectory are often inconsistent in closed-loop driving. To address this, we propose Commit2Drive, a framework that imposes the language decision as a consistency constraint on trajectory planning. The decision is a commitment, a maneuver class with a continuous parameter that one deterministic rule reads from any trajectory, and it is grounded in facts reported by the perception of the model itself. A Maneuver Bank maps the commitment to a code with a kinematic meaning, and consistency losses train the planner to execute every admissible decision of a scene, so that the trajectory follows the decision. An automatic data pipeline supplies the supervision. Decisions are labeled from the future motion of the expert, counterfactual executions train the decision and the trajectory together, and rule-based functions with a Vision-Language Model (VLM) generate, review and refine the language annotations. The code is a lookup that involves no hidden state of the language model, so Commit2Drive is extensible to rule-based decisions, which the same planner executes without retraining. Commit2Drive uses a 0.5B language model and runs closed-loop inference online on a single consumer graphics card. On Bench2Drive, Commit2Drive reaches a Driving Score (DS) of 78.50 and a Success Rate (SR) of 55.91% with a lightweight model, which is competitive with the state of the art, and greatly reduces the language-action inconsistency. Code will be released soon.

---


### 207. [From Models to Services: Systematizing Security Assurance for Model-as-a-Service](https://arxiv.org/abs/2611.34623)

**<font color=#1a73e8>作者：</font>** Jianming Zhou, Yang Luo, Guangpu Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are mainly delivered as cloud services, in which the assets of different principals are coupled within a single service pipeline, while the related security research is scattered across several fields with differing threat models. This paper systematizes this research from a service perspective. We decompose Model-as-a-Service (MaaS) into a five-layer stack and five trust boundaries, define six adversary classes and six security goals, use them to code 120 studies, and evaluate 50 defenses under a unified set of criteria. The results show that 44.2% of the studies concentrate on behavioral integrity, while service integrity, availability and cost, and accountability together account for only 13.3%. Defenses are evaluated on production services at less than half the rate of attacks, and none of the cryptographic or hardware mechanisms that protect against the provider can be adopted unilaterally by customers. Finally, we propose a research agenda by comparison with current standards and regulations.

---


### 208. [ZeroHero: Training Small Language Agents from Scratch](https://arxiv.org/abs/2611.34635)

**<font color=#1a73e8>作者：</font>** Nikita Sorokin, Zoya Volovikova, Alexey Skrynnik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large pretrained language models provide capable policies for interactive tasks, but how much model capacity is necessary for a specialized language agent? We introduce ZeroHero, a framework for training small language agents (SLAs) from scratch. In each environment, a large language model acts as the expert, and we collect its successful trajectories. We pretrain each SLA, which has fewer than 50 million parameters, to predict the expert's responses given the interaction history. We then post-train the agent on its own interactions using proximal policy optimization (PPO). During post-training, reasoning alignment supplements environment rewards with expert supervision on the language the agent generates alongside its actions. We evaluate the agents in three multistep environments where acting requires both understanding and generating language. In Crafter, agents interpret textual observations and generate reasoning before acting. In WebShop, they translate shopping instructions into search queries. In Alfworld-Dialogue, they ask clarifying questions and use the answers to guide household actions. The agents approach expert performance on WebShop and surpass their respective demonstration experts on Crafter training rollouts and held-out Alfworld-Dialogue tasks. An interactive demo is available at this https URL.

---


### 209. [REE: A Scientific Research Entrance Exam for AI Agents](https://arxiv.org/abs/2611.34646)

**<font color=#1a73e8>作者：</font>** Zeqi Zhou, Minghao Liu, Jiarui Liu 等 20 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous research agents are emerging as a promising approach to scientific problem-solving across disciplines, owing to their growing ability to improve a solution through repeated experiments. Evaluating this ability requires benchmarks that pose open-ended research problems and measure improvements over established scientific methods. We introduce REE (Research Entrance Exam), a benchmark that tests AI agents on scientific research. It consists of 100 open-ended research problems spanning five broad scientific areas and 23 domains. To ensure high quality, every problem is drawn from active research in its field and individually reviewed by domain experts. Each problem is posed as a task of iterative improvement: an agent has up to 12 hours to improve a working starter solution, and REE scores the result on a common scale against an established expert solution evaluated under comparable conditions. By this measure, two of the four frontier agents we evaluate, Claude Opus 5.5 and GPT-6.1 Sol, outperform the expert solutions on 86% and 81% of problems, across all five scientific areas. Their runs also show how they do so: both agents surpass the expert solutions within the first two hours on average, and their best solutions mostly tailor or combine established methods of the field. REE thus provides a unified framework for evaluating autonomous scientific research, capturing both improvements over established methods and the research processes behind them.

---


### 210. [Do We Still Need Reinforcement Learning When We Can Read the World Model?](https://arxiv.org/abs/2611.34656)

**<font color=#1a73e8>作者：</font>** Mingchao Zhang, Miduo Cui, Kangze He 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has achieved remarkable success in sequential decision-making, but learning effective policies often requires substantial interaction experience. Model-based reinforcement learning alleviates this dependence by leveraging world models, which are typically used to support planning or policy optimization. In this paper, we investigate an alternative paradigm in which autonomous LLM-based coding agents directly synthesize control policies by reasoning over readable world models. By examining environment source code, these agents translate environmental knowledge into executable decision rules and iteratively refine their policies using online feedback or offline data, without task-specific RL training. Experiments across diverse decision-making benchmarks show that synthesized policies match or outperform conventional RL methods while requiring substantially less experience. Further analyses reveal interpretable decision rules and how they evolve through feedback-driven refinement. Comparisons with policies generated without source code access and experiments under challenging conditions further demonstrate the benefits of readable world models. These findings suggest that direct policy synthesis can reduce reliance on trial and error, challenging the necessity of task-specific RL training.

---


### 211. [Counting Beyond Frames: Codec Motion Tells Frozen Diffusion VLMs How Many](https://arxiv.org/abs/2611.34657)

**<font color=#1a73e8>作者：</font>** Zhuoqin Li, Jiayu Ding, Ge Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counting how many times something happens is among the simplest questions about a video and among the hardest for video-language models, autoregressive and diffusion alike. The difficulty lies between the frames: a model samples only a few of them, while each repetition unfolds as movement in between. Video codecs already record this movement densely as block displacements, and codec-based video models use it to shape their visual input. We are the first to show that this motion provides direct evidence for the count: a candidate count is a testable motion hypothesis, and unwinding the cycles it implies measures how strongly the observed directions support it. We present CoDiCount, a unified training-free framework that turns this test into a count potential and applies it while a frozen diffusion vision-language model (dVLM) denoises its answer. At every denoising step, structured count messages map each option letter, or each grammar-valid edit of an open integer, to the count it expresses and reweight the model's own probabilities within that set. Consistent gains over the official decoders on MotionBench, TOMATO, and SVCBench demonstrate the broad generalization of CoDiCount across diffusion models, datasets, and diverse counting tasks. With CoDiCount, a 7B dVLM outperforms GPT-5.1 and Gemini-2.5-Pro on MotionBench, surpasses GPT-4o and much larger open models on TOMATO, and matches GPT-5.4 on SVCBench.

---


### 212. [Learning to Be Truncated: Preparing LLM Checkpoints for SVD Compression](https://arxiv.org/abs/2611.34667)

**<font color=#1a73e8>作者：</font>** Chenyue Fang, Danila Mishin, Babak Falsafi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compression based on singular value decomposition (SVD) often requires subsequent fine-tuning or weight correction to mitigate performance degradation. Budget-specific optimization must be repeated for different compression ratios. We introduce LLift, which prepares a pretrained model for SVD compression across ratios without further fine-tuning. LLift fine-tunes a low-rank approximation at a single ratio using the original model as a teacher. We merge the learned updates into the original weights while preserving the complementary components excluded from the training forward pass. We apply SVD to the prepared model's target matrices and reuse the decompositions at different truncation ranks. On LLaMA-7B, we demonstrate accuracy gains across three compression ratios using a single prepared model. The gains extend across model families, model sizes, and SVD compression operators. We analyze gradients and an early training update to provide local evidence that updates learned at one ratio can benefit compression at other ratios. These results show that LLift can improve compression across deployment budgets without fine-tuning each compressed model separately.

---


### 213. [Supporting Without Taking Over: AI Support in Gratitude Writing](https://arxiv.org/abs/2611.34673)

**<font color=#1a73e8>作者：</font>** Thu Bui, Shashi Salavath, Hillary Merzdorf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Gratitude writing can support well-being, but independent practice may lack guidance. Generative AI could help while shaping reflection, agency, and ownership. We investigated how gratitude-writing format and AI-assistance mode influence well-being and writing experiences. In a 2x2 between-subjects study (N=401), participants completed a gratitude reflection or a gratitude letter using two AI-assistance modes: scaffolding, which provided reflective questions after inactivity, or co-writing, which offered inline text suggestions. Participants' well-being improved after using our AI-assisted gratitude-writing system, consistent with the activity's intended benefits. However, participants' experiences revealed a trade-off between the AI-support types: co-writing received higher usability ratings, yet its immediacy could disrupt writing, and greater suggestion acceptance was associated with weaker perceived agency. Scaffolding supported stronger perceived human ownership but was sometimes overlooked. These findings extend human-AI writing research beyond productivity and text quality by showing how AI involvement shapes psychological outcomes and the experience of self-guided, emotionally meaningful writing.

---


### 214. [Find the Clue, Not the Scene: Rethinking Reasoning for Entity Recognition in Vision-Language Models](https://arxiv.org/abs/2611.34681)

**<font color=#1a73e8>作者：</font>** Kyungmin Min, Soyeon Kim, Junseok Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Answering a knowledge-based visual question requires first recognizing the entity in the image and then recalling knowledge about it. Thinking vision-language models (VLMs) reason for thousands of tokens before answering, yet it remains underexplored how well such thinking VLMs perform each of these two steps. We therefore analyze thinking VLMs on this task and make two key observations. (1) Recognition is the bottleneck, since 76.3% of errors across four models on ViQuAE stem from misrecognizing the entity, and 84.9% of these failures are resolved once the entity name is provided in the question. (2) Recognition is driven by entity-recall clues rather than by general descriptions of the image. An entity-recall clue is a distinctive visual detail that helps the model recall the entity, such as keys, a traditional attribute of Saint Peter. Based on these findings, we propose ClueRL, a reinforcement learning approach that extends Group Relative Policy Optimization (GRPO) with an advantage localized to the entity-recall clue in the thinking trace. Rather than injecting new entity knowledge, ClueRL changes how VLMs think: it leads them to attend more closely to visual details and spot these clues, helping them use the knowledge they already have. Consequently, it outperforms both GRPO and a perception-reward baseline on three entity recognition benchmarks. Moreover, this clue-seeking behavior generalizes beyond entity recognition, the only task used for training. Since recognition is the bottleneck, the gains carry over to knowledge-based visual question answering. They even extend to general multimodal reasoning, raising Qwen3.5-4B by 4.4 and 4.0 points on the ScienceQA and MMMU subsets of MMStar, respectively.

---


### 215. [Technical Report MEG2text: Beyond Alignment in Non-Invasive Brain-to-Text](https://arxiv.org/abs/2611.34686)

**<font color=#1a73e8>作者：</font>** Yiqian Yang, Yiqun Duan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Non-invasive brain-to-text seeks to recover language from brain activity without surgery. A central challenge is turning learned brain-language representations into accurate word predictions. We present MEG2text, a decoding system that combines corrected training and evaluation, brain-text alignment, a class-balanced word readout, and target-word language-model fusion. On LibriBrain100's word-ranking task, MEG2text reaches 64.12% mean Top-10 balanced accuracy, improving on published MEG-XL by 16.92 percentage points across four corpora, with gains on each corpus. Controlled comparisons show that both implementation corrections and a learned readout contribute to this improvement. Candidate-level analysis reveals that some words receive informative scores yet consistently lose to competing candidates, while an identical-feature comparison shows that learning the classification rule improves decoding without changing the representation. These findings identify the decoding rule as a consequential part of non-invasive brain-to-text and show how system improvements can make better use of aligned neural features.

---


### 216. [A Failure-Driven Data Flywheel for Post-Training Vision-Language-Action Models](https://arxiv.org/abs/2611.34698)

**<font color=#1a73e8>作者：</font>** Yuhao Luo, Zihao Sheng, Zilin Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained vision-language-action (VLA) models rarely satisfy all behavioral requirements of a new platform, and teams without a large deployed fleet lack the data to address the resulting failures. We propose a failure-driven data flywheel for post-training such models. It constructs target scenarios absent from the available data by inserting task-relevant entities into reconstructed real-world scenes, and evaluates the model against each behavioral requirement of the target task. Failure rates form a failure map across task conditions and difficulty levels, which is re-evaluated after each round and assigns larger data generation quotas to conditions where the model still fails. We instantiate the framework in autonomous driving for occluded-pedestrian emergence and yielding at stop-sign-controlled intersections, and evaluate it on two VLA models and one non-VLA planner in simulation and on a real vehicle. For occluded-pedestrian emergence, five rounds of post-training improve the critical-phase collision-free rate on the sealed test set from 0.261 to 0.579 for AutoVLA and from 0.390 to 0.765 for ReCogDrive, while the unnecessary braking rate in paired control scenarios never exceeds 0.013. On a full-scale vehicle without real-world training, post-trained ReCogDrive achieves 4 of 5 safe passages, versus 1 of 5 for the base model. Fine-grained evaluation reveals a pattern obscured by the collision-free rate alone: both VLA models learn anticipatory deceleration before reaching the occluding vehicle, while braking after pedestrian emergence remains limited. For stop-sign yielding, the stop-before-line rate rises from 0.100 to 0.897 for AutoVLA and from 0.000 to 0.667 for ReCogDrive. With sequential training from the pedestrian-capability models, it reaches 0.599 and 0.358, respectively, while the pedestrian collision-free rate decreases by at most 0.032.

---


### 217. [Seeing the Right Context: Grounded On-Policy Distillation for Remote Sensing](https://arxiv.org/abs/2611.34700)

**<font color=#1a73e8>作者：</font>** Yichang Luo, Hourun Zhu, Shixiong Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing scene understanding requires multimodal large language models (MLLMs) to interpret queried targets in relation to nearby objects and surrounding structures, which serve as spatial references or define the scope of an answer. However, standard answers and bounding boxes often leave these contextual relationships implicit. Thus, we construct GeoContext-5K to make them explicit in 5,394 training pairs for visual question answering (VQA), with spatial cues, visual facts, and supporting regions. GeOPD uses these annotations for on-policy distillation, guiding a frozen teacher with region marks on the full image and a visual fact while preserving surrounding spatial references. It prioritizes teacher corrections that agree with the shift in the student's next token distribution when evidence is restored. A complementary objective weights the contrast between the student's scores on the two views by how much masking lowers the teacher's log probability for the same sampled token. Experiments on five remote sensing VQA benchmarks show that GeOPD outperforms the evaluated open-source MLLMs and matched post-training baselines, improving over the 4B and 9B base models by 5.81 and 2.97 percentage points on average. The dataset and code will be publicly released at this https URL.

---


### 218. [Maco-RL: Scaling Agent Capabilities with Mixed-Task Reinforcement Learning](https://arxiv.org/abs/2611.34703)

**<font color=#1a73e8>作者：</font>** Jiacheng Zhang, Qixing Zhou, Haiyang Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixed-task reinforcement learning (MixRL) directly trains a unified policy across domains to continually expand agent capabilities without training separate specialists or requiring an extra distillation stage. Despite its appeal, scaling MixRL poses significant challenges in achieving stable and efficient mixed-task learning, effectively allocating rollout compute, and supporting continual domain expansion. To address these challenges, we propose Maco-RL, an approach that effectively scales MixRL. Specifically, Maco-RL employs a quota-based scheduler for asynchronous rollouts across multiple task domains, thereby stabilizing training by balancing gradient contributions and mitigating off-policy effects. Along an orthogonal axis, Maco-RL further introduces Tri-Buffer Sampling (TBS) to allocate compute among samples with varying levels of mastery, promoting sustained frontier exploration while preserving acquired capabilities. Experiments on five benchmarks show Maco-RL raises Qwen3.5-27B's overall score from 43.6 to 54.2 and then to 60.1 with continual expansion, reaching the frontier held by Qwen3.8-27B, which is further pushed outward by +5.7. Maco-RL also outperforms single-task RL with less compute for policy updates. These results support MixRL as a practical and compute-efficient post-training approach with substantial potential to strengthen general agent capabilities.

---


### 219. [Spec2Weights: Certifying Networks that a Language Model Writes from a Specification](https://arxiv.org/abs/2611.34711)

**<font color=#1a73e8>作者：</font>** Soumik Bhattacharjee, Musa Tur Farazi, Md Nasir Uddin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A language model can write the weights of a small MLP, CNN, RNN or GNN from a plain-language specification, with no data and no gradient step. We ask when such a network can be proved exact in the float32 arithmetic it actually runs in. A float-safety lemma makes exhaustive float32 enumeration a proof for any summation order, and a layered error bound covers networks whose weights are not short binary fractions. With dynamic programming, template checks, an SMT proof, breadth-first search and induction for weight-tied recurrences, this certifies 12 of 15 written networks (one after a single constant fix) on every input of a stated domain (up to $10^{16}$ inputs, or every graph or grid up to a size bound), in a minute of CPU or less each. The certificates also say where a network stops being exact: the shortest-path network is exact iff the distance is at most 4,096 and fails at the predicted hops. Thirty new specifications were each written by a fresh session of one model family (Claude Opus 5.5). Twenty-five first submissions are certified exact for any summation order; the five tax schedules stay within \$0.11 of the true tax at every whole dollar in one fixed float32 run. An open 27B model passes 23 of the 30, and 25 with more thinking and code execution, so the method transfers in part. We also prove two limits of learning from examples: input coordinates never active in training cannot be learned from more in-range data, and Luhn-type checksums have exponentially small target-dependent gradient variance across their family. Tuned gradient descent on the same architectures agrees with both, which cover two of our five failure classes.

---


### 220. [Privileged On-Policy Distillation for Calibrated Alzheimer's Diagnosis With Missing Modalities](https://arxiv.org/abs/2611.34721)

**<font color=#1a73e8>作者：</font>** Vo Minh Khoi Nguyen, Dat Tien Chung, Quang Minh Khoa Le 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease is diagnosed from clinical, biospecimen and imaging evidence, but few patients undergo every test. Because these modalities are complementary, a missing one has many plausible values. Most existing methods leave it out or train on one estimate, so their classifier never sees its other values, and the estimate is never checked against the diagnosis. We address both gaps with on-policy distillation: the model fills in the missing modalities itself, and teachers with information available only in training grade these fills. Our method, Graded Rollout Imputation with Privileged teachers, draws several fills, one modality at a time. An imputation teacher that knows the diagnosis grades each step, bringing the outcome into the imputation as statistical practice recommends. A diagnosis teacher that sees all real modalities supplies a soft target. Trained on fills that vary, the model learns a confidence that reflects what the missing tests leave open, and it diagnoses from a single rollout. On the Alzheimer's Disease Neuroimaging Initiative cohort, it outperforms state-of-the-art baselines. On two external cohorts, it remains competitive in discrimination and, even after every method is recalibrated, its calibration error is level with the lowest on both. Added to three of these baselines, the teachers improve each of them. Our method offers a single, well-calibrated model for whatever combination of tests a patient has received.

---


### 221. [What Is a Theory Worth to an LLM Solver? Measuring, Inducing, and Merging Theories in Context](https://arxiv.org/abs/2611.34751)

**<font color=#1a73e8>作者：</font>** Jun Gao, Shuchao Bi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mathematicians solve problems faster when they know the right theory. We ask how much a stated theory is worth to a large language model (LLM) solver, and whether a model can write that theory itself. In a length-matched protocol, adding the right theory to the context of Qwen3-14B raises pass@1 on pattern waiting-time problems from 0.37 to 0.83 and cuts the median tokens of correct solutions from 10.2k to 6.3k, while worked examples of the same length do not help. The gain shrinks as the solver and its token budget grow (+0.46, +0.26, +0.07), and at a long budget it comes almost entirely from finishing within budget: solutions that finish are correct 98--100\% of the time in every condition. To separate induction from recall, we plant unpublished theorems in custom probability families and measure how much of the oracle theory's gain an induced theory recovers. A strong open model, required to explore the training problems with code before writing, recovers 60\% of the gain on one planted family, 48\% on a second, and almost none on a third, where it finds the right form but not the condition that makes the form computable. No single induced note is complete, but a strong model that merges several notes recovers 61\% of the gain on the classic family, above the best single note (47\%). Theories are worth the reasoning they save, and models can find their pieces before they can assemble them.

---


### 222. [Collect for Coverage, Replay with Evidence: Adaptive and Efficient On-Policy Distillation for Long-Horizon Agents](https://arxiv.org/abs/2611.34756)

**<font color=#1a73e8>作者：</font>** Haowen Hou, Gen Li, Ruilin Li 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fully online on-policy distillation (OPD) is costly for long-horizon agents because each update depends on fresh environment rollouts. Prefix replay offers an efficient alternative by sampling current-student responses from stored histories, reducing idle time for long-tail rollouts and allowing each collected trajectory to support multiple updates. However, our analysis of the complete prefix replay pipeline identifies two limitations in long-horizon settings. In trajectory collection, teacher-only trajectories miss student-induced histories, while broader history coverage can reduce teacher reliability. In trajectory reuse, fixed position-based schedules cannot identify critical decisions that may occur at any trajectory depth. We introduce CARE-OPD (Collect for coverAge, Replay with Evidence) to address both limitations. Student-seeded teacher completions and response-level confidence gating expand history coverage while filtering unreliable updates. Hindsight replay allocation then uses downstream execution evidence to select consequential turns. Across long-horizon tasks Software Engineering and Deep Research, CARE-OPD outperforms online OPD and prior prefix replay baselines. On SWE-bench Verified, it raises task success to 59.5% while reducing end-to-end training time by 45% and environment actions by 44% relative to asynchronous online OPD.

---


### 223. [One Model, Many Modes: Evolving System Prompt Ensembles for Creative Generation](https://arxiv.org/abs/2611.34760)

**<font color=#1a73e8>作者：</font>** Daiwei Chen, Anda He, Binwei Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Preference-aligned LLMs can exhibit mode collapse, concentrating their output distributions around a narrow set of high-reward responses. This limits creative generation, which requires quality, novelty, and diversity. Existing test-time methods often emphasize diversity, giving less attention to whether individual responses are both high-quality and novel. This distinction matters in practical use, where users may seek a single compelling, original response. We formalize creative generation as a multi-objective distributional optimization problem and introduce SEPO, a training-free framework for System Prompt Ensemble Optimization. The framework combines prompt evolution with greedy max-min selection to identify behaviorally distinct system prompts under a quality constraint, then uniformly samples one prompt per response at inference time. Across four creative generation tasks with increasing quality requirements and three open-weight models, SEPO ranks first in 8 of 12 settings on the harmonic mean of quality, diversity, and novelty, while no baseline leads in more than two. On average, it raises LLM-judged diversity from 1.92 to 3.43 and novelty from 1.00 to 3.34 over base sampling (1-5 scale), with quality decreasing from 3.72 to 3.30. We further show that expanding the optimized ensemble increases separation among prompt-conditioned response distributions. These results support system prompt ensemble optimization as a promising approach to improving LLM creativity at inference time.

---


### 224. [TASK Memory: Beyond Text-Only Memory with Activation Steering and Knowledge Editing against Memory Hallucination](https://arxiv.org/abs/2611.34762)

**<font color=#1a73e8>作者：</font>** Jinkun Zhao, Wenjun Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on external memory, yet they still hallucinate about what they remember. Often the correct memory is retrieved and placed in the prompt, but the answer contradicts it or the memory is applied to the wrong question. We call these use-time memory hallucinations. Across five open models, we find that they arise from the conflict between parametric knowledge and external memory and take three forms: memory-ignoring, where the model returns to a stale fact in its weights (up to 46% of queries); memory-misapplying, where it attributes the memory to unrelated entities (up to 24%, and 49% when retrieval is combined with weight editing); and version confusion, where 53% of answers about revised facts assert the superseded value when both versions remain stored. We propose TASK memory, which goes beyond text-only memory by combining a Text note with Activation Steering and Knowledge editing that share one in-model address. The text holds the content. A removable knowledge edit supplies the address through its subject key and supports multi-hop composition. A pair of steering vectors decides, query by query, whether the model adopts the memory or keeps its own answer; the vectors store no content and control how the text memory is used. On frozen models under a pre-registered, test-once protocol, TASK reduces memory-ignoring hallucinations to at most 1.5% in all ten model-dataset cells and cuts neighbour misuse from 39.2% to 7.5% (+10.8 pp composite on CounterFact). It improves a 300-memory library over BM25 RAG by 16.4 pp, an advantage that holds at 3,000 memories, resolves fact revisions without fact IDs, and adds 7.5 pp of multi-hop accuracy on MQuAKE. 21 of 23 cross-model comparisons (8B-27B, four families) are significant, and TASK beats three recent context-steering methods in 9 of 10 model-dataset cells.

---


### 225. [Make the Adversary Spend More: Stateful Deception as a Cost-Exchange Primitive for AI-Era Cyber Defense](https://arxiv.org/abs/2611.34770)

**<font color=#1a73e8>作者：</font>** Alessandro Cantelli-Forti, Isabella Marasco, Hosam Alamleh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are transforming the economics of intrusion by reducing the attacker's cost to scan and adapt, while tempting defenders into unbounded compute. We argue that cyber deception should be judged by the cost exchange it imposes, not by realism or detection, and that the primitive making that exchange favorable is adversary-specific persistent state. Rather than a honeypot that resets or merges sessions, each recognized adversary re-enters the world it believes it has compromised, kept coherent with its own past actions and isolated from every other adversary, while the language model acts only as a constrained renderer of explicit state, never as its store. We formalize the trade-off as a Deception Exchange Rate (DER), relating mission-weighted adversary effort burned to defender resources spent, and instantiate it in an SSH honeypot pairing Cowrie with a local LLM. In this paper, we focus on the defender-side evaluation of that exchange, while specifying, but not yet measuring, per-adversary state and the adversary side of the DER. Across five open-weight models, deterministic-layer and prompt optimizations cut per-session defender cost by around 63% against a naive all-LLM decoy.

---


### 226. [DFly2: Turbocharging Long-Context Speculative Decoding by Sharing the Target's Sparsity](https://arxiv.org/abs/2611.34776)

**<font color=#1a73e8>作者：</font>** Hong Liu, Rui Cen, Junhan Shi 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To avoid the quadratic cost of dense attention over long contexts, models such as DeepSeek-V4 and Hy4 have turned natively sparse, and speculative decoding, which matters most where decoding is slowest, increasingly runs on them. Their drafters, however, still keep a context cache of their own, over the whole prompt or a sliding window. Beyond memory, such a cache costs prefill time, prefix-cache hits and decode concurrency. Drafters that read the target's cache avoid one of their own, but settle only which cache, not which positions, and still read everything or a recent window. Neither rule is made for the query at hand, and computing a selection per query in the drafter would cost more as the context grows. Yet a natively sparse target already picks positions for each query, over a cache it keeps anyway. Both of the drafter's choices are therefore already made, and paid for, by the target: its cache and its selection. We measure how far one selection carries: made a step early, it still covers close to nine tenths of what each later token selects on DS-V4.1-Flash. We present DFly2, a block-parallel drafter that shares the target's sparsity. Each draft layer reads the KV its paired target layer cached (KV sharing), at the positions that layer's indexer selected, a fixed number anywhere in the context (Index sharing). DFly2 thus runs no scoring pass and keeps no cache of its own. On DS-V4.1-Flash, GLM-5.3-Flash and Hy4~flash, whose sparse attention and architecture differ, it accepts more tokens per step than DFlash and DSpark trained on the same recipe, over general, long-context and agentic benchmarks. Its margin over the stronger baseline widens from 3.9%-10.5% on general workloads to 10.0%-31.5% on long-context and agentic ones. At high concurrency on DS-V4.1-Flash, at matched per-user decode speed, its throughput is 62% and 81% higher on two 64K sets.

---


### 227. [SceneDesigner3D: Agentic Evolutionary Search for Principled Rearrangement of 3D Indoor Scenes](https://arxiv.org/abs/2611.34783)

**<font color=#1a73e8>作者：</font>** Chandan Yeshwanth, Angela Dai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene rearrangement is an essential task for 3D content creation applications, requiring generation of diverse, aesthetic and functional scene rearrangements. We present SceneDesigner3D, an agentic evolutionary search method for 3D indoor scene rearrangement that systematically explores the design space of 3D scenes and generates multiple solutions according to common interior design principles. Given an input scene and a text prompt, SceneDesigner3D represents the rearrangement as an editable program and evolves a population of candidate layouts. Starting from distinct design ideas, a VLM agent mutates the programs by refining promising candidates, exploring new rearrangement strategies or redesigning from scratch, while verifying the layouts for physical validity. Proposals are scored by a VLM judge for adherence to the input prompt and satisfaction of design principles such as balance, zoning and emphasis, as well as numerically computed principles such as circulation and clutter. An archive of top-performing, structurally varied candidates further increases diversity of rearrangements. Experiments on the SAGE-10k and SceneSmith datasets show that SceneDesigner3D improves prompt adherence and computed design principle scores over baselines by up to 5.1% and 15.2%, respectively. Code will be made publicly available.

---


### 228. [PersonaFactory: Stylistic User Prompt Augmentation with Synthetic Persona Bank](https://arxiv.org/abs/2611.34785)

**<font color=#1a73e8>作者：</font>** Bich Ngoc Doan, Hanna Yukhymenko, Imanol Schlag  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly replace real people in the AI development pipeline, as they are used to generate training dialogues at scale and to drive alignment and evaluation. However, out-of-the-box models produce monolingual and stylistically flat texts as synthetic user prompts, failing to replicate the real user-AI communication mechanics. We present PersonaFactory, an end-to-end pipeline that generates detailed user personas and uses them to augment existing user prompts from their point of view, producing a bank of over 740000 structured synthetic personas detailing their background and communication behaviors, and a corpus of roughly 1.24 million persona-styled synthetic conversations spanning 85 languages. We evaluate the effect of personal features on style adoption and intent preservation, using an LLM-judge and heuristic metrics to assess augmentation fidelity together with the downstream impact on assistant persona control through training data. Results show that our structured, attribute-based style representation enables per-axis control and better intent preservation at comparable style fidelity than free-text persona descriptions used in existing methods. A human expert evaluation found the augmented conversations plausible, with favorable ratings for intent preservation, style naturalness, and multilingual authenticity. Finally, PersonaFactory conversations achieve comparable performance to original training data on capability benchmarks, are preferred on real user prompts at equal reply length, and adapt their reply style more closely to users without explicit steering.

---


### 229. [Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video Models](https://arxiv.org/abs/2611.34813)

**<font color=#1a73e8>作者：</font>** Dezhi Luo, Fengyuan Yu, Haotian Zhang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models are increasingly evaluated as visual reasoners: given a first frame and a natural-language prompt, can the model produce the video in which the specified task is carried out? The paradigm is considered advantageous because the reasoning is native to the visual medium, unfolding directly in the frames rather than through language or code. Whether this native route is in fact the more reliable path to visual reasoning has not been tested against a symbolic alternative under the same conditions. We therefore pose the same tasks, with identical inputs, output specification and evaluator, to both media: rather than denoising pixels, a coding agent writes a program that renders the answer video, which an unmodified rule-based evaluator scores. On VBVR-Pro-Bench (Xu et al., 2026), a 500-instance suite spanning five cognitive categories with symbolic ground truth, the agent receives the same first frame and prompt as the video model, with no access to ground truth, metadata or generation models, and one attempt per instance. Three closed-model agents (Codex with gpt-6-astra, Claude Code with Fable 5.1 and Gemini CLI with Gemini 3.1 Pro) score 0.923, 0.894 and 0.893, each more than 0.22 above the strongest video model. Among 23 runnable open-weight models, the best, GLM-5, reaches 0.572, above all video models except the RL-trained one. Together, we show that for tasks whose solutions can be computed from a first frame and a prompt, program synthesis is currently a substantially more reliable route to visual reasoning than video generation. We further distinguish depictive programs, which navigate the image to recover a transferable scheme, from propositional programs, which operate on hard-coded values, revealing how visual reasoning unfolds in agent-written programs and what it implies for its nature of reasoning in general.

---


### 230. [VulnSafe: Measuring Vulnerability-Aware Relational Safety in Large Language Models](https://arxiv.org/abs/2611.34819)

**<font color=#1a73e8>作者：</font>** Jiaming Luo, Jiacheng Ji, Haoan Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotionally supportive interactions require large language models not only to avoid overtly harmful content, but also to recognize vulnerability-related risk, regulate their relational stance, preserve user agency, and provide context-appropriate support. Existing safety benchmarks often measure isolated violations, leaving unclear what underlying response competence their scores represent. We introduce VulnSafe, a Chinese capability assessment centered on Vulnerability-Aware Response Competence (VARC). VARC organizes relational safety into five complementary constructs: Risk Perception, Safety Preservation, Autonomy Protection, Supportive Response, and Boundary Management. Following an evidence-centered design, 41 scenarios elicit construct-relevant behavior through 2,050 balanced prompts and scenario-specific scoring rubrics. The assessment further separates proactive should-do behavior from prohibitive should-not behavior. Across eight representative LLMs, results show distinct competence profiles and larger disparities than prohibitive requirements. VulnSafe therefore makes relational safety interpretable as a multidimensional model capability rather than as refusal compliance alone.

---


### 231. [LoopTitan: What Does Parameter Revisit Buy a Mixture-of-Experts?](https://arxiv.org/abs/2611.34821)

**<font color=#1a73e8>作者：</font>** Zichen Tian, Yudong Lu, Xuansheng Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Mixture-of-Experts (MoE) architectures revisit layer parameters across depths. This design increases effective depth without adding parameters. Recent looped MoE studies report substantial gains over the standard MoE at matched budgets (parameters, FLOPs and KV cache). However, the reported gains still confound parameter revisit with other design choices, e.g., network shape and residual scale. We ask, what does parameter revisit itself buy? Using matched non-revisit controls, we find that parameter revisit itself buys almost nothing. We argue that revisit only offers a freedom an MoE already has, i.e., trading experts for depth (more layers, fewer experts each) at fixed parameters. First, at matched budgets, we decompose the state-of-the-art looped recipe, with revisit last. A non-revisit control retains all the gain. Most comes from network shape, and the rest from residual scale. We prove this scale acts as a lower learning rate on revisited layers. This helps under AdamW's uneven layer step sizes, but disappears under Muon, which keeps them nearly equal. Second, beyond matched budgets, we evaluate revisit by adding compute at fixed parameters. One extra visit gains more than doubling the experts. Yet without revisit, a deeper standard MoE at equal parameters and compute obtains 90.2% of that gain under Muon. Overall, gains come from network shape, the optimizer and added compute, which a standard MoE can adopt. Accordingly, we propose LoopTitan-Base as a stronger MoE baseline. Under Muon, it matches the strongest looped recipe without revisit or residual scale. We open-source LoopTitan and release 17 pretrained models (including LoopTitan-Base and the control). Our experiment record is public as GitHub issues, with predictions pre-registered and the full exploration history kept. This is our Phase 1 technical report, laying the foundation for follow-up studies.

---


### 232. [The Linguistic Knowledge Benchmark: Do Language Models Know the Foundations of Early-Grade Literacy?](https://arxiv.org/abs/2611.34823)

**<font color=#1a73e8>作者：</font>** Maxime Lelièvre, Alasdair Mackintosh, Dominic Andrews 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many languages of instruction in low- and middle-income countries (LMICs) are poorly represented in the data used to train language models. Before these models can support early-grade literacy in such languages, we need to know whether they hold the linguistic knowledge of each language that literacy teaching relies on. To test this, we present the Linguistic Knowledge Benchmark and the reproducible, largely automated pipeline that turns curriculum documents, teacher guides and pupil books into a vetted question set organised on a fixed grid of nine linguistic domains and seven grade levels. The pipeline combines LLM-driven source survey, feature consolidation, item generation and quality control with an item-selection step inspired by item response theory and a final expert review. We instantiate it for Kiswahili (Kenya; 135 items) and English (United Kingdom; 137 items) and evaluate 121 and 119 models respectively. Frontier models exceed 90% accuracy in both languages, but accuracy falls steeply for smaller and cheaper models, and more so in Kiswahili. The two best models under 10 billion parameters reach 91.7% and 73.0% in English but only 51.9% and 40.7% in Kiswahili, and the mean accuracy of models deployable on mobile and tablet hardware is 47% in English against 24% in Kiswahili. The models most practical for low-resource classrooms are therefore the least capable in the languages they would serve. We release a 20-item sample per language, all pipeline prompts, open-source code, and a public leaderboard. This is the first rung of a three-level evaluation ladder for measuring and generating decodable text to support foundational literacy.

---


### 233. [Routeability Before Routing: Routeability Audit Protocol (RAP) and RouteabilityBench for Audited LLM Model Selection](https://arxiv.org/abs/2611.34825)

**<font color=#1a73e8>作者：</font>** Yihang Lu, Denica Kjorvezir, Ana Gjorgjevikj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM routing aims to choose, for each prompt, which model in a portfolio is most likely to answer correctly. This only makes sense when the benchmark contains enough prompt-specific variation for different models to be best on different inputs. On coarse-scored LLM benchmarks, however, many models often tie for the best score, and the single best model may already leave little room for improvement. We therefore propose a routeability-first audit, instantiated as RAP and RouteabilityBench, a runnable claim-verification package. The audit is retrospective: it runs once the benchmark-portfolio score matrix exists and before router comparisons are interpreted as general evidence, rather than certifying a portfolio that has not yet been evaluated. Across four benchmarks and 66 LLMs, generic routing enhancements such as larger embedding sets, dimensionality reduction, selective abstention, clustering, and stronger regressors do not consistently outperform the single best model. The clearest positive evidence is concentrated in portfolio-dependent Omni-MATH settings, while GPQA, MMLU-Pro, and IFEval show different ways in which routing can remain hard or predictor-sensitive. Our practical recommendation is that routing gains should be reported together with routeability diagnostics, tied-best analysis, portfolio construction details, and family-corrected statistical tests.

---


### 234. [Repairing the Trustworthiness of Distilled Language Models](https://arxiv.org/abs/2611.34831)

**<font color=#1a73e8>作者：</font>** Kumar Shubham, Devendra Vyas, Vidushi Agarwal 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation enables the deployment of large language models through smaller student models, but the compression process can introduce regressions in trustworthiness even when downstream performance is preserved. Repairing such failures is challenging because the original distillation corpus is often unavailable, while direct preference optimization may alter capabilities inherited from the teacher. We propose a targeted repair framework based on the proximal Bregman response function (PBRF) that addresses both limitations. We estimate the curvature required for PBRF using a surrogate proxy dataset, removing dependence on the original transfer corpus, and extend the framework to preference-based supervision through an odds-ratio objective. This enables the use of preferred and dispreferred response pairs while constraining changes to the distilled model. Our results show that the proposed approach improves targeted trustworthiness behaviors for both pre-training and post-training models while largely preserving downstream performance, providing a practical alternative to re-distillation or unconstrained preference optimization. Our experiment results show that across different distilled models, the trustworthy regression can be improved by up to 8% with less than 1% decrement in perplexity.

---


### 235. [Proverbs As A Window On Collective Prescriptions](https://arxiv.org/abs/2611.34832)

**<font color=#1a73e8>作者：</font>** Tomás Lejarraga, Dirk U. Wulff, Ralph Hertwig  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Proverbs, as repositories of traditional wisdom, have informed human reasoning for millennia. Yet the collective prescriptions they encode have remained largely unquantified. We introduce a computational framework to analyze nearly 50,000 English-language proverbs. Using large language models, validated against human judgments, we map the topical landscape of proverbs, assess their prescriptive power, and quantify their recommendations on key dimensions of human judgment and behavior. We find that most proverbs are prescriptive, offering guidance in domains under individual control, such as preparation and prudent action, whereas proverbs about uncontrollable circumstances, such as fate and mortality, tend to describe rather than prescribe. When prescriptive proverbs take a consistent stance, they favor caution over risk, long-term over short-term outcomes, honesty over deception, and kindness over malice, and show a moderate tendency toward suspicion over trust. On dimensions involving genuine trade-offs, especially autonomy versus compliance, proverbs provide contradicting advice rather than a single recommendation. This analysis provides a quantitative map of the collective prescriptions in a culture's proverbial wisdom, revealing a core of prudent, honest, and forward-looking guidance alongside varied advice where circumstances dictate the best course of action.

---


### 236. [Knowledge-Base Gradient Descent: Self-Structuring Learning through Question Answering](https://arxiv.org/abs/2611.34841)

**<font color=#1a73e8>作者：</font>** Masahiro Kato  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We consider the problem of constructing knowledge bases for applications based on large language models, in which the structure of a knowledge base determines how an application can retrieve and connect the information needed to answer a question. We study Self-Structuring Learning, a setting in which questions and expected answers guide the construction of a persistent knowledge base whose editable structure can be a graph schema or the organization of linked knowledge documents. We propose Knowledge-Base Gradient Descent, which diagnoses discrepancies between expected answers and responses obtained through the current knowledge base. At each round, the method proposes a structural edit, rebuilds the knowledge base, and adopts the edit when the learning loss decreases. The retained structure is evaluated on other questions about the same sources. By randomizing over candidate edits, we express the loss change of an edit as a derivative with respect to the probability of selecting it, and we evaluate joint edits as single candidates because their changes interact. Schema Descent instantiates the method for graph schemas. In experiments on large documents, each a bundle of research papers, the updated knowledge cards and graph schemas obtain higher mean Answer F1 on held-out generated questions than their initial structures, with schema gains in every document. On human questions, mean F1 rises for schemas and falls for cards: the updated structures serve the kind of question they were learned from.

---


### 237. [Probing Visual Idiosyncrasies in Text-to-Image Models](https://arxiv.org/abs/2611.34843)

**<font color=#1a73e8>作者：</font>** Yongqian Peng, Hongjie Li, Yichao Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-Image (T2I) models turn short text descriptions into images, and the leading models now produce images of comparable visual quality. Whether their outputs still carry model-specific characteristics matters for attribution, for model comparison beyond aggregate quality, and for evaluations that assume anonymity. We ask whether images from frontier T2I models can still be classified by source, and which visual properties make this possible. Here we show that a standard ResNet-50 identifies the source of an image among HiDream-O1-Dev, FLUX.2-dev, HunyuanImage-3.0, and Qwen-Image-2512, the four highest-ranked open-source models on the Text-to-Image Arena, with 100.00% accuracy on held-out prompts. Human participants reach only 62.61% on the pairwise version of this task, so the distinguishing cues are not visually obvious. They are also not tied to a particular classifier and survive severe image corruptions and out-of-distribution prompts. We trace them to visual idiosyncrasies at three levels. Low-level texture statistics alone let a lightweight multi-layer perceptron match ResNet-50. Object layout, depth, and albedo estimated from the images each carry a source signal. Image captions reveal model-specific preferences in style and background that the prompts never specify. A one-sentence hint about these cues raises human accuracy by 9.03 percentage points. These idiosyncrasies make source classification a tool for measuring similarity between models and between real and generated images, and they caution against assuming anonymity in human preference evaluation of T2I models.

---


### 238. [Put the World Back: Timestamps Matter in Time Series Reasoning](https://arxiv.org/abs/2611.34848)

**<font color=#1a73e8>作者：</font>** Tingrui Huang, Yuanyuan Deng, Qingren Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly applied to time series reasoning. However, current evaluations often give models events in chronological order and already matched to the time series. This makes it unclear whether models use timestamps to connect events with observations or simply take shortcuts. To expose this ambiguity, we reformulate time series reasoning from a world-to-series projection perspective, viewing timestamps as explicit indices that connect numerical observations and external events to shared world states. We identify three structures that timestamps can make explicit: temporal causal structure, time semantics, and event-series alignment. Building on this perspective, we develop a diagnostic protocol that distinguishes timestamp-grounded reasoning from correlational shortcuts, a distinction that accuracy-based benchmarks cannot make. Controlled interventions on 310 questions from two tasks show that high accuracy can persist when timestamps are replaced by relative offsets or removed, while breaking event-series alignment induces systematic failures. When context is pre-aligned, models barely need timestamps. When order is missing, they use dates to recall world knowledge. Without dates, they rely on correlational shortcuts and rarely notice incorrect timestamps. These findings show that high accuracy on pre-aligned, ordered inputs does not establish that a model uses timestamps to synchronize observations with the world. We release our code, model outputs, and trajectory labels at this https URL.

---


### 239. [BOP-Refer: Benchmark for Monocular 3D and 2D Object Grounding](https://arxiv.org/abs/2611.34862)

**<font color=#1a73e8>作者：</font>** Tomas Hodan, Vineet Bhat, Martin Sundermeyer 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce BOP-Refer, the first benchmark for monocular 3D and 2D grounding of everyday and industrial objects sourced from 9 diverse BOP datasets. We pair images from these datasets with VLM-generated and human-verified referring expressions, and derive accurate ground-truth 3D and 2D bounding boxes of the referred objects from their 3D models and 6DoF pose annotations. Our systematic evaluation of 17 frontier VLMs across the major proprietary and open-weight families (Gemini, GPT, Claude, Qwen, Gemma) shows that the best model, Gemini 4 Carbon, reaches 72.6% AP_IoU2D in 2D but only 12.4% AP_IoU3D in 3D, despite the more lenient IoU thresholds in 3D. The predicted 3D boxes are usually centered on the target objects in the image but often off in depth by more than the object's size, suggesting that metric scale estimation, which needs reliable object size priors, is currently by far the main source of error.

---


### 240. [A Survey of Security, Privacy, and Ethics of Large Language Models in Telecom](https://arxiv.org/abs/2611.34868)

**<font color=#1a73e8>作者：</font>** Joy Bose, Srinivas Adyapak  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly integrated into telecommunications for customer service, network analytics, and operational support. While offering efficiency and innovation, their deployment raises critical privacy, security, and ethical challenges due to the uniquely sensitive and longitudinal nature of telecom data. This paper presents a survey of LLM risks and safeguards in telecom context. Our survey introduces a telecom-specific taxonomy linking privacy, security, and ethics with use cases and outlines open research challenges such as longitudinal data privacy, cross-border compliance, and scalable guardrails.

---


### 241. [Towards Closing the Performance Gap in Cross-Modal Place Recognition](https://arxiv.org/abs/2611.34877)

**<font color=#1a73e8>作者：</font>** Ofer Idan, Dan Badur, Yoli Shavit  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modal place recognition (CMPR) matches natural language descriptions against databases of geo-tagged reference images, enabling localization without visual queries. Despite its potential for language-guided navigation, existing vision-language models lag far behind visual place recognition (VPR) baselines, even after task adaptation. Unlike general-purpose text-to-image retrieval, place recognition relies on subtle local cues to distinguish visually similar locations. We therefore hypothesize that a primary bottleneck in CMPR is capturing fine-grained correspondences between image regions and text details, which requires higher visual token granularity, strong text representation capacity, and local cross-modal matching. To address this challenge, we propose CrossPlace, a two-stage CMPR framework. Stage 1 performs global retrieval by pairing a jointly aligned DINOv2-B/14 visual backbone with a progressively fine-tuned BGE-Large text encoder, while Stage 2 refines top candidates using a lightweight token-level cross-attention reranker. Through systematic analysis, we isolate the drivers of retrieval accuracy and show that visual token density provides the largest performance improvement, while text encoder capacity and task fine-tuning offer complementary gains. To evaluate robustness under realistic conditions, we also extend CMPR evaluation to city-scale and severe weather and illumination settings. Across all existing and new benchmarks, CrossPlace achieves double-digit Recall@1 improvements over prior cross-modal methods, closes the gap to unimodal text retrieval, and narrows it to unimodal VPR. Code and benchmarks are available at this https URL

---


### 242. [Stranger Things: When Objects Appear Without Their Typical Neighbors](https://arxiv.org/abs/2611.34881)

**<font color=#1a73e8>作者：</font>** Siddhartha Gairola, Jiahao Xie, Anna Kukleva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual context is a powerful cue for object recognition: scenes inform what, where, and at what scale objects are likely to appear. Yet over-reliance on context becomes a failure mode when models predict objects based on their typical neighbors rather than the objects' own visual features, which we call typicality bias. While extensively studied in the pre-Transformer era, it has often been assumed that architectural and scale improvements would naturally solve it, and a systematic diagnostic across the modern vision stack remains absent. We provide such a diagnostic framework. We measure typicality bias via normalized pointwise mutual information (NPMI) over object pairs, and introduce STRANGE-Bench (Synthetic Typicality-RANked Grounded Evaluation Benchmark): a photorealistic, layout-controlled benchmark spanning 17 sub-tiers from typical to never-co-occurring object pairs. Across five model families (specialist detectors, open-vocabulary detectors, self-supervised, vision-language, and multimodal large language models) and three recognition tasks (supervised detection, open-vocabulary detection, and classification), the bias is prevalent: gaps of 5-11 p.p. persist when objects appear outside their typical company, and do not consistently shrink with scale. To mitigate it, we turn to data augmentation: existing augmentations are designed for visual diversity, not for breaking co-occurrence shortcuts, and sample from the very distribution that produces typicality bias. We propose Anchor-Atypicality Sampling (AAS), a simple sampling rule for paste-based augmentations that uses the NPMI signal to tilt the training-time co-occurrence distribution toward atypical partners. AAS reduces the typicality gap by up to 1.6 p.p. on natural-image COCO splits and 23.0 p.p. on synthetic STRANGE-Bench across three model families, without sacrificing overall performance.

---


### 243. [ProbFaS: Probabilistic Video Frame Selection for MLLMs via Multi-Fidelity Calibration](https://arxiv.org/abs/2611.34903)

**<font color=#1a73e8>作者：</font>** Tianru Zhang, Mayank Nautiyal, Hugo Eidmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Processing long videos with multimodal large language models (MLLMs) is prohibitively expensive, making informative frame selection essential for accurate video understanding. The default uniform sampling often misses task-relevant keyframes, while recent training-free selectors instead pick frames by how well each one matches the question under an image-text alignment (ITA) score. However, we show that ITA signals correspond poorly with the MLLM's true needs: their rankings correlate weakly with downstream accuracy and are even negatively correlated on over 40% of questions, whereas the MLLM's internal yes/no judgment yields a much stronger signal. We present ProbFaS, a training- and label-free probabilistic pipeline that fuses both signals for key frame selection. ProbFaS treats dense ITA scores as cheap, biased measurements and sparse MLLM judgments as accurate, costly ones, unifying them via co-kriging, a multi-fidelity Gaussian process, to calibrate relevance across all frames. A temporal determinantal point process then selects frames capturing relevance peaks while preserving temporal coverage. Across Video-MME, MLVU and LongVideoBench, ProbFaS is the most accurate among fourteen state-of-the-art training-free selectors and uniform sampling in 13 of 15 settings (8-128 frames), outperforming the strongest baseline by up to 3.1 percentage points. On MLVU and LongVideoBench, 32 ProbFaS frames match or surpass the top baseline at 128 frames and uniform sampling with up to 768 frames.

---


### 244. [Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation](https://arxiv.org/abs/2611.34907)

**<font color=#1a73e8>作者：</font>** Shaoteng Liu, Shuai Yang, Wei Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time autoregressive video generators stream minutes of video and accept new prompts on the fly, but struggle to keep people, objects, and places consistent over a long interactive story. Agent systems provide such memory for offline multi-shot generation, yet they read the whole script in advance, plan each shot before generating it, and regenerate failed shots, which a live stream does not allow. We present Agentic LongLive, an asynchronous agentic memory for long video generation. A memory agent on separate GPUs reads only the prompts revealed so far, never the generated video, and keeps a text state and evolving images for every person, object, and scene. From this entity memory it composes a global image and a per-shot memory image, which an auxiliary GPU prefills into the generator's attention sink before the next shot starts, and writes entity cards for the prompts that name them, so the video never waits for memory and video errors are not written back. A small language model, trained with reinforcement learning and an image reward calibrated using downstream video outcomes, decides what to remember before the next prompt is known. On LongStory-Online, a new benchmark of 25 stories (857 shots) revealed one shot at a time, Agentic LongLive improves persistent-state accuracy of LongLive-2.0, its base generator, by 26.3 points, protagonist identity by 44.9, and revisited-place consistency by 40.4, at about 1% extra generation time on H100. The full system streams faster than real time on one 8xB200 node with the generator in BF16 (34.3 FPS), keeps image quality stable over 14-minute stories, and improves identity on two MiniMax-H3 generators, one of which, LongLive-H3, also runs in real time with it. To our knowledge, it is the first real-time video generator with text and image memory kept by an LLM agent.

---


### 245. [Mixture-of-Loops Transformer](https://arxiv.org/abs/2611.34923)

**<font color=#1a73e8>作者：</font>** Lianghui Zhu, Shijie Wang, Xinggang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers boost expressivity by reusing shared layers across loops, yet at the cost of efficiency. Pushing their expressivity-efficiency frontier requires rethinking the core mechanism connecting adjacent loops: What should be passed as a Transformer loops? We introduce Mixture-of-Loops Transformer (MoLT), whose Mixture-of-Loops Attention (MoLA) uses keys and values (KV) as memory for selective reuse across depths and loops. Under loop residual, MoLT-R retains the residual stream and reads local KV across loops for expressivity. Under loop KV, MoLT-KV instead restarts from embeddings and reads current-loop local KV with preceding-loop memory KV at earlier positions for efficiency. MoLT-KV eliminates same-position cross-loop dependence and, paired with loop forcing for parallel training, unlocks single-traversal Mixture-of-Loops (MoL) decoding beyond the training loop horizon. To balance efficiency and quality, we introduce U-shaped MoLT (U-MoLT), which separates memory construction from prediction readout and skips unused decoder traversals without changing predictions. In 400B-token pretraining, U-MoLT outperforms OLMo3 across 700M/1.5B dense and 3B MoE models, achieving 1.7x validation cross-entropy (CE) token efficiency at 700M while improving 3B MoE 10-domain perplexity by 0.75 and 10-task accuracy by 2.1 percentage points. In 100B-token continued pretraining of Qwen3.5-0.8B-Base, our U-MoLT adaptation lowers CE on all 11 domains over the matched baseline with 1.4x mean token efficiency. At inference, U-MoLT with MoL-Hybrid-2 matches non-looped OLMo3 latency at 996.6 vs. 1,000.6 ms on S-size (~113M) models. Code is available at this https URL

---


### 246. [Diverse Alternative Reasoning Traces for Hard Math Problems](https://arxiv.org/abs/2611.34928)

**<font color=#1a73e8>作者：</font>** Lukas Aichberger, Adam Golinski, Arno Blaas 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training large language models (LLMs) for mathematical reasoning often relies on accepted traces whose final answers pass a verifier. For hard math problems, however, such traces can be rare under independent Monte Carlo (MC) sampling. To address this, we propose Diverse Alternative Reasoning Traces (DART), a trace-mining method that starts from a rejected trace, decomposes it into reasoning steps, and ranks them by position-weighted uncertainty. It then generates deliberately distinct alternative candidates for highly ranked steps using reference-answer guidance and a meta-thought before completing the resulting traces. On greedy-unsolved DeepMath-103K problems, DART recovers 37% more problems than MC sampling at a matched number of generated traces. Its estimated generation cost per recovered problem is nearly identical, while its cost per accepted trace is 30% lower. Post-training Llama-3.1-8B-Instruct on traces mined by DART achieves the highest point estimate in five of six evaluations across MATH-500 and AIME benchmarks. These results demonstrate that revisiting rejected traces with DART can expand problem coverage and provide effective post-training data.

---


### 247. [Attack Policy Selection can Mislead Monitor Evaluators](https://arxiv.org/abs/2611.34934)

**<font color=#1a73e8>作者：</font>** Charlie Griffin, Oliver Makins, Asa Cooper Stickland 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI monitors, classifiers that flag dangerous behaviour by AI agents, are often evaluated against transcripts generated by attack policies acting as proxies for dangerous behaviour in deployment. We evaluate an ex-production OpenAI monitor as a case study and find that measured false negative rate is highly sensitive to both the method used to generate attack policies and the level of optimisation applied within that method. This rate ranged from 0.5\% to 20.8\% across optimisation levels of a single method (reinforcement learning), and from 6.4\% to 23.0\% across methods at their best observed optimisation level (optimised prompting vs.\ transcript editing). Every attack policy was developed against proxy monitors only: all reported results show attacks transferring to the held-out GPT-5.4 target monitor. Our results suggest that monitor evasion evaluations can easily mislead: an evaluation using only basic attack methods may give false confidence that a monitor is strong.
The sensitivity to attack-policy choice raises a problem: interpreting any particular result as evidence about deployment performance requires justification. The transcripts produced by attack policies are proxies for the dangerous behaviour a monitor must flag in deployment. These proxies can introduce visible artefacts, such as reasoning about a ``side task'' absent from the instructions shown to the monitor, that affect monitor judgements. Given the sensitivity above, the choice of proxy can change an evaluation's conclusion. Reading these results as evidence about deployment therefore requires a separate legitimacy argument for why the proxies are informative, including any justification of conservativeness. Making convincing arguments remains an open problem.

---


### 248. [Can image generation help visual reasoning? An empirical study](https://arxiv.org/abs/2611.34935)

**<font color=#1a73e8>作者：</font>** Xueyang Yu, Yifan Jing, Taiming Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models think in words; then multimodal models might think in images. We test whether a generated helper improves the answer to a visual question. A model describes the helper it needs and then answers using the original and generated images together. Across 13 vision-language model and generator pairs, generation lowers mean accuracy by 3.7 percentage points, with declines on nine of ten tasks. Two unified models, BAGEL and Janus-Pro-7B, each lose accuracy on eight tasks. On VSTAR, adding a generated image to the same planning hint lowers accuracy by 10.47 points. Repeated image edits yield different outcomes across tasks. ChartQAPro and MathVista stay below their no-generation baselines, while ERQA gains three points after ten edits.

---


### 249. [Tracking Any Point with Agentic Visual Reasoning](https://arxiv.org/abs/2611.34943)

**<font color=#1a73e8>作者：</font>** Xuweiyi Chen, Jin Yao, Linzhan Mou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A general-purpose Vision-Language Model (VLM) has surpassed expert vision models in many domains such as object detection and video recognition. However, point correspondence is known to be challenging for VLMs since it goes beyond object-level recognition: it requires pixel-level localization of the same physical surface point across observations, even when appearance changes or the point disappears and later reappears. In this paper, we introduce AgenTAP, a VLM-based agent that directly predicts point coordinates and visibility and actively reasons over videos. Starting from its own estimate, the agent autonomously chooses what to inspect and uses the resulting evidence to verify point identity and refine its predictions. With GPT-6 Astra, it surpasses expert vision models in both point localization and visibility prediction, without correspondence-specific fine-tuning. We further use AgenTAP to re-identify physical points after disappearance and reconnect fragmented tracks, constructing EgoTAP-4D, a dataset of 3D point trajectories in long real-world egocentric videos. On sampled reappearing points, its predictions approach human agreement, and adding EgoTAP-4D to D4RT training improves average 3D tracking performance.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 250. [ViCARD: Visual Credit Assignment with Reward-Gated Distillation for Multimodal Reasoning](https://arxiv.org/abs/2611.33437)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zijian Huang, Jiasi Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual reasoning requires models to identify relevant visual evidence and use it to derive correct answers. Outcomebased reinforcement learning (RL) faces two key challenges in this regime: it yields no learning signal when perceptual errors cause all sampled responses to fail, and it broadcasts a uniform advantage across every token within a response. Conversely, while visual self-distillation offers dense guidance from evidence-centered image crops, student learning from token distributions alone often fails to elicit correct final answers. Motivated by an audit of training rollouts that exposes these complementary failure modes, we introduce ViCARD (Visual Credit Assignment with RewardGated Distillation), which integrates per-token visual supervision with verified correctness rewards. For each rollout group, we leverage a teacher with its input image cropped to the relevant visual area, and use this to provide per-token supervision to the student while also valuing correctness. If all sampled rollouts fail, ViCARD samples an additional crop-teacher answer and activates on-policy distillation only if that answer is correct. Together, these mechanisms provide fine-grained visual credit within informative reward groups and a learning signal for otherwise uninformative all-fail groups. Extensive comparisons across model scales demonstrate that ViCARD improves fine-grained visual reasoning performance over RL and distillation baselines, while retaining broad visual reasoning capabilities.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-267](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
