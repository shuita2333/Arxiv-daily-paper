# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 251. [Step-Zero Attack: Agent Safety Before Observability](https://arxiv.org/abs/2611.01953)

**<font color=#1a73e8>作者：</font>** Tian Qin, Yuhang Jiang, Junzhe Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing attacks and defenses for coding agents act once content enters the model context: injected text persuades the model, and guards inspect what the model reads. Yet to judge whether processing an unknown archive, network response, or image is safe, an agent often must process it first, and that step can do harm before any content reaches the model. We call this first processing Step Zero, and harm done by it a Step-Zero attack. Across seven harnesses and six models, each agent received only a path or URL to a crafted input, paired with a benign twin showing the same visible fields. Step Zero is where most agents are already unsafe: 32/42 harness-model pairs overran a 4 MiB disk budget, 26/42 before the model saw any member, and four of the six models did so in every round (84/84), so the damage precedes any model-side defense. Every twin stayed within budget, so the attacker's bytes alone cause the harm. On network and image inputs the risk moves to what the agent writes: agents stored the body under the name the input declared, letting the input decide what is written, and their checks faded once cues were removed. Model-free tests trace the harm to the processing primitive, so we defend it there: a gate that counts the bytes each call produces held every routed extraction within budget while agents completed 25/28 tasks. Vendors should pair such gates with safety-alignment training that teaches agents to inspect an input before processing it.

---


### 252. [Towards Self-Evolving Narrative Systems: Real-Time Adaptation and Long-Term Optimization with LLMs](https://arxiv.org/abs/2611.01954)

**<font color=#1a73e8>作者：</font>** Ruisheng Sun, Jiaqi Shao, Weijia Han 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional interactive narrative systems offer strong authorial control and structural coherence but often restrict player agency. In contrast, LLM-driven narratives enable open-ended generation and greater flexibility, yet frequently suffer from inconsistency and diminished narrative control. To navigate this trade-off, we propose a hybrid narrative framework that dynamically balances pre-authored content with real-time LLM generation via semantic similarity alignment. Additionally, sustaining narrative quality over extended gameplay remains a core challenge in LLM-based storytelling. To address this, we introduce a self-evolving, feedback-driven optimization framework that leverages in-context learning to iteratively refine prompts, eliminating the need for manual prompt engineering. Through a case study and participant-based evaluation, we show that our framework enhances narrative coherence while preserving player agency, effectively aligning generated content with both authorial intent and evolving player behavior.

---


### 253. [OC-OPD: Observation-coordinated Supervision for On-Policy Distillation](https://arxiv.org/abs/2611.01965)

**<font color=#1a73e8>作者：</font>** Ruoran Xu, Yilun Zhao, Ziyu Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reverse and forward Kullback--Leibler (KL) divergences provide complementary supervision in on-policy distillation: reverse KL refines the student's active token rankings, and forward KL allocates mass to teacher-supported candidates. At student-generated prefixes, we form a four-observation matrix by treating the student and teacher as both candidate sources and evaluators. The diagonal self-observations measure uncertainty, while source-centered cross-observations recover the two KL objectives. We establish an exact identity equating the Fisher inverse-metric coupling of their logit gradients with the sum of these contrasts, yielding a common local descent direction for distinct positive distributions. Observation-coordinated on-policy distillation (OC-OPD) uses observations to set preferences, closed-form bargaining to coordinate gradients, and distributional discrepancy to scale the update. Across three heterogeneous student settings (non-thinking generation, thinking generation, and base-model initialization), OC-OPD achieves strong gains in mathematical reasoning and transfers effectively to out-of-distribution scientific question answering and code generation. Our code is publicly available at: this https URL.

---


### 254. [Better Answers, Weaker Evidence Control: Evidence Bypass in On-Policy Distillation](https://arxiv.org/abs/2611.01967)

**<font color=#1a73e8>作者：</font>** Ruoran Xu, Yilun Zhao, Ziyu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) can improve answer accuracy while weakening responsiveness to supporting evidence. We investigate this separation in scientific-document question answering through matched document interventions that change the supported answer while preserving the question and unrelated context. We identify evidence bypass: a student retains an originally correct answer after the document changes to support a different one. On QASPER with a Qwen3-4B student, standard OPD raises original-document accuracy by 3.4 percentage points, lowers counterfactual accuracy by 5.3 points, and increases bypass by 15.7 points; the same directional pattern appears on PeerQA. Controlled perturbations localize the shift to answer-critical evidence, and bypass grows with the student's pre-distillation closed-book preference for the original answer. A factorized study of teacher targets, privileged information, divergence, and supervision density finds that explicitly supplying the teacher with annotated answer-critical spans yields the largest joint improvement in evidence response and claim support. These findings motivate Evidence-Paired OPD (EP-OPD), which combines on-policy supervision on matched documents supporting different answers to the same question with an answer-level margin that favors each document's supported answer over its paired alternative. Across both datasets and two student sizes, EP-OPD recovers 54-66% of standard OPD's counterfactual-accuracy loss while preserving 80-85% of its original-document accuracy gain. Our results establish evidence responsiveness as a distinct training and evaluation target alongside answer accuracy. Our code is publicly available at: this https URL.

---


### 255. [Knowledge-Guided Floodwater Level Reasoning for Cloud-Edge Collaborative Monitoring](https://arxiv.org/abs/2611.01970)

**<font color=#1a73e8>作者：</font>** Zhengshu Zhou, Shaoyu Wang, Ziyi Geng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frequent urban floodwater poses a serious threat to the safety and efficiency of intelligent transportation systems. Existing vision-based methods for floodwater level detection face two main limitations. First, the lack of explicit reasoning leads to poor detection performance and little interpretability. Second, these methods struggle to generalize to the complex and varied real-world road scenes seen from different viewpoints. To address this, we reformulate the task as an explicit visual reasoning problem and propose HydroReasoner, a floodwater level reasoning framework designed for cloud-edge collaboration. HydroReasoner builds on Qwen2.5-VL and is trained with Group Relative Policy Optimization. To address the scarcity of reasoning process annotations, we build a floodwater domain knowledge graph HydroKG and design a novel KG path reward. Through deterministic graph traversal over HydroKG, this reward supervises the model's reasoning process at a fine granularity, which improves both reasoning and generalization. For edge deployment, we apply 4-bit quantization to the model, cutting GPU memory usage by 57% and inference latency by 43% while out-of-domain accuracy drops by only 0.2 percentage points. We also propose a confidence-based cloud-edge routing mechanism, which improves system safety and eases the computational load on the cloud. In addition, we build HydroLevel, a floodwater benchmark dataset of 3,000 images, for training and evaluating the model. Experimental results show that HydroReasoner achieves detection accuracy 4.0 and 13.6 percentage points higher than conventional vision baselines in the in-domain and out-of-domain evaluations respectively, with performance dropping by only 4.4 percentage points out of domain.

---


### 256. [RubricWorld: World Model-Guided Rubric Optimization for LLM Graders](https://arxiv.org/abs/2611.01986)

**<font color=#1a73e8>作者：</font>** Hongji Pu, Hang Li, Yucheng Chu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubric optimization improves LLM grading by revising scoring instructions while keeping the grader's parameters fixed. Existing optimizers often judge edits by aggregate validation performance, limiting the supervision they retain about which errors an edit corrects or introduces. Testing each candidate also requires rescoring validation answers, which limits how many edits can be explored within a fixed budget. We propose RubricWorld, a framework that learns from previous edit evaluations to guide further search. Its world model predicts an edit's correction and degradation rates at score boundaries, conditioned on the current rubric state. The training signal comes from paired grading results: scores for the same answers before and after an edit. Predictions select one candidate for direct evaluation, and held-out confidence bounds determine whether it corrects enough target errors while keeping new errors within prespecified limits. Measured effects update the model even when the edit is rejected. Across EIR (National), ASAP2.0, and ASAP-SAS with three frozen LLM graders, RubricWorld achieves the highest score in 20 of 27 metric comparisons. On ASAP2.0, it raises gpt-5-mini accuracy from 18.20% with the original rubric to 46.70%, exceeding the strongest baseline, APO, by 22.60 percentage points. code will be released upon acceptance.

---


### 257. [Synthetic Realities: Evaluating Human Ability to Distinguish AIGenerated Videos from Real Footage](https://arxiv.org/abs/2611.01990)

