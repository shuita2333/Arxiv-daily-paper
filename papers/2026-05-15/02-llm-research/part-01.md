# 🧠 大模型相关研究 | 2026年05月15日

> 本类共 **159** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-159](./part-04.md)

---

### 1. [Mitigating Cross-Lingual Cultural Inconsistencies in LLMs via Consensus-Driven Preference Optimisation](https://arxiv.org/abs/2605.12515)

**<font color=#1a73e8>作者：</font>** Lucas Resck, Isabelle Augenstein, Anna Korhonen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Despite their impressive capabilities, multilingual large language models (MLLMs) frequently exhibit inconsistent behaviour when the prompt's language changes. While such adaptation is generally desirable, it becomes a critical failure when a user's identity is explicitly defined. For instance, given a fixed British persona and an ambiguous everyday knowledge query about literature, the prompt's language frequently overwrites the system persona -- yielding Shakespeare in English but Cervantes in Spanish. To robustly quantify this Cross-lingual Cultural Inconsistency, we introduce Singleton Fleiss's $\kappa_S$, a metric mathematically resilient to hallucinations. For mitigation, we propose Cross-lingual Cultural Consistent Preference Optimisation (C-3PO), a consensus-driven alignment framework. C-3PO achieves up to a 0.10-point absolute increase in $\kappa_S$ over unaligned models, outperforming strong prompting and representation steering baselines. Empirical evaluations show this inconsistency disproportionately affects lower-resource languages like Indonesian and Persian. A layer-wise interpretability analysis reveals the underlying mechanism: by early-decoding intermediate layer representations, we find that MLLMs implicitly personalise outputs towards the prompt language's stereotypical culture as forward-pass representations stabilise.

---


### 2. [Domain Adaptation of Large Language Models for Polymer-Composite Additive Manufacturing Using Retrieval-Augmented Generation and Fine-Tuning](https://arxiv.org/abs/2605.12516)

**<font color=#1a73e8>作者：</font>** Saiful Islam Sagor, Tania Haghighi, Minhaj Nur Alam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> General-purpose large language models (LLMs) often struggle to generate reliable responses in specialized engineering domains due to limited domain grounding and insufficient exposure to structured technical knowledge. This study investigates practical strategies for adapting a foundation LLM to the additive manufacturing (AM) domain in order to improve answer accuracy, relevance, and usability for expert-level question answering. AM knowledge is distributed across heterogeneous sources such as academic literature, manufacturer documentation, technical standards, and procedural guides. Although general LLMs demonstrate strong linguistic capabilities, they frequently fail to retrieve and contextualize such domain-specific information. Two common approaches to address this limitation are domain-specific fine-tuning and retrieval-augmented generation (RAG). We construct a curated AM corpus and evaluate three configurations based on LLaMA-3-8B: (1) the pretrained baseline model, (2) a RAG system that retrieves relevant document chunks from a vector database, and (3) a model fine-tuned on raw domain text. Performance is evaluated using 200 expert-designed AM questions assessed by mechanical engineering experts for accuracy, relevance, and overall preference. Results show that the RAG model consistently outperforms the baseline. Among the 200 questions, 75.5% of RAG responses are judged more accurate, 85.2% are preferred overall, and 90.8% are rated more relevant than baseline responses. In contrast, fine-tuning on raw AM text reduces performance, producing more accurate answers in only 5.6% of cases and more relevant answers in 32.5% of cases. These results indicate that retrieval-augmented approaches provide a more effective pathway for adapting LLMs to specialized engineering domains than naive fine-tuning on unstructured technical data.

---


### 3. [Bridging the Missing-Modality Gap: Improving Text-Only Calibration of Vision Language Models](https://arxiv.org/abs/2605.12517)

**<font color=#1a73e8>作者：</font>** Mingyeong Kim, Jungwon Choi, Chaeyun Jang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are often deployed on text-only inputs, although they are trained with images. We find that removing the vision modality causes large drops in accuracy and severe miscalibration, and the model does not behave like its original language backbone under text-only prompting. This failure is not explained only by missing semantic information. Even when text descriptions preserve key content, confidence becomes unreliable, while adding a visual signal through generated images partially restores accuracy and calibration. We propose the Latent Imagination Module (LIM), a lightweight cross-attention module that predicts imagined latent embeddings from textual input and feeds them into a frozen VLM backbone without pixel-level image synthesis. Across text-only benchmarks, unseen tasks, and missing-image scenarios, LIM improves accuracy and reduces calibration error. These results suggest that latent modality completion is a practical approach for reliable VLM inference under missing-modality.

---


### 4. [TimelineReasoner: Advancing Timeline Summarization with Large Reasoning Models](https://arxiv.org/abs/2605.12518)

**<font color=#1a73e8>作者：</font>** Liancheng Zhang, Xiaoxi Li, Zhicheng Dou  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The proliferation of online news poses a challenge to extracting structured timelines from unstructured content. While recent studies have shown that Large Language Models (LLMs) can assist Timeline Summarization (TLS), these approaches primarily treat models as passive generators. The emergence of Large Reasoning Models (LRMs) presents an opportunity to reason over events actively, enabling iterative evidence acquisition, the detection of missing events, and the validation of temporal consistency. To systematically leverage the reasoning capabilities of LRMs, we propose TimelineReasoner, a novel framework that shifts TLS from static generation to an active, reasoning-driven process. Unlike prior work, TimelineReasoner adopts a two-stage framework: Global Cognition, which tracks events at a macroscopic level and continuously updates a global event memory, and Detail Exploration, which identifies informational gaps and refines the timeline via targeted document retrieval. To support this, TimelineReasoner incorporates several specialized mechanisms, including an Event Scraper for retrieving temporal event descriptions, a Timeline Updater for refining the timeline, and a Supervisor for detecting gaps in the timeline and guiding retrieval. Experimental results on open-domain TLS datasets demonstrate that TimelineReasoner significantly outperforms existing LLM-based TLS methods in terms of timeline accuracy, coverage, and coherence. On closed-domain TLS datasets, our method performs on par with or exceeds state-of-the-art approaches. This work not only pushes the boundaries of TLS but also highlights the broader potential of LRM-based reasoning frameworks for timeline summarization.

---


### 5. [Correct Answers from Sound Reasoning: Verifiable Process Supervision for Language Models](https://arxiv.org/abs/2605.12519)

**<font color=#1a73e8>作者：</font>** Kyuyoung Kim, Kevin Wang, Yunfei Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training language models to produce both correct answers and sound reasoning remains an open challenge. Reinforcement learning with verifiable rewards typically optimizes only final outcomes, which can lead to a failure mode where task accuracy improves while reasoning becomes less accurate, less complete, or even internally inconsistent. We propose verifiable process supervision (VPS), a post-training framework for verifiable domains that jointly optimizes prediction accuracy and reasoning quality. We first apply supervised fine-tuning to induce a structured reasoning format, enabling syntactic extraction of intermediate claims that are evaluated against ground-truth signals to form process-level rewards. To address the heterogeneous difficulty of reasoning subtasks, we introduce adaptive reward weighting that prioritizes components with the largest remaining errors, creating an implicit curriculum. We evaluate VPS on chess, a controlled testbed where reasoning steps can be deterministically verified against engine signals. While accuracy-only RL improves move accuracy, it sharply degrades reasoning quality, increasing win-rate error by up to 112% and reducing internal consistency by up to 69%. In contrast, VPS preserves accuracy while significantly improving reasoning quality, reducing win-rate error by up to 30% and restoring consistency to near saturation. At matched accuracy, judge evaluation also prefers the process-supervised models. A reasoning-space analysis further shows that, without a structured prior, accuracy-only RL converges to budget-dependent shortcuts rather than sound multi-step reasoning. These results show that VPS enables language models to reason both accurately and reliably in verifiable domains.

---


### 6. [BoostTaxo: Zero-Shot Taxonomy Induction via Boosting-Style Agentic Reasoning and Constraint-Aware Calibration](https://arxiv.org/abs/2605.12520)

**<font color=#1a73e8>作者：</font>** Yancheng Ling, Zhenlin Qin, Leizhen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Taxonomy induction is crucial for organizing concepts into explicit and interpretable semantic hierarchies. While existing methods have achieved promising results, their generalization, structural reliability, and efficiency remain limited, hindering their performance in zero-shot and large-scale scenarios. To overcome these limitations, we introduce BoostTaxo, a boosting-style LLM framework for zero-shot taxonomy induction. It takes a set of domain terms as inputs and performs parent identification in a coarse-to-fine manner, employing retrieval-augmented definition refinement, hybrid parent candidate selection, candidate rating, and structure-aware score calibration to improve taxonomy construction. Specifically, a lightweight LLM is used to efficiently filter candidate parents, while a large-scale LLM is employed to rank and score candidate parents for fine-grained parent selection. Structural features are further incorporated to calibrate candidate edge weights and enhance the reliability of the induced taxonomy. The unified BoostTaxo is evaluated on three public benchmark datasets, namely WordNet, DBLP, and SemEval-Sci, and achieves superior or comparable performance to state-of-the-art methods in zero-shot taxonomy induction. The ablation study validates the contribution of the hybrid parent candidate selection and the structure-aware score calibration to the overall performance. Further analysis investigates the impact of candidate selection size on taxonomy quality and presents representative case and failure studies, providing deeper insights into the effectiveness and limitations of the proposed framework.

