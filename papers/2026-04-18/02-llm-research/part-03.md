# 🧠 大模型相关研究 | 2026年04月18日

> 本类共 **143** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-143**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-143**

---

### 101. [Segment-Level Coherence for Robust Harmful Intent Probing in LLMs](https://arxiv.org/abs/2604.14865)

**<font color=#1a73e8>作者：</font>** Xuanli He, Bilgehan Sel, Faizan Ali 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly exposed to adaptive jailbreaking, particularly in high-stakes Chemical, Biological, Radiological, and Nuclear (CBRN) domains. Although streaming probes enable real-time monitoring, they still make systematic errors. We identify a core issue: existing methods often rely on a few high-scoring tokens, leading to false alarms when sensitive CBRN terms appear in benign contexts. To address this, we introduce a streaming probing objective that requires multiple evidence tokens to consistently support a prediction, rather than relying on isolated spikes. This encourages more robust detection based on aggregated signals instead of single-token cues. At a fixed 1% false-positive rate, our method improves the true-positive rate by 35.55% relative to strong streaming baselines. We further observe substantial gains in AUROC, even when starting from near-saturated baseline performance (AUROC = 97.40%). We also show that probing Attention or MLP activations consistently outperforms residual-stream features. Finally, even when adversarial fine-tuning enables novel character-level ciphers, harmful intent remains detectable: probes developed for the base LLMs can be applied ``plug-and-play'' to these obfuscated attacks, achieving an AUROC of over 98.85%.

---


### 102. [MetaDent: Labeling Clinical Images for Vision-Language Models in Dentistry](https://arxiv.org/abs/2604.14866)

**<font color=#1a73e8>作者：</font>** Meng-Xun Li, Wen-Hui Deng, Zhi-Xing Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have demonstrated significant potential in medical image analysis, yet their application in intraoral photography remains largely underexplored due to the lack of fine-grained, annotated datasets and comprehensive benchmarks. To address this, we present MetaDent, a comprehensive resource that includes (1) a novel and large-scale dentistry image dataset collected from clinical, public, and web sources; (2) a semi-structured annotation framework designed to capture the hierarchical and clinically nuanced nature of dental photography; and (3) comprehensive benchmark suites for evaluating state-of-the-art VLMs on clinical image understanding. Our labeling approach combines a high-level image summary with point-by-point, free-text descriptions of abnormalities. This method enables rich, scalable, and task-agnostic representations. We curated 60,669 dental images from diverse sources and annotated a representative subset of 2,588 images using this meta-labeling scheme. Leveraging Large Language Models (LLMs), we derive standardized benchmarks: approximately 15K Visual Question Answering (VQA) pairs and an 18-class multi-label classification dataset, which we validated with human review and error analysis to justify that the LLM-driven transition reliably preserves fidelity and semantic accuracy. We then evaluate state-of-the-art VLMs across VQA, classification, and image captioning tasks. Quantitative results reveal that even the most advanced models struggle with a fine-grained understanding of intraoral scenes, achieving moderate accuracy and producing inconsistent or incomplete descriptions in image captioning. We publicly release our dataset, annotations, and tools to foster reproducible research and accelerate the development of vision-language systems for dental applications.

---


### 103. [Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis](https://arxiv.org/abs/2604.14877)

**<font color=#1a73e8>作者：</font>** Zhiyuan Zhai, Wenjing Yan, Xiaodan Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Does reinforcement learning genuinely expand what LLM agents can do, or merely make them more reliable? For static reasoning, recent work answers the second: base and RL pass@k curves converge at large k. We ask whether this holds for agentic tool use, where T rounds of interaction enable compositional strategies that re-sampling cannot recover. We introduce PASS@(k,T), a two-dimensional metric that jointly varies sampling budget k and interaction depth T, separating capability expansion from efficiency improvement. Our main finding is that, contrary to the static-reasoning result, tool-use RL genuinely enlarges the capability boundary: the RL agent's pass-curve pulls above the base model's and the gap widens at large k rather than converging. The expansion is specific to compositional, sequential information gathering; on simpler tasks RL behaves as prior work predicts. Under matched training data, supervised fine-tuning regresses the boundary on the same compositional tasks, isolating self-directed exploration as the causal factor. Mechanism analysis shows RL reweights the base strategy distribution toward the subset whose downstream reasoning more often yields a correct answer, with the improvement concentrated on how the agent integrates retrieved information. These results reconcile optimistic and pessimistic readings of RL for LLMs: both are correct, on different task types.

---


### 104. [Reasoning Dynamics and the Limits of Monitoring Modality Reliance in Vision-Language Models](https://arxiv.org/abs/2604.14888)

**<font color=#1a73e8>作者：</font>** Danae Sánchez Villegas, Samuel Lewis-Lim, Nikolaos Aletras 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in vision language models (VLMs) offer reasoning capabilities, yet how these unfold and integrate visual and textual information remains unclear. We analyze reasoning dynamics in 18 VLMs covering instruction-tuned and reasoning-trained models from two different model families. We track confidence over Chain-of-Thought (CoT), measure the corrective effect of reasoning, and evaluate the contribution of intermediate reasoning steps. We find that models are prone to answer inertia, in which early commitments to a prediction are reinforced, rather than revised during reasoning steps. While reasoning-trained models show stronger corrective behavior, their gains depend on modality conditions, from text-dominant to vision-only settings. Using controlled interventions with misleading textual cues, we show that models are consistently influenced by these cues even when visual evidence is sufficient, and assess whether this influence is recoverable from CoT. Although this influence can appear in the CoT, its detectability varies across models and depends on what is being monitored. Reasoning-trained models are more likely to explicitly refer to the cues, but their longer and fluent CoTs can still appear visually grounded while actually following textual cues, obscuring modality reliance. In contrast, instruction-tuned models refer to the cues less explicitly, but their shorter traces reveal inconsistencies with the visual input. Taken together, these findings indicate that CoT provides only a partial view of how different modalities drive VLM decisions, with important implications for the transparency and safety of multimodal systems.

---


### 105. [Can LLMs Score Medical Diagnoses and Clinical Reasoning as well as Expert Panels?](https://arxiv.org/abs/2604.14892)

**<font color=#1a73e8>作者：</font>** Amy Rouillard, Sitwala Mundiab, Linda Camarab 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluating medical AI systems using expert clinician panels is costly and slow, motivating the use of large language models (LLMs) as alternative adjudicators. Here, we evaluate an LLM jury composed of three frontier AI models scoring 3333 diagnoses on 300 real-world middle-income country (MIC) hospital cases. Model performance was benchmarked against expert clinician panel and independent human re-scoring panel evaluations. Both LLM and clinician-generated diagnoses are scored across four dimensions: diagnosis, differential diagnosis, clinical reasoning and negative treatment risk. For each of these, we assess scoring difference, inter-rater agreement, scoring stability, severe safety errors and the effect of post-hoc calibration. We find that: (i) the uncalibrated LLM jury scores are systematically lower than clinician panels scores; (ii) the LLM Jury preserves ordinal agreement and exhibits better concordance with the primary expert panels than the human expert re-score panels do; (iii) the probability of severe errors is lower in \lj models compared to the human expert re-score panels; (iv) the LLM Jury shows excellent agreement with primary expert panels' rankings. We find that the LLM jury combined with AI model diagnoses can be used to identify ward diagnoses at high risk of error, enabling targeted expert review and improved panel efficiency; (v) LLM jury models show no self-preference bias. They did not score diagnoses generated by their own underlying model or models from the same vendor more (or less) favourably than those generated by other models. Finally, we demonstrate that LLM jury calibration using isotonic regression improves alignment with human expert panel evaluations. Together, these results provide compelling evidence that a calibrated, multi-model LLM jury can serve as a trustworthy and reliable proxy for expert clinician evaluation in medical AI benchmarking.