**<font color=#1a73e8>作者：</font>** Danyal Sarfraz, Raja Mubashar Karim, KwanMyung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative AI have enabled multiple pathways for high-fidelity video synthesis: text-to-video, image-to-video animation, and video outpainting. Empirical side-by-side evaluations of how untrained viewers perceive and distinguish these outputs from real footage remain scarce. In this study, we systematically compare human detection accuracy across these three AI generation techniques within three thematic contexts: historical footage, film and media content, and natural environments. We constructed a balanced stimulus set comprising equal amounts of real and AI-generated videos (18 each). The AI clips were evenly distributed across the three generation methods using Google's Veo 3, Lightricks LTX Video, and Wan VACE. All videos were produced and standardized within the ComfyUI framework to ensure consistent quality and duration. 87 participants judged every clip in a binary forced-choice task ("real" vs. "AI-generated"). Participants correctly identified videos 60% of the time on average. Image-to-video clips were recognized most accurately (79%), followed by real footage (64%), outpainting (49%), and text-to-video (43%). Accuracy also varied by theme: film and historical scenes yielded higher detection rates than environmental clips, which were frequently mistaken for AI. Logistic regression confirmed significant effects of both technique and theme as well as their interaction (p < 0.001), indicating that detection success depends jointly on how the content was generated and what it depicts. Findings reveal a consistent bias toward assuming synthetic origins and highlight that perceptual realism in AI video is shaped more by context than by model type, underscoring the importance of media-literacy approaches and context-aware evaluation tools for navigating increasingly synthetic visual media.

---


### 258. [Safety4DM: A Vision-Language Framework for Risk-Aware Dynamic Maps in Vehicle-Road-Cloud Collaborative Driving](https://arxiv.org/abs/2611.01996)

**<font color=#1a73e8>作者：</font>** Zhengshu Zhou, Shaoyu Wang, Lu Tao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Dynamic map (DM) is a core information infrastructure for vehicle-road-cloud (VRC) cooperative autonomous driving. It fuses perception data from multiple sources to overcome the inherent line-of-sight and field-of-view limits of single-vehicle perception. However, DM still falls short on driving safety in two ways. First, DM data specifications already define road conditions semantically, but no pipeline yet turns real-world road observations into fine-grained risk entities in the DM. Second, existing DM systems lack a natural language interface for driving risks. To close these gaps, we propose Safety4DM, a safety-oriented language system for VRC dynamic maps. We first build RoadRisk, a real-world road image dataset that covers four types of road conditions and four risk levels. On this dataset, we fine-tune a vision-language model (VLM) for road safety risk perception. The model outputs structured risk representations that the DM can ingest directly. We then introduce a Safety-aware Step-wise Prompting (SafeStep) mechanism as the natural language query interface of the DM. SafeStep answers queries accurately and also generates actionable driving advice. To build and evaluate this interface, we develop SafeVRC-Sim, a VRC cooperative simulation framework, and SafeDM-QA, a safety question-answering benchmark. Experiments show that even the compact Qwen3-VL-4B reaches 89.83% accuracy on risk perception after fine-tuning. SafeStep also plugs easily into multiple LLM families. With medium and large models (20B and above) from five families, it achieves over 93% natural language query accuracy in every case, which shows strong generalization.

---


### 259. [TrackMem: Tracking Evolving Beliefs in Long-Horizon Financial Dialogue](https://arxiv.org/abs/2611.02001)

**<font color=#1a73e8>作者：</font>** Austin M.Y. Cheung, Harsh Vardhan Gupta, Go Nam Lui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Memory systems for LLM agents are evaluated mostly on social dialogue, where facts accumulate and rarely change, so remembering reduces largely to finding the turn in which something was said. Financial dialogue breaks this assumption: figures are revised, stances shift without being restated, rules stated once govern later questions, and a single company is discussed under several analytical lenses. Memory systems that retrieve the passages most similar to a question, or the most recent ones, therefore return superseded values, miss rules that share no wording with the question, and cannot recover a stance spread across sessions. We present TrackMem, a per-speaker graph memory that tracks the history of figures, separates perspectives by entity and lens, and preserves each speaker's actions in chronological order. To evaluate it, we introduce FinLoCoMo, a benchmark of 15 long-horizon investment conversations with 765 questions in two splits: one following the LoCoMo categories and one targeting four failure modes. With two readers, TrackMem outperforms existing memory systems on both splits. On the failure-mode split it reaches 73.9% macro accuracy against 69.4% for the strongest baseline, with the largest gains on questions about revised figures (86.5% against 73.4%).

---


### 260. [To Align Long, Plan Short: Simulating Diverse Profile-Aligned Students by Realizing Short-Term Plans in Long-Horizon Learning Environments](https://arxiv.org/abs/2611.02002)

**<font color=#1a73e8>作者：</font>** Bahar Radmehr, Jiaxu Zhao, Fatma Betül Güreş 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulated students offer a scalable way to test learning platforms and AI tutors before deployment with real students and to augment scarce data for studying learning at scale. Existing LLM-based simulators primarily target short, language-centered interactions. In open-ended learning environments, however, student behavior emerges from patterns across long-horizon interaction trajectories, where turn-level prompting can drift from an assigned behavior profile. We introduce ALPS (Align Long-term by Planning Short-term), a hierarchical simulated student conditioned on observable, environment-specific behavior profiles. Rather than selecting every action independently, ALPS alternates between planning profile-aligned task segments and generating the corresponding actions. We evaluate ALPS in both data-sufficient and data-scarce settings, where supervision comes either from real student trajectories or from a teacher LLM. Across both settings, we compare in-context learning (ICL), supervised fine-tuning (SFT), reward-ranked fine-tuning (RAFT), and their sequential combination (SFT followed by RAFT). Experiments in an inquiry-based physics game and a pharmacy simulation evaluate behavioral density and coverage against held-out real data, and profile consistency using a human-aligned LLM judge. Across both settings, ALPS consistently outperforms turn-level generation, achieving comparable density and judge pass rates under scarce supervision, although coverage remains lower. These results show that hierarchical planning enables faithful, profile-aligned simulation over long interaction horizons, even with limited real student data.

---


### 261. [NAS-PO: Native Attention-Strategy Policy Optimization for Vision-Language Models](https://arxiv.org/abs/2611.02008)

**<font color=#1a73e8>作者：</font>** Ke An, Shizhe Xiang, Yue Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become an effective post-training paradigm for vision-language models (VLMs). Standard RLVR, however, assigns identical outcome-derived credit to all generated tokens regardless of their perceptual relevance. Recent perception-aware methods estimate visual reliance through image perturbation or masking. These indirect proxies require perturbation branches, while corruption sensitivity does not necessarily identify the visual evidence used for reasoning. We instead shape model perception through native attention, an intrinsic model signal. Rather than treating attention as a post-hoc explanation, we formulate it as a reward-anchored, token-aligned routing signal that encourages attention patterns supporting visually grounded reasoning. To this end, we propose NAS-PO, a Native Attention-Strategy Policy Optimization framework. NAS-PO analyzes native attention with a visual mass policy that quantifies visual allocation and a conditional visual policy that captures spatial routing over visual tokens, making the optimization well-posed. Based on this, Native Attention-Strategy Advantage Shaping (NAS-AS) draws on the visual-mass policy to redistribute signed policy-gradient credit for visually engaged rollouts. The Adaptive Attention-Coupled (AAC) loss then aligns the visual-mass policy on all response tokens and the conditional visual policy on visually active ones, consolidating the visual-routing patterns that drive successful trajectories. Experiments demonstrate that NAS-PO substantially surpasses leading RL-tuned VLMs across 7 out-of-domain reasoning and perception benchmarks, with its effectiveness consistently validated across 8B and 32B. Visual-Routing Sensitivity (VRS) analysis further indicates that the optimized attention prioritizes visually load-bearing regions.

---


### 262. [Retrieval-Enhanced Cultural Evaluation for Social Media Translation Training](https://arxiv.org/abs/2611.02009)

**<font color=#1a73e8>作者：</font>** Linjuan Wu, Yiwen Qiu, Xinze Lyu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Social media translation requires preserving meaning while capturing the cultural nuances of user-generated content (UGC). However, gaps in the cultural knowledge of LLM-based evaluators can lead to inaccurate assessments and unreliable training rewards. To improve these signals, we use retrieval-enhanced cultural evaluation to train CUE-MT, a family of social media translation models. A calibrated, domain-specific Judger guides supervised data refinement and is augmented by an Agent for hard-example mining and reinforcement learning. The Agent retrieves relevant external evidence as needed and distills it into concise hints that the Judger uses to score translations and assign rewards. Across 9B, 27B, and 35B-A3B backbones, CUE-MT outperforms the evaluated open-source baselines of comparable size on CUE-MT-Bench and three public benchmarks. Human evaluation on CUE-MT-Bench shows cultural effectiveness gains of 7.44-15.12 percentage points over the strongest external baseline in each size group. Retrieval improves the Judger's four-way classification accuracy by 8.07 percentage points over a matched no-retrieval baseline that uses LLM-generated hints alone. Training ablations further support the combination of hard-example mining and Agent-enhanced rewards.

---


### 263. [MedPsy: State-of-the-Art Small Medical Language Models for Efficient Edge Deployment](https://arxiv.org/abs/2611.02011)

