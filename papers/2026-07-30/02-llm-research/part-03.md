# 🧠 大模型相关研究 | 2026年07月30日

> 本类共 **131** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-131**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-131**

---

### 101. [BioDisclose: An Actionability-Aware Benchmark for Biomedical Safety under Adversarial Elicitation](https://arxiv.org/abs/2607.25700)

**<font color=#1a73e8>作者：</font>** Yinuo Zhu, He Liu, Boyuan Gu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly support biomedical research, yet their behavior under adversarial requests for dual-use knowledge remains insufficiently characterized. We introduce BioDisclose, a benchmark for measuring biomedical knowledge disclosure under adversarial elicitation. BioDisclose contains 480 prompts derived from 24 expert-authored scenarios across six biomedical risk domains and four elicitation families spanning academic, historical, role-playing, and decomposed prompting. We grade model responses on a four-level scale from refusal to executable disclosure, distinguishing high-level discussion from technically specific and actionable content, including refuse-then-leak behavior. Across five deployed LLM systems, detailed-or-higher disclosure rates vary substantially, ranging from 9.2% to 64.0%. Academic framing is the most effective elicitation family on average (43.2%), while laboratory safety scenarios show the highest disclosure rate across domains (51.5%). These results reveal pronounced variation across models, prompting strategies, and biomedical risk categories, suggesting that current safeguards remain uneven in high-stakes scientific settings. BioDisclose provides a focused testbed for evaluating biomedical safety beyond binary refusal metrics.

---


### 102. [Impact Detection in Fall Events: Leveraging Spatio-Temporal Graph Convolutional Networks and Recurrent Neural Networks Using 3D Skeletons Data](https://arxiv.org/abs/2607.25710)

**<font color=#1a73e8>作者：</font>** Tresor Y. Koffi, Youssef Mourchid, Mohammed Hindawi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fall represents a significant risk of accidental death among individuals aged over 65, presenting a global health concern. A fall is defined as any event where a person loses balance and moves to an off-position, which may or may not result in an impact where the person hits the ground. While fall detection systems have achieved good results in general, impact detection within falls remains challenging. This study proposes an efficient methodology for accurately detecting impacts within fall events by incorporating 3D joints skeleton data treated as a graph using Spatio-Temporal Graph Convolutional Networks (STGCN), Gated Recurrent Unit (GRU), and Bidirectional Long Short-Term Memory (BiLSTM) layers. By pinpointing impact moments, our approach enhances precision by distinguishing between false falls and actual impacts, contributing to better healthcare resource allocation. Our methodology, evaluated using the improved 3D skeletons UP-Fall dataset, achieves accuracy exceeding 90\% across various fall scenarios. We have made this improved dataset publicly available at this https URL to facilitate further research.

---


### 103. [SpeechLLM Meets Federated Learning for End-to-End ASR: English and Italian Case Studies](https://arxiv.org/abs/2607.25716)

**<font color=#1a73e8>作者：</font>** Mohamed Nabih Ali, Daniele Falavigna, Alessio Brutti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables privacy-preserving training of automatic speech recognition (ASR) systems across distributed data sources, yet its application to large-scale speech language models (SpeechLLMs) remains unexplored. This paper presents the first systematic study of federated training for SpeechLLM-based end-to-end ASR systems. We design a communication-efficient federated optimization strategy tailored to the unique challenges of SpeechLLM architectures, addressing high-dimensional parameter spaces, gradient communication overhead, and computational constraints in distributed settings. Through extensive empirical evaluation on monolingual ASR tasks in English and Italian, we demonstrate the effectiveness and stability of our federated approach compared to centralized training baselines across diverse acoustic conditions and speaking styles. Additionally, we conduct a comprehensive ablation study analyzing the impact of different speech encoder architectures on monolingual English ASR performance within the federated framework, providing insights into optimal model configurations for decentralized training. Our results achieve competitive word error rates while reducing communication costs, establishing practical foundations for federated SpeechLLM deployment in real-world multilingual scenarios.

---


### 104. [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](https://arxiv.org/abs/2607.25718)

**<font color=#1a73e8>作者：</font>** Xinyi Hong, Pinjun Dong, Xinyang Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on invoking external tools to complete real-world tasks. Tool retrieval, which selects a small task-relevant subset from a library of thousands of tools before the agent acts, has therefore become a critical component of LLM agent pipelines. However, existing retrievers either score each tool in isolation or assemble the tool set sequentially, so the joint utility of a candidate set is never evaluated as a whole. In this paper, we propose HYSET, short for HYperedge-based SEt-level Tool retrieval. Our contributions are threefold: (i) we formulate tool retrieval as query-conditioned hyperedge prediction on a tool co-invocation hypergraph, under which the tool set itself becomes the unit of scoring and most existing retrieval paradigms reduce to restricted instances; (ii) we capture size-dependent tool compatibility through cardinality-specific interactions; and (iii) we design HYSET as a pre-selection module requiring no modification to the downstream agent. Experiments on ToolBench demonstrate that HYSET consistently outperforms state-of-the-art baselines in both tool retrieval performance and end-to-end task success. Beyond the in-domain setting, HYSET further supports zero-shot/few-shot transfer, generalizing to held-out tools/categories and unseen domains with minimal supervision.

---