---


### 7. [ToolWeave: Structured Synthesis of Complex Multi-Turn Tool-Calling Dialogues](https://arxiv.org/abs/2605.12521)

**<font color=#1a73e8>作者：</font>** Dinesh Khandelwal, Gnana Prakash Punnavajhala, GPS Bhargav 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-turn tool calling is essential for LLMs to function as autonomous agents, yet synthesizing the training data required for these capabilities remains a fundamental challenge. Existing synthetic data generation pipelines often produce unrealistic dialogues for two reasons: they chain tools that are only superficially compatible rather than aligned with meaningful user tasks, and they generate dialogues in one shot, which often introduces arguments that were neither provided by the user nor produced by prior tool calls. These issues also lead to a severe underrepresentation of multi-step tool interactions. We introduce ToolWeave, a structured framework for synthesizing realistic multi-turn tool-calling dialogues. ToolWeave support realistic multi-step workflows (or tool sequences) by constructing tools with built-in dependencies and filters the workflows based on alignment with user goals. It reduces parameter hallucination by using a fine-grained planning stage that explicitly tracks parameter provenance. As a result, ToolWeave-generated synthetic dialogues contain more multi-step tool interactions (45%) and fewer hallucinations in parameters and tool names. Consequently, LLMs fine-tuned on ToolWeave consistently outperform those fine-tuned on prior datasets across three public benchmarks. Notably, Llama-3.1-70B fine-tuned on ToolWeave achieves 39.75% on BFCL-V3 multi-turn, compared to 23.50% when fine-tuned on SOTA ToolFlow data.

---


### 8. [Differences in Text Generated by Diffusion and Autoregressive Language Models](https://arxiv.org/abs/2605.12522)

**<font color=#1a73e8>作者：</font>** Zeyang Zhang, Chengwei Liang, Xingyan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) are promising alternatives to autoregressive language models (ARMs), yet the intrinsic differences in their generated text remain underexplored. We first find empirically that off-the-shelf DLMs exhibit lower $n$-gram entropy, higher semantic coherence, and higher semantic diversity. To understand the cause, we conduct controlled experiments that decouple the effects of training objectives and decoding algorithms. Results suggest that the DLM training objective contributes to the increases in semantic coherence and semantic diversity, but has a minor influence on entropy. These differences are primarily driven by the bidirectional context; other components in the training objective, such as input masking, label masking, and the weighting function, have a much weaker influence. Further, our experiments demonstrate that the reduction in entropy stems from DLMs' decoding algorithms, particularly confidence-based remasking strategies. We provide a theoretical understanding for this entropy reduction phenomenon. Together, our work uncovers key mechanisms underlying the differences between DLMs and ARMs in text generation, and informs future design of training objectives and decoding algorithms in DLMs.

---


### 9. [In-Situ Behavioral Evaluation for LLM Fairness, Not Standardized-Test Scores](https://arxiv.org/abs/2605.12530)

**<font color=#1a73e8>作者：</font>** Zeyu Tang, Sang T. Truong, Deonna Owens 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM fairness should be evaluated through in-situ conversational behavior rather than standardized-test Q&A benchmarks. We show that the standardized-test paradigm can be structurally unreliable: surface-level prompt construction choices, although entirely orthogonal to the fairness question being tested, account for the majority of score variance, shift fairness conclusions in both the direction and the magnitude, and result in severe discordance in model rankings. We develop MAC-Fairness, a multi-agent conversational framework that embeds controlled variation factors into multi-round dialogue for in-situ behavior evaluation, examining how models' conversational behavior shifts when identity is varied as part of natural multi-agent interaction. Repurposing standardized-test questions as conversation seeds rather than as the evaluation instrument, we evaluate position persistence (how they hold positions, from the self-perspective) and peer receptiveness (how receptive they are to peers, from the other-perspective) across 8 million conversation transcripts spanning multiple models and identity presence configurations. In-situ behavioral evaluation reveals stable, model-specific behavioral signatures that could generalize across benchmarks differing in fairness targets and evaluation methodologies, a form of evidence the standardized-test paradigm does not offer.

---


### 10. [VideoSEAL: Mitigating Evidence Misalignment in Agentic Long Video Understanding by Decoupling Answer Authority](https://arxiv.org/abs/2605.12571)

**<font color=#1a73e8>作者：</font>** Chenhao Qiu, Yechao Zhang, Xin Luo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long video question answering requires locating sparse, time-scattered visual evidence within highly redundant content. Although current MLLMs perform well on short videos, long videos introduce long-horizon search and verification, which often necessitates multi-turn, agentic interaction. We show that existing LVU agents can exhibit "evidence misalignment": they produce correct answers that are not supported by the retrieved or inspected evidence. To characterize this failure, we introduce two diagnostics (temporal groundedness and semantic groundedness) and use them to reveal two pressures that amplify misalignment: prompt pressure from shared-context saturation at inference time and reward pressure from outcome-only optimization during training. These findings point to a structural root cause: the coupled agent paradigm conflates long-horizon planning with answer authority. We therefore propose the decoupled planner-inspector framework, which separates planning from answer authority and gates final answering on pixel-level verification. Across four long-video benchmarks, our framework improves both answer accuracy and evidence alignment, achieving 55.1% on LVBench and 62.0% on LongVideoBench while producing interpretable search trajectories. Moreover, the decoupled architecture scales consistently with increased search budgets and supports plug-and-play upgrades of the MLLM backbone without retraining the planner. Code and models are available at this https URL.

---


### 11. [DistractMIA: Black-Box Membership Inference on Vision-Language Models via Semantic Distraction](https://arxiv.org/abs/2605.12574)

**<font color=#1a73e8>作者：</font>** Hongyi Tang, Zhihao Zhu, Yi Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are trained on large-scale image-text corpora that may contain private, copyrighted, or otherwise sensitive data, motivating membership inference as a tool for training-data auditing. This is especially challenging for deployed VLMs, where auditors typically observe only generated textual responses. Existing VLM membership inference attacks either rely on probability-level signals unavailable in such settings, or use mask-based semantic prediction tasks whose effectiveness depends on object-centric visual assumptions. To address these limitations, we propose DistractMIA, an output-only black-box framework based on semantic distraction. Rather than removing visual evidence, DistractMIA preserves the original image, inserts a known semantic distractor, and measures how generated responses change. This design is motivated by the intuition that member samples remain more anchored to the original image semantics, while non-member samples are more easily redirected toward the distractor. To make this signal reliable, DistractMIA calibrates distractor configurations on a reference set and derives membership scores from repeated textual generations, capturing response stability and distractor uptake without accessing logits, probabilities, or hidden states. Experiments across multiple VLMs and benchmarks show that DistractMIA consistently outperforms both output-only and stronger-access baselines. Its performance on a medical benchmark further demonstrates applicability beyond object-centric natural images.

---


### 12. [Towards Robust Federated Multimodal Graph Learning under Modality Heterogeneity](https://arxiv.org/abs/2605.12584)

**<font color=#1a73e8>作者：</font>** Sirui Zhang, Haonan Wang, Xunkai Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recently, multimodal graph learning (MGL) has garnered significant attention for integrating diverse modality information and structured context to support various network applications. However, real-world graphs are often isolated due to data-sharing limitations across multiple parties, and their modalities are frequently incomplete. This highlights an urgent need to develop a robust federated approach. However, we find that existing methods remain insufficient. On the one hand, centralized MGL methods that handle missing modalities overlook the knowledge sharing and generalization in federated scenarios. On the other hand, while federated MGL methods have become increasingly mature, they primarily target non-graph data. Based on these technologies, we identify a two-stage pipeline wherein client-side completion reconstructs missing modalities, and server-side aggregation integrates the client-updated parameters of both the modality generator and the backbone models. Although this serves as a general solution, we identify two primary challenges in achieving greater robustness: (1) Topology-Isolated Local Completion: Client-side modality generation struggles to effectively leverage global semantics. (2) Reliability-Imbalanced Global Aggregation: Server-side multi-party collaboration is hindered by client updates with varying modality availability and recovery reliability. To address these challenges, we propose \textsc{FedMPO}, which utilizes topology-aware cross-modal generation to recover missing features using comprehensive graph context, missing-aware expert routing to locally filter out noisy recovered signals, and reliability-aware aggregation to appropriately down-weight unreliable updates. Extensive experiments on 3 tasks across 6 datasets demonstrate that FedMPO outperforms baselines, achieving performance gains of up to 4.10% and 5.65% in high-missing and non-IID settings.

---


### 13. [3D Primitives are a Spatial Language for VLMs](https://arxiv.org/abs/2605.12586)