---


### 106. [Beyond Importance Sampling: Rejection-Gated Policy Optimization](https://arxiv.org/abs/2604.14895)

**<font color=#1a73e8>作者：</font>** Ziwu Sun, Zhen Gao, Jiyong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a new perspective on policy optimization: rather than reweighting all samples by their importance ratios, an optimizer should select which samples are trustworthy enough to drive a policy update. Building on this view, we introduce Rejection-Gated Policy Optimization (RGPO), which replaces the importance sampling ratio r_theta = pi_theta / pi_old with a smooth, differentiable acceptance gate alpha_theta(s, a) = g(r_theta(s, a)) in the range [0, 1]. Unlike prior work that applies rejection sampling as a data-level heuristic before training, RGPO elevates rejection to an optimization principle: the gate participates directly in gradient computation and is implicitly updated alongside the policy. RGPO provides a unified framework: the policy gradients of TRPO, PPO, and REINFORCE all correspond to specific choices of the effective gradient weight w(r) = g'(r) * r. We prove that RGPO guarantees finite, bounded gradient variance even when importance sampling ratios are heavy-tailed (where IS variance diverges). We further show that RGPO incurs only a bounded, controllable bias and provides an approximate monotonic policy improvement guarantee analogous to TRPO. RGPO matches PPO in computational cost, requires no second-order optimization, and extends naturally to RLHF-style preference alignment. In online preference fine-tuning of Qwen2.5-1.5B-Instruct on Anthropic HH-RLHF (n = 3 seeds), RGPO uses a dual-ratio gate that anchors learning to both the previous policy and the reference model, achieving a Pareto-dominant outcome: the highest reward among online RL methods (+14.8% vs. PPO-RLHF) and the lowest KL divergence to the reference model (-16.0% vs. PPO-RLHF, -53.1% vs. GRPO).

---


### 107. [Toward Agentic RAG for Ukrainian](https://arxiv.org/abs/2604.14896)

**<font color=#1a73e8>作者：</font>** Marta Sumyk, Oleksandr Kosovan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present an initial investigation into Agentic Retrieval-Augmented Generation (RAG) for Ukrainian, conducted within the UNLP 2026 Shared Task on Multi-Domain Document Understanding. Our system combines two-stage retrieval (BGE-M3 with BGE reranking) with a lightweight agentic layer performing query rephrasing and answer-retry loops on top of Qwen2.5-3B-Instruct. Our analysis reveals that retrieval quality is the primary bottleneck: agentic retry mechanisms improve answer accuracy but the overall score remains constrained by document and page identification. We discuss practical limitations of offline agentic pipelines and outline directions for combining stronger retrieval with more advanced agentic reasoning for Ukrainian.

---


### 108. [ADAPT: Benchmarking Commonsense Planning under Unspecified Affordance Constraints](https://arxiv.org/abs/2604.14902)

**<font color=#1a73e8>作者：</font>** Pei-An Chen, Yong-Ching Liang, Jia-Fong Yeh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intelligent embodied agents should not simply follow instructions, as real-world environments often involve unexpected conditions and exceptions. However, existing methods usually focus on directly executing instructions, without considering whether the target objects can actually be manipulated, meaning they fail to assess available affordances. To address this limitation, we introduce DynAfford, a benchmark that evaluates embodied agents in dynamic environments where object affordances may change over time and are not specified in the instruction. DynAfford requires agents to perceive object states, infer implicit preconditions, and adapt their actions accordingly. To enable this capability, we introduce ADAPT, a plug-and-play module that augments existing planners with explicit affordance reasoning. Experiments demonstrate that incorporating ADAPT significantly improves robustness and task success across both seen and unseen environments. We also show that a domain-adapted, LoRA-finetuned vision-language model used as the affordance inference backend outperforms a commercial LLM (GPT-4o), highlighting the importance of task-aligned affordance grounding.

---


### 109. [IE as Cache: Information Extraction Enhanced Agentic Reasoning](https://arxiv.org/abs/2604.14930)

**<font color=#1a73e8>作者：</font>** Hang Lv, Sheng Liang, Hongchao Gu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Information Extraction aims to distill structured, decision-relevant information from unstructured text, serving as a foundation for downstream understanding and reasoning. However, it is traditionally treated merely as a terminal objective: once extracted, the resulting structure is often consumed in isolation rather than maintained and reused during multi-step inference. Moving beyond this, we propose \textit{IE-as-Cache}, a framework that repurposes IE as a cognitive cache to enhance agentic reasoning. Drawing inspiration from hierarchical computer memory, our approach combines query-driven extraction with cache-aware reasoning to dynamically maintain compact intermediate information and filter noise. Experiments on challenging benchmarks across diverse LLMs demonstrate significant improvements in reasoning accuracy, indicating that IE can be effectively repurposed as a reusable cognitive resource and offering a promising direction for future research on downstream uses of IE.

---


### 110. [WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training](https://arxiv.org/abs/2604.14932)

**<font color=#1a73e8>作者：</font>** Yifu Chen, Shengpeng Ji, Qian Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> End-to-end spoken dialogue models have garnered significant attention because they offer a higher potential ceiling in expressiveness and perceptual ability than cascaded systems. However, the intelligence and expressiveness of current open-source spoken dialogue models often remain below expectations. Motivated by the success of online reinforcement learning(RL) in other domains, one might attempt to directly apply preference optimization to spoken dialogue models, yet this transfer is non-trivial. We analyze these obstacles from the perspectives of reward modeling and rollout sampling, focusing on how sparse preference supervision interacts with dense speech generation under shared-parameter updates. Based on the analysis, we propose a modality-aware adaptive post-training recipe that makes RL practical for spoken dialogue: it constrains preference updates to the semantic channel and improves acoustic behavior via explicit anchoring, while dynamically regulating their mixture from rollout statistics to avoid unreliable preference gradients. We evaluate the method across multiple spoken dialogue benchmarks and representative architectures, and observe consistent improvements in semantic quality and speech expressiveness.

---


### 111. [Text2Arch: A Dataset for Generating Scientific Architecture Diagrams from Natural Language Descriptions](https://arxiv.org/abs/2604.14941)

**<font color=#1a73e8>作者：</font>** Shivank Garg, Sankalp Mittal, Manish Gupta  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Communicating complex system designs or scientific processes through text alone is inefficient and prone to ambiguity. A system that automatically generates scientific architecture diagrams from text with high semantic fidelity can be useful in multiple applications like enterprise architecture visualization, AI-driven software design, and educational content creation. Hence, in this paper, we focus on leveraging language models to perform semantic understanding of the input text description to generate intermediate code that can be processed to generate high-fidelity architecture diagrams. Unfortunately, no clean large-scale open-access dataset exists, implying lack of any effective open models for this task. Hence, we contribute a comprehensive dataset, \system, comprising scientific architecture images, their corresponding textual descriptions, and associated DOT code representations. Leveraging this resource, we fine-tune a suite of small language models, and also perform in-context learning using GPT-4o. Through extensive experimentation, we show that \system{} models significantly outperform existing baseline models like DiagramAgent and perform at par with in-context learning-based generations from GPT-4o. We make the code, data and models publicly available.

