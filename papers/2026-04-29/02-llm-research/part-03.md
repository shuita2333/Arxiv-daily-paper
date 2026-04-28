# 🧠 大模型相关研究 | 2026年04月29日

> 本类共 **215** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-215](./part-05.md)

---

### 101. [ComplianceNLP: Knowledge-Graph-Augmented RAG for Multi-Framework Regulatory Gap Detection](https://arxiv.org/abs/2604.23585)

**<font color=#1a73e8>作者：</font>** Dongxin Guo, Jikun Wu, Siu Ming Yiu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Financial institutions must track over 60,000 regulatory events annually, overwhelming manual compliance teams; the industry has paid over USD 300 billion in fines and settlements since the 2008 financial crisis. We present ComplianceNLP, an end-to-end system that automatically monitors regulatory changes, extracts structured obligations, and identifies compliance gaps against institutional policies. The system integrates three components: (1) a knowledge-graph-augmented RAG pipeline grounding generations in a regulatory knowledge graph of 12,847 provisions across SEC, MiFID II, and Basel III; (2) multi-task obligation extraction combining NER, deontic classification, and cross-reference resolution over a shared LEGAL-BERT encoder; and (3) compliance gap analysis that maps obligations to internal policies with severity-aware scoring. On our benchmark, ComplianceNLP achieves 87.7 F1 on gap detection, outperforming GPT-4o+RAG by +3.5 F1, with 94.2% grounding accuracy ($r=0.83$ vs. human judgments) and 83.4 F1 under realistic end-to-end error propagation. Ablations show that knowledge-graph re-ranking contributes the largest marginal gain (+4.6 F1), confirming that structural regulatory knowledge is critical for cross-reference-heavy tasks. Domain-specific knowledge distillation (70B $\to$ 8B) combined with Medusa speculative decoding yields $2.8\times$ inference speedup; regulatory text's low entropy ($H=2.31$ bits vs. $3.87$ general text) produces 91.3% draft-token acceptance rates. In four months of parallel-run deployment processing 9,847 updates at a financial institution, the system achieved 96.0% estimated recall and 90.7% precision, with a $3.1\times$ sustained analyst efficiency gain. We report deployment lessons on trust calibration, GRC integration, and distributional shift monitoring for regulated-domain NLP.

---


### 102. [Personality Shapes Gender Bias in Persona-Conditioned LLM Narratives Across English and Hindi: An Empirical Investigation](https://arxiv.org/abs/2604.23600)

**<font color=#1a73e8>作者：</font>** Tanay Kumar, Shreya Gautam, Aman Chadha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in persona-driven applications such as education, customer service, and social platforms, where models are prompted to adopt specific personas when interacting with users. While persona conditioning can improve user experience and engagement, it also raises concerns about how personality cues may interact with gender biases and stereotypes. In this work, we present a controlled study of persona-conditioned story generation in English and Hindi, where each story portrays a working professional in India producing context-specific artifacts (e.g., lesson plans, reports, letters) under systematically varied persona gender, occupational role, and personality traits from the HEXACO and Dark Triad frameworks. Across 23,400 generated stories from six state-of-the-art LLMs, we find that personality traits are significantly associated with both the magnitude and direction of gender bias. In particular, Dark Triad personality traits are consistently associated with higher gender-stereotypical representations compared to socially desirable HEXACO traits, though these associations vary across models and languages. Our findings demonstrate that gender bias in LLMs is not static but context-dependent. This suggests that persona-conditioned systems used in real-world applications may introduce uneven representational harms, reinforcing gender stereotypes in generated educational, professional, or social content.

---


### 103. [Tandem: Riding Together with Large and Small Language Models for Efficient Reasoning](https://arxiv.org/abs/2604.23623)

**<font color=#1a73e8>作者：</font>** Zichuan Fu, Xian Wu, Guojing Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advancements in large language models (LLMs) have catalyzed the rise of reasoning-intensive inference paradigms, where models perform explicit step-by-step reasoning before generating final answers. While such approaches improve answer quality and interpretability, they incur substantial computational overhead due to the prolonged generation sequences. In this paper, we propose Tandem, a novel collaborative framework that synergizes large and small language models (LLMs and SLMs) to achieve high-quality reasoning with significantly reduced computational cost. Specifically, the LLM serves as a strategic coordinator, efficiently generating a compact set of critical reasoning insights. These insights are then used to guide a smaller, more efficient SLM in executing the full reasoning process and delivering the final response. To balance efficiency and reliability, Tandem introduces a cost-aware termination mechanism that adaptively determines when sufficient reasoning guidance has been accumulated, enabling early stopping of the LLM's generation. Experiments on mathematical reasoning and code generation benchmarks demonstrate that Tandem reduces computational costs by approximately 40% compared to standalone LLM reasoning, while achieving superior or competitive performance. Furthermore, the sufficiency classifier trained on one domain transfers effectively to others without retraining. The code is available at: this https URL.

---


### 104. [GraphPlanner: Graph Memory-Augmented Agentic Routing for Multi-Agent LLMs](https://arxiv.org/abs/2604.23626)

**<font color=#1a73e8>作者：</font>** Tao Feng, Haozhen Zhang, Zijie Lei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM routing has achieved promising results in integrating the strengths of diverse models while balancing efficiency and performance. However, to support more realistic and challenging applications, routing must extend into agentic LLM settings, where task planning, multi-round cooperation among heterogeneous agents, and memory utilization are indispensable. To address this gap, we propose GraphPlanner, a heterogeneous graph memory-augmented agentic router for multi-agent LLMs that generates routing workflows for each query and supports both inductive and transductive inference. GraphPlanner formulates workflow generation as a Markov Decision Process (MDP), where at each step it selects both the LLM backbone and the agent role, including Planner, Executor, and Summarizer. By leveraging a heterogeneous graph, denoted as GARNet, to capture interaction memories among queries, agents, and responses, GraphPlanner integrates historical memory and workflow memory into richer state representations. The entire pipeline is optimized with reinforcement learning, jointly improving task-specific performance and computational efficiency. We evaluate GraphPlanner across 14 diverse LLM tasks and demonstrate that: (1) GraphPlanner outperforms strong single-round and multi-round routers, improving accuracy by up to 9.3% while reducing GPU cost from 186.26 GiB to 1.04 GiB; (2) GraphPlanner generalizes robustly to unseen tasks and LLMs, exhibiting strong zero-shot capabilities; and (3) GraphPlanner effectively leverages historical memories, supporting both inductive and transductive inference for more adaptive routing. Our code for GraphPlanner is released at this https URL.

---


### 105. [Directional Alignment and Narrative Agency in Human-LLM Co-Writing](https://arxiv.org/abs/2604.23676)

**<font color=#1a73e8>作者：</font>** Halfdan Nordahl Fundal, Yuri Bizzoni  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We investigate narrative agency in human-LLM creative co-writing, asking who drives story development in turn-based collaboration. Using a new corpus of 87 human-LLM co-written stories, we apply sentiment and semantic modeling to quantify affective alignment and semantic novelty in turn-taking, and directional measures to assess which agent shapes narrative progression. Our results show asymmetric influence: human turns introduce greater semantic novelty and are more likely to shape subsequent developments, whereas LLM contributions predominantly elaborate on human-introduced elements. At the sentiment level, alignment is also asymmetric, but more bidirectional: LLMs exhibit stronger turn-level emotional adaptation than humans, but both agents track each other's emotional valence and LLMs show an independent tendency to more positive emotional baselines. These findings indicate a complementary division of labor in human-LLM co-writing, where humans drive narrative innovation and direction, while LLMs act as adaptive amplifiers that sustain coherence and elaborate emerging narratives.

---


### 106. [Benchmarking Testing in Automated Theorem Proving](https://arxiv.org/abs/2604.23698)

**<font color=#1a73e8>作者：</font>** Jongyoon Kim, Hojae Han, Seung-won Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have shown promise in formal theorem proving, yet evaluating semantic correctness remains challenging. Existing evaluations rely on indirect proxies such as lexical overlap with human-annotated proof, or expensive manual inspection. Inspired by the shift from lexical comparison to test-based evaluation in code generation, we propose T , a framework that evaluates the semantic correctness of formal theorems: a generated theorem is considered correct only if all dependent successor theorems compile successfully, analogous to integration testing. We construct a benchmark from 5 real-world Lean 4 repositories, comprising 2,206 problems paired with 41 successor theorems on average, automatically extracted without human effort. Experiments demonstrate that while state-of-the-art models achieve high compilation success, they perform significantly worse under our semantic metric. The best model, Claude-Sonnet-4.5, achieves only 38.9% Testing Accuracy on the full set, given both natural language proof and successor theorems as context, revealing a critical gap in current theorem generation capabilities.

