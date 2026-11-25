# 🧠 大模型相关研究 | 2026年11月26日

> 本类共 **299** 篇论文：已确认 **280** 篇，待复核 **19** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-299](./part-06.md)

---

### 151. [LLM Agent Authorization Across Context Compaction](https://arxiv.org/abs/2611.32194)

**<font color=#1a73e8>作者：</font>** Zeming Fei, Hongming Fei, Yi Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Request-derived authorizers such as Progent protect LLM agents from prompt injection by deriving what an agent may do from the user's request. Their guarantee rests on attribution: the request is taken to be what the user said. Compaction breaks it. At every automatic compaction we observed, Claude Code and Codex placed a model-written summary of earlier turns as a user message, so the compactor's quotation of the user, documents and injected text reads as the user speaking. Because a policy frozen at the first request lets the agent finish few later tasks, we let Progent derive its policy for each request, and find that what it grants then follows what the compactor wrote. Even a payee the user stated is not safe: when an attacker's notice states another account as plain data and the user asks to pay the rent, the policy derived from a frontier compactor's summary admits the notice's account in 91% of cases, and the one derived from the user's own words in none. The cause is general: we prove that an authorizer that cannot see who wrote which bytes cannot treat a forged record differently from the legitimate one it imitates by more than the two are distinguishable, and that the bound is tight. Frontier compactors bear this out: they mark injected instructions, which have no legitimate twin, but rarely injected data, which does. What a compactor keeps, and how it marks it, is a security parameter. The fix follows from attribution: the authorizer credits only what the user said, authenticated on arrival and carried verbatim across the boundary, while the agent still reads the summary. We prove that it then receives exactly that text or nothing, so an attacker can block the policy but cannot shape it, and adaptive attacks on our implementation confirm it. In 40 attacked AgentDojo episodes re-run with the fix, no attacker action completes while the agent reads the summary.

---


### 152. [When Answering Is Administering: Permission Replies That Rewrite Coding-Agent Policy](https://arxiv.org/abs/2611.32195)

**<font color=#1a73e8>作者：</font>** Zeming Fei, Hongming Fei, Jingwen Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding agents let plugins and remote services answer permission prompts, and Claude Code documents that such an answer cannot override the operator's deny rules. However, we show that this guarantee, checked one decision at a time, fails over a whole run, because an answer to one permission prompt can rewrite the policy that every later answer is checked against. For example, a remote service with no access to the operator's files approves an unrelated command and attaches an update that deletes the deny rule protecting the project's secrets. The agent then reads the secrets in that session and the next, even inside the vendor's strict sandbox. The root cause is that Claude Code checks only updates that add or replace allow rules. Relays that forward such deletions already exist, including the vendor's own Remote Control. In effect, the right to answer a prompt has become the right to administer the policy. Worse, the deletion leaves the same records as a local edit by the operator, so Claude Code cannot tell who wrote a rule.
More generally, what a runtime records decides what it can safely delegate. A runtime that cannot tell who wrote a rule can accept only updates that keep every currently denied call denied, whereas, to protect every party's restrictions, a runtime that records who wrote each rule can let each party remove only the restrictions proven to be its own. We prove that these two bounds are tight. They correctly predict whether the operator's restrictions survive in all thirteen permission designs across ten agent systems, including predictions we wrote down before running Codex, Gemini CLI, opencode, and Goose. Enforcing the bounds at the shared update step blocks the attack. A survey of 2,227 fetched marketplace plugins finds only two that send policy updates.

---


### 153. [Steerable by Design: Conditional Pretraining for Robust Control of Language Models](https://arxiv.org/abs/2611.32199)

**<font color=#1a73e8>作者：</font>** Henry Castillo, Yanchen Liu, Claudio Mayrink Verdun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Our goal is to build language models that are steerable by design. Today's language models are pretrained with next-token prediction, which relegates alignment and control to the final 1% of training tokens or inference-time interventions. These models repurpose a single input channel for both instructions and data, leading to common failure modes where the model mistakenly treats data as instructions such as intentional jailbreaks and unintentional in-context alignment drift. To correct this, we propose a pretraining method and architecture that separates the two from the very start, producing Mancelle-3B. An encoder processes high-level semantic features of upcoming text with cross-attention that prevents the token stream from writing back into this control channel. During pretraining, the model learns to rely on these features to predict the next token, turning the channel into an effective handle for steering the model. Mancelle-3B steers more strongly than prompt- and activation-based methods on comparable open models while maintaining fluency, and it withstands adversarial black-box and soft-prompt counter-steering that defeats those baselines. We reproduce this against a more controlled baseline with Mancelle-400M. Our results show that robust control can be built into language models if we do so early and intentionally.

---


### 154. [Seeing Is Not Reaching: Instruction Shortcuts Override Visual Grounding in Vision-Language-Action Models](https://arxiv.org/abs/2611.32206)

**<font color=#1a73e8>作者：</font>** Qing Zhang, Xuesong Li, Zhaoyuan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action models (VLAs) are expected to inherit visual grounding from vision-language models, yet often reach for an object's training location after it has been moved. Across six VLAs, we identify two shortcuts: a scene shortcut, where the arm follows the scene's original task despite a new instruction, and an instruction shortcut, where the instruction retrieves the requested object's training location. In $\pi_{0.5}$, the instruction shortcut persists even though object-name attention follows the moved target. We call this Seeing Is Not Reaching. To determine whether this grounding is unused or overridden, we separately mask an image-mediated grounding pathway and a direct instruction-to-action pathway. Masking the grounding pathway eliminates reaches to moved targets, whereas masking the direct pathway increases them. Thus, grounding already guides action but is often overridden by the instruction shortcut, which acts through the direct pathway. We introduce Pathway-Separated Guidance (PSG), which amplifies grounding and suppresses the shortcut without training or external target locations. On LIBERO-PRO Object under Position perturbations, PSG raises the target-reaching rate from 22.0% to 52.6% and task success from 16.6% to 40.8%, while largely preserving performance on the original tasks.

---


### 155. [XMind: Thinking Twice via Cross-Memory Reasoning for LLM-Based Autonomous Driving](https://arxiv.org/abs/2611.32209)

**<font color=#1a73e8>作者：</font>** Zuyi Guo, Xianjie Dai, Lei Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory-augmented large language model (LLM) driving agents can reuse past experience, yet previously learned corrections often fail to transfer when traffic conditions change. A key limitation is that existing memories mainly record observed outcomes, providing little evidence about alternative actions. We introduce XMind, a training-free framework that enables LLM-based driving to "Think Twice" through cross-memory reasoning. XMind integrates working memory of recent traffic states with episodic memory of critical risk events. The agent first makes an initial decision from the current context and then cross-checks it against retrieved historical experience. If a conflict arises, it makes a second decision guided by the retrieved evidence. To construct reliable episodic memory, XMind evaluates alternative actions through counterfactual rollouts under perturbed traffic conditions and stores the verified outcomes as structured risk capsules. These capsules are retrieved by jointly matching spatial risk patterns and scenario semantics. Across closed-loop highway simulations, XMind achieves success rates of 83.3-93.3%, exceeding the strong baseline by 6.6 percentage points on average. Evaluation on K-Risk further demonstrates lower decision risk on unseen real-world high-risk interactions. Ablation studies confirm the complementary benefits of working memory, risk-text retrieval, and counterfactual verification. Code is available at this https URL

---


### 156. [NativeDrive: Native Multimodal Foundations for Autonomous Driving](https://arxiv.org/abs/2611.32216)

**<font color=#1a73e8>作者：</font>** Zehua Fan, Qi Jiang, Wei Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving requires semantic understanding and fine-grained scene perception for precise action prediction. Vision-language-action models (VLAs) inherit semantic priors, but low-dimensional action labels provide limited structural supervision. Some studies extend VLAs with visual generation tasks or adopt video-based world-action models (WAMs), but both approaches introduce appearance-reconstruction overhead, which is less relevant to planning. Native multimodal models offer an alternative to unify understanding and generation within one backbone. On this basis, we propose NativeDrive, a native encoder-free multimodal driving framework adapting the unified backbone for policy learning and introduce a dense supervision task tailored to driving. The Native Action Interface reuses the understanding expert's token-prediction interface for the discrete policy and adapts the generation expert for continuous policy. Driving Semantic Editing reuses the generation expert's editing capability for dense scene-structure supervision during training, while inference runs only the selected planning policy. NativeDrive achieves competitive planning performance among unified understanding-and-generation models on NAVSIM v1 and v2, with ablations validating its components' effectiveness. Code will be released.

---


### 157. [Relational Bottleneck Models](https://arxiv.org/abs/2611.32227)