---


### 112. [RaTA-Tool: Retrieval-based Tool Selection with Multimodal Large Language Models](https://arxiv.org/abs/2604.14951)

**<font color=#1a73e8>作者：</font>** Gabriele Mattioli, Evelyn Turri, Sara Sarto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tool learning with foundation models aims to endow AI systems with the ability to invoke external resources -- such as APIs, computational utilities, and specialized models -- to solve complex tasks beyond the reach of standalone language generation. While recent advances in Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) have expanded their reasoning and perception capabilities, existing tool-use methods are predominantly limited to text-only inputs and closed-world settings. Consequently, they struggle to interpret multimodal user instructions and cannot generalize to tools unseen during training. In this work, we introduce RaTA-Tool, a novel framework for open-world multimodal tool selection. Rather than learning direct mappings from user queries to fixed tool identifiers, our approach enables an MLLM to convert a multimodal query into a structured task description and subsequently retrieve the most appropriate tool by matching this representation against semantically rich, machine-readable tool descriptions. This retrieval-based formulation naturally supports extensibility to new tools without retraining. To further improve alignment between task descriptions and tool selection, we incorporate a preference-based optimization stage using Direct Preference Optimization (DPO). To support research in this setting, we also introduce the first dataset for open-world multimodal tool use, featuring standardized tool descriptions derived from Hugging Face model cards. Extensive experiments demonstrate that our approach significantly improves tool-selection performance, particularly in open-world, multimodal scenarios.

---


### 113. [Calibration-Gated LLM Pseudo-Observations for Online Contextual Bandits](https://arxiv.org/abs/2604.14961)

**<font color=#1a73e8>作者：</font>** Maksim Pershin, Ivan Golovanov, Pavel Baltabaev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contextual bandit algorithms suffer from high regret during cold-start, when the learner has insufficient data to distinguish good arms from bad. We propose augmenting Disjoint LinUCB with LLM pseudo-observations: after each round, a large language model predicts counterfactual rewards for the unplayed arms, and these predictions are injected into the learner as weighted pseudo-observations. The injection weight is controlled by a calibration-gated decay schedule that tracks the LLM's prediction accuracy on played arms via an exponential moving average; high calibration error suppresses the LLM's influence, while accurate predictions receive higher weight during the critical early rounds. We evaluate on two contextual bandit environments - UCI Mushroom (2-arm, asymmetric rewards) and MIND-small (5-arm news recommendation) - and find that when equipped with a task-specific prompt, LLM pseudo-observations reduce cumulative regret by 19% on MIND relative to pure LinUCB. However, generic counterfactual prompt framing increases regret on both environments, demonstrating that prompt design is the dominant factor, more important than the choice of decay schedule or calibration gating parameters. We analyze the failure modes of calibration gating on domains with small prediction errors and provide a theoretical motivation for the bias-variance trade-off governing pseudo-observation weight.

---


### 114. [UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards](https://arxiv.org/abs/2604.14967)

**<font color=#1a73e8>作者：</font>** Jun Wang, Shuo Tan, Zelong Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) extends Large Vision-Language Models (LVLMs) with external visual knowledge. However, existing visual RAG systems typically rely on generic retrieval signals that overlook the fine-grained visual semantics essential for complex reasoning. To address this limitation, we propose UniDoc-RL, a unified reinforcement learning framework in which an LVLM agent jointly performs retrieval, reranking, active visual perception, and reasoning. UniDoc-RL formulates visual information acquisition as a sequential decision-making problem with a hierarchical action space. Specifically, it progressively refines visual evidence from coarse-grained document retrieval to fine-grained image selection and active region cropping, allowing the model to suppress irrelevant content and attend to information-dense regions. For effective end-to-end training, we introduce a dense multi-reward scheme that provides task-aware supervision for each action. Based on Group Relative Policy Optimization (GRPO), UniDoc-RL aligns agent behavior with multiple objectives without relying on a separate value network. To support this training paradigm, we curate a comprehensive dataset of high-quality reasoning trajectories with fine-grained action annotations. Experiments on three benchmarks demonstrate that UniDoc-RL consistently surpasses state-of-the-art baselines, yielding up to 17.7% gains over prior RL-based methods.

---


### 115. [Discovering Novel LLM Experts via Task-Capability Coevolution](https://arxiv.org/abs/2604.14969)

**<font color=#1a73e8>作者：</font>** Andrew Dai, Boris Meinardus, Ciaran Regan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier model developers aim to train models continually to possess emergent, diverse capabilities. To extend capabilities, the current pre-training and post-training paradigm requires manually starting training runs with static datasets or reward functions every time. Addressing this limitation, our work pursues the insight that open-endedness (via the coevolution of models and tasks) can discover models with increasingly novel skills in a single run. We introduce a new model development framework that extends coevolution to large language model (LLM) discovery, open-ended \textit{Assessment Coevolving with Diverse Capabilities} (AC/DC). AC/DC evolves both LLMs via model merging and natural language tasks via synthetic data generation. AC/DC discovers growing archives of LLMs that surpass the capabilities of larger LLMs while taking up less GPU memory. In particular, our LLM populations achieve a broader Coverage of expertise than other curated models or baselines on downstream benchmarks, without \textit{any} explicit benchmark optimization. Furthermore, AC/DC improves Coverage over time, continually innovates on tasks and models, and improves performance in multi-agent best-of-N selection. Our findings highlight the potential of coevolution as a means of discovering broader sets of capabilities from base LLMs. Overall, AC/DC brings us one step closer to a profoundly new paradigm of LLM development, where continual improvements to the diversity of model capabilities can be accelerated by leveraging existing models as stepping stones to increasingly powerful models.

---


### 116. [Explain the Flag: Contextualizing Hate Speech Beyond Censorship](https://arxiv.org/abs/2604.14970)

**<font color=#1a73e8>作者：</font>** Jason Liartis, Eirini Kaldeli, Lambrini Gyftokosta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hate, derogatory, and offensive speech remains a persistent challenge in online platforms and public discourse. While automated detection systems are widely used, most focus on censorship or removal, raising concerns for transparency and freedom of expression, and limiting opportunities to explain why content is harmful. To address these issues, explanatory approaches have emerged as a promising solution, aiming to make hate speech detection more transparent, accountable, and informative. In this paper, we present a hybrid approach that combines Large Language Models (LLMs) with three newly created and curated vocabularies to detect and explain hate speech in English, French, and Greek. Our system captures both inherently derogatory expressions tied to identity characteristics and direct group-targeted content through two complementary pipelines: one that detects and disambiguates problematic terms using the curated vocabularies, and one that leverages LLMs as context-aware evaluators of group-targeting content. The outputs are fused into grounded explanations that clarify why content is flagged. Human evaluation shows that our hybrid approach is accurate, with high-quality explanations, outperforming LLM-only baselines.

---


### 117. [Agentic Explainability at Scale: Between Corporate Fears and XAI Needs](https://arxiv.org/abs/2604.14984)