---


### 107. [Agri-CPJ: A Training-Free Explainable Framework for Agricultural Pest Diagnosis Using Caption-Prompt-Judge and LLM-as-a-Judge](https://arxiv.org/abs/2604.23701)

**<font color=#1a73e8>作者：</font>** Wentao Zhang, Qi Zhang, Mingkun Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Crop disease diagnosis from field photographs faces two recurring problems: models that score well on benchmarks frequently hallucinate species names, and when predictions are correct, the reasoning behind them is typically inaccessible to the practitioner. This paper describes Agri-CPJ (Caption-Prompt-Judge), a training-free few-shot framework in which a large vision-language model first generates a structured morphological caption, iteratively refined through multi-dimensional quality gating, before any diagnostic question is answered. Two candidate responses are then generated from complementary viewpoints, and an LLM judge selects the stronger one based on domain-specific criteria. Caption refinement is the component with the largest individual impact: ablations confirm that skipping it consistently degrades downstream accuracy across both models tested. On CDDMBench, pairing GPT-5-Nano with GPT-5-mini-generated captions yields \textbf{+22.7} pp in disease classification and \textbf{+19.5} points in QA score over no-caption baselines. Evaluated without modification on AgMMU-MCQs, GPT-5-Nano reached 77.84\% and Qwen-VL-Chat reached 64.54\%, placing them at or above most open-source models of comparable scale despite the format shift from open-ended to multiple-choice. The structured caption and judge rationale together constitute a readable audit trail: a practitioner who disagrees with a diagnosis can identify the specific caption observation that was incorrect. Code and data are publicly available this https URL

---


### 108. [Talking Slide Avatars: Open-Source Multimodal Communication Approach for Teaching](https://arxiv.org/abs/2604.23703)

**<font color=#1a73e8>作者：</font>** Xinxing Wu  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Slide-based teaching is widely used in higher education, yet in online, hybrid, and asynchronous contexts, slides often lose the instructor presence, narrative continuity, and expressive framing that help learners connect with content. Full lecture video can partly restore these qualities, but it is time-consuming to record, revise, and reuse. This study addresses that pedagogical and production challenge by presenting a practice-based analysis of an open-source workflow for creating talking slide avatars for slide-based teaching. The workflow integrates OpenVoice for text-to-speech generation and voice cloning with Ditto-TalkingHead for audio-driven talking-image synthesis, enabling instructors to transform a script and a static portrait into a short narrated video that can be embedded in slide decks or HTML-based lecture materials. Rather than treating this workflow merely as a technical solution, the study frames talking slide avatars as multimodal communication artifacts at the intersection of digital pedagogy, aesthetic education, and art-technology practice. Using a practice-based implementation and analytic reflection approach, the study documents the production pipeline, examines its communicative and aesthetic affordances, and proposes practical guidelines for script length, image selection, pacing, disclosure, accessibility, and ethical use. The study makes three primary contributions: it presents an educator-oriented open-source production model, reframes talking avatars as an educational communication design problem, and proposes a responsible pathway for incorporating generative synthetic media into teaching. It concludes that short, transparent, and carefully designed avatars can humanize slide-based instruction while providing a reusable communicative layer for introductions, transitions, reminders, and recaps across online, hybrid, and asynchronous learning environments.

---


### 109. [Weakly Supervised Multicenter Nancy Index Scoring in Ulcerative Colitis Using Foundation Models](https://arxiv.org/abs/2604.23706)

**<font color=#1a73e8>作者：</font>** Adam Kukučka, Ondřej Fabián, Vít Musil 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Histologic assessment of ulcerative colitis (UC) activity is an important endpoint in clinical trials and routine care, but manual grading with indices such as the Nancy histological index (NHI) is time-consuming and prone to observer variability. While computational pathology methods can automate scoring, many approaches depend on dense region-level annotations, which are costly to obtain, particularly in heterogeneous, multicenter cohorts.
We propose a weakly supervised multiple instance learning (MIL) approach for whole-slide images that learns from case- and slide-level NHI labels, leveraging foundation models. Our method targets clinically relevant endpoints, including neutrophilic activity and derived Nancy-low/high groupings, enabling full five-grade NHI prediction.
On a multicenter dataset of H&E-stained colon biopsies from three hospitals (2019-2025), we evaluate multiple foundation model encoders and aggregation strategies. We find that foundation model choice and resolution substantially affect performance, with Virchow2 providing the most consistent gains, and that a simple ensembling rule improves five-grade NHI prediction compared to a hierarchical gating baseline.
Overall, our results demonstrate that weakly supervised MIL with modern foundation-model representations can provide robust, interpretable UC histology activity assessment in realistic multicenter settings.

---


### 110. [AIPsy-Affect: A Keyword-Free Clinical Stimulus Battery for Mechanistic Interpretability of Emotion in Language Models](https://arxiv.org/abs/2604.23719)

**<font color=#1a73e8>作者：</font>** Michael Keeman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability research on emotion in large language models -- linear probing, activation patching, sparse autoencoder (SAE) feature analysis, causal ablation, steering vector extraction -- depends on stimuli that contain the words for the emotions they test. When a probe fires on "I am furious", it is unclear whether the model has detected anger or detected the word "furious". The two readings have very different consequences for every downstream claim about emotion circuits, features, and interventions. We release AIPsy-Affect, a 480-item clinical stimulus battery that removes the confound at the stimulus level: 192 keyword-free vignettes evoking each of Plutchik's eight primary emotions through narrative situation alone, 192 matched neutral controls that share characters, setting, length, and surface structure with the affect surgically removed, plus moderate-intensity and discriminant-validity splits. The matched-pair structure supports linear probing, activation patching, SAE feature analysis, causal ablation, and steering vector extraction under a strong methodological guarantee: any internal representation that distinguishes a clinical item from its matched neutral cannot be doing so on the basis of emotion-keyword presence. A three-method NLP defense battery -- bag-of-words sentiment, an emotion-category lexicon, and a contextual transformer classifier -- confirms the property: bag-of-words methods see only situational vocabulary, and a contextual classifier detects affect (p < 10^-15) but cannot identify the category (5.2% top-1 vs. 82.5% on a keyword-rich control). AIPsy-Affect extends our earlier 96-item battery (arXiv:2603.22295) by a factor of four and is released openly under MIT license.

---


### 111. [Expert Evaluation of LLM's Open-Ended Legal Reasoning on the Japanese Bar Exam Writing Task](https://arxiv.org/abs/2604.23730)

**<font color=#1a73e8>作者：</font>** Jungmin Choi, Keisuke Sakaguchi, Hiroaki Yamada  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong performance on legal benchmarks, including multiple-choice components of bar exams. However, their capacity for generating open-ended legal reasoning in realistic scenarios remains insufficiently explored. Notably, to our best knowledge, there are no prior studies or datasets addressing this issue in the Japanese context.
This study presents the first dataset designed to evaluate the open-ended legal reasoning performance of LLMs within the Japanese jurisdiction. The dataset is based on the writing component of the Japanese bar examination, which requires examinees to identify multiple legal issues from long narratives and to construct structured legal arguments in free text format. Our key contribution is the manual evaluation of LLMs' generated responses by legal experts, which reveals limitations and challenges in legal reasoning. Moreover, we conducted a manual analysis of hallucinations to characterize when and how the models introduce content not supported by precedent or law.
Our real exam questions, model-generated responses, and expert evaluations reveal the milestones of current LLMs in the Japanese legal domain. Our dataset and relevant resources will be available online.

---


### 112. [Multimodal QUD: Inquisitive Questions from Scientific Figures](https://arxiv.org/abs/2604.23733)

**<font color=#1a73e8>作者：</font>** Yating Wu, William Rudman, Venkata S Govindarajan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Asking inquisitive questions while reading, and looking for their answers, is an important part in human discourse comprehension, curiosity, and creative ideation, and prior work has investigated this in text-only scenarios. However, in scientific or research papers, many of the critical takeaways are conveyed through both figures and the text that analyzes them. While scientific visualizations have been used to evaluate Vision-Language Models (VLMs) capabilities, current benchmarks are limited to questions that focus simply on extracting information from them. Such questions only require lower-level reasoning, do not take into account the context in which a figure appears, and do not reflect the communicative goals the authors wish to achieve. We generate inquisitive questions that reach the depth of questions humans generate when engaging with scientific papers, conditioned on both the figure and the paper's context, and require reasoning across both modalities. To do so, we extend the linguistic theory of Questions Under Discussion (QUD) from being text-only to multimodal, where implicit questions are raised and resolved as discourse progresses. We present MQUD, a dataset of research papers in which such questions are made explicit and annotated by the original authors. We show that fine-tuning a VLM on MQUD shifts the model from generating generic low-level visual questions to content-specific grounding that requires a high-level of multimodal reasoning, yielding higher-quality, more visually grounded multimodal QUD generation.

