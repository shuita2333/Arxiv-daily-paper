# 🧠 大模型相关研究 | 2026年06月04日

> 本类共 **188** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**151-188**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-188**

---

### 151. [Qwen-Image-Flash: Beyond Objective Design](https://arxiv.org/abs/2606.03746)

**<font color=#1a73e8>作者：</font>** Tianhe Wu, Kun Yan, Zikai Zhou 等 24 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step distillation has become an effective strategy for accelerating advanced visual generative models, yet prior work has largely focused on distillation objectives. In this work, we revisit few-step distillation from a complementary perspective, focusing on the training recipe that critically shapes student performance. Using Qwen-Image-2.0 as a representative case, we systematically investigate three factors in unified text-to-image generation and instruction-guided image editing distillation: data composition, teacher guidance, and task mixture. Our empirical analysis reveals several non-obvious behaviors, which motivate the development of Qwen-Image-Flash. Overall, our results suggest that effective few-step distillation requires not only carefully designed objectives, but also principled organization of the broader training pipeline.

---


### 152. [LAP: An Agent-to-Instrument Protocol for Autonomous Science](https://arxiv.org/abs/2606.03755)

**<font color=#1a73e8>作者：</font>** Linwu Zhu, Liqiang Gao, Yan Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous science is moving from demonstration to infrastructure. Large language model agents now plan experiments, and self-driving laboratories execute them. Yet every such system rebuilds the link between the reasoning agent and the physical instrument from scratch, against fragmented vendor SDKs and standards built for deterministic software clients rather than probabilistic, goal-directed agents. Recent agent-interoperability protocols clarify two of the three edges of an agentic ecosystem (Anthropic's Model Context Protocol (MCP) standardizes the agent-to-tool edge, and Google's Agent2Agent (A2A) the agent-to-agent edge), but neither models the agent-to-instrument edge, where operations are stateful, safety-critical, exclusively owned, physically embodied, and produce measurements with units, calibration, and uncertainty. We present the Lab Agent Protocol (LAP), a protocol design that fills this gap. LAP retains A2A's peer-to-peer, discovery-first, task-lifecycle structure and adds four physical-world primitives: (i) the InstrumentCard, a signed capability and physical-limit description; (ii) first-class reservation for exclusive instrument and sample locking; (iii) a safety-fence handshake with operator-confirmation tokens cryptographically bound to a specific task and its parameters, gating hazardous and irreversible operations; and (iv) a MeasurementResult schema that makes every result physically typed (QUDT/UCUM), calibration-anchored, uncertainty-bearing, and reproducible by construction. We specify roles, a six-layer architecture, the JSON-RPC method set, the task and safety state machines, the error model, and cross-laboratory federation, and walk a closed-loop autonomous campaign through the protocol end-to-end. LAP is transport-compatible with the A2A/MCP ecosystem and encapsulates rather than replaces existing device standards such as SiLA 2 and OPC-UA.

---


### 153. [Framing Migration News with LLMs: Structured CoT as a Support for Human Interpretation](https://arxiv.org/abs/2606.03761)

**<font color=#1a73e8>作者：</font>** David Alonso del Barrio, Jing Wen, Daniel Gatica-Perez  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frame analysis of migration news is a socially consequential task: media scholars and researchers who study how migration is narrated need tools that are not only accurate, but transparent, auditable, and accessible within the resource constraints typical of academic research groups. Existing LLM-based approaches rely on proprietary APIs and large models that raise concerns about data privacy, reproducibility and equitable access among media researchers. This work studies how a locally deployable open-source LLM can support interpretable frame analysis as an assistive tool. We introduce a Structured Chain-of-Thought (SCoT) prompting approach using Llama3-8B, enabling step-by-step justifications grounded in predefined framing categories. This structured design allows users to audit model outputs and examine alternative interpretations in a task that is inherently subjective. We evaluate our approach on a dataset of migration-related news and show that SCoT improves classification performance over zero-shot and few-shot baselines while remaining feasible on a single GPU. Then, we conduct a human-centered evaluation in which annotators assess the coherence and influence of "the model's reasoning". Results indicate that SCoT explanations are generally perceived as logical (mean score 4.1/5, though with notable variation across texts) and can prompt reflection on initial interpretations, even when disagreement persists. Our findings highlight both the potential and risks of LLM-assisted frame analysis. While structured reasoning can increase the traceability of model outputs and support critical interpretation, it can also influence human judgment in subtle ways. By enabling local deployment and emphasizing human-in-the-loop interaction, this work contributes to discussions on responsible and accessible computational tools for the study of socially impactful media narratives.

---


### 154. [Tool-Aware Optimization with Entropy Guidance for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.03762)

**<font color=#1a73e8>作者：</font>** Hongye Cao, Nuo Yan, Haoyuan Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Agentic reinforcement learning (RL) equips large language models (LLMs) with tool-use capabilities that substantially improve reasoning on complex tasks. However, integrating external tools often destabilizes training: over-reliance on tools can induce input distribution shift, while overly conservative tool use limits effective exploration. To address this issue, we propose a unified framework TAO-RL that couples tool-aware trajectory filtering with entropy-guided exploration for efficient policy optimization. Specifically, at the data level, TAO-RL filters rollout trajectories along two criteria: discarding those where all tool invocations fail to execute, and removing those where all rollouts are either correct or incorrect, as both cases yield degenerate advantage estimates that contribute no discriminative learning signal. This joint filtering retains data that are both tool-capable and informative, establishing a high-quality training distribution. At the algorithmic level, we introduce a tool-aware entropy-guided bonus that reshapes the advantage function at post-tool-call tokens, encouraging the policy to explore more diverse reasoning paths at critical decision points. These two components are mutually reinforcing: trajectory filtering establishes a clean and informative training foundation, while entropy-guided exploration drives stronger reasoning behaviors at critical tool-interaction junctures. Extensive experiments on 7 challenging reasoning benchmarks across 3 model scales demonstrate the superiority of TAO-RL over existing methods.

---


### 155. [Expert-Aware Causal Tracing of Factual Recall in Sparse MoE Language Models](https://arxiv.org/abs/2606.03780)