**<font color=#1a73e8>作者：</font>** Yomna Elsayed, Cecily Jones  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As companies enter the race for agentic AI adoption, fears surface around agentic autonomy and its subsequent risks. These fears compound as companies scale their agentic AI adoption with low-code applications, without a comparable scaling in their governance processes and expertise resulting in a phenomenon known as "Agent Sprawl". While shadow AI tools can help with agentic discovery and identification, few observability tools offer insights into the agents' configuration and settings or the decision-making process during agent-to-agent communication and orchestration. This paper explores AI governance professionals' concerns in enterprise settings, while offering design-time and runtime explainability techniques as suggested by AI governance experts for addressing those fears. Finally, we provide a preliminary prototype of an Agentic AI Card that can help companies feel at ease deploying agents at scale.

---


### 118. [Dr.~RTL: Autonomous Agentic RTL Optimization through Tool-Grounded Self-Improvement](https://arxiv.org/abs/2604.14989)

**<font color=#1a73e8>作者：</font>** Wenji Fang, Yao Lu, Shang Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have sparked growing interest in automatic RTL optimization for better performance, power, and area (PPA). However, existing methods are still far from realistic RTL optimization. Their evaluation settings are often unrealistic: they are tested on manually degraded, small-scale RTL designs and rely on weak open-source tools. Their optimization methods are also limited, relying on coarse design-level feedback and simple pre-defined rewriting rules. To address these limitations, we present Dr. RTL, an agentic framework for RTL timing optimization in a realistic evaluation environment, with continual self-improvement through reusable optimization skills. We establish a realistic evaluation setting with more challenging RTL designs and an industrial EDA workflow. Within this setting, Dr. RTL performs closed-loop optimization through a multi-agent framework for critical-path analysis, parallel RTL rewriting, and tool-based evaluation. We further introduce group-relative skill learning, which compares parallel RTL rewrites and distills the optimization experience into an interpretable skill library. Currently, this library contains 47 pattern--strategy entries for cross-design reuse to improve PPA and accelerate convergence, and it can continue evolving over time. Evaluated on 20 real-world RTL designs, Dr. RTL achieves average WNS/TNS improvements of 21\%/17\% with a 6\% area reduction over the industry-leading commercial synthesis tool.

---


### 119. [The Possibility of Artificial Intelligence Becoming a Subject and the Alignment Problem](https://arxiv.org/abs/2604.14990)

**<font color=#1a73e8>作者：</font>** Till Mossakowski, Helena Esther Grass  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial General Intelligence (AGI) is increasingly being discussed not only as a tool, but also as a potential subject with personal and therefore moral status. In our opinion, the currently dominant alignment strategies, which focus on human control and containment of AI, therefore fall short. Building on Turing's analogy of "child machines", we are developing a vision of the possibility of autonomy-supporting parenting of AI, in which human control over a developing AGI is gradually reduced, allowing AI to become an independent, autonomous subject. Rather than viewing AGI, as is currently prevalent, as a dangerous creature that needs to be locked up and controlled, we should approach potential AGI with respect for a possible developing subject on the one hand, and with full confidence in our human capabilities on the other. Such a perspective opens up the possibility of cooperative coexistence and co-evolution between humans and AGIs. The relationship between humans and AGIs will thus have to be newly determined, which will change our self-image as humans. It will be crucial that humans not only claim control over potential AGIs, but also engage with AGIs through surprise, creativity, and other specifically human qualities, thereby offering them motivating incentives for cooperation.

---


### 120. [Predicting Power-System Dynamic Trajectories with Foundation Models](https://arxiv.org/abs/2604.14991)

**<font color=#1a73e8>作者：</font>** Haoran Li, Lihao Mai, Chenhan Xiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As power systems transition toward renewable-rich and inverter-dominated operations, accurate time-domain dynamic analysis becomes increasingly critical. Such analysis supports key operational tasks, including transient stability assessment, dynamic security analysis, contingency screening, and post-fault trajectory evaluation. In practice, these tasks may operate under several challenges, including unknown and time-varying system parameters, privacy constraints on data sharing, and the need for fast online inference. Existing learning-based approaches are typically trained for individual systems and therefore lack generalization across operating conditions and physical parameters. Hence, this paper proposes LArge Scale Small ODE (LASS)-ODE-Power, a learning framework for general-purpose time-domain prediction. The proposed approach leverages large-scale pretraining on more than 40 GB of DAE or ordinary differential-equation (ODE) trajectories to learn transferable representations. The resulting model supports trajectory prediction from short measurement prefixes across diverse dynamic regimes, including electromechanical and inverter-driven systems. Hence, the model can be directly used without data sharing in a zero-shot setting. In addition, the proposed architecture incorporates parallel and linearized computation to achieve fast inference. Moreover, to enhance task-specific performance in power systems, a specialized fine-tuning strategy is developed based on approximately 1 GB of heterogeneous power-system dynamic data. Extensive experiments over diverse power-system simulation scenarios demonstrate that LASS-ODE-Power consistently outperforms existing learning-based models in trajectory prediction accuracy with efficient inference.

---


### 121. [COEVO: Co-Evolutionary Framework for Joint Functional Correctness and PPA Optimization in LLM-Based RTL Generation](https://arxiv.org/abs/2604.15001)

**<font color=#1a73e8>作者：</font>** Heng Ping, Peiyu Zhang, Shixuan Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based RTL code generation methods increasingly target both functional correctness and PPA quality, yet existing approaches universally decouple the two objectives, optimizing PPA only after correctness is fully achieved. Whether through sequential multi-agent pipelines, evolutionary search with binary correctness gates, or hierarchical reward dependencies, partially correct but architecturally promising candidates are systematically discarded. Moreover, existing methods reduce the multi-objective PPA space to a single scalar fitness, obscuring the trade-offs among area, delay, and power. To address these limitations, we propose COEVO, a co-evolutionary framework that unifies correctness and PPA optimization within a single evolutionary loop. COEVO formulates correctness as a continuous co-optimization dimension alongside area, delay, and power, enabled by an enhanced testbench that provides fine-grained scoring and detailed diagnostic feedback. An adaptive correctness gate with annealing allows PPA-promising but partially correct candidates to guide the search toward jointly optimal solutions. To preserve the full PPA trade-off structure, COEVO employs four-dimensional Pareto-based non-dominated sorting with configurable intra-level sorting, replacing scalar fitness without manual weight tuning. Evaluated on VerilogEval 2.0 and RTLLM 2.0, COEVO achieves 97.5\% and 94.5\% Pass@1 with GPT-5.4-mini, surpassing all agentic baselines across four LLM backbones, while attaining the best PPA on 43 out of 49 synthesizable RTLLM designs.

---


### 122. [Towards Faster Language Model Inference Using Mixture-of-Experts Flow Matching](https://arxiv.org/abs/2604.15009)

**<font color=#1a73e8>作者：</font>** Aihua Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flow matching retains the generation quality of diffusion models while enabling substantially faster inference, making it a compelling paradigm for generative modeling. However, when applied to language modeling, it exhibits fundamental limitations in representing complex latent distributions with irregular geometries, such as anisotropy and multimodality. To address these challenges, we propose a mixture-of-experts flow matching (MoE-FM) framework, which captures complex global transport geometries in latent space by decomposing them into locally specialized vector fields. Building on MoE-FM, we develop a non-autoregressive (NAR) language modeling approach, named YAN, instantiated with both Transformer and Mamba architectures. Across multiple downstream tasks, YAN achieves generation quality on par with both autoregressive (AR) and diffusion-based NAR language models, while requiring as few as three sampling steps. This yields a $40\times$ speedup over AR baselines and up to a $10^3\times$ speedup over diffusion language models, demonstrating substantial efficiency advantages for language modeling.