---


### 113. [SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning](https://arxiv.org/abs/2604.23747)

**<font color=#1a73e8>作者：</font>** Alexis Limozin, Eduard Durech, Torsten Hoefler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent mixed-policy optimization methods for LLM reasoning that interleave or blend supervised and reinforcement learning signals report improvements over the standard SFT-then-RL pipeline. We show that numerous recently published research papers rely on a faulty baseline caused by two distinct bugs: a CPU-offloaded optimizer bug in DeepSpeed that silently drops intermediate micro-batches during gradient accumulation (affecting multiple downstream frameworks including TRL, OpenRLHF and Llama-Factory), and a loss aggregation bug in OpenRLHF that incorrectly weights per-mini-batch losses. Together they suppress SFT performance, with the optimizer bug accounting for most of the gap and the loss aggregation bug contributing a smaller additional effect. Once corrected, the standard SFT-then-RL pipeline surpasses every published mixed-policy method we evaluate by +3.8 points on math benchmarks with Qwen2.5-Math-7B and by +22.2 points with Llama-3.1-8B. Even a truncated variant with just 50 RL steps outperforms mixed-policy methods on math benchmarks while using fewer FLOPs.

---


### 114. [The Override Gap: A Magnitude Account of Knowledge Conflict Failure in Hypernetwork-Based Instant LLM Adaptation](https://arxiv.org/abs/2604.23750)

**<font color=#1a73e8>作者：</font>** Shuaizhi Cheng, Xiang Shi, Mingwei Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypernetwork-based methods such as Doc-to-LoRA internalize a document into an LLM's weights in a single forward pass, but they fail systematically on conflicts: when the document contradicts pretraining knowledge, accuracy collapses to 46.4% on the deepest facts. We show the failure is a magnitude problem rather than a representational one. The hypernetwork already targets the right layers, but its adapter margin is approximately constant across documents while the pretrained margin grows with training frequency, so deep conflicts lose by construction. The account predicts that failure should track prior strength: sorting 194 conflicts by the base model's log-probability on the contradicted fact, baseline accuracy falls from 68% on weak-prior questions to 16% on strong-prior ones, a 52 percentage-point gap. The cure is amplitude. Selective Layer Boosting scales the adapter at its top-norm layers, and Conflict-Aware Internalization triggers boosting only when the base model is confident. Both are training-free; together they raise deep-conflict accuracy from 46.4% to 71.0% on Gemma-2B and from 53.6% to 72.5% on Mistral-7B while preserving novel-knowledge recall, and beat vanilla retrieval-augmented generation on medium conflicts by 18 percentage points despite operating entirely in parameter space. We release KID-Bench, a 489-question benchmark that separates novel recall, cross-knowledge combination, and prior-graded conflicts.

---


### 115. [Modeling Induced Pleasure through Cognitive Appraisal Prediction via Multimodal Fusion](https://arxiv.org/abs/2604.23753)

**<font color=#1a73e8>作者：</font>** Nastaran Dab, Raziyeh Zall, Mohammadreza Kangavari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal affective computing analyzes user-generated social media content to predict emotional states. However, a critical gap remains in understanding how visual content shapes cognitive interpretations and elicits specific affective experiences such as pleasure. This study introduces a novel computational model to infer video-induced pleasure via cognitive appraisal variables. The proposed model addresses four challenges: (1) noisy and inconsistent human labels, (2) the semantic gap between "positive emotions" and "pleasure," (3) the scarcity of pleasure-specific datasets, and (4) the limited interpretability of existing black-box fusion methods. Our approach integrates data-driven and cognitive theory-driven methods, using cognitive appraisal theory and a fuzzy model within an innovative framework. The model employs transformer-based architectures and attention mechanisms for fine-grained multimodal feature extraction and interpretable fusion to capture both inter- and intra-modal dynamics associated with pleasure. This enables the prediction of underlying appraisal variables, thereby bridging the semantic gap and enhancing model explainability beyond conventional statistical associations. Experimental results validate the efficacy of the proposed method in detecting video-induced pleasure, achieving a peak accuracy of 0.6624 in predicting pleasure levels. These findings highlight promising implications for affective content recommendation, intelligent media creation, and advancing our understanding of how digital media influences human emotions.

---


### 116. [Agentic Fusion of Large Atomic and Language Models to Accelerate Materials Discovery](https://arxiv.org/abs/2604.23758)

**<font color=#1a73e8>作者：</font>** Mingze Li, Yu Rong, Songyou Li 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The discovery of novel materials is critical for global energy and quantum technology transitions. While deep learning has fundamentally reshaped this landscape, existing predictive or generative models typically operate in isolation, lacking the autonomous orchestration required to execute the full discovery process. Here we present ElementsClaw, an agentic framework for materials discovery that synergizes Large Atomic Models (LAMs) with Large Language Models (LLMs). In response to varied human requirements, ElementsClaw dynamically orchestrates a suite of LAM tools finetuned from our proposed model Elements for atomic-scale numerical computation, while leveraging LLMs for high-level semantic reasoning. This shift moves AI-driven materials science from isolated processes toward integrated and human interactive discovery. In the demanding domain of superconductors, our agentic system guides the experimental synthesis of four new superconductors, including Zr3ScRe8 with a transition temperature of 6.8 K and HfZrRe4 at 6.7 K. At scale, ElementsClaw screens more than 2.4 million stable crystals within only 28 GPU hours, identifying 68,000 high-confidence superconducting candidates and vastly expanding the known superconducting space. These results demonstrate how our agent accelerates materials discovery with high physical fidelity.

---


### 117. [WISE-FM:Operation-Aware, Engineering-Informed Foundation Model for Multi-Task Well Design](https://arxiv.org/abs/2604.23767)

**<font color=#1a73e8>作者：</font>** Carine de Menezes Rebello, Anderson Rapello dos Santos, Idelfonso B. R. Nogueira  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deploying machine learning models across diverse well portfolios requires generalisation to wells with design parameters outside the training distribution. Current data-driven approaches to virtual flow metering (VFM) and bottomhole estimation typically treat each well independently or ignore the influence of well design on operational behaviour. We present WISE (Well Intelligence and Systems Engineering Foundation Model), a design-aware, physics-informed multi-task model that integrates three complementary mechanisms: Feature-wise Linear Modulation (FiLM) and cross-modal attention to condition operational embeddings on well design parameters; multi-task learning for simultaneous prediction of flow rates, bottomhole conditions, and flow regime classification; and structural mass conservation with soft physics constraints derived from well engineering principles. Evaluation on the ManyWells benchmark (2000 simulated wells, $10^6$ data points) demonstrates that design-aware models reduce VFM prediction error by up to $13\times$ compared to design-unaware baselines, and that physics constraints reduce negative flow predictions by 65%. Flow regime classification achieves 97.7% bottomhole accuracy, providing continuous well integrity monitoring without additional sensors. The methodology transfers to real operational data from five Equinor Volve producers (oil rate $R^2 = 0.89$, bottomhole pressure $R^2 = 0.98$, water rate $R^2 = 0.97$). The trained model additionally serves as a fast surrogate for integrity-aware well design optimisation over a 24-dimensional design space, with more than $1000\times$ speedup over drift-flux simulations. These results demonstrate that design awareness, physics enforcement, and multi-task learning are essential and complementary ingredients for foundation models intended to operate across large well portfolios.

---


### 118. [PageGuide: Browser extension to assist users in navigating a webpage and locating information](https://arxiv.org/abs/2604.23772)

**<font color=#1a73e8>作者：</font>** Tin Nguyen, Thang T. Truong, Runtao Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Users browsing the web daily struggle to quickly locate relevant information in cluttered pages, complete unfamiliar multi-step tasks, and stay focused amid distracting content. State-of-the-art AI assistants (e.g., ChatGPT, Gemini, Claude) and browser agents (e.g., OpenAI Operator, Browser Use) can answer questions and automate actions, yet they return answers without showing where the information comes from on the page, forcing users to manually verify results and blindly trust every automated steps. We present PageGuide, a browser extension that grounds LLM answers directly in the HTML DOM via visual overlays, addressing three core user needs: (a) Find-locating and highlighting relevant evidence in-situ so users can instantly verify answers on the page; (b) Guide-showing step-by-step instructions (e.g. how to change password) one at a time so users can follow and perform actions by themselves; and (c) Hide-hiding distracting content-giving users a chance to decide to hide an element or not. In a user study (N=94), PageGuide outperform unaided browsing across all modes: Hide accuracy improve by 26 percentage points (86.7% relative gain) and task completion time drops by 70%; Guide completion rate increases by 30 percentage points; and Find reduces manual search effort, with Ctrl+F usage falling by 80% and task time decreasing by 19%. Code and demo is at: this http URL.

