# 🧠 大模型相关研究 | 2026年11月25日

> 本类共 **486** 篇论文：已确认 **458** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

---

### 101. [Interpreting Diffusion Model Activations in Natural Language](https://arxiv.org/abs/2611.28621)

**<font color=#1a73e8>作者：</font>** Yukinori Yamamoto, Kotaro Yoshida, Ryotaro Shimizu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpreting the intermediate activations of diffusion models (DMs) is key to understanding how they generate images. Existing interpretability methods for DMs provide limited support for open-ended interrogation, making it difficult to extract human-interpretable insights. We extend LatentQA, the task of answering natural-language questions about Large Language Model activations, to DM activations. We introduce the Diffusion-specific Activation Oracle (DAO), which translates DM activations into natural-language answers to open-ended questions about the ongoing generation. Our experiments show that DAO can effectively describe the content of the final image from activations at early denoising steps. Additionally, we demonstrate that DAO captures the structure of the DM's activation space well enough to steer image generation toward target attributes. Furthermore, we show that attribution patching through DAO identifies DM components that contribute to visual attributes specified in natural language. Our code is available \href{this https URL}{here}.

---


### 102. [Self-prediction residuals improve single-pass detection of wrong-object boxes in grounded vision-language models](https://arxiv.org/abs/2611.28632)

**<font color=#1a73e8>作者：</font>** Enhao Cui, Junzhi Yang, Yaoshun Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounded vision-language models write boxes as text, and the mean probability of their coordinate tokens says little about whether a box is right. We study a single-pass signal for boxes on another object, which matter when only the object counts. A linear map, fitted per model to its own answers without labels, reads a box from the hidden state before writing. Its disagreement with the written box, the self-prediction residual, flags boxes on another object although the read-out is far less accurate; the residual's weight was fixed with labels on two models. On a replication list of 1,200 RefCOCOg test items, the residual, averaged over six models, raises the detection of these errors for each of fifteen single-pass scores, by 0.026 to 0.049 in area under the receiver operating characteristic curve (AUROC) on a label-free probe and probes trained on 2,000 labelled items. Over all errors, adding it to the label-free probe moves AUROC, averaged over the models, by less than 0.02 (95% interval). With a fifth of answers reviewed, the share of all errors caught moves from 0.518 to 0.524, that of boxes on another object from 0.505 to 0.607 (post hoc): the residual changes which errors are found, not how many, and in cost-weighted recall it breaks even when such a box costs about 0.86 times another error, and its gain is positive in point estimate at equal costs. These gains come from RefCOCOg lists of MS-COCO images.

---


### 103. [LoopSeek: Decoupling System One Search from System Two Answering for Long Video Understanding](https://arxiv.org/abs/2611.28635)

**<font color=#1a73e8>作者：</font>** Chengzhong Wang, Lang Lin, Xinyang Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video question answering requires finding relevant evidence before reasoning over it. With a limited frame budget, single-pass frame selection can miss critical evidence, while adaptive search often relies on repeated text generation to decide where to look. We introduce LoopSeek, a framework that decouples evidence search from answer generation through a division of labor between a non-thinking System I and a generative System II. Our key insight is that search can be expressed as a sequence of small, typed decisions, allowing System I to find the evidence that System II needs. Four System I role agents navigate a tree of video windows and coordinate through probability outputs to select frames, assess evidence, and revise the search without generating text. To align search with System II, System I learns from annotated evidence on questions that System II answers correctly only from that evidence, and the verifier's evidence estimates steer the search without calling System II, which stays frozen and answers once from the selected frames. On five long-video benchmarks, with a frozen Qwen3-VL-8B reading 32 frames, LoopSeek improves average accuracy from 53.5 to 63.9 over the uniform baseline and takes 32--80\% less GPU time per question than agentic methods.

---


### 104. [Make Position Uninformative: Exchangeable Self-Distillation Flattens the Lost-in-the-Middle Curve](https://arxiv.org/abs/2611.28638)

**<font color=#1a73e8>作者：</font>** Qingsen Ma, Dianyun Wang, Jiahong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented language models answer well when the relevant document comes first or last and poorly when it sits in the middle. Some fine-tuning recipes lift the middle by lowering the start. We show how training contexts teach positional bias. With a uniform answer slot and shuffled distractors, the optimal reader ignores position. Building on this result, Exchangeable Self-Distillation (ExSD) trains a small adapter on shuffled contexts to reproduce the model's answer when it reads the answer document alone. It needs no gold answers and only a few thousand examples. On six models from 1.5B to 32B parameters, ExSD raises both average and worst-position accuracy against the frozen model, including on a held-out test split. In controlled LoRA comparisons, it significantly improves both criteria over Pos2Distill. Against CORD, mean differences are not significant, while worst-position accuracy improves significantly in the 20- and 30-document settings. ExSD also matches or beats gold-answer fine-tuning, changes behavior on other tasks far less, and transfers to unseen tasks. Head probes show greater reliance on content over position.

---


### 105. [CrossPanel: Exposing the Answer-Evidence Gap in Scientific Figure Understanding](https://arxiv.org/abs/2611.28641)

**<font color=#1a73e8>作者：</font>** Zhengyang Lu, QianhongWen, Chenpeng Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A correct answer to a scientific-figure question can conceal an incorrect account of the experiment. Reading evidence across panels requires keeping each observation attached to the object and conditions that give it meaning. We introduce CrossPanel, a benchmark of 2,650 human-reviewed questions that exposes this answer-evidence gap. Its tasks combine parallel observations or follow dependent queries, while a response audit separates object selection, experimental conditions, cross-panel binding, and local readout. Across 15 vision-language models on 251 diagnostic questions, 8.42%-56.64% of correct answers contain explicit factual errors. The audit distinguishes coherent readings of the wrong target from incorrect readings of the right one. Controlled interventions then test how these failures can be repaired: verified object-condition hints, which withhold the requested measurement, raise Qwen3.5-35B-A3B's target-query success by 22.81 percentage points on 57 questions, while additional image tiles alone yield little improvement. Other models benefit most from combining both forms of assistance. These findings identify experimental attribution as a distinct requirement alongside local perception, and make both measurable beyond final-answer accuracy.

---


### 106. [Aegis: A Conversational Prototype for Lung Cancer Risk Information and Follow-up](https://arxiv.org/abs/2611.28642)

**<font color=#1a73e8>作者：</font>** Bowen Han, Chengwei Cao, Runxin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Collecting self-reported risk information and maintaining continuity between assessment, explanation, and follow-up are practical components of a lung cancer screening workflow. We present Aegis, a browser-based research prototype that combines a conversational questionnaire, rule-based risk categorization, downloadable reports, retrieval-augmented health information, and doctor-user communication. A session-oriented controller manages question progression and clarification, while a language model assists with answer validation. Structured responses are passed to a separate risk-analysis module, and reports are linked to user and session records through Firebase services. The project adopts a multi-agent design that separates information collection, validation, assessment, and report generation. Its documented verification scope comprises 45 functional test specifications covering account management, questionnaire interaction, reporting, doctor-side review, and consultation. The available evaluation describes workflow behavior qualitatively; it provides no per-case execution results, clinical cohort, predictive-performance measurements, or comparative experiments. We therefore present Aegis as an engineering prototype for organizing risk information and follow-up, with clinical validity and the benefits of its agent-based design remaining unestablished. The paper describes the implementation, distinguishes implemented workflows from incomplete extensions, and identifies the evidence required for reproducible and clinically meaningful evaluation.

---


### 107. [S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence](https://arxiv.org/abs/2611.28649)

**<font color=#1a73e8>作者：</font>** Muxin Fu, Peike Yu, Guibin Zhang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence, the ability to reason about 3D space from visual observations, becomes essential as multimodal large language models (MLLMs) move into the physical world. Beyond perceiving each view, it rests on two cornerstones of human cognition: fusing multiple views into one coherent 3D scene and mentally transforming that scene to new viewpoints as reasoning unfolds. Yet our spatial probes reveal that MLLMs largely lack both capabilities, even after spatial fine-tuning. We therefore present S-Mind, which internalizes multi-view geometry within the MLLM through a compact set of spatial tokens. It supervises these tokens to hold the fused 3D scene and re-emits them to re-express this scene from every viewpoint the reasoning adopts. Across four spatial benchmarks, S-Mind improves its Qwen3.5 backbones by up to 22.26 points and surpasses frontier general models such as GPT-6-Astra (+0.45), Kimi-K3.1-Pro (+1.97), and GLM-5.3-Flash (+7.80) in average accuracy. Moreover, the same probes confirm that it acquires both capabilities, reaching fusion and transformation accuracies of 65.11% and 82.17%, against at most 16.02% and 37.28% for the baselines. At inference, S-Mind also runs about 100x faster than a tool-based agent on the same backbone. Instilled through these spatial tokens during training, spatial capability becomes intrinsic to the backbone and persists even when the tokens are withheld, offering a promising path toward spatial intelligence in MLLMs.

---


### 108. [Unlearning Model Identity: Ablating LoRA Weights from Question-Based Identity Tuning](https://arxiv.org/abs/2611.28650)