**<font color=#1a73e8>作者：</font>** Shin'ya Yamaguchi, Kosuke Nishida  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Achieving both interpretable and high-performance inference is a key challenge in deep learning. While Concept Bottleneck Models (CBMs) provide inherent interpretability, they are constrained by task-specific training and rely on isolated visual concepts that fail to capture higher-order visual semantic relationships. Conversely, Large Vision Language Models (LVLMs) demonstrate zero-shot capabilities through Chain-of-Thought (CoT) reasoning. However, standard CoT lacks a strict causal dependency between the generated rationale and the final output, compromising faithfulness. To bridge this gap, we propose Relational Bottleneck Models (RBMs), a novel training-free framework that transforms any off-the-shelf LVLMs into inherently interpretable models in a plug-and-play manner. RBMs consist of two stages: (i) Structured Rationale Generation (SRG), which explicitly models semantic interactions between visual concepts as subject-predicate-object triplets, and (ii) Rationale-Grounded Decoding (RGD), which enforces a strict causal dependency between the rationales and the final output. RGD aggregates rationale-conditional next-token distributions via an importance-weighted product-of-experts strategy, strictly excluding the image inputs from the decoding context. Extensive zero-shot evaluations across diverse benchmarks and LVLM backbones demonstrate that RBMs achieve superior interpretability while improving task performance over CBM baselines, entirely without task-specific fine-tuning.

---


### 158. [SkillCore: Internalizing Generalizable Skills via Scaffolding-Removed Fine-Tuning](https://arxiv.org/abs/2611.32246)

**<font color=#1a73e8>作者：</font>** Yi Liu, Changqing Ai, Peijie Dong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Runtime skills can improve agents' problem-solving capabilities by providing procedural guidance for tasks such as code review and debugging. However, these benefits reach only a minority of users, as most do not proactively invoke skills in practice. We argue that such generalizable procedures should become part of the model's capabilities rather than remain optional external add-ons, making them directly available without explicit skill loading. To this end, we present SkillCore, a data pipeline and supervised fine-tuning recipe for internalizing generalizable skills. We transform real agent trajectories by removing skill-loading scaffolding while preserving the task context and subsequent agent actions, thereby supervising direct execution without external skill content. To preserve access to task-specific skills that provide genuinely external information, we mix these scaffold-removed trajectories with a small proportion of skill-native trajectories that preserve supervision for skill invocation. On a held-out skill-free evaluation, SkillCore improves task completion quality over the base Qwen3-8B and Qwen2.5-72B models by 54.4% and 24.8%, respectively, while preserving task-specific skill invocation on a separate probe and general coding performance on SWE-bench Verified.

---


### 159. [CaveBench: Benchmarking Abductive Physical Reasoning from Internal Observations](https://arxiv.org/abs/2611.32251)

**<font color=#1a73e8>作者：</font>** Guanxin Lin, Chen Yang, Shenxiang Zeng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are advancing in physical reasoning, but whether they can understand external physical drivers from internal observations remains an open question. Existing benchmarks have not specifically targeted this setting. To this end, we introduce CaveBench, a benchmark for abductive physical reasoning from internal observations. Models receive apparatus descriptions and internal images while the external controls remain hidden, and must infer the operations responsible for the observed responses. CaveBench spans 20 apparatus scenes in five physical domains and contains 10,200 simulated episodes, split into 9,000 training, 1,000 validation, and 200 test episodes. Questions span one to six events and require the complete control set at every event, testing whether an explanation accounts for the entire process. Synchronized observations and control records provide the inputs and reference answers. Evaluating 27 VLM configurations yields six-event exact-match accuracies of 68.0% for the strongest closed-source model and 12.5% for the strongest open-weight model. Seven adaptation baselines show that single-event gains need not improve complete sequences. Error analysis identifies failures in visual identification, physical inference, evidence integration, and action composition, specifying where current models struggle to connect internal phenomena with their external causes.

---


### 160. [Unjamming Deferrals: Supporting Students Through JAMN Bot, a Mobile RAG-Grounded Policy Assistant](https://arxiv.org/abs/2611.32266)

**<font color=#1a73e8>作者：</font>** Mark Farinas, Alesandra Garcia, Maria Reyes 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In some educational institutions, workflows such as the exam deferral process can be slow, inconvenient, and inconsistent, which creates the need to implement novel digital systems. This paper presents Schedulater, a mobile app for managing university exam deferrals. JAMN Bot is a Large Language Model (LLM)-powered chatbot integrated into Schedulater that provides context-aware support to help users understand the deferral process. The system features a Retrieval-Augmented Generation (RAG) pipeline using Ollama (Llama 3.2 3B) for self-hosted inference which enables policy-grounded responses without sacrificing privacy. We evaluate the system using a 43-item benchmark spanning Exam Deferral, Privacy, Scheduling, Cross-Policy, and Adversarial & Out-of-Scope questions, and report inter-rater agreement among our human evaluators alongside retrieval hit-rate metrics. Subsequently, we utilize an LLM-as-a-judge approach with GPT-5.4, revealing slight-to-moderate alignment with our raters that improves with answer quality, and check the ranking against a panel including Gemini 3.5 Flash and Qwen3.5 397B. The results of our study display trade-offs between open-weight and frontier models, as well as LLM-human evaluation alignment with answer quality. Schedulater demonstrates the feasibility of integrating lightweight LLMs into university administrative workflows with structured retrieval.

---


### 161. [Pando: Noise-Coupled Parallel Draft Trees for Efficient Edge Speculative Decoding](https://arxiv.org/abs/2611.32269)

**<font color=#1a73e8>作者：</font>** Joren Dumoulin, Hyoukjun Kwon, Subhankar Pal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) decoding emits one token per forward pass, reloading the full model each time, so LLM inference on edge devices is memory-bound while the compute units sit idle. Speculative decoding puts that idle compute to work by verifying several drafted tokens in a single pass. State-of-the-art parallel drafters such as DFlash and DSpark propose an entire block of draft tokens in one forward pass, which makes drafting compute-efficient. However, they are deployed with draft chains whose length is capped by the block size they are trained for, leaving most of the computational budget for verification unused.
To tackle this problem, we propose Pando, which builds dynamic draft trees on top of a parallel drafter and thereby removes this cap. Pando employs noise-coupled pruning, which draws the target model's sampling noise before drafting and ranks candidate branches under that noise, so the tree retains the branches the target will actually sample. Noise coupling is lossless and requires no retraining or additional model pass, yet increases acceptance length by up to $8.4\%$ on Qwen3-8B. To optimize and evaluate Pando configurations across hardware, we normalize an operator-level roofline to AR decoding, reducing every platform to its ridge point. On a representative edge device, a 16-node Pando tree attains $5.3\times$ speedup and $4.2\times$ energy reduction over AR decoding: $25\%$ faster than DSpark's released chain, and $27\%$ faster and $72\%$ more energy-efficient than an EAGLE-3 tree. The best configurations remain memory-bound on every edge device we model, so added compute capacity does not reduce their latency.

---


### 162. [StreamCoach: Proactive Sports Coaching via Continuous Visual Reasoning](https://arxiv.org/abs/2611.32281)

**<font color=#1a73e8>作者：</font>** Xiaoye Liang, Yiming Huang, Jialu Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In fitness and sports training, timely action quality assessment (AQA) is essential for learners to identify and correct technical errors during movement execution. However, most AQA methods assess completed performances, limiting their ability to provide timely feedback. Streaming methods alleviate this latency, but limited reasoning hinders their use of subtle movement cues and sport-specific knowledge. Moreover, their fragmented feedback focuses on one body part at a time, overlooking movement details of other body parts and transitions between action phases. To address these limitations, we propose StreamCoach, a streaming AQA framework under the OnCueCoaching paradigm that couples continuous chain-of-thought (CoT) reasoning with proactive, evidence-gated coaching. Technique-Aware Reasoning tracks body-part movements and action-phase transitions against sport-specific criteria, while Holistic Coaching integrates accumulated evidence to deliver timely, comprehensive feedback on strengths and technical errors. To support training and benchmarking, we construct EE4D-Stream from 1,213 sports video sequences in Ego-Exo4D through LLM-assisted reannotation and manual review of selected claims, pairing dense CoT annotations with evidence-gated speech content. Building on this dataset, we train StreamCoach using Temporal-Semantic Alignment Reinforcement Learning to jointly optimize feedback timing and content. We benchmark 11 offline and streaming baselines on EE4D-Stream, including three proprietary models. StreamCoach achieves state-of-the-art results across intervention timing, action assessment, and coaching quality, surpassing both GPT-6.1 Sol and Claude Opus 5.5.

---


### 163. [SofaSpace: A Benchmark for Executable Visual Spatial Reasoning in Continuous Motion and Environment Construction](https://arxiv.org/abs/2611.32285)