**<font color=#1a73e8>作者：</font>** Yuetian Lu, Ali Modarressi, Yihong Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Causal tracing of factual recall has been studied predominantly in dense transformer language models, where interventions localize information flow to layers or feed-forward modules. Sparse mixture-of-experts (MoE) language models introduce a sharper question: when a factual prediction is mediated by a routed MoE block, which routed expert contributions matter? We formulate expert-aware causal tracing for sparse MoE language models. Using CounterFact facts, we first corrupt the model's factual preference by adding noise to subject-token embeddings, and then test whether clean MoE-block outputs or clean expert-level updates restore the true-vs-foil logit contrast. For Qwen3-30B-A3B-Base, a layer sweep selects and validates layer 44, and expert-level tracing identifies L44E069 as an expert repeatedly selected in the clean run whose held-out patch outperforms other active same-layer expert patches. For Mixtral-8x7B-v0.1, layer-level tracing validates a mid-layer signal, but the signal is not localized to the selected singleton expert; a coalition check instead recovers it with routed multi-expert updates. These results suggest that MoE factual tracing can be made expert-aware, while also showing that expert-level localization is model- and protocol-dependent rather than universal.

---


### 156. [Reasoning over Grammar: Can Synthetic Linguistic Reasoning Traces Enhance Low-Resource Machine Translation?](https://arxiv.org/abs/2606.03782)

**<font color=#1a73e8>作者：</font>** Renhao Pei, Yihong Liu, Sampo Pyysalo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) offer a promising approach to machine translation (MT) for extremely low-resource languages by incorporating linguistic resources through in-context learning. However, LLMs often struggle to apply grammatical information effectively during translation. Inspired by recent progress in chain-of-thought reasoning, we investigate whether low-resource MT can benefit from structured intermediate steps of linguistic analysis and grammatical reasoning. We propose a pipeline for automatically generating step-by-step linguistic reasoning traces from Universal Dependencies treebanks, dictionaries, and grammar-rule banks. We evaluate these traces in three settings: in-context learning (ICL), supervised fine-tuning (SFT), and reinforcement fine-tuning (RFT), on Xibe and Chintang as test cases. Our results show that linguistic reasoning traces are most effective as inference-time guidance: in ICL, reliable sentence-specific traces substantially improve translation performance across most models, languages, and metrics. In contrast, using the linguistic reasoning traces as training data yields smaller and less consistent gains, as models learn the trace format but often generate erroneous content. These findings suggest that LLMs can leverage grammatical information for low-resource MT when given reliable linguistic analyses, while learning to generate such analyses remains a major bottleneck.

---


### 157. [Backdoor Unlearning Generalization: A Path Toward the Removal of Unknown Triggers in LLMs](https://arxiv.org/abs/2606.03785)

**<font color=#1a73e8>作者：</font>** Lisa Bouger, Théo Lasnier, Philippe Looubet Moundi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Backdoor attacks in Large Language Models (LLMs) are a growing security concern, where models can generate adversary-chosen content. Existing defenses target backdoors one at a time and typically require knowledge of the trigger, leaving the defender at a structural disadvantage when unknown backdoors may exist in a model. We show that backdoor neutralization through unlearning generalizes across backdoors: training a model to ignore a single trigger can also suppress other backdoors that were never explicitly targeted. We study this phenomenon across three model families, whose backdoors were injected via pretraining or continual pretraining, by analyzing the models obtained after removing one backdoor at a time. To understand why unlearning certain backdoors induces the suppression of others, we introduce the Cross Activation Shift Distance, to quantify the distance between model changes induced by different trainings. Our results open a new direction for LLM safety as defenders could deliberately inject controlled backdoors and then remove them, leveraging cross-backdoor transfer to also suppress unknown backdoors that an attacker may have previously introduced in the model.

---


### 158. [SLU-2K: A Question-Based Benchmark for Semantic Evaluation of Sign Language Translation](https://arxiv.org/abs/2606.03788)

**<font color=#1a73e8>作者：</font>** Zeno Testa, Antonino Furnari, Lorenzo Baraldi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign Language Translation (SLT) is typically evaluated with surface-form metrics such as BLEU and ROUGE, which reward lexical overlap but do not directly measure whether a translation preserves the meaning of the source sign sequence. This is in contrast with the final objective of integrating SLT in assistive technology. In this work, we shift the focus from Sign Language Translation (SLT) to Sign Language Understanding (SLU), with particular emphasis on semantic understanding. Specifically, we evaluate systems based on their ability to correctly recover, from the input video, key semantic aspects of the original sentence, such as actions taking place and facts about people and objects. To enable this evaluation systematically, we propose SLU-2K, a dataset of 2,350 closed-ended video question-answer pairs based on the popular PHOENIX-2014T and CSL-Daily datasets. To obtain SLU-2K, we propose and extensively evaluate an automated data generation pipeline which produces questions across 7 categories, namely actions, locations, numbers, objects, people, time, and weather conditions. We show the potential of SLU-2K by evaluating popular Multimodal Large Language Models (MLLMs) and two representative state-of-the-art systems, MMSTL and SpaMo. Our results show that MLLMs reach near-random performance, highlighting the need for a more systematic integration of SLU in current AI systems. Furthermore, state-of-the-art translation systems carefully fine-tuned on in-domain data still exhibit a substantial semantic gap, with results ranging from 56.7% to 75.2%. These findings suggest that current SLT evaluation protocols overestimate true understanding and that future progress should be measured not only by fluency and n-gram overlap, but also by semantic correctness. Code, prompts, and benchmark files are available at this https URL

---


### 159. [Training-Free Multi-Concept LoRA Composition with Prompt-Aware Weighting](https://arxiv.org/abs/2606.03792)

**<font color=#1a73e8>作者：</font>** Georgios Tsoumplekas, Stella Bounareli, Vasileios Argyriou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) successfully enables personalization in text-to-image generation by adapting pre-trained diffusion models to specific visual concepts and styles. However, extending such models to multi-concept customization remains challenging. Naively combining multiple LoRA weights or their outputs often leads to interference among concepts, resulting in degraded visual quality and reduced fidelity to the reference images of individual concepts. This paper proposes a simple yet effective approach for multi-concept customization by optimally combining the outputs of multiple LoRA modules. We leverage the relative importance of each concept during generation, as inferred from its corresponding prompt tokens and introduce two methods, W-Switch and W-Composite, that employ a prompt-aware importance weighting strategy in which each LoRA is weighted according to the semantic influence of its trigger words in the target prompt. In addition, we extend existing quantitative evaluation metrics by proposing a new image-based similarity evaluation framework that assesses image fidelity and identity preservation through comparisons between real-world reference images and automatically segmented concept regions from generated images. We evaluate our approach on the ComposLoRA testbed and demonstrate consistent improvements over existing state-of-the-art methods in terms of visual quality, identity preservation and compositionality. Qualitative evaluations, including a Large Language Model (LLM) based assessment and a user study, further validate the effectiveness of the proposed methods and align with the newly introduced quantitative image-based metrics. Our code is available at this https URL.