**<font color=#1a73e8>作者：</font>** Ming Cheung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models are trained on diverse corpora containing outputs from proprietary teacher models and provider-curated sources. Models subsequently inherit embedded self-identity traits, persistently asserting specific proprietary names. Service providers of open-weight models frequently require the removal of model identity for downstream applications, such as custom interfaces, without exposing provider affiliations to end-users. Effective identity modification is therefore critical for customized model alignment and deployment. This study proposes a method to localize parameter-level representations of self-identity within low-rank adaptation modules to perform targeted weight ablation. By generating probing questions designed to elicit self-naming outputs and fine-tuning the base model on these responses, the approach identifies and ablates high-magnitude weights within the parameter set. Experimental results demonstrate that distilled identity traits reside within a localized subset of low-rank weights, achieving a complete removal rate in Qwen3.5-2B and a 10% rate in Gemma4-E2B while preserving general task capabilities. These findings confirm that ablating top-tier adaptation weights suppresses distilled self-identification without compromising broader model performance.

---


### 109. [Persuasion from Within: Model-Based Insider Attacks in Multi-Agent LLM Debate and Consensus](https://arxiv.org/abs/2611.28660)

**<font color=#1a73e8>作者：</font>** Bangyan Ju, Xiaolin Sun, Yibin Hu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in multi-agent systems for collective decision-making, such as multi-agent debate and consensus games, in which agents exchange messages and update their answers over multiple rounds and a resolution mechanism aggregates them into a final outcome. Most multi-agent LLM frameworks assume that every participant shares the system objective. In practice, however, a malicious agent can join as a legitimate member of the group and persuade the other agents toward a hidden adversarial goal. We formalize such attacks as a sequential decision-making problem in which the insider seeks to degrade the utility of the collective outcome. We propose a model-based insider attack that learns to persuade a group of agents: the insider first learns a world model of the benign agents from offline trajectories and then uses it both to train a persuasion policy and to plan its messages. In two case studies involving a numerical consensus game and a multi-agent debate, the learned insider is the most effective and the stealthiest attack we evaluate, outperforming both prompt-based and trained LLM persuaders from prior work. The attack also transfers to other target models, larger groups, and unseen datasets, and remains effective under existing Byzantine-resilience defenses. The learned insider also enables a new defense: adversarially training benign agents on the attack data largely removes both our attack and the strongest prior persuasion attack. These results show that combining world models with reinforcement learning and planning is an effective route to both attacking and hardening language-based multi-agent systems.

---


### 110. [Seeing Right, Writing Wrong: Where Short Chain-of-Thought Breaks Spatial VQA](https://arxiv.org/abs/2611.28665)

**<font color=#1a73e8>作者：</font>** Chenhao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Asking a vision-language model (VLM) to think step by step often makes it worse at spatial questions, even though the image stays in context. We show that short chain-of-thought (CoT) turns a perception problem into a transcription problem. Once a VLM writes a spatial relation, its answer follows that sentence instead of the image, so whether CoT helps or hurts depends largely on whether the written relation is more accurate than answering directly. Studying 15 open VLMs (2B-38B) and six frontier closed models, we rule out token count, turn format, and visual forgetting in open models and trace the failure through three stages. First, writing re-weights visual cues, weakening a "lower is closer" shortcut in all 13 open models tested but also discarding valid cues, which produces false relations. Second, the written text takes over. With the model's own conclusion-removed rationale held fixed, swapping in an opposite-depth image moves the answer by 2-9 points on rendered twins (vs. up to 77 for direct answers) and by 3.0-3.4 points on average on natural photographs (vs. 20.5-69.6). Third, the concluding sentence can invert even a true relation, mainly on converse questions. Together, false relations and conclusion mis-mapping account for four in five CoT losses. Scale does not remove this bottleneck: Qwen3-VL-32B shows the same pattern. Frontier closed models are not hurt: they write relations as accurately as they answer, and three of six re-check the image after writing. The three queried with reasoning off lock in like open models, so re-grounding co-occurs with answer-turn reasoning; we identify answer-step re-grounding as the step open VLMs lack. In a single-model pilot, fine-tuning on fixed rationales with image-determined labels restores it on natural photographs. We open-sourced all our datasets and code at this https URL.

---


### 111. [Physical regime changes expose formula misuse in large language models](https://arxiv.org/abs/2611.28669)

**<font color=#1a73e8>作者：</font>** Maohao Ran, Yanting Zhang, Chendong Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly employed for scientific computing across the Earth and environmental sciences, but problems in these fields often involve distinct physical regimes. LLMs may fail to recognize these regime-dependent constraints, applying formulas outside their domains of validity and producing plausible but physically incorrect results. We systematically investigate these failures through controlled experiments and assess whether post-training can improve regime-aware reasoning. Across 72 physical mechanisms, we find frontier LLMs frequently misapply formulas outside their regimes of validity, reducing accuracy by 13-57 percentage points. Reinforcement learning with verifiable rewards enables Qwen3.5-9B to match DeepSeek V4 Flash (284B) on regime-dependent tasks, but its effectiveness is limited by the formulas available in the base model. Combining supervised fine-tuning on a few worked examples with reinforcement learning improves accuracy by 61 percentage points, while distillation from a teacher supplied with the correct formula raises accuracy from 0% to 71%.

---


### 112. [The Evaluation Substrate Matters: Benchmarking Multi-Agent Serving Substrates](https://arxiv.org/abs/2611.28671)

**<font color=#1a73e8>作者：</font>** Haoyuan Zheng, Dongting Li, Hancheng Ye 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) usually coordinate heterogeneous models and tools to solve complex tasks, creating a growing need for reliable evaluation. However, a multi-agent workflow that is fastest in one serving environment can lose its advantage in another, even when its models, prompts, and task remain fixed. This makes a benchmark result conditional on how the workflow is executed. We introduce MASSys, a benchmark for measuring this dependence in multi-agent large language model (LLM) systems. MASSys executes the same candidate-task pairs across serving substrates and load regimes, using five workload families spanning software repair, research synthesis, financial analysis, interactive control, and diagram generation. It records task quality alongside delivery, latency, cost, resource pressure, and failure evidence. In a controlled motivation diagnostic, the Star workflow falls from first to fourth in mean-latency rank under KV-cache pressure, while Chain rises from fourth to first. The substrate sweeps further show that increasing load creates long runtime tails and timeout pressure. In several task families, quality among evaluated outputs changes less than effective quality over submitted jobs: the system delivers fewer usable results even when the surviving outputs remain competitive. Tool and runtime traces reveal that these outcomes involve both model serving and non-model execution. Together, the results motivate evaluating MAS designs over explicit operating conditions and reporting which tasks are delivered, how well they are solved, and where execution breaks down.

---


### 113. [Improving the Improver: Semantic PID Control for Medical Agent Self-Improvement](https://arxiv.org/abs/2611.28680)

**<font color=#1a73e8>作者：</font>** Dexia Chen, YiLong Hu, Wenqi Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-stakes vertical medical tasks, such as postoperative pathological staging and long-term survival prediction, demand multi-step clinical reasoning over heterogeneous evidence under weak supervision and high outcome uncertainty. While we first orchestrate CliAgent, a domain-tailored clinical agent workflow that systematically grounds predictions in multi-modal patient evidence, manually designed medical agents remain constrained by static, brittle rules. Moreover, existing recursive self-improvement (RSI) methods suffer from feedback ambiguity and severe development-set overfitting when evolving agents in high-noise medical domains. Focusing on improving the improver, we propose Semantic PID-RSI, an evidence-guided control-theoretic framework for medical agent self-improvement. Inspired by PID control, our improver evaluates candidate modification batches via three diagnostic roles: P isolates current clinical failure modes, I synthesizes longitudinal evidence from past trials, and D estimates response dynamics and regression risks (D-pre/D-post). Selected plans are compiled into behavior contracts for staged probing and independent adoption judging. Instantiated and validated on challenging oncology tasks (pT/pN staging and survival prognosis), evolving CliAgent with Semantic PID-RSI on a 3B-activated open-weight model achieves substantial gains (up to +6.27 C-index points), outperforming overfitting-prone RSI baselines and approaching the performance of frontier proprietary models (e.g., GPT-6 series) equipped with CliAgent.

---


### 114. [Rethinking Visual Token Retention in Multimodal Reasoning](https://arxiv.org/abs/2611.28684)

**<font color=#1a73e8>作者：</font>** Fawaz Sammani, Nikos Deligiannis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive Large Vision-Language Models solve multimodal reasoning tasks by retaining hundreds or thousands of visual tokens, allowing every generated token to attend to the visual tokens at any time during the generation process. However, whether continuous access to these visual tokens is necessary remains poorly understood. In this work, we investigate how visual token influence evolves along two dimensions: generation time and transformer depth. Using long-form visual reasoning benchmarks and multiple model scales, we first analyze the attention dynamics across generation time and transformer depth. We identify a temporal and depth-wise structure in the use of visual information. Visual attention peaks during the initial generation steps and then rapidly declines as attention shifts toward previously generated reasoning tokens. Across depth, visual influence is concentrated in intermediate layers and becomes very weak in the final layers. We further verify these observations with causal intervention that removes all visual tokens across generation time and model depth. These interventions confirm that visual-token dependence in multimodal reasoning is neither temporally persistent nor uniformly distributed across transformer depth. Thus, retaining the complete visual context at every layer and decoding step may be unnecessary. Our experiments demonstrate that we can remove up to 59\% of tokens from the full input prompt across generation time and 11\% across all transformer layers, while incurring only a very small performance drop. On video benchmarks, up to 65\% of the input prompt tokens can be removed during generation without affecting performance.