---


### 119. [ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents](https://arxiv.org/abs/2604.23781)

**<font color=#1a73e8>作者：</font>** Fanqing Meng, Lingxiao Du, Zijian Wu 等 47 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-model agents are increasingly used as persistent coworkers that assist users across multiple working days. During such workflows, the surrounding environment may change independently of the agent: new emails arrive, calendar entries shift, knowledge-base records are updated, and evidence appears across images, scanned PDFs, audio, video, and spreadsheets. Existing benchmarks do not adequately evaluate this setting because they typically run within a single static episode and remain largely text-centric. We introduce \bench{}, a benchmark for coworker agents built around multi-turn multi-day tasks, a stateful sandboxed service environment whose state evolves between turns, and rule-based verification. The current release contains 100 tasks across 13 professional scenarios, executed against five stateful sandboxed services (filesystem, email, calendar, knowledge base, spreadsheet) and scored by 1537 deterministic Python checkers over post-execution service state; no LLM-as-judge is invoked during scoring. We benchmark seven frontier agent systems. The strongest model reaches 75.8 weighted score, but the best strict Task Success is only 20.0\%, indicating that partial progress is common while complete end-to-end workflow completion remains rare. Turn-level analysis shows that performance drops after the first exogenous environment update, highlighting adaptation to changing state as a key open challenge. We release the benchmark, evaluation harness, and construction pipeline to support reproducible coworker-agent evaluation.

---


### 120. [FAIR_XAI: Improving Multimodal Foundation Model Fairness via Explainability for Wellbeing Assessment](https://arxiv.org/abs/2604.23786)

**<font color=#1a73e8>作者：</font>** Sophie Chiang, Tom Brennan, Fethiye Irmak Dogan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, the integration of multimodal machine learning in wellbeing assessment has offered transformative potential for monitoring mental health. However, with the rapid advancement of Vision-Language Models (VLMs), their deployment in clinical settings has raised concerns due to their lack of transparency and potential for bias. While previous research has explored the intersection of fairness and Explainable AI (XAI), its application to VLMs for wellbeing assessment and depression prediction remains under-explored. This work investigates VLM performance across laboratory (AFAR-BSFT) and naturalistic (E-DAIC) datasets, focusing on diagnostic reliability and demographic fairness. Performance varied substantially across environments and architectures; Phi3.5-Vision achieved 80.4% accuracy on E-DAIC, while Qwen2-VL struggled at 33.9%. Additionally, both models demonstrated a tendency to over-predict depression on AFAR-BSFT. Although bias existed across both architectures, Qwen2-VL showed higher gender disparities, while Phi-3.5-Vision exhibited more racial bias. Our XAI intervention framework yielded mixed results; fairness prompting achieved perfect equal opportunity for Qwen2-VL at a severe accuracy cost on E-DAIC. On AFAR-BSFT, explainability-based interventions improved procedural consistency but did not guarantee outcome fairness, sometimes amplifying racial bias. These results highlight a persistent gap between procedural transparency and equitable outcomes. We analyse these findings and consolidate concrete recommendations for addressing them, emphasising that future fairness interventions must jointly optimise predictive accuracy, demographic parity, and cross-domain generalisation.

---


### 121. [MIRAGE: A Micro-Interaction Relational Architecture for Grounded Exploration in Multi-Figure Artworks](https://arxiv.org/abs/2604.23788)

**<font color=#1a73e8>作者：</font>** Jui-Cheng Chiu, Yu-Chao Wang, Shengyang Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Appreciating multi-figure paintings requires understanding how characters relate through subtle cues like gaze alignment, gesture, and spatial arrangement. We present MIRAGE, an evidence-centric framework designed to scaffold the exploration of these "micro-interactions" in multi-figure artworks. While such cues are essential for deep narrative appreciation, they are often distributed across complex scenes and difficult for viewers to systematically identify. Existing vision-language models (VLMs) frequently fail to provide reliable assistance, offering ungrounded interpretations that lack traceable visual evidence.
MIRAGE addresses this by constructing a structured intermediate representation capturing identities, pose cues, and gaze hypotheses. However, the challenge extends beyond extracting these cues to coordinating them during interpretation. Without an explicit mechanism to organize and reconcile relational evidence, models often collapse multiple interaction hypotheses into a single unstable or weakly grounded narrative, even when low-level signals are available. This representation allows users to verify how high-level interpretations are anchored in low-level visual facts.
By separating spatial grounding from narrative generation, MIRAGE enables users to inspect and reason about figure-to-figure relationships through a verifiable evidence layer. We evaluate MIRAGE against painting-only VLM baselines using a blind assessment protocol. Results show that MIRAGE significantly improves identity consistency, reduces relational hallucinations, and increases the coverage of subtle interactions. These findings suggest that structured grounding can serve as a critical interaction control layer, providing the necessary scaffolding for a more reliable, transparent, and human-led understanding of complex visual narratives.

---


### 122. [Domain Fine-Tuning vs. Retrieval-Augmented Generation for Medical Multiple-Choice Question Answering: A Controlled Comparison at the 4B-Parameter Scale](https://arxiv.org/abs/2604.23801)

**<font color=#1a73e8>作者：</font>** Avi-ad Avraam Buskila  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Practitioners deploying small open-weight large language models (LLMs) for medical question answering face a recurring design choice: invest in a domain-fine-tuned model, or keep a general-purpose model and inject domain knowledge at inference time via retrieval-augmented generation (RAG). We isolate this trade-off by holding model size, prompt template, decoding temperature, retrieval pipeline, and evaluation protocol fixed, and varying only (i) whether the model has been domain-adapted (Gemma 3 4B vs. MedGemma 4B, both 4-bit quantized and served via Ollama) and (ii) whether retrieved passages from a medical knowledge corpus are inserted into the prompt. We evaluate all four cells of this 2x2 design on the full MedQA-USMLE 4-option test split (1,273 questions) with three repetitions per question (15,276 LLM calls). Domain fine-tuning yields a +6.8 percentage-point gain in majority-vote accuracy over the general 4B baseline (53.3% vs. 46.4%, McNemar p < 10^-4). RAG over MedMCQA explanations does not produce a statistically significant gain in either model, and in the domain-tuned model the point estimate is slightly negative (-1.9 pp, p = 0.16). At this scale and on this benchmark, domain knowledge encoded in weights dominates domain knowledge supplied in context. We release the full experiment code and JSONL traces to support replication.

---


### 123. [LegalDrill: Diagnosis-Driven Synthesis for Legal Reasoning in Small Language Models](https://arxiv.org/abs/2604.23809)

**<font color=#1a73e8>作者：</font>** Tianchun Li, Haochen Liu, Vishwa Pardeshi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) are promising for real-world deployment due to their efficiency and low operational cost. However, their limited capacity struggles with high-stakes legal reasoning tasks that require coherent statute interpretation and logically consistent deduction. Furthermore, training SLMs for such tasks demands high-quality, concise reasoning trajectories, which are prohibitively expensive to manually collect and difficult to curate via standard rejection sampling, lacking granularity beyond final verdicts. To address these challenges, we propose {LegalDrill}, a diagnosis-driven synthesis framework that extracts and iteratively refines reasoning trajectories from a capable teacher via fine-grained prompting, then a self-reflective verification is employed to adaptively select the most effective data for the SLM student. The resulting data empower SLM training through supervised fine-tuning and direct preference optimization. Extensive experiments on several legal benchmarks demonstrate that {LegalDrill} significantly bolsters the legal reasoning capabilities of representative SLMs while bypassing the need for scarce expert annotations, paving a scalable path toward practical legal reasoning systems.

---


### 124. [ShredBench: Evaluating the Semantic Reasoning Capabilities of Multimodal LLMs in Document Reconstruction](https://arxiv.org/abs/2604.23813)

**<font color=#1a73e8>作者：</font>** Zichun Guo, Yuling Shi, Wenhao Zeng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have achieved remarkable performance in Visually Rich Document Understanding (VRDU) tasks, but their capabilities are mainly evaluated on pristine, well-structured document images. We consider content restoration from shredded fragments, a challenging VRDU setting that requires integrating visual pattern recognition with semantic reasoning under significant content discontinuities. To facilitate systematic evaluation of complex VRDU tasks, we introduce ShredBench, a benchmark supported by an automated generation pipeline that renders fragmented documents directly from Markdown. The proposed pipeline ensures evaluation validity by allowing the flexible integration of latest or unseen textual sources to prevent training data contamination. ShredBench assesses four scenarios (English, Chinese, Code, Table) with three fragmentation granularities (8, 12, 16 pieces). Empirical evaluations on state-of-the-art MLLMs reveal a significant performance gap: The method is effective on intact documents; however, once the document is shredded, restoration becomes a significant challenge, with NED dropping sharply as fragmentation increases. Our findings highlight that current MLLMs lack the fine-grained cross-modal reasoning required to bridge visual discontinuities, identifying a critical gap in robust VRDU research.