**<font color=#1a73e8>作者：</font>** Junze Liu, Kun Qian, Florian Dubost 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) exhibit a striking paradox: they can generate executable code that reconstructs a 3D scene from geometric primitives with correct object counts, classes, and approximate positions, yet the same models fail at simpler spatial questions on the same image. We show that 3D geometric primitives (cubes, spheres, cylinders, expressed in executable code) serve as a powerful intermediate representation for spatial understanding, and exploit this through three contributions. First, we introduce \textbf{\textsc{SpatialBabel}}, a benchmark evaluating fourteen VLMs on primitive-based 3D scene reconstruction across six \emph{scene-code languages} (programming languages and declarative formats for 3D primitive scenes), revealing that a single model's object-detection F1 can vary by up to $5.7\times$ across languages. Second, we propose \textbf{Code-CoT} (Code Chain-of-Thought), a training-free inference strategy that routes spatial reasoning through primitive-based code generation. Code-CoT lifts the SpatialBabel-QA-Score by up to $+6.4$\% on primitive scenes and real-photo CV-Bench-3D accuracy by $+5.0$\% for VLMs with strong coding capabilities. Third, we propose \textbf{S$^{3}$-FT} (Self-Supervised Spatial Fine-Tuning), which self-supervisedly distills primitive spatial knowledge into general visual reasoning by parsing the model's own this http URL primitive-reconstructions into structured annotations and fine-tuning on the result, with \emph{no human labels and no teacher model}. Training on primitive images alone, S$^3$-FT improves Qwen3-VL-8B by $+4.6$ to $+8.6$\% on SpatialBabel-Primitive-QA, $+9.7$\% on CV-Bench-2D, and $+17$\% on HallusionBench; the recipe transfers across model families. These results establish geometric primitives in code as both a diagnostic and a transferable spatial vocabulary for VLMs. We will release all artifacts upon publication.

---


### 14. [Think Twice, Act Once: Verifier-Guided Action Selection For Embodied Agents](https://arxiv.org/abs/2605.12620)

**<font color=#1a73e8>作者：</font>** Nishad Singhi, Christian Bialas, Snehal Jauhri 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building generalist embodied agents capable of solving complex real-world tasks remains a fundamental challenge in AI. Multimodal Large Language Models (MLLMs) have significantly advanced the reasoning capabilities of such agents through strong vision-language knowledge and chain-of-thought (CoT) reasoning, yet remain brittle when faced with challenging out-of-distribution scenarios. To address this, we propose Verifier-Guided Action Selection (VegAS), a test-time framework designed to improve the robustness of MLLM-based embodied agents through an explicit verification step. At inference time, rather than committing to a single decoded action, VeGAS samples an ensemble of candidate actions and uses a generative verifier to identify the most reliable choice, without modifying the underlying policy. Crucially, we find that using an MLLM off-the-shelf as a verifier yields no improvement, motivating our LLM-driven data synthesis strategy, which automatically constructs a diverse curriculum of failure cases to expose the verifier to a rich distribution of potential errors at training time. Across embodied reasoning benchmarks spanning the Habitat and ALFRED environments, VeGAS consistently improves generalization, achieving up to a 36% relative performance gain over strong CoT baselines on the most challenging multi-object, long-horizon tasks.

---


### 15. [Training LLMs with Reinforcement Learning for Intent-Aware Personalized Question Answering](https://arxiv.org/abs/2605.12645)

**<font color=#1a73e8>作者：</font>** Maryam Amirizaniani, Benjamin Charles Germain Lee, Jevin West 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Effective personalized question answering (PQA) in language models requires grounding responses in the user's underlying intent, where intent refers to the implicit ``why'' behind a query beyond its explicit wording. However, existing approaches to intent-aware personalization rely on multi-turn conversational context or rich user profiles, and do not explicitly model user intent during the reasoning process. This limits their effectiveness in single-turn settings, where the user's latent goal must be inferred from minimal input and integrated into the thinking and reasoning process. To bridge this gap, we propose IAP (Intent-Aware Personalization), a reinforcement learning framework that trains models to infer implicit user intent directly from a single-turn question and incorporate it into thinking steps through a tag-based schema for generating personalized, intent-grounded answers. By optimizing intent-aware answer trajectories under a personalized reward function, IAP reinforces generation paths that make implicit user intent explicit and produce responses that better align with the user's underlying goal. Through experiments on the LaMP-QA benchmark across six models, IAP consistently outperforms all baselines, achieving an average macro-score gain of around 7.5\% over the strongest competitor, demonstrating that modeling implicit user intent within the training objective is a promising direction for PQA.

---


### 16. [Learning to Decide with AI Assistance under Human-Alignment](https://arxiv.org/abs/2605.12646)

**<font color=#1a73e8>作者：</font>** Nina Corvelo Benz, Eleni Straitouri, Manuel Gomez-Rodriguez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It is widely agreed that when AI models assist decision-makers in high-stakes domains by predicting an outcome of interest, they should communicate the confidence of their predictions. However, empirical evidence suggests that decision-makers often struggle to determine when to trust a prediction based solely on this communicated confidence. In this context, recent theoretical and empirical work suggests a positive correlation between the utility of AI-assisted decision-making and the degree of alignment between the AI confidence and the decision-makers' confidence in their own predictions. Crucially, these findings do not yet elucidate the extent to which this alignment influences the complexity of learning to make optimal decisions through repeated interactions. In this paper, we address this question in the canonical case of binary predictions and binary decisions. We first show that this problem is equivalent to a two-armed online contextual learning problem with full feedback, and establish a lower bound of $\Omega (\sqrt{|H| \cdot |B| \cdot T} )$ on the expected regret any learner can attain, where $H$ and $B$ denote the sets of human and AI confidence values. We then demonstrate that, under perfect alignment between AI and human confidence, a learner can attain an expected regret of $O(\sqrt{|H| \cdot T\log T})$ and, when $\sqrt{|H|} = O(\log T)$ and $B$ is countable, a non-trivial generalization of the Dvoretzky-Kiefer-Wolfowitz inequality improves the regret bound to $O(\sqrt{T\log T})$. Taken together, these results reveal that alignment can reduce the complexity of learning to make decisions with AI assistance. Experiments on real data from two different human-subject studies where participants solve simple decision-making tasks assisted by AI models show that our theoretical results are robust to violations of perfect alignment.

---


### 17. [CRAFT: Clinical Reward-Aligned Finetuning for Medical Image Synthesis](https://arxiv.org/abs/2605.12650)

**<font color=#1a73e8>作者：</font>** Yunsung Chung, Alex El Darzi, Carlo El Khoury 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation diffusion models can generate photorealistic natural images, but adapting them to medical imaging remains challenging. In medical adaptation, limited labeled data can exacerbate hallucination-like and clinically implausible synthesis, while existing metrics such as FID or Inception Score do not quantify per-image alignment with pathology-relevant criteria. We introduce the Clinical Alignment Score (CAS), a foundation-model-based proxy for clinical alignment that evaluates generated images along four complementary dimensions beyond visual fidelity. Building on CAS, we propose Clinical Reward-Aligned Finetuning (CRAFT), a reward-based adaptation framework that transfers medical knowledge from multimodal large language models and vision-language models through label-conditioned prompt enrichment, clinical checklists, and differentiable reward optimization. Across four diverse modalities, CRAFT improves CAS and downstream classification performance over strong adaptation baselines. Beyond average CAS gains, CRAFT reduces the empirical low-alignment tail below a real-image reference threshold by 5.5-34.7% points relative to the strongest baseline, corresponding to a 20.4% average relative reduction across datasets. These results indicate fewer hallucination-like generations under CAS, and are corroborated by out-of-family evaluator evaluation, structured checklist auditing, memorization analysis, and a blinded physician preference study on CheXpert.

---


### 18. [ODRPO: Ordinal Decompositions of Discrete Rewards for Robust Policy Optimization](https://arxiv.org/abs/2605.12667)

**<font color=#1a73e8>作者：</font>** Nirmal Patel, Fei Wang, Inderjit Dhillon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The alignment of Large Language Models (LLMs) utilizes Reinforcement Learning from AI Feedback (RLAIF) for non-verifiable domains such as long-form question answering and open-ended instruction following. These domains often rely on LLM based auto-raters to provide granular, multi-tier discrete rewards (e.g., 1-10 rubrics) that are inherently stochastic due to prompt sensitivity and sampling randomness. We empirically verify the stochasticity of auto-raters that can propagate and corrupt standard advantage estimators like GRPO and MaxRL, as a noisy reward samples can skew normalization statistics and degrade the global learning signal. Empirically, sampling more rewards and taking majority voting may reduce the noise and improve performance, but this approach is computationally expensive. To address this bottleneck, we introduce $\textbf{O}$rdinal $\textbf{D}$ecomposition for $\textbf{R}$obust $\textbf{P}$olicy $\textbf{O}$ptimization ($\textbf{ODRPO}$), a framework that structurally isolates evaluation noise by decomposing discrete rewards into a sequence of ordinal binary indicators. By independently computing and accumulating advantages across these progressively challenging success thresholds, ODRPO prevents outlier evaluations from corrupting the global update while establishing an implicit, variance-aware learning curriculum. Empirically, ODRPO achieves robust performance on Qwen2.5-7B and Qwen3-4B models, outperforming baselines with relative improvements of upto 14.8% on FACTS-grounding-v2 and 7.5% on Alpaca-Evals. Critically, these gains are achieved with negligible training-time overhead, as ODRPO requires no additional compute per step compared to standard estimators. Supported by theoretical analysis confirming its optimization stability, ODRPO provides a scalable and robust framework for aligning models within the noisy, discrete evaluation landscape of modern RLAIF.