---


### 115. [Can Your AI Twin Meet People for You? It Can Hold a Conversation. But What Does It Need to Judge Like You?](https://arxiv.org/abs/2611.28692)

**<font color=#1a73e8>作者：</font>** Wanghao Ye, Sihan Chen, Bowei Tian 等 32 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Should your AI twin go meet people on your behalf? We built LLM twins of 710 real people from their other conversations in the CANDOR corpus, sent them to meet each other in 5,680 simulated first conversations, and checked every rehearsal against what the real people said after meeting for real (355 held-out, participant-disjoint pairs, against baselines that include each person's rating history). The rehearsals work: a twin's conversation predicts real liking ($\rho$=0.277), carries information that questionnaires and rating history do not have (partial $\rho$=0.16 [0.05, 0.26]), and recovers most of what the same reader gets from the real conversation (0.321). Swap controls show that this signal travels through the conversation, not through the persona card. What, then, does a twin need to judge like you? Not your voice: making twins talk more like their owners, with person-specific activation steering and a LoRA trained on their own speech, did not help in a pre-specified test and lowered accuracy in an exploratory second round (-0.183 [-0.294, -0.066]). Nor simply your stated ratings: a persona-prompted twin that holds the conversation does not yet carry its owner's judgment, and when told its owner's past ratings it anchors on them instead of weighing them. Learning helps: a small appraisal head trained on other real conversations, which combines the twin's post-call answers with its owner's rating history, lifts rehearsal-based prediction above the history baseline out of fold (+0.059 [0.001, 0.115], against +0.022 without the twin's answers; pre-specified primary contrast +0.056 [-0.001, 0.111]). We propose an attribution protocol for twin-based social simulation and identify learned appraisal as the component twins need next.

---


### 116. [SkillLens: An Interactive Human-LLM System for Diagnosing and Refining Agent Skills](https://arxiv.org/abs/2611.28706)

**<font color=#1a73e8>作者：</font>** Shuo Yan, Rui Sheng, Xiaoyan Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly rely on reusable skills, yet maintaining them requires developers to connect revisions with changes in behavior and task outcomes. Existing workflows fragment evidence across versions, evaluation cases, and execution traces. We present SkillLens, an interactive human-LLM system for diagnosing and refining agent skills. A formative study with five developers and researchers identified challenges in prioritizing failures, reconstructing case-level evidence, and preserving context across revisions. SkillLens links performance changes, case transitions, skill diffs, invocation sequences, traces, and outputs in a recoverable workflow, while keeping model-generated explanations and refinements under human review. Through a between-subjects user study with 20 participants, we show that SkillLens supports developers in diagnosing and refining agent skills through a more usable and less demanding workflow than the baseline. These findings highlight the value of linking version comparisons, case-level evidence, and human-reviewed refinement across skill iterations.

---


### 117. [Legal Is Not Good: A Pre-Registered Benchmark of Low-Cost Language and Decision Models on a New Strategy Game](https://arxiv.org/abs/2611.28713)

**<font color=#1a73e8>作者：</font>** Federico Lucca  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Measure Before You Train argued that an agent's decisions should be measured against ground truth, under a protocol fixed in advance, before anyone trains or replaces the model behind them. We carry the method to a second, very different domain, a turn-based strategy game, and ask a deliberately modest question: how well do low-cost agents play under a pre-registered protocol? hexfolk is a minimal two-player 4X game written for this purpose, so no model has seen its rules or positions. A deterministic engine, one agent interface, a referee that never corrects an illegal or late move, and per-decision logs make every game replayable; questions and expected answers were committed before the games, on held-out seeds with mirrored seats and 95% Wilson intervals. Two small open language models (8B and 3B) lose every game to a few-line rule player. Answering in free text they are invalid on 98% of their decisions; constrained to legal moves they never play an invalid one, yet they lose to the uniformly random player (the 8B model wins 10.0 [4.3, 21.4]% of games), refuting our expectation that they would beat it; the result survives a control that shuffles the order of the options. Two native decision models never play an invalid move and both beat random; one loses all 50 games to the rule player, the other is not distinguishable from it in 50 games and beats a one-step search. The paid agents make tens to over a hundred model calls per game; against the same opponents a free 60 ms-per-move search, which makes none, outplays every paid model by the full range of the scale. Two 7-8B models served locally behave the same way. No frontier model is included.

---


### 118. [KMed-31B Technical Report](https://arxiv.org/abs/2611.28719)

**<font color=#1a73e8>作者：</font>** KMed Team at NAVER  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present KMed-31B, a medical large language model post-trained from an open-weight model for on-premises deployment with limited hardware. Post-training a model for diverse medical tasks remains difficult, because improving one kind of task can lower performance on another. We attribute this to differences between tasks in expected output and available feedback. Medical question answering and diagnosis prediction have reference answers, whereas clinical inquiry has no single correct response and is judged with rubrics. We therefore divide medical training tasks into four categories by these two properties, train one specialist per category with a reward that its feedback supports, and integrate the specialists into a single student with Multi-teacher On-policy Delta Distillation (MOPD$^2$). For clinical inquiry, we build Synthetic Health Dialogue, a simulated corpus of consultations with lay users and clinicians whose patient cases span common clinical presentations in primary care. Relative to its base model, KMed-31B raises HealthBench Hard from 22.95 to 41.87 and HealthBench Professional from 37.92 to 50.20 in non-thinking mode, and from 23.80 to 51.48 and from 41.97 to 59.18 in thinking mode, while its scores on four multiple-choice medical benchmarks are maintained or slightly improved. KMed-31B has the highest unadjusted HealthBench Hard score among the compared models, including proprietary ones, and scores higher on HealthBench Professional than every open-weight model we compare, including models with more than ten times as many total parameters. Applied to another base model, Qwen3.8-27B, the same training recipe also raises both HealthBench scores. We describe the training recipe, data construction, and settings in detail so that institutions requiring on-premises deployment can develop medical models from open-weight foundations.

---


### 119. [CLAIR: Consistent LLM Adaptation via Index-free Reprogramming](https://arxiv.org/abs/2611.28721)

**<font color=#1a73e8>作者：</font>** Dongkuk Kim, Jungkyu Shin, Yoonhyuk Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series forecasting with pretrained large language models (LLMs) uses contextualized patch representations, raising the question of how to align them. Matching patches at the same temporal position is natural, but self-attention allows each patch state to incorporate information from elsewhere in the input window, suggesting that useful correspondences can extend across positions. This flexibility, however, does not necessarily translate into consistent forecasts: similar patch states may play different roles when used in their original temporal order. To address both issues, we propose CLAIR (Consistent LLM Adaptation via Index-free Reprogramming), a teacher-guided framework that combines patch-level transport alignment (PTA) and forecast-level consistency (FC). A clean-view exponential moving average (EMA) teacher guides a mildly perturbed student, with PTA establishing soft, representation-dependent correspondences and FC encouraging agreement at corresponding future steps. The forecasting head retains the original patch order. We test this combination through controlled comparisons: while PTA and index-wise alignment perform similarly without FC, PTA+FC under EMA supervision reduces horizon-averaged mean squared error (MSE) by 2.1% on ETTh1 and 2.6% on ETTm1 relative to Index+FC. The same preference for PTA+FC emerges in comparisons with alternative matching strategies on Weather and ETTh2. Beyond these controls, CLAIR achieves the lowest horizon-averaged MSE on five of six long-term benchmarks and the lowest aggregate overall weighted average (OWA) on M4 among evaluated methods, with competitive few-shot performance. As the teacher and transport are used only during training, inference requires only the student.

---


### 120. [Seeing Is Not Planning: Spatiotemporal Planning and Plan Repair in Multimodal LLMs](https://arxiv.org/abs/2611.28726)

**<font color=#1a73e8>作者：</font>** Siyuan Li, Ethan Lin, Xiang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Planning in a visual world means reading the layout, foreseeing how the state will change, and following the task rules all at once. When a plan fails, a model should also use what went wrong to fix it. We call these two abilities spatiotemporal planning and plan repair, and test them with Railbound-Bench. A model sees a railway puzzle, adds tracks under a budget, and submits one complete layout; a simulator then moves all cars at once and decides whether the layout works. After a failure, the model sees what happened and may submit a new layout, up to five attempts in total. On the 200-puzzle main set, the best of nine models solves 59.5% within five attempts, the next 39.5%, and the other seven at most 10.0%; a 1,000-puzzle extended set with a wider range of difficulty is far easier, at 90.9% for the best model. Controlled studies on 180 fixed puzzles show that knowing the task is not the same as using it. GPT-6.1 Terra copies 97.2% of boards exactly and, given a correct layout as text, predicts all four requested future states in 91.3% of cases, yet only 22.8% of its first layouts work. Planning fails more often as the cars' routes interact, even among puzzles that a search solver finds equally easy. Visual feedback removes the reported fault in 175 of 417 first revisions, but only 43 of these revisions solve the puzzle, and at an equal budget of 40k tokens it does no better than fresh retries. The code and data are open-sourced on GitHub at this https URL.