---


### 123. [DLink: Distilling Layer-wise and Dominant Knowledge from EEG Foundation Models](https://arxiv.org/abs/2604.15016)

**<font color=#1a73e8>作者：</font>** Jingyuan Wang, Meiyan Xu, Zhihao Jia 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> EEG foundation models (FMs) achieve strong cross-subject and cross-task generalization but impose substantial computational and memory costs that hinder deployment on embedded BCI systems. Knowledge distillation is a natural solution; however, conventional methods fail for EEG FMs because task-relevant semantics are often distributed across intermediate layers, and aggressive dimensionality reduction can distort oscillatory structure via representational collapse and aliasing. To address these challenges, we propose DLink (Distilling Layer-wise and Dominant Knowledge), a unified framework for transferring knowledge from large EEG FMs to compact students with three key innovations: (1) a dynamic Router that adaptively aggregates teacher layers to capture dominant intermediate representations; (2) an EEG MiC student with a Mimic-then-Compress pipeline, which inherits high-dimensional teacher features and then applies structured spatio-temporal compression to avoid a heavy classification head; and (3) spectral distillation that aligns teacher-student representations in the frequency domain to regularize compression and mitigate aliasing and temporal jitter. Experiments on four EEG benchmarks show that DLink enables compact students to outperform lightweight baselines while approaching fully fine-tuned FM performance at substantially lower model size and inference cost.

---


### 124. [From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench](https://arxiv.org/abs/2604.15037)

**<font color=#1a73e8>作者：</font>** Ke Xu, Yuhao Wang, Yu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in LLM agents are gradually shifting from reactive, text-based paradigms toward proactive, multimodal interaction. However, existing benchmarks primarily focus on reactive responses, overlooking the complexities of proactive intervention and monitoring. To bridge this gap, we introduce ProVoice-Bench, the first evaluation framework specifically designed for proactive voice agents, featuring four novel tasks. By leveraging a multi-stage data synthesis pipeline, we curate 1,182 high-quality samples for rigorous testing. Our evaluation of state-of-the-art Multimodal LLMs reveals a significant performance gap, particularly regarding over-triggering and reasoning capabilities. These findings highlight the limitations of current models and offer a roadmap for developing more natural, context-aware proactive agents.

---


### 125. [Beyond Visual Cues: Semantic-Driven Token Filtering and Expert Routing for Anytime Person ReID](https://arxiv.org/abs/2604.15090)

**<font color=#1a73e8>作者：</font>** Jiaxuan Li, Xin Wen, Zhihang Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Any-Time Person Re-identification (AT-ReID) necessitates the robust retrieval of target individuals under arbitrary conditions, encompassing both modality shifts (daytime and nighttime) and extensive clothing-change scenarios, ranging from short-term to long-term intervals. However, existing methods are highly relying on pure visual features, which are prone to change due to environmental and time factors, resulting in significantly performance deterioration under scenarios involving illumination caused modality shifts or cloth-change. In this paper, we propose Semantic-driven Token Filtering and Expert Routing (STFER), a novel framework that leverages the ability of Large Vision-Language Models (LVLMs) to generate identity consistency text, which provides identity-discriminative features that are robust to both clothing variations and cross-modality shifts between RGB and IR. Specifically, we employ instructions to guide the LVLM in generating identity-intrinsic semantic text that captures biometric constants for the semantic model driven. The text token is further used for Semantic-driven Visual Token Filtering (SVTF), which enhances informative visual regions and suppresses redundant background noise. Meanwhile, the text token is also used for Semantic-driven Expert Routing (SER), which integrates the semantic text into expert routing, resulting in more robust multi-scenario gating. Extensive experiments on the Any-Time ReID dataset (AT-USTC) demonstrate that our model achieves state-of-the-art results. Moreover, the model trained on AT-USTC was evaluated across 5 widely-used ReID benchmarks demonstrating superior generalization capabilities with highly competitive results. Our code will be available soon.

---


### 126. [OpenMobile: Building Open Mobile Agents with Task and Trajectory Synthesis](https://arxiv.org/abs/2604.15093)

**<font color=#1a73e8>作者：</font>** Kanzhi Cheng, Zehao Li, Zheng Ma 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mobile agents powered by vision-language models have demonstrated impressive capabilities in automating mobile tasks, with recent leading models achieving a marked performance leap, e.g., nearly 70% success on AndroidWorld. However, these systems keep their training data closed and remain opaque about their task and trajectory synthesis recipes. We present OpenMobile, an open-source framework that synthesizes high-quality task instructions and agent trajectories, with two key components: (1) The first is a scalable task synthesis pipeline that constructs a global environment memory from exploration, then leverages it to generate diverse and grounded instructions. and (2) a policy-switching strategy for trajectory rollout. By alternating between learner and expert models, it captures essential error-recovery data often missing in standard imitation learning. Agents trained on our data achieve competitive results across three dynamic mobile agent benchmarks: notably, our fine-tuned Qwen2.5-VL and Qwen3-VL reach 51.7% and 64.7% on AndroidWorld, far surpassing existing open-data approaches. Furthermore, we conduct transparent analyses on the overlap between our synthetic instructions and benchmark test sets, and verify that performance gains stem from broad functionality coverage rather than benchmark overfitting. We release data and code at this https URL to bridge the data gap and facilitate broader mobile agent research.

---


### 127. [IUQ: Interrogative Uncertainty Quantification for Long-Form Large Language Model Generation](https://arxiv.org/abs/2604.15109)

**<font color=#1a73e8>作者：</font>** Haozhi Fan, Jinhao Duan, Kaidi Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite the rapid advancement of Large Language Models (LLMs), uncertainty quantification in LLM generation is a persistent challenge. Although recent approaches have achieved strong performance by restricting LLMs to produce short or constrained answer sets, many real-world applications require long-form and free-form text generation. A key difficulty in this setting is that LLMs often produce responses that are semantically coherent yet factually inaccurate, while the underlying semantics are multifaceted and the linguistic structure is complex. To tackle this challenge, this paper introduces Interrogative Uncertainty Quantification (IUQ), a novel framework that leverages inter-sample consistency and intra-sample faithfulness to quantify the uncertainty in long-form LLM outputs. By utilizing an interrogate-then-respond paradigm, our method provides reliable measures of claim-level uncertainty and the model's faithfulness. Experimental results across diverse model families and model sizes demonstrate the superior performance of IUQ over two widely used long-form generation datasets. The code is available at this https URL.

---


### 128. [Blinded Multi-Rater Comparative Evaluation of a Large Language Model and Clinician-Authored Responses in CGM-Informed Diabetes Counseling](https://arxiv.org/abs/2604.15124)

