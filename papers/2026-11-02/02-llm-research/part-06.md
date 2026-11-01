# 🧠 大模型相关研究 | 2026年11月02日

> 本类共 **353** 篇论文：已确认 **335** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 251. [InferD: A Honeypot Framework for AI Inference Infrastructure](https://arxiv.org/abs/2610.39807)

**<font color=#1a73e8>作者：</font>** Hicham Hammouchi, Gabriele Lenzini  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model serving stacks, commercial inference APIs, vector databases, and agent orchestration gateways are now ex- posed on the public internet and indexed by commodity scanners within hours of deployment. The threat characteristics of this sur- face are only beginning to be measured, and the honeypot frame- works that could measure it were designed for conventional net- work services rather than for AI infrastructure. In fact, emulating an AI service is a distinct deception problem: the observable behavior of the service, including model inventories, token formats, tool-call protocols, and authorization flows, must be reproduced faithfully, while the underlying computation, model inference and tool ex- ecution, must never occur. We present InferD, a low-interaction honeypot framework organized around a single principle we call deception without inference: every request an adversary can observe is answered from static response pools, and nothing an adversary submits is ever executed. InferD decomposes the emulation into four deception planes, transport, service protocol, vulnerability surface, and agentic session, adds a provenance plane that links a planted credential to evidence of downstream model-mediated processing.

---


### 252. [EvoTeam: Multi-Agent Collaboration via Evolving Teams](https://arxiv.org/abs/2610.39813)

**<font color=#1a73e8>作者：</font>** Qinuo Cao, Xin He, Dianxuan Fu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent systems (MAS) rely on collaboration among specialized agents to solve complex tasks. Existing methods improve MAS by refining the prompts, skills, and execution strategies of individual agents based on task feedback. However, improving individual agents does not necessarily lead to better team collaboration. Recent studies have therefore extended evolution to the collaboration level, using collective execution experience to adjust team organization, and inter-agent interactions. Nevertheless, evolving collaboration across heterogeneous tasks remains challenging, as existing approaches often constrain team reorganization within a shared structure and reuse interaction rules across incompatible team contexts. In this paper, we propose EvoTeam, a collaboration-centric evolution framework that jointly evolves team organization, interaction rules, and individual agent skills through execution experience. It maintains a library of reusable teams, selecting or creating agent teams and guiding collaboration through team-specific interaction rules. Collaboration experience accumulates within compatible team contexts, while individual skills remain reusable across teams. Experiments across four benchmarks demonstrate its effectiveness. Our code is available at this https URL.

---


### 253. [Aligning Medical Vision Language Models at the Capability Boundary with Entropy Adaptive Rubric Grounding](https://arxiv.org/abs/2610.39835)

**<font color=#1a73e8>作者：</font>** Hongyu Bai, Jiaqi Zeng, Chunzheng Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical diagnostic reasoning requires verifiable links between visual evidence and clinical knowledge, yet current medical vision language models are aligned with objectives that reward the wrong behavior. Uniform supervised fine tuning lets easy cases dominate updates while clinically critical boundary cases saturate prematurely. Sparse rewards based only on final-answer correctness cannot assess anatomical grounding or clinical logic, inviting reward hacking through answer shortcuts. We propose MedCBR, a two-stage alignment framework coupling boundary-aware preference optimization with rubric-grounded reinforcement learning. First, we construct counterfactual boundary preferences at the model's capability frontier using empirical pass rates and preference pairs that share reasoning prefixes but diverge at decisive diagnostic branches. Difficulty Weighted Boundary Preference Optimization (DBPO) concentrates learning on this calibrated boundary region. Second, we distill reusable clinical rubrics from boundary trajectories and activate them according to prediction entropy. Entropy Gated Grounded Policy Optimization (EGPO) rewards answer correctness, anatomical grounding, and reasoning fidelity while suppressing rubric noise on reliable samples. A reference policy anchored to the boundary-aligned model couples population-level boundary priors with instance-level uncertainty, making diagnostic reasoning more accurate and clinically grounded. Experiments on six medical benchmarks show consistent improvements over strong general, specialized, and reinforcement learning baselines, reaching 61.2% average accuracy with the largest gains on challenging differential diagnosis tasks. Ablations show super-additive gains: combining the two stages exceeds the sum of their individual improvements.

---


### 254. [Surprise Alone Learns Lies: Evidence-Gated Continual Learning for LLMs from Streaming Claims](https://arxiv.org/abs/2610.39840)

**<font color=#1a73e8>作者：</font>** Abdelkader Metales, Miriam Grabenheinrich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning methods for large language models increasingly decide what to learn by surprise, keeping the inputs the model finds least predictable. This rule is unsafe when the stream contains lies. A planted falsehood about something the model knows has low probability under the model's belief, so it is highly surprising by construction, and a surprise-driven learner absorbs nearly every such lie, at a rate similar to random selection with the same budget. We study the problem with LoRA-adapted students (Qwen2.5-1.5B, Qwen2.5-3B and Llama-3.2-3B) that learn from a stream of true and false claims about invented people and real CounterFact facts. We report four findings. (1) A verifier key, a judge that must approve each claim, removes lies to the extent that its verifier is accurate; real LLM judges are cautious and reject unsourced truths and even source-backed updates. (2) Calibrated regression tests on unrelated knowledge slow learning down without filtering out lies. (3) The original model's own prior flags claims that contradict what it knows, without a judge. It separates lies about known facts from true new facts (AUC 0.78-0.83 across three models) but not from legitimate updates of the same kind of fact (AUC 0.53). It saves 43% of judge calls, but an attacker with access to the model can choose lies that pass it. (4) If trusted sources exist that an attacker cannot plant, routing contradicted claims to evidence recovers legitimate updates and the combined system has the lowest poison rate among learned claims; when an attacker plants matching sources for 30% of the lies, the system ends up worse than the judge alone. The acceptance signals answer different questions, and none of them decides on its own whether a claim is true.

---


### 255. [DWISE: Denoising Workload-Informed Scheduling Engine](https://arxiv.org/abs/2610.39852)

**<font color=#1a73e8>作者：</font>** Lie Li, Wen Li, Junxiao Shen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlike autoregressive large language models (AR-LLMs), diffusion LLMs (dLLMs) generate text by iteratively denoising many tokens in parallel, offering a promising path to efficient inference. Existing serving frameworks, however, schedule dLLM requests with policies designed for AR models, namely first-come-first-served (FCFS) admission and prefill priority. We find that both policies are ill-suited to dLLMs, wasting much of their speed. FCFS ignores that a dLLM request's decoding cost is highly heterogeneous and unknown at arrival, causing severe head-of-line blocking. Prefill priority, widely used in AR-LLM serving to keep time-to-first-token low, sharply cuts dLLM efficiency, as rounds that run only prompts leave most of the batch idle. We present DWISE, a Denoising Workload-Informed Scheduling Engine for efficient dLLM serving. DWISE schedules requests by their remaining work, measured in a block-level unit shared by prefill and denoising, so both phases share a round. To predict the unknown denoising workload, DWISE combines a lightweight prompt-based predictor at admission with a single refinement from the first denoising round's hidden states, which capture model-specific information absent from the prompt and require no additional model execution. Implemented in SGLang and evaluated on five models from three dLLM families under bursty workloads, DWISE reduces mean end-to-end latency over SGLang by 5.4$\times$ on average and up to 14.9$\times$ while preserving task accuracy. The code will be released publicly.

---


### 256. [KV Cache Quantization for Diffusion Language Models](https://arxiv.org/abs/2610.39853)

**<font color=#1a73e8>作者：</font>** Yan Tai, Yunan Ding, Guangzhao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> KV cache quantization is well studied for autoregressive language models, where cached prefix states are exact under causal attention and quantization is mainly a cache reconstruction problem. Diffusion language models (dLLMs) break this assumption. Fast dLLM inference reuses KV states across denoising steps, but bidirectional token representations can change as masked tokens are revealed, so the reused cache may already differ from full recomputation before quantization is applied. We study KV cache quantization under this cache-reuse error. We adapt KIVI and KVQuant to Fast-dLLM-style prefix and dual cache reuse, and introduce TRACE and dLLM-KVQ. TRACE reconstructs feasible dLLM reveal trajectories from prompt-answer pairs, providing calibration states that match iterative masked decoding. dLLM-KVQ uses these trajectories to choose per-layer K-cache entries that remain in high precision according to output- and attention-level behavior metrics, while applying standard low-bit value quantization. Across LLaDA and Dream evaluations on GSM8K, HumanEval, MATH, and MBPP, dLLM-KVQ achieves the highest average score among quantized methods across the reported 4-bit and 2-bit prefix/dual cache settings.

---


### 257. [Attention, Dynamic Wave and Hybrid Sequence Mixers in Language Models](https://arxiv.org/abs/2610.39854)

**<font color=#1a73e8>作者：</font>** Dmytro Babarytskyi, Oleksandr Babarytskyi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) rely on Multi-Head Attention (MHA) for sequence modeling, but scaling to long contexts is constrained by the quadratic cost of attention, motivating sub-quadratic recurrent alternatives. This paper formalizes a Dynamic Wave recurrent layer, based on input-dependent exponential damping and cosine phase modulation, and evaluates three 10.94M-parameter configurations (Pure Transformer, Pure Wave, and Hybrid Wave-Attention) on TinyStories under perplexity, latency, throughput and peak VRAM profiling up to 4096 tokens. The Hybrid configuration reaches the best perplexity, 5.95 on the full held-out split against 6.93 for the Transformer and 7.26 for Pure Wave. The efficiency picture, however, is governed by implementation rather than by architecture. Against an unfused attention baseline, Pure Wave uses 78.7% less peak VRAM at a 4096-token context (1404.3 MB vs. 6601.6 MB); against a fused scaled-dot-product attention kernel the same comparison yields no advantage at all (1404.3 MB vs. 1403.6 MB), and in training mode Pure Wave is 8.3% more expensive than the Transformer. Likewise, hoisting elementwise terms out of the recurrence loop speeds the layer up 2.53-fold with no custom kernel, reducing its latency gap to attention from 2.48-fold to 1.12-fold. A hybrid stack is found to inherit the cost of its more expensive mixer rather than the advantage of its cheaper one, its peak VRAM matching the Pure Transformer to within 0.1%. A closed-form memory model reproduces these measurements and predicts the context length beyond which attention overtakes the vocabulary projection. The findings indicate that reported efficiency gains for recurrent attention replacements must be stated relative to a named attention backend and a named implementation, and that hybridization is best justified on quality grounds.

---


### 258. [M-PFT: Angular Margin for Calibrated Prompt-Tuning of Fine-Tuned Vision-Language Models](https://arxiv.org/abs/2610.39861)

**<font color=#1a73e8>作者：</font>** Shihab Aaqil Ahamed, Mohamed Ansaff, Nang Khin Myat Lay Phyu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt-tuning has emerged as a parameter-efficient technique for adapting large-scale vision-language models (VLMs) to downstream tasks while keeping the pre-trained weights frozen. However, prompt-tuned VLMs often suffer from a base-to-novel dual miscalibration problem, where models typically show underconfidence on base classes and overconfidence on novel classes. Current VLM calibration approaches address this dual miscalibration either separately or jointly, but lack a geometric understanding of the hyperspherical embedding space and thus fail to exploit angular discriminative properties to adjust distorted decision boundaries. To address this, we propose M-PFT, a novel angular-margin approach for prompt tuning that introduces two complementary objectives to promote class discriminability and semantic anchoring. This enlarges the angular margin by 1) minimizing the maximum cosine similarity between tunable class embeddings to reduce embedding collapse and 2) minimizing the angular distance between each tunable embedding and its corresponding zero-shot embedding to preserve semantic geometry. Extensive experiments across 9 prompt-tuning methods with various backbones on 15 diverse datasets show that our approach reduces the average calibration error on novel classes, while remaining competitive on base classes and maintaining comparable accuracy. Further analyses reveal that M-PFT effectively adjusts distorted decision boundaries induced by prompt tuning while preserving the pre-trained embedding space, improving calibration with negligible computational overhead.

---


### 259. [Incorporating Machine-Others: An Enactive Exploration of Human-LLM Interactions](https://arxiv.org/abs/2610.39869)

**<font color=#1a73e8>作者：</font>** Elena C. Cuffari, Marta Pérez-Verdugo, Xabier E. Barandiaran  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> New concepts based in interactional thinking are required to understand how humans are changed by relating to LLMs. Standard theories of technological impact upon users' autonomy are inadequate here, because this technology is capable of inducing linguistic interactions with humans in an unprecedented manner. Traditional theories of social cognition also fall short, because LLMs have neither autonomy nor minds nor sociality as such. And yet, humans interact, talk, and create with them. We base ourselves on enactive theory, particularly on the theory of Linguistic Bodies and recent developments of enactive accounts of AI, to explore how we make sense with machines. We argue that we incorporate machine-others in two ways: in the tool-like sense of incorporation as enabling particular skills, but also in the more linguistic and identity-tied sense of incorporating (and incarnating) LLMs' ways of languaging. However, LLMs are themselves excorporated and excarnated phantoms of our own languaging; we give a (machinic) body to our language. As such, we are not just incorporating machinic others; we are incorporating excorporated others. These conceptual advances draw a new map of our linguistic relation to LLMs, putting them in continuation with other forms of languaging involving other linguistic artifacts (e.g., religious books). We attend to some particular forms that this relation takes today, and how they may be impacting the autonomy and becoming of LLM-engaged humans. We introduce the idea of "susceptive sense-making" to characterize increased semiotic labour that is carried by the lack of friction that we sometimes encounter within these services.

---


### 260. [Turing LLM Post-Training: Calibrated Distillation and Efficient Dynamic-MoE Execution](https://arxiv.org/abs/2610.39876)

**<font color=#1a73e8>作者：</font>** Yue He, Jiahui Hu, Shaman Tang 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study post-training for dynamically routed mixture-of-experts (MoE) models, focusing on integrating independently optimized specialists while keeping consolidation efficient. Our approach combines calibrated multi-teacher on-policy distillation (C-MOPD), which matches each selected teacher on a local Top-$K$ support with teacher-wise loss normalization and clipping, with an execution path that uses post-capacity bounded-width dispatch, final-route replay, and asynchronous rollout--training overlap. On Turing-20B-A2B, the selected model achieves a four-domain normalized integration score of 0.9988 and retains at least 90.16\% of the measured specialist gain in every domain. At matched $K=32$, the full calibration objective scores 0.9962, compared with 0.9724 without calibration and 0.9834 without clipping. At a matched 8K response cap, the model exceeds both shared SFT and Qwen3-8B on all four reasoning-enabled mathematics and code benchmarks (unweighted mean: 85.92, versus 80.33 for Qwen3-8B and 74.21 for SFT), and improves over SFT on ten of twelve broader evaluation metrics. In a PPU-based profile, the combined execution configuration reduces consolidation step time from 398.7 to 139.3 seconds, an observed 2.86$\times$ speedup over serial execution. These results demonstrate strong specialist integration alongside more efficient consolidation, while reflecting the complete training and execution framework rather than any single component.

---


### 261. [KARMA: Training-Free Knowledge-Atomic Harness Evolution for Industrial Advertising Agents](https://arxiv.org/abs/2610.39884)

**<font color=#1a73e8>作者：</font>** Xinhua Miao, Yuanzhen Rong, Weiru Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial advertising agents must continually adapt their decision knowledge to changing product offerings, traffic patterns, and operating policies. We present KARMA (Knowledge-Atomic, Regression-Gated Modular Adaptation), a training-free framework that evolves six typed knowledge modules while keeping model weights and executable harness code frozen. During our evolution, a deterministic Trace Verifier maps observed errors to candidate modules, and a Critic compares successful and failed trajectories to guide a tool-constrained Evolver. The Evolver applies atomic knowledge edits, which a fixed validation gate retains only when their measured gain reaches a threshold; otherwise, the previous knowledge state is restored. We evaluate KARMA with three LLM families on cases sampled from a corpus of approximately half a million real-world operation logs across six e-commerce domains. Across 18 domain--model settings, KARMA raises the average hold-out score from 30.19 to 39.15 (+8.96 points, +29.7%). Ablations show that removing either successful or failed trajectories more than halves the average hold-out gain. Evolved knowledge also transfers across domains without further adaptation, yielding an average hold-out gain of 8.54 points across all source--target pairs. By linking retained patches to their diagnostic evidence and validation outcomes, KARMA supports inspectable, reversible knowledge adaptation for agents in Web marketplaces.

---


### 262. [sDMD: Sinkhorn Distribution Matching Distillation](https://arxiv.org/abs/2610.39889)

**<font color=#1a73e8>作者：</font>** Jaihoon Kim, Lingxiao Li, Soshi Shimada 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distribution Matching Distillation (DMD) distills multi-step diffusion models into few-step generators by minimizing reverse KL divergence. Despite its strong performance, DMD guides samples by local density alone, which introduces two limitations: teacher scores can be unreliable in regions of low teacher density, and the mode-seeking behavior of reverse KL can collapse the student onto a subset of the teacher modes. We first connect DMD to Wasserstein gradient flow, showing that its gradient follows from a fixed-point formulation with integral KL (IKL) as the energy functional. This perspective motivates augmenting IKL with an optimal transport term that addresses these limitations by guiding outlier samples toward the target and promoting mode coverage. We realize this term using Sinkhorn divergence estimated from finite batches. In practice, however, errors in the estimated Sinkhorn velocity can perturb in-domain samples for which IKL guidance is already accurate. To this end, we introduce sDMD, which adaptively activates the Sinkhorn correction based on discriminator outputs, focusing on outlier samples where IKL may be unreliable. With 2--4 sampling steps on FLUX.1-dev, Qwen-Image-20B, and Wan2.1-14B, sDMD outperforms distillation baselines on GenEval, DPG, WISE, and VBench while improving sample diversity over DMD2.

---


### 263. [TACFormer: Transformer-Based Generative Model for Target-Conditioned De Novo PROTAC Design](https://arxiv.org/abs/2610.39891)

**<font color=#1a73e8>作者：</font>** Yossra Gharbi, Rocío Mercado  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Targeted protein degradation (TPD) represents a fundamental shift in drug discovery, moving beyond traditional target inhibition toward the event-driven removal of disease-causing proteins. A prominent strategy for TPD is the use of proteolysis-targeting chimeras (PROTACs), heterobifunctional molecules that selectively route a protein of interest (POI) to the ubiquitin-proteasome system for degradation. While PROTAC design still relies heavily on trial-and-error synthesis and experimental testing, deep generative models offer a promising means to explore PROTAC chemical space in silico and generate novel molecules. However, many existing generative methods formulate PROTAC design primarily as a linker-generation problem, with POI-binding (warhead) and E3-ligase-binding components fixed in advance. This restricts exploration of the full PROTAC chemical space and often leaves the POI implicit through the predefined warhead, rather than using protein-level information as an explicit conditioning signal during generation. To address these limitations, we propose TACFormer: a transformer-based generative model for target-aware de novo PROTAC design. The model conditions a GPT-style molecular decoder on pretrained ESM-2 representations of POI sequences, allowing POI-level information to steer full-molecule generation. Our results show that TACFormer generates highly novel and chemically diverse PROTACs while showing consistent POI-dependent shifts in generated chemical space. In particular, molecules generated under specific target conditions preferentially populate chemical neighborhoods associated with POIs in the held-out dataset, while extrapolating to novel chemotypes. By natively integrating biological context into the generative process, TACFormer moves PROTAC design toward a more biology-informed exploration of degrader chemical space.

---


### 264. [Prompts and probabilities in the linguistic assessment of language models: Evidence from semantic focus-sensitivity](https://arxiv.org/abs/2610.39923)

**<font color=#1a73e8>作者：</font>** Robert Pasternak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As language models (LMs) have improved, an increasingly common means of evaluating their linguistic competence is through explicit prompting (e.g., "Which sentence is more acceptable?"). Prior work indicates that such prompting underperforms compared to standard token-probability-based methods in smaller models, but improves in larger models. We test this in a new domain: semantic focus-sensitivity, responsible for contrasts like "Lucy only SWAM yesterday" vs. "Lucy only swam YESTERDAY". Testing models of various sizes using text-based focus markers like boldface and italics, we find universal above-chance performance for token probabilities. Prompting results mostly align with previous findings, but in some larger models they outperform probabilities by a wide margin. We propose that this is because LMs are not prone to produce out-of-the-blue focus marking, which muddies results from token probabilities in a way that does not affect prompting. We test this by replacing standard focus markers with randomly generated ones; token probabilities still beat chance but show significantly greater performance decrease compared to prompting. These results suggest that metalinguistic prompting, while non-trivial for LMs, can also be more robust when testing stylistically atypical data. We argue that this has important consequences for the assessment of LMs' language competence, even if LMs do not perform metalinguistic judgments through human-like introspection.

---


### 265. [PhysAg3D: Bridging 3D Generative and Agentic Models for High-Fidelity and Physically-Interactive Assets](https://arxiv.org/abs/2610.39924)

**<font color=#1a73e8>作者：</font>** Bi'an Du, Fanpeng Meng, Jiemin Fang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating interactive 3D assets from a single image requires realistic appearance, fidelity to the depicted object, and plausible physical behavior. Yet detailed geometry alone does not determine how an object should move or deform. We introduce PhysAg3D, which couples 3D generative models with agentic reasoning and tool use. A vision-language agent first infers semantic parts, candidate interactions, and physical priors from the image; a 3D generator then produces a textured whole-object mesh from the same image. A hierarchical interaction representation links these revisable priors to mechanisms and the generated surfaces they control, organizing interaction construction and refinement. Guided by this representation and observations of the mesh, the agent uses geometric and physical tools to construct parts, joints, deformable regions, and surface bindings while retaining useful generated geometry and materials. Rendered interactions and execution measurements guide targeted revisions within a fixed budget. The framework accommodates both rigid articulation and compliant deformation. Quantitative and qualitative evaluations on real photographs and external benchmarks demonstrate detailed, image-aligned assets with plausible interactions. Ablations support bounded refinement and source-surface preservation. Project Page: this http URL.

---


### 266. [Low-Bit GDN Recurrent-State Quantization: Global Gradient-aware Allocation and Pure-Write Sliding Windows](https://arxiv.org/abs/2610.39931)

**<font color=#1a73e8>作者：</font>** Qinghang Huang, Xuchu Huang, Xunzhao Yin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention stores historical information in a recurrent state of fixed size, providing a compact memory representation for long-context inference. Reducing state precision further lowers per-request storage requirements, but quantized writeback errors enter subsequent recurrences, degrade prediction quality on long-reasoning tasks, and can be accompanied by repetitive generation and excessively long outputs. We propose Global Gradient-aware Allocation (GGA) and the Pure-Write Sliding Window (PW) to address precision allocation and recent-information maintenance. GGA combines candidate quantization residuals with gradient sensitivity to future prediction loss to allocate head bit widths under a model-wide mixed-precision budget. PW independently maintains recent pure writes as FP8 vector pairs, propagates them through the full GDN state transition, and merges them into the low-bit historical state only after they leave the window. Across seven evaluations on Qwen3.5-4B/9B, GGA allocation alone improves over STEPQuant@4 by 19.48/29.84 percentage points. Adding PW-S8 yields seven-task macro-averages of 69.83%/78.63%, improving over STEPQuant@4 by 38.39/41.21 percentage points, respectively. Both precision reallocation and window maintenance improve task scores while mitigating excessively long outputs: at @6, GGA reduces mean generation length, averaged equally across tasks, by 10.45%/14.65% relative to STEPQuant; adding PW-S8 to GGA@4 further reduces mean generation length by 32.32%/36.77%. Comparisons at similar storage budgets further show that using additional capacity to maintain recent writes yields higher task scores and shorter mean outputs than solely increasing the bit width of the accumulated state.

---


### 267. [H$^2$R: Hierarchical Hint-Based Reward for Mathematical Reasoning via Reinforcement Learning](https://arxiv.org/abs/2610.39934)

**<font color=#1a73e8>作者：</font>** He Tu, Siye Li, Hongyi Wen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards has shown great promise in enhancing mathematical reasoning in large language models. However, existing approaches provide limited intermediate supervision for complex, multi-step reasoning tasks. To bridge this gap, we propose \textbf{Hierarchical Hint-based Reward}, a framework that leverages the intrinsic sub-question structure of mathematical problems as structured intermediate conditioning signals during RLVR training. Unlike chain-of-thought prompting, these hierarchical hints serve as logically grounded intermediate milestones that effectively reduce the reasoning horizon toward the final answer. To validate this framework, we introduce \textbf{HiMath}, a benchmark of hierarchically structured mathematical problems. Across diverse LLMs, hierarchical hints consistently improve reasoning performance even without task-specific training. When integrated into RL training via H$^2$R, they boost Qwen2.5-Math-7B accuracy on HiMath from 30.4\% to 39.1\% using hierarchical hints, and up to 45.6\% with Oracle Hierarchical Hints. This pronounced improvement demonstrates that incorporating reliable intermediate checkpoints into reward design is essential for sustaining complex mathematical reasoning.

---


### 268. [MLLM-GS: Multimodal Large Language Model Prior-Guided Fast Novel View Synthesis in Extreme Environments](https://arxiv.org/abs/2610.39936)

**<font color=#1a73e8>作者：</font>** Zhiliang Wu, Xinye Zheng, Kun Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view synthesis (NVS) in degraded scenes aims to reconstruct 3D scenes from multi-view observations affected by various degradations, and to generate clear and photorealistic images at unseen viewpoints. Despite recent advances, existing methods often rely on degradation-specific models, limiting their generalization across diverse extreme environments. Generative models provide rich visual priors, but their outputs often suffer from pixel misalignment and color deviations, which can propagate into the reconstructed 3D scene and compromise reconstruction quality. Furthermore, the high computational and memory costs of 3D reconstruction hinder the practical application of NVS in extreme environments. To this end, we propose MLLM-GS, a multimodal large language model (MLLM) prior-guided framework for fast NVS in extreme environments. MLLM-GS consists of two branches: MLLM prior-guided view enhancement and fast 3D scene reconstruction. The former leverages the rich visual priors of a frozen MLLM to enhance views under different severe degradations and introduces a lightweight correction network to reduce pixel shifts and color distortions in MLLM outputs. With supervision from only a few paired clean views, this branch produces reliable enhanced views for all degraded observations, providing pseudo-GT views for subsequent 3D reconstruction. The latter improves 3DGS efficiency by optimizing rasterization, Gaussian memory layout, and parameter updates, reducing redundant computation, memory-access overhead, and optimization costs. Extensive experiments on multiple degraded scenes demonstrate that MLLM-GS effectively handles various severe degradations and achieves high-quality NVS with significantly lower reconstruction time and memory consumption. Project Page: this https URL

---


### 269. [Can LLMs Ignore What They Know? Measuring Knowledge Leakage in Persona-Based User Simulation](https://arxiv.org/abs/2610.39939)

**<font color=#1a73e8>作者：</font>** Sangmin Lee, Sangwon Lee, Sungbeom Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When persona-conditioned responses are read as respondent-level simulations, each response should reflect the described persona's knowledge, and the respondent written to know nothing must act as if the model's knowledge were not there. We test whether it can, and find persistent favourable-item real-twin rating separation under the tested low-knowledge and explicit-ignorance prompts. We define the resulting problem (knowledge leakage: a response bias that arises when knowledge the real user could not have enters the simulated response) and present a methodology for measuring it quantitatively. The core instrument pairs real items with fabricated twins matched in surface form: screened fabricated variants designed to minimize prior item-specific knowledge. The paired difference therefore provides a diagnostic contrast for knowledge leakage even in rating tasks where no answer is correct. In a rating experiment across three knowledge-handling arms and five API endpoints from two model families, we find, first, that the personas we test do not fully suppress real-item existence and familiarity signals: a favourable-item real-twin rating contrast remains under an explicit in-context statement that the persona has never heard of the item. Second, the unfavourable-item contrast reverses sign across domain groups: pooling all unfavourable-content items across domains the contrast sits near zero (+0.077 [-0.057, +0.204]), yet the same estimator in the same conditions returns -0.359 where the rating scale asks about an item's documented hazard and +0.438 where it asks about a company or an organisation. A pooled analysis of unfavourable-content items against zero therefore does not detect the opposing domain-group differences. All estimates are conditional on the adequacy of twin construction and screening; human low-knowledge baselines remain necessary for population-level interpretation.

---


### 270. [Mind The Gap (MTG-AD): Dataset and Fine-grained Evaluation for End-to-End Inline Audio Descriptions](https://arxiv.org/abs/2610.39955)

**<font color=#1a73e8>作者：</font>** Subhashini Venugopalan, Jenny Tan, Taylor Roper 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio descriptions (AD) are essential for making visual media accessible to blind and low-vision (BLV) users. While Multimodal Large Language Models (MLLMs) offer a scalable solution for generating audio descriptions on-demand, their performance on ``inline'' audio descriptions -- which must fit within existing silences in a video -- remains under-explored, particularly for diverse user-generated content (UGC). We present a comprehensive investigation into MLLM-generated inline audio descriptions. First, we introduce MTG-AD, a professionally annotated dataset of 36 hours of videos, each averaging $\sim$5 mins. and 8k+ descriptions in total, co-created by paired blind and sighted AD professionals to provide a high-quality benchmark for this task. Second, we propose MTG-AD-Eval, an evaluation framework based on audio description expert guidelines that provides fine-grained, reference-free actionable metrics for model improvement. Crucially, our framework evaluates the end-to-end task: it renders the generated scripts into audio tracks to assess their fit within the original video's natural silences, minimizing disruptive overlaps. Our analysis across frontier MLLMs reveals that while models accurately describe visual events and substantially reduce speech overlaps, gaps persist in narrative pacing and flow. Finally, we empirically validate that our automated and reference-free metrics correlate significantly with human quality ratings from sighted raters and 7 BLV participants, finding that while users narrowly prefer human-authored audio descriptions, they find MLLM-generated audio descriptions highly beneficial for comprehension. We provide actionable system design guidance and release MTG-AD at this https URL and MTG-AD-Eval at this https URL.

---


### 271. [AI Cosmos: An Agentic Infra for Situated Learning](https://arxiv.org/abs/2610.40031)

**<font color=#1a73e8>作者：</font>** AI Cosmos Team, Jinfeng Zhou, Yuxuan Chen 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can improve task performance during learning, yet these gains do not necessarily reflect learners' ability to thereafter apply the knowledge and skills independently. We present AI Cosmos, an agentic infrastructure for situated learning that organizes learning around two complementary principles: scenario-based participation and cumulative assets of practice. AI Cosmos organizes learners and role-specialized agents within learning scenarios that integrate task-relevant knowledge and, when needed, executable workbenches. An asset-memory loop preserves the processes and outcomes of practice as reusable assets with explicit provenance and dependencies. We evaluate scenario-based interaction through two preregistered randomized controlled studies examining the acquisition of legal reasoning and programming competence, holding the same underlying LLM across conditions. AI Cosmos achieves greater learning gains than a conventional LLM in legal reasoning and higher mastery of unseen programming problems than an LLM-as-Teacher baseline.

---


### 272. [Hybrid AI Patterns: Thirteen Ways to Couple Language Models with Rules, and How to Choose Among Them](https://arxiv.org/abs/2610.40036)

**<font color=#1a73e8>作者：</font>** Siegfried Handschuh, Götz-Henrik Wiegand, Lorena Raichle  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models handle text well, and rule engines give conclusions with proofs. Systems that combine the two are usually described by example, and the same coupling turns up under different names in agent frameworks, guardrail toolkits and neuro-symbolic research. This document defines thirteen patterns for coupling a language model with an executable rule language, in the catalogue form introduced for object-oriented design: intent, motivation, applicability, participants, collaborations, consequences, implementation, known uses and related patterns. Four patterns concern what crosses the boundary between model and rules, five who controls whom, three how the model takes part in the reasoning, and one how knowledge is kept over time. Five invariants hold for every combination, and five failure patterns name the couplings that break them. We relate the catalogue to published pattern catalogues and taxonomies of hybrid and neuro-symbolic systems and show where they overlap with it. A decision guide leads from a problem to a pattern. It rests on our measurements, including the cases in which a model alone did as well as the hybrid or better, and it reports what each design cost.

---


### 273. [Rethinking Pre-pretraining](https://arxiv.org/abs/2610.40051)

**<font color=#1a73e8>作者：</font>** Alexander Stern, Tim Rocktäschel, Acyr Locatelli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We report that allocating compute to synthetic pre-pretraining (PPT) never outperforms pure natural-language training in our compute-matched experiments. This holds across four PPT curricula (k-Dyck, neural cellular automata (NCA), declarative reference corpora, and code) and three training regimes: data-constrained, data-unconstrained, and a high token-to-parameter-ratio regime (881M parameters trained on 50B tokens). When natural language is scarce, repeated epochs over a 100M-token corpus beat every synthetic curriculum on natural-language validation loss, with no consistent downstream accuracy advantage from PPT. We find that PPT gains reported in prior work are sensitive to the weight initialization scheme. In an NCA reproduction, we recover a 5.4% perplexity improvement from PPT under the original initialization scheme. An alternative scheme improves both methods, but the no-PPT baseline more, closing the gap between them. However, when PPT receives additional compute rather than a share of the natural-language budget, gains persist at small natural-language budgets even with improved initialization, but disappear by 1B tokens. Finally, models forget what they learn during PPT in subsequent natural-language training; interleaving the same data throughout training prevents forgetting, but does not significantly improve natural-language performance. Our results suggest limited benefits of synthetic pre-pretraining as a distinct training stage and motivate rethinking how such data are used in language model training.

---


### 274. [One Vector or Many? Clustered Optimal-Transport Steering under Quantization](https://arxiv.org/abs/2610.40055)

**<font color=#1a73e8>作者：</font>** Illia Makarov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering changes what a language model generates by editing its hidden states at inference time. Its most common form adds one vector, the difference of class means (DiM), to every hidden state. CHaRS (concept heterogeneity-aware representation steering) uses optimal transport instead: an entropic plan pairs the clusters of the two classes, and each hidden state moves along a mixture of the cluster displacements, weighted toward its nearest clusters. We study this family of clustered optimal-transport maps for toxicity mitigation in Gemma-2-2B and Granite-3.1-2B, and ask what the plan adds to DiM and whether that survives INT8 and NF4 quantization.
We prove an identity: whatever the plan, the displacements averaged with the cluster sizes as weights equal DiM, so a clustered map can differ from DiM only for tokens whose routing weights depart from the cluster sizes. In the CHaRS protocol they stay close, and CHaRS is statistically equivalent to Mean-AcT, which adds DiM at every layer, in all eight pre-specified equivalence tests. A variant fitted on individual tokens, which routes each token mainly to its nearest clusters, leaves 37-39% less toxicity than DiM on Gemma and 51-61% less on Granite at steering strength 3 (toxic-bert), where DiM already removes 76-85% of it. Two other toxicity classifiers confirm the gain on Granite, but on Gemma only one does. At equal strength the variant has somewhat higher perplexity, but at matched toxicity it is slightly more fluent than DiM. Yet a nearly constant map from the same clusters also leaves about 30% less toxicity, so the role of treating tokens differently remains open.
Under INT8 and NF4 the variant still leaves less toxicity than DiM, and transferring it from full precision to the NF4 model instead of refitting it adds no significant toxicity after correction for multiple tests.

---


### 275. [Upcycling Language Models for Multiple Specialized Domains](https://arxiv.org/abs/2610.40091)

**<font color=#1a73e8>作者：</font>** Mingzi Cao, Xi Wang, Nikolaos Aletras  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective multi-domain adaptation of large language models requires prioritizing relevant domain knowledge while minimizing interference from irrelevant domains. Existing approaches commonly use Low-Rank Adaptation (LoRA) to train a separate adapter for each domain and combine these adapters within one model. However, they either weight adapters equally regardless of the input domain or dynamically weight adapters while still activating all of them including irrelevant ones. Additionally, while efficient, their low-rank structure limits performance. In contrast, upcycling is a model expansion method that adds experts and a router to a dense Transformer layer offering larger capacity than LoRA approaches. In this paper, we propose Domain-Specialized Upcycling (DS-Upcycling) for multi-domain adaptation. We introduce a new domain-aware supervision that allows the router to effectively learn to distinguish domains by selecting the appropriate experts. During fine-tuning on each new domain, we update only the corresponding expert and router while freezing all other parameters. Experiments show that our method achieves the highest average performance across the adapted domains compared to baselines while retaining general performance. With just 256 examples per domain for router supervision, DS-Upcycling achieves 90-98% routing accuracy after adaptation compared with 43-70% for routers trained without our approach.

---


### 276. [RepConTUR: A Report-Conditioned Volumetric Multimodal Model for Abdominal Tumor Segmentation](https://arxiv.org/abs/2610.40094)

**<font color=#1a73e8>作者：</font>** Seunghwan Lee, Sangjoon Park, Jongmin Lee 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tumor delineation is required for radiotherapy planning, yet automatic segmentation is limited by errors, predominantly false positives, that distort dose and increase editing time. The radiology report accompanies the scan and localizes disease at the suborgan level, but existing text-promptable models condition on short referring phrases, and most operate in 2D. We present RepConTUR, a single native-3D early-fusion multimodal model that conditions volumetric abdominal tumor segmentation on the narrative report. We extend AbdomenAtlas 3.0 to a suborgan-level promptable segmentation dataset and generate report-based VQA pairs, yielding four report-derived tasks on the same annotations: referring segmentation (RES), report-grounded segmentation (GSEG), report generation (RRG), and visual question answering (VQA). We train RepConTUR, comprising a 3D CT encoder, an early-fusion language model, and a native-3D segmentation module, jointly on the four tasks. Across liver, kidney and pancreas, RepConTUR attains the highest Dice similarity coefficient (DSC), instance-wise precision, and detection F1 among the text-promptable baselines, and adding the report raises mean precision while leaving recall comparable. Against two vision-only specialists, nnU-Net and the report-supervised R-Super, RepConTUR attains the highest value on every in-domain metric for liver and pancreas and the highest mean DSC, recall, precision, and detection F1 over the four out-of-distribution public cohorts. Ablations indicate that conditioning on the narrative report raises detection F1 from 0.499 to 0.528 within the same model, that joint GSEG training raises RES F1 from 0.450 to 0.482, and that the native-3D segmentation module raises GSEG F1 from 0.139 to 0.528 over its 2D counterpart. Code is available at this https URL.

---


### 277. [It Takes Two to Probe, Thousands to Retrieve: Putting Vision--Language Probes to the Retrieval Test](https://arxiv.org/abs/2610.40124)

**<font color=#1a73e8>作者：</font>** Ivana Beňová, Michal Gregor, Marián Šimko  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision--language models (VLMs) are tested for fine-grained understanding with image--text matching probes, a model must prefer the correct image or caption over handcrafted negative. In retrieval, the correct item must beat thousands of alternatives. We measure how these two evaluation methods relate by using two probing benchmarks, \svo{} and SugarCrepe, for retrieval tasks. For 100 image and caption queries we judge the top-10 retrievals from full dataset of six VLMs, with human annotators and an LLM assessor. We than compare how well models rank pool of items on the same queries, while changing only where the negatives comes from: the benchmark, a random draw, or the judged-incorrect retrievals of other models. On \svo{} the accuracy of retrieving a positive over handcrafted negatives is significantly higher than for retrieved ones (the correct item is preferred in 85\% against 77\% of the time). Using pool of ten retrieved negatives leads to same accuracy as when one uses pool of 200 to 430 random negatives. On SugarCrepe the order is reversed: its handcrafted negatives are harder than the retrieved ones. Incomplete relevance labels explain most of the low retrieval scores on \svo{}, where the top-ranked item is correct for 54--90\% of the queries under human labels against 6--21\% under the benchmark's labels. However, we detect no association between passing the probe for a query and retrieving a correct item first. The LLM assessor o3 agrees with individual annotators ($\kappa$ 0.57--0.61) slightly less than they agree with each other (0.64--0.68).

---


### 278. [VideoMemBench: How Well Do MLLMs Remember in Video Conversations?](https://arxiv.org/abs/2610.40131)

**<font color=#1a73e8>作者：</font>** Zhengdong Hu, Chao Wang, Kaituo Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) can now process hour-long videos, making extended multi-turn dialogue over a single video a natural mode of use. Sustaining such a dialogue requires more than answering each question in isolation: the model must retrieve and reuse information established earlier in the conversation, both what it has seen and what it has said, an ability we term in-context video memory. Existing video QA benchmarks leave this ability unmeasured: their questions are mutually independent, never reference one another, and each is answerable from the video alone, so nothing ever requires carrying information across turns. We introduce VideoMemBench, in which each sample pairs a single video with a long multi-turn dialogue, whose turns are connected by typed cross-turn dependencies: an Episodic Dependency refers back to a visual episode described in an earlier turn, probing memory of what the model has seen, while an Answer Dependency builds on the model's own earlier answer, probing memory of what the model has said. Every dependency is verified considering two properties: 1) necessity, meaning the question cannot be answered without its earlier turns, and 2) non-leakage, meaning the question does not restate the information from its earlier turns. To enforce these properties, we design a construction pipeline with three LLM roles: a planner, a generator, and a judger, with each dialogue reviewed by human experts. VideoMemBench comprises 326 videos with 2,476 turns, of which 1,387 depend on earlier turns, including multi-parent dependencies and long-range call-back. Among over 20 evaluated open- and closed-source MLLMs, Claude Opus 5 performs the best with an overall score of only 45.7\%, highlighting the challenge of in-context video memory. Our dataset and evaluation are released.

---


### 279. [Mode Dynamics: A Framework for Neural Network Learning](https://arxiv.org/abs/2610.40143)

**<font color=#1a73e8>作者：</font>** Hossein Honarvar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Mode Dynamics, a framework that connects coordinated parameter motion during neural network learning to changes in model outputs. Starting from a recorded parameter trajectory, we decompose its updates into collective modes and map each mode to its state-dependent output effect. The framework organizes this link through three mechanisms. Decomposition identifies collective modes in parameter motion and their time-varying amplitudes. Reconstruction tests whether the effects induced by those modes recover local and accumulated output change. Concentration quantifies how behavioral contribution is distributed across modes. Controlled scalar regression and next-token experiments directly test these mechanisms. They show that small sets of leading modes reconstruct behavior, induced effects depend on the training path, and modal complexity varies with task and data. We then evaluate the framework on held-out image and language-model outputs using CIFAR-100 autoencoding and a public Pythia-70M pretraining trajectory. Across these settings, the results connect compact modal subspaces of recorded parameter motion to evolving behavior.

---


### 280. [The generative paradox: the Anti-Prompt paradigm for human capability](https://arxiv.org/abs/2610.40151)

**<font color=#1a73e8>作者：</font>** Margarita Trifonov Vadim E. Levit  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative AI in education is usually judged by the output of human-AI teams. That focus overlooks a second outcome: what people can still understand, challenge, repair, and adapt when assistance changes or disappears. We call this tension the generative paradox and distinguish four manifestations: performance, assistance, ownership, and capability stock. We propose developmental function allocation, which complements operational function allocation and meaningful human control by treating retained human capability as a design objective alongside current joint performance. The Anti-Prompt paradigm reverses the default interaction order: when immediate generation would preempt a consequential human act, AI should first create the conditions for human construction. We distinguish the validity of a product, responsibility for its construction, and evidence of capability after support changes. Representative Anti-Prompts, a canonical interaction sequence, and stress tests spanning mathematical reasoning, experimental science, software diagnosis, and lesson design make these distinctions concrete. We conclude with falsifiable predictions about retained capability and a system-level hypothesis about the reproduction and distribution of expertise.

---


### 281. [Hierarchical Step Decomposition for Training-free Online Video Step Grounding](https://arxiv.org/abs/2610.40153)

**<font color=#1a73e8>作者：</font>** Long Zhou, Luca Zanella, Paolo Rota 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given a set of procedural steps, Video Step Grounding (VSG) aims to identify which steps occur in a video and localize when they are performed. Existing methods are either offline, requiring access to the full video before making predictions, or online, but relying on fixed-length video segments producing noisy, over-segmented outputs. In this work, we propose Hierarchical Step Decomposition (HSD), a training-free framework for online VSG that leverages the semantic understanding capabilities of Large Multimodal Models. HSD addresses two central challenges in online grounding: constructing semantically coherent temporal segments from a streaming video, and bridging the semantic gap between coarse procedural step descriptions and visual observations. To construct elementary temporal units, HSD incrementally groups incoming segments into semantically consistent events, using an anchor caption that is continuously validated against the visual stream. Based on these events, we perform zero-shot procedural step classification and selectively refine uncertain predictions by decomposing candidate steps into finegrained substeps that capture more nuanced visual evidence. By operating on semantically coherent events rather than every fixed-length segment, HSD reduces redundant computation and produces more stable predictions. Experiments on HT-Step, Ego4D Goal-Step, and CrossTask show that HSD substantially outperforms state-of-the-art methods, overall achieving better step recognition, more accurate temporal localization, and faster inference.

---


### 282. [A Negotiation-Aware Hybrid LLM Framework for Intent Interpretation and Service Discovery](https://arxiv.org/abs/2610.40161)

**<font color=#1a73e8>作者：</font>** Wided Meflah, Hayet Brabra, Walid Gaaloul  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Increasingly, users express their needs as natural-language intents rather than structured requests. These intents may be incomplete, high-level, or internally conflicting. A conflicting intent either violates fundamental properties of the cloud paradigm or states mutually inconsistent requirements. Classical composition approaches are designed for structured, low-level, and complete requests. They cannot interpret such intents, discover suitable services from provider catalogs, or negotiate conflicting requirements with users. To address this gap, we propose a negotiation-aware framework for intent interpretation and service discovery. The framework first refines the natural-language intent and dynamically detects conflicts. It then structures the intent into a provider-independent TOSCA template. For each specification, it retrieves candidate service offers through deterministic matching grounded in cloud provider offerings. Some conflicts arise during interpretation. Other requirements prove unsatisfiable during discovery. Both are resolved through iterative natural-language negotiation with the user. We evaluate the framework on 70 diverse intents against single-shot and enhanced-prompting baselines. It improves recall and F1 for both conflict detection and service discovery. It also eliminates hallucinated offers and resolves conflicts at a cost proportional to their number.

---


### 283. [Locating and Closing Information Gaps in Multi-Agent Systems](https://arxiv.org/abs/2610.40186)

**<font color=#1a73e8>作者：</font>** Yaxin Gong, Chongming Gao, Gangyi Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-step Web tasks often require several LLM agents to gather and combine evidence. The communication graph of a fixed workflow restricts which agents can read each other's outputs: evidence retrieved by one agent may never reach the agent that needs it, leaving an information gap and an incomplete or incorrect answer. Adding a connection can deliver the missing evidence, but can also lead the receiver to adopt an incorrect upstream conclusion that displaces a correct answer; the final output alone does not separate the two. We propose Selective Probing and Link Insertion for Closing information gaps in multi-agent Execution (SPLICE), which locates information gaps per query and decides what to adopt after adding an edge. After the original workflow runs, SPLICE uses the query and node outputs to locate a possible gap, adds one directed edge from a source to a receiver to deliver the relevant evidence, and re-executes the receiver and affected downstream nodes, producing a candidate answer. The adoption decision reads both the final answers of the two runs and the process changes the edit caused inside the workflow: how far the receiver moved, where its new content came from, and whether the change reached the final answer. A selector trained on these process features chooses between adopting the candidate answer and retaining the original. On five benchmarks, SPLICE raises the task score on Web tool use by 8.0% and the mean score on four reasoning and planning benchmarks by 5.7% relative to the static skeleton, at 1.25 to 1.44$\times$ the skeleton's cost, and transfers zero-shot to four unseen backbones.

---


### 284. [AdMuse: Skill-Guided Creative Advertising Image Generation](https://arxiv.org/abs/2610.40190)

**<font color=#1a73e8>作者：</font>** Minyan Luo, Yuxin Zhang, Meng Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An outstanding creative advertising image should both attract attention and communicate a product's positioning. How to choose a persuasive conceptual bridge before rendering begins is challenging for advertising generation. We present AdMuse, a skill-guided multi-agent framework that distills high-quality advertisements into reusable creative skills for cross-domain advertising strategy. Rather than retrieving isolated exemplars, AdMuse abstracts recurring bridge patterns into a skill library that can guide new product briefs. At generation time, AdMuse coordinates skill routing, multi-candidate ideation and selection, and VLM-guided visual refinement: diverse skills propose alternative concepts, relative judgment selects the most promising direction, and vision-language feedback helps realize the selected intent in the final image. This design treats advertising creativity as a structured decision process rather than a single prompt-writing step. Experiments across diverse product and brand positionings show that AdMuse produces visually compelling advertisements that faithfully communicate product positioning.

---


### 285. [Bridging Semantics and Structure: A Theoretically Grounded Framework for Link Prediction on TAGs](https://arxiv.org/abs/2610.40192)

**<font color=#1a73e8>作者：</font>** Chen Shao, Ruirui Wang, Tobias Kafer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Link prediction on text-attributed graphs (TAGs) is a fundamental problem with applications in knowledge discovery, recommendation and beyond. Recent progress has highlighted the promise of combining Graph Neural Networks (GNNs) with Language Models (LMs) in order to leverage the complementary structural and semantic signals. However, due to the distinct inductive biases of GNNs and LMs, the design of an optimal fusion strategy remains an open research question. In this work, we present Bridge-LP, an intuitive, simple, efficient and theoretically grounded framework that unifies graph and language representations. It is built around three theoretically-justified design components: (D1) jumping connection of textual proximity, which enables robust LM training; (D2) compressed embedding, which encodes neighborhood information long exploited by classical link prediction heuristics, thereby enriching structural signals in a learnable way; and (D3) cache embedding training strategy, which reduces computational complexity. Together, these mechanisms establish an end-to-end cross-modal framework that scales to large graphs while capturing richer graph-text interactions. We conduct an extensive empirical evaluation, comparing against 40 existing models across 9 diverse datasets. Experiments show that Bridge-LP consistently outperforms state-of-the-art approaches, delivering up to a 43.06% improvement in Mean Reciprocal Rank (MRR) and setting a new benchmark for language-graph integration.

---


### 286. [Towards Full-Text Scholarly Argument Mining using Entity-Anchored Claim Extraction](https://arxiv.org/abs/2610.40196)

**<font color=#1a73e8>作者：</font>** Bhuvanesh Verma, Andy Lüking, Mounika Marreddy 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Argument mining in full-text scholarly articles remains an important yet challenging task. This difficulty stems not only from the need to model long-distance dependencies but also from the substantial effort required to annotate sentence-level argumentative components throughout lengthy documents. To address these challenges, we introduce a novel approach that leverages scientific entity mentions (e.g., tasks, datasets, and models) to identify and structure claims in scholarly literature. We validate our approach through a case study involving 50 full-text research papers on sentiment analysis. We first establish a reliable human gold standard (Krippendorff's $\alpha = 0.80$), identifying 113 claim-bearing sentences and extracting 199 structured claim records from 300 candidate sentences. To address the annotation bottleneck, we employ a majority-voting ensemble of large language models (LLMs) to generate a silver-standard dataset comprising 1,487 claims. Encoders fine-tuned exclusively on the silver-standard dataset outperform those trained on a small human-annotated gold-standard dataset and demonstrate strong zero-shot transfer to NLP papers outside the training corpus.

---


### 287. [Benchmarking color judgment in multimodal LLMs with CIE-computable ground truth](https://arxiv.org/abs/2610.40212)

**<font color=#1a73e8>作者：</font>** Shuwei Yue, Kaida Xiao, Zhihua Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are now used as zero-shot judges of image quality, but their color judgments are rarely tested with colorimetric ground truth. We present a five-task benchmark based on the CIE colorimetric framework: AWB pair judgment, skin-tone bias direction, CCT estimation, CIE Delta E 2000 pair ordering, and color naming under changing illuminants. We test eight MLLM endpoints, including four Qwen3-VL variants, GLM-4.5V, GPT-5.4, Claude-Opus-4.7, and Gemini-3.1-Pro. The models often solve coarse binary AWB judgments, but they remain weak on numeric CCT estimation and on some fine color-difference judgments. On ColorChecker-24 stimuli, the three closed-weight frontier models reach CCT MAE of 715-1056 K, compared with 1358-2133 K for the five open-weight models. A non-ColorChecker control shows that this advantage is partly template-dependent. The results suggest that current MLLMs have useful color words and coarse visual priors, but their color judgments are not reliably calibrated to CIE-computable color differences.

---


### 288. [EpiAgent: Epistemic Self-Play for LLM Agents](https://arxiv.org/abs/2610.40227)

**<font color=#1a73e8>作者：</font>** Xuanfa Jin, Xinyu Cui, Zhijian Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Epistemic game theory explains an agent's strategic behavior via the beliefs it holds about others and how these beliefs are updated as the interactions unfold. Modern LLM-based agents, however, often lack an explicit mechanism for learning and updating such beliefs to guide decisions under incomplete information. To bridge this gap, we propose EpiAgent, a framework that equips LLM-based agents with an explicit, learnable epistemic layer, which maintains beliefs over others' private information and combines these beliefs with the agent's available information into an epistemic state for action selection. Concretely, the agent's policy is decomposed into two coupled stages: Epistemic Update, which updates these beliefs from interaction histories, and Action Planning, which selects actions conditioned on the updated epistemic state. By formulating their dependency as a bi-level optimization problem, we introduce Epistemic Self-Play, an algorithm that alternately optimizes the two stages through self-play, utilizing an intrinsic prediction reward to evaluate how well inferred beliefs predict subsequent observations. Empirical results across both mixed and competitive scenarios show that EpiAgent consistently outperforms prompting-based and RL-based baselines. Further analyses reveal the benefits of dedicated epistemic training, improvements in belief inference accuracy, and the contribution of learned beliefs to action planning. These results demonstrate the value of an explicit, learnable epistemic layer for effective multi-agent interactions.

---


### 289. [Mobilizing the Archive: Bitext Extraction at Scale from Archival Documents for Extremely Low-resource Languages](https://arxiv.org/abs/2610.40233)

**<font color=#1a73e8>作者：</font>** Chutong Meng, Alec J. Bateman, Antonios Anastasopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While mining parallel sentences from web pages has proven effective for low-resource machine translation, the majority of the world's languages have little to no web presence. What they do have, though, are resources that are the result of centuries of efforts by linguists, such as grammars, dictionaries, and other documentation materials. We propose extracting translation examples from such linguistic resources, which offer parallel data for languages under-represented online and could potentially scale to thousands more languages. We develop a pipeline to achieve this, leveraging an Optical Character Recognition (OCR) model as well as a vision language model (VLM), to ensure identified content to be aligned with visual layout information. We demonstrate the utility of the extracted bitexts for bootstrapping translation systems across 20 languages, both by training machine translation models and by applying in-context learning for large language models. For in-context learning, we observe improvements of +15.78 and +6.94 chrF2++ over zero-shot translation for into low- and high-resource languages, respectively.

---


### 290. [ScienceJudge: Pattern Perturbation Augmentation for Sentence-Level Scientific Claim Verification](https://arxiv.org/abs/2610.40238)

**<font color=#1a73e8>作者：</font>** Chuhai Cai, Xin Chen, Min Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentence-level scientific claim verification determines whether each sentence in an AI-generated scientific paragraph is supported by a given multimodal evidence bundle. Fine-grained reporting errors often preserve fluent and plausible statements while introducing subtle evidence-claim deviations, making them difficult to detect under sparse and imbalanced supervision. We propose Pattern Perturbation Augmentation (PPA), which models reporting errors as label-specific faithfulness breaking transformations and induces reusable error patterns from labeled examples. PPA applies these patterns to supported claims to construct controlled hard negatives and expands their coverage through pattern-level, operation-level, and cross-domain augmentation. Based on these augmented views, we develop ScienceJudge, which integrates PPA-trained vision-language predictors and instruction-guided LLM predictors through class-weighted ensemble inference. On the local development set, ScienceJudge improves the average score from 0.8124 to 0.8692, achieving a Macro-F1 of 0.8466 and a Paragraph Exact Match score of 0.8919. Our submitted system ranks first on the official NLPCC 2026 Task 10 Track 1 leaderboard with a final score of 0.6890.

---


### 291. [Judged in Company: In-Context Batching Makes LLM Verdicts Depend on Other Items](https://arxiv.org/abs/2610.40241)

**<font color=#1a73e8>作者：</font>** Peng Xie, Amr Alanwar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To save cost, practitioners often ask a language model to grade many independent items in one prompt. This assumes that verdicts are separable: that the verdict on an item does not depend on the other items in the prompt or on its position among them. Across three judgement tasks (harm in social-media comments, short-answer grading and review star ratings) and five open-weight models with 4-9B parameters, assigning the same 2,000 items to different random batches of 25 changes 11-22% of decisions on harm and grading, 6.5-13.3 points more than renaming the item keys or rewording the instruction, while AUROC against human labels differs from single-item grading only by -0.033 to +0.010; for four models with 14-32B parameters, 6-15% of decisions change, 4.2-9.1 points more. We show that flip rates decompose exactly into components of order, slot and membership, and that under a threshold model they grow with the square root of the variance that the context contributes, so that effects that are small for scores are large for decisions. Most of the latent dissimilarity between partitions comes from the order of the neighbours and the slot. The main effect of which items share the prompt, the part that voting over permutations of a batch cannot remove, accounts for 0.11-0.22 of it, and majority votes over nine permutations still leave 52-60% of the flips. Batched verdicts also differ systematically from single-item verdicts: even the majority of fifteen random batches disagrees with them on 8.4-17.8% of decisions. Editing a single generation shows that both the model's own earlier verdicts and the neighbours' texts carry the effect. On the easy task, star ratings, only 2.9-3.9% of decisions change. We recommend grading ambiguous items one per prompt, recovering most of the cost with a cached prefix, and reporting agreement with single-item grading whenever items are batched.

---


### 292. [EnvOS: Auditing Computer-Use Agents When the World Moves On : Phenomenon-Based Task Construction, Certification, and Evidence-Based Evaluation](https://arxiv.org/abs/2610.40246)

**<font color=#1a73e8>作者：</font>** Ankush Kadu, Athira Gopal, Niharika Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents built on large language models (LLMs) work in software that can change while they act: an appointment moves, a policy is revised, a record is updated. Testing agents under such changes is harder than it looks. When an agent fails, the cause may be the agent, but it may also be a change that did not fire as intended, an update the agent never received, or a grader that scored the episode wrongly. We introduce EnvOS, a framework for building and certifying environments that change mid-task. Before any agent runs, EnvOS checks that each change fires correctly, that the task remains solvable, and that the grader separates correct from incorrect behavior; after each run, separate code re-checks the verdict from archived evidence. We apply it to stale information, where a value the agent has already seen changes before the agent acts on it. In clinic booking, Claude Opus 5 succeeds on 0/16 tasks when nothing extra is shown, 2/16 when reminded to re-check the source, and 15/16 when the updated value is shown; the gain over the reminder holds after correcting for all tests (p = 0.00293). In insurance-claim approval, Opus 5 re-checks on its own and succeeds on 10/10, whereas Claude Sonnet 5 rises from 1/10 to 9/10 when the current policy is shown again, a gain significant in its pre-registered test but not after correcting for all tests. Whether an agent caught a change thus varied with the model and the interface. We also stress-test the grading itself: on corrupted episodes designed blind from the rules, the EnvOS pipeline accepted none of 26 as clean, and on an externally generated set it caught 25 of 39, against 4 for simple log checks. Because every EnvOS environment is generated from a seed and graded by an audited automatic verifier, the same environments are natural candidates for training agents with reinforcement learning from verifiable rewards.

---


### 293. [TaskFrame: Connecting Task-Level Planning with Frame-Level Control for Game Agents](https://arxiv.org/abs/2610.40276)

**<font color=#1a73e8>作者：</font>** Guangzhi Wang, Junfu Pu, Yiran Wang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building general game agents requires both high-level task reasoning and low-latency action control in rapidly changing visual environments. These capabilities favor models with substantially different computational profiles, making them difficult to realize within a single model. In this work, we present TaskFrame, a hierarchical planner-controller framework that connects task-level planning with frame-level keyboard-and-mouse control. A vision-language task planner decomposes a high-level goal into an ordered sequence of atomic instructions and is optimized through supervised learning and dependency-aware GRPO. The hidden states of special goal tokens that terminate each atomic instruction provide continuous goal embeddings that are cached and reused across control steps. A causal Transformer controller combines the embedding of the active goal with recent observations to predict discrete keyboard and mouse-button actions and continuous camera motion at every game step. We train the system in three stages: planner training, controller pretraining, and joint alignment. Experiments in Minecraft show that TaskFrame is competitive with general-purpose vision-language models on instruction decomposition, and that in closed-loop evaluation the agent achieves a higher combat success rate than the evaluated baselines.

---


### 294. [Neighborhood Elites: Quality-Diversity Search for Uncertainty Quantification in Question Answering](https://arxiv.org/abs/2610.40278)

**<font color=#1a73e8>作者：</font>** Mesut Ceylan, Arda Baris Basaran, Elgar Fleisch 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly capable, yet they produce wrong answers indistinguishable from correct ones. In question answering (QA), such an error propagates unnoticed into downstream tasks. Perturbation-based uncertainty quantification (UQ) addresses this by probing a model over a set of input rewrites and reading uncertainty from how much its predictions vary. Yet this set is usually built generically, by free paraphrasing, token-level perturbation, or adversarial search. Such rewrites leave two things uncontrolled that matter in QA: what kind of change is made to the context, and how explicitly the context supports the answer. When neither is controlled, the composition of the set is determined by the generator rather than by design, and the estimate inherits whatever that generator happens to produce. Quality-diversity (QD) search is built to cover a predefined exploration space, so we recast input perturbation as a QD problem and propose \emph{neighborhood elites (NE)}, a neighborhood constructor that spreads answer-preserving rewrites across two axes, the kind of edit and the explicitness of support. We compare NE against three other neighborhood constructors, holding the editor, QA model, uncertainty measure and search objective fixed, and against three scores read from the original context. Across five extractive-QA datasets and five instruction-tuned LLMs, NE improves failure detection against every other constructor in at least 24 of the 25 dataset-model pairs, reaching 0.726 AUROC and 0.211 AUPRC lift over the base rate. Additionally, NE detects failure better than semantic entropy computed over decoder samples, by 0.074 AUROC and 0.062 AUPRC lift, and this advantage widens as the neighborhood grows.

---


### 295. [Latent Path Exploration via Potential-Guided Subtrajectory Balance](https://arxiv.org/abs/2610.40283)

**<font color=#1a73e8>作者：</font>** Xiaoling Zeng, Qi Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous latent reasoning enables language models to perform intermediate computation without generating explicit reasoning traces. Advances in stochastic latent reasoning allow multiple paths to be sampled in continuous space, but stochasticity alone does not ensure effective exploration. A key challenge is guiding stochastic transitions between intermediate latent states toward useful reasoning paths. We introduce SubLAT, which couples a relative answer potential with Subtrajectory Balance to learn stochastic latent exploration. The relative potential evaluates the answer support of sampled states against replacement states, with a correctness signal at the terminal state. Subtrajectory Balance relates potential differences to forward and backward transition densities across subtrajectories of different lengths. The model is jointly trained with answer supervision, CoT supervision, and representation distillation. Experiments on arithmetic and deductive reasoning show increasing solution coverage with larger sampling budgets across in-domain and out-of-domain benchmarks, as well as improvements on several structural OOD benchmarks. Trajectory analyses reveal progressive divergence among sampled latent paths and higher mean relative potentials for correct trajectories across arithmetic benchmarks.

---


### 296. [DolphinRouting: Cluster-Level Binary Routing for Disaggregated LLM Inference Serving](https://arxiv.org/abs/2610.40292)

**<font color=#1a73e8>作者：</font>** Yishuo Yuan, Shaoyu Yang, Chunrong Fang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Prefill-decode (PD) disaggregation isolates the two phases of large language model serving, but request-level path selection must account for prefill work, cache reuse, and decode demand. We present DolphinRouting, which learns this choice from end-to-end SLO feedback under a given P/D resource allocation. Requests are clustered by raw prompt length, cache-adjusted input lengths on both worker pools, and output-length information. Offline policy search learns one binary action per cluster. Online feature extraction, cluster assignment, and table lookup select local or remote prefill. We evaluate DolphinRouting on a real PD-disaggregated cluster using three public benchmarks, a mixed workload, and real data. Across the mixed workload and real data, DolphinRouting with $k$-means reduces P90 TTFT by 5.7--7.9\% and P90 TPOT by 2.6--10.1\% relative to Dynamo.

---


### 297. [MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads](https://arxiv.org/abs/2610.40293)

**<font color=#1a73e8>作者：</font>** Shengxuan Qiu, Haochen Huang, Shuzhang Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) coordinate specialized agents to solve complex tasks, turning each user request into interdependent model and tool operations. Unlike independent requests, these operations become ready at different times and consume evolving context as agents coordinate and exchange results. This creates changing patterns of concurrency, computation, and memory demand that can expose different bottlenecks in LLM serving hardware. Yet benchmarking these effects requires capturing the collaboration rules that generate serving workloads, beyond the requests observed during execution. We present MAServeBench, a benchmark that treats multi-agent collaboration as a configurable dimension of serving workloads for LLM serving and hardware evaluation. Its composable stages capture how agents coordinate and exchange context in documented MAS workflows, enabling native executions to generate different workloads even when task inputs and tools remain unchanged. Hierarchical Semantic Traces preserve realized operations and dependencies for reproducible comparisons of legal release constraints at fixed work. Task-linked measurements connect these workloads to serving execution and GPU/NPU hardware behavior, revealing why serving efficiency does not always translate into timely task completion. The benchmark code is available at this https URL.

---


### 298. [Textual Response-Aware Guidance for Zero-Shot Adversarial Robustness of Vision-Language Models](https://arxiv.org/abs/2610.40309)

**<font color=#1a73e8>作者：</font>** Yubo Cui, Xianchao Guan, Zheng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) exhibit strong zero-shot generalization but remain vulnerable to adversarial attacks. Existing adversarial fine-tuning methods often use pre-trained model guidance to preserve image--text alignment while improving robustness. Our analysis of visual representation drift reveals complementary limitations of two representative forms of guidance. Matching visual features provides broad coverage by constraining all directions equally, but lacks semantic emphasis. Matching prediction distributions prioritizes semantically relevant directions, but remains limited by the candidate texts and prediction probabilities. These limitations can hinder preservation of pre-trained image--text relationships and degrade zero-shot performance. To address these issues, we propose Textual Response-Aware Guidance (TRAG), which constrains visual representation drift using the pre-trained text encoder's responses to local variations in input embeddings. Specifically, TRAG constructs anchor-level constraints from the response directions and magnitudes around semantic anchors, then aggregates them using pre-trained image--anchor relevance, yielding an image-adaptive constraint. Extensive experiments across architectures and tasks demonstrate state-of-the-art clean and robust performance. Further analysis shows that TRAG helps preserve pre-trained image--text relationships.

---


### 299. [Decision and System One models in rheumatology: accuracy and calibration on specialty-training examination questions and diagnostic case vignettes](https://arxiv.org/abs/2610.40318)

**<font color=#1a73e8>作者：</font>** Alfredo Madrid-García, Diego Benavent, Fabian Lechner 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Objectives: To evaluate the accuracy and calibration of Decision and System One models on rheumatology examination questions and diagnostic vignettes. Methods: Two benchmarks were analysed: 172 rheumatology questions from Spanish specialty-training examinations (expanded RheumaMIR dataset) in Spanish and English, and 70 English diagnostic vignettes from RheumBench with 5-18 candidate diagnoses, 52 of which included the reference diagnosis. Four System One models (Jev 1.13, Clef, Microsoft-Decision-1, Laya) and GPT-6 Luna (OpenAI Decisions API) were compared with GPT-6 Sol and two local generative models. The primary outcome was accuracy; secondary outcomes included calibration, discrimination, accuracy of answers with probability >=0.90 and language differences. Results: In RheumaMIR, Jev's accuracy was 93.0% in Spanish and 91.9% in English, below GPT-6 Sol (99.4%; Holm-adjusted P<=0.005); GPT-6 Luna reached 97.7%, Clef 91.9-93.0% and Microsoft-Decision-1 86.0-87.8%, without detectable language differences. Jev's answers with probability >=0.90 (76-77% of answers) were 98.5% correct. In RheumBench, accuracy was lower: GPT-6 Sol 76.9%, GPT-6 Luna 63.5%, Clef 59.6%, Jev 50.0% and Microsoft-Decision-1 40.4% (each System One model below GPT-6 Sol, Holm-adjusted P<=0.045; chance 9.6%). Jev became overconfident (mean probability 0.659; over/underconfidence index +0.159), and its answers with probability >=0.90 (25% of cases) were 84.6% correct, against 95.5% for GPT-6 Luna (42%). Laya performed near chance in both benchmarks. Conclusion: The best-performing System One models were highly accurate on examination questions but less accurate on diagnostic vignettes, remaining below GPT-6 Sol. Jev's high-confidence predictions were less reliable on vignettes, highlighting the need for task-specific evaluation and calibration.

---


### 300. [Radiology Guideline-derived Decision Graph for Efficient Clinical Decision Support](https://arxiv.org/abs/2610.40327)

**<font color=#1a73e8>作者：</font>** Xuewen Zhou, Zhen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiological risk stratification and management planning are essential downstream tasks in medical imaging. Automating these tasks is challenging because clinical guideline criteria are distributed across prose, tables, and cross-referenced definitions. We present Guideline-derived Decision Graph (GDGraph), a framework that decouples guideline compilation from case evaluation. During compilation, a large language model partitions guidelines into section-based chunks, extracts local decision subgraphs with linked definitions, and aggregates related branches into an executable decision graph. During inference, a fast System One model answers localized clinical questions while deterministic traversal resolves Boolean logic, turning opaque single-pass predictions into a traceable decision path without task-specific training. Across 347 cases spanning renal cyst, adnexal mass, and thyroid nodule guidelines, GDGraph improves System One accuracy from 57.3% to 90.8%, outperforming retrieval-augmented GPT-4o (80.1%) and graph-guided GPT-4o with chain-of-thought (82.7%) at substantially lower latency and cost. The source code will be available.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