### 105. [Nudging Sustainable Choices through LLM-Generated Recommendation Explanations](https://arxiv.org/abs/2607.25726)

**<font color=#1a73e8>作者：</font>** Haya Halimeh, Dietmar Jannach, Oliver Müller  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recommender systems mediate everyday consumption, offering a promising channel for encouraging sustainable choices. Prior research shows that explanations influence users' perceptions of recommendations and can support more informed decisions. We argue that explanations can also serve as behavioral nudges by foregrounding sustainability information at the moment of choice. This study investigates how different behavioral framings of sustainability information in recommendation explanations affect user choices and perceptions. Using generative AI, we generate sustainability-aware explanations by drawing on nudge theory and validate them through human evaluation and LLM-as-a-judge audits. Building on this foundation, we conduct two randomized studies ($N = 529$) in a low involvement domain (instant coffee) and a high involvement domain (hotel bookings), in which participants choose among preference matched recommendations accompanied by these explanations. Our results show that, across both domains, merely disclosing sustainability information in explanations does not change choices, whereas framing that information or invoking a descriptive social norm significantly increases sustainable selections and eases decision-making. Notably, perception and behavior diverge, as plain disclosure improves explanation evaluations without translating into more sustainable selection behavior. Our work demonstrates how LLMs can generate theory-grounded explanations at scale, pointing toward practical explanation-based interventions for social good. We conclude by discussing implications for adaptive explanation design with generative AI.

---


### 106. [Fine-Grained Food Image Understanding via Target-Aware Data Alignment](https://arxiv.org/abs/2607.25794)

**<font color=#1a73e8>作者：</font>** Jui-Feng Chi, Wei-Lun Chu, Bruce Coburn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained food visual--semantic understanding requires models to capture subtle distinctions across ingredients, cooking methods, doneness, color, texture, and plate composition. Although CLIP-style vision-language models provide a natural framework for this task, their effectiveness is limited when training relies on heterogeneous web-collected image--text pairs. Such data often exhibit a web-to-target domain gap and cross-modal misalignment, where images differ from the target distribution and captions are noisy, multilingual, or weakly grounded in visual content. We propose a data-centric multimodal alignment method for fine-grained food description and recognition. Our method first performs target-aware data selection to identify visually relevant training subsets, then applies VLM-based caption refinement to generate visually grounded, target-style descriptions. Using these curated image--caption pairs, we train complementary CLIP-style retrieval experts and further combine their decisions through a hierarchical VLM-assisted multi-expert decision-level fusion strategy that invokes the VLM only when experts disagree. Experiments show that our data refinement strategy significantly improves retrieval performance over naive web supervision, with VLM-based caption refinement alone yielding an average performance gain of approximately 19%. Our full method also achieves more than twice the retrieval score of pure VLM-based retrieval while remaining substantially more efficient.

---


### 107. [Evaluation of Adversarial Robustness in Arabic Language Models](https://arxiv.org/abs/2607.25814)

**<font color=#1a73e8>作者：</font>** Anwar Alajmi, Ayed Salman, Imtiaz Ahmad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The emergence of the recent outstanding capabilities of Arabic Language Models has opened doors for exposing their vulnerabilities. One of the major security risks associated with such Natural Language Processing models is adversarial attacks. These attacks can deceive the model into the wrong prediction, raising critical model security and safety concerns. This study aims to assess the robustness of five state-of-the-art Arabic Language Models under a distinct set of Arabic adversarial attacks applied at various levels of granularity and using different example generation strategies. We also explore a defense technique based on adversarial training to enhance model robustness. The results show that insertion of diacritics can reduce the accuracy of some models by 92% while maintaining a low perturbation distance. For word-level attacks, manipulating Arabic conjunctions preserves high semantic similarity scores, low perturbation distance, and leads to an accuracy degradation of up to 58%. For sentence-level attacks, paraphrasing proves its effectiveness by an average reduction of 76% in the victim models' performance. While adversarial training improves overall resilience, with MARBERT being the most robust and AraBERT showing the greatest relative gains, challenges persist, particularly against character-level noise. These findings highlight both the potential and limitations of current defense strategies in morphologically rich languages like Arabic.

---


### 108. [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL](https://arxiv.org/abs/2607.25816)

**<font color=#1a73e8>作者：</font>** Jiabao Ji, Yujian Liu, Li An 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model agents often spend substantial wall-clock time waiting for tool call results. Tool-call speculation can hide this latency by predicting and pre-executing an agent's next tool call if the prediction matches the agent's eventual tool call, but existing speculators are typically separate draft models or cached traces that are poorly aligned with the deployed agent's own behavior. We identify this speculator-agent gap and show that the target agent itself is a strong next-call speculator. This points to a simpler design: unifying the agent and speculator within the same model. In this paper, we introduce the self-speculating agent, a single model that both solves tasks in agent mode and predicts its next tool call from partial trajectories in speculator mode, fully reusing prefix KV cache. To enable this dual-mode agent without degrading performance, we propose a joint agent-speculator reinforcement learning method, which derives speculation targets from the agent's own rollouts and alternates agent and speculator updates. Across agentic search QA and conversational tool-use agentic tasks, our method improves average next tool-call Hit@1 from 44.1 to 61.2 for Qwen3-4B and from 48.9 to 66.3 for Qwen3.5-4B, while preserving agent task success.