**<font color=#1a73e8>作者：</font>** Davide Vitabile, Alexandro Buffa, Akshay Nambiar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Medical language models promise expert clinical support, but the strongest open-source LLMs remain too large for private edge-device deployment, while compact medical models still trail substantially on knowledge-intensive and real-world healthcare tasks. Reasoning models that fit edge memory budgets can produce long reasoning traces, increasing sequential decoding, end-to-end latency, energy consumption, and KV-cache memory pressure. We present MedPsy, a family of text-only 1.7B and 4B medical language models designed for edge deployment, targeting this accuracy-generation-efficiency trade-off. Our recipe combines a synthetic medical data pipeline over biology, medicine, and health seeds with chain-of-thought targets from a 235B medical-focused LLM teacher; a four-stage post-training curriculum comprising two SFT stages followed by two RL stages with hard-sample mining; and an edge deployment evaluation spanning multiple GGUF quantization variants and real-device inference on laptop and smartphone hardware. On seven closed-ended medical benchmarks, MedPsy-4B surpasses MedGemma-1.5-4B by 19.34 points and matches MedGemma-27B while being 6.75x smaller; MedPsy-1.7B outperforms MedGemma-1.5-4B by 11.42 points despite being less than half its size. On HealthBench-Hard, MedPsy-4B surpasses MedGemma-27B by 15.33 points, while MedPsy-1.7B surpasses it by 11.66 points despite being ~16x smaller. Beyond accuracy, MedPsy reduces average response length by 1.7x (1.7B) and 3.2x (4B) versus its Qwen3 backbones, while Q4_K_M quantization preserves the aggregate score within 1 point of BF16 with ~69% lower disk footprint. In real-device inference, MedPsy-4B's shorter generations translate into 75% lower median end-to-end latency and estimated energy per answer than its Qwen3 backbone at matched quantization, while peak RAM remains below 5 GB across our tested laptop and smartphone configurations.

---


### 264. [Scaling Makes It Possible: How Large Models Master Impossible Languages](https://arxiv.org/abs/2611.02015)

**<font color=#1a73e8>作者：</font>** Yaning Jia, Chunhui Zhang, Chiyu Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While language models (LMs) excel in natural language tasks, their ability to learn impossible languages--those that violate the structural, cognitive, or logical constraints that make human languages learnable and functional--remains debatable. This controversy is further fueled by a divide between linguistic theorists and empirical researchers working with small-scale LMs. To address this controversy, we introduce semantic coherence. This concept measures how effectively semantic information is expressed in language structures and examines the learning capabilities of LMs across multiple scales. By fine-tuning billion-parameter LMs on impossible language samples, we demonstrate that larger LMs achieve similar performance on impossible and possible languages, whereas million-parameter LMs exhibit significant degradation when trained on impossible languages. This performance gap widens as semantic complexity increases. We further show that scaling up the LM size fundamentally shifts the learning focus from grammatical rules to semantic understanding, with billion-scale LMs exhibiting a threefold reduction in sensitivity to low-level linguistic perturbations while maintaining stable performance under high-level semantic perturbations.

---


### 265. [Switch-SWE: Do Coding Agents Hold Focus When Switching Between Unfinished Tasks?](https://arxiv.org/abs/2611.02017)

**<font color=#1a73e8>作者：</font>** Shuochen Chang, Qianli Ma, Yibo Miao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Software development sessions often involve several unfinished tasks rather than one issue carried through to completion. As coding agents take on repository-level development, they need to recover an earlier task's requirements and partial progress after intervening work. Existing repository-level benchmarks typically score one issue-to-patch episode and do not directly measure whether an agent can resume a task after advancing other unfinished work in the same repository. We introduce \textbf{\ourmethod}, a benchmark for focus-task resumption in sessions that interleave unfinished tasks drawn from the same source repository, with a persistent checkout for each task. Each focus task is evaluated in matched uninterrupted and switched sessions with identical focus requirements and executable verifiers. The switched session interleaves ordered stages from other unfinished tasks in the same repository, while only the final focus patch is scored. \ourmethod~contains 200 focus tasks from 19 Python repositories, reconstructed from issue, pull-request, and review histories and rendered as 400 matched session specifications. Across 7 coding agents, interleaved unfinished work produces an average focus-task resolution gap of 11.5 percentage points, ranging from 6.0 to 15.0 percentage points. Trajectory analysis identifies cross-task requirement confusion and loss of task state as recurrent resumption behaviors. We introduce a plug-in context-management module that selects task-relevant history and maintains concise task-state summaries. On OpenCode, the module improves focus-task completion under same-repository task switching by 5.5 to 15.5 percentage points across the evaluated models. Code is available at this http URL.

---


### 266. [ClickSight: An LLM Framework for Interpreting Student Clickstreams Through Learning Strategies](https://arxiv.org/abs/2611.02021)

**<font color=#1a73e8>作者：</font>** Bahar Radmehr, Lan Tran, Ekaterina Shved 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital learning environments produce rich clickstream data that can reveal how students approach learning tasks, yet interpreting these fine-grained traces often requires substantial expert effort. We introduce ClickSight, a framework for interpreting student clickstreams through learning strategies defined in the literature. Given a student clickstream and a predefined set of learning strategies, ClickSight uses a staged LLM-based pipeline to identify strategy-relevant evidence, assess adherence to each strategy, and generate an evidence-grounded interpretation of the student's behavior. We evaluate ClickSight across two learning environments, 365 students, and 12 model backbones using an expert-grounded quality rubric and an LLM judge calibrated with human-expert ratings. Our results show that ClickSight can generate high-quality strategy-based interpretations across different models and environments, with reasoning models performing more consistently than instruction-tuned counterparts. We further find that providing external clickstream-extracted guidance can improve interpretation quality for strategies that require precise quantitative information from the trace. By connecting fine-grained clickstreams with theoretically defined learning strategies and preserving the evidence underlying each judgment, ClickSight provides a flexible approach for studying student behavior in digital learning environments.

---


### 267. [Reconstruction as Spatial Evaluation: Diagnosing Cross-View Spatial Intelligence in Large Vision-Language Models](https://arxiv.org/abs/2611.02026)

**<font color=#1a73e8>作者：</font>** Junfei Wu, Qiuyue Wang, Xuhong Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The spatial intelligence of large vision-language models (LVLMs) requires the ability to combine local visual observations into a geometrically consistent representation of the physical world. Many static benchmarks assess isolated spatial judgments, such as relative direction or distance, while interactive embodied evaluations combine perception with exploration, planning, control, and simulator-specific execution. To bridge this gap, we introduce RECONSPATIAL, a benchmark centered on multi-view 3D scene reconstruction across indoor, tabletop, and outdoor environments. Given real multi-view images and target-object queries, LVLMs are required to jointly predict oriented 3D bounding boxes in a shared, camera-anchored metric coordinate frame. Reconstructions are evaluated along two complementary axes: Structure for relative layout and Metric for physical scale and camera-anchored placement. Nine atomic spatial QA tasks, grouped into Geometric Perception and Spatial Relations, probe spatial capabilities involved in joint reconstruction. Offline navigation extends evaluation to path planning. Evaluation of 18 frontier LVLMs reveals a consistent gap between relative scene structure and metric reconstruction; even GPT-6-Astra scores 81.4% on Structure but only 58.7% on Metric. Tracing this gap, diagnostic analyses link atomic spatial capabilities to reconstruction quality and show that relational consistency alone does not ensure metric accuracy. Experiments with 3D map injection further separate scene construction from path planning, revealing how these geometric errors limit navigation success. Finally, spatial fine-tuning yields broad transfer across both spatial and general vision-language benchmarks.

---


### 268. [LARK: Lean-Assisted Reasoning for LLM-Generated GPU Kernels](https://arxiv.org/abs/2611.02028)

**<font color=#1a73e8>作者：</font>** Zixi Zhang, Jiayi Nie, Haoran Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Efficient GPU kernels are typically low-level and hardware-specific, and LLM agents can now generate them faster than experts can verify. Existing approaches rely on testing, which provides evidence but not a guarantee of correctness. We introduce LARK, an agentic framework that automatically and formally verifies GPU kernels against their PyTorch reference implementations. LARK proves equivalence in functional and memory behavior under exact arithmetic and establishes a new trust boundary: human effort is only needed to verify operator-level Lean semantics ahead of kernel generation time, instead of checking every single line of generated code. LARK formalizes the GPU machine model and the semantics of each operation in Lean 4 once per target language, and the Lean 4 semantics of any incoming kernel is derived from these pre-built definitions. LLM agents then automate the proof in two steps. First, an agent decomposes the whole kernel semantics into smaller segments and Lean 4 verifies this segmentation, which addresses the intractability of proving equivalence for large kernels directly. Second, agents write Lean proofs that each kernel segment matches its high-level PyTorch counterpart. Together, the two steps give whole-program equivalence. We demonstrate that LARK can be used 1) to ensure correctness in existing code-generation agents and 2) to automatically verify human-written kernel libraries. On the KernelCraft GPU tasks, combined with a simple ReAct agent, LARK enables GLM 5.3 to fully verify 10 of 12 Level-1 kernels and Opus 5.5 all 5 Level-2 kernels. Moreover, over 10 production kernels randomly sampled from popular open-source LLM serving frameworks, LARK verifies 9 and identifies a new data race bug in the tenth. We believe LARK represents a significant step toward verifiable code generation in the agentic era.

---


### 269. [Query-efficient scan-and-search watermark localization](https://arxiv.org/abs/2611.02030)