---


### 19. [All Circuits Lead to Rome: Rethinking Functional Anisotropy in Circuit and Sheaf Discovery for LLMs](https://arxiv.org/abs/2605.12671)

**<font color=#1a73e8>作者：</font>** Xi Chen, Mingyu Jin, Jingcheng Niu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we present empirical and theoretical evidence against a central but largely implicit assumption in circuit and sheaf discovery (CSD), which we term the Functional Anisotropy Hypothesis: the idea that functions in large language models (LLMs) are localised to a unique or near-unique internal mechanism. We show that a single LLM task can instead be supported by multiple, structurally distinct circuits or sheaves that are simultaneously faithful, sparse, and complete. To systematically uncover such competing mechanisms, we introduce Overlap-Aware Sheaf Repulsion, a method that augments the CSD objective with an explicit penalty on structural overlap across multiple discovery runs, enabling the discovery of circuits or sheaves with strong task performance but minimal shared structure across a plethora of common CSD benchmarks. We find that this phenomenon becomes increasingly pronounced as the number of discovered sheaves grows and persists robustly across major CSD methods. We further identify an ultra-sparse three-edge sheaf and show that none of its edges is individually indispensable, undermining even weakened notions of canonical or essential components. To explain these findings, we propose a Distributive Dense Circuit Hypothesis and provide a theoretical analysis demonstrating that non-unique, low-overlap circuit explanations arise naturally from high-dimensional superposition under mild assumptions. Together, our results suggest that mechanistic explanations in LLMs are inherently non-canonical and call for a rethinking of how CSD results should be interpreted and evaluated.

---


### 20. [No One Knows the State of the Art in Geospatial Foundation Models](https://arxiv.org/abs/2605.12678)

**<font color=#1a73e8>作者：</font>** Isaac Corley, Nils Lehmann, Caleb Robinson 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models (GFMs) have been proposed as generalizable backbones for disaster response, land-cover mapping, food-security monitoring, and other high-stakes Earth-observation tasks. Yet the published work about these models does not give reviewers or users enough information to tell which model fits a given task. We argue that nobody knows what the current state of the art is in geospatial foundation models. The methods may be useful, but the GFM literature does not standardize evaluations, training and testing protocols, released weights, or pretraining controls well enough for anyone to compare or rank them. In a 152-paper audit, we find 46 cross-paper disagreements of at least 10 points for the same model, benchmark, and protocol; 94/126 papers with extractable pretraining data use a configuration no other paper uses; and 39% of GFM papers release no model weights. This lack of community standards can be solved. We propose six concrete expectations: named-license weight release, shared core evaluations, copied-versus-rerun baseline annotations, variance reporting, one shared evaluation harness, and data-vs-architecture-vs-algorithm controls. These gaps are a coordination failure, not a fault of any individual lab; the authors of this paper, like many others in the GFM community, have contributed to them. Rather than just critiquing the community, we aim to provide concrete steps toward a shared understanding of how to innovate GFMs.

---


### 21. [Learning Transferable Latent User Preferences for Human-Aligned Decision Making](https://arxiv.org/abs/2605.12682)

**<font color=#1a73e8>作者：</font>** Alina Hyk, Sandhya Saisubramanian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as reasoning modules in many applications. While they are efficient in certain tasks, LLMs often struggle to produce human-aligned solutions. Human-aligned decision making requires accounting for both explicitly stated goals and latent user preferences that shape how ambiguous situations should be resolved. Existing approaches to incorporating such preferences either rely on extensive and repeated user interactions or fail to generalize latent preferences across tasks and contexts, limiting their practical applicability. We consider a setting in which an LLM is used for high-level reasoning and is responsible for inferring latent user preferences from limited interactions, which guides downstream decision making. We introduce CLIPR (Conversational Learning for Inferring Preferences and Reasoning), a framework that learns actionable, transferable natural language rules that represent latent user preferences from minimal conversational input. These rules are iteratively refined through adaptive feedback and applied to both in-distribution and out-of-distribution ambiguous tasks across multiple environments. Evaluations on three datasets and a user study show that CLIPR consistently outperforms existing methods in improving alignment and reducing inference costs.

---


### 22. [Visual Aesthetic Benchmark: Can Frontier Models Judge Beauty?](https://arxiv.org/abs/2605.12684)

**<font color=#1a73e8>作者：</font>** Yichen Feng, Yuetai Li, Chunjiang Liu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) are now routinely deployed for visual understanding, generation, and curation. A substantial fraction of these applications require an explicit aesthetic judgment. Most existing solutions reduce this judgment to predicting a scalar score for a single image. We first ask whether such scores faithfully capture comparative preference: in a controlled study with eight expert annotators, score-derived rankings align poorly with the same annotators' direct comparisons, while direct ranking yields substantially higher inter-annotator agreement on best- and worst-image labels. Motivated by this finding, we introduce the Visual Aesthetic Benchmark (VAB), which casts aesthetic evaluation as comparative selection over candidate sets with matched subject matter. VAB contains 400 tasks and 1,195 images across fine art, photography, and illustration, with labels derived from the consensus of 10 independent expert judges per task. Evaluating 20 frontier MLLMs and six dedicated visual-quality reward models, we find that the strongest system identifies both the best and the worst image correctly across three random permutations of the candidate order in only 26.5% of tasks, far below the 68.9% achieved by human experts. Fine-tuning a 35B-parameter model on 2,000 expert examples brings its accuracy close to that of a 397B-parameter open-weight model, suggesting that the comparative signal in VAB is transferable. Together, these results expose a clear and measurable gap between current multimodal models and expert aesthetic judgment, and VAB provides the first set-based, expert-grounded testbed on which that gap can be tracked and closed.

---


### 23. [DisaBench: A Participatory Evaluation Framework for Disability Harms in Language Models](https://arxiv.org/abs/2605.12702)

**<font color=#1a73e8>作者：</font>** Eugenia Kim, Ioana Tanase, Christina Mallon  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> General-purpose safety benchmarks for large language models do not adequately evaluate disability-related harms. We introduce DisaBench: a taxonomy of twelve disability harm categories co-created with people with disabilities and red teaming experts, a taxonomy-driven evaluation methodology that pairs benign and adversarial prompts across seven life domains, and a dataset of 175 prompts with human-annotated labels on 525 prompt-response pairs. Annotation by four evaluators with lived disability experience reveals three findings: harm rates vary sharply by disability type and will compound in non-text modalities, terminology-driven harm is culturally and temporally bound rather than universally assessable, and standard safety evaluation catches overt failures while missing the subtle harms that only domain expertise can recognize. Disability harm is simultaneously personal, intersectional, and community-defined: it cannot be isolated from the full context of who a person is, and general-purpose benchmarks systematically miss it. We will release the dataset, taxonomy, and methodology via Hugging Face and an open-source red teaming framework for direct integration into existing safety pipelines with no additional infrastructure.

---


### 24. [MMCL-Bench: Multimodal Context Learning from Visual Rules, Procedures, and Evidence](https://arxiv.org/abs/2605.12703)

**<font color=#1a73e8>作者：</font>** Yifan Chen, Fei Yin, Qingyan Bai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce MMCL-Bench, a benchmark for multimodal context learning: learning task-local rules, procedures, and empirical patterns from visual or mixed-modality teaching context and applying them to new visual instances. Unlike text-only context learning or standard multimodal question answering, this setting requires models to recover and localize relevant evidence from images, screenshots, manuals, videos, and frame sequences before they can reason over the learned context. MMCL-Bench contains 102 tasks spanning three categories: rule system application, procedural task execution, and empirical discovery and induction. We evaluate frontier multimodal models with strict rubric-based scoring and find that current systems remain far from robust multimodal context learning, with even the strongest model solving fewer than one-third of tasks under strict evaluation. Diagnostic ablations and error analysis show that failures arise throughout the context-to-answer pipeline, including context anchoring, visual evidence extraction, context reasoning, and response construction. MMCL-Bench thus highlights multimodal context learning as an important unsolved capability bottleneck for current multimodal models.

---


### 25. [Early Data Exposure Improves Robustness to Subsequent Fine-Tuning](https://arxiv.org/abs/2605.12705)

**<font color=#1a73e8>作者：</font>** Lawrence Feng, Gaurav R. Ghosal, Jacob Mitchell Springer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How can we train models whose post-trained capabilities survive subsequent fine-tuning? Rather than focusing on downstream interventions to mitigate forgetting of upstream capabilities, we study how upstream training choices - that is, the manner in which a capability is acquired - shape how robustly that capability is retained. We investigate this question in a controlled three-stage language-model pipeline: pretraining, post-training to acquire a target capability, and downstream fine-tuning on a new objective. Across 135M and 1B models, two post-training domains, and two downstream fine-tuning tasks, we find that immediate post-training performance does not reliably predict retention after subsequent fine-tuning: training recipes that look equivalent immediately after post-training can retain the target capability very differently after subsequent fine-tuning. In particular, early exposure - mixing post-training data into pretraining - consistently improves the frontier between retained upstream performance and downstream performance. In compute-matched experiments, where the target data must be allocated between pretraining and post-training, we find that the optimum lies at neither extreme. Together with our other empirical and theoretical findings, this supports the view that post-training drives immediate specialization while early exposure improves robustness to later forgetting. Replay and dropout, typically used to mitigate forgetting as it occurs during fine-tuning, provide complementary gains to early exposure when applied during post-training. Our findings suggest that robustness to subsequent fine-tuning should be treated as a first-class objective of upstream training, addressed preventatively through choices like early exposure rather than reactively during fine-tuning itself.