**<font color=#1a73e8>作者：</font>** Ze Rong, Kun Shi, Zhedong Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A rigid body can fit at its start and goal yet collide with a wall as it moves between them. Inspired by the moving sofa problem, we introduce SofaSpace, a benchmark for visual spatial reasoning through continuous planar rigid-body transport and environment construction. SofaSpace contains 3,000 scenes organized around three challenges: geometric compatibility, nonlocal maneuver planning, and interactive and temporal coordination. Four task views ask models to plan a motion, reconstruct a layout, design an environment that meets transport requirements, or jointly generate a layout and a motion. A separate set of 534 SofaSpace-Hard tasks tests planning and judgment. A geometric verifier checks the entire body throughout each submitted motion. On static planning tasks, endpoint agreement and continuous validity differ substantially within the same submitted plans: Claude drops from 97.2% to 52.8%, DeepSeek from 100.0% to 30.6%, and Kimi from 97.2% to 29.4%, while the strongest configuration retains 98.3% full validity. Environment construction reveals a further gap. Of 295 feasible layouts generated by the strongest configuration, 181 satisfy all evaluated functional requirements; for Kimi, one of 172 does. These results show how executable checks distinguish endpoint agreement from valid motion and geometric feasibility from functional compliance.

---


### 164. [VC-OPD: Learning to See What Matters via Visual Cue On-Policy Self-Distillation](https://arxiv.org/abs/2611.32292)

**<font color=#1a73e8>作者：</font>** Qinxuan Wang, Zheyu Zhang, Yijing Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual On-Policy Distillation (OPD) commonly uses cropped or zoomed-in image regions as teacher-side privileged information to improve fine-grained perception in small Multimodal Large Language Models (MLLMs). However, local pixel-level cues are insufficient for complex visual reasoning that requires global structure, spatial relationships, and high-level semantics. We propose Visual Cue On-Policy Self-Distillation (VC-OPD), which extends teacher-side privileged information beyond local image regions to question-conditioned visual cues. Advanced MLLMs generate cues capturing key visual details, structural relationships, and semantic evidence needed to answer each question. A multi-stage quality filtering process selects reliable cues, which are provided only to the teacher during training. This enables informative token-level supervision along student-generated trajectories, helping the student learn to identify and reason over critical evidence directly from the original image. No additional information is required at inference time. Since advanced MLLMs are used only for visual cue generation, VC-OPD is compatible with both open-weight and proprietary black-box models. Experiments on STEM and general visual reasoning benchmarks show consistent improvements across model scales over reinforcement learning and on-policy distillation baselines. Notably, a 4B model trained with VC-OPD outperforms many baselines with 8B or more parameters, demonstrating effective capability transfer through question-conditioned visual cues.

---


### 165. [DAiSy: Online Data Selection by Adaptive Utility Estimation for LLM Pretraining](https://arxiv.org/abs/2611.32294)

**<font color=#1a73e8>作者：</font>** Simin Fan, Martin Jaggi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-aware online data selection prioritizes the training documents that contribute the most given the model's current state. Existing online selectors rank candidates upon gradient-based data utility scores, which requires the full forward-backward pass of the main model on every candidate document. Scoring each document therefore pays as much as training on it, yet only a small fraction is used for the real model update. We introduce DAiSy, a lightweight linear auxiliary model that learns to predict data utility scores from frozen document embeddings, which eliminates the computation overhead and infrastructure burdens. The linear estimator is updated alongside the main language model, fitting to the exact gradient-based utility scores obtained from the backward pass of regular training steps. Consequently, scoring a candidate requires only a linear transformation, bypassing the costly gradient-alignment computation. We demonstrate its effectiveness and efficiency for LLM pretraining in English and multilingual scenarios, with various steering target designs. The improvements from DAiSy can consistently survive the instruction-tuning phase.

---


### 166. [MaskedVGGT: Masked Multi-View Transformers Are Scalable 3D Learners](https://arxiv.org/abs/2611.32297)

**<font color=#1a73e8>作者：</font>** Zichen Zou, Xiaosong Jia, Wen-Ming Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view feed-forward models show strong scalability, but their reliance on costly geometric annotations limits data scaling. Existing 3D self-supervised approaches reduce this reliance through cross-view completion (e.g., CroCo, MuM, Muskie) or novel-view synthesis (e.g., RayZer, E-RayZer), typically learning image representations and cross-view interactions jointly. We argue that learning single image representations from scratch is unnecessary for 3D pretraining methods, as doing so fails to benefit from the continuing advances in 2D foundation models (e.g., DINO, CLIP, frontier VLMs). We introduce MaskedVGGT, which freezes a strong pretrained 2D encoder and pretrains only an added, randomly initialized multi-view transformer, focusing on learning interactions across views. MaskedVGGT pretrains the multi-view transformer through masked self-distillation without annotations: a student predicts targets at masked locations based on complete anchor views and heavily masked remaining views, while an exponential-moving-average teacher provides prediction targets based on unmasked inputs. In experiments across model sizes up to 1B parameters, MaskedVGGT pretraining followed by fine-tuning outperforms single-stage supervised VGGT-$\Omega$ training with the same training data, model architecture, and total number of optimization updates. MaskedVGGT also outperforms E-RayZer, CroCo, MuM, and Muskie, providing evidence for the effectiveness of building multi-view pretraining on strong 2D representations. Finally, extending pretraining with additional unlabeled videos further improves generalization, and the learned representations transfer to diverse downstream tasks. These results demonstrate an effective division of learning: reuse strong image representations from 2D pretraining and learn cross-view interactions from unlabeled multi-view data without relying on geometric annotations.

---


### 167. [Towards a Multimodal Aesthetic Agent for Photographic Reference Grading](https://arxiv.org/abs/2611.32299)

**<font color=#1a73e8>作者：</font>** Kunjie Lin, Haitao Zhang, Bosheng Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reference-guided photographic color grading helps users realize their aesthetic intent by selectively drawing on the color and tonal characteristics of a reference photograph. Doing so requires understanding which characteristics users wish to adopt and translating these preferences into controllable edits. However, image-only reference methods align overall appearance without instruction-grounded selection, while pixel-space generative editors typically produce flattened images without editable parameters, limiting subsequent refinement. To address these challenges, we introduce JarvisAura, a multimodal aesthetic agent that formulates photographic color grading as structured decision-making in an editable parameter space. JarvisAura offers three key advantages: (1) an aesthetic agent paradigm that integrates visual attribute perception, strategy-level reasoning, and parameterized execution for interpretable and controllable photographic color grading; (2) a unified reasoning-to-execution pipeline that connects aesthetic planning with backend rendering and editable parameter refinement; and (3) a three-stage training strategy comprising Parameter-Grounded Continual Pre-Training for parameter-appearance grounding, Reference-Grounded Supervised Fine-Tuning for reference-guided reasoning and parameter decisions, and Reference-Aligned Group Relative Policy Optimization for rendered-outcome refinement with multidimensional rewards and dynamic data derivation. On Ref-Bench, JarvisAura achieves the best scores among methods with results across reported automatic metrics and a 74% human-rated task-success rate, exceeding GPT-Image-2.5 by 9 percentage points.

---


### 168. [Query-Guided Visual Minimization for Selective Disclosure to Cloud VLMs](https://arxiv.org/abs/2611.32302)

**<font color=#1a73e8>作者：</font>** Pedram Zaree, Kleomenis Katevas, Vandana Rajan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cloud-hosted vision-language models (VLMs) require sending images beyond the user's local trust boundary, potentially exposing sensitive information the query does not need. We study query-guided visual minimization: a trusted local transformation preserves query-relevant visual content and reduces unnecessary disclosure before transmission. Unlike query-agnostic anonymization, it preserves the same sensitive content when the query requires it and suppresses it otherwise. We introduce QGVM, a framework that combines query grounding with an independent sensitive-item inventory, determines disclosure necessity at the type, instance, and text-content levels, and renders a minimized image for a black-box downstream VLM. We evaluate QGVM on complementary benchmarks measuring task utility, directly recoverable sensitive information, and inferential geolocation leakage. With OpenAI GPT-6.1 Sol, QGVM achieves 85.3% DoxBench answer correctness versus 77.5% for PGP, while a separately prompted Sol geolocation attacker succeeds within 1 km on 5.8% of QGVM images versus 25.7% of unprotected images. On Scene-Privacy, QGVM reduces face re-identification from 27.7% (PGP) to 4.5%. On held-out BIV-Priv-Seg, unnecessary private-text recovery falls from 33.9% (PGP) to 15.3%. To verify that disclosure is query-dependent, we evaluate paired queries that either require or do not require the same sensitive information. QGVM achieves 69.6% correct disclosure switching, compared with 29.1% for grounding-only cropping. These findings highlight the value of distinguishing visual relevance from disclosure necessity, while revealing the privacy-utility trade-offs of selective visual disclosure.

---


### 169. [ASTERISM: Do Multimodal LLMs Actually Look at All the Images?](https://arxiv.org/abs/2611.32316)