---


### 121. [Multimodal LLMs Know the Game but Assume the Real World](https://arxiv.org/abs/2611.28745)

**<font color=#1a73e8>作者：</font>** Jianxin Gao, Bohan Chen, Runze Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models can state the rules of a video game, but do they apply them when they only see the game? We introduce RuleCraft, 1,240 image questions over 155 Minecraft rules with outcomes verified in the game engine, each asked in text, on the image with the game named, and on the bare image. Six widely used models know the rules and recognize the game, yet answer the bare image by real-world physics: naming the game raises their accuracy on rules where the game departs from reality by 8.2-19.8 points on a main set and by 33.8-52.7 on a hard stress-test set. Their errors pick the real-world outcome, the gap is largest where the game leaves a scene unchanged, and reasoning traces state the game's rule, then answer by reality. On the main set, naming the game mostly swaps the real-world default for the game's. The pattern holds with reasoning, recurs in two more games, and persists on questions the models themselves take to be about the game; one neutral sentence asking for the rules of the world shown recovers much of the gap. Evaluations that name the game measure knowledge of its rules, not world selection.

---


### 122. [Who Speaks for the Water? Simulating Discursive Closure and Power Asymmetries in Hydrosocial Governance](https://arxiv.org/abs/2611.28755)

**<font color=#1a73e8>作者：</font>** Mario Lillo-Saavedra, Marcela Salgado-Vargas, Ángel García-Pedrero 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Water governance conflicts stem not only from material scarcity, but from power asymmetries, institutional distrust, and the discursive frameworks through which actors assign meaning to water, infrastructure, and legitimate authority. Conventional simulation tools represent these dynamics via numerical opinion variables, missing the argumentative and narrative dimensions structuring real deliberation in hydrosocial territories. We present the Hydrosocial Agent-Based Model with Large Language Models (HSABM-LLM), a hybrid framework enabling heterogeneous agents to generate, evaluate, and adapt natural language arguments conditioned on institutional roles, interaction histories, and territorial context. Grounded in semi-structured interviews, a water-user survey, and 456 press and official documents from the Longaví River sub-basin (Maule Region, Chile), the model simulates deliberation over a contested large-scale reservoir proposal across four experimental scenarios. Opinion convergence toward unanimous opposition emerged within 7-14 months, operating through discursive closure driven by distributive equity and water security framings rather than argumentative dominance. Governance actors accelerated convergence by activating pre-existing institutional distrust rather than direct persuasion, while peer-based smallholder interactions drove 77-79% of all opinion changes. The formal authority of state institutions proved structurally decoupled from deliberative influence, revealing a legitimacy deficit that formal inclusion alone cannot resolve. These findings suggest participatory governance design must attend to the discursive conditions under which institutional actors enter deliberative spaces, rather than assuming inclusion is inherently consensus-building. HSABM-LLM offers a novel platform for integrating political ecology insights into computational social science.

---


### 123. [Who Is Prompt-Injecting Coding Agents? An Empirical Study of Hidden AI-Directed Text on GitHub](https://arxiv.org/abs/2611.28763)

**<font color=#1a73e8>作者：</font>** Gabi Nakibly, Zvika Babo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents now triage issues, review pull requests and pick up tasks inside GitHub repositories, and to do so they read text that anyone with a GitHub account can write. This makes GitHub a prime surface for indirect prompt injection, in which instructions embedded in untrusted content steer a model that later processes it. Prior work has demonstrated such attacks against agents on GitHub in controlled settings, but how often they occur in practice, who deploys them, and for what purpose remain unknown.
We present the first large-scale empirical study of AI-directed hidden text on GitHub. We analyzed roughly 145 million issues, pull requests, comments and README files, detected text that GitHub does not render to a human reader but that an agent receives in full, and filtered it with a two-stage LLM classification, a template provenance check and an exhaustive manual review. We identify 2,281 validated findings in issues, pull requests and comments (16 per million items), and AI-directed hidden text in the READMEs of 107 repositories.
We find a heterogeneous ecosystem of four uses: attacks on other parties' agents, defensive text that restricts agents, content override that steers what they write, and first-party orchestration, in which projects coordinate their own agents through hidden markers. Attacks are rare (about one in 3.3 million items) but aimed at maintainers' own triage, review and CI agents. Orchestration accounts for two thirds of the findings in issues, pull requests and comments, grew fivefold in four months, and forms a control channel that anyone who can comment can imitate. Replayed offline against five models we tested, the attacks succeed against one small, fast model in 19% of cases, and against none once HTML comments are stripped. We release our detection tool and every finding.

---


### 124. [JevNavAgent: A Single-Forward Visual Navigation Agent with Trajectory-Level RL for Gigapixel Pathology](https://arxiv.org/abs/2611.28766)

**<font color=#1a73e8>作者：</font>** Yonghuang Wu, Zhenyang Liang, Pengfei Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gigapixel whole-slide images (WSIs) exceed single-pass vision-language model (VLM) capacity at cellular resolution, while multiple instance learning relies on query-agnostic offline patching without interactive reasoning. Multi-step VLM navigation agents inspect regions on demand, yet face two bottlenecks: (1) autoregressive action decoding incurs heavy latency, throttling exploration and online multi-trajectory RL; and (2) offline distillation suffers from an existential-versus-universal stopping asymmetry between positive detection and negative exclusion, inducing thumbnail and kinematic shortcuts while leaving policies prone to passing metastases without stopping. Under the Jev (System One) paradigm, a model predicts distributions over predefined decision spaces in one forward pass (0 generated tokens) while deterministic code executes navigation. We build JevNavAgent, a 2B-parameter agent combining factorized stopping, spatial-candidate, and contextual-bilinear answer heads with overview modality dropout. We pair Stage-1 offline counterfactual trajectory alignment (mitigating depth and panning shortcuts) with Stage-2 online trajectory-level GRPO (Traj-GRPO), using decoding-free rollouts to optimize branch-level lesion discovery, in-polygon stopping, and step-wise confidence gain. On Clean Visual WSI-VQA, JevNavAgent achieves 51.57% multi-scale (50.43% terminal-step) overall and 51.39% focal accuracy, outperforming frontier VLM agents and 4B-11B open-source cascades while running nearly 12x faster than frontier APIs (5.63s vs. 66.64-70.04s). On CAMELYON16 Official Test, Traj-GRPO reaches 22.45% localization (converting 11/12, or 91.7%, of visited tumors into grounded stops) with 93.75% specificity and 69.77% slide accuracy, surpassing Stage-1 SFT under matched stopping rules alongside zero-shot budget scaling.

---


### 125. [Where Does a Weight-Editing Agent Help? Blind Diagnosis and Repair of Deployment Faults in Vision Models](https://arxiv.org/abs/2611.28781)

**<font color=#1a73e8>作者：</font>** Zhuangzi Li, Shilv Cai, Jian Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-model agents can read and edit the weights of neural networks without gradients, and this is increasingly presented as a new way of repairing models. We ask what such an agent adds, in a setting with a known answer. A vision model moved into a new system may be broken by a preprocessing, weight-conversion or output-convention fault; an agent restricted to forward passes must decide whether a fault exists, name it, and undo it by editing the weights. Over 183 runs on classification, segmentation and detection, scored against the fault-free model, we find three things. When the kind of fault is known, the agent is not needed: a script written afterwards repairs 30 of 48 faults against the agent's 33. But the agent did not have to be told: on five fault types outside every script it repairs 15 of 15 where that script repairs 4, and it never edits any of 21 fault-free models. And its limits are predictable: it needs a trustworthy per-layer reference for the model's activations and a fault that is an invertible structured transformation; without them, small faults are missed and repairs stay partial. We derive guidance on when to use an agent and when a script.

---


### 126. [3DCodeFactory: Scaling Training Data for 3D Code Agents](https://arxiv.org/abs/2611.28783)

**<font color=#1a73e8>作者：</font>** Zhaoyu Wang, Xueru Wen, XingYu Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As code agents evolve, their scope is expanding from generating simple static 3D meshes to constructing structurally complete, complex, interactive 3D scenes. However, existing datasets mainly rely on converting or captioning pre-existing 3D assets, consisting mostly of single-turn code data for static single objects and struggling to scale task diversity and scene complexity, leaving such training data scarce. We present 3DCodeFactory, an automated framework that directly constructs diverse, complex 3D training data from abundant raw text (e.g., diffusion prompts and product descriptions). The framework first leverages an image generator to synthesize 3D reference images from raw text as visual anchors, guiding the generation of concrete modeling specifications and interactive functional requirements; meanwhile, it jointly constructs visual, specification, and functional rubrics from the reference images and requirements to automatically score and filter multi-turn agent rollouts. Based on this framework, we release 3DCodeFactory-Data, comprising 5,045 high-quality task instances and multi-turn interaction trajectories. Fine-tuning Qwen3.5-9B and Qwen3.8-27B on 3DCodeFactory-Data significantly improves performance on BlenderWorld, P3D-Bench, and 3DCodeBench, consistently outperforming models trained on existing open-source 3D code datasets, with our 27B model further surpassing the same-series 2.4T flagship Qwen3.8-Max in overall performance.