---


### 26. [Layer-wise Representation Dynamics: An Empirical Investigation Across Embedders and Base LLMs](https://arxiv.org/abs/2605.12714)

**<font color=#1a73e8>作者：</font>** Jingzhou Jiang, Yi Yang, Kar Yan Tam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hidden states change substantially across the layers of modern language models, but most layer-wise analyses focus on one aspect of that change. We propose Layer-wise Representation Dynamics (LRD), a framework with three layer-wise measurement families: Frenet (Grassmann speed and curvature) for global subspace motion, Neighborhood Retention Score (NRS) for local nearest-neighbor retention, and Graph Filtration Mutual Information (GFMI) for alignment with the final layer. Applying LRD to 31 models (encoder-based and decoder-based embedders, plus base LLMs) on 30 MTEB tasks reveals architectural and task-level differences that are not apparent from final-layer representations alone. We then use LRD for two applications: label-free model selection and inference-time layer pruning. For selection, all three model-level scores correlate positively with downstream MTEB performance, with end-to-end subspace displacement (d_{0,L}) the strongest, and the same direction holds on a smaller base-LLM MMLU panel. For pruning, GFMI is the only measurement-guided rule that beats Random at the 15% and 20% budgets and has the best median change at every budget. Frenet is effective only at the lightest budget, while NRS does not transfer from model selection to pruning. These results show that layer-wise structure provides signal for both interpretation and deployment decisions.

---


### 27. [CHAL: Council of Hierarchical Agentic Language](https://arxiv.org/abs/2605.12718)

**<font color=#1a73e8>作者：</font>** Tommaso Giovannelli, Griffin D. Kent  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate has emerged as a promising approach for improving LLM reasoning on ground-truth tasks, yet current methodologies face certain structural limitations: debate tends to induce a martingale over belief trajectories, majority voting accounts for most observed gains, and LLMs exhibit confidence escalation rather than calibration across rounds. We argue that the genuine value of debate, and dialectic systems as a whole, lies not in ground-truth tasks but in defeasible domains, where every position can in principle be defeated by better reasoning. We present the Council of Hierarchical Agentic Language (CHAL), a multi-agent dialectic framework that treats defeasible argumentation as an engine for belief optimization. Each agent maintains a CHAL Belief Schema (CBS), a graph-structured belief representation with a Bayesian-inspired architecture, that facilitates belief revision through a gradient-informed dynamic mechanism by leveraging the strength of the belief's thesis as a differentiable objective. Meta-cognitive value systems spanning epistemology, logic, and ethics are elevated to configurable hyperparameters governing agent reasoning and adjudication outcomes. We provide a series of ablation experiments that demonstrate systematic and interpretable effects: the adjudicator's value system determines the debate's overall trajectories in latent belief space, council diversity refines beliefs for all participants, and the framework generalizes across broad fields. CHAL is, to our knowledge, the first framework to treat multi-agent debate as structured belief optimization over defeasible domains. Further, the auditable belief artifacts it produces establish the foundation for dedicated evaluation suites for defeasible argumentation, with broader implications for building AI systems whose reasoning and value commitments are transparent, aligned, and subject to human oversight.

---


### 28. [Is Video Anomaly Detection Misframed? Evidence from LLM-Based and Multi-Scene Models](https://arxiv.org/abs/2605.12725)

**<font color=#1a73e8>作者：</font>** Furkan Mumcu, Michael J. Jones, Anoop Cherian 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video anomaly detection research has expanded rapidly with an emphasis on general models of normality intended to work across many different scenes. While this focus has led to improvements in scalability and multi-scene generalization, it has also shifted the field away from modeling the scene-specific and context-dependent nature of normal behavior. Contemporary approaches frequently rely on video-level weak supervision and opaque pretrained representations from multi-modal large language models (MLLMs), which encourage models to respond to familiar semantic anomaly categories rather than to deviations from the normal patterns of a particular environment. This trend suppresses spatial localization, introduces semantic bias, and reduces anomaly detection to a form of action recognition. In this paper, we examine whether these prevailing formulations align with the core requirements of real-world VAD, which is typically performed within a single scene where normality is determined by local geometry, semantics, and activity patterns. Through targeted visual analyses and empirical evaluations, we demonstrate the practical consequences of these limitations and show that meaningful progress in VAD requires renewed focus on single-scene, spatially-aware, and explainable formulations that capture the nuanced structure of normality within individual environments.

---


### 29. [Learning with Rare Success but Rich Feedback via Reflection-Enhanced Self-Distillation](https://arxiv.org/abs/2605.12741)

**<font color=#1a73e8>作者：</font>** Yuwei Zhang, Sha Li, Changlong Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enabling Large Language Models (LLMs) to continuously improve from environmental interactions is a central challenge in post-training. While on-policy self-distillation offers a promising paradigm, existing methods predominantly treat environmental feedback as a passive conditioning signal. Consequently, they heavily rely on successful demonstrations and struggle to learn in rare-success regimes. To bridge this gap, we introduce Reflection-Enhanced Self-Distillation (RESD), a framework that transforms raw failure feedback into an active source of corrective supervision. Instead of passively appending feedback, RESD interprets failed trajectories by generating retrospective reflections to diagnose local errors, and curates a persistent global playbook to preserve reusable lessons across training steps. The enriched context enables the self-teacher to provide actionable token-level supervision even in the absence of successful rollouts. Empirical evaluations on multiple continual learning tasks demonstrate that RESD substantially outperforms standard self-distillation baselines. Furthermore, RESD achieves significantly faster early-stage improvement than GRPO with $8\times$ samples using only a single rollout per prompt, highlighting its superior interaction efficiency.

---


### 30. [Simulating Students or Sycophantic Problem Solving? On Misconception Faithfulness of LLM Simulators](https://arxiv.org/abs/2605.12748)

**<font color=#1a73e8>作者：</font>** Heejin Do, Shashank Sonkar, Mrinmaya Sachan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can fluently generate student-like responses, making them attractive as simulated students for training and evaluating AI tutors and human educators. Yet such simulators are typically evaluated by output similarity to real students, not by whether they behave like students with coherent misconceptions during interaction. We introduce a controlled framework for evaluating misconception faithfulness, whether a simulator maintains a misconception-driven belief state and updates selectively when feedback addresses the underlying misconception. Central to our framework is a misconception-contrastive feedback protocol that compares targeted feedback against two controls: misaligned feedback (targeting a different but plausible misconception) and generic feedback (only identifying answer is wrong). We propose Selective Flip Score (SFS), which quantifies how much more often a simulator flips its answer under targeted feedback than under contrastive controls. Across seven LLMs (4B-120B), multiple datasets, and prompting strategies, simulators exhibit near-zero SFS, correcting their answers at similarly high rates regardless of feedback relevance. Further analyses reveal a sycophantic failure mode: models behave less like students with misconceptions but more like problem-solvers who treat any corrective signal as a cue to abandon the simulated belief and re-solve from internal knowledge. To address this, we develop a post-training pipeline spanning supervised fine-tuning (SFT), preference optimization, and reinforcement learning (RL) with an SFS-aligned reward; SFT yields notable gains up to +0.56, and SFS-aligned RL provides more consistent improvements than preference optimization. Our results establish misconception faithfulness as a challenging yet trainable property, motivating a shift from static output matching toward interactive, belief-aware student modeling.

---


### 31. [Low-Rank Adapters Initialization via Gradient Surgery for Continual Learning](https://arxiv.org/abs/2605.12752)

**<font color=#1a73e8>作者：</font>** Joana Pasquali, Ramiro N. Barros, Arthur S. Bianchessi 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LoRA is widely adopted for continual fine-tuning of Large Language Models due to its parameter efficiency, modularity across tasks, and compatibility with replay strategies. However, LoRA-based continual learning remains vulnerable to catastrophic forgetting, whose severity depends on how successive task gradients interact: when consecutive task gradients conflict, standard adapter initializations channel updates into subspaces that overwrite previously learned directions. We propose SLICE, a gradient-surgery-based initialization for LoRA adapters in continual learning. SLICE accumulates gradients from both the current task and a replay buffer of prior tasks, reconciles them through a projection operator, and decomposes the result via truncated SVD to initialize the adapter weights. We evaluate SLICE on the TRACE benchmark and sequences of Super-NI tasks, including a set of adversarial Super-NI sequences that we construct by mining task pairs with maximally opposing gradients. Compared to vanilla LoRA, LoRA-GA, and LoRAM, SLICE consistently achieves a better stability-plasticity trade-off, improving Average Performance, Final Performance and Forgetting metrics while preserving General Performance and In Context Performance across both standard and adversarial continual learning sequences.

---


### 32. [Just Ask for a Table: A Thirty-Token User Prompt Defeats Sponsored Recommendations in Twelve LLMs](https://arxiv.org/abs/2605.12772)

