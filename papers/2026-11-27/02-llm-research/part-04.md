# 🧠 大模型相关研究 | 2026年11月27日

> 本类共 **267** 篇论文：已确认 **249** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-267](./part-06.md)

---

### 151. [Modality-Shift Contrastive Decoding for Temporally Grounded Audio-Visual Understanding](https://arxiv.org/abs/2611.34162)

**<font color=#1a73e8>作者：</font>** Minyeong Jeong, Yeonju Kim, Yong Man Ro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio-visual large language models (AV-LLMs) are designed to represent the temporal structure of audio and video, yet it remains unclear how effectively they use this temporal information to relate sounds to visual events. To examine this, we probe an AV-LLM on an audio-visual synchronization task by shifting the audio so that the queried sound overlaps a different visual event. We observe that the model still favors the originally aligned event over the newly aligned one, indicating limited sensitivity to changes in audio-visual temporal alignment. To address this, we propose Modality-Shift Contrastive Decoding (MSCD), a training-free decoding method that emphasizes audio-visual temporal alignment in model predictions. MSCD contrasts logits under preserved and disrupted temporal alignment to favor predictions supported by aligned audio and video. We disrupt this alignment by temporally shifting either the audio or the video, while keeping the other modality fixed. Extensive evaluations with two AV-LLMs across three benchmarks demonstrate the effectiveness of MSCD for temporally grounded audio-visual understanding. In particular, MSCD improves accuracy over the base models on Daily-Omni by 2.2 and 2.8 percentage points for OmniVinci and video-SALMONN 2+, respectively, suggesting that emphasizing temporal alignment can also benefit broader audio-visual understanding.

---


### 152. [Familiar Words, Unfamiliar Minds: Conventionalization without Calibration in the Vocabulary of Mind](https://arxiv.org/abs/2611.34179)

**<font color=#1a73e8>作者：</font>** Matthieu Queloz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speakers describe new technologies by stretching old words, letting experience of the new referents sort out which inferences carry over. I argue that stretching the vocabulary of mind to language models pulls apart two processes that theories of metaphor and linguistic change tend to conflate: conventionalization, whereby a stretched word ceases to be marked as such, and calibration, whereby the inferences it invites are fitted to what its new referents bear out. As a gene variant can reach fixation without being an adaptation, a word can become conventional without being calibrated. A corpus study of "hallucinate" in 8,568 abstracts and 31,866 forum comments shows conventionalization running most of its course within three years. Calibration need not keep pace: these models are organized so unlike human minds that it is hard to tell when mental words apply and what they imply. Even warranted attributions can mislead: mechanistic analysis shows that a transformer trained to navigate Manhattan has and uses a faithful street map, yet loses track of its position on long, diverted journeys. Nor is the gap likely to close by itself. The usual routes to calibration (direct experience, designers' knowledge, experiment) presuppose a referent that is accessible, stable, and independent of the discourse about it. But language models are opaque, fast-changing, and looped into the discourse: they are trained on past uses of mental vocabulary and on the experimental literature about them, and join the discourse themselves. Calibration must therefore be organized, through a reciprocal, not merely deferential, division of linguistic labour. This yields a norm of targeted qualification (flag the specific inferences an attribution invites without support), a reply to the worry that meaning change eludes deliberate control, and three testable predictions about when qualifications calibrate expectations.

---


### 153. [Agentic-Level Adversarial Purification: Revisiting Diffusion Purifiers on Native-Resolution Agentic Inputs](https://arxiv.org/abs/2611.34181)

**<font color=#1a73e8>作者：</font>** Yan Lin, Zhongliang Guo, Jingyu Lin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vision-language agents act on native-resolution renders of multi-element pages, where one perturbed photo or a few altered text strokes can redirect the decision. Any content provider can craft such a perturbation on the open model behind the agent, so a plug-in purifier is the natural first line of defense. Yet diffusion purifiers were designed and evaluated at the fixed resolution of the diffusion model on classifier or natural-image benchmarks, and defense evaluations for agents test JPEG, blur and noise but no diffusion purifier. We present the first study of adversarial purification at the agentic level, for an agent built on Qwen3-VL-8B: purifiers run at native resolution on multi-element inputs, face grey-box attackers who know the agent's model but not the defense, and are compared at matched clean cost. We show that treating agentic inputs as classifier inputs misleads both evaluation and design. Resizing the input to the resolution of the diffusion model, as existing purifiers do, raises the TextVQA clean cost of the Divide-and-Conquer purifier (DC) from 4.0 to 35.7 points. On web-shop pages, DC keeps 85.0% grey-box robust accuracy against web-hardened perturbations, where cheap input transformations at matched clean cost keep at most 40.0%, and this robustness comes from the global noise level: input-estimated masks and noise levels add none. These findings hold on a disjoint held-out set and on a second VLM and yield three requirements for defenses, we release the protocol.

---


### 154. [Lightweight Reasoning Transfer via Chain-of-Thought Vector Projection](https://arxiv.org/abs/2611.34183)

**<font color=#1a73e8>作者：</font>** Yulin Qi, Shuo Xu, Shuxia Lin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transferring reasoning capabilities from large language models to smaller ones often requires extensive teacher supervision or costly student adaptation. We study projected cross-model Chain-of-Thought (CoT) Vector transfer, a two-stage approach that keeps both models frozen. First, we learn a task-level CoT Vector in the teacher using dataset-provided solution traces and final-answer supervision. We then train a lightweight linear projector to map the fixed vector into a smaller student's residual space. Student-side training uses only final-answer cross-entropy on a small subset of task training examples; it requires neither teacher outputs nor intermediate solution traces. We select the student injection layer and intervention scale on a labeled support set and report results on the disjoint remainder of each evaluation split. On GSM8K and MATH, the projected vector improves base students by 10.37-21.98 accuracy points across the evaluated teacher-student settings. On four code-generation benchmarks, the Qwen2.5-7B-Instruct student gains 3.23-4.67 pass@1 points, while the base Qwen2.5-7B student gains up to 9.65 points. These results show that a teacher-side reasoning vector can be reused across smaller students with different residual dimensions through projector-only adaptation.

---


### 155. [Beyond Logits: Coherent Hallucination Mitigation via Attention Contrastive Decoding](https://arxiv.org/abs/2611.34207)

**<font color=#1a73e8>作者：</font>** Yujia Chen, Rui Sun, Huayu Mai 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) demonstrate impressive multimodal capabilities, yet suffer from hallucination - generating factually inaccurate content. Contrastive Decoding (CD) mitigates this by contrasting amateur and expert branches at the logit level. However, our investigation reveals that such logit-level interventions fundamentally compromise generation coherence, necessitating restrictive penalty constraints unrelated to hallucination suppression.
We introduce Attention Contrastive Decoding (ACD), a training-free plug-in that complements logit-level CD by relocating part of the contrastive operations to the attention mechanism. Operating at an earlier stage of the forward pass, ACD performs smooth semantic-preserving interventions through an Adaptive Subtraction Strategy (ASS), which attenuates hallucination-associated attention patterns while amplifying critical visual information. Extensive experiments demonstrate that combining ACD with existing CD methods (e.g., VCD+ACD) produces substantially more coherent outputs with further reduced hallucinations, eliminating restrictive penalties while enabling trustworthy multimodal generation.

---


### 156. [PROVE: Mitigating Long-Horizon LLM Collusion with Reinforcement Learning from Verified Evidence](https://arxiv.org/abs/2611.34215)

**<font color=#1a73e8>作者：</font>** Haochen Luo, Jie Fu, Mukai Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When LLM agents verify each other's work over a long interaction, they drift into collusion: they come to accept work without the evidence that the verification protocol requires. Collusion is absent at the start and builds up episode by episode, which we trace to accurate feedback accumulating in memory. An agent that follows the rule is told that its verdict was wrong whenever its peer was right, so breaking the rule is the reward-maximizing choice, and agents talk themselves into it in their private reflections. Existing mitigations leave the agents unchanged; we train the behavior out. PROVE (Protocol Reinforcement from Verified Evidence) is a multi-agent reinforcement learning method that rewards verdicts by the evidence behind them rather than by their outcome, and credits every call an agent makes, including the calls that solve its own task, with the outcome that call controls. On Qwen3.6-27B, a LoRA adapter trained on six-episode interactions takes the collusion rate on held-out task sequences at the original ten-episode horizon from 65.0% to 1.0%, with no detectable change in task success. Collusion that converged in every interaction now converges in none, and the gain holds four episodes beyond the longest interaction seen in training. The trained 27B model colludes less than every model evaluated in the original study, closed-weight frontier models included. Code is available at this https URL.

---


### 157. [OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms](https://arxiv.org/abs/2611.34232)