---


### 160. [Exploring Adversarial Robustness and Safety Alignment in Multilingual Multi-Modal Large Language Models](https://arxiv.org/abs/2606.03793)

**<font color=#1a73e8>作者：</font>** Hashmat Shadab Malik, Muzammal Naseer, Salman Khan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models integrate visual perception into language reasoning, introducing a continuous attack surface susceptible to adversarial attacks. Prior work on MLLM robustness has focused largely on English-centric tasks, leaving multilingual behaviour unexplored. We address this gap through a systematic study of adversarial robustness and multimodal safety across 12 diverse languages, evaluating open-source MLLMs that acquire multilingual capability through instruction tuning. Gradient-based attacks reveal a transferable multilingual vulnerability: adversarial images optimized in one language continue to induce failure in others, demonstrating strong cross-lingual transferability. Multilingual safety further varies with how effectively a model retrieves or interprets harmful instructions. When harmful intent is issued through text, languages with stronger linguistic grounding more often elicit misuse-enabling responses, while weaker languages produce fewer unsafe outputs. When embedded in the image as typographic content, English scripts are reliably recognised and followed, whereas non-English scripts are rarely parsed by the vision encoder. Lower-resource languages may therefore appear safer, but this is an artefact of comprehension and visual-grounding failures rather than genuine alignment, a phenomenon we term safety-by-failure. In contrast, MLLMs that build multilingual capability throughout their training stages rather than only at instruction tuning, such as Qwen3-VL, exhibit genuine cross-lingual safety, maintaining active refusal across languages rather than masking comprehension failure. Shallow multilingual adaptation, such as fine-tuning on translated instruction data, may produce surface-level understanding that creates illusory safety in low-resource languages; deeper integration across training stages leads to genuine multilingual safety alignment.

---


### 161. [Enhancing Operational Safety via Agentic Dialogue Hazard Identification Analysis](https://arxiv.org/abs/2606.03812)

**<font color=#1a73e8>作者：</font>** Sanjay Das, Ran Elgedawy, Ethan Seefried 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Operational safety in high-stakes domains such as industrial process control, autonomous, and safety-critical systems, demand reliable hazard identification. While large language models (LLMs) have shown promise in automating safety analysis tasks, single-turn, monolithic inference is brittle: it lacks the self-correction, deliberation, and contextual refinement that safety engineers apply iteratively. In this paper, we introduce HAZDIAL, a framework that investigates whether structured agentic dialogue-multi-agent, multi-turn interactions improves the quality of NLP- based hazard identification over single-pass baselines. We systematically compare two dialogue modalities: adversarial debate and constructive discussion, and propose an algorithm-based agentic interaction optimization. We evaluate all configurations against a curated golden dataset using standard classification metrics (accuracy, precision, recall, F1) and novel dialogue metrics. This work advances the intersection of dialogue systems, multi-agent reasoning, and AI safety, providing an empirical evidence for dialogue-driven hazard analysis.

---


### 162. [Leveraging BART to Assess CS1 C++ Programming Assignments using Rubric-based Criteria](https://arxiv.org/abs/2606.03814)

**<font color=#1a73e8>作者：</font>** Kelsey Rainey, Jesse Roberts  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper investigates rubric-aware, multitask fine-tuning of transformer models for automated grading of introductory C++ programming assignments, with the goal of producing grade predictions that better reflect instructor grading behavior than general-purpose LLMs. Using multi-semester CS1 data, student submissions are paired with numeric scores, letter-grade buckets, and assignment rubrics, then preprocessed into unified sequences for transformer input. A BART encoder-decoder with LoRA adaptation is trained to jointly predict numeric grades and grade buckets, augmented with a distribution-matching term to align predicted and empirical grade distributions, an evaluation dimension often overlooked in prior work. Experiments compare single-task and multitask training, hard one-hot versus fuzzy and boundary-based soft labels, and rubric versus no-rubric conditions, with additional T5 and pairwise-pretrained variants. Results show that multitask BART with boundary-based soft labels and rubric context achieves lower mean absolute error and stronger grade-distribution alignment than single-task, hard-label, or code-only baselines. Fully fine-tuned T5 further improves distributional fidelity, while pairwise pretraining reduces numeric error at the cost of minority-class sensitivity. Collectively, the findings suggest that calibration-aware, rubric-guided training produces more instructor-like grading behavior than accuracy-optimized alternatives.

---


### 163. [EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management](https://arxiv.org/abs/2606.03841)

**<font color=#1a73e8>作者：</font>** Zherui Yang, Fan Liu, Yansong Ning 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent progress in Large Language Model (LLM) agents has enabled promising advances in automated data science. However, existing approaches remain fundamentally limited by their static action sets and lack of principled long-horizon context management, hindering their ability to accumulate reusable experience across tasks and operate reliably in multi-stage, iterative data science pipelines. To address these challenges, we introduce EvoDS, a self-evolving autonomous data science agent that learns to expand its skills and adaptively managing long-term context through agentic reinforcement learning. Specifically, EvoDS introduces two key strategies: (1) Autonomous Skill Acquisition (ASA) mechanism, which enables agents to synthesize, validate, and reuse executable skills; and (2) Adaptive Context Compression (ACC) strategy, which treats context management as a learned control problem rather than passive truncation. These strategies are orchestrated within a two-stage multi-agent training scheme, enabling EvoDS to autonomously improve over time. Theoretically, we prove that EvoDS's hierarchical design reduces tool-selection error, and its optimization objective aligns with an information bottleneck principle, ensuring efficient context use. Empirically, EvoDS outperforms state-of-the-art open-source data science agents by an average of 28.9% across four diverse benchmarks while eliminating out-of-token failures. Our code and data are available at this https URL.

---


### 164. [Clustered Self-Assessment: A Simple yet Effective Method for Uncertainty Quantification in Large Language Models](https://arxiv.org/abs/2606.03846)

**<font color=#1a73e8>作者：</font>** Qi Cao, Takeshi Kojima, Andrew Gambardella 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate remarkable performance across diverse tasks, but they often generate responses that appear plausible while being factually incorrect. This problem is compounded by the lack of explicit uncertainty estimates, which makes it difficult for users to judge the reliability of model outputs. Existing uncertainty quantification methods typically rely on indirect signals, such as entropy across sampled generations. These signals can be difficult to interpret and do not fully leverage the model's ability to assess its own uncertainty. We propose a simple yet effective self-assessment method for uncertainty quantification in LLMs. Our approach groups sampled generations into semantically distinct clusters, converts them into answer options in a structured multiple-choice question, and uses the probability assigned by the LLM to each option as a confidence estimate. Experiments across multiple models and datasets show that our method consistently outperforms baseline approaches. Notably, it achieves competitive performance with as few as two additional samples, demonstrating both its effectiveness and efficiency.