---


### 125. [Resource-Lean Lexicon Induction for German Dialects](https://arxiv.org/abs/2604.23824)

**<font color=#1a73e8>作者：</font>** Robert Litschko, Barbara Plank, Diego Frassinelli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic induction of high-quality dictionaries is essential for building lexical resources, yet low-resource languages and dialects pose several challenges: limited access to annotators, high degree of spelling variations, and poor performance of large language models (LLMs). We empirically show that statistical models (random forests) trained on string similarity features are surprisingly effective for inducing German dialect lexicons. They outperform LLMs, enable cross-dialect transfer, and offer a lightweight data-driven alternative. We evaluate our models intrinsically on bilingual lexicon induction (BLI) and extrinsically on dialect information retrieval (IR). On BLI, random forests outperform Mistral-123b while being more resource-lean. On dialect IR with BM25, using our dialect dictionaries for query expansion yields relative improvements of up to 28.9% in nDCG@10 and 50.7% in Recall@100. Motivated by the resource scarcity in dialects, we further investigate the extent to which models transfer across different German dialects, and their performance under varying amounts of training data.

---


### 126. [One Size Fits None: Heuristic Collapse in LLM Investment Advice](https://arxiv.org/abs/2604.23837)

**<font color=#1a73e8>作者：</font>** Jillian Ross, Andrew W. Lo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed as advisors in high-stakes domains -- answering medical questions, interpreting legal documents, recommending financial products -- where good advice requires integrating a user's full context rather than responding to salient surface features. We investigate whether frontier LLMs actually do this, or whether they instead exhibit heuristic collapse: a systematic reduction of complex, multi-factor decisions to a small number of dominant inputs. We study the phenomenon in investment advice, where legal standards explicitly require individualized reasoning over a client's full circumstances. Applying interpretable surrogate models to LLM outputs, we find systematic heuristic collapse: investment allocation decisions are largely determined by self-reported risk tolerance, while other relevant factors contribute minimally. We further find that web search partially attenuates heuristic collapse but does not resolve it. These findings suggest that heuristic collapse is not resolved by web search augmentation or model scale alone, and that deploying LLMs as advisors requires auditing input sensitivity, not just output quality.

---


### 127. [JigsawRL: Assembling RL Pipelines for Efficient LLM Post-Training](https://arxiv.org/abs/2604.23838)

**<font color=#1a73e8>作者：</font>** Zhengding Hu, Hehua Ouyang, Chang Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present JigsawRL, a cost-efficient framework that explores Pipeline Multiplexing as a new dimension of RL parallelism. JigsawRL decomposes each pipeline into a Sub-Stage Graph that exposes the intra-stage and inter-worker imbalance hidden by stage-level systems. On this abstraction, JigsawRL resolves multiplexing interference through dynamic resource allocation, eliminates fragmented utilization by migrating long-tail rollouts across workers, and formulates their coordination as a graph scheduling problem solved with a look-ahead heuristic. On 4-64 H100/A100 GPUs across different agentic RL pipelines and models, JigsawRL achieves up to 1.85x throughput over Verl on synchronous RL, 1.54x over StreamRL and AReaL on asynchronous RL, and supports heterogeneous pipelines with moderate latency trade-off.

---


### 128. [ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation](https://arxiv.org/abs/2604.23853)

**<font color=#1a73e8>作者：</font>** Boqin Yuan, Renchu Song, Yue Su 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill-distillation pipelines learn reusable rules from LLM agent trajectories, but they lack a key signal: how much each step costs. Without per-step cost, a pipeline cannot distinguish adding a missing step to fix a bug from removing an expensive step that never affected the outcome. We introduce ClawTrace, an agent tracing platform that records every LLM call, tool use, and sub-agent spawn during an agent session and compiles each session into a TraceCard: a compact YAML summary with per-step USD cost, token counts, and redundancy flags. Built on ClawTrace, CostCraft is a distillation pipeline that reads TraceCards and produces three types of skill patches. Preserve patches keep behaviors that led to success. Prune patches remove expensive steps that did not matter, each backed by a counterfactual argument against a named high-cost step. Repair patches fix failures grounded in oracle evidence. Ablations on 30 held-out SpreadsheetBench tasks show that both cost attribution and prune patches independently reduce quality regressions. When the same skill is applied to 30 unrelated SkillsBench tasks, an unexpected asymmetry emerges: prune rules transferred across benchmarks and cut median cost by 32%, while preserve rules, trained on benchmark-specific conventions, caused regressions on new task types. We release ClawTrace and TraceCards as open infrastructure for cost-aware agent research.

---


### 129. [Learning Selective LLM Autonomy from Copilot Feedback in Enterprise Customer Support Workflows](https://arxiv.org/abs/2604.23855)

**<font color=#1a73e8>作者：</font>** Nikita Borovkov, Elisei Rykov, Olga Tsymboi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a deployed system that automates end-to-end customer support workflows inside an enterprise Business Process Management (BPM) platform. The approach is scalable in production and reaches selective automation within two weeks for a new process, leveraging supervision already generated at scale: structured per-case UI interaction traces and low-overhead copilot feedback, where operators either accept a suggestion or provide a correction. A staged deployment pipeline trains a next UI action policy, learns a critic from copilot feedback to calibrate abstention, and executes only high-confidence steps in the background while deferring uncertain decisions to operators and resuming from the updated UI state. This setup lets one operator supervise multiple concurrent sessions and be interrupted only when the system is uncertain. The system operates on a schema-driven view of the BPM interface and includes monitoring and safe fallbacks for production. In production, it automated 45% of sessions and reduced average handling time by 39% without degrading support quality level.

---


### 130. [Exploring Audio Hallucination in Egocentric Video Understanding](https://arxiv.org/abs/2604.23860)

**<font color=#1a73e8>作者：</font>** Ashish Seth, Xinhao Mei, Changsheng Zhao 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric videos provide a distinctive setting in which sound serves as crucial cues to understand user activities and surroundings, particularly when visual information is unstable or occluded due to continuous camera movement. State-of-the-art large audio-visual language models (AV-LLMs) can generate multimodal descriptions. However, we show in this work that they are prone to audio hallucinations, often inferring sounds from visual cues that are visible but not heard. We present a systematic and automatic evaluation framework for analyzing audio hallucinations in egocentric video through a targeted question-answering (Q/A) protocol. We curate a dataset of 300 egocentric videos and design 1,000 sound-focused questions to probe model outputs. To characterize hallucinations, we propose a grounded taxonomy that distinguishes between foreground action sounds from the user activities and background ambient sounds. Our evaluation shows that advanced AV-LLMs, such as Qwen2.5 Omni, exhibit high hallucination rates, achieving only 27.3% and 39.5% accuracy on Q/As related to foreground and background sounds, respectively. With this work, we highlight the need to measure the reliability of multimodal responses, emphasizing that robust evaluation of hallucinations is essential to develop reliable AV-LLMs.

---


### 131. [Inverting Foundation Models of Brain Function with Simulation-Based Inference](https://arxiv.org/abs/2604.23865)

**<font color=#1a73e8>作者：</font>** Niels Bracher, Xavier Intes, Stefan T. Radev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models of brain activity promise a new frontier for in silico neuroscience by emulating neural responses to complex stimuli across tasks and modalities. A natural next step is to ask whether these models can also be used in reverse. Can we recover a stimulus or its properties from synthetic brain activity? We study this question in a proof-of-concept setting using TRIBEv2. We pair the brain emulator with large language models (LLMs) that generate news headlines from linguistic parameters such as valence, arousal, and dominance. We then use simulation-based inference to learn a probabilistic mapping from brain maps to latent stimulus parameters. Our results show that these parameters can be recovered from predicted brain maps, validating the quality of neural encodings. They also show that LLMs can serve as controllable stimulus generators for simulated experiments. Together, these findings provide a step toward decoding and inverse design with foundation brain models.

---


### 132. [Knowledge Vector of Logical Reasoning in Large Language Models](https://arxiv.org/abs/2604.23877)