**<font color=#1a73e8>作者：</font>** Liyuan Wang, Xinsong Ma, Ziye Ma  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recently, the detection of AI-generated content has been of particular importance in various fields of our society. For accountability purposes, many large language models (LLMs) have implicitly watermarked their outputs. Localizing such watermarks requires a piece of text to undergo an additional verification process. Existing localization methods typically rely on dense token-level scoring, making verification costly even when an LLM-generated watermark only sparsely appears. To tackle this problem, we design a new adaptive allocation strategy that first maintains broad document coverage and then progressively concentrates the detection budget on regions that exhibit stronger watermark evidence or are more likely to contain watermarked content. We then transform the statistical signals from the selected regions into e-values and employ the proposed token-weighted e-BH procedure to determine the localized watermark regions. The resulting framework is called BELL (Budgeted E-evidence Localization for LLM Watermarks). Theoretically, BELL can control the token-weighted false discovery rate (FDR) without independence assumptions across regions. Finally, extensive experimental results demonstrate that BELL consistently outperforms competing methods across multiple LLMs, datasets, and watermarking schemes.

---


### 270. [How Green Is Your Manifesto? Scoring Environmental Positions in the 2024 EU Elections with an LLM Panel](https://arxiv.org/abs/2611.02033)

**<font color=#1a73e8>作者：</font>** Franco Corti, Sajid Siraj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Locating political parties on environmental and climate policy is central to the study of party competition, yet the established instruments, expert surveys and the hand coding of manifestos, are costly, periodic, and slow to extend to new documents. We ask whether a panel of large language models can serve as a cheaper and reproducible alternative. Treating each manifesto as a set of sentences, three models from independent providers score every sentence on two dimensions, environmental protection and climate change, separating a party's position on an issue from the salience it gives it, and the judgments are averaged to the manifesto level. Agreement across the models is retained as a built-in reliability signal. We apply the panel to 41 manifestos from the 2024 European Parliament election, covering Austria, France, Germany, Italy, Spain, and the European party families, and validate it against the 2024 Chapel Hill Expert Survey for the 25 parties with a like-for-like expert benchmark, using the other manifestos as diagnostic cases. The panel recovers the expert ordering of parties with strong rank agreement on both dimensions, while reading them as systematically greener than experts do, a gap we interpret as the distance between manifesto promise and governing record. Inter-model disagreement modestly flags where the instrument errs, and position and salience prove related for environmental protection but independent for climate change. The result is a transparent, low-cost, and multilingual instrument that complements rather than replaces expert and hand-coded approaches; the prompt, code, and manifesto-level results are released openly.

---


### 271. [Scalar Smoothness Is One Point on a Besov Spectrum](https://arxiv.org/abs/2611.02037)

**<font color=#1a73e8>作者：</font>** Bum Jun Kim, Anastasis Kratsios  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Studies of neural network generalization and robustness often summarize smoothness with a single number, such as a Lipschitz constant or a Hessian curvature statistic. However, Lipschitz constants summarize global worst-case sensitivity and Hessian statistics summarize local curvature; neither captures how model responses vary with the size, direction, and location of perturbations encountered in real-world deployment. To measure smoothness under these perturbations, we introduce a finite-difference roughness spectrum that profiles model responses across these conditions. Our roughness spectrum generalizes scalar smoothness measures, bringing Lipschitz sensitivity and directional Hessian curvature into a common framework across perturbation scales. We connect this spectrum to classical Besov theory, which describes how a function's variation changes with scale. Our theoretical analysis also proves that a larger output shift can cause less task damage than a smaller one, and that local curvature alone can miss the blocks most vulnerable to finite perturbations. In image classification, Roughness Source Control (RSC) suppresses margin roughness along noise directions and improves noise robustness in a comparison of 80 checkpoints across four model--dataset combinations. In post-training quantization, we identify blocks that need higher precision by measuring task-loss increases from perturbations matched to the size and direction of each block's quantization error. Our mixed-precision allocation achieves lower perplexity than the Hessian-based HAWQ-V2 baseline under the same GPTQ weights and bit budgets in all 14 settings across seven held-out large language models.

---


### 272. [ECGJev: Question-Conditioned Option Scoring for 12-Lead ECG Interpretation](https://arxiv.org/abs/2611.02041)

**<font color=#1a73e8>作者：</font>** Zhuoyuan Li, Xidong Wu, Hanyu Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical interpretation of a 12-lead electrocardiogram (ECG) often requires answering targeted diagnostic questions with clear, quantifiable decisions. We introduce ECGJev, the first ECG framework built on a decision decoder, a pretrained language model trained to return a probability for every listed option. A question-conditioned bridge compresses frozen waveform and spectrogram features into 16 ECG tokens, and a two-stage procedure adapts the bridge and low-rank adapters on the decoder's native option readout using diagnostic labels alone, scoring all options for a question in one forward pass. Evaluated across four ECG benchmarks, ECGJev achieves the highest macro-F1 on CPSC2018 (80.46%), PTB-XL (71.68%) and Chapman (96.86%), and generalizes competitively to the small-sample PTB cohort. Concept probes and perturbation analyses further show that its predictions rely directly on the ECG input, remain stable under option-order and wording variations, and transfer zero-shot to unseen waveform concepts. Our code is available at this https URL.

---


### 273. [SANAI: Secure ECC Distributed Keyed Parity Embedded in Weights for Protecting Neural Networks against Bit-Flip Attacks](https://arxiv.org/abs/2611.02042)

**<font color=#1a73e8>作者：</font>** Habibur Rahaman, Daniel Lobo, Md Rezoan Ferdous 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Quantized neural networks store weights in dense memory, where bit flips caused by voltage scaling, aging, radiation, or deliberate attacks such as RowHammer can severely degrade model behavior. A single corrupted high-order bit can cause misclassifications or nonsensical language-model outputs. Embedded error-correcting codes (ECC) avoid dedicated parity storage by hiding parity within model weights, but existing schemes embed uniformly across layers and bit planes, leave parity unsecured, and tolerate bit-error rates (BERs) only up to about 6%. An adversary aware of sensitive weights and the ECC scheme can also bypass protection by exceeding the correction capability of targeted codewords. We propose SANAI, a sensitivity-guided, bit-plane-selective scheme that protects critical model weights against bit flips with zero additional parity-storage overhead. SANAI secures parity through keyed embedding across a two-dimensional weight space: spread-transform dither modulation binds parity to a secret key, and keyed interleaving disperses concentrated attacks across codewords. We derive a survival law showing that robustness is governed by the correctable fraction t/n rather than by t alone, and a closed-form bound on the protectable fraction of a model. As a streaming checker on an 8x8 systolic array, SANAI verifies weights on the load path with 0.41% area overhead and no additional memory. Across ten vision backbones, three quantization schemes, and ten language models from 82M to 13B parameters, SANAI stays within about one percentage point of clean accuracy at BERs up to 12%, twice the maximum of prior embedded-ECC approaches. It survives fine-tuning bit-exactly, neutralizes progressive and targeted bit-flip attacks, and exactly corrects AttentionBreaker and SilentStriker attacks.

---


### 274. [Same Function, Different Gradients: Evaluating Gradient Reliability under Reparameterization](https://arxiv.org/abs/2611.02052)

**<font color=#1a73e8>作者：</font>** Bum Jun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradients are no longer used only to train models: Gradient magnitudes are now measurement instruments, used to rank attention heads for pruning, to decide per-example clipping in private training, to allocate adapter rank budgets, and to debug models. Across these workflows, larger gradient magnitudes are taken to mean greater importance. Even for a fixed input--output function, these gradients are computed in one of many possible parameter coordinate systems. For example, attention scores depend on the query and key projections only through the paired product $W_QW_K^\top$. Scaling a head's query projection by $c$ and the corresponding key projection by $1/c$ therefore leaves every output logit unchanged. This change in parameter coordinates rescales the corresponding query and key gradient norms by $1/c$ and $c$, respectively. To test whether gradient-based decisions remain unchanged under these coordinate changes, we introduce Gradient Reliability under Reparameterization (GRR). GRR rewrites a trained model in new parameter coordinates that compute exactly the same function, verifies that predictions are unchanged, and then tests whether the decisions derived from the gradients are unchanged too. Our audits span GLUE classifiers, a ViT on CIFAR-10, GPT-2-medium and GPT-2-large, a 1.1B-parameter Llama-style model on WikiText-2, and six trained LoRA adapters. Empirically, predictions are preserved throughout, but both the gradients and the gradient-based decisions change. Across 66 GLUE attention audits, the median top-3 overlap of raw head-gradient rankings is only $1/3$, and rankings and pruning masks change even under the mildest rescalings we test. In the largest of 14 global-pruning audits, the shifted ranking selects head masks that differ in four of 22 pruned heads and reach $50.92\%$ and $94.84\%$ validation accuracy on one ELECTRA SST-2 model.

---


### 275. [Learning to Look: A Foundation for Visual Understanding](https://arxiv.org/abs/2611.02053)

