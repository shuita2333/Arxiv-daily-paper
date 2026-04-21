# 🧠 大模型相关研究 | 2026年04月22日

> 本类共 **353** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 251. [Do LLMs Need to See Everything? A Benchmark and Study of Failures in LLM-driven Smartphone Automation using Screentext vs. Screenshots](https://arxiv.org/abs/2604.17817)

**<font color=#1a73e8>作者：</font>** Shiquan Zhang, Tianyi Zhang, Le Fang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of large language models (LLMs), mobile agents have emerged as promising tools for phone automation, simulating human interactions on screens to accomplish complex tasks. However, these agents often suffer from low accuracy, misinterpretation of user instructions, and failure on challenging tasks, with limited prior work examining why and where they fail. To address this, we introduce DailyDroid, a benchmark of 75 tasks in five scenarios across 25 Android apps, spanning three difficulty levels to mimic everyday smartphone use. We evaluate it using text-only and multimodal (text + screenshot) inputs on GPT-4o and o4-mini across 300 trials, revealing comparable performance with multimodal inputs yielding marginally higher success rates. Through in-depth failure analysis, we compile a handbook of common failures. Our findings reveal critical issues in UI accessibility, input modalities, and LLM/app design, offering implications for future mobile agents, applications, and UI development.

---


### 252. [PDDL-Mind: Large Language Models are Capable on Belief Reasoning with Reliable State Tracking](https://arxiv.org/abs/2604.17819)

**<font color=#1a73e8>作者：</font>** Wang Bill Zhu, Qiutong Tony Yi, Robin Jia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) perform substantially below human level on existing theory-of-mind (ToM) benchmarks, even when augmented with chain-of-thought prompting or probabilistic belief updates. We argue that these failures primarily arise from unreliable implicit state tracking rather than limitations in high-level reasoning. We introduce PDDL-Mind, a neuro-symbolic framework that decouples environment state evolution from belief inference. By translating narrative descriptions into explicit states and actions expressed in Planning Domain Definition Language (PDDL), and by verifying action-induced state transitions against a predefined domain, PDDL-Mind provides LLMs with a logically consistent and explicit representation of world states for ToM tasks. Experiments on MMToM-QA, MuMA and FanToM show that PDDL-Mind achieves over 5% absolute accuracy gain over the best existing state-of-the-art method on ToM benchmark questions.

---


### 253. [Learning to Seek Help: Dynamic Collaboration Between Small and Large Language Models](https://arxiv.org/abs/2604.17827)

**<font color=#1a73e8>作者：</font>** Hang Zeng, Xiangyu Liu, Yong Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) offer strong capabilities but raise cost and privacy concerns, whereas small language models (SLMs) facilitate efficient and private local inference yet suffer from limited capacity. To synergize the complementary strengths, we introduce a dynamic collaboration framework, where an SLM learns to proactively decide how to request an LLM during multi-step reasoning, while the LLM provides adaptive feedback instead of acting as a passive tool. We further systematically investigate how collaboration strategies are shaped by SLM and LLM capabilities as well as efficiency and privacy constraints. Evaluation results reveal a distinct scaling effect: stronger SLMs become more self-reliant, while stronger LLMs enable fewer and more informative interactions. In addition, the learned dynamic collaboration strategies significantly outperform static pipelines and standalone inference, and transfer robustly to unseen LLMs.

---


### 254. [Polysemantic Experts, Monosemantic Paths: Routing as Control in MoEs](https://arxiv.org/abs/2604.17837)

**<font color=#1a73e8>作者：</font>** Charles Ye, Bo Yuan, Lee Sharkey  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM's residual stream is both state and instruction: it encodes the current context and determines the next transformation. We introduce a parameter-free decomposition for Mixture-of-Experts models that splits each layer's hidden state into a control signal that causally drives routing and an orthogonal content channel invisible to the router. Across six MoE architectures, we find that models preserve surface-level features (language, token identity, position) in the content channel, while the control signal encodes an abstract function that rotates from layer to layer. Because each routing decision is low-bandwidth, this hand-off forces compositional specialization across layers. While individual experts remain polysemantic, expert paths become monosemantic, clustering tokens by semantic function across languages and surface forms. The same token (e.g., ":") follows distinct trajectories depending on whether it serves as a type annotation, an introductory colon, or a time separator. Our decomposition identifies the source of this structure: clusters in the control subspace are substantially more monosemantic than those in the full representation. As a result, the natural unit of interpretability in MoEs is not the expert but the trajectory.

---


### 255. [QuickScope: Certifying Hard Questions in Dynamic LLM Benchmarks](https://arxiv.org/abs/2604.17842)

**<font color=#1a73e8>作者：</font>** Taylor Lundy, Narun K. Raman, Kevin Leyton-Brown  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM benchmarks are increasingly dynamic: instead of containing a fixed set of questions, they define templates and parameters that can generate an effectively unlimited number of question variants. This flexibility is valuable, but it makes evaluation expensive -- especially when the goal is not just determining an average score, but reliably identifying a model's weak spots. This paper introduces a new methodology for identifying hard questions in dynamic benchmarks. It leverages COUP, a recent Bayesian optimization algorithm (Graham, Velez & Leyton-Brown, 2026), after introducing several substantive modifications to make the algorithm suitable for practical LLM pipelines. We also wrap it in a tool that supports flexible choices of datasets and utility functions, enabling users to target the kinds of questions they care about (e.g., low-accuracy questions; questions that are unusually hard relative to their measured complexity). In experiments across a range of benchmarks, we show that our method, dubbed $\texttt{QuickScope}$, discovers truly difficult questions more sample efficiently than standard baselines, while also reducing false positives from noisy outcomes.

---


### 256. [M100: An Orchestrated Dataflow Architecture Powering General AI Computing](https://arxiv.org/abs/2604.17862)

**<font color=#1a73e8>作者：</font>** Yan Xie, Changkui Mao, Changsong Wu 等 37 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As deep learning-based AI technologies gain momentum, the demand for general-purpose AI computing architectures continues to grow. While GPGPU-based architectures offer versatility for diverse AI workloads, they often fall short in efficiency and cost-effectiveness. Various Domain-Specific Architectures (DSAs) excel at particular AI tasks but struggle to extend across broader applications or adapt to the rapidly evolving AI landscape. M100 is Li Auto's response: a performant, cost-effective architecture for AI inference in Autonomous Driving (AD), Large Language Models (LLMs), and intelligent human interactions, domains crucial to today's most competitive automobile platforms. M100 employs a dataflow parallel architecture, where compiler-architecture co-design orchestrates not only computation but, more critically, data movement across time and space. Leveraging dataflow computing efficiency, our hardware-software co-design improves system performance while reducing hardware complexity and cost. M100 largely eliminates caching: tensor computations are driven by compiler- and runtime-managed data streams flowing between computing elements and on/off-chip memories, yielding greater efficiency and scalability than cache-based systems. Another key principle was selecting the right operational granularity for scheduling, issuing, and execution across compiler, firmware, and hardware. Recognizing commonalities in AI workloads, we chose the tensor as the fundamental data element. M100 demonstrates general AI computing capability across diverse inference applications, including UniAD (for AD) and LLaMA (for LLMs). Benchmarks show M100 outperforms GPGPU architectures in AD applications with higher utilization, representing a promising direction for future general AI computing.

---


### 257. [Sharpening Lightweight Models for Generalized Polyp Segmentation: A Boundary Guided Distillation from Foundation Models](https://arxiv.org/abs/2604.17865)

**<font color=#1a73e8>作者：</font>** Shivanshu Agnihotri, Snehashis Majhi, Deepak Ranjan Nayak  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated polyp segmentation is critical for early colorectal cancer detection and its prevention, yet remains challenging due to weak boundaries, large appearance variations, and limited annotated data. Lightweight segmentation models such as U-Net, U-Net++, and PraNet offer practical efficiency for clinical deployment but struggle to capture the rich semantic and structural cues required for accurate delineation of complex polyp regions. In contrast, large Vision Foundation Models (VFMs), including SAM, OneFormer, Mask2Former, and DINOv2, exhibit strong generalization but transfer poorly to polyp segmentation due to domain mismatch, insufficient boundary sensitivity, and high computational cost. To bridge this gap, we propose \textit{\textbf{LiteBounD}, a \underline{Li}gh\underline{t}w\underline{e}ight \underline{Boun}dary-guided \underline{D}istillation} framework that transfers complementary semantic and structural priors from multiple VFMs into compact segmentation backbones. LiteBounD introduces (i) a dual-path distillation mechanism that disentangles semantic and boundary-aware representations, (ii) a frequency-aware alignment strategy that supervises low-frequency global semantics and high-frequency boundary details separately, and (iii) a boundary-aware decoder that fuses multi-scale encoder features with distilled semantically rich boundary information for precise segmentation. Extensive experiments on both seen (Kvasir-SEG, CVC-ClinicDB) and unseen (ColonDB, CVC-300, ETIS) datasets demonstrate that LiteBounD consistently outperforms its lightweight baselines by a significant margin and achieves performance competitive with state-of-the-art methods, while maintaining the efficiency required for real-time clinical use. Our code is available at this https URL.

---


### 258. [Latent Abstraction for Retrieval-Augmented Generation](https://arxiv.org/abs/2604.17866)

**<font color=#1a73e8>作者：</font>** Ha Lan N.T, Minh-Anh Nguyen, Dung D. Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) has become a standard approach for enhancing large language models (LLMs) with external knowledge, mitigating hallucinations, and improving factuality. However, existing systems rely on generating natural language queries at each hop and maintaining a strict architectural separation between retriever and generator, preventing them from leveraging the full representational capacity of the LLM. We propose \textbf{LAnR} (Latent Abstraction for RAG), a unified framework in which a single LLM jointly performs encoding, retrieval, and generation entirely within its own latent space. Rather than generating textual queries, LAnR produces dense retrieval vectors from the hidden states of a designated \texttt{[PRED]} token and uses them to match against encoded document representations from the same model. Furthermore, LAnR adaptively decides when sufficient evidence has been retrieved using a lightweight MLP control head over those same hidden states, eliminating both the separate retriever and explicit token-level stopping reasoning. This design is motivated by our empirical observation that answer token entropy reliably signals retrieval sufficiency. Extensive experiments on six QA benchmarks spanning single-hop and multi-hop settings demonstrate that LAnR outperforms existing RAG methods, while achieving improved inference efficiency through reduced number of retrieval calls and tighter model integration.

---


### 259. [GraSP: Graph-Structured Skill Compositions for LLM Agents](https://arxiv.org/abs/2604.17870)

**<font color=#1a73e8>作者：</font>** Tianle Xia, Lingxiang Hu, Yiding Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skill ecosystems for LLM agents have matured rapidly, yet recent benchmarks show that providing agents with more skills does not monotonically improve performance -- focused sets of 2-3 skills outperform comprehensive documentation, and excessive skills actually hurt. The bottleneck has shifted from skill availability to skill orchestration: agents need not more skills, but a structural mechanism to select, compose, and execute them with explicit causal dependencies. We propose GraSP, the first executable skill graph architecture that introduces a compilation layer between skill retrieval and execution. GraSP transforms flat skill sets into typed directed acyclic graphs (DAGs) with precondition-effect edges, executes them with node-level verification, and performs locality-bounded repair through five typed operators -- reducing replanning from O(N) to O(d^h). Across ALFWorld, ScienceWorld, WebShop, and InterCode with eight LLM backbones, GraSP outperforms ReAct, Reflexion, ExpeL, and flat skill baselines in every configuration, improving reward by up to +19 points over the strongest baseline while cutting environment steps by up to 41%. GraSP's advantage grows with task complexity and is robust to both skill over-retrieval and quality degradation, confirming that structured orchestration -- not larger skill libraries -- is the key to reliable agent execution.

---


### 260. [Design and Evaluation of a Culturally Adapted Multimodal Virtual Agent for PTSD Screening](https://arxiv.org/abs/2604.17871)

**<font color=#1a73e8>作者：</font>** Cengiz Ozel, Waleed Nadeem, Samuel Potter 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Post-traumatic stress disorder (PTSD) is highly prevalent yet chronically underreported among combat-exposed military personnel. This paper presents Molhim, a culturally adapted multimodal conversational AI platform that supports purpose-specific interactions through a configurable conversational pipeline consisting of session setup, real-time dialogue with a high-fidelity virtual avatar, and post-session analysis and feedback. In this work, we examine the PTSD screening configuration of the Molhim platform in a military healthcare context. The system employs a conversational avatar driven by a large language model, integrating real-time speech recognition, visual understanding of user input, text-to-speech synthesis, and a high-fidelity human avatar to support structured multi-turn dialogue and automated post-session analysis, including administration of the PTSD Checklist for DSM-5 (PCL-5). These findings suggest the feasibility of Molhim as a conversational platform for PTSD screening and highlight design considerations for socially cooperative human-AI systems in clinical environments.

---


### 261. [Spatiotemporal Sycophancy: Negation-Based Gaslighting in Video Large Language Models](https://arxiv.org/abs/2604.17873)

**<font color=#1a73e8>作者：</font>** Ziyao Tang, Pengkun Jiao, Bin Zhu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video Large Language Models (Vid-LLMs) have demonstrated remarkable performance in video understanding tasks, yet their robustness under conversational interaction remains largely underexplored. In this paper, we identify spatiotemporal sycophancy, a failure mode in which Vid-LLMs retract initially correct, visually grounded judgments and conform to misleading user feedback under negation-based gaslighting. Rather than merely changing their answers, the models often fabricate unsupported temporal or spatial explanations to justify incorrect revisions. To systematically investigate this phenomenon, we propose a negation-based gaslighting evaluation framework and introduce GasVideo-1000, a curated benchmark designed to probe spatiotemporal sycophancy with clear visual grounding and temporal reasoning requirements. We evaluate a broad range of state-of-the-art open-source and proprietary Vid-LLMs across diverse video understanding tasks. Extensive experiments reveal that vulnerability to negation-based gaslighting is pervasive and severe, even among models with strong baseline performance. While prompt-level grounding constraints can partially mitigate this behavior, they do not reliably prevent hallucinated justifications or belief reversal. Our results indicate that current Vid-LLMs lack robust mechanisms for maintaining grounded spatiotemporal beliefs under adversarial conversational feedback.

---


### 262. [SPREG: Structured Plan Repair with Entropy-Guided Test-Time Intervention for Large Language Model Reasoning](https://arxiv.org/abs/2604.17884)

**<font color=#1a73e8>作者：</font>** Xuan Wang, Yu Ming, Xinhao Zhong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are prone to logical hallucinations and stochastic drifts during long-chain reasoning. While Classifier-Free Guidance (CFG) can improve instruction adherence, standard static implementations often cause semantic dilution and linguistic degradation. We propose SPREG (Structured Plan-guided Real-time Entropy Gating), a lightweight inference-time framework for surgical error rectification. SPREG employs an adaptive dual-threshold mechanism to monitor real-time entropy, identifying sudden ``entropy spikes'' as reliable indicators of logical failure. Upon detection, it triggers a dynamic repair by replacing uninformative null-priors with reference distributions synthesized from historical high-confidence states. By modulating guidance intensity according to structured reasoning stages (e.g., Action, Observation), SPREG steers the model back to a stable manifold without compromising fluency. Our experiments demonstrate significant gains, notably a 20.0% absolute accuracy improvement on AIME25, while effectively suppressing uncontrolled entropy drift in complex tasks.

---


### 263. [Latent Preference Modeling for Cross-Session Personalized Tool Calling](https://arxiv.org/abs/2604.17886)

**<font color=#1a73e8>作者：</font>** Yejin Yoon, Minseo Kim, Taeuk Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Users often omit essential details in their requests to LLM-based agents, resulting in under-specified inputs for tool use. This poses a fundamental challenge for tool-augmented agents, as API execution typically requires complete arguments, highlighting the need for personalized tool calling. To study this problem, we introduce MPT, a benchmark comprising 265 multi-session dialogues that cover three challenges: Preference Recall, Preference Induction, and Preference Transfer. We also propose PRefine, a test-time memory-augmented method that represents user preferences as evolving hypotheses. Through a generate--verify--refine loop, it extracts reusable constraints from history and improves tool-calling accuracy while using only 1.24% of the tokens required by full-history prompting. These results indicate that robust personalization in agentic systems depends on memory that captures the reasons behind user choices, not just the choices themselves.

---


### 264. [AeroRAG: Structured Multimodal Retrieval-Augmented LLM for Fine-Grained Aerial Visual Reasoning](https://arxiv.org/abs/2604.17889)

**<font color=#1a73e8>作者：</font>** Junxiao Xue, Quan Deng, Tingqi Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent progress in multimodal large language models (MLLMs), reliable visual question answering in aerial scenes remains challenging. In such scenes, task-critical evidence is often carried by small objects, explicit quantities, coarse locations, and inter-object relations, whereas conventional dense visual-token representations are not well aligned with these structured semantics. To address this interface mismatch, we propose AeroRAG, a scene-graph-guided multimodal retrieval-augmented generation framework for visual question answering. The framework first converts an input image into structured visual knowledge, including object categories, quantities, spatial locations, and semantic relations, and then retrieves query-relevant semantic chunks to construct compact prompts for a text-based large language model. Rather than relying on direct reasoning over dense visual tokens, our method introduces a more explicit intermediate interface between perception and language reasoning. Experiments on the AUG aerial dataset and the general-domain VG-150 benchmark show consistent improvements over six strong MLLM baselines, with the largest gains observed in dense aerial scenes and relation-sensitive reasoning. We further evaluate the framework on VQAv2 to verify that the proposed interface remains compatible with standard visual reasoning settings. These results suggest that structured retrieval is a practical design direction for deployment-oriented and grounded visual reasoning systems.

---


### 265. [LEPO: \underline{L}atent R\underline{e}asoning \underline{P}olicy \underline{O}ptimization for Large Language~Models](https://arxiv.org/abs/2604.17892)

**<font color=#1a73e8>作者：</font>** Yuyan Zhou, Jiarui Yu, Hande Dong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, latent reasoning has been introduced into large language models (LLMs) to leverage rich information within a continuous space. However, without stochastic sampling, these methods inevitably collapse to deterministic inference, failing to discover diverse reasoning paths. To bridge the gap, we inject controllable stochasticity into latent reasoning via Gumbel-Softmax, restoring LLMs' exploratory capacity and enhancing their compatibility with Reinforcement Learning (RL). Building on this, we propose \textbf{\underline{L}}atent R\textbf{\underline{e}}asoning \textbf{\underline{P}}olicy \textbf{\underline{O}}ptimization~(\textbf{LEPO}), a novel framework that applies RL directly to continuous latent representations. Specifically, in rollout stage, LEPO maintains stochasticity to enable diverse trajectory sampling, while in optimization stage, LEPO constructs a unified gradient estimation for both latent representations and discrete tokens. Extensive experiments show that LEPO significantly outperforms existing RL methods for discrete and latent reasoning.

---


### 266. [Empowering Vocabulary Learning Through Teaching AI: Using LLMs as a Student to Perform Learning by Teaching in Vocabulary Acquisition](https://arxiv.org/abs/2604.17893)

**<font color=#1a73e8>作者：</font>** Tokio Uchida, Ko Watanabe, Andrew Vargo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> "Learning by Teaching (LbT)" helps learners deepen their understanding by explaining concepts to others, with questions playing a vital role in identifying knowledge gaps and reinforcing comprehension. However, existing systems for generating such questions often rely on rigid templates and are expensive to build. To overcome these limitations, we developed a system using Large Language Models (LLMs) to create dynamic, contextually relevant questions for LbT. In our English vocabulary learning study, we examined which learner characteristics best leverage the system's benefits. Our results showed improved memory retention over traditional methods at three and seven days of testing, with ten participants. Additionally, we identified traits linked to better learning outcomes, highlighting the potential for tailored approaches. These findings support the development of scalable, cost-effective solutions to enhance LbT methods across various fields.

---


### 267. [LoReC: Rethinking Large Language Models for Graph Data Analysis](https://arxiv.org/abs/2604.17897)

**<font color=#1a73e8>作者：</font>** Hongyu Zhan, Qixin Wang, Yusen Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The advent of Large Language Models (LLMs) has fundamentally reshaped the way we interact with graphs, giving rise to a new paradigm called GraphLLM. As revealed in recent studies, graph learning can benefit from LLMs. However, we observe limited benefits when we directly utilize LLMs to make predictions for graph-related tasks within GraphLLM paradigm, which even yields suboptimal results compared to conventional GNN-based approaches. Through in-depth analysis, we find this failure can be attributed to LLMs' limited capability for processing graph data and their tendency to overlook graph information. To address this issue, we propose LoReC (Look, Remember, and Contrast), a novel plug-and-play method for GraphLLM paradigm, which enhances LLM's understanding of graph data through three stages: (1) Look: redistributing attention to graph; (2) Remember: re-injecting graph information into the Feed-Forward Network (FFN); (3) Contrast: rectifying the vanilla logits produced in the decoding process. Extensive experiments demonstrate that LoReC brings notable improvements over current GraphLLM methods and outperforms GNN-based approaches across diverse datasets. The implementation is available at this https URL.

---


### 268. [OneDrive: Unified Multi-Paradigm Driving with Vision-Language-Action Models](https://arxiv.org/abs/2604.17915)

**<font color=#1a73e8>作者：</font>** Yiwei Zhang, Xuesong Chen, Jin Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models(VLMs) excel at autoregressive text generation, yet end-to-end autonomous driving requires multi-task learning with structured outputs and heterogeneous decoding behaviors, such as autoregressive language generation, parallel object detection and trajectory regression. To accommodate these differences, existing systems typically introduce separate or cascaded decoders, resulting in architectural fragmentation and limited backbone reuse. In this work, we present a unified autonomous driving framework built upon a pretrained VLM, where heterogeneous decoding behaviors are reconciled within a single transformer decoder. We demonstrate that pretrained VLM attention exhibits strong transferability beyond pure language modeling. By organizing visual and structured query tokens within a single causal decoder, structured queries can naturally condition on visual context through the original attention mechanism. Textual and structured outputs share a common attention backbone, enabling stable joint optimization across heterogeneous tasks. Trajectory planning is realized within the same causal LLM decoder by introducing structured trajectory queries. This unified formulation enables planning to share the pretrained attention backbone with images and perception tokens. Extensive experiments on end-to-end autonomous driving benchmarks demonstrate state-of-the-art performance, including 0.28 L2 and 0.18 collision rate on nuScenes open-loop evaluation and competitive results (86.8 PDMS) on NAVSIM closed-loop evaluation. The full model preserves multi-modal generation capability, while an efficient inference mode achieves approximately 40% lower latency. Code and models are available at this https URL

---


### 269. [Prompting Foundation Models for Zero-Shot Ship Instance Segmentation in SAR Imagery](https://arxiv.org/abs/2604.17920)

**<font color=#1a73e8>作者：</font>** Islam Mansour, Francescopaolo Sica, Michael Schmitt  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic Aperture Radar (SAR) plays a critical role in maritime surveillance, yet deep learning for SAR analysis is limited by the lack of pixel-level annotations. This paper explores how general-purpose vision foundation models can enable zero-shot ship instance segmentation in SAR imagery, eliminating the need for pixel-level supervision. A YOLOv11-based detector trained on open SAR datasets localizes ships via bounding boxes, which then prompt the Segment Anything Model 2 (SAM2) to produce instance masks without any mask annotations. Unlike prior SAM-based SAR approaches that rely on fine tuning or adapters, our method demonstrates that spatial constraints from a SAR-trained detector alone can effectively regularize foundation model predictions. This design partially mitigates the optical-SAR domain gap and enables downstream applications such as vessel classification, size estimation, and wake analysis. Experiments on the SSDD benchmark achieve a mean IoU of 0.637 (89% of a fully supervised baseline) with an overall ship detection rate of 89.2%, confirming a scalable, annotation-efficient pathway toward foundation-model-driven SAR image understanding.

---


### 270. [HEALing Entropy Collapse: Enhancing Exploration in Few-Shot RLVR via Hybrid-Domain Entropy Dynamics Alignment](https://arxiv.org/abs/2604.17928)

**<font color=#1a73e8>作者：</font>** Zhanyu Liu, Qingguo Hu, Ante Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Reward (RLVR) has proven effective for training reasoning-oriented large language models, but existing methods largely assume high-resource settings with abundant training data. In low-resource scenarios, RLVR is prone to more severe entropy collapse, which substantially limits exploration and degrades reasoning performance. To address this issue, we propose Hybrid-domain Entropy dynamics ALignment (HEAL), a framework tailored for few-shot RLVR. HEAL first selectively incorporates high-value general-domain data to promote more diverse exploration. Then, we introduce Entropy Dynamics Alignment (EDA), a reward mechanism that aligns trajectory-level entropy dynamics between the target and general domains, capturing both entropy magnitude and fine-grained variation. Through this alignment, EDA not only further mitigates entropy collapse but also encourages the policy to acquire more diverse exploration behaviors from the general domain. Experiments across multiple domains show that HEAL consistently improves few-shot RLVR performance. Notably, using only 32 target-domain samples, HEAL matches or even surpasses full-shot RLVR trained with 1K target-domain samples.

---


### 271. [Heterogeneity in Formal Linguistic Competence of Language Models: Is Data the Real Bottleneck?](https://arxiv.org/abs/2604.17930)

**<font color=#1a73e8>作者：</font>** H S V N S Kowndinya Renduchintala, Sumit Bhatia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) exhibit a puzzling disparity in their formal linguistic competence: while they learn some linguistic phenomena with near-perfect mastery, they often perform below chance on others, even after training on trillions of tokens. In this work, we investigate whether these failures stem from inherent architectural limitations or simply the scarcity of these specific grammatical constructions in web-scale corpora. We pre-train simple GPT-2 Small (124M) models on a 100M-token random sample of the FineWeb corpus and intervene by injecting a minimal amount (1%) of synthetic data targeting specific linguistic phenomena. We find that this targeted intervention substantially improves model performance in 8 out of the 9 worst-performing BLiMP paradigms - notably the accuracy on a specific paradigm, only_npi_scope, surges from 20.9% to 69.4%. Furthermore, we observe that these interventions generally preserve or slightly improve aggregate performance. However, while we also identify a resistant phenomenon, principle_A_c_command, whose performance remains below chance even after our data augmentation, our findings do serve as an optimistic existence proof that even small language models can substantially improve on those linguistic phenomena on which models typically perform poorly, provided the pre-training data contains sufficient exposure to them. This suggests that efforts towards human-scale language modeling may benefit greatly by focusing on data composition. The code to reproduce our results is open-sourced at this https URL.

---


### 272. [LiteResearcher: A Scalable Agentic RL Training Framework for Deep Research Agent](https://arxiv.org/abs/2604.17931)

**<font color=#1a73e8>作者：</font>** Wanli Li, Bince Qu, Bo Pan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning (RL) has emerged as a powerful training paradigm for LLM-based agents. However, scaling agentic RL for deep research remains constrained by two coupled challenges: hand-crafted synthetic data fails to elicit genuine real-world search capabilities, and real-world search dependency during RL training introduces instability and prohibitive cost, which limits the scalability of Agentic RL. LiteResearcher is a training framework that makes Agentic RL scalable: by constructing a lite virtual world that mirrors real-world search dynamics, we enable a continuously improving training recipe that empowers a tiny search agent to outperform large-scale open-source and commercial models (e.g., Tongyi DeepResearch and Claude-4.5 Sonnet). Specifically, on common benchmarks such as GAIA and Xbench, our LiteResearcher-4B achieves open-source state-of-the-art results of 71.3% and 78.0% respectively, demonstrating that scalable RL training is a key enabler for Deep Research Agents.

---


### 273. [From Heads to Neurons: Causal Attribution and Steering in Multi-Task Vision-Language Models](https://arxiv.org/abs/2604.17941)

**<font color=#1a73e8>作者：</font>** Qidong Wang, Junjie Hu, Ming Jiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work has increasingly explored neuron-level interpretation in vision-language models (VLMs) to identify neurons critical to final predictions. However, existing neuron analyses generally focus on single tasks, limiting the comparability of neuron importance across tasks. Moreover, ranking strategies tend to score neurons in isolation, overlooking how task-dependent information pathways shape the write-in effects of feed-forward network (FFN) neurons. This oversight can exacerbate neuron polysemanticity in multi-task settings, introducing noise into the identification and intervention of task-critical neurons. In this study, we propose HONES (Head-Oriented Neuron Explanation & Steering), a gradient-free framework for task-aware neuron attribution and steering in multi-task VLMs. HONES ranks FFN neurons by their causal write-in contributions conditioned on task-relevant attention heads, and further modulates salient neurons via lightweight scaling. Experiments on four diverse multimodal tasks and two popular VLMs show that HONES outperforms existing methods in identifying task-critical neurons and improves model performance after steering. Our source code is released at: this https URL.

---


### 274. [Domain-oriented RAG Assessment (DoRA): Synthetic Benchmarking for RAG-based Question Answering on Defense Documents](https://arxiv.org/abs/2604.17943)

**<font color=#1a73e8>作者：</font>** Bao Gia Doan, Aditya Joshi, Pantelis Elinas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Open-domain RAG benchmarks over public corpora can overestimate deployment performance due to pretraining overlap and weak attribution requirements. We present DoRA (Domain-oriented RAG Assessment), a domain-grounded benchmark built from defense documents that pairs synthetic, intent-conditioned QA (question answering) with auditable evidence passages for attribution. DoRA covers five question types (find, explain, summarize, generate, provide) and contains 6.5K curated instances. In end-to-end evaluation with a fixed dense retriever, general-purpose Language Models (LMs) perform similarly, while a model trained on DoRA (DoRA SFT) yields large gains over the base model (Llama3.1-8B-Instruct): up to 26% improvement in QA task success, while reducing the hallucination rate by 47% in RAG faithfulness scores, supporting contamination-aware regression testing under domain shift.

---


### 275. [ZSG-IAD: A Multimodal Framework for Zero-Shot Grounded Industrial Anomaly Detection](https://arxiv.org/abs/2604.17949)

**<font color=#1a73e8>作者：</font>** Qiuhui Chen, Jiaxiang Song, Shuai Tan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based industrial anomaly detectors often behave as black boxes, making it hard to justify decisions with physically meaningful defect evidence. We propose ZSG-IAD, a multimodal vision-language framework for zero-shot grounded industrial anomaly detection. Given RGB images, sensor images, and 3D point clouds, ZSG-IAD generates structured anomaly reports and pixel-level anomaly masks. ZSG-IAD introduces a language-guided two-hop grounding module: (1) anomaly-related sentences select evidence-like latent slots distilled from multimodal features, yielding coarse spatial support; (2) selected slots modulate feature maps via channel-spatial gating and a lightweight decoder to produce fine-grained masks. To improve reliability, we further apply Executable-Rule GRPO with verifiable rewards to promote structured outputs, anomaly-region consistency, and reasoning-conclusion coherence. Experiments across multiple industrial anomaly benchmarks show strong zero-shot performance and more transparent, physically grounded explanations than prior methods. We will release code and annotations to support future research on trustworthy industrial anomaly detection systems.

---


### 276. [DifFoundMAD: Foundation Models meet Differential Morphing Attack Detection](https://arxiv.org/abs/2604.17961)

**<font color=#1a73e8>作者：</font>** Lazaro J. Gonzalez-Soler, André Dörsch, Christian Rathgeb 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we introduce DifFoundMAD, a parameter-efficient D-MAD framework that exploits the generalisation capabilities of vision foundation models (FM) to capture discrepancies between suspected morphs and live capture images. In contrast to conventional D-MAD systems that rely on face recognition embeddings or handcrafted feature differences, DifFoundMAD follows the standard differential paradigm while replacing the underlying representation space with embeddings extracted from FMs. By combining lightweight finetuning with class-balanced optimisation, the proposed method updates only a small subset of parameters while preserving the rich representational priors of the underlying FMs. Extensive cross-database evaluations on standard D-MAD benchmarks demonstrate that DifFoundMAD achieves consistent improvements over state-of-the-art systems, particularly at the strict security levels required in operational deployments such as border control: The error rates reported in the current state-of-the-art were reduced from 6.16% to 2.17% for high-security levels using DifFoundMAD.

---


### 277. [TPS-CalcBench: A Benchmark and Diagnostic Evaluation Framework for LLM Analytical Calculation Competence in Hypersonic Thermal Protection System Engineering](https://arxiv.org/abs/2604.17966)

**<font color=#1a73e8>作者：</font>** Jinglai Zheng, Chuhan Qiao, Haiming Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying LLMs as reasoning assistants in safety-critical aerospace engineering requires stricter evaluation criteria than general scientific benchmarks. In hypersonic thermal protection system (TPS) design, inaccurate stagnation-point heat flux or boundary-layer calculations may cause catastrophic design margin violations. Models with numerically reasonable but physically invalid answers are more dangerous than those declining to respond. Current scientific benchmarks only test abstract math and basic physics, evaluate final answers solely, ignore engineering reasoning processes, and cannot detect such critical failures. We propose TPS-CalcBench, the first diagnostic benchmark for closed-form analytical calculations in hypersonic aerodynamics and high-temperature gas dynamics that experienced TPS engineers conduct without simulations. Our contributions include domain-oriented task taxonomy with 4 difficulty levels and 8 categories from Anderson's textbook, dual-track evaluation measuring result accuracy and reasoning quality via an 8-dimension rubric and calibrated judge with human audit to identify right answer wrong reasoning issues, human-AI data pipeline producing 420 high-confidence core items and 810 noise-controlled pre-gating items from 4560 raw data, noise-sensitivity analysis measuring data quality impacts on model ranking, and three diagnostic intervention methods: DFA-TPS fine-tuning, RAG-EQ retrieval grounding and PA-CoT process-aware prompting. Tests on 13 models from 7 groups show wide performance differences (KPI 12.6-87.9), hidden formula selection defects, data-driven rank changes and effective intervention improvements, establishing a complete diagnose-evaluate-intervene framework for safety-critical engineering LLM deployment assessment.

---


### 278. [From Fallback to Frontline: When Can LLMs be Superior Annotators of Human Perspectives?](https://arxiv.org/abs/2604.17968)

**<font color=#1a73e8>作者：</font>** Hasan Amin, Harry Yizhou Tian, Xiaoni Duan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although large language models (LLMs) are increasingly used as annotators at scale, they are typically treated as a pragmatic fallback rather than a faithful estimator of human perspectives. This work challenges that presumption. By framing perspective-taking as the estimation of a latent group-level judgment, we characterize the conditions under which modern LLMs can outperform human annotators, including in-group humans, when predicting aggregate subgroup opinions on subjective tasks, and show that these conditions are common in practice. This advantage arises from structural properties of LLMs as estimators, including low variance and reduced coupling between representation and processing biases, rather than any claim of lived experience. Our analysis identifies clear regimes where LLMs act as statistically superior frontline estimators, as well as principled limits where human judgment remains essential. These findings reposition LLMs from a cost-saving compromise to a principled tool for estimating collective human perspectives.

---


### 279. [Mitigating Multimodal Hallucination via Phase-wise Self-reward](https://arxiv.org/abs/2604.17982)

**<font color=#1a73e8>作者：</font>** Yu Zhang, Chuyang Sun, Kehai Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) still struggle with vision hallucination, where generated responses are inconsistent with the visual input. Existing methods either rely on large-scale annotated data for fine-tuning, which incurs massive computational overhead, or employ static post-hoc strategies that overlook the dynamic nature of hallucination emergence. To address these, we introduce a new self-rewarding framework, enabling dynamic hallucination mitigation at inference time without external supervision. On the empirical side, we reveal that visual hallucination exhibits phase-wise dynamic patterns, peaking at the onset of each semantic phase. Drawing on these insights, we propose \textbf{PSRD} (\textbf{Phase-wise \textbf{S}elf-\textbf{R}eward \textbf{D}ecoding) for online hallucination correction guided by phase-wise self-reward signals. To reduce the cost of repeated self-evaluation during decoding, we distill the hallucination guidance signal from LVLMs into a lightweight reward model. The reward model subsequently provides on-the-fly guidance for targeted intervention during the decoding process, enabling precise hallucination suppression. The proposed PSRD significantly reduces the hallucination rate of LLaVA-1.5-7B by 50.0% and consistently outperforms existing post-hoc methods across five hallucination evaluation benchmarks for four LVLMs. Further analysis confirms that PSRD effectively mitigates hallucination propagation and achieves a highly controllable trade-off between strong performance and inference efficiency.

---


### 280. [Employing General-Purpose and Biomedical Large Language Models with Advanced Prompt Engineering for Pharmacoepidemiologic Study Design](https://arxiv.org/abs/2604.17988)

**<font color=#1a73e8>作者：</font>** Xinyao Zhang, Nicole Sonne Heckmann, Manuela Del Castillo Suero 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: The potential of large language models (LLMs) to automate and support pharmacoepidemiologic study design is an emerging area of interest, yet their reliability remains insufficiently characterized. General-purpose LLMs often display inaccuracies, while the comparative performance of specialized biomedical LLMs in this domain remains unknown. Methods: This study evaluated general-purpose LLMs (GPT-4o and DeepSeek-R1) versus biomedically fine-tuned LLMs (QuantFactory/Bio-Medical-Llama-3-8B-GGUF and Irathernotsay/qwen2-1.5B-medical_qa-Finetune) using 46 protocols (2018-2024) from the HMA-EMA Catalogue and Sentinel System. Performance was assessed across relevance, logic of justification, and ontology-code agreement across multiple coding systems using Least-to-Most (LTM) and Active Prompting strategies. Results: GPT-4o and DeepSeek-R1 paired with LTM prompting achieved the highest relevance and logic of justification scores, with GPT-4o-LTM reaching a median relevance score of 4 in 8 of 9 questions for HMA-EMA protocols. Biomedical LLMs showed lower relevance overall and frequently generated insufficient justification. All LLMs demonstrated limited proficiency in ontology-code mapping, although LTM provided the most consistent improvements in reasoning stability. Conclusion: Off-the-shelf general-purpose LLMs currently offer superior support for pharmacoepidemiologic design compared to biomedical LLMs. Prompt strategy strongly influenced LLM performance.

---


### 281. [SELF-EMO: Emotional Self-Evolution from Recognition to Consistent Expression](https://arxiv.org/abs/2604.18003)

**<font color=#1a73e8>作者：</font>** Shaowei Zhang, Faqiang Qian, Yan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotion Recognition in Conversation (ERC) has become a fundamental capability for large language models (LLMs) in human-centric interaction. Beyond accurate recognition, coherent emotional expression is also crucial, yet both are limited by the scarcity and static nature of high-quality annotated data. In this work, we propose SELF-EMO, a self-evolution framework grounded in the hypothesis that better emotion prediction leads to more consistent emotional responses. We introduce two auxiliary tasks, emotional understanding and emotional expression, and design a role-based self-play paradigm where the model acts as both an emotion recognizer and a dialogue responder. Through iterative interactions, the model generates diverse conversational trajectories, enabling scalable data generation. To ensure quality, we adopt a data flywheel mechanism that filters candidate predictions and responses using a smoothed IoU-based reward and feeds selected samples back for continuous self-improvement without external supervision. We further develop SELF-GRPO, a reinforcement learning algorithm that stabilizes optimization with multi-label alignment rewards and group-level consistency signals. Experiments on IEMOCAP, MELD, and EmoryNLP show that SELF-EMO achieves state-of-the-art performance, improving accuracy by +6.33% on Qwen3-4B and +8.54% on Qwen3-8B, demonstrating strong effectiveness and generalization.

---


### 282. [Diversity Collapse in Multi-Agent LLM Systems: Structural Coupling and Collective Failure in Open-Ended Idea Generation](https://arxiv.org/abs/2604.18005)

**<font color=#1a73e8>作者：</font>** Nuo Chen, Yicheng Tong, Yuzhe Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems (MAS) are increasingly used for open-ended idea generation, driven by the expectation that collective interaction will broaden the exploration diversity. However, when and why such collaboration truly expands the solution space remains unclear. We present a systematic empirical study of diversity in MAS-based ideation across three bottom-up levels: model intelligence, agent cognition, and system dynamics. At the model level, we identify a compute efficiency paradox, where stronger, highly aligned models yield diminishing marginal diversity despite higher per-sample quality. At the cognition level, authority-driven dynamics suppress semantic diversity compared to junior-dominated groups. At the system level, group-size scaling yields diminishing returns and dense communication topologies accelerate premature convergence. We characterize these outcomes as collective failures emerging from structural coupling, a process where interaction inadvertently contracts agent exploration and triggers diversity collapse. Our analysis shows that this collapse arises primarily from the interaction structure rather than inherent model insufficiency, highlighting the importance of preserving independence and disagreement when designing MAS for creative tasks. Our code is available at this https URL.

---


### 283. [How Creative Are Large Language Models in Generating Molecules?](https://arxiv.org/abs/2604.18031)

**<font color=#1a73e8>作者：</font>** Wen Tao, Yiwei Wang, Peng Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Molecule generation requires satisfying multiple chemical and biological constraints while searching a large and structured chemical space. This makes it a non-binary problem, where effective models must identify non-obvious solutions under constraints while maintaining exploration to improve success by escaping local optima. From this perspective, creativity is a functional requirement in molecular generation rather than an aesthetic notion. Large language models (LLMs) can generate molecular representations directly from natural language prompts, but it remains unclear what type of creativity they exhibit in this setting and how it should be evaluated. In this work, we study the creative behavior of LLMs in molecular generation through a systematic empirical evaluation across physicochemical, ADMET, and biological activity tasks. We characterize creativity along two complementary dimensions, convergent creativity and divergent creativity, and analyze how different factors shape these behaviors. Our results indicate that LLMs exhibit distinct patterns of creative behavior in molecule generation, such as an increase in constraint satisfaction when additional constraints are imposed. Overall, our work is the first to reframe the abilities required for molecule generation as creativity, providing a systematic understanding of creativity in LLM-based molecular generation and clarifying the appropriate use of LLMs in molecular discovery pipelines.

---


### 284. [JudgeMeNot: Personalizing Large Language Models to Emulate Judicial Reasoning in Hebrew](https://arxiv.org/abs/2604.18041)

**<font color=#1a73e8>作者：</font>** Itay Razumenko, Arnon Sturm, Nir Grinberg  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite significant advances in large language models, personalizing them for individual decision-makers remains an open problem. Here, we introduce a synthetic-organic supervision pipeline that transforms raw judicial decisions into instruction-tuning data, enabling parameter-efficient fine-tuning of personalized models for individual judges in low-resource settings. We compare our approach to state-of-the-art personalization techniques across three different tasks and settings. The results show that Causal Language Modeling followed by synthetically generated instruction-tuning significantly outperforms all other baselines, providing significant improvements across lexical, stylistic, and semantic similarity. Notably, our model-generated outputs are indistinguishable from the reasoning of human judges, highlighting the viability of efficient personalization, even in low-resource settings.

---


### 285. [Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity](https://arxiv.org/abs/2604.18058)

**<font color=#1a73e8>作者：</font>** Blaise Delaney, Salil Patel, Yuji Xing 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Sonata, a compact latent world model for six-axis trunk IMU representation learning under clinical data scarcity. Clinical cohorts typically comprise tens to hundreds of patients, making web-scale masked-reconstruction objectives poorly matched to the problem. Sonata is a 3.77 M-parameter hybrid model, pre-trained on a harmonised corpus of nine public datasets (739 subjects, 190k windows) with a latent world-model objective that predicts future state rather than reconstructing raw sensor traces. In a controlled comparison against a matched autoregressive forecasting baseline (MAE) on the same backbone, Sonata yields consistently stronger frozen-probe clinical discrimination, prospective fall-risk prediction, and cross-cohort transfer across a 14-arm evaluation suite, while producing higher-rank, more structured latent representations. At 3.77 M parameters the model is compatible with on-device wearable inference, offering a step toward general kinematic world models for neurological assessment.

---


### 286. [Enhancing Continual Learning of Vision-Language Models via Dynamic Prefix Weighting](https://arxiv.org/abs/2604.18075)

**<font color=#1a73e8>作者：</font>** Hyeonseo Jang, Hyuk Kwon, Kibok Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate recently introduced domain-class incremental learning scenarios for vision-language models (VLMs). Recent works address this challenge using parameter-efficient methods, such as prefix-tuning or adapters, which facilitate model adaptation to downstream tasks by incorporating task-specific information into input tokens through additive vectors. However, previous approaches often normalize the weights of these vectors, disregarding the fact that different input tokens require different degrees of adjustment. To overcome this issue, we propose Dynamic Prefix Weighting (DPW), a framework that dynamically assigns weights to prefixes, complemented by adapters. DPW consists of 1) a gating module that adjusts the weights of each prefix based on the importance of the corresponding input token, and 2) a weighting mechanism that derives adapter output weights as a residual of prefix-tuning weights, ensuring that adapters are utilized only when necessary. Experimental results demonstrate that our method achieves state-of-the-art performance in domain-class incremental learning scenarios for VLMs. The code is available at: this https URL.

---


### 287. [Predicting LLM Compression Degradation from Spectral Statistics](https://arxiv.org/abs/2604.18085)

**<font color=#1a73e8>作者：</font>** Mingxue Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix-level low-rank compression is a promising way to reduce the cost of large language models, but running compression and evaluating the resulting models on language tasks can be prohibitively expensive. Can compression-induced degradation be predicted before committing to this compute? We systematically analyze the Qwen3 and Gemma3 model families across four representative low-rank compression methods: vanilla SVD, two ASVD variants, and SVD-LLM. We find that stable rank and information density, measured in bits per parameter, dominate performance degradation. The interaction term $\gamma \cdot \bar{\rho}_s$, defined as compression ratio times stable rank, is a robust predictor of accuracy degradation, achieving leave-one-out cross-validation Pearson correlations of $0.890$ for attention layers and $0.839$ for MLP layers. We provide theoretical intuition for why this predictor succeeds by connecting it to standard SVD truncation bounds and error composition mechanisms in transformer layers. These findings enable a predict-then-compress workflow: compute $\gamma \cdot \bar{\rho}_s$ from weights, estimate degradation, and invest compute only in desirable configurations.

---


### 288. [Culture-Aware Humorous Captioning: Multimodal Humor Generation across Cultural Contexts](https://arxiv.org/abs/2604.18091)

**<font color=#1a73e8>作者：</font>** Run Xu, Lu Li, Rongzhao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models have shown promising ability in generating humorous captions for images, yet they still lack stable control over explicit cultural context, making it difficult to jointly maintain image relevance, contextual appropriateness, and humor quality under a specified cultural background. To address this limitation, we introduce a new multimodal generation task, culture-aware humorous captioning, which requires a model to generate a humorous caption conditioned on both an input image and a target cultural context. Captions generated under different cultural contexts are not expected to share the same surface form, but should remain grounded in similar visual situations or humorous this http URL support this task, we establish a six-dimensional evaluation framework covering image relevance, contextual fit, semantic richness, reasonableness, humor, and creativity. We further propose a staged alignment framework that first initializes the model with high-resource supervision under the Western cultural context, then performs multi-dimensional preference alignment via judge-based GRPO with a Degradation-aware Prototype Repulsion Constraint to mitigate reward hacking in open-ended generation, and finally adapts the model to the Eastern cultural context with a small amount of supervision. Experimental results show that our method achieves stronger overall performance under the proposed evaluation framework, with particularly large gains in contextual fit and a better balance between image relevance and humor under cultural constraints.

---


### 289. [Generalization Boundaries of Fine-Tuned Small Language Models for Graph Structural Inference](https://arxiv.org/abs/2604.18092)

**<font color=#1a73e8>作者：</font>** Michal Podstawski  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Small language models fine-tuned for graph property estimation have demonstrated strong in-distribution performance, yet their generalization capabilities beyond training conditions remain poorly understood. In this work, we systematically investigate the boundaries of structural inference in fine-tuned small language models along two generalization axes - graph size and graph family distribution - and assess domain-learning capability on real-world graph benchmarks. Using a controlled experimental setup with three instruction-tuned models in the 3-4B parameter class and two graph serialization formats, we evaluate performance on graphs substantially larger than the training range and across held-out random graph families. Our results show that fine-tuned models maintain strong ordinal consistency across structurally distinct graph families and continue to rank graphs by structural properties on inputs substantially larger than those seen during training, with distinct architecture-specific degradation profiles. These findings delineate where fine-tuned small language models generalize reliably, providing empirical grounding for their use in graph-based reasoning tasks.

---


### 290. [Stability Implies Redundancy: Delta Attention Selective Halting for Efficient Long-Context Prefilling](https://arxiv.org/abs/2604.18103)

**<font color=#1a73e8>作者：</font>** Yujie Chen, Tailai Chen, Yifeng Gao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prefilling computational costs pose a significant bottleneck for Large Language Models (LLMs) and Large Multimodal Models (LMMs) in long-context settings. While token pruning reduces sequence length, prior methods rely on heuristics that break compatibility with hardware-efficient kernels like FlashAttention. In this work, we observe that tokens evolve toward \textit{semantic fixing points}, making further processing redundant. To this end, we introduce Delta Attention Selective Halting (DASH), a training-free policy that monitors the layer-wise update dynamics of the self-attention mechanism to selectively halt stabilized tokens. Extensive evaluation confirms that DASH generalizes across language and vision benchmarks, delivering significant prefill speedups while preserving model accuracy and hardware efficiency. Code will be released at this https URL.

---


### 291. [Efficient Low-Resource Language Adaptation via Multi-Source Dynamic Logit Fusion](https://arxiv.org/abs/2604.18106)

**<font color=#1a73e8>作者：</font>** Chen Zhang, Jiuheng Lin, Zhiyuan Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting large language models (LLMs) to low-resource languages (LRLs) is constrained by the scarcity of task data and computational resources. Although Proxy Tuning offers a logit-level strategy for introducing scaling effects, it often fails in LRL settings because the large model's weak LRL competence might overwhelm the knowledge of specialized smaller models. We thus propose TriMix, a test-time logit fusion framework that dynamically balances capabilities from three different sources: LRL competence from a continually pretrained small model, task competence from high-resource language instruction tuning, and the scaling benefits of large models. It is data- and compute-efficient, requiring no LRL task annotations, and only continual pretraining on a small model. Experiments across four model families and eight LRLs show that TriMix consistently outperforms single-model baselines and Proxy Tuning. Our analysis reveals that prioritizing the small LRL-specialized model's logits is crucial for success, challenging the prevalent large-model-dominant assumption.

---


### 292. [FLiP: Towards understanding and interpreting multimodal multilingual sentence embeddings](https://arxiv.org/abs/2604.18109)

**<font color=#1a73e8>作者：</font>** Santosh Kesiraju, Bolaji Yusuf, Šimon Sedláček 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents factorized linear projection (FLiP) models for understanding pretrained sentence embedding spaces. We train FLiP models to recover the lexical content from multilingual (LaBSE), multimodal (SONAR) and API-based (Gemini) sentence embedding spaces in several high- and mid-resource languages. We show that FLiP can recall more than 75% of lexical content from the embeddings, significantly outperforming existing non-factorized baselines. Using this as a diagnostic tool, we uncover the modality and language biases across the selected sentence encoders and provide practitioners with intrinsic insights about the encoders without relying on conventional downstream evaluation tasks. Our implementation is public this https URL.

---


### 293. [Retrieval-Augmented Multimodal Model for Fake News Detection](https://arxiv.org/abs/2604.18112)

**<font color=#1a73e8>作者：</font>** Yiheng Li, Weihai Lu, Hanyi Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, multimodal multidomain fake news detection has garnered increasing attention. Nevertheless, this direction presents two significant challenges: (1) Failure to Capture Cross-Instance Narrative Consistency: existing models usually evaluate each news in isolation, fail to capture cross-instance narrative consistency, and thus struggle to address the spread of cluster based fake news driven by social media; (2) Lack of Domain Specific Knowledge for Reasoning: conventional models, which rely solely on knowledge encoded in their parameters during training, struggle to generalize to new or data-scarce domains (e.g., emerging events or niche topics). To tackle these challenges, we introduce Retrieval-Augmented Multimodal Model for Fake News Detection (RAMM). First, RAMM employs a Multimodal Large Language Model (MLLM) as its backbone to capture cross-modal semantic information from news samples. Second, RAMM incorporates an Abstract Narrative Alignment Module. This component adaptively extracts abstract narrative consistency from diverse instances across distinct domains, aggregates relevant knowledge, and thereby enables the modeling of high-level narrative information. Finally, RAMM introduces a Semantic Representation Alignment Module, which aligns the model's decision-making paradigm with that of humans - specifically, it shifts the model's reasoning process from direct inference on multimodal features to an instance-based analogical reasoning process. Extensive experimental results on three public datasets validate the efficacy of our proposed approach. Our code is available at the following link: this https URL

---


### 294. [TLoRA: Task-aware Low Rank Adaptation of Large Language Models](https://arxiv.org/abs/2604.18124)

**<font color=#1a73e8>作者：</font>** Weicheng Lin, Yi Zhang, Jiawei Dang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) has become a widely adopted parameter-efficient fine-tuning method for large language models, with its effectiveness largely influenced by the allocation of ranks and scaling factors, as well as initialization. Existing LoRA variants typically address only one of these factors, often at the cost of increased training complexity or reduced practical efficiency. In this work, we present Task-aware Low-Rank Adaptation (TLoRA), a unified framework that jointly optimizes initialization and resource allocation at the outset of training. TLoRA introduces a data-driven initialization strategy that aligns the LoRA $A$ matrix with task-relevant subspaces by performing singular value decomposition on the product of pre-trained weights and input activation covariance. After this, the $A$ matrix is frozen, and only the $B$ matrix is trained. Furthermore, TLoRA employs a sensitivity-based importance metric to adaptively allocate ranks and scaling factors across layers under a fixed parameter budget. We conduct extensive experiments that demonstrate TLoRA consistently performs excellently across various tasks, including natural language understanding, commonsense reasoning, math reasoning, code generation, and chat generation, while significantly reducing the number of trainable parameters.

---


### 295. [Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration](https://arxiv.org/abs/2604.18131)

**<font color=#1a73e8>作者：</font>** Qifan Zhang, Dongyang Ma, Tianqing Fang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most agents today ``self-evolve'' by following rewards and rules defined by humans. However, this process remains fundamentally dependent on external supervision; without human guidance, the evolution stops. In this work, we train agents to possess an intrinsic meta-evolution capability to spontaneously learn about unseen environments prior to task execution.
To instill this ability, we design an outcome-based reward mechanism that measures how much an agent's self-generated world knowledge improves its success rate on downstream tasks. This reward signal is used exclusively during the training phase to teach the model how to explore and summarize effectively. At inference time, the agent requires no external rewards or human instructions. It spontaneously performs native self-evolution to adapt to unknown environments using its internal parameters.
When applied to Qwen3-30B and Seed-OSS-36B, this shift to native evolution yields a 20% performance increase on WebVoyager and WebWalker. Most strikingly, the generated world knowledge even enables a compact 14B Qwen3 model to outperform the unassisted Gemini-2.5-Flash, establishing a new paradigm for truly evolving agents.

---


### 296. [Multi-Agent Systems: From Classical Paradigms to Large Foundation Model-Enabled Futures](https://arxiv.org/abs/2604.18133)

**<font color=#1a73e8>作者：</font>** Zixiang Wang, Mengjia Gong, Qiyu Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the rapid advancement of artificial intelligence, multi-agent systems (MASs) are evolving from classical paradigms toward architectures built upon large foundation models (LFMs). This survey provides a systematic review and comparative analysis of classical MASs (CMASs) and LFM-based MASs (LMASs). First, within a closed-loop coordination framework, CMASs are reviewed across four fundamental dimensions: perception, communication, decision-making, and control. Beyond this framework, LMASs integrate LFMs to lift collaboration from low-level state exchanges to semantic-level reasoning, enabling more flexible coordination and improved adaptability across diverse scenarios. Then, a comparative analysis is conducted to contrast CMASs and LMASs across architecture, operating mechanism, adaptability, and application. Finally, future perspectives on MASs are presented, summarizing open challenges and potential research opportunities.

---


### 297. [Can LLM-Generated Text Empower Surgical Vision-Language Pre-training?](https://arxiv.org/abs/2604.18134)

**<font color=#1a73e8>作者：</font>** Chengan Che, Chao Wang, Jiayuan Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in self-supervised learning have led to powerful surgical vision encoders capable of spatiotemporal understanding. However, extending these visual foundations to multi-modal reasoning tasks is severely bottlenecked by the prohibitive cost of expert textual annotations. To overcome this scalability limitation, we introduce \textbf{LIME}, a large-scale multi-modal dataset derived from open-access surgical videos using human-free, Large Language Model (LLM)-generated narratives. While LIME offers immense scalability, unverified generated texts may contain errors, including hallucinations, that could potentially lead to catastrophically degraded pre-trained medical priors in standard contrastive pipelines. To mitigate this, we propose \textbf{SurgLIME}, a parameter-efficient Vision-Language Pre-training (VLP) framework designed to learn reliable cross-modal alignments using noisy narratives. SurgLIME preserves foundational medical priors using a LoRA-adapted dual-encoder architecture and introduces an automated confidence estimation mechanism that dynamically down-weights uncertain text during contrastive alignment. Evaluations on the AutoLaparo and Cholec80 benchmarks show that SurgLIME achieves competitive zero-shot cross-modal alignment while preserving the robust linear probing performance of the visual foundation model. Dataset, code, and models are publicly available at \href{this https URL}{this https URL}.

---


### 298. [Leveraging AI for Direct Bystander Intervention Against Cyberbullying](https://arxiv.org/abs/2604.18153)

**<font color=#1a73e8>作者：</font>** Peinuan Qin, Jiting Cheng, Jungup Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Cyberbullying is a pervasive problem in online environments, causing substantial psychological harm to victims. Although bystander intervention has proven effective in mitigating its impact, motivating bystanders to engage in direct intervention remains a persistent challenge. Studies have suggested that difficulties in intervention skills and defending self-efficacy hinder bystanders from initiating direct intervention. To address this challenge, we introduced EmojiGen, an AI intervention tool designed to empower bystanders for direct intervention. EmojiGen enabled users to simply select an emoji as an intention clue, which subsequently combined the cyberbullying context to generate responses. In a between-subjects experiment involving 90 participants on a custom-built social media platform, we found that EmojiGen significantly increased the frequency of direct bystander interventions, both in supporting victims and in confronting perpetrators, driven by different factors. EmojiGen also increased the sense of knowing how to help and defending self-efficacy, while reducing perceived workload and anxiety associated with initiating intervention. The study contributed to the CSCW community through offering an effective direct bystander intervention method and providing design implications for future cyberbullying interventions.

---


### 299. [FreezeEmpath: Efficient Training for Empathetic Spoken Chatbots with Frozen LLMs](https://arxiv.org/abs/2604.18159)

**<font color=#1a73e8>作者：</font>** Yun Hong, Yan Zhou, Yang Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Empathy is essential for fostering natural interactions in spoken dialogue systems, as it enables machines to recognize the emotional tone of human speech and deliver empathetic responses. Recent research has made significant progress in developing empathetic spoken chatbots based on large language models (LLMs). However, several challenges still exist when training such models, including reliance on costly empathetic speech instruction data and a lack of emotional expressiveness in the generated speech. Finetuning LLM with cross-modal empathetic instruction data may also lead to catastrophic forgetting and a degradation of its general capability. To address these challenges, we propose FreezeEmpath, an end-to-end empathetic spoken chatbot trained in a simple and efficient manner. The entire training process relies solely on existing speech instruction data and speech emotion recognition (SER) data, while keeping the LLM's parameters frozen. Experiments demonstrate that FreezeEmpath is able to generate emotionally expressive speech and outperforms other empathetic models in empathetic dialogue, SER, and SpokenQA tasks, demonstrating the effectiveness of our training strategy.

---


### 300. [MM-JudgeBias: A Benchmark for Evaluating Compositional Biases in MLLM-as-a-Judge](https://arxiv.org/abs/2604.18164)

**<font color=#1a73e8>作者：</font>** Sua Lee, Sanghee Park, Jinbae Im  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have been increasingly used as automatic evaluators-a paradigm known as MLLM-as-a-Judge. However, their reliability and vulnerabilities to biases remain underexplored. We find that many MLLM judges fail to reliably integrate key visual or textual cues, yielding unreliable evaluations when evidence is missing or mismatched, and exhibiting instability under semantically irrelevant perturbations. To address this, we systematically define Compositional Bias in MLLM-as-a-Judge systems and introduce MM-JudgeBias, a benchmark for evaluating it. MM-JudgeBias introduces controlled perturbations across Query, Image, and Response, and evaluates model behavior via two complementary metrics: Bias-Deviation (BD) for sensitivity and Bias-Conformity (BC) for stability. Our dataset of over 1,800 curated and refined multimodal samples, drawn from 29 source benchmarks, enables a fine-grained diagnosis of nine bias types across diverse tasks and domains. Experiments on 26 state-of-the-art MLLMs reveal systematic modality neglect and asymmetric evaluation tendencies, underscoring the need for more reliable judges.

---


> [!TIP]
> 当前位于：**251-300**（第 6/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