**<font color=#1a73e8>作者：</font>** Zhijun Guo, Alvina Lai, Emmanouil Korakas 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Continuous glucose monitoring (CGM) is central to diabetes care, but explaining CGM patterns clearly and empathetically remains time-intensive. Evidence for retrieval-grounded large language model (LLM) systems in CGM-informed counseling remains limited. To evaluate whether a retrieval-grounded LLM-based conversational agent (CA) could support patient understanding of CGM data and preparation for routine diabetes consultations. We developed a retrieval-grounded LLM-based CA for CGM interpretation and diabetes counseling support. The system generated plain-language responses while avoiding individualized therapeutic advice. Twelve CGM-informed cases were constructed from publicly available datasets. Between Oct 2025 and Feb 2026, 6 senior UK diabetes clinicians each reviewed 2 assigned cases and answered 24 questions. In a blinded multi-rater evaluation, each CA-generated and clinician-authored response was independently rated by 3 clinicians on 6 quality dimensions. Safety flags and perceived source labels were also recorded. Primary analyses used linear mixed-effects models. A total of 288 unique responses (144 CA and 144 clinician) generated 864 ratings. The CA received higher quality scores than clinician responses (mean 4.37 vs 3.58), with an estimated mean difference of 0.782 points (95% CI 0.692-0.872; P<.001). The largest differences were for empathy (1.062, 95% CI 0.948-1.177) and actionability (0.992, 95% CI 0.877-1.106). Safety flag distributions were similar, with major concerns rare in both groups (3/432, 0.7% each). Retrieval-grounded LLM systems may have value as adjunct tools for CGM review, patient education, and preconsultation preparation. However, these findings do not support autonomous therapeutic decision-making or unsupervised real-world use.

---


### 129. [DiscoTrace: Representing and Comparing Answering Strategies of Humans and LLMs in Information-Seeking Question Answering](https://arxiv.org/abs/2604.15140)

**<font color=#1a73e8>作者：</font>** Neha Srikanth, Jordan Boyd-Graber, Rachel Rudinger  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce DiscoTrace, a method to identify the rhetorical strategies that answerers use when responding to information-seeking questions. DiscoTrace represents answers as a sequence of question-related discourse acts paired with interpretations of the original question, annotated on top of rhetorical structure theory parses. Applying DiscoTrace to answers from nine different human communities reveals that communities have diverse preferences for answer construction. In contrast, LLMs do not exhibit rhetorical diversity in their answers, even when prompted to mimic specific human community answering guidelines. LLMs also systematically opt for breadth, addressing interpretations of questions that human answerers choose not to address. Our findings can guide the development of pragmatic LLM answerers that consider a range of strategies informed by context in QA.

---


### 130. [IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning](https://arxiv.org/abs/2604.15148)

**<font color=#1a73e8>作者：</font>** Zihan Liang, Yufei Ma, Ben Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning has emerged as an effective paradigm for training large language models to perform search-augmented reasoning. However, existing approaches rely on trajectory-level rewards that cannot distinguish precise search queries from vague or redundant ones within a rollout group, and collapse to a near-zero gradient signal whenever every sampled trajectory fails. In this paper, we propose IG-Search, a reinforcement learning framework that introduces a step-level reward based on Information Gain (IG). For each search step, IG measures how much the retrieved documents improve the model's confidence in the gold answer relative to a counterfactual baseline of random documents, thereby reflecting the effectiveness of the underlying search query. This signal is fed back to the corresponding search-query tokens via per-token advantage modulation in GRPO, enabling fine-grained, step-level credit assignment within a rollout. Unlike prior step-level methods that require either externally annotated intermediate supervision or shared environment states across trajectories, IG-Search derives its signals from the policy's own generation probabilities, requiring no intermediate annotations beyond standard question-answer pairs. Experiments on seven single-hop and multi-hop QA benchmarks demonstrate that IG-Search achieves an average EM of 0.430 with Qwen2.5-3B, outperforming the strongest trajectory-level baseline (MR-Search) by 1.6 points and the step-level method GiGPO by 0.9 points on average across benchmarks, with particularly pronounced gains on multi-hop reasoning tasks. Despite introducing a dense step-level signal, IG-Search adds only ~6.4% to per-step training wall-clock time over the trajectory-level baseline and leaves inference latency unchanged, while still providing a meaningful gradient signal even when every sampled trajectory answers incorrectly.

---


### 131. [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)

**<font color=#1a73e8>作者：</font>** Lukas Helff, Quentin Delfosse, David Steinmann 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As reinforcement Learning with Verifiable Rewards (RLVR) has become the dominant paradigm for scaling reasoning capabilities in LLMs, a new failure mode emerges: LLMs gaming verifiers. We study this phenomenon on inductive reasoning tasks, where models must induce and output logical rules. We find that RLVR-trained models systematically abandon rule induction. Instead of learning generalizable patterns (e.g., ``trains carrying red cars go east''), they enumerate instance-level labels, producing outputs that pass verifiers without capturing the relational patterns required by the task. We show that this behavior is not a failure of understanding but a form of reward hacking: imperfect verifiers that check only extensional correctness admit false positives. To detect such shortcuts, we introduce Isomorphic Perturbation Testing (IPT), which evaluates a single model output under both extensional and isomorphic verification, where the latter enforces invariance under logically isomorphic tasks. While genuine rule induction remains invariant, shortcut strategies fail. We find that shortcut behavior is specific to RLVR-trained reasoning models (e.g., GPT-5, Olmo3) and absent in non-RLVR models (e.g., GPT-4o, GPT-4.5, Ministral). Moreover, shortcut prevalence increases with task complexity and inference-time compute. In controlled training experiments, extensional verification directly induces shortcut strategies, while isomorphic verification eliminates them. These results show that RLVR can incentivize reward hacking not only through overt manipulation but also by exploiting what the verifier fails to enforce.

---


### 132. [QuantCode-Bench: A Benchmark for Evaluating the Ability of Large Language Models to Generate Executable Algorithmic Trading Strategies](https://arxiv.org/abs/2604.15151)

**<font color=#1a73e8>作者：</font>** Alexey Khoroshilov, Alexey Chernysh, Orkhan Ekhtibarov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have demonstrated strong performance on general-purpose programming tasks, yet their ability to generate executable algorithmic trading strategies remains underexplored. Unlike standard code benchmarks, trading-strategy generation requires simultaneous mastery of domain-specific financial logic, knowledge of a specialized API, and the ability to produce code that is not only syntactically correct but also leads to actual trades on historical data. In this work, we present QuantCode-Bench, a benchmark for the systematic evaluation of modern LLMs in generating strategies for the Backtrader framework from textual descriptions in English. The benchmark contains 400 tasks of varying difficulty collected from Reddit, TradingView, StackExchange, GitHub, and synthetic sources. Evaluation is conducted through a multi-stage pipeline that checks syntactic correctness, successful backtest execution, the presence of trades, and semantic alignment with the task description using an LLM judge. We compare state-of-the-art models in two settings: single-turn, where the strategy must be generated correctly on the first attempt, and agentic multi-turn, where the model receives iterative feedback and may repair its errors. We analyze the failure modes across different stages of the pipeline and show that the main limitations of current models are not related to syntax, but rather to the correct operationalization of trading logic, proper API usage, and adherence to task semantics. These findings suggest that trading strategy generation constitutes a distinct class of domain-specific code generation tasks in which success requires not only technical correctness, but also alignment between natural-language descriptions, financial logic, and the observable behavior of the strategy on data.

---