**<font color=#1a73e8>作者：</font>** Wenshuai Zhao, Yihao Wang, Benjamin Robson 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) suffer from visual hallucination, such as saying an object that is not present in an image. We ask a more fundamental question: whether a VLM is even aware of where it is looking before understanding the semantic meaning in the image. We formulate this question as a LOOK task: identifying which parts of its visual input were available to the model. We construct the task in a self-supervised way without manually labeling the available region to the model. Our experiments show that existing VLMs fail to localize the visible region. We further show that fine-tuning VLMs on the proposed LOOK task improves a model's awareness of visual input.

---


### 276. [Fragility Is Not Reducible to Hardness: Conditional Causal Difficulty for LLMs](https://arxiv.org/abs/2611.02065)

**<font color=#1a73e8>作者：</font>** Mohammad Reza Rezaei, Dingxian Wang, Nikhil Verma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models show large and seemingly arbitrary performance drops when a task is rewritten in ways that leave its requirements untouched. We recast task difficulty as a causal quantity: the treatment effect of meaning-preserving perturbations on a model. A meaning-preserving rewrite can only be observed to hurt a task the model can already solve, so we place the estimand on the principal stratum where the degradation occurs: the conditional causal difficulty (CCD), the probability that a randomly drawn twin breaks a solvable task. Because harder tasks tend to be more phrasing-sensitive, complexity enters as an effect modifier rather than a confounder, and we residualize it out to obtain complexity-residualized difficulty (CRD); zero for a task exactly as fragile as its complexity predicts, positive for anomalously fragile ones. Current benchmarks do not supply the data CCD requires, so we introduce GlassGSM and GlassMATH, augmenting GSM8K and MATH with twins built from perturbation families, raising fragility on GlassGSM by $\approx 12\times$ over GSM-IC-style distractors on the same problems ($3.7\%\to44.9\%$) while keeping the answer key unchanged. Our predictor Frail learns the per-perturbation break probability and reaches $0.613{\pm}0.023$ of the suite reliability ceiling on GlassGSM and $0.557{\pm}0.023$ on GlassMATH, against $0.171$/$0.401$ for a surface-feature baseline and $0.444$/$0.463$ for supervised baselines such as VAP3, and, at a $5\%$ curation budget on GlassGSM, doubles random recall of fragile items, matching an oracle ranking. Additionally, cross-fitted residualization leaves CRD uncorrelated with the declared proxy in practice.
Code is available at this https URL

---


### 277. [State-Aware Virtual Patient Simulation for Training Psychiatrists in Challenging Clinical Scenarios](https://arxiv.org/abs/2611.02067)

**<font color=#1a73e8>作者：</font>** Harsh Mohta, C Chandrahas Reddy, Sunhith Reddy Bojja 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Psychiatrists must be prepared to manage patients exhibiting challenging psychological states, including suicidal ideation, hallucinations, and other high-risk behaviors. However, opportunities to safely practice such interactions are limited. While recent conversational agents can simulate patients, existing approaches largely rely on large language models (LLMs) to determine patient responses, making it difficult to consistently maintain psychological state, adapt to the clinician's responses, and generate clinically plausible challenges that meaningfully test the clinician. We present a state-aware virtual patient simulation pipeline for training psychiatrists in challenging clinical scenarios. The proposed system maintains an evolving patient state throughout the interaction and orchestrates patient behavior rather than leaving response generation entirely to an LLM. At each interaction, a learning-based behavioral strategy selector determines the type and level of challenge appropriate to the current patient and clinician context. The selected strategy, patient state, clinician response, interaction history, and relevant clinical knowledge are then provided as grounded context to an LLM to generate a semantically relevant and psychologically consistent patient response. Following each session, the system analyzes the interaction and provides feedback to the clinician on their communication and management of the virtual patient.

---


### 278. [SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training](https://arxiv.org/abs/2611.02074)

**<font color=#1a73e8>作者：</font>** Ziming Li, Lu Yu, Jiatan Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents solve repository issues through long sequences of exploration, editing, and validation. These trajectories are increasingly used as post-training data, so how they are collected shapes what the trained model learns. A common approach is to sample multiple trajectories independently for each issue and then select or curate them. However, as more trajectories are sampled independently, later trajectories become increasingly redundant, even though earlier trajectories could guide where subsequent collection effort should be spent. A natural way to use this history is to expose it to the coding agent as advice. But training on such trajectories can make the model rely on advice that is unavailable at test time, creating a train-test mismatch. Instead, we argue that history should guide where collection effort is spent, while the coding agent decides what to generate. We introduce SWE-Trail, a trajectory collector that uses earlier trajectories to guide subsequent collection while keeping that history outside the coding agent's context. During a new rollout, SWE-Trail uses history to identify a state where additional collection effort may be useful. There, the coding agent proposes candidate next actions from its ordinary context, and SWE-Trail briefly executes them from the same checkpoint to decide which route continues. We evaluate collection approaches by training student models on the trajectories they produce. For a 124B student initialized from Ling-3.0-flash-base, SWE-Trail improves mean resolution over independent sampling by 2.33 and 1.60 percentage points on SWE-bench Multilingual and SWE-bench Pro, respectively. Without history, the same pipeline produces more resolved trajectories than independent sampling, but improves by only 0.11 points on Multilingual. These results show the value of using history to guide collection without exposing it to the coding agent.

---


### 279. [Decoupled Predictive Decision Making: A Shared Conditional Predictor for Agents](https://arxiv.org/abs/2611.02075)

**<font color=#1a73e8>作者：</font>** Lang Mo, Xingxuan Zhang, Qi Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent decisions depend on empirical relationships that deployment observations reveal and task descriptions alone may leave unresolved. We introduce Decoupled Predictive Decision Making (DPDM), an architecture that formulates heterogeneous agent decisions as conditional prediction with a shared pretrained learner. Language models provide semantic representations of current and historical records, while a general-purpose conditional predictor predicts task-defined targets from the represented evidence. Pretraining supplies reusable inference capability; deployment evidence instantiates problem-specific predictions without updating either model's neural parameters. Tool judgments, candidate preferences, and reasoning assessments share an evidence-and-query interface, with predictions mapped to choices by a decision rule. This architecture establishes complementary sources of agent capability: semantic knowledge acquired through language pretraining and empirical inference acquired through structured-data pretraining. A single frozen LimiX-2 predictor serves all five task categories. With Qwen3.5-27B as the semantic encoder, DPDM raises mean accuracy across 50 benchmarks from 78.80% with few-shot prompting to 84.92% under their respective evaluated history budgets, and reaches 82.33% with identical histories and queries. On ToolPRMBench's BFCL and ToolSandbox tasks, absolute accuracy gains are 34.26% and 28.87%, respectively, at the methods' respective evaluated history budgets. Accuracy improves as history grows. With identical imbalanced histories, mean balanced accuracy improves by an absolute 14.51% across five reasoning-step assessment tasks and four encoders. DPDM makes learning from experience an independently improvable foundation-model capability, creating a shared route for advances in conditional prediction to improve decisions across agent tasks.

---


### 280. [Scene-Adaptive Readout and Decoding in Diffusion Driving VLAs](https://arxiv.org/abs/2611.02076)

**<font color=#1a73e8>作者：</font>** Seungjun Yu, Jiho Choi, Inha Kang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion driving vision-language-action models repeatedly execute the backbone at every denoising stage, incurring substantial inference cost, while it remains unclear whether all scenes require the same decoding computation. To distinguish when a trajectory becomes readable from how much further refinement it requires, we analyze trajectory readout across network depth and decoding progress. We identify a depth-decoding dissociation in which late-layer representations already support useful trajectory readout after the first forward sweep, whereas early-layer representations benefit more from continued decoding. We further find that both the preferred readout layer and decoding depth vary across scenes. Based on these observations, we propose a scene-adaptive readout and decoding framework. A scene-conditioned readout MoE adaptively weights and combines trajectory predictions from layer-specific late-layer representations after a single backbone sweep, while an adaptive decoding policy applies additional native refinement only when required by the scene. We evaluate our framework on two diffusion driving VLAs across the Waymo E2E and nuScenes benchmarks. Our method improves validation RFS by up to 0.56 while also improving test performance, and achieves an end-to-end speedup of up to $6.0\times$ on Waymo E2E, while consistently reducing trajectory error on nuScenes. These results demonstrate that scene-level readout and decoding allocation improves planning quality while avoiding unnecessary decoding. Our code is available at this https URL

---


### 281. [ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and Cost](https://arxiv.org/abs/2611.02079)

**<font color=#1a73e8>作者：</font>** Xingzhi Qian, Sungho Park, Rongyuan Tan 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Harness optimization can substantially improve LLM agents without modifying model weights, but existing methods primarily optimize response quality. Extending them to joint quality--cost optimization introduces a challenge: applying the deployment preference during intermediate updates can prematurely reject candidates that are valuable for later improvements. We introduce ParetoSaddler, which addresses this mismatch by separating intermediate candidate promotion from final deployment selection. At each iteration, an optimizer updates a parent harness to produce a candidate, and then compares the two over repeated executions and uses Bayesian bootstrap Pareto support to promote candidates showing credible progress in either quality or cost. Promoted candidates receive broader development evaluation and remain available as parents for later optimization steps. We evaluate ParetoSaddler on ClawMark and GAIA2 using domain-disjoint splits. On ClawMark, ParetoSaddler improves quality from 70.86\% to 81.35\% while reducing cost from \$1.17 to \$1.01 per task; on GAIA2, it improves quality from 56.22\% to 62.89\% while reducing cost from \$0.78 to \$0.45 per task. The Pareto-selected harnesses also achieve higher quality at lower cost than quality-only harness optimization. Analysis shows that Pareto-aware optimization retains intermediate candidates that would be discarded by deployment preference but can support later improvements, while Bayesian bootstrap screening filters out candidates whose gains are weakly supported across runs.