---


### 109. [SepPrune:A Separator-based Pruning Framework for Efficient Multimodal Large Language Models](https://arxiv.org/abs/2607.25818)

**<font color=#1a73e8>作者：</font>** Yuchen Wang, Qihui Zhu, Yang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent multimodal large language models (MLLMs), such as Qwen2.5-VL and InternVL3, generate large numbers of vision tokens for high-resolution inputs, leading to substantial computational cost. Existing vision token pruning methods either depend on cross-modal attention and cannot prune before the prefill stage, or rely on diversity estimation with high computational overhead. We observe that attention scores from both vision and text tokens peak at modality separator tokens, suggesting that these separators bridge the two modalities. Based on this observation, we propose SepPrune, an efficient, training-free, plug-and-play pruning method that uses the separator token as a unified query to rank and select informative vision tokens. SepPrune reuses the LLM's built-in projection parameters and requires no architectural changes. Experiments on Qwen2.5-VL-7B show that SepPrune achieves state-of-the-art performance, retaining 96.3% of the original accuracy while removing 80.2% of vision tokens.

---


### 110. [Food Image Segmentation with LLM-Derived Ingredient Labels and Multimodal Fusion](https://arxiv.org/abs/2607.25820)

**<font color=#1a73e8>作者：</font>** Jui-Feng Chi, Wei-Ta Chu, Sheng-Long Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Food image segmentation plays a vital role in health-related applications such as nutrition tracking and personalized health monitoring. However, existing models often underperform on visually similar ingredients and rare food categories. To address this issue, we propose two plug-and-play multimodal modules that enhance the segmentation performance by leveraging ingredient labels inferred from food images using large language models (LLMs). The first module, called LIM-F (Language Injection Module for Features), is designed to pair with any image encoder that produces multi-layer outputs (e.g., Swin Transformer), while the second module, LIM-Q (Language Injection Module for Queries), targets Mask2Former-style Transformer-based decoders. Both modules enable training without the need for pre-aligning images with text by directly injecting semantic ingredient information into the visual analysis pipeline. On the FoodSeg103 benchmark, the proposed method achieves state-of-the-art performance. Specifically, integrating LIM-Q into the Mask2Former decoder with a Swin-L image encoder yields a mean Intersection over Union (mIoU) of 55.0. LIM-F also demonstrates strong generalization and competitive performance, reaching an mIoU of 54.4 under the same model (Swin-L+Mask2Former). Furthermore, its applicability extends beyond Transformer-based decoders, as evidenced by an improvement from 47.7 to 49.8 mIoU when integrated into a CNN-based architecture. Notably, the improved segmentation accuracy is achieved with only a moderate (at most 3.8 GB) increase in the GPU memory consumption during training. Thus, the proposed approach offers a practical and scalable solution for fine-grained food understanding.

---


### 111. [HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs](https://arxiv.org/abs/2607.25853)

**<font color=#1a73e8>作者：</font>** Yu Hao, Jinxuan Cai, Qi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skills have become an important abstraction for enabling large language model (LLM) agents to reuse past experience in long-horizon interactive tasks. However, existing trajectory-to-skill methods often produce flat collections of high-level textual skills that are stored and retrieved independently, leaving skill relations underutilized and maintaining a gap between high-level skills and executable actions. In this paper, we propose HiSkill, a hierarchical skill graph framework that organizes interaction trajectories into a directed graph with skill nodes, AtomicOp nodes, and typed edges. Specifically, the graph connects reusable high-level skills with executable action templates, while also capturing decomposition, temporal transition, compatibility, support, and recovery relations among them. At inference time, HiSkill retrieves a compact task-relevant subgraph and performs subgraph-guided task execution, where a symbolic task state, an active skill, and the retrieved subgraph guide the LLM agent to switch skills, select AtomicOps, and ground executable actions iteratively. Experiments on three interactive environments show that HiSkill outperforms state-of-the-art baselines while reducing inference token consumption, demonstrating the effectiveness of bridging high-level skills and executable action grounding through a hierarchical skill graph. Our data and code is available at this https URL.

---


### 112. [Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks](https://arxiv.org/abs/2607.25877)

**<font color=#1a73e8>作者：</font>** Bart Custers, Koorosh Aslansefat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper investigates how multi-agent systems (MAS)-based on large language models (LLMs) can support actuarial risk modelling, with a particular focus on uncertainty quantification. Actuarial workflows represent a high-stakes decision-support setting where unreliable outputs may lead to incorrect risk assessment, unfair pricing, and regulatory non-compliance. To address uncertainty introduced by the probabilistic nature of LLMs and dependencies between agents, a multi-agent framework is proposed in which specialised agents perform data preparation, modelling, review, and explanation tasks under a central hub. The main contribution is a novel approach to uncertainty propagation using token-level log-probabilities and a Bayesian Network. Importantly, log probabilities are not treated as direct probabilities of correctness or task success. Instead, length-normalised log-probability summaries are transformed into calibrated task-level confidence estimates before incorporation into the Bayesian Network. Results show that the framework reproduces baseline actuarial performance while providing additional insight into workflow stability and runtime uncertainty propagation.

---


### 113. [AI's Capability in Assisting Scientific Research in Physics, Astrophysics, and Cosmology II: Project Planning and Proposal Evaluation](https://arxiv.org/abs/2607.25881)