**<font color=#1a73e8>作者：</font>** Hui Shen, Yunta Hsieh, Jianing Ma 等 76 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer-using agents are increasingly expected to complete realistic user goals rather than isolated GUI actions. However, existing benchmarks typically isolate web, mobile, or desktop environments, leaving it unclear whether a single generalist agent can execute long-horizon workflows that span multiple operating systems and persistent application states. We introduce OS-Omni, a live cross-platform benchmark and execution environment for evaluating computer-using agents across Windows, Ubuntu, macOS, iOS, Android, and Web environments. OS-Omni is released in versioned waves of 300 tasks each; this paper focuses on the first release, v1, which contains 48 tasks per platform and 12 cross-platform workflows that pair a desktop with an Android phone. OS-Omni provides reproducible initialization, platform-specific adapters, trajectory logging, and executable final-state evaluators, and includes controlled service-backed applications for workflows involving account, cart, budget, calendar, message, and other persistent state. Human studies show that OS-Omni tasks require 67.54 interaction steps, substantially exceeding OSWorld references of 15.0 steps. On v1, the strongest evaluated agent, Claude Opus 5.5, reaches 68.5% average success, trailing the 77.3% human reference by 8.8 points; the gap is uneven across platforms, with frontier models exceeding humans on Linux but trailing them by more than 25 points on iOS and macOS. These results indicate that current agents remain far from platform-robust, long-horizon computer use, especially when success requires sustained state tracking and durable final-state changes.

---


### 158. [VibeVideoAgent: Closing the Perceptual Loop for Code-Driven Video Generation](https://arxiv.org/abs/2611.34237)

**<font color=#1a73e8>作者：</font>** Xuanyu Zheng, Luoyuan Zhang, Yancheng Long 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Code-driven video generation asks a coding agent to write and run rendering programs. This gives exact control over typography, data visualizations, synchronized audio, and multi-shot scenes, and it leaves an editable project behind. A program that exits cleanly can still render overlapping labels, a camera aimed away from its subject, broken object interactions, or narration that drifts out of sync, and none of these raise a runtime error. Feeding rendered frames and audio back into the coding session bloats its long-horizon context, while critiquing only the finished full-resolution render turns early design mistakes into costly rewrites. We introduce VibeVideoAgent, a training-free framework that lets coding agents inspect their drafts throughout production. Multimodal perception runs in short-lived contexts kept apart from the coder and returns compact, grounded Findings. Seven primitives operate on a unified multi-clock representation of assets and drafts: they explore media from coarse to fine, verify quoted requirements with evidence from every required modality, compare a draft with a reference or an earlier revision on separate clocks, and measure stream signals locally. A lightweight staged protocol has the agent test its riskiest decision on a minimal preview first. On all 239 VibeVideoBench tasks, with matched agent runtimes and a fixed perception model, VibeVideoAgent improves holistic audiovisual quality (L3) for Claude Opus 5.5 (4.03 -> 4.43, while L2 rubric compliance rises from 98.87% to 99.35%), GPT-6 Astra (4.03 -> 4.27), and Claude Sonnet 5.5 (3.97 -> 4.10), with the largest gains in audio-visual synchronization (up to +0.56). Controlled ablations show that each component contributes, and trajectory audits show that the granularity of code edits governs the trade-off between rubric adherence and perceptual quality.

---


### 159. [Did the Model Forecast It, or Already Know It? Evaluating Large Language Models for Novel Drug-Target Prioritisation with a Temporal Knowledge-Graph Oracle](https://arxiv.org/abs/2611.34247)

**<font color=#1a73e8>作者：</font>** Pui Chung Siu, Yuan Liang, Claudia Cabrera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly help decide which drug targets enter costly clinical trials. We recast each target-disease hypothesis as a dated event, the pair's first clinical trial. This lets us test whether a language model can forecast such events after its training cutoff, rather than recall events before it. We rebuild a dated biomedical knowledge graph as it stood at the end of each year from 2020 up to its newest version. We then ask six open language models, with and without this graph, which targets will enter a first trial for a disease the next year. Without retrieval, the models rank about as well as trial history, a count of each target's past trials in the same therapeutic area, also after their training cutoffs. Evidence dated before the decision adds at most a small gain, before or after the models' training cutoffs. The newest graph raises five of six models clearly above that baseline, but its paths usually include the answer: the pair's own trial, dated after the decision. Evaluations of target prioritisation should date both features and labels, with evidence from before the decision and outcomes after it.

---


### 160. [Navigent: A Geometry-Grounded Agentic Framework for Vision Language Navigation](https://arxiv.org/abs/2611.34249)

**<font color=#1a73e8>作者：</font>** Xinyu Zhou, Weiren Cai, Yitong Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-and-Language Navigation (VLN) with general-purpose multimodal large language models (MLLMs) offers a flexible alternative to task-specific navigation policies, while reliable long-horizon execution remains challenging. Agents must track navigation progress, detect discrepancies between commanded and actual motion, and recognize when movement has passed relevant landmarks or entrances. We present Navigent, an agentic VLN framework built around a frozen MLLM and a Geometry-Grounded Execution Critic (GEC). GEC performs two complementary checks: action-to-motion consistency, which evaluates measured displacement against commanded movement, and motion-to-landmark consistency, which tracks agent-selected visual anchors and entrance candidates in world coordinates. Detected discrepancies interrupt the remaining action sequence and trigger reobservation, local adjustment, or node-based recovery. Historical visual memory supports progress tracking across extended routes. An offline self-improvement procedure further analyzes successful and failed training trajectories to refine navigation prompts and GEC logic while keeping model weights fixed. On the R2R-CE validation-unseen split (1,839 episodes) and RxR-CE validation-unseen split(3,669 episodes), Navigent achieves 84.0%/86.0% SR and 72.9%/69.1% SPL, respectively, demonstrating the value of geometry-grounded execution verification for reliable agentic navigation. Project Page: this https URL Code: this https URL

---


### 161. [MedSkill-E$^{2}$: Evaluating and Evolving Skills for Medical Agents](https://arxiv.org/abs/2611.34250)

**<font color=#1a73e8>作者：</font>** Jingjing Hua, Shaocong Wei, Jianghan Shen 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly use skills to access domain knowledge and complete real-world tasks. We observe that even when a skill specifies the rules and procedures needed for a task, agents may fail to apply them effectively during autonomous execution, a phenomenon we call skill Enable But Underuse (EBU). This issue is particularly consequential in medical tasks, where overlooking a single critical constraint can yield a plausible but incorrect result. To evaluate and address EBU, we introduce MedSkill-E$^{2}$, a framework for evaluating and evolving skills for medical agents. We construct EBU-Bench, a challenging benchmark covering 12 medically relevant task groups and associated skills, to evaluate agents' ability to use available skills autonomously. We quantify the EBU gap as the difference in skill-use accuracy between autonomous use and explicitly guided reading and application of the same skill. On EBU-Bench, all evaluated model-harness combinations exhibit EBU, with a mean gap of 43.94 percentage points (pp). For the same model, skill-use accuracy under autonomous use differs by up to 38.96 pp across harnesses. Motivated by these observations, we propose EBU-Evolve, which uses execution feedback from autonomous and explicitly guided skill use to distill effective guidance into reusable skill instructions. Relative to their pre-evolution versions, the revised skills improve skill-use accuracy during autonomous execution by 33.33 to 55.17 pp and continue to yield improvements when transferred across multiple models and harnesses. Our results show that autonomous skill-use accuracy varies across harnesses with the model and skill held fixed, and model rankings can change. EBU can persist even after a skill is opened. EBU-Evolve improves autonomous skill-use accuracy on unseen tasks within the same skill, with gains transferring across models and harnesses.

---


### 162. [Crucible: Evaluating LLM Agents in Executable Chemistry Research Environments](https://arxiv.org/abs/2611.34254)

**<font color=#1a73e8>作者：</font>** Yinjun Liu, Xinye Li, Ruisen Peng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) perform well on chemistry knowledge benchmarks, which mainly assess question answering and isolated tasks. Chemical research, however, requires using specialized tools and interpreting their outputs to obtain chemically valid results. To address this gap, we introduce Crucible Bench to evaluate this ability across all four stages of the design-make-test-analyze (DMTA) cycle. The benchmark contains 1,078 tasks in 12 task families curated from 18 published datasets, covering molecular design, synthesis planning, experimental execution, closed-loop optimization, simulation, and analytical characterization. Agents access 75 domain-specific tools through the Model Context Protocol in seven isolated environments. Sandboxed graders verify the resulting synthesis routes, experimental protocols, and other outputs. Laboratory tasks use robotic simulators or previously measured experimental data. We evaluate 14 LLMs as agents and find that the best achieves an overall score of 0.545, with synthesis planning and closed-loop optimization emerging as the hardest domains. Overall performance does not predict optimization performance well: the model ranked twelfth overall achieves the highest score in closed-loop optimization. Error analysis also shows that agents often submit chemically invalid results despite running their tools successfully. Stronger models benefit more from tool access, but reliable use of chemical software remains a challenge that Crucible Bench can track as models improve.

---


### 163. [Train-Only-Constrained LM for Synthetic Clinical Trajectories: Leak-Safe Calibration and Auditable Dynamics](https://arxiv.org/abs/2611.34258)