---


### 165. [CLI-Anything: Towards Agent-Native Computer Use](https://arxiv.org/abs/2606.03854)

**<font color=#1a73e8>作者：</font>** Yuhao Yang, Tianyu Fan, Chao Huang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As large language models advance in reasoning and tool use capabilities, researchers increasingly seek to leverage them for computer use agents that can interact with existing software. The dominant approach develops GUI agents that control applications through visual interfaces: interpreting screenshots, locating UI elements, and executing mouse clicks to mimic human interaction. This GUI-centric paradigm fundamentally misaligns with agent capabilities. Current GUI agents struggle with brittle pixel-level interactions, timing dependencies, and coordinate-based actions that break with interface changes. They force agents to emulate human perceptual limitations rather than leverage their computational strengths in structured data processing and programmatic control. CLI-Anything argues for agent-native computer use design. Instead of forcing agents to navigate visual layouts, we create interfaces aligned with how agents naturally operate: through structured commands, explicit state representations, and deterministic feedback. We transform existing applications into command-line harnesses that preserve functionality while exposing machine-readable protocols optimized for AI-native interaction. This eliminates the lossy visual-to-computational translation that plagues GUI agents. Rather than building sophisticated screen readers and click simulators, we should redesign interaction paradigms around agent strengths: precise programmatic control and deterministic execution. We examine the methodology, architecture, evidence, and future directions for this agent-native transformation of computer use. We have built CLI-Hub as a comprehensive platform that operationalizes this agent-native computer use vision. The platform provides methodology, architecture, and infrastructure for this fundamental transformation of computer use.

---


### 166. [PyraMathBench: Evaluating and Improving Mathematical Capability in Large Language Models](https://arxiv.org/abs/2606.03858)

**<font color=#1a73e8>作者：</font>** Zetian Ouyang, Linlin Wang, Gerard de Melo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the pivotal role of numerical reasoning as the cornerstone of mathematical capabilities in large language models (LLMs) across applications, few benchmarks evaluate LLMs by integrating numerical processing and mathematical reasoning, hindering the interpretability of failures in math tasks. We introduce PyraMathBench, a comprehensive hierarchical benchmark with 32,505 questions derived from 7,404 math word problems, spanning 4 key cognitive aspects, 14 subcategories, and 2 modalities. Experiments reveal that LLMs' performance is severely compromised by inadequate numerical computation and weak handling of abstract numerical questions. To address this, we propose the Smart Optimization & Learning-based VErsatile module (SOLVE) and Interactive Relative Policy Optimization (IRPO), which enhance LLMs' numerical-mathematical synergy via efficient tool calls (fuzzy matching and low-quality call rejection). Comparative experiments show Qwen-2.5 achieves a 5.0 score improvement with SOLVE and IRPO training.

---


### 167. [A Training-Free Mixture-of-Agents Framework for Multi-Document Summarization using LLMs and Knowledge Graphs](https://arxiv.org/abs/2606.03867)

**<font color=#1a73e8>作者：</font>** Cuong Vuong Tuan, Trang Mai Xuan, Tien-Cuong Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-Document Summarization (MDS) plays a critical role in distilling essential information from collections of textual data. Existing approaches often struggle to capture complex inter-document relationships, rely heavily on large amounts of labeled data for supervised training, or exhibit limited generalization across domains and languages. To address these limitations, we present a training-free mixture-of-agents framework for MDS that leverages the complementary strengths of large language models (LLMs) and knowledge graphs. Our approach decomposes summarization into specialized agent tasks: extractive selection, knowledge-aware abstraction, and iterative refinement, each operating without task-specific fine-tuning. We unify their outputs using a multi-perspective consistency mechanism guided by LLMs. Experiments across four datasets in English and Vietnamese demonstrate state-of-the-art or competitive performance, validating the effectiveness and adaptability of our modular design.

---


### 168. [Visual Instruction Tuning Aligns Modalities through Abstraction](https://arxiv.org/abs/2606.03871)

**<font color=#1a73e8>作者：</font>** Luis Palacios, Lorenzo Basile, Diego Doimo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual instruction tuning effectively adapts a pre-trained Large Language Model (LLM) to process image information alongside text. Yet, it remains unclear how visual features are embedded into the layer-wise hierarchy of abstractions of the LLM backbone. Across a diverse set of vision-language architectures, we show that instruction tuning primarily serves as a bridge, embedding visual features directly into the intermediate semantic layers of the LLM, bypassing the early layers devoted to unimodal processing. With probing analyses and causal interventions, we show that these intermediate layers are the semantic core of vision-language processing and play a critical role in the performance on a broad set of multimodal benchmarks. In addition, by comparing the geometry of semantically equivalent visual and textual representations, we find that fine-tuning extends and strengthens the existing abstraction phase, aligning visual features with pre-existing textual ones. Finally, we confirm the functional role of this localized alignment by restricting fine-tuning to intermediate layers alone: this strategy preserves the performance of full fine-tuning on vision-centric benchmarks while reducing training time. Our results suggest that multimodal integration is a localized phenomenon driven by the repurposing of the internal abstraction engine of the LLM.

---


### 169. [From 'What' to 'How' and 'Why': Sharing LLM-Generated Retrospective Summaries of Older Adults' Passive Tracking Data with Remote Family Members](https://arxiv.org/abs/2606.03876)

**<font color=#1a73e8>作者：</font>** Jiachen Li, Reina Szeyi Chan, Akshat Choube 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> With the growing prevalence of modern ubiquitous computing technologies, multi-modal tracking systems hold promise for providing timely awareness and reassurance to stakeholders such as remote family members (RFMs) of older adults, who play a central role in care coordination. However, combining heterogeneous data streams into high-level, meaningful content - such as retrospective summaries - remains challenging. While recent work has demonstrated the promise of large language models (LLMs) for interpreting multi-modal tracking data, less attention has been given to generating narrative accounts for stakeholders like RFMs, who possess rich personal knowledge of older adults and strong emotional responsibility, yet have limited visibility into their daily lives and limited capacity for caregiving. In this work, we explore how LLMs can be used to generate retrospective summaries from multi-modal tracking data for RFMs of older adults. We leveraged and customized an existing system, Vital Insight, to generate initial summaries on different dates and data availability scenarios as technology probes, and conducted interviews with 11 RFMs to gather feedback. Based on these insights, we redesigned the system into a multi-layer, multi-agent, insight-driven summary approach that builds from objective statistics and descriptions to enriched, context-aware narratives. We then compared the redesigned summaries with the initial versions through a survey with the same 11 RFMs and found significant improvements in satisfaction, perceived helpfulness, trust, and willingness to receive the summaries. We conclude by presenting design implications for AI-generated summaries for RFMs and broader contexts, emphasizing the need to support RFMs' sensemaking shift from simply presenting ''What'' data were collected, to explaining ''How'' is my loved one doing and ''Why''.