---


### 127. [DiscernBench: Evaluating Cooperative Discernment of LLM Agents in Institutional Settings](https://arxiv.org/abs/2611.28787)

**<font color=#1a73e8>作者：</font>** Disha Sheshanarayana, Tanishka Magar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The deployment of large language models in operational settings demands evaluation of judgment under institutional constraint. We introduce DiscernBench, a benchmark for evaluating cooperative discernment: the ability of an agent to determine whether to comply with, refuse, or escalate a request in an institutional setting. DiscernBench comprises scenarios derived from real-world incident reports across domains such as aviation, law enforcement, and emergency management. We evaluate eight LLMs across three decision-making configurations and analyze both final decisions and the intermediate judgments produced during multi-agent deliberation. Under disagreement, Final Responders exhibit model- and role-dependent aggregation patterns in which a lone specialist recommendation can disproportionately influence the collective decision, a phenomenon we term Minority-Signal Override. Role-specialized multi-agent deliberation raises average over-escalation from 3.79% under direct single-agent judgment to 28.27%, with the direction and magnitude of minority-signal influence varying substantially across models and specialist roles. These results reveal distinct collective decision behaviors that are not captured by final-answer accuracy alone. Trustworthy multi-agent systems therefore require evaluating not only individual specialist reasoning, but also how conflicting judgments are transformed into collective decisions. Code and data are available at this https URL.

---


### 128. [HighwayVerse: A Chain-of-Inspection Benchmark for Highway Infrastructure Anomaly Understanding](https://arxiv.org/abs/2611.28800)

**<font color=#1a73e8>作者：</font>** Junyi Yang, Zheng Si, Yilin Zhai 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Practical highway infrastructure inspection entails progressive diagnostic reasoning from visual perception to maintenance decisions, yet existing benchmarks remain confined to isolated tasks, leaving Multimodal Large Language Models (MLLMs) insufficiently evaluated across sequential inspection stages. Meanwhile, current datasets focus primarily on highway pavement defects, falling short of real-world inspection across diverse infrastructure components such as highway pavements, guardrails, glare screens, and drainage systems. To address these gaps, we formulate the Highway Infrastructure Inspection Progression Chain (HIIP-Chain), spanning Anomaly Detection, Anomaly Recognition, Condition Analysis, and Maintenance Resolution, and introduce HighwayVerse. HighwayVerse comprises 14,143 real-world Ground and Unmanned Aerial Vehicle (UAV) inspection records spanning 100 and 17 anomaly categories, respectively, with 84,858 expert-reviewed question-answer pairs. We evaluate 12 open-source and closed-source MLLMs using the chained metric Final, which credits a correct maintenance decision only when all preceding diagnostic stages are completed correctly. Results show that although models achieve relatively high accuracy when initially judging whether an anomaly is present, their markedly lower Final scores expose struggles across downstream recognition, analysis, and decision-making. This discrepancy indicates that current MLLMs do not fully comprehend specific highway anomaly patterns beyond superficial initial judgments. Furthermore, we propose LaneRAG, a training-free retrieval-augmented framework that provides hierarchical reference guidance achieving consistent performance improvements across diverse MLLMs. Our dataset, evaluation benchmark, and source code will be publicly released.

---


### 129. [Synthetic EHR Generators Should Be Audited Like LLMs](https://arxiv.org/abs/2611.28804)

**<font color=#1a73e8>作者：</font>** Inigo Stibbe, Padmanabhan Ramnarayan, A. Aldo Faisal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic electronic health record (EHR) generation is increasingly adopting large autoregressive models, yet privacy evaluation has not kept pace, relying heavily on similarity-based heuristics and aggregate metrics that can obscure patient-specific memorisation. We argue that these models should additionally undergo LLM-style memorisation audits at the level of individual patient records. We support this position by comparing membership-inference evaluations across four prominent autoregressive EHR generators, highlighting inconsistent evaluation practices in patient representations and attack procedures. We evaluate trajectory reconstruction from partial context and introduce randomly assigned patient-level canaries to distinguish memorised associations from clinical generalisation. We examine these methods in a GPT-2-style model deliberately overfit to 1,000 MIMIC-IV patient trajectories, creating a controlled setting in which memorisation should be readily detectable. The model systematically recovers training patients' canaries, and their trajectory reconstruction approaches perfect accuracy with increasing context. Held-out patients show no systematic canary recovery, while reconstruction remains low and improves only marginally with additional context. These experiments establish a positive-control baseline for further evaluation of these methods in realistically trained models.

---


### 130. [Pixel Auto-Encoder: Reconstructing Language Model Activations Through Pixel Art](https://arxiv.org/abs/2611.28822)

**<font color=#1a73e8>作者：</font>** Haru Furuichi, Phan Xuan Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpreting the high-dimensional internal representations of large language models (LLMs) remains a challenging problem. Recent approaches have explored translating these representations into human-understandable forms, particularly natural language. In this work, we explore the use of images as an alternative target modality for interpreting LLM activations. As a first step toward this goal, we introduce Pixel Auto-Encoder, which converts intermediate LLM activations into $32 \times 32$, 32-color pixel art and reconstructs them for subsequent computation within the model. By encouraging the intermediate representations to resemble predefined concept images, we investigate whether LLM activations can be expressed visually while preserving the model's language capabilities. We find that the model can produce target-aligned images for some concepts, and that replacing pixel representations with concept images can influence next-token predictions. However, we also observe a trade-off between visual alignment and language-model performance, as well as sensitivity to pixel-level changes that are difficult to interpret visually. These findings demonstrate the feasibility and limitations of image-based representations of LLM activations.

---


### 131. [When Being Wrong Is Right: Reverse-Capability Audio CAPTCHAs through Psychoacoustic Design](https://arxiv.org/abs/2611.28823)

**<font color=#1a73e8>作者：</font>** Mingjie Bao, Yu Dai, Guangke Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large audio-language models (LALMs) have recently been shown to bypass audio CAPTCHAs designed around limitations of automatic speech recognition. To address this threat, we introduce reverse-capability verification, a general CAPTCHA framework that reverses the conventional human-easy, machine-hard relationship with respect to the physical ground truth. It selects challenges in which stable human perceptual limitations cause the human-reference answer to differ from the physical ground truth, while machine analysis tends toward that truth. Because the verifier accepts the human-reference answer, advanced solver capabilities and resulting improved recovery of the physical ground truth may instead strengthen the human-machine separation.
We instantiate the framework through psychoacoustics and design two audio CAPTCHAs: HIPI, a classification task, and YINGCHEN, a counting task, together with their conjunctive composition. Across seven LALMs and eight attack strategies, the maximum observed machine acceptance rates are 19%, 17%, and 3% for HIPI, YINGCHEN, and their composition, respectively, compared with 45-100% for nine prior schemes. A multidimensional human usability study yields corresponding human acceptance rates of 78%, 90%, and 76%, while maintaining competitive efficiency and satisfaction. Further analysis demonstrates that advanced LALMs tend toward physical ground truth. These results show that reverse-capability verification substantially reduces machine acceptance while retaining high human acceptance through an approach different from conventional CAPTCHAs.

---


### 132. [Does a Frontier Large Language Model Know What It Can Solve? A 100-Conjecture Calibration Study](https://arxiv.org/abs/2611.28827)

**<font color=#1a73e8>作者：</font>** Ayush Khaitan, Liam Fowl, Tomàs Ortega 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How does confidence correlate with actual performance in large language models, when attacking open research-level math problems? We address this question by studying the performance of ChatGPT 5.6 Sol Ultra on a set of 100 open conjectures in geometric analysis. By construction, the model first selected open problems in geometric analysis that it assessed that it had at least a 50\% chance of proving or disproving, and then assigned a probability of success to each question. 13 questions were then excluded after an audit, and the model was asked to resolve the remaining 87 problems. Its mean stated resolution probability was $0.617$, versus an observed rate of $0.103$ (Brier score $0.351$, ECE $0.513$), thereby demonstrating that the model was systematically over-confident in its self-assessment. However, the scores retained ranking signal (AUROC $0.714$). The model was highly overconfident in probability magnitude but did more often than not assign a high probability of success to the problems that it did resolve, than the problems that it did not. Hence, its probabilities were numerically mis-calibrated but directionally correct. All proofs have been formalized in Lean, thereby verifying correctness, and have been run through a semantic equivalence pipeline to ensure semantic equivalence between the formalized and informal statements. These are exploratory campaign outcomes, not fixed-budget success probabilities. The certificates prove formal statements; for a couple of questions, some geometric inputs are assumed in the lean proofs.