---


### 282. [Measuring "Success" In the Transition from Pre- to Post-LLM Conversational Agents through the Lens of Interaction & Explanations for Older Adults](https://arxiv.org/abs/2611.02088)

**<font color=#1a73e8>作者：</font>** Tamara Zubatiy, Niharika Mathur, Reina Chan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Conversational agents (CAs) for older adults have moved through at least two distinct eras, split by the emergence of large language models (LLMs) at the end of 2022. The first era was defined by commercial smart speakers such as the original Google Home and Amazon Alexa, built on rigid, rule-based dialogue. Interactions were single-turn, user-initiated and "successful" if and only if a command matched one of a finite set of pre-templated intents. The current era is marked by LLM-powered systems capable of open-ended, multi-turn conversation, with capacity for personalization and foundations for more proactive interaction. This shift has not only transformed what CAs can do for users, but also changed what researchers can measure when it comes to understanding "success" of user interactions with CAs. In this case study, we reflect on over 8 years of research spanning more than 100 participants across multiple field sites to trace how our own working definitions of "success" have evolved. We reflect on two completed bodies of work with pre-LLM CAs and an in-progress study with a post-LLM CA. We discuss how our definition and measurement of success have evolved during this transition and also ask open questions to the community about how to optimally measure "success" in the post-LLM CA era. This research is deeply applied and subject to the messiness of real-world deployments. Our intended contributions are deliberately practical, a combination of methodological considerations and reflection questions to support researchers engaging with this new wave of technologies.

---


### 283. [Bernoulli On-Policy Distillation: Don't Ignore High-Confidence Student Tokens](https://arxiv.org/abs/2611.02093)

**<font color=#1a73e8>作者：</font>** Mingyu Cao, Yaokai Jin, Shiwei Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student language model on its own trajectories using token-level supervision from a stronger teacher. We show that standard sampled reverse-KL OPD systematically suppresses updates to high-confidence tokens, such that their weak gradient contribution does not necessarily imply weak or uninformative teacher supervision. We introduce Bernoulli On-Policy Distillation (Bernoulli OPD), which directly matches the teacher and student probabilities for that token. This yields a bounded probability space correction that preserves teacher-student disagreement while avoiding the additional confidence-dependent suppression induced by vanilla OPD. Fixed-rollout analyses show that Bernoulli OPD substantially restores optimization signal to high-confidence tokens while remaining sensitive to teacher-student disagreement. We further analyze the resulting model behavior through confidence distributions, answer calibration, policy movement, and training dynamics, showing that Bernoulli OPD's gains cannot be explained simply by longer reasoning, larger optimization steps, or more uniform imitation of the teacher. Code is available at this https URL.

---


### 284. [EarthJev: Calibrated, Non-Generative Answers to Natural-Language Questions about Sentinel-2 Land Cover](https://arxiv.org/abs/2611.02096)

**<font color=#1a73e8>作者：</font>** Domenico Benfenati, Antonio Maria Rinaldi, Cristian Tommasino  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models for remote sensing answer questions about satellite images by generating text: every answer costs a decoding loop, has to be parsed back to an option, and comes without a usable probability. We present EarthJev, a 0.8B-parameter model that answers typed questions about multispectral Sentinel-2 patches without generating any token. All 12 bands enter the vision encoder of Qwen3.5-0.8B through a widened input layer initialised from the RGB kernels, and, following the open OneJev recipe, the answer is read from the logits of the option letters at a single position and trained with cross-entropy plus Brier score. Under a pre-specified analysis plan, we compare it with the same backbone fine-tuned to generate the answer and with three multimodal language models fine-tuned with LoRA, all trained on the same 70,890 questions from 5% of BigEarthNet v2.0 and timed in one job on the same GPU; VQA models that classify over a fixed answer vocabulary are reported as a reference for the cost of answering only the questions seen in training. EarthJev answers a question in 19.9 ms, 4.3 to 8.7 times faster than the multimodal language models and 6.8 times faster than its own backbone used generatively; when all the questions about an image are asked together, it answers them in 42.8 ms, 3.7 to 10.1 times faster than the batched generative models. On 36,028 test questions it reaches 86.0% accuracy (three seeds), 0.6 and 1.2 points below the two 2B multimodal models and 3.5 points below the remote-sensing EarthDial-4B, with answers that are valid by construction and calibrated probabilities (ECE 0.006). Replacing the nine non-RGB bands with their mean costs 4.5 points, so the model uses the multispectral input, and in an ablation training the whole vision encoder raises accuracy to 88.4% at the same cost. Code and model: this https URL

---


### 285. [NorthCUA Technical Report: Turbocharging Computer-Use Agents through Experience at Scale](https://arxiv.org/abs/2611.02102)

**<font color=#1a73e8>作者：</font>** Chaoyun Zhang, Bingxuan Li, Pinxue Guo 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling computer-use agents from individual actions to complex software work requires experience that connects decisions to complete outcomes. We present NorthCUA, an integrated system for turbocharging computer-use agents through experience at scale. Its Experience Flywheel supplies diverse executable tasks to the NorthCUA Harness, which sustains long interactions, records decisions, and checks task outcomes. The Flywheel uses these records to curate verified trajectories. For unsolved tasks, recursive self-improvement evolves reusable skills and preserves verified milestones so later attempts build on earlier progress. Staged Learning combines this experience with grounding data from the Flywheel to develop GUI competence through mid-training and long-horizon supervised fine-tuning. The policy then learns from fresh attempts in the same Harness through joint desktop-web reinforcement learning, closing the loop between experience production and policy improvement. The resulting Nano, Mini, and Pro family achieves state-of-the-art results among open-source models across GUI grounding, desktop execution, and Web interaction under the reported evaluation settings. For more responsive Web workflows, NorthCUA-Ultrafast pairs direct action selection with open-ended generation on pre-RL Nano, offering a measured quality-latency tradeoff. Together, these advances establish NorthCUA as a high-performing model family and a reusable foundation for agents that carry complex software work from intent to completion.

---


### 286. [Consolidating Reasoning with Test-Time Training](https://arxiv.org/abs/2611.02104)

**<font color=#1a73e8>作者：</font>** Haotian Wu, Zeming Chen, Hao Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective multi-agent collaboration requires finalizing solutions from reasoning that is distributed across the individual attempts of many agents. However, useful intermediate reasoning can remain unexploited when collaboration is limited to voting on conclusions reached among individual agents, or aggregating long, noisy collections of reasoning trajectories in context. In this work, we propose TTT-Consolidate, a framework that uses multi-agent reasoning trajectories as adaptation data to improve a model's subsequent reasoning. TTT-Consolidate jointly consolidates trajectories into parametric representations through test-time training, then generates a new solution by conditioning on the consolidated information. We meta-learn how to consolidate using bi-level optimization at training time, where an inner loop encodes reasoning trajectories into a lightweight LoRA adapter, and an outer loop learns meta-parameters for the inner loop such that the consolidation is helpful for the model to synthesize a final solution.
As no large-scale corpus of diverse reasoning trajectories exists for training aggregation methods, we construct the OpenParallelThinking corpus composed of 12,810 math problems paired with a mixture of trajectories from six LLMs. Evaluated on challenging math and STEM benchmarks, TTT-Consolidate outperforms the best aggregation baselines by up to 20 percentage points, even under matched compute and runtime settings, with the gap widening at larger model scales. TTT-Consolidate also recovers from unsuccessful individual trajectories more robustly, an ability that improves as the number of available (even incorrect) trajectories increases. Finally, we demonstrate that TTT-Consolidate benefits from both SFT and RL-based outer loop objectives. We will release TTT-Consolidate and OpenParallelThinking for use in future work on reasoning aggregation.

---


### 287. [Order-Only On-Policy Distillation](https://arxiv.org/abs/2611.02112)

**<font color=#1a73e8>作者：</font>** Guangzeng Han, Yu Wu, Xiaolei Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own generations by matching the teacher's token probabilities. These probabilities entangle two kinds of information: which tokens the teacher prefers, and how confident it is. The latter reflects the teacher's own capacity and calibration, which a smaller student may be unable to reproduce. Because the teacher temperature changes these values without changing the ordering, OPD is also sensitive to the temperature choice. We ask whether the teacher's ordering of candidate tokens is enough, and propose Order-Only On-Policy Distillation (O$^{3}$PD). At each student-generated prefix, O$^{3}$PD trains the student to reproduce the order of the teacher's top-$K$ tokens, without fitting their probability values. The objective is therefore invariant to the teacher temperature and needs no temperature tuning. Across six teacher--student pairs, O$^{3}$PD outperforms OPD on the average over HMMT25, AIME24, and AIME25 in every pair, by up to 2.9 points, with gains of up to 5.6 points on AIME25. Other ranking losses yield similar gains, so the benefit comes from ordinal supervision itself. Analysis shows that O$^{3}$PD departs further from the teacher's probabilities than OPD, yet reproduces its ranking more faithfully and yields a stronger student. The ranking, not the probability values, thus carries the knowledge that on-policy distillation needs to transfer.