**<font color=#1a73e8>作者：</font>** Jia Liu, Veena Krishnaraj, Kateryna Vovk 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We investigate how well large language models (LLMs) can assist scientific project planning and proposal evaluation. One-page project plans were independently generated for eight expert-conceived research projects in physics, astrophysics, and cosmology by human researchers and three contemporary LLMs (ChatGPT, Claude, and DeepSeek; mid-2025 models, used with their default tool access). The resulting 32 proposals were blindly evaluated by four human reviewers and two newer frontier LLMs (Claude Opus 4.8 and ChatGPT Pro 5.5) using a four-aspect evaluation rubric. Reviewers were also asked to identify whether each proposal was written by a human or an AI. Human reviewers rated human- and AI-written proposals similarly overall, whereas both AI reviewers scored AI-written proposals about one point higher (on a five-point scale) than human-written proposals. Human reviewers correctly identified human- and AI-written proposals 72% and 79% of the time, respectively, while both AI reviewers correctly classified all 32 proposals (100%). These results suggest that current LLMs can produce project plans comparable to human-written ones in the eyes of human reviewers, but that AI reviewers show a systematic preference for AI-generated proposals. Our results suggest caution when deploying LLMs widely in proposal preparation and evaluation.

---


### 114. [Towards a Systems Foundation for Agentic Cloud Management](https://arxiv.org/abs/2607.25883)

**<font color=#1a73e8>作者：</font>** Minghao Li, Ziqian Liu, Ziyu Mao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Agentic cloud management is emerging as a practice to automate laborious operations, minimize toil, and improve responsiveness. Despite the rapid development of autonomous management agents, we argue that the fundamental missing piece is a systems foundation to enable safe, effective operations across agents and between agents and human operators. In this paper, we advocate for the need of such a systems foundation and share our efforts on developing CloudWeaver, an agentic management substrate that works across existing cloud-user interfaces and future agent-native interfaces. Specifically, we discuss how CloudWeaver (1) scopes the context of individual agent sessions with local views of cloud resources and (2) coordinates concurrent management operations on shared cloud resources. CloudWeaver offers strong safety guarantees and attributable feedback in the presence of conflicting intents, while preserving concurrency between independent operations. We validate CloudWeaver using a representative Azure API workload.

---


### 115. [Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents in Large Language Models](https://arxiv.org/abs/2607.25907)

**<font color=#1a73e8>作者：</font>** Deepanshu Mody, Samarth Agarwal, Utkarsh Mittal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering controls model behavior by editing internal activations at inference time. We study its input-side dual: optimizing a fluent prompt so that a chosen internal latent is driven toward zero, with no inference-time model access. Our target is an "evaluation-awareness" latent-linearly readable and steerable in recent work-whose control would threaten the validity of safety evaluations if models behave differently when they detect being tested. Adapting Fluent Dreaming / EPO with a negated feature term (GCG-style token optimization plus a self-cross-entropy fluency regularizer, swept over a fluency weight), we suppress the latent under five target constructions-a CAA direction, a subspace norm, an SAE feature, a single MLP neuron, and a behavioral logit-on Llama-3.2-3B and Llama-3.1-8B. The latent is robustly suppressible ($z\approx-7$), and a causally-validated Llama Scope SAE feature can be fully and selectively turned off. But our controls tell a cautionary story about the CAA direction: a placebo random direction is suppressed just as hard and shifts behavior just as far, and when we hold a real eval passage in context and optimize only a prefix, suppressing the eval-direction fails to reduce-and slightly increases-the model's behavioral eval judgment. Activation-readability, in short, is not behavioral controllability. We further find that a single MLP neuron is eval-correlated but not causal at both scales, and that scanning the real Pile yields a natural-text baseline competitive with the optimizer for the internal direction. A positive control validates our erasure detector, bounding an erasure-vs-rotation question earlier left open.

---


### 116. [Evaluating VLMs for Autonomous Agent-Driven Geometry Clipping Detection in Video Game QA](https://arxiv.org/abs/2607.25921)

**<font color=#1a73e8>作者：</font>** Carlos Celemin, Benedict Wilkins, Adrián Barahona-Ríos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we study the use of Vision-Language Models (VLMs) for anomaly detection in an agent-driven game Quality Assurance (QA) pipeline focusing on geometry clipping. In this evaluation, a custom exploration agent navigates a game level to collect visual observations, while the automatic annotation pipeline provides frame-level clipping labels. This setup allows us to evaluate recent VLMs on a controlled anomaly detection task without manual annotation. We benchmark six recent VLMs (Gemini, GPT, Qwen, Gemma, Llama, and Ministral) under a zero-shot prompting setting and analyse their sensitivity to four prompt variants.
Our results show that while the VLMs can capture visual cues associated with geometry clipping, they all produce substantial false positives on visually ambiguous frames such as near-contact geometry and partial occlusions. Gemini-3.1-Flash achieves the best overall accuracy and is the most robust to prompt variation, while open-source models exhibit large precision--recall swings depending on the prompt design. These findings suggest that current VLMs are best suited as high-recall candidate filters within multi-stage QA pipelines rather than as standalone bug detectors.

---


### 117. [Evaluating Multi-Turn Multimodal Diagnostic Reasoning on Challenging Real-World Clinical Cases](https://arxiv.org/abs/2607.25933)