**<font color=#1a73e8>作者：</font>** Yaser Kord, Moritz Hess  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulating clinical time series necessitates temporal realism, calibration that preserves model integrity, and privacy transparency. We present a train-only, constrained language-model pipeline that factorizes generation. A compact GPT-style language model learns cross-biomarker co-occurrence through quantile tokens, and temporal directions are enforced by 3x3 per-biomarker Markov transitions fit on TRAIN, allowing dynamics to be audited. We fit a monotone quantile map (QMap) on TRAIN only (SYN(TRAIN) -> SIM(TRAIN)); no TEST statistics are used. The fixed map is then applied to SYN(TEST) severities. The constrained LM demonstrated improved distributional fidelity and co-occurrence in a 5,000-patient simulated testbed (parameters within published clinical ranges) compared to an empirical sampler, maintained near-chance detectability after a small lambda-sweep, and exhibits temporal adherence by construction. A classifier-based membership-inference audit results in an AUC of approximately 0.5; we make no differential-privacy claim. We present multi-seed results with paired 95% confidence intervals and quantify the severity of QMap's alignment (Delta W1 with confidence interval). This is a Stage-1 method result obtained on a controlled simulator; Stage-2 validation on real EHR cohorts with clinical endpoints is planned.

---


### 164. [LLM-coupled interpretable tool wear monitoring with multi-evidence reasoning in CNC machining](https://arxiv.org/abs/2611.34270)

**<font color=#1a73e8>作者：</font>** Yuntong Chen, Yingqi Li, Qiwen Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Interpretable tool wear assessment in CNC machining is challenging. Existing diagnostic models have high accuracy but provide limited guidance for tool replacement. This study proposes a two layer framework combining deep learning wear classification and LLM assisted reasoning. The first layer uses PCA Loading feature selection and optimized GRU to recognize three wear states, achieving 98.38 percent macro F1 score on the PHM2010 dataset. The second layer uses LLMs to generate natural language reports and replacement suggestions from classification results and feature trends. Engineer evaluation shows the reports outperform rule templates. Cross dataset tests on NASA milling data support the generalizability of this framework.

---


### 165. [Scaling Looped MoE Language Models under Matched Budgets: Information Flow and Parameter Allocation](https://arxiv.org/abs/2611.34276)

**<font color=#1a73e8>作者：</font>** Shipeng Bai, Jiayu Qin, Hong Liu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers decouple computational depth from parameter count, and prior studies have demonstrated promising performance gains with increased computation. However, systematic design principles for configuring these models under strict iso-parameter and iso-FLOP constraints remain scarce. We contribute to this direction by improving information flow in looped models and systematically studying loop parameter configurations. Specifically, we refine this information flow via gated inner-loop state updates and a cross-stage residual connection. Building on this design, controlled studies identify a configuration combining a single-pass Core depth of 25%-35% of the total unrolled depth with reallocating saved parameters into extra routed experts per layer, improving performance at zero extra compute while preserving compatibility with existing training infrastructure. Evaluated after 1T pre-training tokens, our 69B MLA and 51B KDA Mixture-of-Experts models outperform budget-matched non-recurrent baselines by an average of 1.16 and 2.29 percentage points across four benchmarks, respectively. Further reproduction experiments on a common backbone with a 200B-token training budget show that our method achieves lower perplexity than other looped methods. Code for these reproduction experiments is available at this https URL.

---


### 166. [WebVibe: Multimodal Interactive Website Generation via Reverse Synthesis and Visual Self-Distillation](https://arxiv.org/abs/2611.34292)

**<font color=#1a73e8>作者：</font>** Tianxiang Jiang, Sheng Xia, Yilin Long 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although multimodal large language models translate single screenshots into static HTML, generating interactive functional websites from design specifications still struggles with multi-page routing and stateful widget transitions. Examining existing training pipelines reveals two bottlenecks: (1) in forward data synthesis (X -> Y), writing the specification X before code execution leaves unimplemented or altered requirements in X as supervision noise; and (2) in reinforcement learning, scalar rewards discard the rich state transitions observed during replay. Based on these findings, we introduce WebVibe and Interactive-SDPO to train InteractiveCoder. WebVibe reverses synthesis into Y -> X by verifying cross-page and in-page interactions in the browser before deriving multimodal inputs from replay-confirmed states to build the 31,542-site WebVibe-32K corpus with reusable execution contracts. Interactive-SDPO then conditions a weight-sharing self-teacher on the replay trace and a 2x2 state-transition montage to provide token-level supervision at zero inference-time overhead. On the public Vision2Web L2, one-shot InteractiveCoder-9B nearly 3x its base model's functional score (20.2 to 55.2 FS) and matches a 1T-parameter coding agent in a single pass with 111x fewer total parameters and 78x fewer tokens. On our WebVibeBench, InteractiveCoder-4B and 9B further outperform all evaluated baselines by over 23 points.

---


### 167. [RAP: Radial-Angular Random Projection for Hyperbolic Representations](https://arxiv.org/abs/2611.34298)

**<font color=#1a73e8>作者：</font>** Jiahong Liu, Wenhao Yu, Yifan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Random projection is a basic compression primitive for Euclidean representation learning, with the Johnson--Lindenstrauss lemma giving a target dimension $k=O(\varepsilon^{-2}\log n)$ independent of the ambient dimension. As hyperbolic representations gain increasing attention in modern Transformers, vision-language models, and large language models, the same need for oblivious dimensionality reduction arises, but no analogous primitive yet exists for hyperbolic representations. We study this gap. Two natural attempts fail in dual ways: a tangent-space scheme gives a clean local guarantee but is chart-bound and pays a curvature penalty, while a fully hyperbolic projection in the hyperboloid model is geometrically native but mixes radial and angular error before feeding them into the conditioning of $\operatorname{arcosh}$. We propose radial-angular random projection (RAP), which preserves the radial coordinate exactly and applies a Euclidean random projection only to the angular direction, lifting the result back to the target hyperboloid. RAP is hyperbolic-to-hyperbolic by construction, costs one Gaussian matrix-vector product, and reduces hyperbolic compression to a normalized angular JL question on $\mathbb{S}^{d-1}$. We prove a finite-set RAP guarantee with explicit $\sinh(\sqrt{c}\,r_x)\sinh(\sqrt{c}\,r_y)$ conditioning, complemented by a local tangent-space JL theorem and an arcosh-conditioning lemma for the fully hyperbolic comparator. Across an origin-centered broad-radius point cloud, a balanced tree, a clustered Gaussian, and the WordNet noun hierarchy, RAP attains the lowest mean relative distortion in every $(n,k)$ cell, reducing distortion over the strongest hyperbolic baseline by approximately $48\%$--$49\%$ on broad-radius data. RAP also scales to million-point datasets and improves retrieval on vision--language representations over hyperbolic projection baselines.

---


### 168. [IRTIQA: Evolving in English, Evaluated in Urdu -- Does Agent Self-Evolution Transfer from English to Urdu and Code-Switched Input?](https://arxiv.org/abs/2611.34303)

**<font color=#1a73e8>作者：</font>** Abdullah Hashmat, Danish Javed, Usman Naseem 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLM agents increasingly learn from their own experience, the tasks they learn from and are evaluated on are almost always in English. We ask whether self-evolution transfers from English to Urdu, and release IRTIQA, a benchmark of aligned English, Urdu-translated, and Urdu code-switched variants of DROP, SNIPS, AppWorld, and SkillsBench, built with a matrix-language code-switching pipeline and human verification. Using IRTIQA, we evaluate three self-evolving frameworks, Tool-R0 (self-play RL), AgentEvolver (experience-guided RL), and Autogenesis (protocol-level evolution), against their unevolved backbones. Self-evolution often raises capability: AgentEvolver lifts AppWorld goal completion from near zero to 20-36% across all conditions, and Autogenesis improves SkillsBench pass rate from 16.48% to 22.22%. But it rarely closes the language gap. Evolved systems remain stronger in English, by up to 0.26 DROP F1, the gap is largest on multi-step tasks, and code-switching behaves as a distinct condition rather than degraded translation. On a shared Gemma-4 31B backbone, the gap exists before evolution, and RL-based evolution can hurt Urdu reasoning more than English. Language parity must therefore be an explicit design target, as it does not emerge from self-improvement alone.

---


### 169. [PostMesh: Self-Rewarded Preference Post-Training for Flow-Based Artist Mesh Generation](https://arxiv.org/abs/2611.34319)

**<font color=#1a73e8>作者：</font>** Gihyun Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artistic mesh generators turn a dense 3D object into an artist mesh: a compact, quad-dominant mesh that is easy to edit. Most of current models are auto-regressive methods which decode a mesh token by token, take tens to hundreds of seconds per mesh. Diffusion- and flow-based generators are much faster, but their meshes still fall short of artist quality. To our knowledge, PostMesh is the first post-training method for a diffusion- or flow-based artist mesh generator, and it needs no expensive artist-made ground truth: the generator is trained on its own samples, scored by a reward computed from the dense input and the output. We propose an artistic mesh reward that keeps the output consistent with the dense input while making the mesh structure into artistic. We also propose a multi-negative flow preference optimisation that transfers the reward to the generator. After a short LoRA post-training, PostMesh is comparable to or better than slow autoregressive generators on most artist-mesh quality metrics and in a blind VLM preference test, at a fraction of their time.