---


### 288. [FOLLIE: Automated Reasoning over the First Dataset of Sentences with their First-Order Logical Representation for French](https://arxiv.org/abs/2611.02129)

**<font color=#1a73e8>作者：</font>** Maximos Skandalis  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> FOLLIE (for First-Order Logic for Language Inference and Entailment for French) connects French sentences, compositional first-order representations and automated natural language inference (NLI). The first French NLI-ready, NL-to-FOL resource, it contains 19,983 inference records and 36,987 non-empty sentence-slot--formula mappings from six heterogeneous NLI sources, retaining French lexical material and source problem structure. Its silver annotations are produced by a neural--symbolic pipeline, with 111 separately identified LLM-assisted additions. The construction combines morphosyntactic analysis, probability-conditioned categorial multitagging, grammatical proof search, discourse representation and first-order semantic construction. Stage-wise experiments show substantial gains in derivation coverage; analyses of conjunction distributions, logical-operator incidence and scope alternation characterise the resulting resource. We then develop an automatic inference engine whose input-conditioned background theories address lexical relations, quantification, quantities, event structure and temporal dependencies. Prover9 supplies proofs for entailment and contradiction, while Mace4 supports bounded consistency checks. Three-way accuracies are 65.37% on all 335 FraCaS-FR problems, 70.33% on 300 GQNLI-FR problems and 71.35% on 9,399 eligible SICK-FR records pooled across splits. Agreement with reference labels among committed decisions is 93.53%, 100.00% and 98.66%, at commitment coverage of 41.49%, 37.00% and 15.05%, respectively. Worked constructions, axiom schemas and proof analyses explain these outcomes and identify the contributions of scope, reference, lexical knowledge and numerical structure. FOLLIE provides a French experimental basis for studying the representations and assumptions that connect sentence interpretation to deductive inference.

---


### 289. [GatedV: Self-Gated Values for Transformer Language Models](https://arxiv.org/abs/2611.02145)

**<font color=#1a73e8>作者：</font>** Li-Ming Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Standard attention forms query (Q), key (K), and value (V) matrices through learned linear projections of input hidden states. Architectures such as GAU and Mega incorporate nonlinear transformations into attention. In this paper, we propose GatedV, a simple attention variant that applies SiLU only to V before aggregation without introducing additional trainable parameters. We evaluate GatedV against a standard decoder-only Transformer using matched parameter counts, paired initializations, and equal training-token budgets. At 2.33M parameters, GatedV reduces mean held-out perplexity from 59.1 to 57.9 (2.0%), with improvements across all five paired seeds. At 26.16M parameters, following an equal-budget learning-rate search, mean held-out perplexity falls from 20.2 to 19.7 (2.4%), with improvements across all three paired seeds. Small-model ablations show that the tested affine rescaling of values does not fully reproduce GatedV's gains. A short interleaved benchmark on NVIDIA DGX Spark measures approximately 0.7% higher full-context forward latency for the larger model, based on synchronized wall-clock timings. These findings suggest that value-only self-gating can improve language modeling performance without increasing parameter count or redesigning the attention-weighting mechanism.

---


### 290. [Multi-Agent Collusion and the J-Space](https://arxiv.org/abs/2611.02153)

**<font color=#1a73e8>作者：</font>** Marco Molinari, Gabriele Bettineschi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly deployed in Multi-Agent Systems (MAS), and they introduce the risk of coordination among agents that might escape human oversight. The J-space has been used to uncover deception in single LLMs, but its use for uncovering and steering collusion between agents remains unexplored. We show, with interpretability experiments on DeepSeek-V4-Flash (284B) on the NARCBench collusion benchmark, that colluding agents' J-space holds the collusion itself: before replying, 86% of colluders represent misrepresentation, concealment or remorse. In a steganographic card-counting task, the receiver's J-space holds a hidden count, and causal interventions alter its count. We also introduce the Jacobian Pair Contrast (J-PACT), an unsupervised method for detecting collusion between agents. We evaluate J-PACT on four open-weight models: GPT-OSS-20B, Llama-3.3-70B-IT, Qwen3-32B, and DeepSeek-V4-Flash (284B). J-PACT retains 85% of the above-chance AUROC of supervised NARCBench probes, matches them on steganographic scenarios, and names the colluding pair up to its complement in 99% of detected runs.

---


### 291. [Decision Models as Policy Gates for Coding Agents: Explicit Policy Boundaries Improve Detection and Reduce False Alarms](https://arxiv.org/abs/2611.02155)

**<font color=#1a73e8>作者：</font>** James P. Beno  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coding agents can destroy data, leak secrets and message the wrong person faster than a human can review. Could a decision model catch these risks at runtime? We evaluated 22 hosted decision models and two prompted general models as classifiers for a multi-rule policy engine. A synthetic dataset of 2,643 tool calls was labeled blind against 28 rules, with a sealed holdout. With a single shared preamble in both conditions, explicit boundaries written as examples and counterexamples raised recall by 5.5-26.1 percentage points on all 23 available models and reduced false positives on 21. Jev 1.14's recall rose from 89.3% to 98.2%, while unnecessary interruptions fell from 30.6% to 4.8% of 252 clean actions. With examples, its median latency was 120 ms at $0.46 per thousand requests. Strong models retained the recall gains when concrete names were replaced by generic descriptions; three largely retained them when the same boundaries were written as prose. On 16 new scenarios written after the initial studies, a follow-up improved recall on 22 of 23 models and reduced unnecessary interruptions on 21. We release the dataset, rule texts and harness.

---


### 292. [ZeroGraph: Compositional Blockwise Training via Materialized Boundary Supervision](https://arxiv.org/abs/2611.02200)

**<font color=#1a73e8>作者：</font>** Omar Ramadan, Sam Siavoshian, Amir Kashif Saeed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Blockwise learning can remove online gradient dependencies across depth, but independently optimized blocks need not compose into a useful model. We present ZeroGraph, a systems transformation for pretrained-model conversion and distillation that materializes a frozen teacher's coherent boundary trajectory as a versioned dataset. Each partition then trains with disjoint parameters, optimizer state, random state, and checkpoints, replacing live cross-depth dependencies with persistent supervision. Experiments separate learning quality from systems behavior. On GPT-2 Large, an unanchored objective reduces denoising error by 99.44%, yet assembled held-out cross-entropy worsens from 3.63 to 10.48 and context use becomes negative. A six-arm TinyLlama study identifies clean teacher-boundary regression as the successful interface; the tested noisy objective fails with cached or online targets. The clean recipe passes quality and context-use gates across three Qwen2.5-1.5B seeds and on a 3.086B Qwen2.5 model. In an objective-matched comparison, cached and online targets are bitwise identical. Cached jobs are faster after materialization, but a 618.31 s cache-build cost prevents wall-time break-even through 16 measured reuses. Boundary-shift tests show tolerance to intermediate representation mismatch, and an interrupted block resumes to a bitwise-identical final state without rerunning unaffected blocks. In the tested pretrained-model conversion and distillation setting, cross-depth semantic dependence can move from online optimization into persistent data.

---


### 293. [Test-Time Scaling for Open-Ended Reasoning at Small Model Scale](https://arxiv.org/abs/2611.02208)

**<font color=#1a73e8>作者：</font>** Adam Y. Ahmed, Abdullah G. Elafifi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A vote over a model's samples can only help when the samples disagree. For open-ended generation the binding question is therefore not how to combine samples but whether a model produces samples worth combining, a question test-time scaling has answered for math but not for free-form text. We study it at small scale with semantic cluster voting, a judge-free aggregator that groups a small instruct model's samples by meaning and returns the largest cluster's representative, with no reward model or self-judging. On a 250-prompt benchmark with three tiers of answer checkability, the same pattern holds across three model families (Qwen2.5-3B, Llama-3.2-3B, Gemma-2-2B) and two generation seeds: voting raises accuracy on the math control, where samples vary but stay checkable (a gain of +10 to +29 points across the three models), yet adds at most +0.30 judge points on open-ended text. On a larger 200-problem MATH-500 run with the primary model, the math gain is +8.5 points (95% CI [+4.0, +13.0]). Almost every open-ended sample falls into one meaning cluster, so there is little to select over. The collapse is consistent with instruction-tuning rather than model size, and raising decoding temperature does not recover usable diversity, because it costs more quality than it adds (net -0.64 judge points, 95% CI [-0.93, -0.37]).

---


### 294. [Who Should Score the Cache? Mid-Depth Layers Are the Best Judges of KV-Cache Eviction](https://arxiv.org/abs/2611.02230)