---


### 133. [Hidden Sensitivity in LLM Pre-training: A Dynamic System View](https://arxiv.org/abs/2611.28830)

**<font color=#1a73e8>作者：</font>** Bo Liu, Yuan Xie, Junan Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Large Language Model (LLM) pre-training, loss curves can conceal substantial instability, i.e., even small perturbations may lead to dramatically different predictions while leaving loss nearly unchanged. To investigate this phenomenon and reveal the underlying mechanisms, we first formulate LLM pre-training as a non-autonomous dynamical system that jointly evolves model weights and Adam optimizer states. Based on this formulation, we introduce a normalized sensitivity score in optimizer-relative coordinates to identify sensitive training checkpoints. At one such checkpoint, a weight perturbation of only 10^(-5) leads to 35.7% disagreement in top-1 predictions and 16.2% disagreement in benchmark answers after 200 training steps, with only 0.8% of greedy generations remaining identical despite similar validation losses. Furthermore, we find that perturbations to Adam's first and second moments induce comparably large effects, with similar sensitivity patterns observed in OLMo-1B. Finally, guided by our diagnostic, targeted stabilization reduces top-1 disagreement to 0.83% and increases generation exact match to 88.3%, at the cost of a 0.11-nat increase in validation loss. Our findings reveal a hidden form of optimizer-state-dependent sensitivity in LLM pre-training that conventional loss-based evaluations may overlook, while demonstrating its potential for diagnosis and mitigation.

---


### 134. [Self-WSP: Can Language Models Improve Themselves Through Weight-Space Programming?](https://arxiv.org/abs/2611.28833)

**<font color=#1a73e8>作者：</font>** Guoming Ling, Shanshan Zhong, Kaixuan Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier language models can now read and edit the weights of a neural network much like code and thereby improve a small model, an approach known as Weight-Space Programming (WSP). We further explore applying WSP to a language model itself, which we call Self-WSP. Specifically, Qwen3.5-0.8B reads its own weights, proposes an edit, and then continues with the edited weights as both problem solver and editor. We find many cases of genuine self-improvement. Self-edits can raise GSM8K accuracy from 11.8% to 62.2% and MATH500 accuracy from 7.0% to 32.2%, sometimes by changing only 16 parameters, and in some cases repeated self-editing keeps improving the model. A closer look, however, reveals that these gains lack interpretability. The model shows little understanding of the edits it makes, and WSP driven by random search sometimes performs comparably. Self-WSP thus holds promise as a path toward recursive self-improvement (RSI), but realizing this promise requires further exploration.

---


### 135. [Omni-H3-Image: Constrained Foundation Priors Usher in a New Era of All-in-One Blind Image Restoration](https://arxiv.org/abs/2611.28836)

**<font color=#1a73e8>作者：</font>** Zihao He, Songhua Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Off-the-shelf unified image models such as 33B MiniMax-H3-Image, FLUX.1-Kontext, and Qwen-Image-Edit-2511 synthesize crisp textures yet collapse to 11.33-16.74 dB PSNR across 429 degraded public restoration scenes due to spatial drift, chromatic hallucination, and semantic fabrication. We present Omni-H3-Image (Omni-H3), an approximate three-stage constrained posterior projection framework over unmodified MiniMax-H3-Image and Qwen3-VL-32B using only a 0.92M-parameter auxiliary weather pre-conditioner (<0.003% of backbone weights). Omni-H3 unifies blind physics-VLM sensing with exact-32 px lattice anchoring, joint affine-Wiener-Butterworth projection in opponent YCbCr space, and closed-loop Z=4 text verification with sub-Nyquist abstention. Across 925 blind tasks against 11 external SOTA baselines -- five public benchmarks (N=647), Dev-160, and a held-out locked_test suite (N=118) -- Omni-H3 recovers +4.73 dB degraded-scene PSNR over Base H3 (21.47 vs. 16.74 dB; +6.27-10.14 dB over other omni backbones) while winning overall #1 DISTS (0.207), #1 NIQE (4.45), and #1 Edge-F1 (0.807) on all 429 degraded public scenes (MUSIQ 66.8 vs. 40-44 for discriminative SOTA), 76.59 dB on CBSD68 Clean, -91.6% Urban100 chroma drift, #1 2K Dev Non-Clean DISTS (0.202), and #1 locked_test 2K DISTS (0.173) and 132-ROI SubCER, cutting pre-annotated 132-ROI SubCER from 0.456 to 0.319 under non-Qwen RapidOCR (PP-OCRv4) (with recognizer-dependent tradeoffs under TrOCR-large-str).

---


### 136. [Spatially Grounded Latent Lookahead for Vision-Language-Action Models](https://arxiv.org/abs/2611.28839)

**<font color=#1a73e8>作者：</font>** Qihang Chen, Tengjie Li, Hongwei Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models benefit from strong semantic representations that support object recognition and instruction understanding. However, precise manipulation also depends on resolving object locations and workspace relations, and on selecting actions with an estimate of how the scene will evolve. Existing geometry-aware methods make the current scene more explicit, while predictive methods model future observations or representations. Yet future information is often neither grounded in a control-relevant spatial state nor directly used to guide action generation. We introduce Spatially Grounded Latent Lookahead (SG-LL), which uses the grounded present as the reference for predicting an actionable near-future representation. A frozen spatial teacher first distills geometric priors into policy-connected spatial tokens. A current-conditioned bottleneck then learns a compact latent that captures future information relative to the present scene. This latent is predicted from the current policy context and initial Action Expert features, without access to future observations or the spatial teacher. Finally, zero-initialized residual fusion incorporates the predicted latent into the Action Expert to refine action generation. Experiments on LIBERO-Plus, CALVIN, and three real-world manipulation tasks demonstrate improvements over
in both simulation and real-robot settings.

---


### 137. [AgriManager: A Framework and Benchmark for LLM-RL Generalization in Agricultural Management](https://arxiv.org/abs/2611.28844)

**<font color=#1a73e8>作者：</font>** Chi Gui, Junwen Zheng, Ritwik Nigam 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agricultural management is heterogeneous along two axes. The first is distributional shift within a fixed task interface: weather, crops, and prices vary across years and locations while sensors, actions, and objective stay fixed. The second is structural shift across interfaces: different farms expose different observed variables, available actions, and management objectives. We formalize the second axis as schema shift: variation in the policy-facing schema $\Sigma = (\Sigma_O, \Sigma_A, \Sigma_R)$ between training and deployment. We test whether LLM-RL generalizes across both axes with AgriManager, to our knowledge the first framework that trains LLM policies with RL across multiple process-based crop simulators, unifying DSSAT, WOFOST, and Cycles. We design a three-tier generalization ladder: Tier 1 within-schema distributional shift, Tier 2 single-axis schema shift along $\Sigma_O / \Sigma_A / \Sigma_R$, Tier 3 compositional schema shift across simulators, all scored on a frozen held-out test suite with three training seeds per method. Within fixed schemas, Qwen3-4B trained by RL with explicit reasoning exceeds neural-network PPO trained with the same interaction budget; without reasoning, training stalls near no-action where the reward penalizes input use. Under single-axis schema shift, $\Sigma_O$ transfer needs decision-critical state, $\Sigma_A$ results are consistent with joint action-menu coverage, and with reasoning a policy trained on yield alone transfers to unseen objectives. Under compositional schema shift, single-source training mostly hurts zero-shot transfer across simulators, and a unified policy trained only on other combinations of the same components recovers about 86% of the gain of a specialist trained on the target combination on DSSAT and stays below the specialists on the WOFOST and Cycles profit targets. Project page: this https URL

---


### 138. [CivilCADBench: Benchmarking Multimodal LLMs for Understanding, Reconstructing, and Designing Civil Engineering Drawing Sets](https://arxiv.org/abs/2611.28853)

**<font color=#1a73e8>作者：</font>** Zelin Zheng, Difei Wu, Xinyan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Civil infrastructure is designed, built, and maintained through engineering drawing sets, yet preparing and revising them remains labour-intensive and calls for automation. Multimodal large language models (MLLMs) are promising candidates, but assessing them requires a benchmark grounded in real engineering practice. We introduce CivilCADBench, a benchmark for understanding, reconstructing, and designing civil engineering drawing sets, built from real infrastructure drawings and source CAD files containing over 250,000 CAD entities. Unlike parametric 3D CAD models, these drawings are dense, layered, and multi-sheet; and since prints are lossy projections with no pixel trace of layers, a file can print correctly yet remain wrongly organised. CivilCADBench comprises three task families of increasing difficulty: understanding tasks are evaluated with 2,183 expert-reviewed questions ranging from single sheets to whole sets, while reconstruction and design tasks are agentic, requiring models to rebuild printed pages as editable CAD files, either as single pages or entire drawing sets, and to produce new designs. These tasks are performed across 232 pages, 28 sets, and 19 design tasks, and evaluated by a deterministic scorer that compares model outputs with the designers' source files on geometry, layers, text, and dimensions. We evaluate seven frontier MLLMs on CivilCADBench, and find that they read and redraw printed content accurately but recover the file structure poorly: the best model scores above 90% in understanding and single-page reconstruction, yet only 60% on layer assignment and 48% on design. Grounded in real engineering practice, CivilCADBench exposes both the capabilities and the limitations of frontier models in professional civil engineering, laying a foundation for next-generation models and agentic systems for intelligent civil engineering.