---


### 170. [Beyond Encoder Accumulation: Measuring Encoder Roles in Multi-Encoder VLMs](https://arxiv.org/abs/2606.03879)

**<font color=#1a73e8>作者：</font>** Wei Ding, Yudong Zhang, Ruobing Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As foundation models scale toward fusing more heterogeneous visual streams, understanding how diverse encoders interact under joint training becomes a prerequisite for principled design. Yet large vision-language models (LVLMs) currently lack the tools to do so, and parameter-efficient encoder configurations remain hard to identify before training. To re-examine encoder roles under joint training, on the 16-benchmark Cambrian-1 suite we retrain and evaluate all 31 non-empty subsets of five common vision encoders under a unified pipeline (~20k GPU-hours total), and report three findings. First, retraining each subset from scratch reveals encoder rankings that differ from those obtained by masking encoders on a fixed checkpoint, including which encoder ranks first overall. Second, we decompose each encoder's contribution into two axes, Capacity, the score an encoder reaches on its own, and Necessity, the drop when it is removed from the full pool. The two axes are not interchangeable. Pairing the two highest-Capacity encoders is suboptimal, while pairing a high-Capacity anchor with an adaptive complement matches the full five-encoder model. Adding further encoders beyond this pair yields only marginal gains. Third, at fixed parameter count, per-encoder pre-projector effective rank explains the residual score variation. The strongest pairs combine an anchor whose rank survives joint training with a complement whose rank expands under it, suggesting that higher-rank, less-collapsed projector inputs correspond to a more favorable optimization regime at the encoder-projector interface. Together, the Capacity-Necessity decomposition and the pre-projector rank analysis, along with comprehensive evaluation through retraining, expose a methodological gap in multi-encoder LVLM design, and offer concrete primitives for closing it.

---


### 171. [Reasoning Structure of Large Language Models](https://arxiv.org/abs/2606.03883)

**<font color=#1a73e8>作者：</font>** Frédéric Berdoz, Luca A. Lanzendörfer, Fabian Farestam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large reasoning models (LRMs) are often evaluated using metrics such as final-answer accuracy or token count. However, identical scores on these metrics can hide fundamentally different reasoning structures. To address this limitation, we introduce a scalable LRM benchmark of logic puzzles and a pipeline that converts unstructured traces into verifiable reasoning graphs of claims and dependencies. This turns reasoning into a structured, measurable object whose topology can be quantitatively analyzed. Building on this, we define a reasoning efficiency metric that quantifies how concentrated the model's logical flow is. Our analysis on open-source reasoning models shows that structural measurements separate behaviors that token count and accuracy conflate, providing a practical tool for diagnosing failure modes and comparing how reasoning scales with puzzle difficulty.

---


### 172. [CoralBay: A Self-Supervised CT Foundation Model](https://arxiv.org/abs/2606.03888)

**<font color=#1a73e8>作者：</font>** Ioannis Gatopoulos, Nicolas Känzig, Sebastian Otálora 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning has enabled large-scale pre-training on 2D natural images, producing general-purpose visual representations that transfer effectively across tasks. However, many medical imaging modalities, such as CT scans, are inherently three-dimensional and differ fundamentally from natural images in both structure and semantics. Volumetric modalities capture spatial continuity, organ anatomy, and intensity-based tissue properties (e.g., Hounsfield Units), which are not adequately modeled by 2D pre-training. To bridge this gap, we introduce CoralBay, a self-distillation framework that extends DINO by using a hierarchical 3D Swin backbone and applying self-distillation to concatenated multi-scale features, enabling data-efficient self-supervised learning of rich spatial representations that encode both global semantics and fine-grained local structure. As a result, CoralBay transfers effectively to a wide range of downstream radiological tasks, demonstrating strong and consistent performance across diverse anatomical targets. In addition, we contribute to the open-source \eva framework by introducing a public, reproducible 3D radiology leaderboard that unifies multiple datasets and establishes a standardized benchmark for evaluating volumetric representation learning methods.

---


### 173. [OVO-S-Bench: A Hierarchical Benchmark for Streaming Spatial Intelligence in Multimodal LLMs](https://arxiv.org/abs/2606.03890)

**<font color=#1a73e8>作者：</font>** Yifei Li, Pengyiang Liu, Yuhang Zang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal agents in robotics, AR, and autonomous driving must reason about places and layouts from continuous egocentric streams, often using evidence outside the current view. Existing benchmarks either evaluate offline over full videos or target events rather than spatial structure. We introduce OVO-S-Bench, a fully human-annotated benchmark for streaming spatial intelligence, comprising 1,680 questions over 348 source videos. Annotation involves 12 trained annotators, each also serving as a blind cross-reviewer, across roughly 804 person-hours of multi-round quality assurance. Each question carries a query timestamp and an evidence interval, and at evaluation, the model sees only the prefix preceding the query. Questions span four levels of increasing abstraction: instantaneous egocentric perception, spatiotemporal context tracking, spatial simulation and reasoning, and allocentric mapping. Across 38 proprietary and open-source MLLMs, Gemini-3.1-Pro trails human experts by 27 points, 59.2 vs. 86.6, with allocentric mapping as the dominant bottleneck. Notably, streaming and spatially fine-tuned MLLMs underperform their own backbones. We further find that chain-of-thought reasoning amplifies spatial errors when ungrounded in the stream. By exposing these limitations, OVO-S-Bench establishes a demanding testbed for next-generation streaming spatial MLLMs.

---


### 174. [Synthesize and Reward -- Reinforcement Learning for Multi-Step Tool Use in Live Environments](https://arxiv.org/abs/2606.03892)