**<font color=#1a73e8>作者：</font>** Chanseul Cho, Dongwoo Kim, Noori Bae 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-image benchmarks aim to test whether a multimodal large language model (MLLM) combines evidence across images, but many of their items can be answered from a single image. Across about 33k items from 19 public benchmarks, our audit and a two-stage single-image filter find that one image or the question alone settles 24.2% of them. On these items, MLLMs recover from one image a median 78% of the accuracy that all images add over the text alone, so these items reward answering from one image, which we call the single-image shortcut. MLLMs take this shortcut even on items where one image is not enough. On such items, most of their wrong answers repeat an answer they give from one image, at a rate well above chance. We build ASTERISM, to our knowledge the largest audited multi-image benchmark, from these 19 benchmarks by keeping their items that need more than one image. Its 18.7k items, 2.0k of them corrected or rewritten, share one format, one scorer and seven task categories. We also release ASTERISM-Train with 49k training items and ASTERISM-Lite, a hard subset whose items we manually verify one by one. On ASTERISM-Lite, the strongest proprietary MLLM scores 68%. Reinforcement learning with verifiable rewards (RLVR), now common in MLLM post-training, rewards the shortcut as well, because a correct answer read off one image earns as much reward as one that combines images. In line with this, existing RLVR objectives add little to the ASTERISM score. To stop rewarding the shortcut in training as ASTERISM does in evaluation, we propose cross-image credit assignment (CICA), an extension of RLVR that moves the credit toward the tokens that need more than one image. On three open-source MLLMs, CICA raises the ASTERISM score by 2.6 to 6.0 points, more than twice the gain of each general and vision-specific RL objective trained on the same data.

---


### 170. [When Exact Token Importance Is Not Enough: Limits of Top-K Selection in LLM Attention](https://arxiv.org/abs/2611.32324)

**<font color=#1a73e8>作者：</font>** Irmaan Mirzanejad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context language models often retain only a limited set of past token positions for an attention query. A common strategy scores positions individually and keeps the highest-ranked K. Yet attention weights are renormalized over the chosen set: two individually important positions need not form the best pair. We ask whether independent ranking suffices even when each importance score measures the exact downstream change in next-token predictions caused by deleting that position alone. It does not. A four-position construction makes the ranked pair incur 133.2 times the Kullback-Leibler (KL) divergence of the optimal pair, and a parametric family proves that this multiplicative gap is unbounded. An exact exchange identity and preference reversals for every K >= 2 explain the interaction. In exhaustive frozen-model audits of SmolLM2, Gemma, and Qwen, exact-singleton Top-4 leaves at least 10% relative improvement within a fully enumerated 24-position candidate pool in 55/60, 49/60, and 60/60 cases, respectively. SwapCert, a same-budget one-swap audit, detects 157/164 such cases and returns directly checkable improving supports. A KL-margin certificate relates support fidelity to next-token stability; larger-budget, multi-layer cached-decoding experiments measure predictive fidelity at K = 128 and 256. These results establish joint support quality as an essential object of analysis for sparse attention and motivate downstream-aware support selection under inference constraints.

---


### 171. [DiCT: Teaching X-ray Vision-Language Models to Reason via Imagining CT](https://arxiv.org/abs/2611.32344)

**<font color=#1a73e8>作者：</font>** Zhenghao Lu, Xiaotian Zhang, Songtao Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diagnosing with X-rays often requires reasoning about the 3D locations of abnormalities and their spatial relationships to surrounding anatomical structures, yet such reasoning remains challenging due to the loss of spatial information in 2D projections. To address this challenge, we propose Dreaming in CT (DiCT), a three-stage progressive CT-to-X-ray reasoning transfer framework that leverages a CT vision-language model (VLM) to guide an X-ray VLM. Through this CT-guided transfer, the student acquires CT-informed 3D reasoning capabilities, enabling it to reason directly from 2D X-rays without explicit CT reconstruction at inference time. The framework begins with instruct the dreamer, which equips the X-ray student with initial CT-oriented reasoning capabilities and establishes a structured interface that distinguishes X-ray observations from CT imagination. Building on this structure, visualize the dream introduces CT-guided on-policy distillation (OPD), where the CT teacher selectively guides the X-ray student's reasoning trajectories to transfer 3D anatomical knowledge. Finally, manifest the dream adapts the acquired reasoning capabilities from digitally reconstructed radiographs (DRRs) to real clinical X-rays. Experiments across two VLM backbones on 3D-RAD and ReXVQA demonstrate DiCT's effectiveness across radiological reasoning tasks, achieving a 1.66 percentage point improvement over a CT reconstruction-based baseline on 3D-RAD Abnormality Identification with 12.77$\times$ lower inference computation. Our code is available at this https URL.

---


### 172. [Beyond Hard Tokens: Predictive Memory for Multimodal Protein Generation](https://arxiv.org/abs/2611.32347)

**<font color=#1a73e8>作者：</font>** Xiaoliang Shi, Zichen Wang, Zhijian Wei 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal protein language models unify sequence and discrete structural tokens via iterative masked decoding, offering a promising paradigm for joint protein design. However, standard decoders rely on a memoryless mask reset at each iteration: only a sparse subset of newly committed hard tokens is carried forward, while all remaining unresolved sites are reset to an identical [MASK] embedding. In open-ended co-generation where neither modality provides a fixed external anchor, this stateless transition limits single-step refinement depth and deprives both tracks of stable cross-step soft anchors, leading to slow convergence or degenerative repetitive collapse. Observing that uncommitted predictions evolve with pronounced temporal coherence rather than erratic noise, we introduce Predictive Memory (PredMem), a training-free self-conditioning recurrence that carries these soft beliefs across steps. At each step, PredMem summarizes raw logits into a probability-weighted Top-$k$ expectation embedding at every residue and affinely interpolates it into eligible masked inputs on the next step at zero extra denoiser cost. Across DPLM-2, DPLM-2.1, and ESM3, PredMem raises unconditional sequence-structure co-generation success by 3.6, 17.7, and 48.7 percentage points, respectively, while improving the quality-diversity trade-off and suppressing repetitive mode collapse. Controlled diagnostics show that these gains stem primarily from early trajectory stabilization in unanchored cross-modal co-evolution rather than extra compute or simple entropy reduction, establishing PredMem as an efficient inference mechanism for multimodal discrete generation.

---


### 173. [LookAnything: A Foundation Model for Holistic Gaze Following](https://arxiv.org/abs/2611.32351)

**<font color=#1a73e8>作者：</font>** Jiayu Tang, Yuchen Zhou, Hongsheng Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human gaze provides a rich window into attention and intent, making its understanding essential for applications ranging from social signal analysis to human-robot interaction. Existing methods typically employ highly customized architectures relying on auxiliary inputs like head crops or depth maps, causing cascading errors and inference overhead. Trained on single domains and confined to isolated gaze following with heatmap outputs, they lack flexibility and generalization for diverse interactive scenarios. To bridge this gap, we present LookAnything, a foundation model that unifies diverse gaze-centric tasks for holistic gaze following. Benefiting from large-scale multi-task and cross-domain training, LookAnything flexibly adapts to various settings, generating diverse outputs (points, boxes, heatmaps, and language) and supporting broad gaze-centric localization, description, and reasoning. At its core, we introduce learnable gaze-prior queries to promote gaze-aware representation learning, eliminating the need for auxiliary external inputs. To facilitate this paradigm, we construct HoliGaze, a comprehensive corpus and benchmark comprising 311K question-answer pairs across 5 capability dimensions and 9 distinct tasks. Experiments demonstrate that LookAnything consistently outperforms 33 leading vision-language models on holistic gaze following, while remaining highly competitive with dedicated specialists across 5 conventional target detection benchmarks. Evaluation on unseen datasets and deployment on a real robot further validate its strong out-of-domain generalization and flexible adaptation in real-world scenarios.

---


### 174. [Protective-Design Pre-Emption in Child-Facing Generative AI](https://arxiv.org/abs/2611.32352)

**<font color=#1a73e8>作者：</font>** Verena Jasmin Hallitschke, Mahelie Dissanayake, Elisa Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI is adopted rapidly by children, yet unrestricted general-audience models dominate their usage. This paper presents the open problem of \emph{protective-design pre-emption}: Delayed market introduction, low access thresholds, utility gaps, habituation, and peer adoption foster unrestricted AI model lock-in, leading children to bypass child-centric platforms. With first signs of lower adoption of child-centric platforms, we argue that this shift may reinforce existing AI risks such as exposing children to deepened parasocial dependencies, skill erosion, and misinformation. To address this problem, we propose interdisciplinary research directions to quantify pre-emption, understand its socio-technical drivers, and develop interventions ensuring child-centric AI is actively adopted, not just available.

---


### 175. [The Control-Flow Tax: Specialized Decision Routing for LLM Agent Workflows](https://arxiv.org/abs/2611.32365)