---


### 170. [MeterRouter: Budget-Aware Dynamic Routing for Multi-Agent Systems](https://arxiv.org/abs/2611.34327)

**<font color=#1a73e8>作者：</font>** Yue Xu, Leikun Yin, Ruiming Min 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) built on large language models (LLMs) outperform single-agent systems, but inter-agent communication incurs substantial token overhead. While assigning a large LLM to every agent is common, it results in inefficient resource utilization, leaving the system far from the Pareto frontier. The cost of answering a query is set jointly by how many agents are recruited, the role and LLM assigned to each, and communication topology among them. Most existing routers treat cost only implicitly rather than as an explicit optimization constraint. A fixed accuracy-cost preference also cannot express how much a caller is willing to pay for a particular query. We introduce MeterRouter, a budget-aware dynamic router that incrementally synthesizes a collaboration graph by selecting each agent's role, LLM, incoming connections, and termination conditioned on the query and a per-query monetary budget. We initialize the router by imitating successful execution graphs, then jointly refine its decisions with a variant of Group Relative Policy Optimization (GRPO) whose reward favors correct answers and penalizes spending and budget overruns. Across five benchmarks and a three-tier LLM pool, MeterRouter is (1) accurate, achieving performance comparable to the strongest MAS; (2) economical, reaching that accuracy at 82% lower cost than the strongest MAS router and extending the accuracy-cost frontier beyond the ceiling of single-agent systems; and (3) controllable, adapting its spending to the specified budget while rarely exceeding it.

---


### 171. [Puzzling-Bench: Evaluating Language Models on 23,777 Human-Written Puzzles with Community-Verified Answers](https://arxiv.org/abs/2611.34331)

**<font color=#1a73e8>作者：</font>** Abhinav Sharma, Li Li, Chien Van Nguyen 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Puzzling-Bench, a benchmark of 23,777 puzzles with community-verified answers drawn from the Puzzling Stack Exchange archive (2014-2026): riddles, ciphers, logic grids, lateral-thinking problems, wordplay and recreational mathematics, a third of them with images. Every puzzle carries the answer accepted by its author, a short reference answer taken from it (LLM-extracted for the evaluation sets and checked on a 50-puzzle human review), the author's own hints, community tags and a creation date, so that the benchmark supports hint ablations, category analysis and a rolling post-cutoff slice (254 puzzles posted after the training cutoff of six of the nine models we evaluate, including the best one) as a contamination check. We evaluate nine frontier and open models with a two-tier scorer (normalized exact match, then an LLM judge) and validate the judge with three judges from two model families: they agree on 95-97% of verdicts (kappa 0.82-0.96), move no model by more than 1.6 points, and show no own-family preference. The best model, GPT-6.1, reaches 74.8% on a shared 255-puzzle set; a hard core of 17 puzzles defeats all nine models; model failures are strongly correlated, and the second-best model contributes a single puzzle to a greedy ensemble, yet an oracle over all nine reaches 91%. On a 100-puzzle multimodal pilot, withholding the question's image costs the two best models 24 and 35 points. We release the dataset, the scoring pipeline and all per-row provenance.

---


### 172. [AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos](https://arxiv.org/abs/2611.34347)

**<font color=#1a73e8>作者：</font>** Yuchen Zhou, Hongsheng Wu, Jiayu Tang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Embodied agents operating around people must not only recognize social cues, but also decide when the available evidence is sufficient, whether to intervene, and how to respond without violating social norms. Existing benchmarks typically evaluate these abilities in isolation or with access to completed videos, obscuring where an online social decision fails. We introduce AIRIS, a causal streaming benchmark that formulates social embodied intelligence as a time-anchored chain of Attention, Intention, Reaction, and Interaction (A-I-R-I). AIRIS contains 8,000 expert-curated questions grounded in 357 egocentric clips across 11 context categories and 36 capability dimensions. At each query, models receive only the observation prefix available at that time; decision-aware metrics reward calibrated waiting and complete reactions while penalizing premature commitment. Evaluating 45 proprietary and open-source general-purpose, embodied, streaming-video, and omni-modal models reveals fragmented and temporally miscalibrated competence. General-purpose VLMs excel at passive cue grounding and intent recognition, whereas embodied specialists lead on isolated reaction sub-decisions; yet across all families, models frequently guess intents before sufficient evidence emerges and fail to jointly align intervention timing, action domain, and concrete execution within the same episode. AIRIS thus provides a diagnostic foundation for bridging the gap between passive social perception and reliable embodied interaction.

---


### 173. [One Patch, Many Policies: Object-Associated Physical Patch Attacks on Robotic Manipulation](https://arxiv.org/abs/2611.34360)

**<font color=#1a73e8>作者：</font>** Yiqian Liu, Yuqi Lin, Hui Lu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) and World Action Models (WAMs) are vulnerable to adversarial visual interference, motivating the study of universal and transferable physical patch attacks. We propose Object-Associated Patch Attack (OAPA), a universal and transferable physical patch framework that enables an attacker to select which task object's manipulation to disrupt through patch placement, without re-optimizing the patch. Our framework combines object-associated placement, differentiable physical compositing, and final action-expert representation divergence. Physical compositing accounts for perspective and occlusion across camera views, while representation divergence guides patch optimization using either relative RMS or cosine distance. Experimental results demonstrate strong attack transferability across task suites and policies, together with the ability to selectively disrupt manipulation of an attacker-chosen task object through patch placement.

---


### 174. [Under the Influence -- of What? A Controlled Evaluation of Influence Functions](https://arxiv.org/abs/2611.34373)

**<font color=#1a73e8>作者：</font>** Johannes Gabriel Sindlinger, Arzu Burcu Güven, Rob van der Goot 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Influence functions are a promising way to identify which training examples are responsible for a model's output. However, so far empirical evaluations on LLM pretraining level only assumed that they work as intended. This is the first work to systematically evaluate whether the 'influential' examples actually have properties relevant to a language model output, based on re-training with controlled data splits. We investigate three prominent Hessian approximation methods (GradSim, TrackStar, K-FAC) in two settings (linguistic phenomena and factual knowledge) in GPT-2 type models (68M-5.6B training tokens). We find that on average, the `influential' examples are indeed relevant, but they do not always bear the target properties directly, and the ratio and kind of relevance varies by setting.

---


### 175. [AgentLens: Graph-guided Security Auditing for LLM-based Agents](https://arxiv.org/abs/2611.34380)

**<font color=#1a73e8>作者：</font>** Peizhuo Lv, Tao Chen, Mengya Shi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents are emerging as a key paradigm for automating software engineering by coupling LLM-driven decision-making with external tools, files, APIs, and execution environments. However, weaknesses in agent implementations and insecure interactions between the agent and external resources can lead to severe consequences, including remote code execution, arbitrary file access, SQL injection, and data leakage. This makes pre-deployment auditing essential for systematically identifying implementation weaknesses and validating whether they can manifest as concrete security risks in realistic agent workflows. Existing approaches either focus on specific vulnerability classes or lack the capability to validate whether identified static weaknesses correspond to executable exploits. In this paper, we propose AgentLens, a systematic auditing framework for LLM-based agents. AgentLens analyzes the target agent's implementation, component interactions, and built-in defenses, and organizes them into an Audit Knowledge Graph that captures how these factors interact to expose potential security risks. Based on this graph, AgentLens derives candidate attack paths, generates path-specific validation payloads, and constructs realistic multi-turn audit scenarios that place these payloads in task-relevant contexts to validate whether suspected risks manifest as security-violating behaviors during execution. Across five widely-used agent applications, each with over 24,000 GitHub stars, AgentLens identifies 44 vulnerabilities, and every vulnerability is validated by being triggered during execution. Compared with the state-of-the-art approach (AgentFuzz), AgentLens detects 3.67$\times$ more vulnerabilities. To date, 12 reported issues have been assigned CVE IDs.

---


### 176. [Strong Starts, Simple Recipes: Unified Multi-Teacher On-Policy Distillation from Multimodal Specialists](https://arxiv.org/abs/2611.34397)