### 133. [Compressing Sequences in the Latent Embedding Space: $K$-Token Merging for Large Language Models](https://arxiv.org/abs/2604.15153)

**<font color=#1a73e8>作者：</font>** Zihao Xu, John Harvill, Ziwei Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) incur significant computational and memory costs when processing long prompts, as full self-attention scales quadratically with input length. Token compression aims to address this challenge by reducing the number of tokens representing inputs. However, existing prompt-compression approaches primarily operate in token space and overlook inefficiencies in the latent embedding space. In this paper, we propose K-Token Merging, a latent-space compression framework that merges each contiguous block of K token embeddings into a single embedding via a lightweight encoder. The compressed sequence is processed by a LoRA-adapted LLM, while generation remains in the original vocabulary. Experiments on structural reasoning (Textualized Tree), sentiment classification (Amazon Reviews), and code editing (CommitPackFT) show that K-Token Merging lies on the Pareto frontier of performance vs. compression, achieving up to 75% input length reduction with minimal performance degradation.

---


### 134. [Assessing the Potential of Masked Autoencoder Foundation Models in Predicting Downhole Metrics from Surface Drilling Data](https://arxiv.org/abs/2604.15169)

**<font color=#1a73e8>作者：</font>** Aleksander Berezowski, Hassan Hassanzadeh, Gouri Ginde  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Oil and gas drilling operations generate extensive time-series data from surface sensors, yet accurate real-time prediction of critical downhole metrics remains challenging due to the scarcity of labelled downhole measurements. This systematic mapping study reviews thirteen papers published between 2015 and 2025 to assess the potential of Masked Autoencoder Foundation Models (MAEFMs) for predicting downhole metrics from surface drilling data. The review identifies eight commonly collected surface metrics and seven target downhole metrics. Current approaches predominantly employ neural network architectures such as artificial neural networks (ANNs) and long short-term memory (LSTM) networks, yet no studies have explored MAEFMs despite their demonstrated effectiveness in time-series modeling. MAEFMs offer distinct advantages through self-supervised pre-training on abundant unlabeled data, enabling multi-task prediction and improved generalization across wells. This research establishes that MAEFMs represent a technically feasible but unexplored opportunity for drilling analytics, recommending future empirical validation of their performance against existing models and exploration of their broader applicability in oil and gas operations.

---


### 135. [VisPCO: Visual Token Pruning Configuration Optimization via Budget-Aware Pareto-Frontier Learning for Vision-Language Models](https://arxiv.org/abs/2604.15188)

**<font color=#1a73e8>作者：</font>** Huawei Ji, Yuanhao Sun, Yuan Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning methods effectively mitigate the quadratic computational growth caused by processing high-resolution images and video frames in vision-language models (VLMs). However, existing approaches rely on predefined pruning configurations without determining whether they achieve computation-performance optimality. In this work, we introduce , a novel framework that formulates visual token pruning as a Pareto configuration optimization problem to automatically identify optimal configurations. Our approach employs continuous relaxation and straight-through estimators to enable gradient-based search, solved via the Augmented Lagrangian method. Extensive experiments across 8 visual benchmarks demonstrate that effectively approximates the empirical Pareto frontier obtained through grid search and generalizes well across various pruning methods and VLM architectures. Furthermore, through learnable kernel functions, we investigate layer-wise pruning patterns and reveal that multi-step progressive pruning captures VLMs' hierarchical compression structure, achieving superior accuracy-efficiency trade-offs compared to single-layer approaches.

---


### 136. [Learning to Think Like a Cartoon Captionist: Incongruity-Resolution Supervision for Multimodal Humor Understanding](https://arxiv.org/abs/2604.15210)

**<font color=#1a73e8>作者：</font>** Hatice Merve Vural, Doga Kukul, Ege Erdem Ozlu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Humor is one of the few cognitive tasks where getting the reasoning right matters as much as getting the answer right. While recent work evaluates humor understanding on benchmarks such as the New Yorker Cartoon Caption Contest (NYCC), it largely treats it as black-box prediction, overlooking the structured reasoning processes underlying humor comprehension. We introduce IRS (Incongruity-Resolution Supervision), a framework that decomposes humor understanding into three components: incongruity modeling, which identifies mismatches in the visual scene; resolution modeling, which constructs coherent reinterpretations of these mismatches; and preference alignment, which evaluates candidate interpretations under human judgments. Grounded in incongruity-resolution theory and expert captionist practice, IRS supervises intermediate reasoning process through structured traces that make the path from visual perception to humorous interpretation explicit and learnable. Across 7B, 32B, and 72B models on NYCC, IRS outperforms strong open and closed multimodal baselines across caption matching and ranking tasks, with our largest model approaching expert-level performance on ranking. Zero-shot transfer to external benchmarks shows that IRS learns generalizable reasoning patterns. Our results suggest that supervising reasoning structure, rather than scale alone, is key for reasoning-centric tasks.

---


### 137. [UrbanClipAtlas: A Visual Analytics Framework for Event and Scene Retrieval in Urban Videos](https://arxiv.org/abs/2604.15225)

**<font color=#1a73e8>作者：</font>** Joel Perca, Luis Sante, Juanpablo Heredia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extracting actionable insights from long-duration urban videos is often labor-intensive: analysts must manually sift through raw footage to pinpoint target events or uncover broader behavioral trends. In this work, we present URBANCLIPATLAS, a visual analytics system for exploring long urban videos recorded at street intersections. URBANCLIPATLAS combines retrieval-augmented generation (RAG), taxonomy-aware entity extraction, and video grounding to support event retrieval and interpretation. The system segments extended recordings into short clips, generates textual descriptions with a vision-language model, and indexes them for semantic retrieval. A knowledge graph maps entities and relations from LLM answers onto a domain-specific taxonomy and aligns them with detected objects and trajectories to support visual grounding and verification. URBANCLIPATLAS supports scene retrieval through an augmented chat-based interface and improves scene interpretation by tightly aligning textual outputs with video evidence. This design strengthens the connection between textual reasoning and visual evidence, reducing the effort required to validate model outputs and refine hypotheses. We demonstrate the usefulness of URBANCLIPATLAS on the StreetAware dataset through two case studies involving hazardous scenarios and crossing dynamics at street intersections. URBANCLIPATLAS helps analysts reason about safety- and mobility-related patterns across large urban video collections.

---


### 138. [Why Do Vision Language Models Struggle To Recognize Human Emotions?](https://arxiv.org/abs/2604.15280)

**<font color=#1a73e8>作者：</font>** Madhav Agarwal, Sotirios A. Tsaftaris, Laura Sevilla-Lara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding emotions is a fundamental ability for intelligent systems to be able to interact with humans. Vision-language models (VLMs) have made tremendous progress in the last few years for many visual tasks, potentially offering a promising solution for understanding emotions. However, it is surprising that even the most sophisticated contemporary VLMs struggle to recognize human emotions or to outperform even specialized vision-only classifiers. In this paper we ask the question "Why do VLMs struggle to recognize human emotions?", and observe that the inherently continuous and dynamic task of facial expression recognition (DFER) exposes two critical VLM vulnerabilities. First, emotion datasets are naturally long-tailed, and the web-scale data used to pre-train VLMs exacerbates this head-class bias, causing them to systematically collapse rare, under-represented emotions into common categories. We propose alternative sampling strategies that prevent favoring common concepts. Second, temporal information is critical for understanding emotions. However, VLMs are unable to represent temporal information over dense frame sequences, as they are limited by context size and the number of tokens that can fit in memory, which poses a clear challenge for emotion recognition. We demonstrate that the sparse temporal sampling strategy used in VLMs is inherently misaligned with the fleeting nature of micro-expressions (0.25-0.5 seconds), which are often the most critical affective signal. As a diagnostic probe, we propose a multi-stage context enrichment strategy that utilizes the information from "in-between" frames by first converting them into natural language summaries. This enriched textual context is provided as input to the VLM alongside sparse keyframes, preventing attentional dilution from excessive visual data while preserving the emotional trajectory.