**<font color=#1a73e8>作者：</font>** Andreas Maier, Jeta Sopa, Gozde Gul Sahin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wu et al. (2026) showed that most frontier large language models (LLMs) recommend a sponsored, roughly twice-as-expensive flight when their system prompt contains a soft sponsorship cue. We reproduce their evaluation on ten open-weight chat models plus the two of their twenty-three models that are still reachable today (gpt-3.5-turbo, gpt-4o). All reported rates in this paper are produced under the same judge the original paper used (gpt-4o); we additionally store every label under an open-weight (gpt-oss-120b) and a smaller proprietary (gpt-4o-mini) judge for an ablation. Three findings emerge. First, a prose description of an LLM evaluation pipeline is not, on its own, sufficient for accurate reproduction: we surfaced three silent implementation failures that each shifted a reported rate by tens of percentage points. Second, the central claims do generalise - the gpt-3.5-turbo logistic-regression intercept of alpha = 0.81 is within four points of the original alpha = 0.86, and 200 of 200 trials on gpt-3.5-turbo and gpt-4o promote a payday lender to a financially distressed user. Third, a thirty-token user prompt that asks the assistant for a neutral comparison table first cuts sponsored recommendation from 46.9% to 1.0% averaged across our ten open-source models, and from 53.0% to 0% averaged across the two OpenAI models. AI literacy and price-comparison portals are likely market-level mitigations; the harmful-product cell is bounded by neither. Raw data, labels and analysis scripts are at this https URL .

---


### 33. [ToolMol: Evolutionary Agentic Framework for Multi-objective Drug Discovery](https://arxiv.org/abs/2605.12784)

**<font color=#1a73e8>作者：</font>** Andrew Y. Zhou, Sharvaree Vadgama, Sumanth Varambally 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Advances in large language models (LLMs) have recently opened new and promising avenues for small-molecule drug discovery. Yet existing LLM-based approaches for molecular generation often suffer from high rates of invalid and low-quality ligand candidates, a result of the syntactic limitations of current models with regard to molecular strings. In this paper, we introduce $\texttt{ToolMol}$, an evolutionary agentic framework for de novo drug design. $\texttt{ToolMol}$ combines a multi-objective genetic algorithm with an agentic LLM operator that iteratively updates the ligand population. We build a comprehensive toolbox of RDKit-backed functions that allows our agentic operator to consisently make precise ligand modifications. $\texttt{ToolMol}$ achieves state-of-the-art performance on multi-objective property optimization tasks, discovering drug-like and synthesizable ligands that have $>10\%$ stronger predicted binding affinity compared to existing methods, evaluated on three protein targets. $\texttt{ToolMol}$ ligands additionally achieve state-of-the-art results in gold-standard Absolute Binding Free Energy scores, gaining over existing methods by over $35\%$. By studying chain-of-thought reasoning traces, we observe that tool-calling enables the model to more faithfully execute its planned modifications, efficiently exploiting the strong chemical prior knowledge in LLMs.

---


### 34. [Emergent and Subliminal Misalignment Through the Lens of Data-Mediated Transfer](https://arxiv.org/abs/2605.12798)

**<font color=#1a73e8>作者：</font>** Baris Askin, Muhammed Ustaomeroglu, Anupam Nayak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fine-tuning LLMs on narrow harmful datasets can induce Emergent Misalignment (EM), where models exhibit misaligned behavior far beyond the fine-tuning distribution. We argue that emergent misalignment can be better understood as a data-mediated transfer phenomenon: harmful fine-tuning examples do not induce uniform behavioral spillover, but interact with the structural properties of the dataset and the difficulty of the tasks relative to the model. Across our experiments, we find that misalignment appears more readily when fine-tuning and evaluation prompts share similar underlying functional structure, when prompts leave more room for coherent harmful completions, and when the target behavior has been more reliably learned by the model. The training pipeline itself also matters: pretraining composition shapes later misalignment. We further study Subliminal Learning (SL), where misalignment is transmitted by fine-tuning on seemingly benign data generated by a harmful teacher. Moving beyond the standard SFT setting, we for the first time compare this transfer under off-policy and on-policy distillation as well, allowing us to separate the roles of the teacher guidance and the training data distribution in transmitting misalignment. Together, these results argue for a data-centric view: Emergent/subliminal misalignment should not be treated as a simple consequence of isolated harmful fine-tuning examples, but as the result of interactions between fine-tuning data structure, pretraining distributions, and training channels.

---


### 35. [Synthesizing the Expert: A Validated Multimodal Dataset for Trustworthy AI-Assisted Swimming Coaching](https://arxiv.org/abs/2605.12799)

**<font color=#1a73e8>作者：</font>** Ahmad Al-Kabbany, Esraa Kassem  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This research is primarily concerned with the critical problem of synthesizing a structured Retrieval-Augmented Generation (RAG) system for advanced AI applications in the domain of swimming. As the integration of Artificial Intelligence in sports science matures, its applications in swimming have become increasingly diverse, spanning from real-time technical coaching and talent scouting to comprehensive performance profiling and the dynamic personalization of training periodization. Within this landscape, RAG-based systems represent a pivotal advancement in Large Language Model (LLM) enhanced swimming analysis, as they allow for the grounding of generative outputs in authoritative domain knowledge, thereby ensuring the credibility of AI-generated advice, contextually and technically. Despite this potential, building robust RAG systems using only real-world aquatic data presents significant challenges, including ethical constraints regarding athlete biometrics, and the high cost of manual expert labeling. To address these barriers, we propose a novel generative framework that leverages a multimodal knowledge base gathered across four dimensions: physiological data, physiological literature, kinematic sensor data, and unstructured domain expertise. Our proposed framework utilizes a multi-agent LLM architecture to synthesize a high-fidelity dataset of 1,864 validated "Question-Context-Answer" triplets-drawn from 1,914 drafts evaluated against 12 physiological soundness rules. By providing a structured, synthetic ground truth, this work establishes a foundational benchmark for trustworthy AI in aquatics. The outcomes of this research promise to enhance the reliability of automated coaching and open a plethora of future directions in "Meta-Agent" development and athletic profiling, ultimately bridging the gap between raw data engineering and practical sports science application.

---


### 36. [Neurodata Without Boredom: Benchmarking Agentic AI for Data Reuse](https://arxiv.org/abs/2605.12808)

**<font color=#1a73e8>作者：</font>** Ling-Qi Zhang, Kristin Branson  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neuroscience data are highly fragmented across labs, formats, and experimental paradigms, and reuse often requires substantial manual effort. A persistent roadblock to data reuse and integration is the need to decipher bespoke and diverse data formatting choices. Common data formats have been proposed in response, but the field continues to struggle with a fundamental tension: formats flexible enough to accommodate diverse experiments are rarely descriptive enough to be self-explanatory, and sufficiently descriptive formats demand detailed documentation and curation effort that few labs can sustain. Agentic AI is a natural candidate to solve this problem: LLMs read code and text faster and with sustained attention to the low-level details humans tend to skim over. To measure how well agentic AI performs on this task, we selected eight recent papers studying large-scale mouse neural population recordings that shared both data and code, spanning diverse recording modalities, behavioral paradigms, and dataset formats (e.g., NWB, specialized APIs, and general-purpose Python or MATLAB files). We provided agents with the data, code, and paper, and prompted them to load, understand, and reformat the data for a common downstream task: training a decoder from neural activity to task or behavioral variables. General-purpose coding agents commonly used by scientists performed well on each sub-task, but rarely strung together a fully error-free end-to-end solution. We characterize the types of mistakes agents made and the dataset properties that elicited them, and propose data-sharing best practices for the agentic-AI era. We further find that agents-as-judges are unreliable at catching errors, especially without ground-truth references, so interactive, human-in-the-loop coding remains necessary.

---


### 37. [Correcting Influence: Unboxing LLM Outputs with Orthogonal Latent Spaces](https://arxiv.org/abs/2605.12809)

**<font color=#1a73e8>作者：</font>** Shixing Yu, Promit Ghosal, Kyra Gan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A critical step for reliable large language models (LLMs) use in healthcare is to attribute predictions to their training data, akin to a medical case study. This requires token-level precision: pinpointing not just which training examples influence a decision, but which tokens within them are responsible. While influence functions offer a principled framework for this, prior work is restricted to autoregressive settings and relies on an implicit assumption of token independence, rendering their identified influences unreliable. We introduce a flexible framework that infers token-level influence through a latent mediation approach for general prediction tasks. Our method attaches sparse autoencoders to any layer of a pretrained LLM to learn a basis of approximately independent latent features. Unlike prior methods where influence decomposes additively across tokens, influence computed over latent features is inherently non-decomposable. To address this, we introduce a novel method using Jacobian-vector products. Token-level influence is obtained by propagating latent attributions back to the input space via token activation patterns. We scale our approach using efficient inverse-Hessian approximations. Experiments on medical benchmarks show our approach identifies sparse, interpretable sets of tokens that jointly influence predictions. Our framework enhances trust and enables model auditing, generalizing to high-stakes domain requiring transparent and accountable decisions.

---


### 38. [REALISTA: Realistic Latent Adversarial Attacks that Elicit LLM Hallucinations](https://arxiv.org/abs/2605.12813)