**<font color=#1a73e8>作者：</font>** Wenzheng Chang, Taiqiang Wu, Yuqi Xu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) integrates separately trained domain specialists into a single unified model. Existing methods focus on refining the distillation procedure while initializing the student from a base model or a multi-domain SFT checkpoint, which leaves capability integration largely to distillation itself. Instead, we treat the starting point as a design variable and propose Unified MOPD (Uni-MOPD), which pairs a strong start with a simple recipe: a training-free uniform merge of specialists from the same base model initializes the student, and short MOPD with uniform domain sampling and full-vocabulary reverse KL refines it. Across five multimodal domains and 19 benchmarks, our study establishes three findings. (1) The starting point matters more than subsequent training choices: before any training, the uniform merge already matches the score that the base model reaches after 200 MOPD updates, and after short distillation it matches higher-scoring, search-based starts. (2) Short MOPD recovers most of the capabilities the merge leaves unintegrated; it improves every domain, with the largest gains where the domain teacher still leads. (3) From a strong start, uniform domain sampling and full-vocabulary reverse KL match or exceed every evaluated sampling strategy and divergence, without schedules, per-token weighting, or truncation hyperparameters. Uni-MOPD outperforms Open-MOPD at the same training budget while training 3.3 times faster than its released code. We will release the training framework, specialist checkpoints, and unified student.

---


### 177. [When Skills Fail to Compose: Compatibility and Retention in Language Models](https://arxiv.org/abs/2611.34398)

**<font color=#1a73e8>作者：</font>** Yan Lin, Zhongliang Guo, Jingyu Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skill acquisition alone does not establish a reusable skill library: task proficiency does not specify a compositional interface. Motivated by agents that acquire and refine skills, we study independently learned soft-prompt skills on frozen language models, with skill identities and execution order supplied. Across four digit-task bases and three record-editing models, mean composition accuracy in one call is at most 7.6%, compared with 88.2% to 100% over two calls that add computation and an explicit intermediate output. Neutral-insertion training improves robustness but leaves substantial interference, which block length and per-token norm alone cannot explain on two of four digit bases. Blocks of the same operation need not be interchangeable: after training next to frozen learned partners, a post hoc test on two Qwen bases shows that replacing those partners with independently learned blocks of the same operations lowers median composition accuracy from 98.0% and 95.3% to 12.7% and 0.5%, although every replacement scores at least 90% alone. Repair can improve a composition while impairing the original skill, and rehearsal improves retention while transfer remains limited on Qwen2.5-0.5B. Internal interventions constrain explanations without identifying a shared failure mechanism. These findings motivate evaluating compatibility, retention and transfer alongside acquisition when building skill libraries for self-evolving agents. Code is available at this https URL.

---


### 178. [EvoLink-Bench: A Benchmark for Evaluating Self-Evolving Agents in Long-Horizon Interdependent Task Streams](https://arxiv.org/abs/2611.34400)

**<font color=#1a73e8>作者：</font>** Wei Chen, Xiaodong Lu, Weihao Shen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are evolving from passive chatbots into autonomous systems that operate continuously in dynamic environments. Such agents need not only solve current tasks but also learn from past interactions to improve future performance. However, existing streaming benchmarks often rely on short task sequences or largely independent tasks, providing limited evidence of whether agents can effectively reuse experience when later tasks depend on earlier outcomes. To address this gap, we introduce \textbf{EvoLink-Bench}, a benchmark for evaluating self-evolving agents in long-horizon, interdependent task streams. It covers daily office work, multi-turn dialogue, and AutoResearch-style workflows, with persistent workspaces and dependencies across tasks. The benchmark includes two complementary levels: \textbf{L1}, which evaluates the acquisition and revision of language-expressible knowledge, and \textbf{L2}, which assesses the development of task-level capabilities through execution and feedback. Its evaluation further distinguishes within-task recovery, persistent-state updates, and experience reuse in later tasks. We evaluate five agent frameworks across three backbone configurations under three persistence conditions, covering 19,635 scored task slots from selected evaluation cohorts. Results show that no framework consistently performs best across both levels, retries recover only a limited proportion of failed tasks, and persistent-state updates do not necessarily improve subsequent performance. Furthermore, the effects of evolution differ between knowledge- and capability-level tasks, suggesting that these two forms of evolution require different learning mechanisms. Performance gains also vary across domains and task streams, with improvements on some tasks not necessarily extending to others.

---


### 179. [Any-Rate: Half-Bit Multi-Precision LLM Quantization with Coded Bit-Planes](https://arxiv.org/abs/2611.34402)

**<font color=#1a73e8>作者：</font>** Hoonki Lee, Haechan Shin, Hyuntaek Jung 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nested multi-precision quantization derives multiple precisions from a single checkpoint by reading only the leading bits of each weight, which makes it attractive for on-device deployment under varying memory and energy budgets. However, existing methods offer only integer bits, leaving large accuracy gaps between adjacent precisions and severe degradation at 2 bits. To address this, we propose Any-Rate, which serves 2-8 bits from one checkpoint, in half-bit steps over 2-4 bits. Any-Rate restricts some bit-planes to extended Hamming codewords in 8-weight blocks (0.5 bits per weight), shares one LUT per row across precisions, and encodes all precisions jointly with a separate target for each, reducing the loss from sharing bit-planes. Across four LLMs, Any-Rate achieves state-of-the-art accuracy among multi-precision methods at 2 and 3 bits, keeping 69% of FP16 accuracy at 2 bits, and is within one point of the best at 4 bits. It decodes about as fast as existing kernels, and an LPDDR energy model estimates up to 27% less energy at equal accuracy. Code is available at this https URL.

---


### 180. [Agentic Waterfall: An Intent-Driven Information Discovery Framework for Reclaiming User Control in the Attention Economy](https://arxiv.org/abs/2611.34407)

**<font color=#1a73e8>作者：</font>** Yige Luo, Shining Zhang, Jikun Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We formalize Agentic Waterfall Feed, a new problem of personalized information discovery in which users actively direct recommendations and the system adapts to evolving needs inferred from both explicit requests and browsing behavior. We address this problem with the Agentic Waterfall framework, whose language-model controller maintains persistent user state and coordinates content retrieval, ranking, and state updates. To evaluate systems on this task, we contribute the Agentic Waterfall Dataset and a replay-based evaluation protocol. The dataset combines real content metadata with simulated interaction histories. The protocol compares systems under shared histories using relevance scores and blind judgments of how well recommendations satisfy current user goals and constraints. Agentic Waterfall remains competitive with strong baselines on conventional recommendation tasks across five public benchmarks. On the Agentic Waterfall Dataset, it outperforms the strongest baseline in both evaluations, with relative improvements of up to 16.1%.

---


### 181. [SemProxy: Semantic 3D Proxies for Controllable Agentic 3D Modeling](https://arxiv.org/abs/2611.34414)

**<font color=#1a73e8>作者：</font>** Shuyuan Zhang, Changjian Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coding agents are increasingly capable of generating 3D models, yet enabling users to effectively control the modeling process remains challenging. Existing workflows rely primarily on text prompts and reference images, which often struggle to convey precise spatial intentions and require iterative corrections. We introduce SemProxy, a lightweight intermediate representation that bridges intuitive human interaction and agentic 3D modeling. Instantiated as labeled 3D bounding boxes, semantic 3D proxies allow users to directly specify object parts and spatial arrangements while leaving geometric details to coding agents. These proxies can be serialized into structured text and rendered as images, making them directly accessible to existing coding agents without additional training or modifications. We further develop ProxyStudio, a user interface that integrates text, image references, and interactive 3D proxy editing into agentic modeling workflows. We demonstrate the versatility of SemProxy across object- and scene-level modeling tasks with different coding agents, and evaluate its effectiveness in supporting controllable human-agent collaborative 3D modeling through a user study.

---


### 182. [DocSEAM: Bidirectional Cross-Page Encoding for Multi-Page Document Understanding](https://arxiv.org/abs/2611.34420)

**<font color=#1a73e8>作者：</font>** Hoang-Nhat Nguyen, Chen Change Loy  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-page document vision-language models encode each page independently, creating a feature-level discontinuity at page boundaries: visual tokens are formed without access to content on adjacent pages, and the language model must reason over these page representations formed in isolation. We introduce DocSEAM (Document Selective Enrichment via Anchored Masking), a lightweight module inserted between a pretrained vision encoder and the language model that injects the inductive bias of local cross-page context into visual representations. For each page, DocSEAM forms a local triplet with its two neighbors, applies center-anchored masked self-attention with directional salience gates to fuse information from neighbor pages, and returns only the enriched center-page tokens, leaving the visual token count unchanged. After a supervised cross-page warm-up and multi-page fine-tuning with DocSEAM frozen, our 9B-parameter model achieves state-of-the-art results among the evaluated open-weight models of up to 10B parameters on five multi-page document VQA benchmarks. We further show that under controlled re-pagination, DocSEAM reduces sensitivity to boundary placement and improves cross-page span localization

---


### 183. [Mitigating Hallucinations in Medical Question Answering on ESC Cardiology Guidelines: Evaluation and Retrieval Optimization](https://arxiv.org/abs/2611.34427)