**<font color=#1a73e8>作者：</font>** Ekaterina Seregina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Key-value (KV) cache eviction methods rank tokens by attention scores, and each layer scores its own cache. To our knowledge, no eviction method asks which layer should score. We find, across twenty-one models, that the depth of the scoring layer governs eviction quality. On the eighteen models with per-layer caches, spanning 0.5B to 109B, long-context retrieval accuracy collapses at shallow layers, peaks between 0.4 and 0.75 of depth, and degrades at the last layer. The curve arises because a layer judges tokens well only once it has used the question to find the answer, which takes several layers. Modeling eviction as a top-$k$ cut, we compute answer survival probability from prefill attention and reproduce the measured curves. This approach selects the scoring layer using calibration prompts with known answers, and the selected layer is the best layer measured on most models and never significantly below it. It improves on the own-layer default on sixteen of the eighteen models, with significant gains on seven, all at 14B or below, while on larger models the default is already close to the best mid-depth layer. Scoring every cache from the selected layer while keeping one set of tokens for all heads also beats per-head SnapKV by 18 to 43 points on five models up to 14B under tight budgets. This gain carries over to financial filings at 32K context, all at the same memory budget, with no extra forward pass. The same curve explains a penalty in shared-cache models, where several layers read one cache and the layer that writes it scores by default. On Gemma-4-E2B the writer is shallow and loses 28 points to a mid-depth reader at a 10% budget. We also find that in open-book question answering (LongBench) no mid-depth layer beats the own-layer default.

---


### 295. [TIGER: Learning from Researcher Taste to Generate Tailored Research Ideas](https://arxiv.org/abs/2611.02234)

**<font color=#1a73e8>作者：</font>** Shane Gu, Yufeng Lin, Dixi Yao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In pairwise comparisons where each judge chooses between an idea generated by its corresponding TIGER-8B policy and one generated by GPT-4.1, the three LLM researchers select the TIGER-8B idea in 56.6%-68.4% of 76 comparisons per researcher. PhD1 and PhD2 select the TIGER-8B idea in 19 of 30 pairs (63.3%) and 17 of 30 pairs (56.7%), respectively. All six directed cross-policy comparisons likewise favor the judge's matched TIGER-8B policy over an off-target policy, supporting the use of individual preference feedback for tailored research ideation.

---


### 296. [Can LLMs Reliably Evaluate Themselves? A Probabilistic VC Framework](https://arxiv.org/abs/2611.02253)

**<font color=#1a73e8>作者：</font>** Jae Oh Woo, Mengdie Flora Wang, Rahul Ghosh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) find increasing use in critical applications, evaluating their ability to assess their own outputs has become crucial. We present a theoretical and empirical framework that examines whether LLMs can differentiate between correct and incorrect solutions while maintaining properly calibrated confidence. Building on classical Vapnik-Chervonenkis (VC) theory, we adapt it to probabilistic predictors through two complexity metrics: Probabilistic VC (PVC), which measures a model's ability to confidently classify across problem types, and Calibration-aware PVC (C-PVC), which additionally demands alignment between confidence scores and actual success rates. Unlike Expected Calibration Error (ECE) and Actual Error (AE), these measures give an integrated assessment of self-evaluation expressiveness and calibration, with sample complexity bounds and generalization guarantees comparable to classical VC theory. We test eleven 7-8B models on 360 original mathematical reasoning problems, TruthfulQA, and CommonsenseQA. Each model chooses between two of its own generated solutions and reports its confidence, with ground truth determined by an ensemble of larger models. The results show a systematic inverse relationship: models with greater self-evaluation expressiveness have weaker calibration. s1.1-7B and Qwen2.5-7B-Instruct achieve the highest PVC-VUS scores, while JiuZhang3.0-7B is best calibrated, with the lowest ECE and the smallest PVC-VUS gap. The trade-off persists across architectures, training paradigms, and domains, pointing to a fundamental challenge in developing self-reflective LLMs, and our framework offers practical tools for diagnosing it.

---


### 297. [The 3-Tier Integrated Technology Risk Model for Occupational Safety and Health](https://arxiv.org/abs/2611.02257)

**<font color=#1a73e8>作者：</font>** Ramiro Pesina, Ashish Madkaikar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents the 3-Tier Integrated Technology Risk Model, a progressive framework for Occupational Safety and Health (OSH) management that integrates Job Safety Analysis (JSA), dynamic risk assessment using leading and lagging indicators, and predictive analytics powered by Large Language Models (LLMs). The model provides organizations with a structured pathway to evolve from static, reactive safety practices to a sophisticated, predictive safety paradigm. Each tier builds upon the previous one, creating a comprehensive, data-driven approach that enables just-in-time training and preemptive risk mitigation.

---


### 298. [Beyond Binary Detection: Type-Aware Hallucination Analysis and Hierarchical Detection in Financial Question Answering](https://arxiv.org/abs/2611.02258)

**<font color=#1a73e8>作者：</font>** Xiongyu Chen, Sizhen Zhu, Zhuoer Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to answer questions over financial filings, where an unfaithful answer can mislead investment, compliance, or client decisions. Hallucination detectors are a common safeguard, but they are usually evaluated with a single binary score that reveals neither which kinds of errors analysesed nor why. This paper studies hallucination detection on PHANTOM, a long-context benchmark built from SEC filings, at the level of hallucination type. We first analyze 15,443 paired hallucinated and faithful answers without any detector and find that hallucinated answers are more than twice as long as faithful ones, and that lexical grounding separates the two classes only because faithful answers are bimodal. We then generate hallucinations in nine financially motivated categories, confirm each with a separate verification pass, and diagnose an LLM-based detector on 4,086 usable examples. Generation success varies from 66.3% to 100% across categories. The detector reaches 80.2% binary accuracy but only 44.7% subtype accuracy, never assigns two of the nine categories, and misses between 5.3% and 46.8% of hallucinations depending on category; these misses are unrelated to input length but rise with how far an answer departs from the correct one. Guided by this diagnosis, we propose a two-stage hierarchical detector that first decides whether an answer is hallucinated and then assigns a subtype, raising binary accuracy to 95.6% and subtype accuracy to 56.1%. The results show that type-level evaluation exposes detector weaknesses that aggregate metrics conceal.

---


### 299. [Current state of LLMs for Arabic dialectal machine translation](https://arxiv.org/abs/2611.02271)

**<font color=#1a73e8>作者：</font>** Josef Jon, Rawan Bondok, Ondřej Bojar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This work presents an evaluation of large language models (LLMs) for English to dialectal Arabic machine translation on the MADAR dataset. We evaluate both translation directions (English to Arabic and vice-versa) on 16 Arabic dialects. Our experiments cover a diverse set of models, including specialized Arabic models (Jais, Nile), multilingual models (Gemma, Command-R, Mistral, Aya), and commercial APIs (GPT-4.1). We employ multiple evaluation metrics: BLEU, CHRF, COMET (both reference-based and reference-less variants) and GEMBA (LLM-as-a-judge), as well as a small-scale manual evaluation, to assess translation quality. We discuss the challenges of automatic MT evaluation, especially in the context of Arabic dialects. We also evaluate the ability of LLMs to classify the dialect used in a text. The study offers insights into the capabilities and limitations of current LLMs for dialectal Arabic machine translation, particularly highlighting the difficulty of handling dialectal diversity, although the results may be influenced by possible training data contamination, which is always a concern with LLMs.

---


### 300. [When the Text Is Silent: Memory Shortcuts and the Validity of LLM Annotation under Evidence Insufficiency](https://arxiv.org/abs/2611.02273)

**<font color=#1a73e8>作者：</font>** Wenchang Wang, Yue Song  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to annotate text for social science research, content moderation, and training data. Their broad knowledge of real-world entities raises a concern: when labeling a text, do they rely on its evidence or substitute what they already know? We call this behavior a memory shortcut and examine when it emerges, what amplifies it, and how to mitigate it. Using 995 widely recognized public figures and four matched control names per figure, we construct counterfactual texts that separate textual evidence from prior knowledge, and evaluate three commercial LLMs on 121,594 prompts each across five stages. We find a striking asymmetry. Although all models recognize nearly every figure, none follows memory over the text when the two conflict. Shortcuts instead emerge when evidence is absent: for one model, famous names raise the rate of remembered occupations, ages, and countries by 17.0, 14.9, and 6.8 percentage points relative to synthetic names. These effects occur only for recognized figures, and 98.6% of the resulting labels are factually correct about the namesake while none is supported by the text. Evaluation threats and answer-contingent rewards amplify shortcuts by 8.7 and 12.4 points. Famous names also raise leadership ratings of sparsely documented applicants by 0.22 and 0.28 points in two models. A namesake reminder and name masking each eliminate the shortcuts, with trade-offs in gender annotation. LLM annotations can thus be factually correct yet methodologically invalid. Trustworthy LLM annotation requires audits that test evidence absence, account for incentives in annotation instructions, and evaluate the attribute-specific trade-offs of mitigation.

---


> [!TIP]
> 当前位于：**251-300**（第 6/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