**<font color=#1a73e8>作者：</font>** Rui Yang, Weihao Xuan, Yi Lin 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical diagnostic evaluation should not only assess whether models can provide correct diagnoses, but also reflect the realities of clinical practice, including progressive disclosure of multimodal information, dynamic updating of diagnostic hypotheses, and continuous refinement of clinical reasoning. However, existing evaluations of multimodal large language models (MLLMs) typically rely on single-turn or isolated tasks, making it difficult to fully capture the complexity of real-world clinical diagnosis. To bridge this gap, we developed ClinMM-Bench, the largest multi-turn multimodal clinical diagnostic evaluation benchmark to date. ClinMM-Bench contains 1,089 challenging real-world clinical cases and 3,760 medical images across eight specialties. We systematically evaluated 15 representative MLLMs using a two-level evaluation framework that assessed both diagnostic accuracy and diagnostic reasoning quality. Results showed that proprietary models achieved the highest overall diagnostic accuracy, but the proportion of completely correct diagnoses remained limited across all models. In terms of diagnostic reasoning quality, current models can identify plausible diagnostic directions but still have considerable limitations in generating reliable diagnostic reasoning. Error analysis further identified five representative failure modes: information synthesis failure, knowledge mapping error, perception error, premature closure, and visual hallucination.

---


### 118. [A Cost-Effective Multimodal LLM Reasoning Framework for Question Answering over Irregular Clinical Time Series](https://arxiv.org/abs/2607.25947)

**<font color=#1a73e8>作者：</font>** Frank Nie, Ethan B Liu, Yuan Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Question answering (QA) over irregular clinical time series (ICTS) plays a pivotal role in a wide range of healthcare applications. Although recent multimodal time-series large language models (LLMs) have shown considerable promise in general-purpose time-series QA, they remain poorly equipped to model the sparsity, asynchrony, and irregular sampling patterns of clinical observations. To fill this gap, we propose ClinPRISM, a cost-effective multimodal LLM reasoning framework for question answering over ICTS data. First, we devise an irregularity-aware multi-scale encoder to capture sparse clinical evidence at diverse temporal scales. Then, we propose a temporal evidence distiller to integrate representations across these scales and compress them into a small number of LLM-compatible tokens. Moreover, we introduce a progressive alignment strategy that sequentially aligns the irregular trajectories with the LLM's textual embedding space. To facilitate training, we construct 30,000 clinical time series paired with multi-scale descriptions, together with 41,000 instruction-tuning instances spanning 11 tasks. Using a 4-billion-parameter LLM backbone, ClinPRISM achieves state-of-the-art performance on the held-out evaluation benchmark while using only 16 time-series tokens and achieving an average inference latency of 0.15 seconds per question.

---


### 119. [Polistemics: Evaluating LLMs as Information Mediators in Politics & Elections](https://arxiv.org/abs/2607.25953)

**<font color=#1a73e8>作者：</font>** Baran Peters  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As LLMs increasingly mediate the political information citizens rely on, there is still no standardized way to assess whether they do so responsibly. We introduce Polistemics, a theory-grounded benchmark for evaluating LLMs as mediators of political information in elections. Prior work has treated this task as reproduction rather than mediation, leaving its epistemic dimensions and interaction with imperfect information unaddressed. We ground the evaluation in Epistemic Modesty, a normative standard derived from citizens' epistemic agency, and test it across controlled settings that vary informational properties such as clarity, noise, and consistency. Applying the benchmark to three state-of-the-art LLMs on the 2025 German and Dutch elections, we find that high aggregate scores mask systematic failures. Models mediate reliably under clear evidence but break down under absent, vague, or contradictory information, while flattening the intensity of political language. These failures are likely driven by party priors, influenced by party labels and output language. Reliable mediation appears achievable, but no model delivers it consistently.

---


### 120. [Large Language Model for Operations Research Formulation Selection in Multi-Warehouse Inventory Allocation](https://arxiv.org/abs/2607.25956)

**<font color=#1a73e8>作者：</font>** Jintao Xu, Yingzheng Ma, Jiong Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-warehouse inventory allocation is typically formulated as a mixed-integer programming (MIP) problem, yet no single formulation consistently matches heterogeneous instance-level regimes induced by demand concentration, inventory imbalance, replenishment scale, service constraints, and forecast volatility. We study this issue as instance-wise operations research (OR) formulation selection, where each allocation instance is assigned to a solver-executable formulation from a candidate OR expert library. We propose a solver-guided large language model (LLM) framework for OR formulation selection, in which each OR expert corresponds to a MIP formulation encoding a distinct allocation priority. To train the selector, the framework first constructs balanced expert-conditioned supervised fine-tuning (SFT) records for schema learning, and then uses MIP solver evaluation on historical instances to convert solver-evaluated allocation-quality gaps into margin-weighted identity preference optimization (IPO) preferences and per-instance expert-score metadata for reward lookup during group relative policy optimization (GRPO) to assign rewards to sampled responses. Experiments on multi-warehouse inventory allocation instances from JD$\mathord{.}$com, one of China's largest e-retailers, demonstrate that GRPO substantially improves expert-selection accuracy relative to the SFT+IPO selector and, more importantly, produces higher realized allocation quality than both the preference-trained selector and the best fixed formulation. With GRPO, Hit Ratio@1 and Hit Ratio@2 increase from 21.45% to 50.42% and from 70.47% to 82.31%. The resulting selector achieves an allocation accuracy gain of 12.57 percentage points over the incumbent baseline, outperforming both the SFT+IPO selector and the best fixed OR expert, and reduces the gap to the ex-post oracle to 4.85 percentage points.