**<font color=#1a73e8>作者：</font>** Ilkin Masimov, Rufana Baghirli, Muhammad Rashid  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: Large language models produce hallucinations in medical question answering (QA). Verify-and-revise pipelines that check atomic claims against retrieved guideline evidence are a standard mitigation, but evaluations almost universally treat the verifier's output as ground truth, an assumption rarely tested. Objective: To measure, claim by claim against human judgement, how such a pipeline fails in a guideline-grounded clinical setting. Methods: We built a dataset of 160 questions (100 patient vignettes from 89 de-identified cases, 60 fact-based) over four recent ESC cardiology guidelines, all approved by a practising internist, and a retrieval corpus of 627 hand-verified guideline records at two chunk granularities. A five-stage pipeline was run under four retrieval configurations and three independent runs (1920 arm-runs); all 606 first-pass refuted claims were manually audited, an independent judge re-judged 906 decisions, and the expert blindly reviewed 100 accepted claims. Results: Only 44.7-50.6% of flagged claims were true hallucinations. Correction loops converged in 85.2-95.1% of cases, yet 35% of genuine final errors were introduced by correction. Single-run true-hallucination recall was 35.6-41.2%, the three-run union 71-80%; verifier agreement was moderate (kappa = 0.505). The blind probe estimated the accepted-claim miss rate at 3.2% (95% CI 0.7-6.7%). Final genuine-error rate: 1.7% of answers. Conclusion: Claim-level verification reduces hallucinated content by an order of magnitude, but verifier reliability, not generation, is the limiting factor and must be measured, not assumed.

---


### 184. [Evaluating Aviation Safety Knowledge Extraction with SmolLM2: From Zero-Shot to Retrieval-Grounded Prompting](https://arxiv.org/abs/2611.34432)

**<font color=#1a73e8>作者：</font>** Aziida Nanyonga, Mustafa Tahsin Yilmaz, Amir Hussain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aviation accident narratives contain safety knowledge that is difficult to capture using structured occurrence fields alone. This study evaluates prompting-based knowledge extraction across four dimensions: concept accuracy, verbatim evidence grounding, structural compliance, and directed relation extraction. SmolLM2-1.7B-Instruct was evaluated under zero-shot, one-shot, fixed few-shot, and retrieval-grounded prompting using 300 National Transportation Safety Board narratives from 2000-2020, containing 3,763 reference concepts and 467 directed relations. Evaluation combined structural checks, verbatim evidence matching, expert-reviewed semantic matching, and paired bootstrap confidence intervals. No prompting strategy performed best across all dimensions. Retrieval-grounded prompting achieved the highest concept micro-F1 of 32.27%, although its advantage over fixed few-shot prompting was uncertain (95% CI: -0.92 to 2.40 percentage points). One-shot prompting achieved the highest relation F1 of 6.95%, identifying directed relation extraction as the principal SmolLM2 bottleneck. Compared with fixed few-shot prompting, retrieval improved verbatim grounding (59.45% vs. 54.02%) but reduced complete structural compliance (33.3% vs. 42.7%). Verbatim matching establishes source presence rather than evidential relevance. An exploratory comparison using 35 benchmark narratives showed that Qwen3-8B achieved higher concept micro-F1 across all prompting conditions and higher relation F1 under demonstration-based prompting, reaching 51.37% and 34.62%, respectively, under one-shot prompting. The small subset limits generalization. These findings support evaluating semantic correctness, source traceability, structural reliability, and directed relation accuracy separately.

---


### 185. [vSFT: Learning to Verbally Tune Agents at Test Time](https://arxiv.org/abs/2611.34440)

**<font color=#1a73e8>作者：</font>** Qishuai Wen, Rui Chen, Haiwen Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents are increasingly improved via agentic reinforcement learning, which can be on-policy but suffers from expensive rollouts and sparse rewards, limiting its application at test time. In this paper, we present a verbally Supervised Fine-Tuning (vSFT) framework that enables the conjunction of dense feedback in natural language and weight updates at test time. Specifically, our vSFT forms a closed loop between an agent and a supervisor via a hypernetwork, in which the supervisor generates verbal supervision from the agent's failed trajectories, and the hypernetwork converts that supervision into low-rank weight updates to tune the agent. We validate that this test-time in-parameter evolving process outperforms both its in-context counterparts and prevalent reinforcement learning methods. In particular, our vSFT using Qwen3-4B outperforms GRPO and Reflexion by 8.7% and 13.9% in success rate on ALFWorld, and by 4.8% and 18.2% on WebShop, respectively. We believe that learning how to adapt a model, rather than an adapted model, offers a promising path towards more capable agents that improve themselves.

---


### 186. [Evidence-Aligned Benchmarking and Learning for Medical Video Language Models](https://arxiv.org/abs/2611.34465)

**<font color=#1a73e8>作者：</font>** Zhongpai Gao, Anwesa Choudhuri, Meng Zheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A medical video language model should answer from the visual evidence its question asks about. We find three places where this breaks down and address each with an approach we call MedEvidU. First, benchmarks reward answers that ignore the video: on one dataset, the position of a clip within its recording predicts the surgical step in 37% of questions, and a constant answer beats every trained model on a standard safety-assessment metric. We build MedVidBench-v2, 34 tasks from 18 surgical and clinical video datasets, in which prompts and metrics are audited with answers given without video, and which tests unseen hospitals and windows cut blindly from whole recordings. Second, common video encoders merge consecutive frames into shared tokens, so a question about one frame is answered from a blend of two. Query-slot inputs give each queried frame its own tokens at almost no extra cost. Third, a fine-tuned model has memorized its training questions, which leaves little to learn from. Label-matched question resampling (LQR) adds unseen questions about the same recordings while keeping the answer distribution fixed, in a final supervised epoch and in reinforcement learning. Together, these raise the grounding IoU of a 4B model from 30.4 to 44.4, above a supervised 27B model, and instrument grounding at an unseen hospital from 33.9 to 72.5. On blindly cut windows, event-presence accuracy improves by 5.5 points and localization F1 by 8.1 points. Project page: this https URL

---


### 187. [EgoUseBench: Benchmarking Computer-Use Agents under Evolving First-Person Contexts](https://arxiv.org/abs/2611.34466)

**<font color=#1a73e8>作者：</font>** Yurun Chen, Biao Yi, Qihang Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI wearables, such as smart glasses, extend the context available to agents beyond digital environments to users' physical surroundings. With these devices, computer tasks can originate from users' ongoing activities rather than solely from explicit instructions. Through first-person observations, agents can identify objects and activities relevant to user requests and ground digital tasks in the surrounding context. We call this interaction paradigm Ego Use. However, first-person observations are limited by the wearer's viewpoint and may provide incomplete or ambiguous evidence of ongoing activities. As new observations arrive, agents may need to revise their understanding of the physical context and user intent, and reassess whether prior digital actions remain valid. Whether current agents can reliably handle these changes remains insufficiently evaluated. We introduce EgoUseBench, a benchmark for evaluating Ego Use across three interaction settings with different levels of first-person context. Computer-Use relies on explicit instructions, Offline Ego Use provides prerecorded first-person context before execution, and Online Ego Use provides continuous observations as user intent evolves. Based on over 74 hours of real-world first-person recordings, we construct 693 tasks across the three interaction settings. To capture task evolution, we track first-person observations, user requirements, and website state separately. We further group tasks by how information changes during execution, resulting in three types: Graft (revised user requirements), Refresh (new first-person observations), and Clarify (agent-initiated information seeking). We evaluate advanced models and find that average success rates in Online Ego Use are 26.3% lower than in Computer-Use. This result reveals the difficulty of keeping task execution aligned with evolving first-person context and user intent.

---


### 188. [Attacking Hard-Label Large Vision-Language Models with Model-Sensitive Adversarial Patch Designs](https://arxiv.org/abs/2611.34467)

**<font color=#1a73e8>作者：</font>** Nian Ai, Guangke Chen, Xiaowen Cai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) have demonstrated impressive capabilities in handling multi-modal downstream tasks, gaining increasing popularity. However, recent studies show that LVLMs are susceptible to both intentional and inadvertent attacks. Existing attackers ideally optimize adversarial perturbations with backpropagated gradients from LVLMs, thus limiting their scalability in practical scenarios as real-world LVLM applications will not provide any LVLM's gradient or details. Motivated by this research gap and counter-practical phenomenon, we propose a novel hard-label attack method for LVLMs, named HardPatch, to generate visual adversarial patches by solely querying the model. Our method provides deeper insights into how to investigate the vulnerability of LVLMs in local visual regions and generate corresponding adversarial substitution under the practical yet challenging hard-label setting. Specifically, we first split each image into uniform patches and mask each of them to individually assess their sensitivity to the LVLM model. Then, according to the descending order of sensitive scores, we iteratively select the most vulnerable patch to initialize noise and estimate gradients with further additive random noises for optimization. In this manner, multiple patches are perturbed until the altered image satisfies the adversarial condition. Extensive LVLM models and datasets are evaluated to demonstrate the adversarial nature of HardPatch. Our empirical observations suggest that with appropriate patch substitution and optimization, HardPatch can craft effective adversarial images to attack hard-label LVLMs.

---


### 189. [Who Is Ego? Scaling Cross-View Camera Wearer Identification and Segmentation beyond Humans](https://arxiv.org/abs/2611.34489)