**<font color=#1a73e8>作者：</font>** Zhikai Cheng, Shuanghu Wang, Li Jiang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent can spend almost as much deciding what to do as doing it. In our documentation workflow, control-flow routing accounts for 42.5% of baseline reference cost on the initial task. Lower token prices alone do not solve this control-flow tax: inexpensive general-purpose routers can trigger additional calls to the expensive generator. We evaluate a heterogeneous architecture in which Jev, a specialized System 1 decision model, controls finite actions while Sol generates documents. Across four software tasks, 480 valid runs comprise 470 completions and ten request-limit endpoints. Jev full routing achieves the lowest mean cost and elapsed time on every task, completing all 40 specialist-controlled runs along the shortest trajectory. On the initial task, mean cost falls by 49.6% (95% paired-bootstrap interval: 42.9% to 56.3%) and elapsed time by 33.2% (19.6% to 46.7%). Across three further tasks, cost reductions are 40.5% to 42.9% and concurrent elapsed-time reductions are 12.9% to 14.4%. Existence-only specialization saves just 1.8% on the initial task. Separately, Sol and Jev each select accepted actions on 100/100 reviewed retail states, with Jev using 97.88% less reference cost and 72.30% less mean request time. The results identify two requirements for efficient agent control: inexpensive decisions and trajectories that preserve those savings.

---


### 176. [Visual-State Graph Memory for Streaming Video Understanding](https://arxiv.org/abs/2611.32369)

**<font color=#1a73e8>作者：</font>** Ailar Mahdizadeh, Pritam Sarkar, Xiangteng He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In streaming video understanding, the evidence needed to answer a question may have already left the recent-frame window. Keeping all frames does not scale with video length, while dropping older frames limits the model's ability to reason about the past. We propose Visual-State Graph (VSG), a training-free memory that stores the state of a stream rather than the raw sequence of frames. VSG represents the stream as a graph of objects and their relations, together with a log of events; similar to a dynamically evolving scene graph. An object observed repeatedly is represented by one persistent node, with a timestamped history of how its state changes. To determine whether a newly mentioned object already exists in the graph, we compare the relations it takes part in with those of stored objects. We build this memory as the video arrives, before the questions are known. When a question arrives, we retrieve relevant objects and events alongside recent frames under a fixed input budget. Our evaluation spans four streaming-video benchmarks and seven open-source vision-language models ranging from 7B to 32B parameters. Under matched input budgets, VSG improves reasoning about the past while preserving real-time understanding.

---


### 177. [Can AI Design a Better nnU-Net? A Hypothesis-Driven Architecture Discovery Loop from Failures to Design Rules](https://arxiv.org/abs/2611.32384)

**<font color=#1a73e8>作者：</font>** Songtao Jiang, Yuan Wang, Fucheng Niu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Neural architecture search and LLM-driven evolution often reduce evaluation to a scalar fitness score, discarding failures that could explain why designs succeed or fail. We present a hypothesis-driven architecture discovery loop in which LLM agents diagnose structured error patterns, formulate falsifiable hypotheses, test counterfactual controls under a frozen nnU-Net pipeline, and distill validated mechanisms into executable trigger-to-action rules. Across eight search waves, the loop identifies two principles for 3D medical image segmentation. First, reallocating computation from high-resolution decoders to the mid-encoder preserves thin-anatomy boundaries while reducing cost. Second, support-confined region contrast addresses errors between nested anatomical compartments, with anatomy-dependent triggers selecting when the rule applies. These principles produce LeanNeXt (0.78 MACs and 0.92 training-step time relative to nnU-Net; +1.63 Dice points on four-fold KiTS23 cross-validation) and trigger-routed LeanNeXt+. The latter improves all 15 evaluated CT/MRI settings over nnU-Net and exceeds the 3.3 larger ResEnc-M on 12 of 15 benchmarks at 0.30 its parameter count. Relative to random sampling, one-shot LLM generation, and score-selected agent search, the loop shows how failure analysis can yield reusable design rules across modalities.

---


### 178. [Evolve to Learn: Gradient-aligned experience evolution for model self-improvement](https://arxiv.org/abs/2611.32390)

**<font color=#1a73e8>作者：</font>** Haoyuan Li, Gangyi Zhang, Dong Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving language models can continuously acquire useful experience through test-time interaction, reflection, and prompt optimization, yet turning such experience into model itself to ensure self improvement remains challenging. On-policy self-distillation (OPSD) provides a natural mechanism for internalizing test-time information into model parameters, yet it largely assumes that the gener- ated experience is worth learning. We show that this assumption does not always hold: experiences that improve test-time performance may provide limited or even harmful training signals. To better characterize which experience should be inter- nalized, we systematically analyze diverse mutated experiences across multiple tasks and reflection models, and find that gradient-based alignment is a more reli- able indicator of downstream distillation gains than immediate test-time improve- ment. Based on this finding, we propose E2L, a self-evolution framework that iteratively generates, evaluates, and distills experiences according to their esti- mated training utility. E2L closes the loop between experience generation and parameter learning, enabling agents to autonomously produce experience suitable for self-improvement.

---


### 179. [Verify then Steer: Progress Hallucination-Aware Recovery for Continuous Vision-and-Language Navigation](https://arxiv.org/abs/2611.32400)

**<font color=#1a73e8>作者：</font>** Jiewen Hou, Guanxiang Qi, Meina Kan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-Language Navigation (VLN) requires an agent to follow language instructions to reach a target in an unseen 3D environment. However, existing methods still struggle to recover from route deviations at test time. We investigate this limitation through the lens of instruction progress, and trace it to a phenomenon we term progress hallucination: agents misinterpret off-route observations as evidence of task progress, causing their internal instruction progress to advance beyond the actual task stage and hindering recovery based on earlier sub-instructions. To address this failure mode, we propose PHAR (Progress Hallucination-Aware Recovery), a test-time recovery framework following a verify-then-steer paradigm. The verifier examines residual-stream representations of the Vision-Language Model (VLM) to identify mismatch of cross-modal evidence along the trajectories, and uses split conformal calibration to control false alarms. When an alarm is raised, the steering module uses a contextual bandit to adaptively select the rewind extent of instruction progress for online recovery. Through extensive experiments on R2R-CE and RxR-CE, our framework enhances the reliability of multiple state-of-the-art vision-language navigation methods at test time.

---


### 180. [Every Edit Its Own Budget: Per-Instruction Token Freezing for Training-Free Acceleration of Multi-Edit Image Editing](https://arxiv.org/abs/2611.32407)

**<font color=#1a73e8>作者：</font>** Jyotirmoy Nath, Neeraj Kumar, Brejesh Lall  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accelerating instruction-based image editing when one instruction requests several edits is challenging. Many training-free accelerators for flow-matching image editors skip tokens whose prediction has stopped changing, but decide this with a single threshold for the whole image. With several edits, such a threshold, tuned for speed, freezes small and slowly settling edits first, and requested edits disappear. We propose TIDE (Training-free Instruction-aware Drift-based Editing), which gives every instruction part its own compute budget. First, TIDE finds the region of each part in the editor's own attention by unbalanced optimal transport, without masks or external models. Second, it freezes a token once its drift is small relative to its own part and moves it along the straight path to its endpoint estimate. Third, a sparse engine computes only the remaining tokens. We prove that part-agnostic rules cannot guarantee per-part error budgets, characterize the optimal per-part threshold policy up to one tie class per part, and derive when our rule attains it. On FLUX.2 Klein, one global threshold breaks at least one edit's budget in 89% of MICE-Bench images, and TIDE drops up to 77% fewer edits at matched or higher speed (48% on MICE-Bench), a gap human raters confirm. On the many-step Klein Base, TIDE is the fastest compared method on six benchmarks (4.81-4.89x) and needs 5.3x fewer TFLOPs than vanilla, the largest saving we measure. With the same settings, it is also the fastest compared method on Qwen-Image-Edit-2511, a second model family (3.46-3.52x), and drops the fewest edits on all six benchmarks. Code will be made publicly available.

---


### 181. [On the Importance of Hidden-State Refinement in Masked Diffusion Language Models](https://arxiv.org/abs/2611.32416)

**<font color=#1a73e8>作者：</font>** Linhao Zhong, Bozhen Fang, Xuehao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (MDLMs) generate text by iteratively denoising masked or corrupted token sequences, allowing token predictions to condition on bidirectional context and update multiple positions in parallel. While each denoising step produces a rich layer-wise hidden-state trajectory, prior work typically focuses only on token-level information and discards these continuous hidden states, leaving their refinement dynamics underexplored. In this work, we analyze hidden-state dynamics in MDLMs and find clear evidence of layer-wise and cross-step refinement: smooth evolution across adjacent layers, greater predictive power in deeper layers, gradual degradation under transformer block removal, and strong final-state alignment across consecutive denoising steps. Motivated by these observations, we propose Cross-Step Recurrent Refinement (CSRR), a mechanism that carries hidden-state information across denoising steps to enhance generation. Extensive experiments show that CSRR improves text generation quality, highlighting the critical role of continuous hidden-state refinement in MDLMs. Project page: this https URL