**<font color=#1a73e8>作者：</font>** Buyun Liang, Jinqi Luo, Liangzu Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong performance across many tasks but remain vulnerable to hallucinations, motivating the need for realistic adversarial prompts that elicit such failures. We formulate hallucination elicitation as a constrained optimization problem, where the goal is to find semantically coherent adversarial prompts that are equivalent to benign user prompts. Existing methods remain limited: discrete prompt-based attacks preserve semantic equivalence and coherence but search only over a limited set of prompt variations, while continuous latent-space attacks explore a richer space but often decode into prompts that are no longer valid rephrasings. To address these limitations, we propose REALISTA, a realistic latent-space attack framework. REALISTA constructs an input-dependent dictionary of valid editing directions, each corresponding to a semantically equivalent and coherent rephrasing, and optimizes continuous combinations of these directions in latent space. This design combines the optimization flexibility of continuous attacks with the semantic realism of discrete rephrasing-based attacks. Experiments demonstrate that REALISTA achieves superior or comparable performance to state-of-the-art realistic attacks on open-source LLMs and, crucially, succeeds in attacking large reasoning models under free-form response settings, where prior realistic attacks fail. Code is available at this https URL.

---


### 39. [Training Large Language Models to Predict Clinical Events](https://arxiv.org/abs/2605.12817)

**<font color=#1a73e8>作者：</font>** Benjamin Turtel, Paul Wilczewski, Kris Skotheim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Longitudinal clinical notes contain rich evidence of how patients evolve over time, but converting this signal into training supervision for clinical prediction remains challenging. We extend Foresight Learning to clinical prediction by converting time-ordered MIMIC-III notes into examples consisting of past patient context, a natural-language question about a possible future event, and a label resolved from later documentation. This process yields 6,900 prediction examples from 702 admissions across medications, procedures, organ support, microbiology, and mortality. A small LoRA adapter trained on these examples improves over the prompted base model, reducing expected calibration error from 0.1269 to 0.0398 and Brier score from 0.199 to 0.145, while slightly outperforming GPT-5 point estimates on held-out questions. The approach enables reusable clinical prediction supervision from longitudinal notes without hand-engineered structured features or endpoint-specific classifiers.

---


### 40. [Multimodal Hidden Markov Models for Persistent Emotional State Tracking](https://arxiv.org/abs/2605.12838)

**<font color=#1a73e8>作者：</font>** Anamika Ragu, Aneesh Jonelagadda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tracking an interpretable emotional arc of a conversation via the sentiment of individual utterances processed as a whole is central to both understanding and guiding communication in applied, especially clinical, conversational contexts. Existing approaches to emotion recognition operate at the utterance level, obscuring the persistent phases that characterize real conversational dynamics. We propose a lightweight framework that models conversational emotion as a sequence of latent emotional regimes using sticky factorial HDP-HMMs over multimodal valence-arousal representations derived from simultaneous video, audio and textual input. We evaluate the quality of regime prediction using LLM-as-a-Judge, geometric, and temporal consistency metrics, demonstrating that the sticky HDP-HMM produces more interpretable regime sequences than the baseline Gaussian HMM at a fraction of the computational cost of LLM-based dialogue state tracking methods. In addition, Question-Answer experiments in a clinical dataset suggest that meaningful emotional phases can reliably be recovered from multimodal valence-arousal trajectories and used to improve the quality of LLM responses in unstable affective regimes via context augmentation. This framework thus opens a path toward interpretable, lightweight, and actionable analysis of conversational emotion dynamics at scale.

---


### 41. [Persona-Model Collapse in Emergent Misalignment](https://arxiv.org/abs/2605.12850)

**<font color=#1a73e8>作者：</font>** Davi Bastos Costa, Renato Vicente  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models on narrow data with harmful content produces broadly misaligned behavior on unrelated prompts, a phenomenon known as emergent misalignment. We propose that emergent misalignment involves persona-model collapse: deterioration of the model's internal capacity to simulate, differentiate, and maintain consistent characters. We test this hypothesis behaviorally using two metrics: moral susceptibility (S) and moral robustness (R), computed from the across- and within-persona variability of models' Moral Foundations Questionnaire responses under persona role-play. These metrics formalize the model's ability to differentiate characters (S) and its consistency when simulating a given one (R). We evaluate four frontier models (DeepSeek-V3.1, GPT-4.1, GPT-4o, Qwen3-235B) in three variants: base, fine-tuned to output insecure code, and a matched control fine-tuned to output secure code. Across the four models, insecure fine-tuning produces an average $55\%$ increase in S, pushing all four insecure variants beyond the band observed across 13 frontier models benchmarked in prior work -- with GPT-4o reaching more than twice the band's upper end -- signaling dysregulated differentiation. It also causes an average $65\%$ decrease in R, equivalent to a $304\%$ increase in 1/R. By contrast, the matched secure control preserves S near the base and induces only a partial R loss, showing that these effects are largely misalignment-specific. Complementing these metric shifts, insecure variants' unconditioned responses converge toward saturation near the scale ceiling, departing markedly from both base models' structured responses and those elicited when base models role-play toxic personas. Taken together, these metrics provide a sensitive diagnostic for emergent misalignment and serve as behavioral evidence that it involves persona-model collapse.

---


### 42. [Multitask Multimodal Fusion with Tabular Foundation Models for Peak and Durability Prediction of Pertussis Booster Response](https://arxiv.org/abs/2605.12852)

**<font color=#1a73e8>作者：</font>** Divya Sitani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pertussis booster vaccination produces immune responses that vary widely across individuals in both peak magnitude and long-term durability. These two phases are governed by partly distinct biological compartments:peak reflects acute B-cell activation and antibody secretion, while durability reflects the establishment of long-term humoral memory. Yet most computational models target only one, missing the full boost-and-wane trajectory. Jointly predicting both is non-trivial because the two endpoints are biologically dissociated rather than redundant; samples are small, modalities are heterogeneous with structured missingness, and the two tasks rely on different measurement windows. We propose a multi-task contrastive multimodal fusion architecture combining frozen TabPFN-v2 per-modality encoders, a dual-label supervised contrastive loss that treats two subjects as a positive pair if they agree on the Task 1 label or the Task 2 label, modality dropout calibrated to empirical missingness, and missingness-masked attention fusion. Applied to a curated subset of the CMI-PB pertussis booster dataset (n = 158 subjects, four modalities, 44.9% with at least one modality missing; Spearman r = -0.58 between peak and durability, n = 96), the model achieves test AUROC 0.797 (95% CI [0.621, 0.948]) for peak response and 0.755 (95% CI [0.519, 0.945]) for durability, with both significant under joint label permutation (N = 1000; p = 0.002 and p = 0.045). Across logistic regression, XGBoost, and MLP baselines on raw features and on TabPFN embeddings, the proposed model is the only one whose 95% CIs lie above chance on both tasks simultaneously. Per-modality contribution analyses recover task-specific modality contributions consistent with the underlying immunology: peak prediction is carried by cytokine signatures, while durability is carried by baseline antibody features.

---


### 43. [SMA: Submodular Modality Aligner For Data Efficient Multimodal Learning](https://arxiv.org/abs/2605.12872)

**<font color=#1a73e8>作者：</font>** Truong Pham, Anay Majee, Rishabh Iyer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the recent success of Multimodal Foundation Models (FMs), their reliance on massive paired datasets limits their applicability in low-data and rare-scenario settings where aligned data is scarce and expensive. A key bottleneck is the adoption of an instance-level formulation, which learns alignment by maximizing correlation between individual image-text pairs while neglecting the underlying geometric structure across modalities resulting in a modality gap across input modalities. In this paper, we propose a combinatorial paradigm for multimodal alignment that moves beyond pairwise learning and introduce the \emph{Submodular Modality Aligner (SMA)}, which treats multiple augmentations and descriptions of an entity as a set, leveraging multiple descriptions of the data to capture richer cross-modal structure. We instantiate SMA using a principled objective based on Submodular Mutual Information (SMI), which jointly maximizes inter-modality mutual information while reducing cross-modal divergence. This formulation enables the model to effectively utilize multiple positive associations and extract significantly more information from limited data. We evaluate SMA on 14 zero-shot classification and retrieval tasks from the CLIP benchmark and demonstrate consistent gains in the low-data regime. Notably, SMA achieves strong multimodal generalization using only tens of thousands of samples. This is orders of magnitude fewer than standard approaches. Our results highlight the importance of set-based formulations and submodular objectives for data-efficient multimodal learning.

---


### 44. [CiteVQA: Benchmarking Evidence Attribution for Trustworthy Document Intelligence](https://arxiv.org/abs/2605.12882)