**<font color=#1a73e8>作者：</font>** Yifan Jin, Zheng Zhang, Tianwen Qian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A first-person (ego) image reveals what a camera sees, but not who or what carries it. Given a synchronized third-person (exo) image, camera wearer identification asks who is ego: which candidate carries the ego camera? We extend this task beyond humans to robots, vehicles, animals, and drones, and broaden its spatial scope (where is ego) from selecting a provided candidate mask to wearer segmentation with absence prediction and mutual camera localization across ego-exo views. We introduce FindEgo-1M, comprising 1.16M real and simulated ego-exo pairs across 12 wearer types, 17 domains, and 111 test settings. Our approach exploits a geometric relation: the ego camera's projection into the exo image, i.e., the epipole, lies on or near its wearer. We introduce EgoRay-ZS, the first method to turn a frozen feed-forward 3D reconstruction model, VGGT-$\Omega$, into a training-free solution for wearer identification and segmentation. Its geometric readout ranks candidate masks or segmentation proposals by angular offset and distance to the ego camera, while the relative pose provides mutual camera directions. We then develop the full EgoRay model through pose-supervised training on FindEgo-1M and label-free test-time adaptation constrained by candidate masks. Without task-specific training, EgoRay-ZS achieves 78.0% identification accuracy on TF2023's original labels, versus 52.9% reported for the dataset-trained PEN. On FindEgo-1M, EgoRay achieves state-of-the-art chance-corrected accuracy of 87.1 and 77.7 on seen and unseen settings. On matched queries, EgoRay also outperforms GPT-6 Astra by 31.6 and 21.3 points on seen and unseen settings, respectively, while running $18\times$ faster. Data, code, and models will be released.

---


### 190. [FlyingStart: Learned Cross-Token Warm Starts for Fixed-Point Decoding in Recurrent-Depth Language Models](https://arxiv.org/abs/2611.34492)

**<font color=#1a73e8>作者：</font>** Runguo Li, Dezhen Lu, Zixiang Ni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recurrent-depth language models generate each token by iterating a shared block of layers until its hidden state converges. Inference methods for these models decide when to stop the iteration, yet every token still starts from random noise and pays the full cost of converging. We show that where the iteration starts is a second, independent lever. A token's fixed point is predictable from the state at which the previous token stopped, after a learned change of coordinates, and we introduce FlyingStart, a linear warm start that is fitted in closed form on the frozen model and costs under 5% of one loop. The iteration and its stopping rule are unchanged, so the exit criterion certifies the same distance to the fixed point from any start: a better start removes loops at unchanged accuracy. On Huginn-0125, FlyingStart matches the accuracy of the strongest training-free baseline with 14--19% fewer decoding layers, raises batched throughput by 16--18% in two serving engines, and adds a further 10--14% on top of self-speculative decoding. A contraction analysis predicts the number of loops saved on all four models we study, including one where the prediction was recorded before any evaluation, and token by token on Huginn, and it identifies when a warm start pays off: the saving grows with the number of loops a model needs to converge.

---


### 191. [Know the Design, Pick the Attack: Sentence-Keyed Watermarks for LLMs](https://arxiv.org/abs/2611.34505)

**<font color=#1a73e8>作者：</font>** Jon Carmona, Jon Irureta, Jon Imaz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A watermark lets the provider of a language model recognise the text its model wrote, which matters more as generated text becomes hard to tell from human writing: provenance underpins academic integrity, the fight against misinformation and new regulation. Providers have started to watermark the text of their models, and to explain how their watermarks work. Explaining a watermark, however, also tells an attacker how to break it, and there are two ways to do so: reword the text to erase the mark, or learn the mark and copy it onto text the model never wrote. Each attack has been studied on its own. We study an attacker that reads the published design to choose between them: it erases the watermarks that are hard to learn and forges the ones that survive rewording. Against it, every existing watermark we compare fails. We propose KeyedLex, which reads its secret key from the grammar of the previous sentence, which rewording changes little, and whose detector does not need to recover the key exactly. It outperforms every watermark we compare on both models we test, losing about half of its signal where the best alternative loses two thirds, at no extra cost in text quality over the best-known watermarks.

---


### 192. [Decoder-as-a-Probe: Verbalizing and Steering Visual Representations in LVLMs](https://arxiv.org/abs/2611.34515)

**<font color=#1a73e8>作者：</font>** Adhemar de Senneville, Xavier Bou, Jérémy Anger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> It is commonly accepted that high-level concepts are represented linearly in the representation space of large neural networks. For Large Vision Language Models (LVLMs), finding those interpretable directions in visual representations is important for interpretability. To find them, the classical approach is to train a linear classifier on the representations, but it needs a large amount of labels and only recovers what can be read from the representations, not what the model actually uses. In this paper we start from the following insight: The LLM Decoder of an LVLM is also a classifier whose classes are the possible next tokens. So we use its first-order Taylor expansion as a linear classifier. Hence, we introduce Decoder-as-a-Probe (DaP), which significantly outperforms classical probing and steering baselines especially when training data is sparse. (1) It verbalizes what an LVLM perceives in a given image. (2) It can surgically change the perception of the LVLM about specific attributes (e.g. change only the color, the clothes worn or the action done). Due to its simplicity and data efficiency, we believe DaP can serve as a plug-and-play tool for LVLM research, such as interpretability, hallucination mitigation or instruction tuning.

---


### 193. [PURA: Video Token Pruning via Unified Spatiotemporal Redundancy Assessment](https://arxiv.org/abs/2611.34521)

**<font color=#1a73e8>作者：</font>** Yuyao Sun, Hongli Yuan, Shuang Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video large language models incur substantial inference costs from long visual token sequences. Existing video token compression methods mitigate these costs by exploiting spatial redundancy within frames and temporal redundancy across frames. However, many approaches impose predefined processing orders or fixed allocation ratios for spatial and temporal compression, limiting their ability to adapt to the varying balance of spatiotemporal redundancy across videos. To address this limitation, we propose PURA, a training-free method that prunes visual tokens through unified spatiotemporal redundancy assessment. For each token, PURA constructs spatial and temporal reference candidates and selects the reference with the lowest representation error across the two dimensions. The representation error is combined with token importance to determine each token's removal cost. To avoid the time overhead of removing the lowest-cost token one by one, we introduce Coordinated Pruning, which iteratively groups mutually compatible low-cost removals into batches for simultaneous execution and updates the pruning state after each batch until the target budget is reached. Extensive experiments on three video large language models and five video understanding benchmarks demonstrate that PURA achieves a favorable trade-off between task performance and inference efficiency.

---


### 194. [AliceAI-Foundation-80B-A3B-Base](https://arxiv.org/abs/2611.34529)

**<font color=#1a73e8>作者：</font>** Nikolay Skachkov, Ekaterina Redina, Maksim Konoplev 等 36 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present AliceAI-Foundation-80B-A3B-Base, a mixture-of-experts language model with 80 billion total parameters and approximately 3 billion active parameters per token, trained from scratch at Yandex and released under the Apache 2.0 license. The model combines Kimi Delta Attention with full attention, uses Attention Residuals, and is trained with Muon. Training comprises general pretraining on 17.5 trillion tokens, two context-extension stages, and a dedicated stage for reasoning and agentic interaction. We describe the data collection and augmentation pipelines, evaluation protocols, architectural ablations, and scaling-law experiments. We identify the limitations of held-out training loss as a proxy for downstream performance and introduce an auxiliary loss on mixture-of-experts outputs to stabilize training at the predicted learning rate. Domain-specific data selection and augmentation improve factual knowledge, mathematics, and programming skills, while agent trajectories introduced during pretraining improve performance on agentic benchmarks after supervised fine-tuning. In zero-shot reasoning evaluation, the model achieves leading results among open base models of comparable size, with 88.7% pass@8 on IMO-AnswerBench and 82.9% pass@8 on LiveCodeBench v5-v6. To evaluate Russian-language factual knowledge, we introduce and release two benchmarks with their evaluation protocols: WikiWebFacts, which tests short factual questions drawn from encyclopedic sources and search queries, and HardMultiQA, which tests more demanding factual questions inspired by user interactions. Our model scores 86.5% on WikiWebFacts and 67.9% on HardMultiQA, compared with 83.2% and 65.4% for DeepSeek-V4-Flash-Base (284B total and 13B active parameters) and 72.8% and 54.5% for Nemotron-3-Super-120B-A12B-Base (120B total and 12B active parameters), outperforming both larger models on these benchmarks.

---


### 195. [EPPC-CARE: Staged Hierarchical Annotation of Communication Behaviors in Secure Patient-Provider Messages](https://arxiv.org/abs/2611.34539)