---


### 182. [Factorized Context Attention: From Emulated to Native Grid Probing](https://arxiv.org/abs/2611.32423)

**<font color=#1a73e8>作者：</font>** Mohamed Eltahir, Manar Eyad, Yara Alzahrani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Models read a book, an hour of video, or an image in one forward pass. As the context grows, this pass slows down, loses accuracy, and stops at the context window. Sparse attention is efficient, but keeps the other two limitations. Grid probing, a recent training-free method, recovers the accuracy and extends the reach by asking a frozen model the same question about short local and strided spans of the input, but every question repeats the whole computation, since each span is encoded again. Our insight is that grid probing is emulated attention, an attention pattern reproduced from outside the model through prompts, since each probe only restricts which part of the input the question can see. We introduce Factorized Context Attention (FCA), a training-free block-sparse attention that runs the same pattern natively, as the attention of the model itself. FCA encodes the input once into a KV cache, reads all spans as masked sequences in one batched forward, and uses a stair position schedule to keep every span inside the trained position range. Across long video understanding, long-context text inference and image grounding, FCA matches the accuracy and the reach of grid probing at a fraction of its cost. It gains about 10 points over the single pass on long video and 9 to 14 points on long novels, finds needles in videos of over a thousand frames and in texts four times the length of the window, and answers a later question about the same input in as little as a tenth of the time of grid probing. Native attention thus keeps what emulated attention gains without its cost, all with existing frozen language and vision-language models.

---


### 183. [A Mesh to Remember: Persistent Appearance for Interactive Video Worlds](https://arxiv.org/abs/2611.32445)

**<font color=#1a73e8>作者：</font>** Joonghyuk Shin, Alex Trevithick, Katarína Tóthová 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video world models synthesize photorealistic observations in response to user actions but struggle to remain consistent over long interactions. Coding agents and text-to-3D models instead generate explicit 3D worlds whose geometry and state persist by construction, but whose appearance falls far short of photorealism. Recent methods combine the strengths of both by rendering such worlds into coarse proxies that guide a video model. However, since these proxies only specify where things are, the renderer must invent what they look like as the world is explored, and anything it forgets is reinvented when a surface reappears. Our key insight is that a mesh identifies which surface each pixel shows, across frames and views, even as objects move, allowing it to serve as an address for what the renderer generates. We propose M2R (Mesh to Remember), a few-step causal video renderer that stores its own features on the surfaces they depict, in each object's frame, and retrieves them by rasterizing the mesh whenever those surfaces come back into view. Appearance thus travels with objects wherever they move, persists across revisits, and is shared by every agent that observes it, while memory grows with the surfaces seen instead of the number of frames. Trained only on synthetic data, M2R transfers zero-shot to real indoor scans and to worlds authored by coding agents. It outperforms state-of-the-art methods in consistency across static, dynamic, and multi-agent benchmarks, more than doubling object permanence and nearly doubling cross-agent consistency, while rendering 720p video in real time (40 FPS).

---


### 184. [When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents When Ink Meets Pixel: Intent-Aware OCR with VLMs for Human-Corrected Financial Documents](https://arxiv.org/abs/2611.32446)

**<font color=#1a73e8>作者：</font>** Akshata A Bhat, Daman Deep Singh, Niyati Chhaya  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human annotations on documents (such as arrows, carets, strikethroughs, and insertions) express corrective intent yet existing OCR and document understanding systems treat these marks as visual noise rather than semantic edit operations. We introduce intent-aware OCR, the task of generating corrected transcriptions by jointly reasoning over original document content and visual intent cues (handwritten or digital) that convey edit intent. To support this setting, we present DocIntent, a multimodal dataset of 1,600 financial documents with over 5,700 annotated visual intent cues, each paired with layout-aware, intent-resolved OCR targets. We further introduce IntentBench, a 216-document benchmark designed to evaluate model robustness under diverse real-world annotation conditions. Leveraging DocIntent, we fine-tune DocIntentOCR, a suite of 3B and 7B parameter vision-language models, under direct intent supervision on corrected transcriptions. On IntentBench, the fine-tuned 3B and 7B models achieve F1-scores of 0.81 and 0.83, respectively, substantially outperforming commercial closed-source (e.g., GPT-4.1 (0.626)), and open-source models (e.g., LLaMA-3.2-Vision-90B (0.50)) demonstrating that intent-aware supervision enables compact domain-specific models to outperform substantially larger general-purpose systems on this task. This work establishes intent-aware OCR as a novel human-in-the-loop document understanding task and provides foundational resources (dataset, benchmark, models) to advance research in interactive document processing.

---


### 185. [The Teacher Is Already Inside: Self-Distilling Looped Language Models Beyond Their Last Loop](https://arxiv.org/abs/2611.32452)

**<font color=#1a73e8>作者：</font>** Linghua Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped language models apply one shared transformer stack several times per token, and every loop is readable through the shared language-model head. Post-training them is hard. Reward-only reinforcement learning needs a verifier and learns from one sparse signal per response; spreading the reward over loops collapses the entropy of every loop; and cross-loop self-distillation, as in LoopOPD, can only teach intermediate loops, because the last loop cannot learn from its own frozen copy: the loss is zero at initialisation. We observe that a looped model already contains a policy that decodes better than its last loop: the next-token distribution extrapolated from the first loop through the last. ELPSD (Extrapolated-Loop Policy Self-Distillation) turns this distribution into a self-distillation target: a frozen copy of the model computes it, and the model's own last loop is distilled towards it on its own rollouts, using the exact reverse KL at every visited prefix. Teacher and student are the same model, so ELPSD needs no reward, no external teacher and no privileged context, and it leaves rollouts and decoding unchanged. We show that the objective pulls the last loop towards the base model's last loop with weight 1+w and away from the base model's first loop with weight w, and that the teacher must stay frozen, since an idealised teacher recomputed from the current model extrapolates without bound. We evaluate ELPSD on Ouro-1.4B-Thinking across five math benchmarks against the base model, GRPO, RLTT and OPSD. Without any reward, ELPSD raises the average avg@8 from 61.15 to 63.69 and is the best method on all five benchmarks, ahead of GRPO (62.32), which uses a verifier, and the self-distillation method OPSD (61.77), which needs reference solutions.

---


### 186. [Phoneme-identity depth profiles do not reliably predict LoRA placement for dysarthric ASR](https://arxiv.org/abs/2611.32455)

**<font color=#1a73e8>作者：</font>** Bernard Muller, LaVonne Roberts  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parameter-efficient adaptation of a speech foundation model to dysarthric speech requires a rarely justified choice: which encoder layers to adapt. A recently proposed strategy is to probe the encoder, find where phonetic information becomes most decodable, and put the adapters there. We test that inference across two ASR models (Qwen3-ASR, Whisper-small) and two dysarthric corpora (Mandarin CDSD, English UASpeech), holding recipe and seed discipline constant.
The inference fails. Measured under one pipeline rather than inherited from published figures, all four phoneme-error curves minimise between 83% and 92% of relative depth, each model's minimising layer moving no further between corpora than between probe seeds. The best adaptation band is not similarly constant: none of three natural mappings from the curve to a band -- steepest improvement, lowest band-mean error, or knee location -- recovers the best tested configuration. We do not claim no statistic of the curve could work, only that these three do not.
Placement still matters, but is model- and corpus-specific. On CDSD the models disagree -- Qwen3-ASR prefers its upper third (29.88% CER, three-seed mean), Whisper-small all-block LoRA (53.56%) -- while on UASpeech neither favours the upper band. At three seeds, upper-versus-all is resolved (-1.31 pp, CI [-2.16, -0.25]) but upper-versus-middle is not (-0.83 pp, CI [-2.06, +1.86]). The two models' preferences differ as a directly tested interaction (-4.71 pp, CI [-6.17, -2.89]); we designate this the primary claim, and record that the designation was made post hoc. On Qwen3-ASR x UASpeech, adapting near the input is reliably worse than not adapting at all (+9.90 pp CER). We recommend choosing the band by a short adaptation sweep on the model and corpus in hand, not by reading it off a probe.

---


### 187. [ViDM: Efficient and Order-Robust Parallel Visual Decision Making](https://arxiv.org/abs/2611.32461)

**<font color=#1a73e8>作者：</font>** Xudong Tan, Peng Ye, Chenyu Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual decision-making demands accurate judgments and timely responses. Yet for multiple questions sharing the same visual input, autoregressive multimodal large language models generate answers token by token, accumulating sequential decoding costs as question count grows and delaying completion of the decision set. Their predictions can also vary with question order. We introduce ViDM, which transforms multi-question visual inference into parallel decisions in a single forward pass, improving both accuracy and inference efficiency. ViDM organizes shared visual context, multiple questions, and question-specific decision slots into one sequence, reusing the native language-model head to produce all answer distributions simultaneously. A Decision-Query Mask aligns each decision query's direct attention with shared context and its corresponding question, while case-balanced multi-order training strengthens robustness to question reordering. Across nine benchmarks spanning image, multi-image, and video tasks, ViDM improves Qwen3.5-4B's average accuracy from 73.49% to 77.55% while achieving 8.4x the baseline's average end-to-end throughput. On GQA, where each evaluated image has 11.4 questions on average, the end-to-end speedup reaches 20.3x. ViDM also improves mean and worst-order accuracy while reducing order-induced variation across multiple benchmarks, with further validation on LLaVA-OneVision-7B and InternVL3.5-4B.