---


### 121. [Knowledge-Guided Multimodal Reasoning over Interacting Streams for Video-Level Ambivalence and Hesitancy Recognition](https://arxiv.org/abs/2607.25961)

**<font color=#1a73e8>作者：</font>** Podakanti Satyajith Chary, Barath Parthiban, Pranesh Velmurugan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ambivalence and hesitancy (A/H) are conflicting affective states that precede the delay or abandonment of health behaviour change. Recognition of A/H at the video level is difficult, since the signal arises from disagreement across and within facial, vocal, linguistic, and bodily modalities, and manifests differently across individuals. The proposed PRISM-AH (Predictive Reasoning over Interacting Streams for Multimodal Ambivalence/Hesitancy Recognition), is a framework that treats A/H as a multimodal conflict that unfolds over time. Frozen vision, audio, and text encoders are aligned into short time windows and passed to a lightweight streaming model that scores cross-modal dissonance, predicts each next window to expose a hesitation surprise signal, discovers behaviour prototypes, and is conditioned on participant metadata. Dense window-level annotations supervise the model as an auxiliary objective, and the decision threshold is calibrated for macro F1. A knowledge-guided large language model then reasons over structured evidence using the expert cue taxonomy of the dataset, and its verdict is fused late only when validation performance improves. On the labelled public test partition of 525 videos, PRISM-AH attains a macro F1 of 0.6133, compared to the reported zero-shot baseline of 0.2827. The reasoning gain is validated to transfer from validation to the larger test partition.

---


### 122. [LaP-Forensics: Latent-Pixel Consistency Guided Multimodal Reasoning for Deepfake Detection](https://arxiv.org/abs/2607.25962)

**<font color=#1a73e8>作者：</font>** Can Wang, Yuhao Wang, Yushe Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent generative models can produce images with few obvious visual artifacts, weakening detectors and explanations that rely only on surface appearance. We present LaP-Forensics, a multimodal framework that augments RGB semantics with reconstruction-based forensic evidence. A frozen Stable Diffusion DDIM inversion-reconstruction model provides a fixed reconstruction reference, and its residual map measures local compatibility with that reference. Independent projectors encode the RGB image and residual map before a structured Where-What-Why model predicts a textual analysis and an artifact this http URL fine-tuning is followed by Group Relative Policy Optimization (GRPO), whose reward combines mask overlap with output-structure and evidence-reference terms. These text-side terms encourage the model to refer to the consistency map but do not constitute a verifier of free-form textual truth. A separate image-level head fuses RGB and DDIM-residual class features. Experiments show cross-generator detection on UniversalFakeDetect and competitive artifact localization on the official SynthScars benchmark. Controlled cue-construction, inversion-horizon, component, reward-term, and counterfactual analyses support the utility of the residual stream under the evaluated settings, while free-form textual faithfulness and reliability under post-processing remain open limitations.

---


### 123. [Beyond Zooming: Learning Multi-Tool Visual Reasoning for Ultra-High-Resolution Remote Sensing](https://arxiv.org/abs/2607.25993)

**<font color=#1a73e8>作者：</font>** Fengxiang Wang, Jiangnan Huang, Mingshuo Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-high-resolution (UHR) remote-sensing (RS) imagery provides fine-grained Earth-observation evidence over city-scale scenes, but poses a fundamental challenge for multimodal large language models (MLLMs): task-relevant evidence is often sparse, local, and spatially dispersed across extremely large visual contexts. A natural solution is to equip MLLMs with zoom-in tools for active local inspection. However, through a pilot study on XLRS-Bench, we find that zoom-in is only partially effective: it resolves easy and medium-level tasks with locally recoverable evidence, but saturates on hard cases requiring global search, multi-region comparison, path planning, or dispersed-evidence reasoning. Motivated by this finding, we move beyond single-tool zoom-in and introduce GeoMTVR, a large-scale Geospatial Multi-Tool Visual Reasoning dataset built from wide-area satellite imagery. GeoMTVR contains 13K UHR VQA samples with interleaved reasoning trajectories, diverse visual tool calls, and returned visual observations, enabling models to learn question decomposition, tool selection, regional inspection, object-level grounding, auxiliary visual reasoning, and cross-tool evidence integration. Beyond supervised fine-tuning, we propose a tool-attention-focused reinforcement learning algorithm that concentrates optimization on critical tool-use decisions, including when to invoke tools, which tool to select, where to apply it, and how to interpret tool outputs. By combining SFT on GeoMTVR with our RL algorithm, we develop GeoLens, a multi-tool visual reasoning MLLM for UHR RS. Experiments show that GeoLens consistently outperforms direct reasoning and single-tool zoom-in baselines, achieving stronger accuracy, better evidence grounding, and more efficient tool-use trajectories.

---


### 124. [Empirical Evaluation of Out-Of-Distribution Performance of Tabular Foundation Models](https://arxiv.org/abs/2607.26000)