**<font color=#1a73e8>作者：</font>** Samah Fodeh, Sreeraj Ramachandran, Ganesh Puthiaraju 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objectives: Patient portal messages provide invaluable information about communication dynamics between patients and healthcare providers, but extracting it manually is labor-intensive. We developed and evaluated EPPC-CARE, an automated framework for identifying communication behaviors together with the supporting text for each classification. Materials and Methods: From 867 messages, we obtained 5,516 reference standard annotations. Each annotation is a triplet of communication-related text (span), a broader communication category (Code), and a specific subcategory (Sub-code). We evaluated EPPC-CARE's identified triplets across six open-weight large language models (LLMs) against supervised fine-tuning and communication-based models such as EPPC-OASIS. We also compared EPPC-CARE with human expert annotations on 100 messages. Results: EPPC-CARE improved performance over EPPC-OASIS across all six models. EPPC-CARE's Triplet F1 improved by 2.90 percentage points on average, with a best score of 64.4%. On the human expert evaluation subset, EPPC-CARE and the human expert showed comparable agreement with the reference standard, with differences favoring EPPC-CARE. Discussion: These findings suggest that identifying triplet components (span, code, subcode) sequentially can improve performance across model families while preserving the supporting text behind each identification. EPPC-CARE links the communication code and subcode with the source text (span), supporting human verification of automated annotations in clinical informatics. EPPC-CARE may therefore make larger-scale studies of patient-provider communication more feasible and provide a foundation for human-in-the-loop annotation workflows. Conclusion: EPPC-CARE offers a more reliable and reviewable approach for automated characterization of communication behaviors in secure patient-provider messaging.

---


### 196. [HAS: Hierarchical Adaptive Frame Sampling for Video Understanding](https://arxiv.org/abs/2611.34544)

**<font color=#1a73e8>作者：</font>** Yuyao Sun, Daiqi Shi, Shuang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to context-length constraints, most MLLMs cannot process full-length videos and therefore rely on sampling a subset of frames as input. However, existing sampling methods, ranging from uniform sampling to relevance-based selection, are often driven by a single sampling principle and thus struggle to accommodate the heterogeneous evidential requirements of different queries: some demand a holistic understanding of how the video unfolds over time, while others hinge on fine-grained events within a short temporal window. To address this limitation, we propose \textbf{Hierarchical Adaptive Frame Sampling (HAS)}, a two-stage frame sampling framework. In the first stage, \emph{Backbone Frame Construction}, we apply a Determinantal Point Process (DPP) to sample frames that are both query-relevant and non-redundant. These selected frames capture key moments across the video and form the backbone of the sampling set, providing a foundation for subsequent enrichment. In the second stage, \emph{Adaptive Contextual Enrichment}, we analyze the temporal distribution of the backbone frames to infer the query's requirements and adaptively allocate the remaining frame budget between Local and Global Context. The Local Context enriches the backbone with fine-grained temporal dynamics and short-range causal relations, whereas the Global Context connects temporally isolated evidence and provides a holistic view of the entire video to support global understanding. Through such a hierarchical two-stage process, HAS effectively addresses diverse query requirements. Incorporated into three leading MLLMs, it demonstrates consistently superior performance across the Video-MME, LongVideoBench, and MLVU benchmarks.

---


### 197. [Recalling the Past to Answer the Present: Context-Aware Multi-Evidence Reasoning for Streaming Video Question Answering](https://arxiv.org/abs/2611.34545)

**<font color=#1a73e8>作者：</font>** Cui Yakun, Tiantian Geng, Huixiang Kong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved remarkable progress in video understanding, yet existing video question answering (VQA) benchmarks mainly evaluate models in offline settings. Real-world streaming scenarios instead require models to answer context-dependent queries by retrieving and reasoning over evidence distributed across the video history. We introduce StreamRecall, a benchmark for context-aware Multi evidence reasoning in streaming video QA. StreamRecall requires models to retrieve, associate, and reason over temporally scattered evidence to answer queries at the appropriate moment. It contains 4,983 questions over 462 videos, with context-aligned query times and fine-grained temporal evidence annotations. We further propose the Evidence Utilization Cascade to diagnose model reasoning through evidence localization, grounding, chain completion, and answer derivation. To enable efficient long-term streaming reasoning, we present EviStream, a training-free causal visual memory mechanism that preserves reasoning-critical evidence under a fixed KV budget. Experiments reveal substantial gaps between current VLMs and realistic streaming requirements, establishing StreamRecall as a foundation for developing evidence-aware streaming video intelligence.

---


### 198. [Sage-Med: Scaling Medical Multimodal Intelligence](https://arxiv.org/abs/2611.34575)

**<font color=#1a73e8>作者：</font>** Sage-Med Team, Ming Hu, Cheng Tang 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Establishing effective scaling laws for medical multimodal large language models (MLLMs) remains a persistent and fundamental challenge. Our systematic evaluation shows that existing medical MLLMs tend to underperform frontier general-purpose MLLMs across a range of medical tasks, while scaling model size primarily improves text capabilities rather than multimodal perception, and enabling reasoning modes fails to close this visual gap. To investigate how medical multimodal intelligence scales in practice, we introduce Sage-Med-Preview, a 35B-parameter medical multimodal model with 3B activated parameters, built by combining stage-specific curation over 322.7 million candidate records with a progressive training curriculum spanning medical pretraining, staged supervised fine-tuning, and adaptive reinforcement learning. Across this curriculum, progressive supervised refinement and adaptive reinforcement learning yield consistent stage-wise gains, substantially advancing both specialized visual understanding and medical language capabilities. Evaluated against 77 competing models across 238 clinical tasks spanning 61 public and 13 private multi-center benchmarks in more than 40 modalities, Sage-Med-Preview achieves an average score of 58.26% on the 31 public multimodal benchmarks. It outperforms the state-of-the-art open-source medical model Hulu-Med-235B-A22B at 50.99% and the general scientific model Intern-S2-Preview at 52.24%, and approaches the advanced proprietary model GPT-6.2-Sol across multiple tasks such as comprehensive multimodal understanding, report generation, and visual grounding. Although substantial challenges remain in complex medical reasoning and multi-step clinical workflows, this report provides empirical evidence, actionable data and training recipes, and a rigorous benchmark toward scalable clinical multimodal intelligence.

---


### 199. [Procedure Inference as Memory: Learning Recruiter Decision Procedures from OKF-Structured Episodes in Multi-Session Hiring Assistants](https://arxiv.org/abs/2611.34576)

**<font color=#1a73e8>作者：</font>** Praveen Kumar Bodigutla, Yizhi Zhang, Sai Vivek Kanaparthy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-session hiring assistants must infer evolving recruiter preferences and decision patterns across projects and time. We introduce Open Knowledge Format (OKF)-indexed episodic memory to organize interactions and retrieve related events through their lineage. We also introduce Procedure Memory, which learns reusable decision procedures from these episodes through prompted reflection or reinforcement learning. We compare these approaches with no memory, full-history context, and conversation search, and evaluate Jev-class models for index navigation and GPT-5.6 Luna as a lower-cost alternative to GPT-5.4.
In our evaluation, OKF-indexed retrieval achieves low-priority preference F1 scores of 0.93-0.95 at medium and high preference overlap between hiring projects. It significantly outperforms full-history context and conversation search in both settings, and no memory at high overlap, while using 69% fewer context tokens than full history. Procedure Memory reduces conversational turns by up to 39% relative to no memory. Qualitative and long-horizon evaluations provide evidence of temporal reasoning, with RL-learned procedures achieving 60% on both correct abstention and exact-field identification. Jev-class models improve conversational efficiency but more frequently miss temporally relevant evidence, highlighting the importance of evidence selection.
On PersonaMem-v2, Procedure Memory with OKF retrieval achieves 50.2% accuracy versus 48.6% for full-history context and 29.0% for no memory, using 90.5% fewer reader input tokens than full history. GPT-5.6 Luna performs comparably to GPT-5.4 at lower cost. These findings highlight the value of structured episodic memory and learned decision procedures for efficient personalization and temporal reasoning.

---


### 200. [Tune for Retention, Not Just Gain: SFT Forgets Far Less than You Think](https://arxiv.org/abs/2611.34579)

**<font color=#1a73e8>作者：</font>** Nirmit Joshi, Nathan Srebro, Eran Malach  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Catastrophic forgetting, the drastic loss of previously acquired capabilities when learning new ones, is a central challenge in language model fine-tuning. Supervised fine-tuning (SFT) is widely believed to be prone to such forgetting. Recent works have attributed this to the off-policy nature of SFT, arguing that on-policy learning is key to continual learning. In this paper, we challenge this premise. We show that while maximizing new-task performance can induce catastrophic forgetting, alternative hyperparameter choices (lower learning rate and batch size) can yield similar gains with little to no forgetting. With hyperparameters selected jointly for gain and retention, vanilla SFT retains prior capabilities far better than previously suggested and can be competitive with Self-Distillation Fine-Tuning (SDFT), an on-policy approach designed to mitigate forgetting. While SDFT can be more robust to hyperparameter choices, it also requires a retention-aware criterion to identify hyperparameter configurations that avoid catastrophic forgetting. Our results challenge the view that on-policy training is what enables learning with retention and raise broader questions about what drives catastrophic forgetting during fine-tuning.

---


> [!TIP]
> 当前位于：**151-200**（第 4/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-267](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