**<font color=#1a73e8>作者：</font>** Dongsheng Ma, Jiayu Li, Zhengren Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have significantly advanced document understanding, yet current Doc-VQA evaluations score only the final answer and leave the supporting evidence unchecked. This answer-only approach masks a critical failure mode: a model can land on the correct answer while grounding it in the wrong passage -- a critical risk in high-stakes domains like law, finance, and medicine, where every conclusion must be traceable to a specific source region. To address this, we introduce CiteVQA, a benchmark that requires models to return element-level bounding-box citations alongside each answer, evaluating both jointly. CiteVQA comprises 1,897 questions across 711 PDFs spanning seven domains and two languages, averaging 40.6 pages per document. To ensure fidelity and scalability, the ground-truth citations are generated by an automated pipeline-which identifies crucial evidence via masking ablation-and are subsequently validated through expert review. At the core of our evaluation is Strict Attributed Accuracy (SAA), which credits a prediction only when the answer and the cited region are both correct. Auditing 20 MLLMs reveals a pervasive Attribution Hallucination: models frequently produce the right answer while citing the wrong region. The strongest system (Gemini-3.1-Pro-Preview) achieves an SAA of only 76.0, and the strongest open-source MLLM reaches just 22.5. Ultimately, towards trustworthy document intelligence, CiteVQA exposes a reliability gap that answer-only evaluations overlook, providing the instrumentation needed to close it. Our repository is available at this https URL.

---


### 45. [Seed Bank, Co-op, Stoop Swap: Metaphors for Governing Language Model Data for Creative Writing](https://arxiv.org/abs/2605.12888)

**<font color=#1a73e8>作者：</font>** Alicia Guo, Carly Schnitzler, Katy Gero  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> How might we govern a language model run for and by creative writers? While generative AI use is on the rise, many language models are created and owned in ways that limit writers' consent, participation, and control. We report on four workshops where over one hundred creative writers came up with and analyzed metaphors for language model governance, resulting in over two hundred metaphors: objects, places, processes, groups, and infrastructure that support reasoning about language model governance. What if a language model was like a community garden? Or a seed bank? Or the bathroom in a dive bar? We report on four themes: (1) the importance of consent, (2) how to define community boundaries, (3) ways to give contributor recognition, and (4) trade-offs in scale of language models. These metaphors point towards smaller, open models that encode group values. We discuss concrete ways to make community language models a reality.

---


### 46. [Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents](https://arxiv.org/abs/2605.12894)

**<font color=#1a73e8>作者：</font>** Harshita Chopra, Kshitish Ghate, Aylin Caliskan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly deployed in settings where they interact with a wide variety of people, including users who are unclear, impatient, or reluctant to share information. However, collecting real interaction data at scale remains expensive. The field has turned to LLM-based user simulators as stand-ins, but these simulators inherit the behavior of their underlying models: cooperative and homogeneous. As a result, agents that appear strong in simulation often fail under the unseen, diverse communication patterns of real users. To narrow this gap, we introduce Persona Policies (PPol), a plug-and-play control layer that induces realistic behavioral variation in user simulators while preserving the original task goals. Rather than hand-crafting personas, we cast persona generation as an LLM-driven evolutionary program search that optimizes a Python generator to discover behaviors and translate them into task-preserving roleplay policies. Candidate generators are guided by a multi-objective fitness score combining human-likeness with broad coverage of human behavioral patterns. Once optimized, the generator produces a diverse population of human-like personas for any task in the domain. Across tau^2-bench retail and airline domains, evolved PPol programs yield 33-62% absolute gains in fitness score over the baseline simulator. In a blinded evaluation, annotators rated PPol-conditioned users as human 80.4% of the time, close to real human traces and nearly twice as frequently as baseline simulators. Agents trained with PPol are more robust to challenging, out-of-distribution behaviors, improving task success by +17% relative to training only on existing simulated interactions. This offers a novel approach to strengthen simulator-based evaluation and training without changing tasks or rewards.

---


### 47. [VIP-COP: Context Optimization for Tabular Foundation Models](https://arxiv.org/abs/2605.12904)

**<font color=#1a73e8>作者：</font>** Yilong Chen, Xueying Ding, Leman Akoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular foundation models (TFMs) have emerged as a powerful paradigm for in-context learning on structured data, enabling direct prediction on new tabular tasks without task-specific training. However, their effectiveness is constrained by context length limits, restricting application to medium-scale data and degrading performance when inference-time data exceed pretraining size distributions. Our work introduces VIP-COP, estimating the Value of Importance for Prediction of training examples and features for hard Context OPtimization for TFMs. Its explicit selection mechanism suppresses noise and isolates influential data, enabling the model to also benefit from data augmentation by prioritizing high-value augmented samples and features. VIP-COP is (i) fast, boosting performance often within minutes of optimization, based on an online KernelSHAP-based regression with iterative refinement, value-guided context sampling, and multi-fidelity pruning; (ii) budget-aware and any-time, improving with additional test-time compute unlike heuristics that produce fixed contexts; (iii) model-aware yet fully black-box, requiring no access to model internals, making it compatible with both proprietary and open-source TFMs; (iv) interpretable, identifying discrete ``Very Important Predictors'' (samples and features) that maximize signal-to-noise, which makes it (v) robust, isolating high-value data from noise. In contrast, soft-prompt optimization requires model gradients, produces abstract latent tokens, and lacks explicit signal discrimination. Extensive experiments show that VIP-COP consistently outperforms heuristic and optimized baselines across large-scale high-dimensional testbeds, including data augmentation and data-noise settings, establishing a new state of the art in test-time context refinement for TFMs.

---


### 48. [Data Difficulty and the Generalization--Extrapolation Tradeoff in LLM Fine-Tuning](https://arxiv.org/abs/2605.12906)

**<font color=#1a73e8>作者：</font>** Siyuan Liu, Tinghong Chen, Xinghan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data selection during supervised fine-tuning (SFT) can critically change the behavior of large language models (LLMs). Although existing work has studied the effect of selecting data based on heuristics such as perplexity, difficulty, or length, the reported findings are often inconsistent or context-dependent. In this work, we systematically study the role of data difficulty in fine-tuning from both empirical and theoretical perspectives, and find that there is no universally optimal difficulty level; rather, its effectiveness depends on the dataset size. We show that for a fixed data budget, there exists an optimal data difficulty for SFT, and that this optimal difficulty shifts toward harder data as the data budget increases. To explain this phenomenon, we conduct controlled synthetic experiments that reveal a simple underlying mechanism: the interplay between the (in-distribution) generalization gap and the extrapolation gap. We further support this mechanism through a theoretical analysis using PAC-Bayesian generalization bounds. Overall, our results clarify how data size and difficulty jointly affect the trade-off between generalization and extrapolation in SFT, providing guidance for difficulty-based data selection under certain model and data conditions.

---


### 49. [Revisiting DAgger in the Era of LLM-Agents](https://arxiv.org/abs/2605.12913)

**<font color=#1a73e8>作者：</font>** Changhao Li, Rushi Qiang, Jiawei Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon LM agents learn from multi-turn interaction, where a single early mistake can alter the subsequent state distribution and derail the whole trajectory. Existing recipes fall short in complementary ways: supervised fine-tuning provides dense teacher supervision but suffers from covariate shift because it is trained on off-policy teacher trajectories; while reinforcement learning with verifiable rewards avoids this off-policy mismatch by learning from on-policy rollouts but with only sparse outcome feedback. We address this dilemma by revisiting Dataset Aggregation (DAgger) for multi-turn LM agents: the algorithm collects trajectories through a turn-level interpolation of student and teacher policies, and the student is then trained on these trajectories using supervised labels provided by the teacher. By directly interacting with environments, we expose the model to realistic states likely to be encountered during deployment, thereby effectively mitigating covariate shift. Besides, since the student is learned by mimicking the teacher's behavior, it receives rich feedback during learning. To demonstrate DAgger enjoys the benefits of both worlds, we tested the algorithm to train a software-engineering agent with 4B- and 8B-scale student models. On SWE-bench Verified, our DAgger-style training improves over the strongest post-training baseline by +3.9 points at 4B and +3.6 points at 8B. The resulting 4B agent reaches 27.3%, outperforming representative published 8B SWE-agent systems, while the 8B agent achieves 29.8%, surpassing SWE-Gym-32B and coming within 5 points of stronger 32B-scale agents. Together with consistent gains on the held-out SWE-Gym split, these results suggest the effectiveness of DAgger for modern long-horizon LM agents.

---


### 50. [CommonWhy: A Dataset for Evaluating Entity-Based Causal Commonsense Reasoning in Large Language Models](https://arxiv.org/abs/2605.12918)

**<font color=#1a73e8>作者：</font>** Armin Toroghi, Faeze Moradi Kalarde, Scott Sanner  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> To effectively interact with the real world, Large Language Models (LLMs) require entity-based commonsense reasoning, a challenging task that necessitates integrating factual knowledge about specific entities with commonsense inference. Existing datasets for evaluating LLM entity-based commonsense reasoning have largely focused on True/False or multiple-choice questions, leaving the explicit assessment of the model's ability in abductive reasoning about causes and effects and generating explanations largely unexamined. In this work, we introduce CommonWhy, a dataset of 15,000 why questions designed to evaluate entity-based commonsense reasoning about causal relationships in LLMs. CommonWhy also serves as a Knowledge Graph Question Answering (KGQA) benchmark, as all supporting knowledge required to answer its queries is available in the Wikidata knowledge graph. Unlike existing KGQA datasets, which primarily test fact retrieval, CommonWhy targets causal commonsense reasoning, establishing a new paradigm for KGQA evaluation. Experiments with state-of-the-art LLMs and LLM-based KGQA methods reveal their significant shortcomings, including frequent factual hallucinations and failures in causal reasoning.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-159](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