**<font color=#1a73e8>作者：</font>** Zixuan Wang, Yuanyuan Lei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Logical reasoning serve as a central capability in LLMs and includes three main forms: deductive, inductive, and abductive reasoning. In this work, we study the knowledge representations of these reasoning types in LLMs and analyze the correlations among them. Our analysis shows that each form of logical reasoning can be captured as a reasoning-specific knowledge vector in a linear representation space, yet these vectors are largely independent of each other. Motivated by cognitive science theory that these subforms of logical reasoning interact closely in the human brain, as well as our observation that the reasoning process for one type can benefit from the reasoning chain produced by another, we further propose to refine the knowledge representations of each reasoning type in LLMs to encourage complementarity between them. To this end, we design a complementary subspace-constrained refinement framework, which introduces a complementary loss that enables each reasoning vector to leverage auxiliary knowledge from the others, and a subspace constraint loss that prevents erasure of their unique characteristics. Through steering experiments along reasoning vectors, we find that refined vectors incorporating complementary knowledge yield consistent performance gains. We also conduct a mechanism-interpretability analysis of each reasoning vector, revealing insights into the shared and specific features of different reasoning in LLMs.

---


### 133. [LLM-Augmented Traffic Signal Control with LSTM-Based Traffic State Prediction and Safety-Constrained Decision Support](https://arxiv.org/abs/2604.23902)

**<font color=#1a73e8>作者：</font>** Jiazhao Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traffic signal control is a critical task in intelligent transportation systems, yet conventional fixed-time and rule-based methods often struggle to adapt to dynamic traffic demand and provide limited decision interpretability. This study proposes an LLM-augmented traffic signal control framework that integrates LSTM-based short-term traffic state prediction, predictive phase selection, structured large language model reasoning, and safety-constrained action filtering. The LSTM module forecasts future queue length, waiting time, vehicle count, and lane occupancy based on recent intersection-level observations. A predictive controller then generates candidate signal actions, while the LLM module evaluates these actions using structured traffic-state inputs and produces congestion diagnoses, phase adjustment recommendations, and natural-language explanations. To ensure operational reliability, all LLM-generated recommendations are validated by a safety filter before execution. Simulation-based experiments in SUMO compare the proposed method with fixed-time control, rule-based control, and an LSTM-based predictive baseline under balanced demand, directional peak demand, and sudden surge scenarios. The results indicate that the proposed framework improves traffic efficiency, especially under dynamic and non-recurrent traffic conditions, while maintaining zero constraint violations after safety filtering. Overall, this study demonstrates that LLMs can enhance traffic signal control when used as constrained reasoning and decision-support modules rather than direct low-level controllers. Keywords: Intelligent Transportation Systems; Traffic Signal Control; Large Language Models; LSTM; Traffic State Prediction; Decision Support; Safety-Constrained Control; SUMO Simulation.

---


### 134. [Agentic AI platforms for autonomous training and rule induction of human-human and virus-human protein-protein interactions](https://arxiv.org/abs/2604.23924)

**<font color=#1a73e8>作者：</font>** Hung N. Do, Jessica Z. Kubicek-Sutherland, Oscar A. Negrete 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We instruct an AI agent to construct two separate agentic AI platforms: one for autonomous training of predictive ML models for human-human and virus-human PPI, and the other for inducing explicit general rules governing human-human and virus-human PPI. The first agentic AI platform for autonomous training of predictive ML models for PPI is designed to consist of five AI agents that handle autonomous data collection, data verification, feature embedding, model design, and training and validation on three-way protein-disjoint cross-fold datasets. For human-human and human-virus PPIs, the final three-way protein-disjoint ensemble achieves an accuracy of 87.3% and 86.5%, respectively. For cross-checking and interpretability purposes, the second agentic AI platform is designed to replace ML predictions with human-readable rules derived from protein embeddings, physicochemical autocovariance descriptors, compartment annotations, pathway-domain overlap, and graph contexts. For human-human PPI, it is defined by a two-rule induction, whereas human-virus is induced by a more complex set of weighted rules. The rules induced by the second agentic platform align with the SHAP-identified features from the predictive ML models built by the first agentic platform. Taken together, our work demonstrates the agentic AI's ability to orchestrate from data planning to execution, and from rule induction to explanation in ML, opening the door to various applications.

---


### 135. [TSAssistant: A Human-in-the-Loop Agentic Framework for Automated Target Safety Assessment](https://arxiv.org/abs/2604.23938)

**<font color=#1a73e8>作者：</font>** Xiaochen Zheng, Zhiwen Jiang, Melanie Guerard 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Target Safety Assessment (TSA) requires systematic integration of heterogeneous evidence, including genetic, transcriptomic, target homology, pharmacological, and clinical data, to evaluate potential safety liabilities of therapeutic targets. This process is inherently iterative and expert-driven, posing challenges in scalability and reproducibility. We present TSAssistant, a multi-agent framework designed to support TSA report drafting through a modular, section-based, and human-in-the-loop paradigm. The framework decomposes report generation into a coordinated pipeline of specialised subagents, each targeting a single TSA section. Specialised subagents retrieve structured and unstructured data as well as literature evidence from curated biomedical sources through standardised tool interfaces, producing individually citable, evidence-grounded sections. Agent behaviour is governed by a hierarchical instruction architecture comprising system prompts, domain-specific skill modules, and runtime user instructions. A key feature is an interactive refinement loop in which users may manually edit sections, append new information, upload additional sources, or re-invoke agents to revise specific sections, with the system maintaining conversational memory across iterations. TSAssistant is designed to reduce the mechanical burden of evidence synthesis and report drafting, supporting a hybrid model in which agentic AI augments evidence synthesis while toxicologists retain final decision authority.

---


### 136. [What Did They Mean? How LLMs Resolve Ambiguous Social Situations across Perspectives and Roles](https://arxiv.org/abs/2604.23942)

**<font color=#1a73e8>作者：</font>** Qiming Yuan, Linyi Han, Nam Ling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People increasingly turn to large language models (LLMs) to interpret ambiguous social situations: a delayed text reply, an unusually cold supervisor, a teacher's mixed signals, or a boundary-crossing friend. Yet in many such cases, no stable interpretation can be verified from the available evidence alone. We study how LLMs respond to these situations across four domains: early-stage romantic relationships, teacher--student dynamics, workplace hierarchies, and ambiguous friendships. Across 72 responses from GPT, Claude, and Gemini, only 9 (12.5\%) genuinely preserved uncertainty. The remaining 87.5% produced interpretive closure through recurring pathways including narrative alignment, narrative reversal, normative advice under uncertainty, and hedged language that still supported a single conclusion. We further find that narrator perspective shapes the path to closure: first-person accounts more often elicited alignment, while third-person accounts invited more detached interpretation, even when the underlying situation remained comparable. Together, these findings show that LLMs do not simply assist interpersonal sensemaking; they tend to resolve ambiguity into coherent and actionable narratives. These results suggest that the central risk is not only that LLMs may misinterpret social situations, but that they may make unresolved situations feel prematurely settled. We frame this tendency as a design challenge for uncertainty-preserving social AI.

---


### 137. [Context-Aware Hospitalization Forecasting Evaluations for Decision Support using LLMs](https://arxiv.org/abs/2604.23949)

**<font color=#1a73e8>作者：</font>** Rhea Makkuni, Ananya Joshi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical and public health experts must make real-time resource decisions, such as expanding hospital bed capacity, based on projected hospitalization trends during large-scale healthcare disruptions (e.g., operational failures or pandemics). Forecasting models can assist in this task by analyzing large volumes of resource-related data at the facility level, but they must be reliable for decision-making under real-world data conditions. Recent work shows that large language models (LLMs) can incorporate richer forms of context into numerical forecasting. Whereas traditional models rely primarily on temporal context (i.e., past observations), LLMs can also leverage non-temporal public health context such as demographic, geographic, and population-level features. However, it remains unclear how these models should be used to produce stable or decision-relevant predictions in real-world healthcare settings. To evaluate how LLMs can be effectively used in this setting, we evaluate three approaches across 60 counties with low-,mid-, and high-hospitalization intensities in the United States: direct LLM-based forecasting, classical time-series models, and a context-augmented hybrid pipeline (HybridARX) that incorporates LLM-derived signals into structured models. Because the goal is operational decision-making rather than error minimization alone, we evaluate performance with bias and lead-lag alignment in addition to standard forecasting metrics. Our results show that HybridARX improves over classical ARX by yielding more stable and better-calibrated forecasts, particularly when incorporating noisy contextual signals into structured time-series models. These findings suggest that, in non-stationary healthcare resource forecasting, LLMs are most useful when embedded within structured hybrid models.

---


### 138. [LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models](https://arxiv.org/abs/2604.23950)