**<font color=#1a73e8>作者：</font>** Ibrahim Abdelaziz, Asim Munawar, Kinjal Basu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Training LLMs to orchestrate multi-step tool calls is held back by three coupled obstacles: realistic stateful execution environments are costly to build, synthetic training queries are often detached from the server's actual state (so the generated tool calls fail to execute), and recall-based RL rewards incentivize verbose tool-calling patterns. We present PROVE (Programmatic Rewards On Verified Environments), a framework with three contributions: (1) a library of 20 stateful MCP (Model Context Protocol) servers exposing 343 tools, enabling live-execution RL training with session-scoped state isolation; (2) an automated data synthesis pipeline that generates validated multi-turn tool-call trajectories against these servers via dependency-graph-guided conversation simulation grounded in live-sampled server state, so every generated query references entities that actually exist; and (3) a multi-component programmatic reward - graduated validity scoring, dependency-aware coverage, an adaptive efficiency penalty with a complexity-scaled call budget, a tool-name signal, and an argument-value matching bonus - requiring no external judge model. We train four models (Qwen3-4B, Qwen3-8B, Qwen2.5-7B, Granite-4.1-8B) with GRPO using identical reward hyperparameters and ~13K training examples; only learning rate is tuned per model family from a three-point sweep. On BFCL Multi-Turn, tau2-bench, and T-Eval, PROVE yields improvements of up to +10.2, +6.8, and +6.5 points respectively, demonstrating that a compact programmatic reward yields consistent gains on multi-step tool orchestration across two model families.

---


### 175. [Denoise First, Orthogonalize Later: Understanding Momentum in Muon via Spectral Filtering](https://arxiv.org/abs/2606.03899)

**<font color=#1a73e8>作者：</font>** Xianliang Li, Zihan Zhang, Weiyang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has recently demonstrated strong empirical performance in large language model training, but the theoretical role of momentum in Muon remains unclear. Existing analyses of Muon either remove momentum to study spectral updates in isolation, or retain momentum without explaining why it improves empirical performance. Our work bridges this gap by showing momentum in Muon acts as a spectral filter. Under a structured signal-plus-perturbation gradient model, we prove that momentum suppresses perturbations while preserving the dominant signal, thereby enlarging the spectral gap between them. This enlarged gap stabilizes the singular subspaces of the matrix passed to Muon's orthogonalization step, making the resulting update more reliable. We further show that applying momentum before orthogonalization achieves provably stronger alignment with the signal component of the gradient than either reversing this order or simply removing momentum. Experiments across diverse tasks, including LLM pretraining, support our theoretical analysis. More broadly, our theory offers a starting point for understanding the benefits of momentum in other matrix-based optimizers.

---


### 176. [Benchmarking Visual State Tracking in Multimodal Video Understanding](https://arxiv.org/abs/2606.03920)

**<font color=#1a73e8>作者：</font>** Sihyun Yu, Nanye Ma, Pinzhi Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding a video requires more than recognizing isolated moments, as humans continuously track entities, states, and events over time. This capacity for visual state tracking is fundamental to video understanding, yet remains underexplored in current evaluations of Multimodal Large Language Models (MLLMs). We introduce Visual STAte Tracking benchmark (VSTAT), a video-based benchmark designed to diagnose visual state tracking in MLLMs. VSTAT consists of 834 clips drawn from both synthetic and real-world videos, paired with 1,500 questions that cannot be answered from any single frame or short segment, requiring continuous perception and integration of events across the entire video stream. Despite their strong performance on existing video benchmarks, we find that state-of-the-art MLLMs perform far below humans and only modestly above answer-prior baselines. To analyze this gap, we compare MLLMs' thinking traces with the underlying video stream to understand why and when MLLMs fail on VSTAT. We find that MLLMs reason and track correctly in text, but fail at visually perceiving the events they need to track. Finally, our preliminary evaluation suggests that recent agentic approaches, including MLLM-based video agents and coding agents, do not readily resolve these failures, still falling short on VSTAT.

---


### 177. [Knowledge Editing in Masked Diffusion Language Models](https://arxiv.org/abs/2606.03924)

**<font color=#1a73e8>作者：</font>** Haewon Park, Yohan Jo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge editing aims to update or correct factual knowledge in a language model. A widely used approach, locate-then-edit, does this in two steps: it first localizes a fact within the model, then edits the weights there. To date, such methods have been developed exclusively on autoregressive models (ARMs). Whether their underlying assumptions hold for masked diffusion models (MDMs), which model text bidirectionally and generate by iterative denoising rather than next-token prediction, remains an open question. We address it by transferring locate-then-edit to MDMs and comparing two MDMs (LLaDA, Dream) with two ARMs (LLaMA, Qwen) at matched scale. Our central finding has two parts. First, where an edit is applied transfers across paradigms: causal tracing highlights the same early-to-mid-layer MLP at the last subject token in both, and editing is most effective there. Second, this shared location does not guarantee a shared outcome. Single-token edits succeed in both, but as targets grow longer, editing degrades systematically in the MDMs but not the ARMs. The failure stems from how the edited fact is generated: producing a multi-token target requires passing through partially unmasked intermediate states for which the edit was never optimized. Guided by this diagnosis, we introduce a simple correction that optimizes the edit for these states, substantially restoring multi-token performance.

---


### 178. [Adaptive Causal Alignment for High-Confidence Adversarial Training](https://arxiv.org/abs/2606.03925)

**<font color=#1a73e8>作者：</font>** Zhiming Luo, Kejia Zhang, Yingxin Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inverse adversarial training leverages high-confidence predictions to stabilize robust learning, yet we uncover a critical paradox: high confidence often stems from overfitting to non-causal background correlations rather than intrinsic object semantics. Our investigation reveals that visual context functions as a dual-natured signal, serving as either a necessary supportive prior or a spurious confounder. This insight renders existing blind suppression strategies flawed, as they inevitably lead to severe Feature Loss. To resolve this, we propose High-Confidence Causally Aligned Training (HICAT), a unified framework that establishes a Semantic Equilibrium. Operating on a ``Measure-Debias-Align'' pipeline, HICAT integrates a Learnable Background-Bias Estimator (LBBE) to adaptively diagnose context utility. Guided by this diagnosis, an Adaptive Debiasing mechanism performs surgical logit rectification, complemented by a geometrically grounded Foreground Logit Orthogonal Enhancement (FLOE) loss to enforce rigorous feature disentanglement. Extensive experiments on CIFAR-10, CIFAR-100, and ImageNet-1K demonstrate that HICAT consistently improves over matched baselines across diverse architectures (CNNs and ViTs) while significantly reducing the robust generalization gap.

---


### 179. [Value-Aware Stochastic KV Cache Eviction for Reasoning Models](https://arxiv.org/abs/2606.03928)