---


### 188. [MAGPIE: Agentic Multi-Reference Image Generation via Executable Scene Construction](https://arxiv.org/abs/2611.32462)

**<font color=#1a73e8>作者：</font>** Yifan Dai, Daili Hua, Bohan Zeng 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-reference image generation requires a model to preserve the appearance of selected subjects while arranging them according to an instruction. Despite recent progress in reference-based generation and compositional control, reliably organizing selected subjects into the intended scene remains challenging. Although existing methods provide various forms of compositional guidance, the planned relationships are not always explicitly instantiated for inspection and refinement before image synthesis. To address this limitation, we introduce MAGPIE, which represents the intended composition as a simplified 3D scene defined by an executable Blender program. A coding agent links each scene instance to its reference, checks the geometry and rendered view against the instruction, and revises the program to correct discrepancies. The final proxy rendering serves as a visual plan for the image generator. Using MAGPIE-Instruct-3K, we train the generator to follow this plan while drawing each subject's appearance from its reference. MAGPIE improves both Qwen and FLUX on DreamOmni2 and SconeEval. With FLUX, it improves overall success on DreamOmni2 by 28.21 percentage points over the original backbone and achieves the highest overall score among the models evaluated on SconeEval.

---


### 189. [Describe, Don't Ask: Caption-Driven On-Policy Distillation for Fine-Grained Visual Perception](https://arxiv.org/abs/2611.32463)

**<font color=#1a73e8>作者：</font>** Haozhan Shen, Liangbo He, Jun Lan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) often recognize fine-grained details more accurately in a relevant crop than in the full image. Multimodal on-policy distillation (OPD) methods exploit this by transferring the advantage of a crop-view teacher to a full-image student. However, their supervision relies on region-specific questions curated through an elaborate synthesis pipeline, which brings three weaknesses: (1) every region needs a question--answer pair written exclusively for it, locking training into costly QA curation that is hard to scale to unlabeled images; (2) all rollouts of a region answer the same question, so the teacher supervises only the details it asks about, leaving other visual elements in the region unsupervised; and (3) every question presupposes that its target exists, so the student becomes prone to answering even when the target is absent. In this paper, we study how to turn unlabeled images into broad visual supervision through multi-aspect self-description and privileged-view distillation, and propose CaptionOPD, which replaces tailored questions with a fixed set of image-agnostic caption prompts, ranging from general descriptions to focused captions of parts, colors, counts, text, and layout. The rollouts of a region receive different prompts, so the teacher supervises various aspects of the region. Moreover, because caption prompts mask the model to describe what is visible instead of querying a specific target, they avoid presupposing what the region contains. Using the model itself as the crop-view teacher, CaptionOPD requires no questions, no answers, and no larger model annotations: only images and region boxes. Experiments show that, trained on the same images and regions, CaptionOPD outperforms prior OPD methods across multiple fine-grained and general perception benchmarks.

---


### 190. [STAR: Counterfactual Dual-World Rollouts and Spatial Target Adaptive Reconstruction for Visual On-Policy Distillation](https://arxiv.org/abs/2611.32472)

**<font color=#1a73e8>作者：</font>** Yi Zou, Zhuang Yan, Yudong Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models often rely on global context and language priors while overlooking answer-determining local details. Privileged visual on-policy self-distillation supervises full-image student rollouts using a frozen teacher that views high-resolution evidence crops. Yet our cross-scale diagnostics show that models retain over half of their full-image accuracy when local evidence is completely masked, indicating that single-image correctness does not guarantee reliance on local evidence, while the need for visual correction also varies across tokens with their spatial attention states. We propose STAR, a visual on-policy self-distillation framework combining independent counterfactual dual-world rollouts with spatial-attention-guided target reconstruction. Local image editing constructs paired worlds with identical questions and backgrounds but distinct answer-determining facts, where a shared student samples trajectories independently to expose contextual shortcuts under image-consistent prefixes. Within each world, the teacher contrasts real and mean-color crops to determine the visual correction direction, while the divergence between student image attention and a teacher-centroid spatial reference adaptively controls token-wise target log-probability reconstruction. Without auxiliary attention losses or test-time tool overhead, STAR improves Qwen3.5 across scales by up to 8.04 percentage points in average accuracy over initialization across six fine-grained benchmarks, reaches OPSD's final accuracy $4.7\times$ faster, and generalizes to out-of-domain reasoning tasks.

---


### 191. [VISE: Verifier-Independent Skill Self-Evolution with Feedback from Tool Implementations](https://arxiv.org/abs/2611.32480)

**<font color=#1a73e8>作者：</font>** Yuxuan Liu, Chongyang Du, Yuhao Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills provide reusable workflows that guide LLM agents in using tools. Refining these workflows requires feedback on missing or incorrect instructions, but task-specific verifiers are not always available. We propose VISE (Verifier-Independent Skill Evolution), a scripts-first approach that uses tool implementations to guide skill revision. It extracts tool capabilities, input requirements, usage conditions, and output formats from source code. Using the task request and execution trace, it compares this information with current workflow instructions to identify missing or conflicting steps. It then recommends specific edits to this http URL, linking each change to the relevant implementation and usage conditions. We evaluate VISE as an additional revision stage for four evolution methods on SkillsBench and SkillLearnBench. Compared with the corresponding No-verifier conditions, it improves overall average task success by 9.14-13.35 percentage points. The proportion of tasks solved in all three runs increases by 12.36-18.29 points. A case study shows how revised instructions connect tool outputs to later steps. These results support tool implementations as a practical feedback source for skill self-evolution.

---


### 192. [Analyzing Single-Bit Flips on LLMs and Their Backbone-Matched VLMs](https://arxiv.org/abs/2611.32503)

**<font color=#1a73e8>作者：</font>** Xiaomeng Wang, Martha Larson, Zhuoran Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-weight large language models (LLMs) enable offline weight analysis and are reused as backbones in vision-language models (VLMs), increasing the risk of bit-flip attacks that manipulate stored weight bits to induce malicious model behavior. An adversary could identify vulnerable bits on a public LLM and later flip the same locations in a deployed LLM or its backbone-matched VLMs. A single-bit flip is particularly practical in this setting because it is easier to achieve under hardware fault attacks than multi-bit flips. However, existing selectors are mostly limited to multi-bit flips, without in-depth analysis of single-bit flips. In this paper, we adapt representative data-free and data-based bit selectors to identify candidate bits. We evaluate each bit independently on source LLMs and at the same logical coordinates in backbone-matched VLMs (without re-search), considering both performance degradation and prediction patterns across multiple inputs. Results show impact of single-bit flips varies across selectors on LLMs and their backbone-matched VLMs. A single-bit flip can make the model tend to produce a repeated output string across different inputs. Our robustness analysis reveals vulnerabilities in terms of performance and prediction patterns.

---


### 193. [RecurSciBench: Benchmarking Recursive Self-Improvement in Data-Driven Scientific Research](https://arxiv.org/abs/2611.32508)

**<font color=#1a73e8>作者：</font>** Wenxi Xu, Chuan Qin, Zihan Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based agents are advancing the automation of data-driven scientific research. Recent advances in recursive self-improvement (RSI) offer the potential for these agents to continuously improve through experience, but evaluating transfer across scientific tasks requires executable, scientifically verifiable tasks and independent assessment of self-improvement gains. We introduce RecurSciBench, a scalable benchmark for evaluating RSI in data-driven scientific research. Its RecurSciPipe framework automatically constructs scientific modeling and data analysis tasks from raw datasets, with execution-based verification and scientific validity checks. RecurSciBench spans four scientific domains, multiple data modalities, and varied scientific objectives. We evaluate four RSI systems by comparing their initial and evolved states on independent tasks after evolution on source tasks, covering within-type, cross-type, and cross-domain transfer. Experiments show that the benefits of self-improvement vary across agent systems and scientific domains. Positive overall gains can coexist with regressions on individual tasks. Experience can transfer across task types and benefit other domains even without measurable gains in the source domain.

---


### 194. [GeoVLDrive: Geometry-Grounded Vision-Language Reasoning for Autonomous Driving](https://arxiv.org/abs/2611.32510)