**<font color=#1a73e8>作者：</font>** Rinyoichi Takezoe, Yaqian Li, Zihao Bo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have recently demonstrated remarkable capabilities in visual understanding and reasoning, but they also impose significant computational burdens due to long visual sequence inputs. Recent works address this issue by pruning unimportant visual tokens, achieving substantial computational reduction while maintaining model performance. The core of token pruning lies in determining token importance, with current approaches primarily relying on attention scores from vision encoders or Large Language Models (LLMs). In this paper, we analyze the effectiveness of attention mechanisms in both vision encoders and LLMs. We find that vision encoders suffer from attention sink, leading to poor focus on informative foreground regions, while in LLMs, although prior studies have identified attention bias toward token positions, text-to-vision attention demonstrates resistance to this bias and enables effective pruning guidance in middle layers. Based on these observations, we propose LearnPruner, a two-stage token pruning framework that first removes redundant vision tokens via a learnable pruning module after the vision encoder, then retains only task-relevant tokens in the LLM's middle layer. Experimental results show that our LearnPruner can preserve approximately 95% of the original performance while using only 5.5% of vision tokens, and achieve 3.2$\times$ inference acceleration, demonstrating a superior accuracy-efficiency trade-off.

---


### 139. [LLM-Guided Agentic Floor Plan Parsing for Accessible Indoor Navigation of Blind and Low-Vision People](https://arxiv.org/abs/2604.23970)

**<font color=#1a73e8>作者：</font>** Aydin Ayanzadeh, Tim Oates  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Indoor navigation remains a critical accessibility challenge for the blind and low-vision (BLV) individuals, as existing solutions rely on costly per-building infrastructure. We present an agentic framework that converts a single floor plan image into a structured, retrievable knowledge base to generate safe, accessible navigation instructions with lightweight infrastructure. The system has two phases: a multi-agent module that parses the floor plan into a spatial knowledge graph through a self-correcting pipeline with iterative retry loops and corrective feedback; and a Path Planner that generates accessible navigation instructions, with a Safety Evaluator agent assessing potential hazards along each route. We evaluate the system on the real-world UMBC Math and Psychology building (floors MP-1 and MP-3) and on the CVC-FP benchmark. On MP-1, we achieve success rates of 92.31%, 76.92%, and 61.54% for short, medium, and long routes, outperforming the strongest single-call baseline (Claude 3.7 Sonnet) at 84.62%, 69.23%, and 53.85%. On MP-3, we reach 76.92%, 61.54%, and 38.46%, compared to the best baseline at 61.54%, 46.15%, and 23.08%. These results show consistent gains over single-call LLM baselines and demonstrate that our workflow is a scalable solution for accessible indoor navigation for BLV individuals.

---


### 140. [Making Sense of Scams: Understanding Scam Conversations Through Multi-Level Alignment](https://arxiv.org/abs/2604.23973)

**<font color=#1a73e8>作者：</font>** Zhenyu Mao, Jacky Keung, Xiangyu Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Online scams often unfold gradually through interaction, yet existing detection systems predominantly rely on snapshot-based signals and interruptive warnings, revealing two research gaps in the lack of signals that represent scam risk within conversational dynamics and the underexplored design of non-interruptive interaction. To address these gaps, we introduce multi-level alignment-based hints, informed by the Interactive Alignment Model, as a new detection signal for supporting sensemaking in scam-related conversations. These hints operationalize low-level lexical and syntactic alignments and high-level semantic and situation-model alignments between conversational participants, making conversational dynamics visible to users. We first conduct a preliminary evaluation on real-life scam dialogues, showing that as conversations approach scam attempts, low-level alignment scores remain stable while high-level alignment scores systematically decline, revealing a consistent cross-level pattern indicative of scam progression. Building on this insight, we conduct a user study with thirty participants, indicating that relative to the no-hint baseline, multi-level alignment-based hints increase precision by 0.25, recall by 0.16, and F1 score by 0.21, yielding substantially larger gains than the marginal improvements achieved by keyword-triggered alerts. Statistical analyses reveal that the proposed hints support earlier and more stable confidence formation over time, with ablation results further highlighting the effectiveness of combining alignment hints across levels in achieving these advantages.

---


### 141. [Multi-View Synergistic Learning with Vision-Language Adaption for Low-Resource Biomedical Image Classification](https://arxiv.org/abs/2604.23977)

**<font color=#1a73e8>作者：</font>** Xiaoliu Luo, Minxue Xiao, Ting Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate biomedical image classification under low-resource conditions remains challenging due to limited annotations, subtle inter-class visual differences, and complex disease semantics. While vision--language models offer a promising foundation for mitigating data scarcity, their effective adaptation in biomedical settings is constrained by the need for parameter-efficient tuning alongside fine-grained and semantically consistent representation learning. In this work, we propose Multi-View Synergistic Learning (MVSL), a unified framework that addresses these challenges by jointly considering adaptation paradigms, representation granularity, and disease semantic relationships. MVSL decouples the adaptation of visual and textual encoders to respect their distinct representational characteristics, enabling more stable and effective parameter-efficient fine-tuning. It further introduces multi-granularity contrastive learning to explicitly model both global image semantics and localized lesion-level evidence, improving fine-grained discrimination for visually similar disease categories. In addition, MVSL preserves disease-level semantic structure by incorporating structured supervision derived from large language models, which constrains textual representations at the class level and indirectly regularizes visual embeddings through cross-modal alignment. Together, these components enable more stable cross-modal alignment and improved discrimination under limited supervision. Extensive experiments on $11$ public biomedical datasets spanning $9$ imaging modalities and $10$ anatomical regions demonstrate that MVSL consistently outperforms state-of-the-art methods in few-shot and zero-shot classification settings.

---


### 142. [Hierarchical Prototype-based Domain Priors for Multiple Instance Learning in Multimodal Histopathology Analysis](https://arxiv.org/abs/2604.23982)

**<font color=#1a73e8>作者：</font>** Xuemei Qiu, Dawei Fan, Yebin Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital pathology has fundamentally altered diagnostic workflows by enabling the computational analysis of gigapixel Whole Slide Images (WSIs), yet effectively deciphering their complex tumor microenvironments remains a formidable challenge. Existing Multiple Instance Learning (MIL) frameworks typically treat Whole Slide Images as unstructured bags of patches, discarding critical morphological semantics and spatial geometry. This lack of inductive bias often leads to overfitting on background noise and fails to align visual features with high-level diagnostic knowledge. To overcome these limitations, we propose the Hierarchical Prototype-based Domain Priors (HPDP) framework, a unified multimodal approach for joint histopathology diagnosis and prognosis. HPDP mitigates the data-driven "black box" issue by introducing a Morphologically Anchored Prototype System (MAPS), which anchors learning to interpretable morphological clusters, and a Sinusoidal Positional Encoder (SPE) to explicitly model tissue architecture. Furthermore, we bridge the semantic gap via a Hierarchical Cross-Modal Alignment (HCMA) module, using Large Language Model (LLM)-generated descriptions to contextually refine visual representations. Extensive experiments across seven cancer cohorts demonstrate that HPDP consistently achieves state-of-the-art performance with superior robustness and interpretability.

---


### 143. [Representational Curvature Modulates Behavioral Uncertainty in Large Language Models](https://arxiv.org/abs/2604.23985)

**<font color=#1a73e8>作者：</font>** Jack King, Evelina Fedorenko, Eghbal A. Hosseini  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In autoregressive large language models (LLMs), temporal straightening offers an account of how the next-token prediction objective shapes representations. Models learn to progressively straighten the representational trajectory of input sequences across layers, potentially facilitating next-token prediction via linear extrapolation. However, a direct link between this trajectory and token-level behavior has been missing. We provide such a link by relating contextual curvature-a geometric measure of how sharply the representational trajectory bends over recent context-to next-token entropy. Across two models (GPT-2 XL and Pythia-2.8B), contextual curvature is correlated with entropy, and this relationship emerges during training. Perturbation experiments reveal selective dependence: manipulating curvature through trajectory-aligned interventions reliably modulates entropy, while geometrically misaligned perturbations have no effect. Finally, regularizing representations to be straighter during training modestly reduces token-level entropy without degrading validation loss. These results identify trajectory curvature as a task-aligned representational feature that influences behavioral uncertainty in LLMs.

---