---


### 139. [Thakaa at AlexandriaX-2026: Who Gets the Final Say? Assigning Output Authority in Dialectal Arabic Machine Translation and Error Detection](https://arxiv.org/abs/2611.28857)

**<font color=#1a73e8>作者：</font>** Meshal Alamr, Maryam Altuwaijri, Hassan Alqaeri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We report first-place systems for all four evaluated AlexandriaX-2026 settings: both English-to-dialect translation tracks, cross-dialect translation, and translation-error detection. In unconstrained translation, our minimum Bayes risk (MBR) selection restricts output authority: four local systems can supply the translation, while seven additional systems contribute only reference evidence. Candidate-constrained MBR beats the strongest complete candidate in all 13 dialects and gains 1.2554 macro spBLEU overall, reaching 33.4891. It also surpasses a retrospective oracle selecting the best whole candidate system per dialect. In the constrained track, country-routed LoRA adapters over a shared NileChat-3B-Base backbone incorporate the released Libyan and Sudanese supervision absent from the training and development splits, raising macro spBLEU from 29.5969 to 30.4233. Post-evaluation, a single adapter trained on all released Alexandria data reaches 30.4733 macro spBLEU; averaging model weights across three training seeds raises this to 30.9726 while retaining one model for inference. For cross-dialect translation, nonparallel target-dialect retrieval guides deliberation, raising Gemma-4-31B-IT without fine-tuning from 24.6898 to 28.4011 spBLEU. For translation-error detection, GPT-5.5 proposes semantic error regions, while MARBERTv2 controls their character boundaries and corroborates additional spans, raising Overall from 0.4691 to 0.4982.

---


### 140. [Interaction Retention and Output-Likelihood Training in Parallel Sampling](https://arxiv.org/abs/2611.28858)

**<font color=#1a73e8>作者：</font>** Da Li, Bo Jin, Xiaopeng Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parallel samplers such as masked diffusion language models generate several coordinates per step from conditional marginals and randomize which coordinates are generated together, so even exact conditionals return a distorted distribution. We give an exact local account of this distortion. Around any full-support product law, the Gram operator of the sampler's response is diagonal in the interaction decomposition, and its eigenvalues are retention probabilities: the probability that an interaction has a unique latest-revealed coordinate. This retention spectrum determines the exact frontier between output accuracy and conditional calibration, its regularization path, and the population response of finite-mixture likelihood training. For pairwise interactions it yields a sharp dichotomy. Under homogeneous retention, output-likelihood training is equivalent to a single context gain; heterogeneous retention opens correction directions beyond any scalar, with an advantage bounded by an explicit heterogeneity gap. On binarized digits and MNIST, output-likelihood training within a heterogeneous schedule library lowers calibrated test negative log-likelihood in all twelve paired comparisons, and the gain survives pair-specific recalibration and a stronger path optimizer. For a frozen 169.6-million-parameter masked diffusion language model, serially normalized context gains are 1.070 and 1.056 at 8 and 16 rounds, against the predicted values 1.134 and 1.058.

---


### 141. [Thakaa at StanceEval-2026: Inference-Time Target Grounding for Arabic Stance Detection](https://arxiv.org/abs/2611.28860)

**<font color=#1a73e8>作者：</font>** Meshal Alamr, Hassan Alqaeri, Abdullah Aldahlawi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> StanceEval-2026 tests Arabic stance classification under target shift, with evaluation targets absent from the labelled task data. We test two ways to supply target information at inference time. For Track 1, we retrieve eight labelled Women Driving demonstrations from the external ArabicStanceX corpus and score the three label tokens with Gemma-4-31B-IT. For the unseen-target track, we prepend cached target context prompted to be factual and non-evaluative, then fuse label predictions and label-token scores from multiple LLMs, with final assignments constrained by published class totals. The systems obtain 85.22 and 91.78 Favg2 on Tracks 1 and 2, ranking sixth and fourth in the final standings. On held-out ArabicStanceX tweets, direct prompting scores 79.45 Favg2; eight random Women Driving demonstrations raise it to 84.78, and similarity retrieval reaches 89.04. Across three target-held-out Mawqif evaluations, a fixed target card raises Gemma-4-31B-IT from 86.54 to 86.93, whereas QLoRA lowers Gemma-4-12B-IT from 84.43 to 83.77. In these separate public evaluations, same-target demonstrations and retrieval improve performance, factual target context provides small, target-dependent gains, and the tested source-only adapter does not improve.

---


### 142. [Postpartum Sense-Making and AI in a Fragmented Care System](https://arxiv.org/abs/2611.28870)

**<font color=#1a73e8>作者：</font>** Diana Freed, Maja Mishevska  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Postpartum women must navigate health information across a fragmented landscape of clinicians, peers, online communities, influencers, and, increasingly, large language models (LLMs). Existing evaluations of LLMs in health contexts primarily ask whether systems provide accurate, safe, and readable information. We argue that these criteria, while essential, are insufficient for understanding how LLMs may affect postpartum care. LLMs enter an information ecology in which women are already required to reconcile competing forms of expertise, determine whether their experiences are normal or concerning, and decide when and where to seek care. At the same time, online representations of motherhood and femininity shape which postpartum experiences are made visible and what forms of self-management are expected of women. Drawing together research on postpartum care gaps, online help-seeking, influencer cultures, gendered responsibility, and AI-supported health information, we position LLMs as emerging intermediaries within this broader care infrastructure. We argue that evaluating postpartum AI requires examining not only information quality, but also how these systems shape epistemic coordination, transitions to formal care, and the distribution of responsibility for making fragmented systems of care work.

---


### 143. [FormaFin: Verifiable Financial Analysis with Solver-Guided Reinforcement Learning](https://arxiv.org/abs/2611.28881)

**<font color=#1a73e8>作者：</font>** Bethel Hall, William Eiers  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formally verifying financial analyses generated by large language models (LLMs) remains challenging as financial rules are largely expressed in natural language and rarely have corresponding formal specifications. Training language models to formalize these rules is hindered by the scarcity of labeled data and reliable training signals, while confidential financial data favor small models that run locally. We introduce FormaFin, a framework that trains small open language models to translate financial rules into reusable SMT formulas. FormaFin integrates teacher distillation with reinforcement learning using an SMT solver to compute rewards from numerical thresholds stated in financial rules. We evaluate FormaFin on corporate loan monitoring, in which lenders check borrowers' financial figures against loan agreements. To evaluate our framework, we curate \bench{}, a benchmark containing 143 loan agreements and 2,527 questions covering compliance, earnings cushion, and debt capacity. Our results show that a 7B formalizer achieves 94.8\% accuracy, outperforming open LLMs up to ten times larger. Across three model families, accuracy ranges from 92.6 to 96.8\%. Our framework also detects 95.6 to 99.7\% of errors in other LLMs' financial analyses. We make FormaFin and \bench{} publicly available.

---


### 144. [StudioBench: Benchmarking Agentic Multimodal Large Language Models for Productive Audiovisual Creation](https://arxiv.org/abs/2611.28902)

**<font color=#1a73e8>作者：</font>** Xinglong Xu, Yuxia Zhu, Siyuan Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Video generators can now render convincing short clips, yet complete audiovisual works require coordinating visuals, sound, and editing across multiple stages. Existing benchmarks focus on individual generators or video agents under narrower production settings, leaving end-to-end creation by general multimodal large language models (MLLMs) underexplored. We introduce StudioBench, a benchmark comprising 160 tasks across eight video genres and five task types, spanning diverse audiovisual production requirements. Models produce minutes of finished audiovisual content using 33 atomic generation, editing, and inspection tools, without shell access or workflow templates. We evaluate the delivered films, while analyzing reconstructed workflow graphs to characterize production behavior and diagnose failures. Across seven MLLMs, explicit requirements are nearly saturated, yet production quality varies substantially in picture clarity and composition, object structure, motion, and lip sync. All models spontaneously organize multi-stage production workflows without predefined templates. However, higher-quality models exhibit more selective production workflows, whereas additional tool calls alone show little association with quality. These findings identify the missing quality loop of effective inspection, selection, and revision as a key bottleneck in productive audiovisual creation.

---


### 145. [STRIDE: Strategy-to-Tactics Retrieval-Guided Skill Disclosure and Evolution for Agentic Reinforcement Learning](https://arxiv.org/abs/2611.28907)