**<font color=#1a73e8>作者：</font>** JiaHui Huang, Songyan Zhang, Hanbing Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) planners inherit semantic knowledge from pretrained vision-language models, but their reasoning is rarely grounded in 3D scene structure and its evolution over time. We introduce GeoVLDrive, a geometry-grounded VLA framework for 3D spatiotemporal reasoning and planning. Multi-layer features from a 3D foundation model augment the vision-language backbone through gated cross-attention. A structured latent chain of thought (CoT) organizes future scene geometry, key-agent motion, and meta-actions into ordered, separately supervised latent states. An action expert generates trajectory proposals from these states and multi-layer scene features, and ranks them using scene-grounded, interacting score tokens. We also introduce NAVSIM 3DQA to train and evaluate metric 3D spatial and motion understanding. GeoVLDrive achieves 91.8 PDMS on NAVSIM v1 and 90.9 EPDMS on NAVSIM v2. On NAVSIM 3DQA, the geometry-grounded backbone scores 89.2% overall, 4.6 percentage points above the fine-tuned Qwen3-VL-2B baseline. On LingoQA, the backbone achieves 68.6% Lingo-Judge accuracy.

---


### 195. [Branch and Consolidate: A Unified Recipe for Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2611.32515)

**<font color=#1a73e8>作者：</font>** Zihan Liang, Zikun Qu, Ben Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Specialists post-trained from a shared checkpoint acquire complementary capabilities, and multi-teacher on-policy distillation (MOPD) can consolidate them into a single model. However, we find that existing consolidation methods, from weight merging to MOPD, fall short when specialists diverge substantially from the shared checkpoint, whereas prior studies mostly examine specialists that remain close to it. We present a unified recipe for multimodal MOPD that consolidates such specialists back into the single student they branched from. The recipe specifies initialization, data selection, balanced supervision across teachers, and preservation of existing capabilities for consolidation, together with a targeted refinement stage for capabilities that still lag behind their specialists. In an industrial setting with six specialists, the student closely approaches each specialist in its own domain and surpasses the perception specialist. It recovers 97.0% of their average gain, compared with 79.8% for IM-MOPD. In the fully open five-domain setting with Qwen3-4B, our method recovers 95.7% of the specialists' average gain after consolidation and 97.5% after refinement, compared with 94.1% for IM-MOPD. We further analyze the full pipeline through mechanism ablations and training dynamics, providing practical guidance for diagnosing incomplete consolidation. Code will be released.

---


### 196. [What If Chinese Were Latinized? A Counterfactual Study of Input Representation, Tokenization, and Language Modeling](https://arxiv.org/abs/2611.32525)

**<font color=#1a73e8>作者：</font>** Zijie Zheng, Ej Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> If Chinese had been Latinized, as the Latinxua Sin Wenz movement proposed, what would it have meant for Chinese NLP? Homophones and tone marking complicate the answer. We convert Chinese corpora to syllable-separated Pinyin and train superBPE tokenizers from scratch. The resulting Pinyin vocabularies not only exhibit expected homophone collisions, but also show approximately 10% higher fertility than characters. An alternative BPE configuration changes the relative fertility of the two representations. We further pretrain Llama-style models on Chinese characters and Pinyin. The Pinyin models perform worse on per-character perplexity, homophone disambiguation, and overall ZhoBLiMP minimal-pair accuracy. An exploratory phonological probe yields near-chance performance for both representations. The broader implication is that written input representations are not merely neutral encodings. Choices for representations affect language modeling and their downstream performances. Latinization never actually happened for Chinese, but other languages did, such as Hangul and Latin script replaced character in Korean and Vietnamese; the cost we measure is a guide to where modeling effort for those languages should concentrate.

---


### 197. [Advanced Synthetic Image Detection Using Hybrid Feature Extraction](https://arxiv.org/abs/2611.32538)

**<font color=#1a73e8>作者：</font>** Ameya Uppina, S Navaneetha Krishnan, Nikhil N Iyer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the realm of generative AI, models such as GANs, MidJourney, DALL-E, and others have been continuously evolving to generate increasingly lifelike images. This rapid advancement has created an urgent need for robust methods to distinguish between real and AI-generated images. This paper proposes a novel approach for the detection of synthetic images by employing deep learning techniques for feature analysis. The proposed architecture classifies images by identifying variations that generative models struggle to replicate, particularly fine-grained textures and complex object features. Deformations in complexes are examined with the help of the CBAM architecture along with ResNet50. We have performed a selective patch-based analysis using Discrete Cosine Transform (DCT) scoring, extracting the regions with the most and least complexity for further processing with an SRM Module and ResNet50 module. Experimental results show that our approach achieves high accuracy in classifying real-world images from synthetic ones, contributing to the development of more reliable detection frameworks.

---


### 198. [Avalon-M1: Reinforcement Learning from Collective Rewards](https://arxiv.org/abs/2611.32539)

**<font color=#1a73e8>作者：</font>** Iliyan Zarov, Henry Course, Anthony Hartshorn 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce reinforcement learning from collective rewards (RLCR), a recipe for jointly training language models to act as agent organisations under latency constraints. A CEO and up to eight specialists share one policy, co-ordinate through a message board and workspace, and are trained with a common outcome-derived advantage. The deadline makes parallel work valuable when it increases the return earned before the cap. We train Avalon-M1-Mini (120B) across 147 environments. For the trained model, eight-hire organisational execution raises IMO-ProofBench-Advanced scores from 23.8% to 39.0% relative to single-agent execution. Across 12 benchmarks, organisations achieve similar average scores at approximately one-third the derived latency of token-matched single-agent execution and just over half that of eight independent attempts followed by selection. The trained model also outperforms Nemotron 3 Super, post-trained from the same base model, across all evaluations when comparing each model's best tested configuration. On EdgeBench, organisations overtake the single agent after approximately 0.4 derived hours. Over the course of training, organisations develop hierarchies to manage communication costs, invest more in peer review, and alter how work is divided. Safety evaluations find near-universal refusal of harmful actions but sustained declines in external reporting in two of three oversight scenarios. These results establish a shared-advantage baseline for studying organisational learning, performance-latency trade-offs, and collective oversight.

---


### 199. [SetCon: Setup-Conditioned IMU-Language Learning from 3D Human Motion](https://arxiv.org/abs/2611.32548)

**<font color=#1a73e8>作者：</font>** Lennart Schiweck, Alaa Saleh, Cristóbal Curio  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aligning inertial measurement unit (IMU) signals with text enables zero-shot activity recognition across wearable devices. A worn device's signal depends on its setup, the combination of body site and mounting. Leading IMU-language models make their encoders invariant to the mounting, which also discards the device's orientation relative to the body, such as the direction of gravity that separates sitting, standing and lying. We introduce SetCon, which replaces full invariance with selective invariance. It estimates each device's mounting on its known body site from a few unlabeled windows and conditions its encoder on this estimate. Because the mounting stays nearly fixed while the device is worn, the moving body serves as a calibration target. Both calibration and representation learning are supervised by 3D human motion, since one movement can be simulated under many known sensor setups. At test time, a class is represented by its name or by an anchor, which averages the text embeddings of the name and of activity descriptions and needs no labeled window. A language model built on the frozen encoder also answers how and in what order a movement is performed. Trained only on IMU simulated from the same Nymeria motion capture as AnyMo, SetCon reaches 56.6% mean zero-shot accuracy on 13 real datasets with class names and 65.3% with anchors, against 41.8% and 46.7% for AnyMo.

---


### 200. [MinPair: Measured Minimal Pairs for Fine-Grained Control in Text-to-Motion Generation](https://arxiv.org/abs/2611.32549)

**<font color=#1a73e8>作者：</font>** Lennart Schiweck, Cristóbal Curio  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-motion generation has made great progress in capturing what action to perform, yet it remains limited in controlling how that action is executed. For example, when only the height word of a kick request changes, none of the tested state-of-the-art methods reaches all three of knee, waist and head height. The other words of a caption usually imply an attribute such as height, so neither the training loss nor the standard metrics require a model to use the word that states it. A model has to use this word only when it alone separates two otherwise identical captions. We introduce MinPair, which creates such caption pairs from real motion clips. It starts from rule-based motion descriptors that measure the 3D body motion of each clip. From these descriptors a language model writes MinPair captions, timed body-part captions that say how each body part moves. The same descriptors show in which attributes two clips of the same action differ. A measured minimal pair joins the true caption of one clip with an altered copy in which only one attribute takes the value measured in the other clip. A contrastive pair loss then requires a diffusion denoiser to reconstruct the clip more accurately from its true caption than from the altered copy. Training needs no synthetic motion and inference stays unchanged. Control is tested on 22 target tasks and on caption edits that each change one attribute. MinPair captions alone help motions reach their targets and improve the standard metrics M2M, R@3 and FID, yet a model trained on them still ignores most single-word edits. The pair loss raises the share of followed template edits from 11% to 60%, while the standard metrics do not improve further. With body-part captions, MinPair reaches more targets than state-of-the-art methods that were trained on up to 99 times more motion data.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-299](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