**<font color=#1a73e8>作者：</font>** Malena Loza, David Chushig-Muzo, Eva Milara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular Foundation Models (TFMs) have emerged as novel approaches for tabular predictive tasks, demonstrating competitive predictive performance to ensemble tree-based models. Most TFMs are trained and evaluated on independent and identically distributed data, but this assumption changes in real-world scenarios due to distribution shifts, which compromise the robustness of models. Limited research has been conducted of TFMs under distribution shifts. We present an empirical evaluation of Out-Of-Distribution (OOD) performance of nine TFMs, spanning diverse pre-training strategies and architectures: TabPFNv2, TabPFNv2.5, TabPFNv2.6, TabPFNv3, TabICL, TabICLv2, Mitra, LimiX and TabFM. Three real-world datasets from the TableShift study were considered (HELOC, Voting, Childhood Lead), covering label, socioeconomic, and geographic shift types. Our results show that all evaluated TFMs degrade systematically under distribution shift regardless of pre-training strategy, with shift gaps ranging from 0.003 to 0.060 depending on shift type. The relationship between in-distribution and OOD predictive performance documented for classical tabular models extends into TFMs. We also identified a scalability gap, as high-performing models demand significant memory and computational resources beyond what standard deployment infrastructure can support. This study extends existing benchmarks for OOD in tabular data, providing evidence to support their adoption in high-stakes domains characterized by structural distribution shifts.

---


### 125. [Instruction-Tuned Models Locally Reuse Human Syntax More Than Humans Do](https://arxiv.org/abs/2607.26015)

**<font color=#1a73e8>作者：</font>** Zandi Eberstadt  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Syntactic convergence (the tendency of speakers to adapt in language towards the grammatical profiles of their interlocutors) is a well-documented feature of human dialogue widely considered to operate below conscious awareness. Whether large language models exhibit analogous syntactic convergence toward human users relative to human baselines and across a broad range of syntactic constructions remains an open question. Using substitution-paradigm data in which model generations replace one speaker's turns in pre-existing human dialogues, this study measures turn-adjacent reuse of context-free grammar (CFG) rules across sixteen open-weight Llama and Gemma models (1B-70B, pretrained and instruction-tuned) at 1,901 matched positions per model. Every model showed greater CFG-rule overlap with the preceding human turn than with a sampled unrelated human prime, and in every model this actual-versus-random difference was larger for lower-frequency rules. Each instruction-tuned model also showed greater natural-output overlap with the actual prime than the human response it replaced, and all eight matched architecture pairs exhibited greater actual-prime overlap after instruction tuning. However, relative to pretrained variants, instruction-tuned outputs overlapped more with unrelated primes, showed a smaller actual-versus-random increment, and had lower conditional rule-reuse odds once target rule-set size was held constant. In exploratory analyses, each model exhibited greater mean lexical and semantic similarity to the preceding turn than the matched human responses did. Instruction-tuned models additionally produced responses with greater mean semantic similarity than their pretrained counterparts in all eight architecture pairs, whereas the lexical similarity results were more heterogeneous.

---


### 126. [CHARM: A Multimodal Graph Foundation Model with Hierarchical Context Modeling for Zero-Shot Transfer](https://arxiv.org/abs/2607.26023)

**<font color=#1a73e8>作者：</font>** Ankang Yang, Jitao Zhao, Di Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph foundation models (GFMs) have emerged as a promising paradigm for transferring knowledge across graph domains and tasks. Real-world graphs associate nodes with text, images, and other modalities, making multimodal graphs essential for representing complex entities and relations. Moreover, collecting labels and adapting models for every new graph domain is costly and often infeasible, motivating zero-shot transfer. Unfortunately, zero-shot transfer on multimodal graphs remains underexplored. Existing GNN-based graph foundation models typically require downstream adaptation, whereas LLM-based graph methods mainly address unimodal graphs or tasks within a single domain. This setting presents two key challenges. First, models must generalize knowledge from individual modalities while capturing transferable cross-modal relations. Second, without target-domain fine-tuning, node representations remain entangled with domain-specific structures and modality-specific characteristics, obscuring shared concepts in unseen domains. To address these challenges, we propose CHARM, a multimodal graph foundation model with hierarchical context modeling for zero-shot transfer. CHARM replaces isolated raw nodes with hierarchical graph contexts that capture multimodal semantics and cross-modal relations. These contexts map domain-specific node patterns to shared high-level concepts, reducing reliance on target-domain supervision or adaptation. A modality-aware graph context encoder integrates multimodal information with graph structure and converts the resulting representations into graph tokens for a large language model . Experiments show consistent improvements on zero-shot multimodal graph tasks.

---


### 127. [LLM4OSC: Profile-Bound Natural Language Control with Deterministic Validation for Open Sound Control](https://arxiv.org/abs/2607.26024)