### 144. [Continual Calibration: Coverage Can Collapse Before Accuracy in Lifelong LLM Fine-Tuning](https://arxiv.org/abs/2604.23987)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning for large language models is typically evaluated through accuracy retention under sequential fine-tuning. We argue that this perspective is incomplete, because uncertainty reliability can degrade earlier and more sharply than top-1 performance. We study this empirically by measuring conformal coverage and calibration error on sequentially fine-tuned models across three model families and eight task sequences drawn primarily from classification and multiple-choice benchmarks. Across the classification-style settings we study, coverage loss exceeds accuracy loss by a factor of roughly \(3.4\times \pm 0.5\times\) on average across seeds; in the most pronounced case, coverage drops from \(0.92\) to \(0.61\), while accuracy remains within three points of baseline. Standard continual-learning methods that preserve accuracy do not automatically preserve coverage, and naive calibration baselines recover only part of the gap. We propose calibration replay, a lightweight post-hoc procedure that maintains a task-specific held-out buffer and refits a task-specific conformal threshold under the current model after each update. It adds no training-time gradient cost, uses less than one percent of the memory of ordinary experience replay, and typically restores coverage to within two points of nominal at buffer size \(m = 200\). We accompany the empirical study with a drift decomposition, a finite-sample recovery theorem showing exact conformal validity under exchangeability, and a mixture-validity proposition explaining why pooled thresholds do not suffice. Our guarantees are stated for classification-style tasks with task-specific buffers; extensions to open-ended generation are exploratory.

---


### 145. [When to Commit? Towards Variable-Size Self-Contained Blocks for Discrete Diffusion Language Models](https://arxiv.org/abs/2604.23994)

**<font color=#1a73e8>作者：</font>** Danny Wang, Ruihong Qiu, Zi Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models (dLLMs) enable parallel token updates with bidirectional attention, yet practical generation typically adopts blockwise semi-autoregressive decoding. This switch creates a training-inference mismatch: training denoises with full-sequence context, while inference commits tokens within a bounded block without future context. Therefore, decoding with fixed-size or heuristic-based blocks can lead to premature token commitments, as decisions are made without full access to future context that could alter those choices. Motivated by this, we propose self-containedness as a principled criterion for block commitment. A block is self-contained if its predictions remain consistent with Future-Aware (FA) or without No-Future (NF) access to future context, reframing block boundary selection as a test of self-containedness rather than a heuristic choice. Based on this principle, we introduce Variable-size Self-contained Blocks (VSB) for dLLMs. VSB scores and selects block boundaries using the divergence between token-level predictive distributions under NF and FA conditioning, which quantifies how predictions would change if future context were revealed. We provide theoretical justification linking self-containedness to predictive consistency, and extensive experiments validate VSB's efficacy over fixed-size and heuristic blockwise decoding.

---


### 146. [SMoES: Soft Modality-Guided Expert Specialization in MoE-VLMs](https://arxiv.org/abs/2604.23996)

**<font color=#1a73e8>作者：</font>** Zi-Hao Bo, Yaqian Li, Anzhou Hou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) has become a prevalent backbone for large vision-language models (VLMs), yet how modality-specific signals should guide expert routing remains under-explored. Existing routing strategies are either hand-crafted or modality-agnostic, relying on idealized priors that ignore the layer-dependent modality fusion patterns in MoE-VLMs and provide little guidance for expert specialization. We propose Soft Modality-guided Expert Specialization (SMoES), which consists of dynamic soft modality scores that capture layer-dependent fusion patterns, an expert binning mechanism aligned with expert-parallel deployment, and an inter-bin mutual information regularization that encourages coherent modality specialization. Our method leverages attention-based or Gaussian-statistics modality scores to optimize mutual information regularization. Experiments across four MoE-based VLMs and 16 benchmarks demonstrate improvement on both effectiveness and efficiency: 0.9% and 4.2% average gain on multimodal and language-only tasks, 56.1% reduction in EP communication overhead, and 12.3% throughput improvement under realistic deployment. These results validate that aligning routing with modality-aware expert specialization unlocks MoE-VLM capacity and efficiency.

---


### 147. [IntentVLM: Open-Vocabulary Intention Recognition through Forward-Inverse Modeling with Video-Language Models](https://arxiv.org/abs/2604.24002)

**<font color=#1a73e8>作者：</font>** Hamed Rahimi, Clemence Grislain, Adrien Jacquet Cretides 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Improving the effectiveness of human-robot interaction requires social robots to accurately infer human goals through robust intention understanding. This challenge is particularly critical in multimodal settings, where agents must integrate heterogeneous signals including text, visual cues to form a coherent interpretation of user intent. This paper presents IntentVLM, a novel two-stage video-language framework designed for open-vocabulary human intention recognition. The approach is inspired by forward-inverse modeling in cognitive science by decomposing intention understanding into goal candidate generation followed by structured inference through selection, effectively reducing hallucinations in latent reasoning. Evaluated on the IntentQA and Inst-IT Bench datasets, IntentVLM achieves state-of-the-art results with up to 80% accuracy, notably surpassing the baseline performance by 30% and matches human performance. Our findings demonstrate that this structured reasoning approach enhances open-vocabulary intention understanding without catastrophic forgetting, offering a robust foundation for human-centered robotics.

---


### 148. [Stabilizing Efficient Reasoning with Step-Level Advantage Selection](https://arxiv.org/abs/2604.24003)

**<font color=#1a73e8>作者：</font>** Han Wang, Xiaodong Yu, Jialian Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong reasoning performance by allocating substantial computation at inference time, often generating long and verbose reasoning traces. While recent work on efficient reasoning reduces this overhead through length-based rewards or pruning, many approaches are post-trained under a much shorter context window than base-model training, a factor whose effect has not been systematically isolated. We first show that short-context post-training alone, using standard GRPO without any length-aware objective, already induces substantial reasoning compression-but at the cost of increasingly unstable training dynamics and accuracy degradation. To address this, we propose Step-level Advantage Selection (SAS), which operates at the reasoning-step level and assigns a zero advantage to low-confidence steps in correct rollouts and to high-confidence steps in verifier-failed rollouts, where failures often arise from truncation or verifier issues rather than incorrect reasoning. Across diverse mathematical and general reasoning benchmarks, SAS improves average Pass@1 accuracy by 0.86 points over the strongest length-aware baseline while reducing average reasoning length by 16.3%, yielding a better accuracy-efficiency trade-off.

---


### 149. [Coverage-Based Calibration for Post-Training Quantization via Weighted Set Cover over Outlier Channels](https://arxiv.org/abs/2604.24008)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Sanjeda Akter, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-Training Quantization (PTQ) compresses large language models to low bit-widths using a small calibration set, and its quality depends strongly on which samples are chosen. We identify a failure mode in which calibration samples fail to activate outlier channels, hidden dimensions with unusually large activations, causing the quantizer to underestimate their dynamic range and producing per-channel reconstruction errors that dominate layer-wise loss. Motivated by this observation, we argue that PTQ calibration quality is governed more by weighted outlier-channel coverage than by generic sample representativeness, and formulate calibration selection as a weighted set cover problem over outlier channels. The objective is monotone submodular, and the greedy algorithm, COVERCAL, operates on pre-computed activation statistics and requires no GPU time at selection. We further show that the weight choice is internally consistent: under a stylized clipping model, missed weighted coverage upper-bounds surrogate loss, justifying the weighted coverage objective as principled rather than purely empirical. Across LLaMA-2, LLaMA-3, and Mistral, under AWQ and GPTQ backends and five downstream evaluations, COVERCAL improves over random, max-perplexity, max-activation-variance, and stratified baselines, with the largest gains at small calibration budgets. At INT4 with 128 samples, COVERCAL improves MMLU by 1.2 to 1.5 points over random calibration and reduces perplexity degradation by 15 to 30\%; with 64 samples, it matches or exceeds random calibration at 256. The contribution is not a new PTQ backend but a formulation of calibration selection as weighted outlier coverage, with a simple, efficient algorithm and a surrogate-based justification.

---


### 150. [FlashOverlap: Minimizing Tail Latency in Communication Overlap for Distributed LLM Training](https://arxiv.org/abs/2604.24013)

**<font color=#1a73e8>作者：</font>** Rezaul Karim, Austin Wen, Wang Zongzuo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid growth in the size of large language models has necessitated the partitioning of computational workloads across accelerators such as GPUs, TPUs, and NPUs. However, these parallelization strategies incur substantial data communication overhead significantly hindering computational efficiency. While communication-computation overlap presents a promising direction, existing data slicing based solutions suffer from tail latency. To overcome this limitation, this research introduces a novel communication-computation overlap technique to eliminate this tail latency in state of the art overlap methods for distributed LLM training. The aim of this technique is to effectively mitigate communication bottleneck of tensor parallelism and data parallelism for distributed training and inference. In particular, we propose a novel method termed Flash-Overlap that replaces conventional collective operations of reduce-scatter and all-gather with decomposed peer-to-peer (P2P) communication and schedules partitioned computations to enable fine-grained overlap. Our method provides an exact algorithm for reducing communication overhead that eliminates tail latency. Moreover, it presents a versatile solution compatible with data-parallel training and various tensor-level parallelism strategies, including TPSP and UP. Experimental evaluations demonstrate that our technique consistently achieves lower latency, superior Model FLOPS Utilization (MFU), and high throughput.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-215](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