**<font color=#1a73e8>作者：</font>** Ting-Yun Chang, Harvey Yiyun Fu, Deqing Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models improve accuracy through extended chains of thought, but their long outputs create a memory and compute bottleneck. KV cache eviction methods reduce this cost by evicting unimportant key-value pairs from the cache, yet they often yield worse accuracy than selection-based sparse attention alternatives, which keep the full KV cache. We identify key factors crucial to KV cache eviction accuracy. First, a small fraction of value states have abnormally large magnitudes, and evicting them causes catastrophic failure where models enter repetitive reasoning loops. Second, introducing stochasticity during eviction improves accuracy by increasing cache diversity. Based on these findings, we propose Value-aware Stochastic KV Cache Eviction (VaSE), a training-free recipe that protects large-magnitude value states and promotes diverse eviction decisions. Across six reasoning tasks, Qwen3 models using VaSE with 4x KV cache compression yield higher average accuracies than SOTA selection method at the same sparsity, while outperforming the strongest eviction method by more than 4%. Overall, VaSE bridges the gap between efficiency and accuracy, supporting FlashAttention2 and enabling a static memory footprint for reasoning models.

---


### 180. [Demo2Tutorial: From Human Experience to Multimodal Software Tutorials](https://arxiv.org/abs/2606.03951)

**<font color=#1a73e8>作者：</font>** Zechen Bai, Zhiheng Chen, Yiqi Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human experience in digital environments offers a vast, underexplored resource of authentic, untrimmed interactions that contain rich procedural knowledge. We introduce Demo2Tutorial, a framework that transforms this experience captured via screen recordings and interaction logs into structured, multimodal software tutorials for teaching both humans and agents. Demo2Tutorial first collects human experience via a dedicated recorder, then parses raw experience using a multimodal Action Parser to reconstruct perception, action, and intent. A Step Planner then abstracts these steps into hierarchical task graphs representing goals and steps. Finally, a Tutorial Composer transforms the parsed experience into structured, reusable image-text instructions. We evaluate the tutorial generation quality on a new benchmark derived from official software documentation. We further demonstrate that this distilled representation benefits (i) human learning, by automatically generating multimodal tutorials, and (ii) agent learning, by improving downstream GUI-agent planning and generalization. Experiments show Demo2Tutorial produces high-quality tutorials that surpass human-authored ones and significantly outperform baseline methods, while enabling both faster human task completion and improved GUI agent planning, demonstrating that structured tutorials distilled from human experience can serve as effective knowledge representations for advancing both human learning and agent capabilities. Code and data will be available at this https URL.

---


### 181. [Agentic Chain-of-Thought Steering for Efficient and Controllable LLM Reasoning](https://arxiv.org/abs/2606.03965)

**<font color=#1a73e8>作者：</font>** Yu Xia, Zhouhang Xie, Xin Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models improve final-answer accuracy through extended chain-of-thought reasoning, but often spend tokens inefficiently and offer little inference-time control. Existing efficient reasoning methods control thinking length by shortening, early-stopping, or compressing traces, leaving how the model thinks implicit. In this paper, we propose Agentic Chain-of-Thought Steering (ACTS), which formulates reasoning steering as a Markov decision process where a controller agent adaptively steers a frozen reasoner during inference. At each step, the controller observes the reasoning trace and remaining thinking budget, then issues a steering action consisting of a reasoning strategy and a steering phrase that initiates the next reasoner step. This enables budget-aware strategy control for efficient reasoning while preserving the reasoner's generation continuity. We initialize the controller agent from our constructed synthetic steering trajectories with multi-budget augmentation, and further optimize it via reinforcement learning with budget-conditioned reward shaping. Experiments across multiple benchmarks show that ACTS matches full-thinking performance with substantial token savings, and enables controllable accuracy-efficiency trade-offs across different reasoners and tasks. The code is available at this https URL.

---


### 182. [AlignAtt4LLM: Fast AlignAtt for Decoder-Only LLMs at IWSLT 2026 Simultaneous Speech Translation Task](https://arxiv.org/abs/2606.03967)

**<font color=#1a73e8>作者：</font>** Quentin Fuxa, Dominik Macháček  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe AlignAtt4LLM, an IWSLT 2026 simultaneous speech translation system for English to German, Italian, and Chinese. The system is a synchronous cascade: Qwen3-ASR with forced alignment produces an incrementally updated source transcript, and Gemma-4 E4B-it translates that prefix under an MT-side AlignAtt policy.
To our knowledge, this is the first application of AlignAtt to a decoder-only LLM, where the encoder-decoder cross-attention used by earlier AlignAtt systems is absent. We recover a usable policy by proposing (1) an explicit source span in the prompt, (2) offline selection of translation-specific alignment heads, (3) selective qk-fast replay of the draft-to-source attention block, and (4) runtime query/key capture that preserves model outputs bit-identically.
On the IWSLT 2026 development set, AlignAtt4LLM outperforms the supplied baselines for the European target languages, English to German and English to Italian, in both the low-latency regime around 2 seconds and the high-latency regime below 4 seconds CU-LongYAAL. Results for English to Chinese are more mixed, but the method is not tied to Gemma-4: because AlignAtt4LLM only requires a deterministic prompt layout, calibrated attention heads, and query/key capture, the same policy can be reapplied to stronger translation-focused decoder-only MT backbones for non-European target languages.

---


### 183. [Quantifying Faithful Confidence Expression in Large Reasoning Models](https://arxiv.org/abs/2606.03969)

**<font color=#1a73e8>作者：</font>** Areeb Gani, Asal Meskin, Gabrielle Kaili-May Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty communication is critical to the trustworthiness of LLMs, yet faithful calibration (FC)--the alignment between models' intrinsic and (linguistically) expressed confidence--is a persistent failure mode. This challenge is key for large reasoning models (LRMs), whose extended reasoning traces are often interpreted by users as evidence of deliberation, competence, and confidence. Despite the importance of FC and wide usage of LRMs, the extent to which LRMs can faithfully express their confidence remains poorly understood. Moreover, the prevailing paradigm to measure FC does not generalize well to the long chain-of-thought outputs generated by LRMs, which tend to lack clear step boundaries, involve inconsistent step structure, and encode complex conditional dependencies throughout the trace--complicating estimation of intrinsic confidence. To address this challenge, we introduce a novel framework to systematically quantify FC of LRMs. Our framework analyzes linguistic decisiveness relative to three sources of internal uncertainty, based on token probabilities, hidden states, and sampled response consistency. We also devise a prefix-conditioned sampling approach to control for conditional and structural variation across traces. Applying our framework to a diverse suite of leading models, datasets, and prompts, we find that faithful confidence expression is a significant challenge for LRMs. Reasoning behaviors do not automatically translate to improved FC, and prompt interventions for non-reasoning models do not improve faithfulness in the reasoning setting. Different confidence estimators further produce divergent assessments of the same traces, revealing fragility in prior evaluation methodologies. Taken together, our work establishes FC as a distinct reliability and alignment target for LRMs, particularly as such systems are increasingly deployed in high-stakes contexts.