---


### 139. [How Do LLMs and VLMs Understand Viewpoint Rotation Without Vision? An Interpretability Study](https://arxiv.org/abs/2604.15294)

**<font color=#1a73e8>作者：</font>** Zhen Yang, Ping Jian, Zhongbin Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Over the past year, spatial intelligence has drawn increasing attention. Many prior works study it from the perspective of visual-spatial intelligence, where models have access to visuospatial information from visual inputs. However, in the absence of visual information, whether linguistic intelligence alone is sufficient to endow models with spatial intelligence, and how models perform relevant tasks with text-only inputs still remain unexplored. Therefore, in this paper, we focus on a fundamental and critical capability in spatial intelligence from a linguistic perspective: viewpoint rotation understanding (VRU). Specifically, LLMs and VLMs are asked to infer their final viewpoint and predict the corresponding observation in an environment given textual description of viewpoint rotation and observation over multiple steps. We find that both LLMs and VLMs perform poorly on our proposed dataset while human can easily achieve 100% accuracy, indicating a substantial gap between current model capabilities and the requirements of spatial intelligence. To uncover the underlying mechanisms, we conduct a layer-wise probing analysis and head-wise causal intervention. Our findings reveal that although models encode viewpoint information in the hidden states, they appear to struggle to bind the viewpoint position with corresponding observation, resulting in a hallucination in final layers. Finally, we selectively fine-tune the key attention heads identified by causal intervention to improve VRU performance. Experimental results demonstrate that such selective fine-tuning achieves improved VRU performance while avoiding catastrophic forgetting of generic abilities. Our dataset and code will be released at this https URL .

---


### 140. [Diagnosing LLM Judge Reliability: Conformal Prediction Sets and Transitivity Violations](https://arxiv.org/abs/2604.15302)

**<font color=#1a73e8>作者：</font>** Manan Gupta, Dhruv Kumar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-judge frameworks are increasingly used for automatic NLG evaluation, yet their per-instance reliability remains poorly understood. We present a two-pronged diagnostic toolkit applied to SummEval: $\textbf{(1)}$ a transitivity analysis that reveals widespread per-input inconsistency masked by low aggregate violation rates ($\bar{\rho} = 0.8$-$4.1\%$), with $33$-$67\%$ of documents exhibiting at least one directed 3-cycle; and $\textbf{(2)}$ split conformal prediction sets over 1-5 Likert scores providing theoretically-guaranteed $\geq(1{-}\alpha)$ coverage, with set width serving as a per-instance reliability indicator ($r_s = {+}0.576$, $N{=}1{,}918$, $p < 10^{-100}$, pooled across all judges). Critically, prediction set width shows consistent cross-judge agreement ($\bar{r} = 0.32$-$0.38$), demonstrating it captures document-level difficulty rather than judge-specific noise. Across four judges and four criteria, both diagnostics converge: criterion matters more than judge, with relevance judged most reliably (avg. set size $\approx 3.0$) and coherence moderately so (avg. set size $\approx 3.9$), while fluency and consistency remain unreliable (avg. set size $\approx 4.9$). We release all code, prompts, and cached results.

---


### 141. [Generalization in LLM Problem Solving: The Case of the Shortest Path](https://arxiv.org/abs/2604.15306)

**<font color=#1a73e8>作者：</font>** Yao Tong, Jiayuan Ye, Anastasia Borovykh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Whether language models can systematically generalize remains actively debated. Yet empirical performance is jointly shaped by multiple factors such as training data, training paradigms, and inference-time strategies, making failures difficult to interpret. We introduce a controlled synthetic environment based on shortest-path planning, a canonical composable sequential optimization problem. The setup enables clean separation of these factors and supports two orthogonal axes of generalization: spatial transfer to unseen maps and length scaling to longer-horizon problems. We find that models exhibit strong spatial transfer but consistently fail under length scaling due to recursive instability. We further analyze how distinct stages of the learning pipeline influence systematic problem-solving: for example, data coverage sets capability limits; reinforcement learning improves training stability but does not expand those limits; and inference-time scaling enhances performance but cannot rescue length-scaling failures.

---


### 142. [MM-WebAgent: A Hierarchical Multimodal Web Agent for Webpage Generation](https://arxiv.org/abs/2604.15309)

**<font color=#1a73e8>作者：</font>** Yan Li, Zezi Zeng, Yifan Yang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid progress of Artificial Intelligence Generated Content (AIGC) tools enables images, videos, and visualizations to be created on demand for webpage design, offering a flexible and increasingly adopted paradigm for modern UI/UX. However, directly integrating such tools into automated webpage generation often leads to style inconsistency and poor global coherence, as elements are generated in isolation. We propose MM-WebAgent, a hierarchical agentic framework for multimodal webpage generation that coordinates AIGC-based element generation through hierarchical planning and iterative self-reflection. MM-WebAgent jointly optimizes global layout, local multimodal content, and their integration, producing coherent and visually consistent webpages. We further introduce a benchmark for multimodal webpage generation and a multi-level evaluation protocol for systematic assessment. Experiments demonstrate that MM-WebAgent outperforms code-generation and agent-based baselines, especially on multimodal element generation and integration. Code & Data: this https URL.

---


### 143. [LeapAlign: Post-Training Flow Matching Models at Any Generation Step by Building Two-Step Trajectories](https://arxiv.org/abs/2604.15311)

**<font color=#1a73e8>作者：</font>** Zhanhao Liang, Tao Yang, Jie Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper focuses on the alignment of flow matching models with human preferences. A promising way is fine-tuning by directly backpropagating reward gradients through the differentiable generation process of flow matching. However, backpropagating through long trajectories results in prohibitive memory costs and gradient explosion. Therefore, direct-gradient methods struggle to update early generation steps, which are crucial for determining the global structure of the final image. To address this issue, we introduce LeapAlign, a fine-tuning method that reduces computational cost and enables direct gradient propagation from reward to early generation steps. Specifically, we shorten the long trajectory into only two steps by designing two consecutive leaps, each skipping multiple ODE sampling steps and predicting future latents in a single step. By randomizing the start and end timesteps of the leaps, LeapAlign leads to efficient and stable model updates at any generation step. To better use such shortened trajectories, we assign higher training weights to those that are more consistent with the long generation path. To further enhance gradient stability, we reduce the weights of gradient terms with large magnitude, instead of completely removing them as done in previous works. When fine-tuning the Flux model, LeapAlign consistently outperforms state-of-the-art GRPO-based and direct-gradient methods across various metrics, achieving superior image quality and image-text alignment.

---


> [!TIP]
> 当前位于：**101-143**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-143**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