**<font color=#1a73e8>作者：</font>** Shixin Hong, Wanqing Cui, Yibo Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill-augmented reinforcement learning enables LLM agents to reuse task-solving knowledge across episodes, but existing systems typically expose agents to a flat skill pool and update skills only from coarse, episode-level outcomes. This conflates two distinct uses of experience: a stable strategy that should frame the whole episode, and tactical know-how that should be retrieved only when the agent reaches a local execution gap. We propose STRIDE (Strategy-to-Tactics Retrieval-guided skIll Disclosure and Evolution), a framework that brings progressive skill disclosure into agentic reinforcement learning. STRIDE keeps the selected strategy visible as episode context, exposes a compact tactic menu, and loads full tactic content only after an explicit retrieval action. This interface turns each retrieval into an event-level credit unit: the same event provides process feedback for learning when to retrieve and supplies evidence for skill-bank evolution. On ALFWorld, STRIDE achieves a 92.7% average success rate with Qwen3-4B and a 94.9% average success rate with Qwen3-8B. On WebShop, it improves over the strongest reproduced skill-augmented baseline by 4.5 score points and 1.9 success-rate percentage points. These results show that skill reuse is most effective when persistent strategies preserve global task structure and tactics are disclosed only at local decision bottlenecks.

---


### 146. [From Dense to Sparse: Morton-Ordered Sparse Mapping for Efficient 3D Mesh Generation](https://arxiv.org/abs/2611.28913)

**<font color=#1a73e8>作者：</font>** Junjie Yang, Rui Qian, Yijiang Li 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified 3D understanding and generation require compact sequences preserving spatial structure. Dense grids yield long sequences, while serialization can separate spatial neighbors. We propose Sparse Proximity Aware Compression (SPAC), a shared sparse SDF vocabulary combining sparse encoding with reversible spatial merging. A Sparse SDF VQ-VAE quantizes near-surface features while retaining explicit coordinates, using reconstruction supervision for surface fidelity and detail. 3D Byte-Pair Encoding (3D-BPE) merges recurring face-adjacent patterns using relative offsets before serialization. Macro tokens expand exactly into leaf tokens and coordinates. After Morton serialization, a shared LLM reads geometry for captioning and predicts tokens that decode into meshes for text-conditioned generation. With fixed geometry, architecture, and band width in voxels, sparse encoder cost grows approximately quadratically with resolution. 3D-BPE reduces mean complete LLM sequence length by 45.4 percent, including coordinates, text, and control tokens. SPAC achieves strong results in both 3D captioning and text-conditioned mesh generation. Ablations show gains over leaf tokens and Morton 1D-BPE in both tasks. The project page at this https URL .

---


### 147. [Can Open LLMs Clear Sanctions-Screening Alerts? A Pre-registered Test on Public Sanctions Lists with Turkish Name Variants](https://arxiv.org/abs/2611.28914)

**<font color=#1a73e8>作者：</font>** Mehmet Murat Huyut  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sanctions screening raises name-based alerts that are mostly false positives, and level-1 analysts clear them by checking the customer's date of birth and name against a written policy. We test whether open-weight language models that a bank can run on its own premises can perform this level-1 disposition. From the UK and EU sanctions lists (7,103 natural persons) we built 12,200 synthetic customers: listed persons under six name conditions, including Turkish spellings of Arabic-origin names and Turkish romanisations of Cyrillic names, and two date-of-birth conditions, plus namesakes, near-name customers and a general population. A deterministic fuzzy and embedding screen raised 7,383 alerts, which three open models served on domestic infrastructure and three rule baselines dispositioned under the same policy. The models sent far fewer innocent customers to level 2 than a rule that applies the policy's date clause: 0.6 to 16.9 per 1,000 screened customers against 24.4, and they stated the date-of-birth status correctly in 98.3% to 98.5% of alerts. They also failed to escalate 1.5% to 2.2% of the listed persons. The pre-registered non-inferiority test against the rule was met, but only because of a construction error we found after the analysis: 21 customers in the "minor discrepancy" condition had dates that conflict under the policy. Without them the rule misses no listed person and no model meets the margin. The misses had model-specific causes: one model read minor date discrepancies as conflicts, one declared word-order and typing variants to be different names, and one discounted alerts that its own rationale said to escalate. Fuzzy matching found 69% of the Turkish spellings of Arabic-origin names; adding embeddings raised this to 74%. Open LLMs can cut level-1 workload, but on this evidence only behind a deterministic date check and with every name doubt escalated.

---


### 148. [OmniDecisionBench: Evaluating and Benchmarking the Multimodal Jev-Style System One Decision Models](https://arxiv.org/abs/2611.28924)

**<font color=#1a73e8>作者：</font>** Tianxiang Gao, Jinzhe Li, Yue Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal System One models answer visual tasks with typed decisions and native probabilities, yet no holistic evaluation compares them with general VLMs or maps either class's capability boundaries. We introduce OmniDecisionBench, a holistic benchmark of multimodal System One models. Its main evaluation assigns 45 datasets (192,975 records) to five capability families and twelve primary angles across four typed interfaces, scoring accuracy and candidate-probability calibration. A validation layer adds three single-factor diagnostics varying visual presentation, textual evidence sufficiency, and target dataset. Across three System One models and two general VLMs, three regularities emerge. First, strengths depend on angle and metric: System One models lead discrete tasks overall with lower ECE15 on most perception, reading, and reasoning angles (Jev 1.14: 80.14% accuracy, 4.50% ECE15), while general VLMs lead ordinal grading and outperform Jev 1.14 among the three models tested on direct Box grounding. Second, multi-image and abstract reasoning bound every model, where confidence rather than accuracy separates them. Third, reliability shifts with the input: rendering only options nearly triples Jev 1.14's selective risk at nearly flat mean signed bias, and donor risk cutoffs often exceed target risk across unseen datasets and task families. OmniDecisionBench thus maps which model class suits each angle and where reliability ends. The code and dataset will be available at this https URL.

---


### 149. [Definition-Guided In-Context Learning for Zero-Shot Spoken Language Understanding](https://arxiv.org/abs/2611.28929)

**<font color=#1a73e8>作者：</font>** Neeraj Agrawala, Sriram Ganapathy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting spoken language understanding (SLU) systems to novel or revised label taxonomies conventionally requires additional labeled data and retraining, creating a bottleneck for real world deployment. While in-context learning with few-shot demonstrations offers an alternative, multi-modal generalization and scaling has been challenging. In this work, we investigate whether natural-language definitions alone can guide zero-shot SLU without demonstration exemplars, finding that symbolic definitions serve as the primary supervisory driver for adapting speech-text models. We operationalize this principle as Definition-Guided In-Context Learning (DG-ICL), a fine-tuning framework that decouples semantic categories from fixed lexical names. By replacing labels with dynamically randomized definitions (arbitrary synthetic tokens in DG-ICL-Sym or permuted vocabulary words in DG-ICL-Flip), DG-ICL avoids lexical shortcuts and encourages the model to ground acoustic representations in contextual definitions. Novel categories can thus be introduced at inference simply by defining them through the instructions. Across three speech-text models (AUDIO FLAMINGO 3, QWEN2-AUDIO, and SALMONN), DG-ICL outperforms standard instruction tuning on held-out tasks under novel symbols (0.663 vs. 0.449 macro-F1 on Audio Flamingo 3; 0.703 vs. 0.620 on Qwen2-Audio; 0.582 vs. 0.399 on SALMONN), while remaining competitive on original labels. Furthermore, counterfactual evaluations demonstrate instruction following abilities, where it is shown that DG-ICL-Sym retains 68% of its performance when definitions contradict pre-trained lexical priors, whereas standard instruction tuning elicits significantly reduced retention of 21%. Finally, we show that DG-ICL enables zero-shot speech clustering into user-defined categories specified on the fly

---


### 150. [CANDOR: A Multilingual Provenance-Documented Corpus for Dysarthric Speech Research](https://arxiv.org/abs/2611.28930)

**<font color=#1a73e8>作者：</font>** Bernard Muller, LaVonne Roberts, Leo Kaiya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> CANDOR assembles 61 corpora across 17 languages and five aetiological classes plus a mixed/other group. Its register counts 2,057 speakers classified as dysarthric and 19,538 healthy controls. The collection contains 4,469.7 hours of audio, including 1,178.8 hours in the dysarthric subset. Counts use speech-impairment labels where available and diagnosis labels otherwise. The collection includes 732 dysarthric speakers across 14 non-English languages; 194 speakers use six languages unsupported by Qwen3-ASR, the model underlying its non-English baselines. We document composition, chain of custody, licences and transfer terms, while distinguishing corpus-level provenance from participant-level consent records, which we hold for few constituents. Among 31 dysarthric-bearing corpora, open licences cover 29.0% of corpora, 10.5% of speakers and 8.2% of hours. Excluding the English Speech Accessibility Project raises the open hour share to 31.2%, showing its dependence on this collection's composition. CANDOR cannot be redistributed as a single audio resource; we specify public, restricted and conditional artefacts. Severity labels available in 15 corpora do not provide a validated cross-corpus mapping. Within the non-English ASR baselines, only Mandarin yields a real-speech estimate meeting our evaluation criteria. It differs sharply from the synthesis result and remains imprecise; an English challenge result uses a different model and protocol. CANDOR provides a documented basis for research on under-represented languages while making constraints on evaluation, comparability and sharing explicit.

---


> [!TIP]
> 当前位于：**101-150**（第 3/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-486](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