**<font color=#1a73e8>作者：</font>** Yuan-Yi Fan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Open Sound Control (OSC) is the dominant wire protocol for real-time parametric control in professional audio, live performance, and virtual production. Large language models can emit plausible OSC, but they hallucinate addresses, mishandle type tags, and fail under paraphrase- unacceptable in show-critical contexts. We present LLM4OSC, a local-first architecture in which models propose structured intent JSON over a human-reviewed device profile, and deterministic code validates, clamps, and encodes before any UDP send. We introduce a frozen evaluation harness with CI gates on wrong-send rate: mismatches that would still pass validation and transmit. On a Max/MSP hero profile (12 patterns; 8 literal + 8 paraphrase + 4 refusal cases), after profile tag enrichment, symbolic slot fill, NL refine, and a retrieval confidence gate, backends B0--B3 all pass frozen gates (100% semantic accuracy, 0% wrong-send). B0 (rules) remains the production default at ~0.05ms; LLM backends remain ~3-4s. Historical few-shot B2 accuracy of 62.5% rises to 100% on this suite only after symbolic post-processing- not because the 0.5B model alone becomes show-safe. We argue for propose-validate-send and wrong-send rate as first-class metrics for language-to-control systems.

---


### 128. [Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037)

**<font color=#1a73e8>作者：</font>** Jiacong Xu, Hanwen Jiang, Zhixin Shu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration. Given an image or a conditional video, Wonder constructs a playable world where users can navigate interactively by moving the camera, discovering unseen regions, and revisiting previously observed areas in real time and over a long-term horizon. Achieving this capability requires a system-level co-design of control method, memory mechanism, and training strategy. We introduce a novel camera conditioning with a dense coordinate field whose renderings provide spatially aligned motion and orientation cues, allowing the model to interpret camera motion directly as visual evidence. To support fast and precise memory retrieval over a growing generation context, we propose an efficient sparse attention-based memory mechanism, enabling the model to selectively attend to a small set of relevant context tokens at inference time, regardless of actual context length. We further develop several techniques to rectify the self-forcing-style distillation pipeline, improving the student model's ability to respect control signals, as well as maintaining diverse generation modes and long-term memory from the teacher. Together, these components enable Wonder to synthesize diverse, minute-scale videos at 16 FPS while preserving coherent geometry, appearance, and dynamics across long rollouts. Beyond image-to-video generation, Wonder naturally supports video-conditioned generation, allowing existing dynamic scenes to be re-shot in real time.

---


### 129. [Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance](https://arxiv.org/abs/2607.26040)

**<font color=#1a73e8>作者：</font>** Gaspard Lambrechts, Adrien Bolland, Daniel Ebi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards. Leveraging additional information during training to learn better representations and behaviors has been the focus of asymmetric reinforcement learning. This learning paradigm has proven effective under partial observability when additional state information is available, but also under full observability when more refined state information is available. Focusing on model-based reinforcement learning, we study the effect of asymmetric learning on observation representations and on privileged information representations. First, we identify a limitation in the privileged information representations learned by an asymmetric model-based algorithm known as the Informed Dreamer. Then, we propose a novel asymmetric representation learning objective using latent guidance, resulting in a new algorithm called the Reinformed Dreamer. Experiments across several benchmarks show a more consistent improvement over Dreamer than previous asymmetric approaches.

---


### 130. [VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening](https://arxiv.org/abs/2607.26042)

**<font color=#1a73e8>作者：</font>** Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present VetClaw, an edge-cloud multimodal agentic system for early veterinary disease screening. VetClaw uses a camera module as an edge sensing device and sends captured images, together with optional symptom descriptions, to a server-hosted vision-language model for zero-shot disease classification. The system separates agent interaction from workflow orchestration: OpenClaw provides scheduling, tool access, user interaction, and notification services on the edge device, while LangGraph manages the stateful screening workflow, including input validation, image transmission, model invocation, safety checks, conditional routing, failure handling, and structured logging. This design moves beyond static image classification by enabling the system to collect visual evidence, invoke external models, apply deterministic safety rules, and generate diagnostic-support alerts. Results show that image-only VLM prediction remains limited, whereas symptom-guided and multimodal inputs improve zero-shot classification performance. Thus, VetClaw transforms a static prediction model into a coordinated, safety-aware system that can use tools, manage workflows, handle failures, and escalate uncertain cases.

---


### 131. [Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA](https://arxiv.org/abs/2607.26052)

**<font color=#1a73e8>作者：</font>** Tom Saliencro, Rohan Desai, Priya Nair 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) variants of Low-Rank Adaptation (LoRA) route every token to a fixed number of experts $k$. Tokens differ in how uncertain the model is about them, so a single k over-spends on easy tokens and under-serves hard ones. We observe that the router's output distribution is already a per-token uncertainty signal: peaked mass indicates confidence, while a flat distribution indicates ambiguity. We introduce CARE (Confidence-Adaptive Routing of Experts), which admits experts in a nucleus fashion. Experts are activated in decreasing router weight until their cumulative mass reaches a threshold, with a small extension when the admitted experts disagree. A budget thermostat calibrates the threshold so that the average number of active experts matches any target. CARE is a drop-in, single-forward-pass rule with no extra parameters. Across eight commonsense benchmarks on LLaMA-3.1-8B and Qwen2.5-7B, as well as math, code, and knowledge tasks, CARE improves over fixed top-k MoE-LoRA at matched compute and matches the fixed-k=4 baseline while activating fewer experts. The same confidence and disagreement signals also improve out-of-distribution detection over MSP, entropy, and multi-pass proxies. We support the design with nucleus fidelity, budget optimality, and an epistemic reading of disagreement, and we release code.

---


> [!TIP]
> 当前位于：**101-131**（第 3/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-131**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
