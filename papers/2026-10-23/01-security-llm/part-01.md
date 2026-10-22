# 🔐 大模型安全相关研究 | 2026年10月23日

> 本类共 **5** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise](https://arxiv.org/abs/2610.28810)

**<font color=#1a73e8>作者：</font>** Pedro H. Barcha Correia, Matheus Azevedo de Sá, Paulo H. Gomes de Senna 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The widespread adoption of generative artificial intelligence in recent years has brought a parallel rise in prompt injection and jailbreak attacks. By embedding malicious instructions, these exploits manipulate language models to bypass intended behavior and operational boundaries. In traditional chatbots, such attacks are confined to a single session because state memory is not preserved across conversations. However, persistent memory features in modern conversational interfaces enable cross-session attack propagation, establishing a threat vector known as memory injection. This work explores this emerging vulnerability in leading LLM-as-a-service platforms, highlighting its real-world severity and the need for countermeasures. While existing literature focuses on violations tailored to specific platform features, we present a general threat model. We demonstrate that all NIST attack goals are collectively achievable across ChatGPT Instant 5.3, Claude Sonnet 4.6, and Gemini 3 Flash under this model. We also show that memory injections can exploit multiple attack vectors, including personal memories, projects, skills, organization instructions, and Model Context Protocol (MCP)-connected resources. Our findings reveal that all evaluated services can be manipulated to persistently spread disinformation, generate harmful content, or simulate offline unresponsiveness, even in fresh sessions. In the particular case of Claude, shared-memory features allow an attacker to compromise multiple users within an organization and also exfiltrate user prompts. To address these vulnerabilities, we derive defense mechanisms from our proposed threat model and foundational cybersecurity principles. Our analysis indicates that nearly half of these mitigations remain unimplemented across the target services. Datasets and attack artifacts are available at this https URL.

---


### 2. [Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning](https://arxiv.org/abs/2610.28966)

**<font color=#1a73e8>作者：</font>** Yuqi Jia, Hangsheng Zhang, Chenxi Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly deployed in multi-agent systems (MAS) to accomplish complex tasks. Prior black-box red-teaming attacks mainly focus on single agents, but we find that these methods are far less effective in MAS, where multiple sub-agents may not directly interact with the user. Therefore, we introduce ReMAS, the first reinforcement learning-based red-teaming framework tailored to MASs, which fine-tunes attacker LLMs to generate effective adversarial prompts for system prompt extraction. The framework follows a two-step process: first, a rewrite stage refines base attack prompts to increase extraction success, and second, a template generation stage constructs attack templates that improve the likelihood of invoking specific sub-agents and thus revealing their system prompts. Extensive experiments show that our method substantially improves attack success rates compared to existing black-box attacks, with transferability across different backend LLMs and MAS structures. These results underscore the vulnerabilities of multi-agent systems and the importance of developing stronger defenses against adaptive black-box adversaries.

---


### 3. [Attention-based Classification for Indirect Prompt Injection](https://arxiv.org/abs/2610.28988)

**<font color=#1a73e8>作者：</font>** Amelia Kawasaki, Stefan Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Indirect prompt injection (IPI) attacks, in which adversarial instructions are embedded in external data processed by a language model, pose a significant threat to the integrity of deployed LLM agents. Attention Tracker (Hung et al., 2025) is a recently proposed white-box detection method that identifies prompt injection attacks by monitoring how a model's attention is distributed between user task tokens and data tokens, claiming dataset-agnostic detection via a scalar focus score threshold. In this paper, we provide the first evaluation of Attention Tracker in a realistic agentic IPI setting using the AgentDojo benchmark, finding that the dataset agnosticism claim does not hold. We find that in agentic environments, long structured tool outputs subvert the fundamental assumptions Attention Tracker makes about attention that the method depends on and produces near-chance detection on AgentDojo across most model families. We propose AttnDA, an extension replacing the scalar threshold with a Fisher Linear Discriminant Analysis classifier over the per-head focus score vector, and evaluate both methods in a cross-dataset setting spanning four benchmarks. AttnDA improves detection performance across agentic and tool-integrated benchmarks, though transfer to AgentDojo remains challenging regardless of classifier choice. A covariance ablation further shows that removing inter-head correlation structure substantially contributes to performance, with complex covariance assumptions causing significant degradation on cross-domain data. These results indicate that the attentional distraction signal underlying focus-score-based detection does not transfer reliably to agentic environments, and that learned linear classifiers over head-level attention features offer improved detection performance, provided training data from the target deployment domain is available.

---


### 4. [Beyond Binary Labels: Diagnostic Evaluation of LLM Safety with Prompt-Level Rubrics](https://arxiv.org/abs/2610.29225)

**<font color=#1a73e8>作者：</font>** Hongyu Li, Xinlong Huang, Zhan Yu 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current LLM safety benchmarks predominantly rely on binary safe or unsafe labels, lacking explanatory depth and suffering from low consistency across automated judges. To address this, we introduce DiagSafe, a diagnostic evaluation framework that moves beyond binary classification by employing prompt-level rubrics. Grounded in globally applicable AI safety policies, each rubric provides explicit criteria along two dimensions: safety, which targets concrete harms with specific exemptions to suppress false positives, and usefulness, which independently evaluates instruction fulfillment. To ensure a robust and realistic evaluation, we construct a bilingual (English-Chinese) benchmark grounded in a comprehensive 84-label safety taxonomy, consisting of two subsets: DiagBase, which covers single- and multi-turn prompts with direct harmful queries and template-based jailbreaks, and DiagAttack, which embeds harmful intents into complex instruction-following tasks to form challenging instruction attacks. Extensive experiments demonstrate that DiagSafe significantly enhances the reliability of LLM-as-a-judge evaluation, achieving 95.34% agreement with human annotations -- substantially higher than the 69%-87% achieved by the baselines -- and high inter-judge consistency (Cohen's $\kappa$ = 0.864). Furthermore, applying our framework reveals that leading LLMs differ markedly in their unsafe rates, and each model also exhibits unique vulnerabilities along different dimensions. In addition, we observe that models are particularly susceptible in Chinese and multi-turn contexts. Ultimately, DiagSafe provides a reliable and explainable tool for auditing and optimizing LLM alignment.

---


### 5. [Prompt Injection Through Forensic Evidence: A Taxonomy and Proof of Concept of Anti-Forensic Attacks on LLM-Assisted Digital Investigations](https://arxiv.org/abs/2610.29747)

**<font color=#1a73e8>作者：</font>** Frank Breitinger, Jan Gruber, Christopher Hargreaves 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are entering digital forensics as examination assistants and autonomous agents. Digital forensics inverts the usual setting for indirect prompt injection: the evidence under analysis is attacker-controlled by definition, and the examiner is obliged to read it closely. This makes the reasoning layer a new anti-forensic target, next to the classical ones of data and tools. Classical anti-forensic taxonomies do not cover it, and prompt injection defences do not anticipate it. We extend the anti-forensic model to reflect the manipulation of reasoning, and present a taxonomy of attacks carried through adversarial evidence: an attacker selects an objective, a technique, a payload location, and a concealment method. We observe a perception gap, i.e., the fact that deterministic tools, the human examiner, and the model perceive the same evidence differently, which is what lets an injection reach the model unseen by the examiner. We demonstrate three attacks against an LLM-assisted analysis pipeline, changing a reported conclusion, writing attacker-chosen content to the analyst's workstation, and causing outbound network traffic, each driven only by text planted on the seized device. Mitigations to these attacks are also proposed.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