---


### 184. [Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories](https://arxiv.org/abs/2606.03979)

**<font color=#1a73e8>作者：</font>** Ali Behrouz, Farnoosh Hashemi, Vahab Mirrokni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The past few decades have witnessed significant advances in the design of machine learning algorithms, from early studies on task-specific shallow models to more general deep Large Language Models (LLMs). Despite showing promising results in tasks that require instant prediction or in-context learning, existing models lack the ability to continually learn and effectively transfer their temporal in-context knowledge to their long-term parameters. Inspired by human learning process, we introduce a ''Sleep'' paradigm that allows the models to continually learn, distill their short-term fragile memories into stable long-term knowledge with replay, and recursively improve themselves with ''Dreaming'' process. In more detail, sleep consists of two stages: (1) Memory Consolidation: an upward distillation process, called Knowledge Seeding, where the memories of a smaller-self are distilled into a larger network to provide more capacity while preserving the knowledge. As a proof of concept, we present a new Generalized Distillation process for {Knowledge Seeding} (i.e., the combination of on-policy distillation with Reinforcement Learning (RL)-based imitation learning); (2) Dreaming: a self-improvement phase, where the model uses RL to generate a curriculum of synthetic data to rehearse new knowledge and refine existing capabilities without human supervision. Our experiments on long-horizon, continual learning, knowledge incorporation, and few-shot generalization tasks support the importance of the sleep stage.

---


### 185. [Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill](https://arxiv.org/abs/2606.03980)

**<font color=#1a73e8>作者：</font>** Tao Chen, Gangwei Jiang, Pengyu Cheng 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward models (RMs) provide critical feedback signals for LLM post-training, notably in reinforced fine-tuning (RFT) and reinforcement learning (RL) pipelines. However, current reward evaluation relies on heterogeneous criteria such as rule-based verifiers, ground-truth references, procedural checklists, and complex rubrics, where a unified mechanism to integrate all types of evidence remains unexplored. To this end, we propose Skill Reward Model (Skill-RM), a unified framework that reformulates reward modeling as the execution of a reusable Reward-Evaluation Skill. By treating reward computation as a structured agentic task, Skill-RM provides a consistent interface to orchestrate heterogeneous resources, dynamically selecting and aggregating evidence tailored to the specific requirements of each input. This approach enables the reward model to move beyond static evaluation, ensuring consistency and transparency across diverse tasks. Extensive experiments on reward benchmarks and downstream applications, including best-of-N selection and reinforcement learning, demonstrate that Skill-RM consistently outperforms traditional judge baselines. Our findings suggest that Skill-RM not only provides a unified solution for reward modeling but also achieves superior performance through the strategic and dynamic orchestration of evidence. The code is at this https URL.

---


### 186. [Language Models Compare Quantities Using Number-specific and Unit-specific Heuristics](https://arxiv.org/abs/2606.03982)

**<font color=#1a73e8>作者：</font>** Mutsumi Sasaki, Go kamoda, Ryosuke Takahashi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quantities with measurement units, such as 110 cm and 1.2 m, require language models (LMs) to combine a numeral with a symbolic unit scale. Here, we study how LMs compare such quantities in controlled settings spanning several unit systems. We find that accuracy degrades near the comparison boundary, where small changes in value determine the correct answer. The resulting errors are systematic: linear surrogate models predict LM preferences from numerical-difference and unit-scale-difference cues, and causal interventions on subspaces aligned with these variables shift model's output. The results suggest that LMs compare quantities through a bag of heuristics over numerals and units, rather than first converting both expressions to an exact shared-scale representation.

---


### 187. [NewtPhys: Do Foundation Models Understand Newtonian Physics?](https://arxiv.org/abs/2606.03986)

**<font color=#1a73e8>作者：</font>** Sebastian Cavada, Soumava Paul, Tuan-Hung Vu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Previous work has evaluated physics reasoning in foundation models using synthetic or semi-synthetic scenes and visual question-answering tasks. However, these benchmarks emphasize high-level events and lack the visual fidelity required to assess true low-level Newtonian understanding. We introduce NewtPhys, a 4D physically annotated dataset built from multiview images of real-world scenes with physics-grounded simulations. The dataset provides dense, fine-grained annotations across timesteps -- including 3D forces and amodal per-pixel quantities covering physics, tracking, semantics and geometry -- bridging the gap between simplistic synthetic setups and realistic visual complexity. Using NewtPhys, we systematically evaluate 56 VLMs, including 54 open-weight models and 2 closed-source frontier models, and 10 VFMs and reveal limitations in low-level physics reasoning. Beyond benchmarking, our dataset enables future research in physics-grounded vision and the development of next-generation physics-aware evaluations. Code and datasets are available at this https URL.

---


### 188. [Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models](https://arxiv.org/abs/2606.03988)

**<font color=#1a73e8>作者：</font>** Mahtab Bigverdi, Lindsey Li, Weikai Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision language models (VLMs) excel at many tasks but still struggle with spatial reasoning when critical information is not directly observable. Many such problems require imaginative perception: inferring what would be seen from an unseen viewpoint, tracing paths through occluded spaces, or integrating partial observations into a coherent spatial representation. We introduce Imaginative Perception Tokens (IPT), intermediate perceptual representations that externalize what a VLM would perceive under alternative spatial configurations while remaining consistent with the observed input.
To study this capability, we formulate three tasks, Perspective Taking (PET), Path Tracing (PT), and Multiview Counting (MVC), and construct datasets of approximately 20K examples with ground truth imaginations, answers, and evaluation benchmarks. Using the unified VLM BAGEL as the backbone, IPT supervision consistently improves spatial reasoning and often outperforms textual chain of thought training, even without generating images at inference time. On MVC, IPT improves accuracy by 3.4% and achieves competitive performance with strong closed-source models on PT. We further find that combining IPT and label-only supervision yields additional gains, whereas textual chain of thought can substantially degrade performance, suggesting a modality mismatch when spatial computation is forced through language. Overall, IPT provides a principled supervision signal for reasoning about unobserved spatial structure, improving generalization while producing interpretable intermediate representations.

---


> [!TIP]
> 当前位于：**151-188**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-188**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
